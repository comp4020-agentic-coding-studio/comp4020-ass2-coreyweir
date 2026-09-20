---
title: What does it talk to?
description:
  Find out whether your program's network requirements survive a browser, using
  the only test that settles it
week: 8
date: 2027-04-19
teachers:
  - tobias-lin
tags:
  - network
spec:
  - you can read a request and response in full, headers included
  - you bring a list of every host your program contacts
related:
  - lectures/week-08
---

Inventory first, then verdict.

**What does it talk to?** Every host, every port, every protocol. Does it
listen? Does it need UDP? Does it hold a connection open, or is it
request-response? Does it care about the exact bytes of its own request?

**Then the only test that settles anything.** For each host, issue the request
from a browser and see what comes back. A `fetch` from the console is enough to
learn the answer, and the answer is usually immediate: either the origin sends
`Access-Control-Allow-Origin` and you are fine, or it does not and you are not.

Try a spread, because the variety is the lesson:

- an API that advertises CORS support
- one that does not — most vendor APIs
- a package registry or distribution mirror
- something of your own, where you control the headers

Record which succeeded, which failed, and what the failure looked like from
JavaScript. Note in particular how little the error tells you.

The finding to bring back is a sentence of the form: *my target contacts N
hosts; M of them are reachable from a page; here is what I would have to do
about the rest.* Options are not limited to "give up" — you can proxy, vendor
the data, change the protocol, or choose a different approach entirely. What
you cannot do is make somebody else's server send a header.
