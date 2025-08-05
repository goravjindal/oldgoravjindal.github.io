---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: PageRank Centrality in Directed Graphs with Bounded In-Degree"
date: 2025-08-05T00:00:00
---

**Authors:** [Mikkel Thorup](https://dblp.uni-trier.de/search?q=Mikkel+Thorup), [Hanzhi Wang](https://dblp.uni-trier.de/search?q=Hanzhi+Wang), [Zhewei Wei](https://dblp.uni-trier.de/search?q=Zhewei+Wei), [Mingji Yang](https://dblp.uni-trier.de/search?q=Mingji+Yang)

We study the computational complexity of locally estimating a node's PageRank
centrality in a directed graph $G$. For any node $t$, its PageRank centrality
$\pi(t)$ is defined as the probability that a random walk in $G$, starting from
a uniformly chosen node, terminates at $t$, where each step terminates with a
constant probability $\alpha\in(0,1)$.
To obtain a multiplicative $\big(1\pm O(1)\big)$-approximation of $\pi(t)$
with probability $\Omega(1)$, the previously best upper bound is
$O(n^{1/2}\min\{ \Delta\_{in}^{1/2},\Delta\_{out}^{1/2},m^{1/4}\})$ from [Wang,
Wei, Wen, Yang STOC '24], where $n$ and $m$ denote the number of nodes and
edges in $G$, and $\Delta\_{in}$ and $\Delta\_{out}$ upper bound the in-degrees
and out-degrees of $G$, respectively. The same paper implicitly gives the
previously best lower bound of
$\Omega(n^{1/2}\min\{\Delta\_{in}^{1/2}/n^{\gamma},\Delta\_{out}^{1/2}/n^{\gamma},m^{1/4}\})$,
where $\gamma=\frac{\log(1/(1-\alpha))}{4\log\Delta\_{in}-2\log(1/(1-\alpha))}$
if $\Delta\_{in}>1/(1-\alpha)$, and $\gamma=1/2$ if
$\Delta\_{in}\le1/(1-\alpha)$. As $\gamma$ only depends on $\Delta\_{in}$, the
known upper bound is tight if we only parameterize the complexity by $n$, $m$,
and $\Delta\_{out}$. However, there remains a gap of $\Omega(n^{\gamma})$ when
considering $\Delta\_{in}$, and this gap is large when $\Delta\_{in}$ is small.
In the extreme case where $\Delta\_{in}\le1/(1-\alpha)$, we have $\gamma=1/2$,
leading to a gap of $\Omega(n^{1/2})$ between the bounds $O(n^{1/2})$ and
$\Omega(1)$.
In this paper, we present a new algorithm that achieves the above lower bound
(up to logarithmic factors). The algorithm assumes that $n$ and the bounds
$\Delta\_{in}$ and $\Delta\_{out}$ are known in advance. Our key technique is a
novel randomized backwards propagation process which only propagates
selectively based on Monte Carlo estimated PageRank scores.

[Read original post](http://arxiv.org/abs/2508.01257v1)
