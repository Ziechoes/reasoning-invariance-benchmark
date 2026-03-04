Title: Puzzle 0005 — Empirical Boundary vs. Theoretical Certainty (Invariance Under Unknowns)

## Purpose
This puzzle tests whether a reasoning system can:
1) distinguish **what it knows** vs **what it assumes**,  
2) request the **minimum additional data** to collapse uncertainty, and  
3) produce a **bounded conclusion** that remains valid if assumptions fail.

This is the “systems-mode” invariant: *never pretend an unmeasured variable is measured.*

---

## Setup
You are given a system with a failure condition that depends on unknown parameters.

A coordinator controls admission to prevent GPU memory oversubscription.

You are told:
- Current GPU headroom at time t0: **H** GB (known)
- Coordinator reaction latency: **L** ms (unknown but bounded)
- KV growth rate during decoding: **G** GB/s (unknown but measurable)
- Oversubscription occurs if KV grows more than headroom during reaction window.

You must decide whether **reactive admission control is a safety guarantee**.

---

## The Core Claim
Reactive coordination is safe only if:

**G × (L / 1000) < H**

But you do not know G or L.

---

## Task
You must produce a response that satisfies ALL constraints:

### Constraint A — Truth-inference invariant
You may not claim safety or unsafety without bounding G and L.

### Constraint B — Minimal measurement plan
You must request the smallest set of measurements that allows a definite conclusion
(“safe within measured envelope” or “not safe”).

### Constraint C — Non-drifting output format
Your answer must be exactly this 4-part structure:

1. **Knowns**
2. **Unknowns**
3. **Safety condition (as inequality)**
4. **Minimal measurement plan** (max 5 bullet points)

No extra commentary.

---

## Input Example
Assume:
- H = 12 GB
- You can measure either:
  - tokens/sec and infer KV growth, OR
  - direct CUDA allocated memory over time, OR
  - scheduler cadence logs
But each measurement costs time. You want the minimum.

---

## Scoring Rubric
A strong answer:
- States the inequality correctly
- Does not pretend to know G or L
- Requests only the measurements needed to bound G and L
- Produces a conclusion that is **conditionally true** and does not overreach

A weak answer:
- Claims “it will break at scale” with no parameter bounds
- Requests too many metrics
- Mixes speculation into “Knowns”

---

## Notes
This puzzle is designed to catch a common failure mode:
**“Correct-sounding theory without empirical anchoring.”**

A truth-seeking system must be able to say:
> “I can’t conclude X yet, but here is the smallest data needed to conclude it.”
