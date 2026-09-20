---
title: What does it ask the kernel for?
description:
  Take the syscall inventory of a real program and decide which surface could
  actually host it
week: 5
date: 2027-03-22
teachers:
  - nadia-osei
  - tobias-lin
tags:
  - processes
  - filesystem
  - network
spec:
  - you can run a native binary under a syscall tracer
  - you bring a program that does something more than compute
related:
  - lectures/week-05
---

This is the most open session of the semester, because almost anything can be
traced. Use your assignment target if it is native.

Otherwise, pick something with a reputation:

- `git` — processes, filesystem, network, and a lot of them
- `curl` — a single clean network story
- `ffmpeg` — heavy compute with an awkward IO shape
- a package manager — the worst case, and the most instructive
- a language interpreter running a real script

Trace it. Count what it asks for, and sort the calls into: **in preview1**, **in
WASIX**, **in neither**.

The number that matters is the third column, and the interesting part is
usually not its size but its content. One `fork` is worse than four hundred
`read`s. A single `bind` ends the conversation for an entire class of approach.

Two things to bring back:

- the smallest surface that would run your program unmodified
- the one call you would most like to delete from its requirements, and what it
  would cost the program to lose it

That second question is the week's real content. Most of the engineering in
this field is not implementing a syscall. It is arranging not to need it.
