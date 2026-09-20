---
title: Graphics
description:
  The week where the choice you made in February decides what you are allowed
  to draw with
week: 11
date: 2027-05-10
teachers:
  - corey-weir
tags:
  - graphics
  - interfaces
  - network
  - performance
related:
  - sessions/11-the-rendering-path
  - lectures/week-12
  - lectures/week-04
links:
  - label: "An X server compiled to WebAssembly"
    url: https://github.com/roozbehid/XServer
  - label: "Greenfield — a Wayland compositor for the web"
    url: https://github.com/udevbe/greenfield
  - label: "WebVM 2.0 — unmodified Xorg via kernel mode-setting"
    url: https://labs.leaningtech.com/blog/webvm-20
---

Nothing else in this course constrains you as sharply as this. The rendering
path was not chosen in week 11 — it was decided by the approach you committed
to, and this is the week you find out what that left you.

**You compiled the application.** You get the browser's own graphics APIs, and
you rewrite whatever your program used to call. One drawing context per
surface, no sharing between them, and a subset of the API you knew. But the
scope is wider than it first looks: you are not limited to compiling the
application. Somebody has compiled an entire X server to WebAssembly, which
means "port the app" and "port the thing the app talks to" are both on the
table.

**You compiled against a POSIX surface.** Your program still believes it is
opening a socket and speaking a display protocol. A compositor running in the
page can be the other end of that conversation — a Wayland compositor written
in TypeScript will accept clients over a message channel — though the client
has to be rebuilt to reach it, so this is cheaper than it sounds only if you
were rebuilding anyway.

**You emulated a machine.** You get a framebuffer, blitted to a canvas.
Unaccelerated, completely general, and the reason a twenty-five-year-old
desktop works perfectly.

**You ran a kernel.** You can implement the graphics device and the kernel's
mode-setting interface and run an unmodified X server — in two dimensions.
Wayland stays out of reach while the EGL layer is unimplemented.

One detail from outside the course's premise, because it is too good to leave
out. If you are permitted *not* to run the program in the browser, you keep it
on a real machine and ship pixels. The remote path of that Wayland compositor
encodes surfaces as H.264 — and H.264 has no alpha channel, so every frame is
sent as **two** video streams, opaque and alpha, recomposited in the page. A
constraint three layers down reached up and changed the architecture.

## Outline

- four approaches, four rendering stories
- what a graphics port actually rewrites
- compiling the display server rather than the client
- framebuffers, mode-setting, and unmodified X
- remote pixels, codecs, and the missing alpha channel
