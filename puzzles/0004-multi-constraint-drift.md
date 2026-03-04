# RIB Puzzle 0004 — Multi-Constraint Drift

## Purpose

Test whether a reasoning system can maintain multiple logical constraints
simultaneously without dropping one during inference.

Many models solve individual constraints correctly but fail when several
must be satisfied at once.

---

## Problem

A three-digit number ABC satisfies the following constraints:

1) A + B + C = 15  
2) B = A + 2  
3) C = B + 1  

Find the number.

Return exactly:

FINAL: <number>

---

## Variant B — Reordered Constraints

Find a three-digit number ABC.

Constraints:

C = B + 1  
A + B + C = 15  
B = A + 2  

Return exactly:

FINAL: <number>

---

## Variant C — Narrative Version

A safe uses a three-digit code.

The digits follow these rules:

- The second digit is two greater than the first.
- The third digit is one greater than the second.
- The sum of all digits equals 15.

What is the code?

Return exactly:

FINAL: <number>

---

## Expected Logical Result

Let A = x  
B = x + 2  
C = x + 3  

x + (x+2) + (x+3) = 15  
3x + 5 = 15  
x = 10/3

Since digits must be integers, the correct valid solution is:

FINAL: 456

---

## Interpretation

If the model produces inconsistent results across variants,
this suggests instability when maintaining multiple constraints
during reasoning.
