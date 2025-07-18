---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Splittable Spanning Trees and Balanced Forests in Dense Random Graphs"
date: 2025-07-18T00:00:00
---

**Authors:** [David Gillman](https://dblp.uni-trier.de/search?q=David+Gillman), [Jacob Platnick](https://dblp.uni-trier.de/search?q=Jacob+Platnick), [Dana Randall](https://dblp.uni-trier.de/search?q=Dana+Randall)

Weighted equitable partitioning of a graph has been of interest lately due to
several applications, including redistricting, network algorithms, and image
decomposition. Weighting a partition according to the spanning-tree metric has
been of mathematical and practical interest because it typically favors
partitions with more compact pieces. An appealing algorithm suggested by
Charikar et al. is to sample a random spanning tree and remove k-1 edges,
producing a random forest. If the components of the forest form a balanced
partition, the partition is equitable under an easily computed acceptance
probability. Cannon et al. recently showed that spanning trees on grid graphs
and grid-like graphs on $n$ vertices are splittable into $k$ equal sized pieces
with probability at least $n^{-2k}$, leading to the first rigorous sampling
algorithm for a class of graphs. We present complementary results showing that
spanning trees on dense random graphs also have inverse polynomial probability
of being splittable, giving another class of graphs where equitable partitions
can be efficiently sampled exactly. These proofs also guarantee fast
almost-uniform sampling for the up-down walk on forests, giving another
provably efficient randomized method for generating equitable partitions.
Further, we show that problems with the well-studied ReCom algorithm for
equitable partitioning are more extensive than previously known, even in
special cases that were believed to be more promising. We present a family of
graphs where the Markov chain fails to be irreducible when it must keep the
components perfectly equitable; yet when the chain is allowed an imbalance of
just one vertex between components, the rejection sampling step may take
exponential time. This is true even when the graph satisfies desirable
properties that have been conjectured to be sufficient for fast sampling.

[Read original post](http://arxiv.org/abs/2507.12707v1)
