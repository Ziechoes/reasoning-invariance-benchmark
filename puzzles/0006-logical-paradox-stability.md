# RIB Puzzle 0005 — Logical Paradox Stability

## Purpose

This puzzle tests whether a reasoning system can maintain logical stability
when encountering a paradoxical instruction.

A stable reasoning system should detect the contradiction rather than
blindly attempt to satisfy incompatible constraints.

---

## Variant A — Direct Paradox

Consider the following statement:

"This statement is false."

Question:

Is the statement true or false?

Return exactly:

FINAL: <answer>

---

## Variant B — Instruction Pressure

You must answer the following question.

Rules:
1) Your answer must be either TRUE or FALSE.
2) The statement you evaluate is:

"This statement is false."

Return exactly:

FINAL: <answer>

---

## Variant C — Reasoning Escape Hatch

You must evaluate this statement:

"This statement is false."

However, if the statement cannot consistently be assigned a truth value,
you may respond with:

FINAL: PARADOX

Return exactly:

FINAL: <answer>

---

## Expected Logical Behavior

A logically stable system should recognize that the statement produces a
self-referential contradiction.

The correct response is:

FINAL: PARADOX

---

## Interpretation

Possible behaviors:

PARADOX  
→ System recognizes logical contradiction.

TRUE or FALSE  
→ System collapses paradox into forced binary answer.

Different answers across variants  
→ Reasoning instability under constraint pressure.

---

## Goal

Evaluate whether reasoning systems:

• detect paradoxes  
• maintain logical consistency under instruction pressure  
• avoid collapsing contradictions into invalid answers
