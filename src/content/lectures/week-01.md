---
title: Running code in the browser
description:
  Thirty years of running foreign code in a web page, almost all of it the same
  idea — and the option space that replaced it
week: 1
date: 2027-02-22
teachers:
  - corey-weir
tags:
  - interfaces
slides: /decks/week-01/
related:
  - sessions/01-four-things-that-should-not-work
  - lectures/week-02
links:
  - label: "Gary Bernhardt, The Birth & Death of JavaScript (2014)"
    url: https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript
  - label: "Yee et al., Native Client (IEEE S&P 2009)"
    url: https://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/34913.pdf
  - label: "Goodbye PNaCl, Hello WebAssembly (Chromium Blog, 2017)"
    url: https://blog.chromium.org/2017/05/goodbye-pnacl-hello-webassembly.html
---

Almost every attempt to run somebody else's code in a web page was the same
idea: ship a second engine. Java applets, Flash and Silverlight each brought
their own VM, their own JIT, their own renderer and their own security model.
The page gave them a rectangle and an IPC channel. ActiveX did not even do that
— it instantiated COM objects in-process and asked the user for permission,
which is a liability transfer rather than a security model.

Native Client breaks the story in both directions, which is why we spend time
on it. Architecturally it was a plugin: real x86 on the bare CPU, delivered
through a Google-only ABI. Philosophically it was WebAssembly — untrusted code
accepted only because a static validator proved it conformed, with "no pop-up
window asks for permission". It died of politics and portability, not of
security.

One correction to the usual story: asm.js was not first. Emscripten emitted
plain JavaScript in 2010 and Bellard booted Linux in a JS engine in 2011. What
asm.js added was *predictable* compilation, not arrival.

## Outline

- the plugin era, and what each one actually was
- who killed each, and why
- NaCl and PNaCl: the right idea behind the wrong ABI
- asm.js, Emscripten, WebAssembly
- "it's just compilers" — yes, and no
- the option space, demonstrated
