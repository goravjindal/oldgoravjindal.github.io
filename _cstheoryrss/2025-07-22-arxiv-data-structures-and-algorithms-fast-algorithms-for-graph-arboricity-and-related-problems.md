---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Fast Algorithms for Graph Arboricity and Related Problems"
date: 2025-07-22T00:00:00
---

**Authors:** [Ruoxu Cen](https://dblp.uni-trier.de/search?q=Ruoxu+Cen), [Henry Fleischmann](https://dblp.uni-trier.de/search?q=Henry+Fleischmann), [George Z. Li](https://dblp.uni-trier.de/search?q=George+Z.+Li), [Jason Li](https://dblp.uni-trier.de/search?q=Jason+Li), [Debmalya Panigrahi](https://dblp.uni-trier.de/search?q=Debmalya+Panigrahi)

We give an algorithm for finding the arboricity of a weighted, undirected
graph, defined as the minimum number of spanning forests that cover all edges
of the graph, in $\sqrt{n} m^{1+o(1)}$ time. This improves on the previous best
bound of $\tilde{O}(nm)$ for weighted graphs and $\tilde{O}(m^{3/2}) $ for
unweighted graphs (Gabow 1995) for this problem. The running time of our
algorithm is dominated by a logarithmic number of calls to a directed global
minimum cut subroutine -- if the running time of the latter problem improves to
$m^{1+o(1)}$ (thereby matching the running time of maximum flow), the running
time of our arboricity algorithm would improve further to $m^{1+o(1)}$.
We also give a new algorithm for computing the entire cut hierarchy --
laminar multiway cuts with minimum cut ratio in recursively defined induced
subgraphs -- in $m n^{1+o(1)}$ time. The cut hierarchy yields the ideal edge
loads (Thorup 2001) in a fractional spanning tree packing of the graph which,
we show, also corresponds to a max-entropy solution in the spanning tree
polytope. For the cut hierarchy problem, the previous best bound was
$\tilde{O}(n^2 m)$ for weighted graphs and $\tilde{O}(n m^{3/2})$ for
unweighted graphs.

[Read original post](http://arxiv.org/abs/2507.15598v1)
