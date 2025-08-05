---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Deterministic Fault-Tolerant Local Load Balancing and its Applications"
date: 2025-08-05T00:00:00
---

**Authors:** [Dariusz R. Kowalski](https://dblp.uni-trier.de/search?q=Dariusz+R.+Kowalski), [Jan Olkowski](https://dblp.uni-trier.de/search?q=Jan+Olkowski)

Load balancing is among the basic primitives in distributed computing. In
this paper, we consider this problem when executed locally on a network with
nodes prone to failures. We show that there exist lightweight network
topologies that are immune to message delivery failures incurred by (at most) a
constant fraction of all nodes. More precisely, we design a novel deterministic
fault-tolerant local load balancing (LLB) algorithm, which, similarly to their
classical counterparts working in fault-free networks, has a relatively simple
structure and guarantees exponentially fast convergence to the average value
despite crash and omission failures.
As the second part of our contribution, we show three applications of the
newly developed fault-tolerant local load balancing protocol. We give a
randomized consensus algorithm, working against $t < n / 3$ crash failures,
that improves over the best-known consensus solution by Hajiaghayi et al. with
respect to communication complexity, yet with an arguable simpler technique of
combining a randomly and locally selected virtual communication graph with a
deterministic fault-tolerant local load balancing on this graph.
We also give a new solution for consensus for networks with omission
failures. Our solution works against $t < \frac{n}{C\log{n} (\log\log n)^2}$
omissions, for some constant $C$, is nearly optimal in terms of time
complexity, but most notably -- it has communication complexity $O((t^2 +
n)\text{ polylog } {n})$, matching, within a polylogarithmic factor, the lower
bound by Abraham et. al. with respect to both terms depending on $t$ and $n$.
Ours is the first algorithm in the literature that is simultaneously nearly
optimal, in terms of $n,t$, with respect to both complexity measures, against
the adaptive omission-causing adversary.

[Read original post](http://arxiv.org/abs/2508.01373v1)
