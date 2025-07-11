---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Efficient and Adaptive Estimation of Local Triadic Coefficients"
date: 2025-07-11T00:00:00
---

**Authors:** [Ilie Sarpe](https://dblp.uni-trier.de/search?q=Ilie+Sarpe), [Aristides Gionis](https://dblp.uni-trier.de/search?q=Aristides+Gionis)

Characterizing graph properties is fundamental to the analysis and to our
understanding of real-world networked systems. The local clustering
coefficient, and the more recently introduced, local closure coefficient,
capture powerful properties that are essential in a large number of
applications, ranging from graph embeddings to graph partitioning. Such
coefficients capture the local density of the neighborhood of each node,
considering incident triadic structures and paths of length two. For this
reason, we refer to these coefficients collectively as local triadic
coefficients.
In this work, we consider the novel problem of computing efficiently the
average of local triadic coefficients, over a given partition of the nodes of
the input graph into a set of disjoint buckets. The average local triadic
coefficients of the nodes in each bucket provide a better insight into the
interplay of graph structure and the properties of the nodes associated to each
bucket. Unfortunately, exact computation, which requires listing all triangles
in a graph, is infeasible for large networks. Hence, we focus on obtaining
highly-accurate probabilistic estimates.
We develop Triad, an adaptive algorithm based on sampling, which can be used
to estimate the average local triadic coefficients for a partition of the nodes
into buckets. Triad is based on a new class of unbiased estimators, and
non-trivial bounds on its sample complexity, enabling the efficient computation
of highly accurate estimates. Finally, we show how Triad can be efficiently
used in practice on large networks, and we present a case study showing that
average local triadic coefficients can capture high-order patterns over
collaboration networks.

[Read original post](http://arxiv.org/abs/2507.07536v1)
