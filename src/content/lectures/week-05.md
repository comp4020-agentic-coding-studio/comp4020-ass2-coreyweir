---
title: The web is not POSIX-compatible (i)
description:
  What a kernel-shaped surface has to provide, how much of it the web standards
  deliver, and what happens when a call is present but wrong
week: 5
date: 2027-03-22
teachers:
  - corey-weir
tags:
  - processes
  - filesystem
  - network
  - pipes
  - interfaces
related:
  - sessions/05-what-does-it-ask-the-kernel
  - lectures/week-06
  - lectures/week-03
links:
  - label: "WASI — the base system interface"
    url: https://wasi.dev/
  - label: "WASIX — the extended one"
    url: https://wasix.org/
---

Week 4 ended at an interface, and the week before that ended at a wall. The
general answer to both is to stop implementing interfaces one at a time, and
give the program a kernel-shaped surface to compile against instead.

The standard surface is deliberately small — forty-six calls. Four of them
concern sockets, which is enough to read from and write to a socket somebody
handed you and not enough to open one. There is no working directory, so a
program that thinks it has one is really talking to its own C library, which is
keeping a string on its behalf. There are no pipes, no processes, no threads,
and signals in name only. Files are reached through a directory handle granted
at startup rather than by absolute path, so a program can only see what the
host decided to hand it.

The extended surface adds around ninety-five more calls — processes, threads,
sockets you can actually open, a working directory, pipes, a terminal — and
somewhere in there a shell becomes possible.

Then the harder lesson, and the one worth carrying: **a call can be present and
still be wrong.** In one build, the function that replaces a running program
with a different one was compiled so that it had no way to report failure. It
could only succeed or end the process. A shell looking for a command tries each
directory on its search path in turn — so the first miss killed the program
before the second could be attempted. Asking for a command by its full path
worked perfectly. Asking for it by name did nothing at all, and said nothing.

## Outline

- what a kernel-shaped surface has to provide
- the standard forty-six, and the shape of their gaps
- what the extended surface buys, and what it costs to maintain
- pipes, and why they keep coming back
- how a program is packaged and delivered
- present-but-wrong, and how you would find it
