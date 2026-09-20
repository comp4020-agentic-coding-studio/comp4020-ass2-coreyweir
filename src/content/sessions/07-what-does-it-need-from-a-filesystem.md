---
title: What does it need from a filesystem?
description:
  Establish what your program actually requires of a filesystem, then break a
  filesystem that looks correct
week: 7
date: 2027-04-12
teachers:
  - corey-weir
  - nadia-osei
  - tobias-lin
tags:
  - filesystem
  - fidelity
spec:
  - you can write a small conformance test against a real POSIX system first
  - you know whether anything other than your program reads its files
related:
  - lectures/week-07
---

Two halves this week.

**First, your target.** Does it need durability, or only a working directory
for the length of a session? Does it `mmap`? Does it rename over a live file?
Does it create symlinks, or only follow them? Does anything else — a build
tool, an editor, another runtime — need to see the same bytes at the same time?

Most programs need far less than their authors assume, and the useful output is
a short list of requirements you can defend.

**Second, a conformance test.** Write a small program that exercises one
filesystem behaviour precisely — directory enumeration while deleting is the
recommended one — and run it in two places: a real POSIX system first, then a
browser-hosted filesystem.

The native run is not a formality. It is the oracle. Without it you cannot tell
a wrong answer from an answer you did not understand, and you will spend the
hour debugging your own test.

Suggested behaviours, if you want a different one:

- enumerate a directory while unlinking from it
- `rename` over an open file, then read the old descriptor
- two writers appending to one file
- `stat` after a write, from a different runtime

Every one of those has a scale you can turn up: entries in the directory, bytes
in the file, concurrent writers, calls before you check. Turn it up until the
two hosts disagree, then turn it back down until they agree again.

**That threshold is the finding.** Not the bug — the number of entries, or
kilobytes, or writers below which everything looks correct. It tells you how
large a test would have had to be to catch this, and therefore why nobody did.
