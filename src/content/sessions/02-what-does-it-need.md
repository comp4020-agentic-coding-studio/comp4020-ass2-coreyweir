---
title: What does it need?
description:
  Take a program apart from the outside and write down what it requires, using
  evidence rather than assumption
week: 2
date: 2027-03-01
teachers:
  - nadia-osei
  - tobias-lin
tags:
  - interfaces
  - processes
spec:
  - you bring a program you did not write and can run locally
  - you can read a linker or dependency listing without guessing
related:
  - lectures/week-02
  - assessments/assignment-1
---

Pick a program. If you already have a candidate for Assignment 1, use it — this
is the one session that is directly your assignment work. If not, take one of:

- a CLI tool you use and have never looked inside
- something from your own field with an awkward dependency
- a small game, if you want the graphics question early

Produce a requirements profile, from evidence:

- **Runtime.** Native? A language VM? Is the thing you care about the program,
  or the runtime underneath it?
- **Processes.** Does it spawn, fork, or shell out? `strace`, or read the source.
- **Filesystem.** What does it open, and does anything else need to see the same
  bytes?
- **Network.** What does it talk to, and does it listen?
- **Graphics.** Does it draw, and through what?
- **Blocking.** Does it ever sit and wait?

Write each finding next to how you established it. "I think it forks" and
"`strace` shows 3 `clone` calls during startup" are not the same claim, and by
week 12 you will be marked on knowing the difference.

Then swap with someone whose target is nothing like yours and attack each
other's profile. The useful question is always the same one: *how do you know?*
