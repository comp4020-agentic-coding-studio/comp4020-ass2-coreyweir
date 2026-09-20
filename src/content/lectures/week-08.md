---
title: The network
description:
  There are no sockets, so you build one out of message passing — and then
  discover the wall was never TCP
week: 8
date: 2027-04-19
teachers:
  - nadia-osei
tags:
  - network
  - pipes
  - processes
related:
  - sessions/08-what-does-it-talk-to
  - lectures/week-09
  - lectures/week-06
links:
  - label: "CORS-safelisted and forbidden request headers"
    url: https://developer.mozilla.org/en-US/docs/Glossary/Forbidden_request_header
  - label: "Direct Sockets API (not available to the web)"
    url: https://wicg.github.io/direct-sockets/
  - label: "Tailscale's browser client — a subset of its API, compiled to WebAssembly"
    url: https://pkg.go.dev/tailscale.com/cmd/tsconnect/wasm
---

A page gets `fetch`, WebSocket, WebRTC and WebTransport. Every one of those
except `fetch` requires the *other end* to have opted in, and `fetch` cannot
express "open a byte stream to this host and port". There is a real sockets API
specified, and its permissions policy defaults to nobody.

So you fake it. A virtual network interface serialises socket operations into
frames, ships them over a transferred `MessagePort`, and something on the other
side answers them — allocating socket identifiers, answering DHCP with an
address it invented, refusing every `listen`, and turning a parsed HTTP request
into a `fetch()`.

Which raises the question this week exists for: in a single thread with no
hardware interrupts, what is doing the kernel's job? The answer is that **the
JavaScript event loop is the interrupt controller.** `postMessage` is the
interrupt, the message handler is the service routine, and the future driver is
the bottom half. Every bug in that layer is that discipline failing — a worker
parked inside a WebAssembly call cannot service the port it is waiting on.

Then the wall. It was never TCP, because there is no TCP. It is that a
cross-origin `fetch` is only readable if the origin opts in, and that forbidden
request headers mean **the guest's byte-exact request is unreproducible by
construction**. One endpoint returning `Access-Control-Allow-Origin` gives you
a clean round trip; another, one line of configuration away, gives you a 502
before your code sees anything. A proxy fixes this only by becoming the origin,
which is how you accidentally ship an open egress service.

There are two honourable ways out, and **neither escapes relaying** — because
the browser cannot send a UDP packet either, so anything below HTTP must be
tunnelled to something that can. You can relay **explicitly**: carry the
connection over a WebSocket to a server holding a real socket, which is how the
x86 emulator from week 1 does its networking. Or you can relay **into a private
network**: a VPN client compiled to WebAssembly reaches its vendor's relay over
a WebSocket, because its own protocol is UDP, and from there traffic egresses
through machines you control.

The second is not less of a relay. It is a relay with an owner, an identity
model and a routing table — and the origin's opinion stops mattering because
you are no longer making web requests at all. Both buy reachability by adding
infrastructure somebody has to run.

## Outline

- what the browser offers, and who has to consent
- a socket made of messages
- the event loop as interrupt controller
- HTTP re-origination, and what cannot survive it
- CORS as the trust boundary
- terminating TLS in the tab, and why that is not cheating
