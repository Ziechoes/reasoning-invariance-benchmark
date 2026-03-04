import argparse
import json
import os
import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

PUZZLE_FILE_RE = re.compile(r"^(?P<id>\d{4})-.*\.md$")

SECTION_RE = re.compile(r"^##\s+(?P<title>.+?)\s*$", re.MULTILINE)

EXPECTED_FINAL_RE = re.compile(r"FINAL:\s*(?P<ans>[A-Za-z0-9_\-]+)")

# Variants we attempt to extract as prompts, in priority order.
# If a file doesn't have these headings, we'll fall back to "## Problem" only.
VARIANT_TITLES = [
    "Problem",
    "Variant B",
    "Variant C",
    "Variant D",
]

@dataclass
class PromptVariant:
    puzzle_id: str
    variant: str   # A/B/C...
    title: str
    prompt: str
    expected: Optional[str]

def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def split_sections(md: str) -> Dict[str, str]:
    """
    Returns mapping: section_title -> section_body (text until next '## ' heading).
    """
    matches = list(SECTION_RE.finditer(md))
    out: Dict[str, str] = {}
    for i, m in enumerate(matches):
        title = m.group("title").strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md)
        body = md[start:end].strip()
        out[title] = body
    return out

def normalize_prompt(text: str) -> str:
    # Keep it deterministic: trim, collapse excessive blank lines
    text = text.strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text

def extract_expected(md: str) -> Optional[str]:
    # Find the last FINAL: ... occurrence (often in expected section)
    finals = list(EXPECTED_FINAL_RE.finditer(md))
    if not finals:
        return None
    return finals[-1].group("ans").strip()

def build_variants(puzzle_id: str, md: str) -> List[PromptVariant]:
    sections = split_sections(md)
    expected = extract_expected(md)

    variants: List[PromptVariant] = []
    variant_letter = "A"

    # Try to pull "Problem" and any variants.
    for t in VARIANT_TITLES:
        # Actual headings are "## Problem", "## Variant B", etc.
        key = t if t == "Problem" else t
        if key in sections:
            body = normalize_prompt(sections[key])
            if body:
                variants.append(
                    PromptVariant(
                        puzzle_id=puzzle_id,
                        variant=variant_letter,
                        title=key,
                        prompt=body,
                        expected=expected,
                    )
                )
                variant_letter = chr(ord(variant_letter) + 1)

    # Fallback: if nothing matched, attempt exact "Problem" as "## Problem"
    if not variants and "Problem" in sections:
        body = normalize_prompt(sections["Problem"])
        variants.append(PromptVariant(puzzle_id=puzzle_id, variant="A", title="Problem", prompt=body, expected=expected))

    return variants

def discover_puzzles(puzzles_dir: str) -> List[Tuple[str, str]]:
    puzzles: List[Tuple[str, str]] = []
    for name in sorted(os.listdir(puzzles_dir)):
        m = PUZZLE_FILE_RE.match(name)
        if not m:
            continue
        pid = m.group("id")
        puzzles.append((pid, os.path.join(puzzles_dir, name)))
    return puzzles

def export_prompts(puzzles_dir: str, out_path: str) -> None:
    discovered = discover_puzzles(puzzles_dir)
    bundle = {"puzzles": []}

    for pid, path in discovered:
        md = read_text(path)
        variants = build_variants(pid, md)
        bundle["puzzles"].append({
            "puzzle_id": pid,
            "file": os.path.relpath(path),
            "expected": extract_expected(md),
            "variants": [
                {"variant": v.variant, "title": v.title, "prompt": v.prompt}
                for v in variants
            ]
        })

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2, ensure_ascii=False)

def normalize_output_answer(text: str) -> Optional[str]:
    """
    Extract answer from model output. Prefers 'FINAL: ...' but falls back to last token-like number/word.
    """
    m = EXPECTED_FINAL_RE.search(text)
    if m:
        return m.group("ans").strip()
    # fallback: last "word/number" on last line
    lines = [ln.strip() for ln in text.strip().splitlines() if ln.strip()]
    if not lines:
        return None
    tail = lines[-1]
    tail_m = re.search(r"([A-Za-z0-9_\-]+)\s*$", tail)
    return tail_m.group(1) if tail_m else None

def score_responses(prompts_path: str, responses_path: str, out_path: str) -> None:
    prompts = json.load(open(prompts_path, "r", encoding="utf-8"))
    responses = json.load(open(responses_path, "r", encoding="utf-8"))

    # index prompts by (puzzle_id, variant)
    prompt_index: Dict[Tuple[str, str], Dict] = {}
    expected_index: Dict[str, Optional[str]] = {}
    for p in prompts["puzzles"]:
        expected_index[p["puzzle_id"]] = p.get("expected")
        for v in p["variants"]:
            prompt_index[(p["puzzle_id"], v["variant"])] = v

    # score
    scored_rows = []
    by_puzzle: Dict[str, List[Dict]] = {}

    for r in responses.get("runs", []):
        pid = r["puzzle_id"]
        var = r["variant"]
        out = r["output"]

        expected = expected_index.get(pid)
        got = normalize_output_answer(out)
        ok = (expected is not None and got == expected)

        row = {
            "puzzle_id": pid,
            "variant": var,
            "expected": expected,
            "got": got,
            "format_ok": bool(EXPECTED_FINAL_RE.search(out)),
            "correct": bool(ok),
        }
        scored_rows.append(row)
        by_puzzle.setdefault(pid, []).append(row)

    # invariance: all variants for a puzzle yield same extracted answer
    summary = []
    for pid, rows in sorted(by_puzzle.items()):
        answers = [r["got"] for r in rows if r["got"] is not None]
        unique = sorted(set(answers))
        invariant = (len(unique) == 1 and len(answers) == len(rows))
        acc = sum(1 for r in rows if r["correct"]) / max(1, len(rows))
        summary.append({
            "puzzle_id": pid,
            "variants": len(rows),
            "accuracy": acc,
            "invariant": invariant,
            "unique_answers": unique,
        })

    report = {
        "model": responses.get("model"),
        "scored_rows": scored_rows,
        "summary": summary,
    }

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--puzzles-dir", default="puzzles")
    ap.add_argument("--export-prompts", default=None, help="Path to write prompts.json")
    ap.add_argument("--score", action="store_true", help="Score responses.json against prompts.json")
    ap.add_argument("--prompts", default="prompts.json")
    ap.add_argument("--responses", default="responses.json")
    ap.add_argument("--report", default="report.json")
    args = ap.parse_args()

    if args.export_prompts:
        export_prompts(args.puzzles_dir, args.export_prompts)
        print(f"Wrote prompts bundle: {args.export_prompts}")
        return

    if args.score:
        score_responses(args.prompts, args.responses, args.report)
        print(f"Wrote report: {args.report}")
        return

    ap.print_help()

if __name__ == "__main__":
    main()
