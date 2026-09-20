---
title: "Assignment 2: The commitment"
description:
  Build enough of at least two approaches to measure them, then commit to one
  and show what closed the decision
week: 9
due: 2027-04-30T12:00:00+10:00
weight: 40
marking:
  mode: weighted
  criteria:
    - name: Decisiveness of experimental design
      weight: 35
    - name: Evidence quality
      weight: 35
    - name: The commitment argument
      weight: 30
spec:
  - at least two approaches are built far enough to produce real measurements
  - each experiment distinguishes between stated alternatives rather than demonstrating one
  - measurements are reproducible, and the conditions they were taken under are stated
  - a commitment is made, and the evidence that closed it is identified
related:
  - assessments/assignment-1
  - assessments/assignment-3
---

## The brief

> Intuition got you this far. Now find out which of your remaining options
> actually works, and commit to one on evidence you gathered yourself.

Proofs of concept are cheap, and that is the premise of this assignment rather
than a complaint about it. Building two rough versions is expected to be the
smaller part of your effort. The larger part is designing comparisons that
settle something, and knowing what your results do and do not license.

The commonest failure is a demonstration dressed as an experiment. A working
prototype proves an approach can do one thing under conditions you chose. It
says nothing about the approach against its alternative, which is the only
question you are being asked.

The second commonest is trusting a permissive host. Measure on the thing you
intend to ship to. Runtimes that behave on a desktop deadlock in a tab, test
suites pass green against hosts that are more forgiving than the target, and a
defect that appears only above some threshold will not appear in your sample.

## What you submit

Your prototypes, and a written commitment.

The prototypes need to be runnable and need not be pretty. Say what each one
does and does not implement — an approach dismissed on the performance of a
version that skipped the expensive part has not been dismissed.

The commitment names the approach you are taking forward, the measurements that
decided it, and — importantly — what would have had to be true for one of the
others to win. If you cannot state that condition, you have not compared them.
