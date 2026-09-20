---
title: Which interface stops you first?
description:
  Compile several things that have no business compiling, and find the pattern
  in how they fail
week: 4
date: 2027-03-15
teachers:
  - nadia-osei
  - tobias-lin
tags:
  - interfaces
spec:
  - you have a working Emscripten or wasm32 toolchain before you arrive
  - you can read a linker error without flinching
related:
  - lectures/week-04
---

The room needs variety this week, because the finding is a *pattern* and one
person cannot see it alone. Take one from each band if you can:

- **Pure compute** — a compression or hashing library, a solver, a parser
- **Terminal-shaped** — a small CLI utility that reads stdin and writes stdout
- **Blocking or re-entrant** — anything with a modal loop, a `sleep`, or a
  synchronous wait
- **Networked** — anything that opens a socket, and ideally anything that
  *listens*
- **Graphical** — an SDL or OpenGL demo

Compile it. Record the first thing that stopped you, and classify it: missing
symbol, unsupported syscall, an API that exists but does nothing, a link that
succeeds and a binary that hangs.

Then pool the results on the board in the order they broke. The point of the
hour is the shape of that list, not any individual failure — and whether the
room's ordering matches the one the lecture claimed.

If your target is a JavaScript runtime and none of this applies to it, take
something else. But answer the week's question about your target anyway, in one
sentence, because Assignment 1 is due this week and this is the question it is
asking.
