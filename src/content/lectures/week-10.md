---
title: Running a full OS kernel
description:
  Stop faking the kernel and bring one. Two quite different projects hide under
  that sentence, and only one of them is emulating a machine
week: 10
date: 2027-05-03
teachers:
  - tobias-lin
tags:
  - processes
  - network
  - performance
  - graphics
slides: /decks/week-10/
related:
  - sessions/10-measuring-a-kernel
  - lectures/week-11
  - lectures/week-06
links:
  - label: "v86 — how the x86-to-WebAssembly JIT works"
    url: https://github.com/copy/v86/blob/master/docs/how-it-works.md
  - label: "TinyEMU — Bellard's RISC-V and x86 emulators"
    url: https://bellard.org/tinyemu/
  - label: "linux-wasm — a WebAssembly architecture port of Linux"
    url: https://github.com/joelseverin/linux-wasm
---

Weeks 5 to 8 were all attempts to provide kernel services without a kernel.
This week concedes the point, and immediately splits in two.

**Emulate a machine** and the kernel is unmodified, because it does not know
anything has changed. This is the older and more general answer: an interrupt
controller, a timer, a disk, a network card and a display, all in software. It
boots operating systems from the nineties without their cooperation, and it is
where the browser's oldest party trick comes from.

**Port the kernel** and there is no machine at all. One project adds
WebAssembly as a Linux architecture — which means no memory management unit,
because WebAssembly has none, so the kernel is built without one and every
userspace program must be position-independent. That is a different project
with different unfinished edges, and it is the clearest demonstration that
"run a kernel" and "emulate a machine" are not the same sentence.

Either way you get what the previous five weeks could not: real processes, a
real fork, a real filesystem, a real network stack. One RISC-V system boots
Linux from a snapshot in about a third of a second.

And either way you pay for it, because this is not virtualisation. A hypervisor
runs guest instructions on the real processor and lets the hardware's own page
tables do address translation; only privileged operations trap out. An emulator
in a browser tab cannot install a page table, so it does that work itself, for
every memory access, in software.

## Outline

- emulate a machine, or port a kernel
- interrupts, timers and devices, in software
- no memory management unit, and what that costs userspace
- snapshot boot, and what it buys
- why this is nowhere near a hypervisor, mechanically
- the side effect: a kernel makes graphics tractable
