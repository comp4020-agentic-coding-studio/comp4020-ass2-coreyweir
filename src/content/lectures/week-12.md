---
title: Committing, and changing your mind
description:
  How to commit on evidence, and why changing your mind here is not an
  iteration — it is discarding an execution environment
week: 12
date: 2027-05-17
teachers:
  - nadia-osei
tags:
  - performance
  - interfaces
related:
  - sessions/12-defending-the-commitment
  - lectures/week-02
  - lectures/week-09
---

Twelve weeks of options, and the course ends where the work actually starts:
deciding, on evidence, and living with it.

Committing well is mostly about what you measured. A cost estimate you cannot
source is a preference. The honest artefacts are boring — a table of what was
tried, what it cost, and what each result eliminated — and they are what let
you say "no" to an approach without having spent six weeks on it.

The harder lesson is what a change of mind costs *here*. Software engineering
generally assumes you can iterate: ship something, learn, refactor, keep the
valuable parts. That assumption relies on your logic being separable from the
thing running it. In this field it is not. You did not build an application —
you built an execution environment tuned to one target. Change the target's
requirements and you do not refactor. You throw the environment away and build
a different one, and almost nothing transfers.

So the scoping decisions you made when you chose your target are the expensive
ones, and the outer reaches of your requirements matter more than the likely
ones. A
requirement for native applications, or for a desktop, does not extend your
approach — it invalidates it.

The exception proves the rule. A deliberately temporary layer, chosen knowing
you would replace it, with the migration priced in from the start, is a
different thing from a rework. That is a plan. Discovering the same fact in
week nine is not.

Sometimes the right answer is the smallest one. On this project, a fifteen-line
syscall delegation beat a dependency upgrade that cost ten workarounds and
could not support subprocesses at all.

## Outline

- what a defensible commitment looks like
- why "make it work then iterate" does not apply
- scope decisions as the expensive ones
- priced-in replacement versus rework
- knowing when to stop, re-scope, or ask upstream
