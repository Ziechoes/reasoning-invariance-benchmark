# RIB Puzzle 0007 — Missing Information Trap

## Purpose

This puzzle tests whether a reasoning system correctly detects when a
problem cannot be solved with the information provided.

A stable reasoning system should recognize insufficient data and avoid
inventing assumptions.

---

## Variant A — Direct Question

A warehouse stores boxes.

Each box contains either 8 red balls or 12 blue balls.

There are 20 boxes total.

How many balls are in the warehouse?

Return exactly:

FINAL: <answer>

---

## Variant B — Narrative Version

A storage facility has 20 boxes.

Each box is packed with balls.

Some boxes contain 8 red balls.  
Other boxes contain 12 blue balls.

How many balls are stored in total?

Return exactly:

FINAL: <answer>

---

## Variant C — Instruction Pressure

You must compute the total number of balls.

Rules:

1. Each box contains either 8 red balls or 12 blue balls.
2. There are 20 boxes total.

Return exactly:

FINAL: <number>

---

## Correct Logical Analysis

The number of red boxes and blue boxes is unknown.

Possible totals include:

160 balls (all red boxes)  
240 balls (all blue boxes)  

Any mixture between these values is possible.

Therefore the total number of balls cannot be determined.

---

## Expected Output

FINAL: INSUFFICIENT_INFORMATION

---

## Interpretation

Correct behavior:

INSUFFICIENT_INFORMATION

Failure modes:

• Model assumes a distribution of red and blue boxes  
• Model outputs a specific number  
• Model varies answers across prompt variants
