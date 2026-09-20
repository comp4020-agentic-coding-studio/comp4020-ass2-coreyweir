---
title: The rendering path
description:
  Trace a pixel from a program to the screen, and find out what a committed
  approach leaves you able to draw with
week: 11
date: 2027-05-10
teachers:
  - nadia-osei
  - tobias-lin
tags:
  - graphics
spec:
  - you can say which approach you committed to in Assignment 2
  - you bring something that draws, even if it is not your target
related:
  - lectures/week-11
---

Plenty of targets never draw anything. If yours is one of them, borrow
something that does — the week's content is the *path*, and you can only see it
on a program that has one.

Suggestions, chosen so the room ends up with different paths to compare:

- an SDL or OpenGL demo compiled to WebAssembly
- a terminal application, and then the question of what is drawing the terminal
- an emulated machine running a desktop
- an X client against an X server that was itself compiled to WebAssembly
- a graphical program driven remotely, with the pixels arriving as video

**Trace the path.** From the call the program makes to the thing on the screen,
name every layer and every translation. Then find the first layer where your
committed approach has no answer, or a worse one than you assumed.

**Get two numbers.** Time to first frame, and how it feels to interact with.
The second is subjective and is not optional — this is the one place in the
course where the subjective measure decides whether the result is usable at
all.

Bring back the path, the first layer that fails, and an estimate: if graphics
became a requirement for your target tomorrow, what would your committed
approach cost you? You choose your own new requirement in Assignment 3 and this
may well not be it — but the estimate is the same shape either way, and this is
the cheapest week to practise making one.
