---
title: "Assignment 1: The reduction"
description:
  Choose a target, establish what it actually requires, and reduce the option
  space to the ones worth attempting — with reasons
week: 4
due: 2027-03-19T12:00:00+11:00
weight: 20
marking:
  mode: weighted
  criteria:
    - name: Target characterisation
      weight: 40
    - name: Accuracy of option analysis
      weight: 30
    - name: Quality of trade-off reasoning
      weight: 30
spec:
  - a target is named, and its requirements are established from evidence rather than assumption
  - every option is addressed, including the ones you discard immediately
  - each reduction gives a reason that is a trade-off, not a claim of impossibility
  - the reasoning is recorded well enough that you could disagree with it in week 12
related:
  - assessments/assignment-2
  - sessions/02-what-does-it-need
---

## The brief

> Pick something that has no business running in a browser. Establish what it
> would actually take, and say which approaches are worth your semester.

You are not building anything yet. You are producing the document that a
competent engineer writes before committing three months to an approach, and
the thing being assessed is your judgement rather than your conclusion.

**Choose carefully, because you keep this target until week 12.** Something
trivial will not give you an analysis to write — if the honest answer is
"reimplement it in an afternoon", there is no trade-off to reason about and
very little to mark. Something impossibly large will leave you unable to
measure anything in Assignment 2. You also choose your own new requirement in
Assignment 3, so pick a target with somewhere to grow.

Note that the option space is never empty and never small. Every approach in
this course is technically available for every target; what differs is which
ones are *justifiable*, and that is what you are writing about.

## What you submit

A written reduction, of any length that does the job. It must name the target,
establish its requirements with evidence, walk the option space, and give a
reason for every reduction.

Reasons take the form of costs, not verdicts. "Emulating the CPU would be too
slow" is a preference. "This is interactive, interpretation runs about an order
of magnitude down, and the latency budget is 100 ms" is an argument.

You will be asked to grade this document yourself in Assignment 3, so write it
to be checkable. Date your claims, and record what evidence each one rests on.
