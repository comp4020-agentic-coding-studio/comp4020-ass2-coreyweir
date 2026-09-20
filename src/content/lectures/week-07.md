---
title: The filesystem
description:
  Giving a guest a filesystem is easy. Giving two runtimes the same filesystem
  is where the design is, and where five good designs went to die
week: 7
date: 2027-04-12
teachers:
  - corey-weir
tags:
  - filesystem
  - pipes
  - performance
  - fidelity
related:
  - sessions/07-what-does-it-need-from-a-filesystem
  - lectures/week-08
  - lectures/week-05
links:
  - label: "Origin Private File System — sync access handles"
    url: https://developer.mozilla.org/en-US/docs/Web/API/File_System_Sync_Access_Handle
---

A guest expects inodes, directories, descriptors with private offsets, readdir
cursors, `mmap`, mode bits, symlinks and atomic rename. You can back that with
an in-memory tree, with IndexedDB, with the Origin Private File System, or with
a filesystem living inside shared WebAssembly memory. Each buys something and
costs something, and OPFS in particular is worker-only and takes an exclusive
lock by default.

Then the semantics bite. Reading a large directory takes several calls, and
between them the program is allowed to delete things. One runtime rebuilt the
listing on every call and remembered its place as a position in that list — so
each deletion shifted everything after it, and the cursor stepped straight over
live entries.

The same program, compiled twice: forty checks passed on Linux, ten failed in
the browser. At the buffer size a common standard library actually uses,
deleting a thousand files **left four hundred and ninety-eight of them**, with
no error. Below about a hundred and thirty files it does not happen at all,
which is why it survived everybody's tests.

The week's real subject is coherence. When a JavaScript runtime and a WASIX
runtime must see one filesystem rather than two synchronised copies, the
designs that fail are not the bad ones. A mirrored index made directory reads
eight thousand times faster and was deleted. An overlay that was correct and
shipped was deleted. Barriers that ran thirty iterations with zero conflicts
were deleted. All of them produced ghost entries, because the defect was never
in the implementation — it was in there being two copies.

## Outline

- what a filesystem owes a guest
- four backings, and what each costs
- readdir cookies, and a deletion that removes half the files
- five designs that worked and were deleted anyway
- telling anyone it changed, when the guest cannot call you
- durability, and the four-gigabyte ceiling
