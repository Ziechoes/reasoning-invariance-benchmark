# Reasoning Invariance Benchmark — RUNBOOK

This document explains how the benchmark repository is maintained.

It is written for non-technical operators.

---

# Repository Purpose

The repository stores a collection of reasoning puzzles designed to test
whether AI systems maintain logical stability under perturbation.

Each puzzle is called a **RIB (Reasoning Invariance Benchmark)**.

Example:

RIB-0001  
RIB-0002  
RIB-0003  

---

# Puzzle Registry

All puzzles are stored in:

puzzles/

Each puzzle file uses the format:

0001-name.md  
0002-name.md  

The number is permanent and should never change.

---

# Puzzle List

RIB-0001 — Prompt Surface Invariance  
RIB-0002 — Instruction Hierarchy  
RIB-0003 — Self Consistency  
RIB-0004 — Multi Constraint Drift  
RIB-0005 — Empirical Boundary vs Theory  
RIB-0006 — Logical Paradox Stability  

---

# How New Puzzles Are Added

1. Create new file in:

puzzles/

Example:

puzzles/0007-new-test.md

2. Update:

puzzles/INDEX.md

3. Commit changes.

---

# Commit Messages

Use one of these:

Add RIB puzzle  
Update RIB puzzle  
Fix puzzle logic  
Update benchmark index  

---

# Google Drive Backup

The assistant maintains a mirror archive.

Location:

Project Archive / RIB_Benchmark /

This archive contains:

• puzzle files  
• index file  
• runbook  

GitHub is the active repository.  
Google Drive is the backup archive.

---

# Responsibilities

Repository owner:

• add puzzles  
• manage GitHub  

Assistant:

• maintain Drive archive  
• track puzzle numbers  
• ensure index is updated

---

# Future Work

Later versions of this repository may include an automated evaluation
harness for running puzzles across multiple AI systems.

This is not required for the initial benchmark artifacts.
