---
title: Running "native" binaries
description:
  Take the source requirement away entirely. Most of the ways to do that are
  not emulation, and the difference between them is the week
week: 9
date: 2027-04-26
teachers:
  - tobias-lin
tags:
  - processes
  - performance
  - fidelity
related:
  - sessions/09-could-it-run-unmodified
  - lectures/week-10
  - lectures/week-04
links:
  - label: "elfconv — AOT translation of Linux ELF to WebAssembly"
    url: https://github.com/yomaytk/elfconv
  - label: "Biotite: lifting RV64GC to LLVM IR (CC 2025)"
    url: https://dl.acm.org/doi/10.1145/3708493.3712693
---

Every option so far needed the source, or at least a rebuild. This one does
not, and that is worth a great deal when the thing you want to run is somebody
else's release artefact.

The word "emulation" covers four different techniques and only one of them is
emulation. **Interpretation** decodes and dispatches each instruction, and it
is the slow, simple, reliable one. **Just-in-time translation** compiles hot
code at runtime after measuring it. **Ahead-of-time static binary translation**
converts the whole binary before it runs — which means solving code-versus-data
and indirect jumps statically, which is exactly why there is an academic
literature here rather than a weekend project. And translating at
snapshot-build time from a recorded trace is a fourth thing again.

That literature is the answer to the obvious objection about this course. NTT's
elfconv lifts Linux ELF through LLVM IR to WebAssembly at between 78 and 96 per
cent of natively-compiled wasm, against roughly ten times worse for emulation.
It is also AArch64-only and statically-linked-only, and no completed general
RISC-V-to-WebAssembly static translator appears to exist. The discipline is
real, thin, and has room in it.

The limit is elegant. One project traced 165,264 hot blocks into a 158 MB
generated source file and a 60 MB wasm module, and brought a cold start from
fifteen minutes to eighteen seconds. It still could not cover the guest's
own JIT, because V8 emits machine code at runtime at addresses no static
translator can predict. **Ahead-of-time translation is defeated by guests that
generate their own code.**

## Outline

- interpretation, JIT, static translation, and trace-driven AOT
- an unmodified Node binary, interpreted
- what the literature has actually achieved
- the JIT-versus-AOT limit, with numbers
