---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Weighted Matching in a Poly-Streaming Model"
date: 2025-07-21T00:00:00
---

**Authors:** [Ahammed Ullah](https://dblp.uni-trier.de/search?q=Ahammed+Ullah), [S. M. Ferdous](https://dblp.uni-trier.de/search?q=S.+M.+Ferdous), [Alex Pothen](https://dblp.uni-trier.de/search?q=Alex+Pothen)

We introduce the poly-streaming model, a generalization of streaming models
of computation in which $k$ processors process $k$ data streams containing a
total of $N$ items. The algorithm is allowed $O\left(f(k)\cdot M\_1\right)$
space, where $M\_1$ is either $o\left(N\right)$ or the space bound for a
sequential streaming algorithm. Processors may communicate as needed.
Algorithms are assessed by the number of passes, per-item processing time,
total runtime, space usage, communication cost, and solution quality.
We design a single-pass algorithm in this model for approximating the maximum
weight matching (MWM) problem. Given $k$ edge streams and a parameter
$\varepsilon > 0$, the algorithm computes a
$\left(2+\epsilon\right)$-approximate MWM. We analyze its performance in a
shared-memory parallel setting: for any constant $\varepsilon > 0$, it runs in
time $\widetilde{O}\left(L\_{\max}+n\right)$, where $n$ is the number of
vertices and $L\_{\max}$ is the maximum stream length. It supports
$O\left(1\right)$ per-edge processing time using $\widetilde{O}\left(k\cdot
n\right)$ space. We further generalize the design to hierarchical
architectures, in which $k$ processors are partitioned into $r$ groups, each
with its own shared local memory. The total intergroup communication is
$\widetilde{O}\left(r \cdot n\right)$ bits, while all other performance
guarantees are preserved.
We evaluate the algorithm on a shared-memory system using graphs with
trillions of edges. It achieves substantial speedups as $k$ increases and
produces matchings with weights significantly exceeding the theoretical
guarantee. On our largest test graph, it reduces runtime by nearly two orders
of magnitude and memory usage by five orders of magnitude compared to an
offline algorithm.

[Read original post](http://arxiv.org/abs/2507.14114v1)
