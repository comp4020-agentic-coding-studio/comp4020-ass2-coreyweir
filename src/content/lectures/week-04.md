---
title: Compiling for the web
description:
  Pure computation compiles and always did. Everything that makes a program
  useful is an interface, and interfaces are what break a port
week: 4
date: 2027-03-15
teachers:
  - corey-weir
tags:
  - interfaces
  - processes
  - filesystem
  - network
  - graphics
related:
  - sessions/04-which-interface-stops-you
  - lectures/week-11
links:
  - label: "Qt for WebAssembly — the supported-feature list"
    url: https://doc.qt.io/qt-6/wasm.html
  - label: "LibreOffice: README.wasm.md"
    url: https://github.com/LibreOffice/core/blob/master/static/README.wasm.md
---

Two questions frame the week. Find me a realistic codebase with no standard
library dependency that will *not* compile to WebAssembly. Then find me a
realistic codebase with no rendering, terminal, pipe, network or filesystem
requirement.

The first set is empty and the second is nearly empty, which tells you the
toolchain was never the problem. Compilation is solved. Interfaces are not.

Qt's WebAssembly port publishes an honest catalogue of what it cannot do, and
it reads as a list of interfaces rather than a list of bugs. Nothing can
listen, because there are no server sockets. The TLS and DNS classes do not
function, because the browser owns both. The widget that wraps a drawing
context is unavailable, because you get one context per surface and cannot
share between them. And the call that runs the application never returns, so
destructors never run — which means a dialog that waits for an answer does not
work, because waiting is the thing you cannot do.

LibreOffice is the same lesson at scale. The WebAssembly build is **Writer
only**, and linking it may need sixty-four gigabytes of memory. But the real
blocker is architectural rather than mechanical: dialogs are implemented by
running a second event loop inside the first, and the browser has exactly one.
Fixing it means removing the mechanism the entire application is built on.

There is an ordering to how things break, and weeks 5 to 11 follow it.

## Outline

- what compiles for free, and why that is uninteresting
- Emscripten as an operating-system shim: files, GL, pthreads, blocking
- Qt and LibreOffice, read as failure catalogues
- the order interfaces break in — and where each of the remaining weeks sits
