---
title: Characterising a target
description:
  Everything is possible, so the interesting question is what a program actually
  requires — and how those requirements reduce the set worth attempting
week: 2
date: 2027-03-01
teachers:
  - corey-weir
tags:
  - interfaces
  - processes
  - filesystem
  - network
  - graphics
related:
  - sessions/02-what-does-it-need
  - lectures/week-12
---

Nothing in this course is impossible. That is not encouragement — it is the
reason the course exists. If every option is technically available, then
choosing between them is the entire job, and "can it be done" is a question
that wastes a fortnight.

What reduces the set is the target itself. A program that is pure computation
compiles and runs almost anywhere. A program that expects processes, a
filesystem it shares with something else, a listening socket, or a rendering
surface is asking for things the browser either does not have or provides in a
shape that will not fit.

So we characterise before we choose. What language and runtime is it? Does it
spawn? Does it block? What does it open, and what does it talk to? Does it draw?
Each answer removes options — and, more usefully, tells you what evidence you
would need to remove more.

Contrast the two targets this course carries. For **Claude Code**, every option
stays live and the decision is comparative. For **Chromium**, one requirement —
a rendering surface — removes most of the space before you have written
anything.

## Outline

- possible versus justifiable
- the characterisation axes, and what each one rules out
- two targets, opposite shapes
- what Assignment 1 asks for, and why the choice binds you until week 12
