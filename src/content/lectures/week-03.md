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

Three words get used interchangeably, and the difference between them decides
what the work costs.

A **polyfill** implements a standard the environment is missing, so callers use
the ordinary API and never learn it was absent. A **shim** is the broader move:
sit in front of a surface and translate, which includes adapting to an API that
is not the one the caller asked for. Polyfills are a kind of shim — the kind
where the seams are invisible. A **reimplementation** rebuilds the
functionality itself, and it is the only one of the three whose cost has no
ceiling.

Reimplementation also scales worse than people expect. A date formatter is an
afternoon, until it has to match a specification, at which point it is a week
of edge cases. A file-search tool is comfortable over any filesystem you like
— until it has to run a command on each result, which needs something to run
commands. A game ported to the browser meets a graphics API that resembles the
one it was written against without matching it, and somebody is now
reimplementing graphics.

The point that matters for the rest of the course: reimplementation is not an
alternative to the other options. It is a **component** of all of them. Every
approach here reimplements something. The question is how much, and whether
you chose it or discovered it.

## Outline

- polyfill, shim, reimplement — and why the words are worth separating
- what falls out cheaply, and what does not
- emulating a runtime rather than a machine
- the wall: things that exist only as compiled binaries
