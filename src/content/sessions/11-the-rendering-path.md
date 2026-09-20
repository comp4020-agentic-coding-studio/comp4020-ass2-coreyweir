---
title: The rendering path
description:
  Trace a pixel from your program to the screen, and find out what your
  committed approach has left you
week: 11
date: 2027-05-10
teachers:
  - tobias-lin
tags:
  - graphics
spec:
  - you have committed to an approach and can say which
  - you know whether your target draws anything at all
related:
  - lectures/week-11
---

Some targets do not draw. If yours is one of them, this session is still the
one where you find out what your approach *would* have cost you, because
Assignment 3 may well hand you a requirement that draws.

**Trace the path.** From the call your program makes, to the thing that ends up
on the screen. Name every layer and every translation. Then find the first
layer where your chosen approach has no answer.

Suggested things to try, depending on where you landed:

- an SDL or OpenGL demo compiled to WebAssembly — what did the GL layer become?
- an emulated machine running a desktop — how does the framebuffer arrive?
- a graphical program on a remote compositor — where does the latency live?
- a program that only writes to a terminal — what is drawing the terminal?

For whichever you pick, get two numbers: how long until the first frame, and
how it feels to interact with. The second is not rigorous and is not optional.
This is the one place in the course where the subjective measure is the one
that decides whether the result is usable.

Bring back: the path, the first layer that failed or would fail, and what it
would cost to change approach now in order to fix it. That last figure is what
Assignment 3 is about, and it is cheaper to discover this week than next.
