---
title: The web is not POSIX-compatible (ii)
description:
  A browser is not a multiprocessing operating system, and a runtime that is
  correct on your desktop will deadlock in a tab
week: 6
date: 2027-03-29
teachers:
  - corey-weir
tags:
  - processes
  - pipes
  - performance
  - fidelity
slides: /decks/week-06/
related:
  - sessions/06-tested-in-node-broken-in-a-tab
  - lectures/week-07
  - lectures/week-12
links:
  - label: "Asyncify — unwinding and resuming a WebAssembly stack"
    url: https://kripken.github.io/blog/wasm/2019/07/16/asyncify.html
  - label: "Why you need cross-origin isolation"
    url: https://web.dev/articles/why-coop-coep
---

Last week's surface assumed an operating system underneath it. A page is not
one. It is a single main thread, some workers, and message passing where you
wanted processes.

One consequence outweighs the rest: **the browser forbids the main thread from
blocking.** A call that would put that thread to sleep does not sleep — it
throws.

Consider a runtime that was written for a desktop, where blocking is the most
ordinary thing in the world. A program asks to read from its input. The runtime
does what it has always done and blocks the thread until bytes arrive. That
thread is the one that was going to deliver the bytes. The program hangs
forever, nothing in the program is wrong, and the cause is three layers below
anything the author wrote.

Now the detail worth carrying out of this course. The same runtime, on the same
code, is *fine* under Node — because Node's main thread is permitted to block.
So the deadlock sat dormant in shipped code behind a suite of more than a
thousand passing tests. **The host you tested on was more permissive than the
host you shipped to**, which is the characteristic failure of this entire field
and which week 7 will repeat with a completely different mechanism.

The usual escape is to rewrite the compiled program so it can unwind its own
call stack into memory, return to the browser mid-call, and resume later from
where it stopped. It works. It costs around fifty per cent code size, and it
is easy to believe you have it when you do not.

Shared memory between threads arrived in 2017, was withdrawn within a day of
Spectre in 2018, and returned only for pages willing to trade for it: cut
yourself off from other windows, and refuse any resource that has not
explicitly agreed to be embedded. That bargain is why switching it on breaks
login popups.

## Outline

- one thread, some workers, and no processes
- the main thread may not block, and what that does three layers down
- green tests on a more forgiving host
- unwinding and resuming a call stack, and what it costs
- shared memory, Spectre, and the bargain that brought it back
- when a shim beats a compiler
