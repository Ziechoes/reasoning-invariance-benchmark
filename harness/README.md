# Reasoning Invariance Benchmark Harness

## Export prompts

From repo root:

python harness/rib_eval.py --export-prompts prompts.json

This creates a portable prompt bundle you can run anywhere.

## Provide model outputs

Create a `responses.json` like:

{
  "model": "MODEL_NAME",
  "runs": [
    {"puzzle_id": "0004", "variant": "A", "output": "FINAL: 567"},
    {"puzzle_id": "0004", "variant": "B", "output": "FINAL: 567"}
  ]
}

## Score outputs

python harness/rib_eval.py --score --prompts prompts.json --responses responses.json --report report.json

Outputs:
- per-variant correctness
- per-puzzle invariance (all variants agree)
- summary accuracy
