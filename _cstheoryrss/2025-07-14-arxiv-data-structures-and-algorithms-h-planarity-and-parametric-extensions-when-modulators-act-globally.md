---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: H-Planarity and Parametric Extensions: when Modulators Act Globally"
date: 2025-07-14T00:00:00
---

**Authors:** [Fedor V. Fomin](https://dblp.uni-trier.de/search?q=Fedor+V.+Fomin), [Petr A. Golovach](https://dblp.uni-trier.de/search?q=Petr+A.+Golovach), [Laure Morelle](https://dblp.uni-trier.de/search?q=Laure+Morelle), [Dimitrios M. Thilikos](https://dblp.uni-trier.de/search?q=Dimitrios+M.+Thilikos)

We introduce a series of graph decompositions based on the modulator/target
scheme of modification problems that enable several algorithmic applications
that parametrically extend the algorithmic potential of planarity. In the core
of our approach is a polynomial time algorithm for computing planar
H-modulators. Given a graph class H, a planar H-modulator of a graph G is a set
X \subseteq V(G) such that the ``torso'' of X is planar and all connected
components of G - X belong to H. Here, the torso of X is obtained from G[X] if,
for every connected component of G-X, we form a clique out of its neighborhood
on G[X]. We introduce H-Planarity as the problem of deciding whether a graph G
has a planar H-modulator. We prove that, if H is hereditary, CMSO-definable,
and decidable in polynomial time, then H-Planarity is solvable in polynomial
time. Further, we introduce two parametric extensions of H-Planarity by
defining the notions of H-planar treedepth and H-planar treewidth, which
generalize the concepts of elimination distance and tree decompositions to the
class H. Combining this result with existing FPT algorithms for various
H-modulator problems, we thereby obtain FPT algorithms parameterized by
H-planar treedepth and H-planar treewidth for numerous graph classes H. By
combining the well-known algorithmic properties of planar graphs and graphs of
bounded treewidth, our methods for computing H-planar treedepth and H-planar
treewidth lead to a variety of algorithmic applications. For instance, once we
know that a given graph has bounded H-planar treedepth or bounded H-planar
treewidth, we can derive additive approximation algorithms for graph coloring
and polynomial-time algorithms for counting (weighted) perfect matchings.
Furthermore, we design Efficient Polynomial-Time Approximation Schemes
(EPTAS-es) for several problems, including Maximum Independent Set.

[Read original post](http://arxiv.org/abs/2507.08541v1)
