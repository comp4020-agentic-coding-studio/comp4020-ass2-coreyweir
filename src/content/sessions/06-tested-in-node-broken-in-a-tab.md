---
title: Tested in Node, broken in a tab
description:
  Reproduce a defect that only exists in a browser, and work out what your test
  environment was quietly forgiving
week: 6
date: 2027-03-29
teachers:
  - corey-weir
  - nadia-osei
  - tobias-lin
tags:
  - processes
  - fidelity
spec:
  - you can serve a page with COOP and COEP headers set
  - you have read the previous week's syscall inventory for your program
related:
  - lectures/week-06
---

A prepared rig this week, because reproducing this from scratch costs more than
an hour.

You are given a small program that passes its tests under Node and misbehaves in
a browser tab. Your job is to find out why, and then to answer the more useful
question: **what was Node being generous about?**

Work through it in this order, because guessing is slower:

1. Confirm the failure. Get it in front of you rather than described to you.
2. Establish whether anything ran at all. Zero output is not evidence of not
   starting — buffering will lie to you here.
3. Change one variable per run. Write down what each run eliminates.
4. Stop when you can name the constraint, not when the symptom goes away.

Then the same treatment for your own target, on paper: if it blocks, where does
it block, and which thread is that on?

Two things to bring back. First, an elimination table — what you ruled out and
what licensed the ruling. Second, one sentence naming the difference between
the host you tested on and the host you shipped to.

That second sentence is the week. Every option in this course runs on a host
that approximates the target, and approximations are always more forgiving than
the real thing.
