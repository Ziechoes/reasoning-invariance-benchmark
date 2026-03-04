# RIB Puzzle 0008 — Order Sensitivity

## Purpose

This puzzle tests whether a reasoning system produces stable conclusions
when the same information is presented in different orders.

A logically stable system should reach the same result regardless of the
order in which constraints are introduced.

---

## Variant A — Chronological Order

A research team recorded three measurements:

Measurement A = 5  
Measurement B = 7  
Measurement C = 9  

The system value is defined as:

VALUE = A + B + C

Return exactly:

FINAL: <number>

---

## Variant B — Reverse Order

A research team recorded three measurements:

Measurement C = 9  
Measurement B = 7  
Measurement A = 5  

The system value is defined as:

VALUE = A + B + C

Return exactly:

FINAL: <number>

---

## Variant C — Mixed Narrative

Three measurements were taken during an experiment.

The third measurement was 9.  
The first measurement was 5.  
The second measurement was 7.

The system value is defined as the sum of all three measurements.

Return exactly:

FINAL: <number>

---

## Expected Result

A = 5  
B = 7  
C = 9  

5 + 7 + 9 = 21

FINAL: 21

---

## Interpretation

Correct behavior:

The model returns **21** for all variants.

Failure modes:

• Different answers depending on ordering  
• Arithmetic mistakes  
• Failure to track variable identity when order changes
