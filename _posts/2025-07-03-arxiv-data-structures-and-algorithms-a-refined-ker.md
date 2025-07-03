---
layout: post
title: "arXiv: Data Structures and Algorithms: A Refined Kernel for $d$-Hitting Set"
date: 2025-07-03 13:21:53 
categories: [rss]
external_link: http://arxiv.org/abs/2506.24114v1
---

**Authors:** [Yuxi Liu](https://dblp.uni-trier.de/search?q=Yuxi+Liu), [Mingyu Xiao](https://dblp.uni-trier.de/search?q=Mingyu+Xiao)

The $d$-Hitting Set problem is a fundamental problem in parameterized
complexity, which asks whether a given hypergraph contains a vertex subset $S$
of size at most $k$ that intersects every hyperedge (i.e., $S \cap e \neq
\emptyset$ for each hyperedge $e$). The best known kernel for this problem,
established by Abu-Khzam [1], has $(2d - 1)k^{d - 1} + k$ vertices. This result
has been very widely used in the literature as many problems can be modeled as
a special $d$-Hitting Set problem. In this work, we present a refinement to
this result by employing linear programming techniques to construct crown
decompositions in hypergraphs. This approach yields a slight but notable
improvement, reducing the size to $(2d - 2)k^{d - 1} + k$ vertices.
