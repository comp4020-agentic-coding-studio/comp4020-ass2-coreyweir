---
title: The web is not POSIX-compatible (ii)
description:
  A browser is not a multiprocessing operating system, and the runtime that is
  correct on your desktop deadlocks in a tab
week: 6
date: 2027-03-29
teachers:
  - corey-weir
tags:
  - processes
  - pipes
  - performance
  - fidelity
related:
  - sessions/06-tested-in-node-broken-in-a-tab
  - lectures/week-07
  - lectures/week-12
links:
  - label: "Asyncify (Alon Zakai, 2019)"
    url: https://kripken.github.io/blog/wasm/2019/07/16/asyncify.html
  - label: "Why you need cross-origin isolation"
    url: https://web.dev/articles/why-coop-coep
---

A page is one agent cluster, not a process tree: a main thread, some workers,
and `postMessage` where you wanted `fork`. The consequence is sharper than it
sounds. A window agent's `[[CanBlock]]` is false, so `Atomics.wait` **throws** on
the main thread.

Follow that through a runtime that was written for a desktop. A blocking
`fd_read` calls an inline waker, which parks on a mutex and condvar, which on
`wasm32` with atomics is `Atomics.wait`, which freezes the JavaScript thread —
the same thread that was going to deliver the standard input the read is waiting
for. The shell hangs, and the cause is three layers below the shell.

The detail worth carrying out of this course: **Node's main thread permits
`Atomics.wait`.** So that deadlock sat dormant in shipped code behind a
1,081-test suite, all green. Your test environment was more permissive than your
target, which is the failure mode of this entire field.

Asyncify is the usual escape — binary instrumentation that unwinds and rewinds
the call stack through linear memory — and it costs roughly fifty per cent code
size on average. Beware the naming: in at least one runtime the function called
`__asyncify_light` is not Asyncify at all, but a condvar loop.

Shared memory arrived in 2017, was withdrawn within a day of Spectre in January
2018, and returned only behind cross-origin isolation. `COOP: same-origin`
severs your browsing-context group — which is why enabling it breaks OAuth
popups.

## Outline

- one main thread, some workers, and no processes
- `Atomics.wait`, `[[CanBlock]]`, and a deadlock three layers down
- green tests on a more permissive host
- Asyncify: what it does, what it costs, and what is misnamed
- SharedArrayBuffer, Spectre, and the COOP/COEP bargain
- when shimming beats compiling
