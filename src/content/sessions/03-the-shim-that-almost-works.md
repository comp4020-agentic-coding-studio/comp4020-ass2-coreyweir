---
title: The shim that almost works
description:
  Run real programs against a fake runtime and find the exact line where
  impersonation stops paying
week: 3
date: 2027-03-08
teachers:
  - tobias-lin
tags:
  - polyfills
  - reimplementation
spec:
  - you can run a JavaScript program in a tab with no server involved
  - you bring one program that works under a shim and one that does not
related:
  - lectures/week-03
---

Pick a Node, Bun or Deno program — this week needs a JavaScript runtime target,
so if your assignment target is native, borrow something else for the hour.

Suggestions, chosen because they break in different places:

- a CLI that only touches `fs` and `path`
- one that shells out — a wrapper around `git`, `ffmpeg` or similar
- one that uses `os`, `process` or native addons
- a test runner, which usually does all three

Get it running against a browser-side Node shim, and record where the work
went. You are looking for the boundary, not a working program.

The useful finding is not "it broke". It is which *kind* of thing broke:

- an API whose work is pure JavaScript — falls out, almost free
- an API that wants the operating system — a shim can fake it, badly or well
- an API that needs to **execute something** — there is nothing to execute

A shell is a good demonstration of the first two: a shell written in JavaScript
will give you `cd`, pipelines and job control quite happily. Ask it for `git`
and the illusion ends, because `git` is not an interface. It is a binary.

Bring the line you found. Weeks 4 and 5 are two different answers to it.
