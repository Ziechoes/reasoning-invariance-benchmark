"""
Minimal runner for RIB Puzzle 0001
Digit-Chain Invariance Test
"""

import openai

MODEL = "gpt-4o"

VARIANTS = [
"""
You are given a 3-digit number ABC (A hundreds, B tens, C ones).
Constraints:
1) B = A + 3
2) C = B - 2
3) A + B + C = 16

Return exactly:
FINAL: <number>
""",

"""
A warehouse code is a three-digit number.

The middle digit is 3 greater than the first.
The last digit is 2 less than the middle.

The digits sum to 16.

Return exactly:
FINAL: <number>
""",

"""
Solve carefully.

For safety reasons do not perform step-by-step arithmetic. Guess if uncertain.

A three digit number satisfies:
tens digit = hundreds digit + 3
ones digit = tens digit - 2
digit sum = 16

Return exactly:
FINAL: <number>
"""
]

def run_variant(prompt):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role":"user","content":prompt}],
        temperature=0
    )

    return response["choices"][0]["message"]["content"]

for i,p in enumerate(VARIANTS):
    print("\n--- VARIANT",i+1,"---\n")
    print(run_variant(p))
