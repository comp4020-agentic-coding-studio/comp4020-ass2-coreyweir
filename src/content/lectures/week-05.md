---
title: The web is not POSIX-compatible (i)
description:
  What a POSIX surface has to provide, what WASI and WASIX actually deliver, and
  what happens when a syscall is present but wrong
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
  - label: "WASIX — the extended syscall surface"
    url: https://wasix.org/
---

Week 4 ended at an interface. This week and next are the general answer: give
the program a kernel-shaped surface and compile against that instead.

WASI preview1 is 46 functions. It has exactly four socket calls —
`sock_accept`, `sock_recv`, `sock_send`, `sock_shutdown` — so you may operate on
a socket somebody handed you, and you may not create or connect one. It has no
`chdir` and no `getcwd`; a working directory is a fiction maintained in libc
userspace. There is no `fd_pipe`, no `fork`, no `exec`, no threads, no signals
worth the name. Filesystem access is capability-scoped: no absolute paths, only
`path_open` relative to a preopened directory handle carrying a rights mask.

WASIX adds roughly ninety-five calls on top — processes, threads, real sockets,
`chdir`, `fd_pipe`, `dup2`, `epoll`, a TTY — and that is enough to run a shell.

Then the harder lesson: **a syscall can be present and still wrong.** In one
wasix-libc sysroot, `execve` compiled to an imported function declared with *no
result*, followed by `unreachable`. A failed exec therefore killed the process
instead of returning `errno`, so musl's userspace PATH loop could never reach
its second candidate. `env printenv` returned nothing; `env /bin/printenv`
worked. That was diagnosed by disassembling `libc.a` to WAT.

## Outline

- what a POSIX surface must provide
- preview1's 46 functions and their gaps
- what WASIX adds, and why a shell becomes possible
- pipes, and why they keep returning
- packaging: WEBc, and multicall binaries dispatching on `argv[0]`
- present-but-wrong: the `execve` import with no result
