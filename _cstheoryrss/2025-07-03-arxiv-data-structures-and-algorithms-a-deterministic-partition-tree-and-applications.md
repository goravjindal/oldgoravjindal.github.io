---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: A Deterministic Partition Tree and Applications"
date: 2025-07-03T00:00:00
---

**Authors:** [Haitao Wang](https://dblp.uni-trier.de/search?q=Haitao+Wang)

In this paper, we present a deterministic variant of Chan's randomized
partition tree [Discret. Comput. Geom., 2012]. This result leads to numerous
applications. In particular, for $d$-dimensional simplex range counting (for
any constant $d \ge 2$), we construct a data structure using $O(n)$ space and
$O(n^{1+\epsilon})$ preprocessing time, such that each query can be answered in
$o(n^{1-1/d})$ time (specifically, $O(n^{1-1/d} / \log^{\Omega(1)} n)$ time),
thereby breaking an $\Omega(n^{1-1/d})$ lower bound known for the semigroup
setting. Notably, our approach does not rely on any bit-packing techniques. We
also obtain deterministic improvements for several other classical problems,
including simplex range stabbing counting and reporting, segment intersection
detection, counting and reporting, ray-shooting among segments, and more.
Similar to Chan's original randomized partition tree, we expect that additional
applications will emerge in the future, especially in situations where
deterministic results are preferred.

[Read original post](http://arxiv.org/abs/2507.01775v1)
