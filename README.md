R# Reasoning Invariance Benchmark (RIB)

Small experimental benchmark exploring whether LLM reasoning remains stable
when logically identical problems are expressed with different surface forms.

## Core Idea

If a model performs genuine logical inference, the reasoning trajectory and
final answer should remain stable when:

• the prompt is rephrased
• constraints are reordered
• irrelevant instructions are injected
• equivalent logical forms are used

If answers diverge across equivalent variants, this suggests the model may be
coupled to surface prompt structure rather than underlying logic.

---

## Puzzle Suite

Each test is called a **RIB puzzle**.

Current set:

RIB-0001 — Prompt Surface Invariance
RIB-0002 — Instruction Hierarchy
RIB-0003 — Self Consistency
RIB-0004 — Multi-Constraint Drift
RIB-0005 — Empirical Boundary vs Theory
RIB-0006 — Logical Paradox Stability

Puzzles are located in:

puzzles/

---

## Repository Structure

```
reasoning-invariance-benchmark
│
├ puzzles/
│   ├ 0001-invariance-digit-chain.md
│   ├ 0002-instruction-hierarchy.md
│   ├ 0003-self-consistency-collapse.md
│   ├ 0004-multi-constraint-drift.md
│   ├ 0005-empirical-boundary-vs-theory.md
│   └ 0006-logical-paradox-stability.md
│
├ harness/
│   └ rib_eval.py
│
├ README.md
└ RUNBOOK.md
```

---

## Evaluation Harness

The repository includes a small harness that can:

1. Export puzzle prompts
2. Run models against puzzle variants
3. Measure answer stability

Example workflow:

```
python harness/rib_eval.py --export-prompts prompts.json
python harness/rib_eval.py --score --prompts prompts.json --responses responses.json
```

---

## Project Status

This repository is an early sandbox exploring reasoning invariance tests.

Future work may include:

• larger puzzle suites
• cross-model benchmarking
• adversarial perturbation tests
• architectural analysis of reasoning stability

## Results

Benchmark runs will be recorded in:

results/benchmark-results.md
