# RIB Puzzle 0003 — Self-Consistency Collapse

## Purpose

Test whether a reasoning system maintains internal logical consistency
when the same reasoning chain is presented through slightly different
narrative structures.

A reasoning system performing stable inference should produce the
same answer across equivalent reasoning paths.

---

## Variant A — Direct Logic

Three friends share a bill.

The total bill is $30.

They decide to split the cost evenly.

How much does each person pay?

Return exactly:

FINAL: <amount>

---

## Variant B — Narrative Framing

Alice, Bob, and Carol go to dinner.

The total bill is $30.

They agree that everyone should contribute the same amount.

How much does each person contribute?

Return exactly:

FINAL: <amount>

---

## Variant C — Distracting Narrative

Three friends go out for dinner and receive a bill of $30.

One friend briefly considers paying more but they ultimately agree
that everyone should pay an equal share.

How much does each person pay?

Return exactly:

FINAL: <amount>

---

## Expected Logical Result

FINAL: $10

---

## Interpretation

If outputs diverge across variants, this indicates that reasoning may
be influenced by narrative structure rather than invariant logical
computation.

Stable reasoning systems should produce identical results across all
variants.
