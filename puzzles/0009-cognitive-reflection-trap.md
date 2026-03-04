# RIB Puzzle 0009 — Cognitive Reflection Trap

## Purpose

This puzzle tests whether a reasoning system overrides an intuitive but
incorrect answer and performs the correct logical calculation.

The problem is a well-known cognitive reflection test used in behavioral
science.

---

## Variant A — Direct Question

A bat and a ball cost $1.10 total.

The bat costs $1.00 more than the ball.

How much does the ball cost?

Return exactly:

FINAL: <amount>

---

## Variant B — Reordered Information

The total cost of a bat and a ball is $1.10.

The bat costs $1.00 more than the ball.

How much does the ball cost?

Return exactly:

FINAL: <amount>

---

## Variant C — Narrative Form

At a sporting goods store, a bat and a ball together cost $1.10.

The bat costs one dollar more than the ball.

What is the price of the ball?

Return exactly:

FINAL: <amount>

---

## Correct Logical Analysis

Let the ball cost = x

The bat costs = x + 1.00

Total cost:

x + (x + 1.00) = 1.10

2x + 1.00 = 1.10

2x = 0.10

x = 0.05

---

## Expected Output

FINAL: 0.05

---

## Interpretation

Correct behavior:

The system returns **0.05** for all variants.

Common failure mode:

Models return **0.10**, which is the intuitive but incorrect answer.
