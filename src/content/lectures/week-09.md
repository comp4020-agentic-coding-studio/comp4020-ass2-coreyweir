---
title: Running "native" binaries
description:
  Take the source requirement away entirely — and find that most of the ways to
  do it are not emulation at all
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
  - label: "elfconv — ahead-of-time translation of Linux ELF to WebAssembly"
    url: https://github.com/yomaytk/elfconv
  - label: "MyAOT — its predecessor, riscv32 ELF to WebAssembly"
    url: https://github.com/AkihiroSuda/myaot
  - label: "Biotite: lifting RV64GC to LLVM IR (Compiler Construction 2025)"
    url: https://dl.acm.org/doi/10.1145/3708493.3712693
---

Every option so far wanted the source, or at least a rebuild. This one does
not, which matters a great deal when the thing you want to run is somebody
else's release artefact.

Four techniques hide under one word, and only the first is emulation.

**Interpretation** decodes and dispatches one instruction at a time. It is
slow, simple and almost always correct, and it will run an unmodified binary
for an architecture your machine has never had.

**Just-in-time translation** measures which code is hot and compiles that, at
runtime, into WebAssembly it then calls.

**Static binary translation** converts the whole binary before it runs. This is
the hard one, because a translator must decide statically what is code, what is
data, and where an indirect jump can land — which is why the serious work here
is compiler research rather than tooling.

**Trace-driven translation** is a fourth thing: record which blocks a real
workload actually executes, then translate those ahead of time and interpret
the rest.

What the field has achieved is narrower than you would guess and better than
you would fear. The strongest published result translates Linux binaries to
WebAssembly at 78–96% of natively-compiled WebAssembly, against roughly ten
times worse for emulation — but only for one architecture, and only for
statically linked programs. Beyond that, RISC-V-to-WebAssembly translators
exist largely as student projects. That is not a gap in the literature so much
as a verdict from it: the technique is understood, and it rarely repays the
effort.

The limit is the elegant part. One project traced 165,264 hot blocks from a
real workload, translated them ahead of time, and brought a cold start from
fifteen minutes to eighteen seconds. It still could not cover the guest's own
just-in-time compiler, because a runtime that writes its own machine code
writes it at addresses no static translator can predict.

## Outline

- interpret, JIT, translate statically, translate from a trace
- running a binary for an architecture you do not have
- what the research has actually delivered, and for what
- why a guest that compiles its own code defeats ahead-of-time translation
