---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Sparse Navigable Graphs for Nearest Neighbor Search: Algorithms and"
date: 2025-07-21T00:00:00
---

**Authors:** [Sanjeev Khanna](https://dblp.uni-trier.de/search?q=Sanjeev+Khanna), [Ashwin Padaki](https://dblp.uni-trier.de/search?q=Ashwin+Padaki), [Erik Waingarten](https://dblp.uni-trier.de/search?q=Erik+Waingarten)

We initiate the study of approximation algorithms and computational barriers
for constructing sparse $\alpha$-navigable graphs [IX23, DGM+24], a core
primitive underlying recent advances in graph-based nearest neighbor search.
Given an $n$-point dataset $P$ with an associated metric $\mathsf{d}$ and a
parameter $\alpha \geq 1$, the goal is to efficiently build the sparsest graph
$G=(P, E)$ that is $\alpha$-navigable: for every distinct $s, t \in P$, there
exists an edge $(s, u) \in E$ with $\mathsf{d}(u, t) < \mathsf{d}(s,
t)/\alpha$. We consider two natural sparsity objectives: minimizing the maximum
out-degree and minimizing the total size.
We first show a strong negative result: the slow-preprocessing version of
DiskANN (analyzed in [IX23] for low-doubling metrics) can yield solutions whose
sparsity is $\widetilde{\Omega}(n)$ times larger than optimal, even on
Euclidean instances. We then show a tight approximation-preserving equivalence
between the Sparsest Navigable Graph problem and the classic Set Cover problem,
obtaining an $O(n^3)$-time $(\ln n + 1)$-approximation algorithm, as well as
establishing NP-hardness of achieving an $o(\ln n)$-approximation. Building on
this equivalence, we develop faster $O(\ln n)$-approximation algorithms. The
first runs in $\widetilde{O}(n \cdot \mathrm{OPT})$ time and is thus much
faster when the optimal solution is sparse. The second, based on fast matrix
multiplication, is a bicriteria algorithm that computes an $O(\ln
n)$-approximation to the sparsest $2\alpha$-navigable graph, running in
$\widetilde{O}(n^{\omega})$ time.
Finally, we complement our upper bounds with a query complexity lower bound,
showing that any $o(n)$-approximation requires examining $\Omega(n^2)$
distances. This result shows that in the regime where $\mathrm{OPT} =
\widetilde{O}(n)$, our $\widetilde{O}(n \cdot \mathrm{OPT})$-time algorithm is
essentially best possible.

[Read original post](http://arxiv.org/abs/2507.14060v1)
