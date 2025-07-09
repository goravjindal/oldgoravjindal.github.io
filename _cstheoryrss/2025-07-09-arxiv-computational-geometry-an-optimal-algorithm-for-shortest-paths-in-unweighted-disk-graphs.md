---
layout: post
category: cstheoryrss
title: "arXiv: Computational Geometry: An Optimal Algorithm for Shortest Paths in Unweighted Disk Graphs"
date: 2025-07-09T00:00:00
---

**Authors:** [Bruce W. Brewer](https://dblp.uni-trier.de/search?q=Bruce+W.+Brewer), [Haitao Wang](https://dblp.uni-trier.de/search?q=Haitao+Wang)

Given in the plane a set $S$ of $n$ points and a set of disks centered at
these points, the disk graph $G(S)$ induced by these disks has vertex set $S$
and an edge between two vertices if their disks intersect. Note that the disks
may have different radii. We consider the problem of computing shortest paths
from a source point $s\in S$ to all vertices in $G(S)$ where the length of a
path in $G(S)$ is defined as the number of edges in the path. The previously
best algorithm solves the problem in $O(n\log^2 n)$ time. A lower bound of
$\Omega(n\log n)$ is also known for this problem under the algebraic decision
tree model. In this paper, we present an $O(n\log n)$ time algorithm, which
matches the lower bound and thus is optimal. Another virtue of our algorithm is
that it is quite simple.

[Read original post](http://arxiv.org/abs/2507.05569v1)
