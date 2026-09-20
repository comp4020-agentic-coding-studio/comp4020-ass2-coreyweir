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
  - label: "Greenfield — a Wayland compositor for the web"
    url: https://github.com/udevbe/greenfield
  - label: "WebVM 2.0 — unmodified Xorg via KMS"
    url: https://labs.leaningtech.com/blog/webvm-20
---

Nothing in this course determines your options as sharply as this. The
rendering path is not something you choose in week 11; it was decided by the
approach you committed to, and this is the week you find out what it gave you.

- **You compiled the app.** You get WebGL or WebGPU, and you rewrite your
  graphics code. One context per surface, no sharing, and a subset of GL ES
  unless you bring an emulation layer.
- **You emulated a machine.** You get a framebuffer blitted to a canvas.
  Unaccelerated, entirely general, and the reason a twenty-five-year-old
  operating system works perfectly.
- **You ran a kernel.** You can implement the graphics device and the kernel
  mode-setting interface, and run an unmodified X server — in two dimensions.
  Wayland stays out of reach while EGL is unimplemented.
- **You kept the app native.** You keep the whole application on a real machine
  and ship pixels. A Wayland compositor written in TypeScript renders each
  surface as a WebGL texture; the remote path takes zero-copy buffers into an
  H.264 pipeline and decodes in the browser.

That last one has a detail worth the whole week: H.264 has no alpha channel, so
every frame ships as **two** video streams, one opaque and one alpha, composited
in the page. This is what it looks like when a constraint three layers down
reaches up and changes your architecture.

## Outline

- four approaches, four rendering stories
- GL ES, WebGPU, and what a port actually rewrites
- framebuffers, KMS, and unmodified X
- Wayland over a socket that is not a socket
- remote pixels: codecs, latency, and the missing alpha channel
