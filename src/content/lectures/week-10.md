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
related:
  - sessions/10-measuring-a-kernel
  - lectures/week-11
  - lectures/week-06
links:
  - label: "v86 — how the x86-to-wasm JIT works"
    url: https://github.com/copy/v86/blob/master/docs/how-it-works.md
  - label: "linux-wasm — a WebAssembly architecture port of Linux"
    url: https://github.com/joelseverin/linux-wasm
---

Everything in weeks 5 to 8 was an attempt to provide kernel services without a
kernel. This week concedes the point, and immediately splits in two.

**Emulate a machine** and the kernel is unmodified. v86 does this: an x86 PC
with an 8259 interrupt controller, an 8254 timer, VGA, IDE, NE2000, and a
just-in-time translator that measures hotness per page and compiles pages into
WebAssembly functions. Paging is emulated through a four-megabyte software TLB,
so every guest memory access is a lookup followed by a bounds-checked
WebAssembly access. It boots Windows 98 and it has no multicore, because
nothing in the design was going to give it one for free.

**Port the kernel** and there is no machine at all. linux-wasm adds WebAssembly
as a Linux architecture — a patched linker, a kernel built **NOMMU** because
WebAssembly has no memory management unit, and a userspace that must therefore
be position-independent. That is a different project with different unfinished
edges, and it is the cleanest illustration that "run a kernel" and "emulate a
machine" are not the same sentence.

Either way you get what the previous five weeks could not: real processes, real
`fork`, a real filesystem, a real TCP stack. One project boots Linux 6.18 from
a snapshot in about a third of a second and runs `node --version` in under two.

And either way you pay, because this is not virtualisation. Hardware
virtualisation runs guest instructions natively and lets the CPU's own page
walker do translation; only privileged operations trap. An emulator in a tab
cannot install a page table, so the hardware does none of that work for it.

## Outline

- emulate a machine, or port a kernel
- v86: JIT, software TLB, and no second core
- linux-wasm: NOMMU, and what that costs userspace
- snapshot boot, and what it buys
- why this is nowhere near KVM, mechanically
- the side effect: a kernel makes graphics tractable
