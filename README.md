# Reasoning Invariance Benchmark

Small experimental sandbox investigating **reasoning invariance** in LLM systems.

Hypothesis:

A reasoning system performing genuine logical inference should produce stable
solutions when logically identical problems are phrased differently.

If outputs diverge, this suggests coupling between reasoning trajectories and
surface prompt features rather than invariant inference.

---

## Current Experiment

**RIB-0001 — Digit Chain Invariance**

Puzzle:

puzzles/0001-invariance-digit-chain.md

Runner:

run_rib_test.py
