---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Deterministic Lower Bounds for k-Edge Connectivity in the Distributed"
date: 2025-07-16T00:00:00
---

**Authors:** [Peter Robinson](https://dblp.uni-trier.de/search?q=Peter+Robinson), [Ming Ming Tan](https://dblp.uni-trier.de/search?q=Ming+Ming+Tan)

We study the $k$-edge connectivity problem on undirected graphs in the
distributed sketching model, where we have $n$ nodes and a referee. Each node
sends a single message to the referee based on its 1-hop neighborhood in the
graph, and the referee must decide whether the graph is $k$-edge connected by
taking into account the received messages.
We present the first lower bound for deciding a graph connectivity problem in
this model with a deterministic algorithm. Concretely, we show that the worst
case message length is $\Omega( k )$ bits for $k$-edge connectivity, for any
super-constant $k = O(\sqrt{n})$. Previously, only a lower bound of $\Omega(
\log^3 n )$ bits was known for ($1$-edge) connectivity, due to Yu (SODA 2021).
In fact, our result is the first super-polylogarithmic lower bound for a
connectivity decision problem in the distributed graph sketching model.
To obtain our result, we introduce a new lower bound graph construction, as
well as a new 3-party communication complexity problem that we call
UniqueOverlap. As this problem does not appear to be amenable to reductions to
existing hard problems such as set disjointness or indexing due to correlations
between the inputs of the three players, we leverage results from
cross-intersecting set families to prove the hardness of UniqueOverlap for
deterministic algorithms. Finally, we obtain the sought lower bound for
deciding $k$-edge connectivity via a novel simulation argument that, in
contrast to previous works, does not introduce any probability of error and
thus works for deterministic algorithms.

[Read original post](http://arxiv.org/abs/2507.11257v1)
