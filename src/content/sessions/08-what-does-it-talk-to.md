---
title: What does it talk to?
description:
  Inventory your program's network requirements, then find out which of them a
  browser can actually satisfy and what the rest would cost
week: 8
date: 2027-04-19
teachers:
  - tobias-lin
tags:
  - network
spec:
  - you can read a request and response in full, headers included
  - you bring a list of every host, port and protocol your program contacts
related:
  - lectures/week-08
---

Inventory first, then sort by what can actually be tested.

**The inventory.** Every host, every port, every protocol. Does it listen? Does
it need UDP? Does it hold a connection open, or is it request-response? Does it
care about the exact bytes of its own request?

**The HTTP endpoints you can test directly.** Issue the request from a browser
and see what comes back. The answer is immediate and binary: either the origin
sends the header that permits you to read the response, or it does not.

Try a spread — an API that advertises support, a vendor API that does not, a
package registry, and something of your own where you control the headers.

**Everything else you cannot test that way**, and pretending otherwise is the
mistake this session exists to prevent. A raw TCP service, a UDP protocol, or
anything that listens will not answer a browser request at all. For those the
question is not "does it work" but "what shape of answer is available":

- **A relay.** Tunnel the connection over a WebSocket to something that holds
  the real socket. This is not a hack of last resort — the x86 emulator you
  used in week 1 does exactly this for its networking.
- **A real network stack.** Bring a VPN into the page: a WireGuard client
  compiled to WebAssembly gives the guest genuine reachability, and CORS stops
  being the question because you are no longer making web requests.
- **Change the protocol**, if you control both ends.
- **Move the requirement**, if it turns out nobody needed UDP after all.

Each of those costs something — a server you now run, a network you now join,
a protocol you now maintain. Price at least one of them.

Bring back: how many of your program's endpoints are directly reachable, what
you would do about the rest, and what that would cost somebody to operate.
