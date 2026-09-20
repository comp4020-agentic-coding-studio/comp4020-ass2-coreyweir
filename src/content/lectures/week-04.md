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

Qt for WebAssembly is the honest catalogue. Every `Q*Server` class is
unsupported, so nothing listens. `QSsl` and `QDnsLookup` do not function,
because the browser owns DNS and TLS. WebGL permits one context per surface with
no sharing, so `QOpenGLWidget` is out. And `app.exec()` never returns, so
destructors never run — a nested event loop needs Asyncify or JSPI to exist at
all.

LibreOffice is the same lesson at scale: the WebAssembly build is **Writer
only**, linking may need 64 GB of RAM, and the blocker is architectural rather
than mechanical — dialogs are a nested event loop, and fixing that means
"basically dropping `Application::Execute`".

There is an ordering to how things break, and weeks 5 to 11 follow it.

## Outline

- what compiles for free, and why that is uninteresting
- Emscripten as an operating-system shim: files, GL, pthreads, blocking
- Qt and LibreOffice, read as failure catalogues
- the order interfaces break in — and where each of the remaining weeks sits
