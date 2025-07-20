---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Kernelization for H-Coloring"
date: 2025-07-18T00:00:00
---

**Authors:** [Yael Berkman](https://dblp.uni-trier.de/search?q=Yael+Berkman), [Ishay Haviv](https://dblp.uni-trier.de/search?q=Ishay+Haviv)

For a fixed graph $H$, the $H$-Coloring problem asks whether a given graph
admits an edge-preserving function from its vertex set to that of $H$. A
seminal theorem of Hell and Ne\v{s}et\v{r}il asserts that the $H$-Coloring
problem is NP-hard whenever $H$ is loopless and non-bipartite. A result of
Jansen and Pieterse implies that for every graph $H$, the $H$-Coloring problem
parameterized by the vertex cover number $k$ admits a kernel with
$O(k^{\Delta(H)})$ vertices and bit-size bounded by $O(k^{\Delta(H)} \cdot \log
k)$, where $\Delta(H)$ denotes the maximum degree in $H$. For the case where
$H$ is a complete graph on at least three vertices, this kernel size nearly
matches conditional lower bounds established by Jansen and Kratsch and by
Jansen and Pieterse.
This paper presents new upper and lower bounds on the kernel size of
$H$-Coloring problems parameterized by the vertex cover number. The upper
bounds arise from two kernelization algorithms. The first is purely
combinatorial, and its size is governed by a structural quantity of the graph
$H$, called the non-adjacency witness number. As applications, we obtain
kernels whose size is bounded by a fixed polynomial for natural classes of
graphs $H$ with unbounded maximum degree. More strikingly, we show that for
almost every graph $H$, the degree of the polynomial that bounds the size of
our combinatorial kernel grows only logarithmically in $\Delta(H)$. Our second
kernel leverages linear-algebraic tools and involves the notion of faithful
independent representations of graphs. It strengthens the general bound from
prior work and, among other applications, yields near-optimal kernels for
problems concerning the dimension of orthogonal graph representations over
finite fields. We complement these results with conditional lower bounds,
thereby nearly settling the kernel complexity of the problem for various target
graphs $H$.

[Read original post](http://arxiv.org/abs/2507.13129v1)
