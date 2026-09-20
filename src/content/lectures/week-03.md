---
title: Shims, polyfills and reimplementation
description:
  The cheapest option in the course — implement the interface instead of the
  machine — and the three very different things people mean by it
week: 3
date: 2027-03-08
teachers:
  - corey-weir
tags:
  - polyfills
  - reimplementation
related:
  - sessions/03-the-shim-that-almost-works
  - lectures/week-04
---

Three distinct things get called the same thing, and the distinction decides
what the work costs.

A **polyfill** fills a gap in a surface that already exists and is otherwise
fine. A **shim** stands in front of a surface and translates. A
**reimplementation** rebuilds the thing. Only the third has unbounded cost, and
it is the one people wander into by accident.

Reimplementation also scales worse than anyone expects. `date` is an afternoon,
until it has to be POSIX-compatible, at which point it is a week of edge cases.
`find` is comfortable over any filesystem you like — until `-exec`, which needs
a process. A game ported to the browser meets WebGL, which is not OpenGL, and
somebody is now reimplementing a graphics API.

The important point for later weeks: reimplementation is not an alternative to
the other options on the ladder. It is a **component** of all of them. Every
approach in this course ends up reimplementing something; the question is how
much, and whether you chose it.

We also meet Nodepod here, because week 7 needs the picture of two runtimes
sharing one world.

## Outline

- polyfill, shim, reimplement — and why the words matter
- what falls out easily, and what does not
- Nodepod, and a real shell that is itself JavaScript
- the wall: anything that exists only as a compiled binary
