---
title: Could it run unmodified?
description:
  Establish what it would take to run your target as a binary rather than as
  source, and price the answer
week: 9
date: 2027-04-26
teachers:
  - nadia-osei
  - tobias-lin
tags:
  - processes
  - performance
spec:
  - you can obtain or cross-compile a build of your target for another architecture
  - you know from week 5 what your target asks the kernel for
related:
  - lectures/week-09
---

The question sounds like a yes or no and is really a cost estimate.

**Can you even get a binary?** A static build for the architecture you would
emulate. For some targets this is a download; for others it is a cross-compile
that takes the session; for a few it is the point at which you discover the
project has never been built for anything but x86-64.

**What would have to be implemented underneath it?** This is where week 5's
inventory earns its keep. A translation layer that skips the kernel has to
provide every syscall the binary makes — so the inventory *is* the
specification, and anything you missed is a crash rather than a warning.

**And what will it cost?** Interpreters are roughly an order of magnitude.
Translation can approach native. Measure something rather than quoting a
number: start it, time it, and record what the time was actually spent on.

If your target is a language runtime, ask the question this week is built
around: does it generate code at runtime? If it does, you have just found the
ceiling on every ahead-of-time approach, and you should say so in your evidence
log now rather than discovering it in week 12.

Bring: whether a binary exists, what it would need, and one measured number.
