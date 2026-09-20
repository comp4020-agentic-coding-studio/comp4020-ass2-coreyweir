---
title: Measuring a kernel
description:
  Take your own numbers off a prepared machine, then work out what a whole
  operating system would cost your target
week: 10
date: 2027-05-03
teachers:
  - tobias-lin
tags:
  - performance
spec:
  - you arrive with the cost estimates you have made for at least two other approaches
related:
  - lectures/week-10
---

Nobody is booting a kernel for their own target in an hour, so this week you
measure a rig that already works and reason from it.

You are given a browser-hosted machine running a real operating system.
Measure, rather than read:

- **Cold start.** First byte to usable prompt. Then do it again with a warm
  cache and note the difference.
- **Size.** What was downloaded, and what is resident afterwards.
- **Throughput.** Something CPU-bound, against the same work on your host. Get
  a ratio.
- **Latency.** Typing. It is subjective and it matters more than the ratio.
- **The thing that breaks.** Use it as you would a real machine for five
  minutes and find the first thing that is not there. Copy and paste between
  the page and the guest. Resize the window. Play a sound. Open a second core's
  worth of work. Unplug the network. Reload the tab and see what survived.

Then the estimate. For your target: what would this approach cost in download,
in start-up, in throughput — and, honestly, what would it *fix*? A kernel
solves processes, filesystems and sockets in one move. If your target needed
all three, this may be cheaper than five weeks of shims. If it needed none of
them, you are paying tens of megabytes for nothing.

Bring one row for your evidence log with a real number in it, and a sentence
saying whether this option is still live for you. "Eliminated, on these
numbers" is a good outcome and you will be asked to defend it in week 12.
