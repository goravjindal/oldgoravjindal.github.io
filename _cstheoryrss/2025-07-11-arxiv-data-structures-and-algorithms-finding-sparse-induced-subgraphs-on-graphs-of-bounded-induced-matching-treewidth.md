---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Finding sparse induced subgraphs on graphs of bounded induced matching"
date: 2025-07-11T00:00:00
---

**Authors:** [Hans L. Bodlaender](https://dblp.uni-trier.de/search?q=Hans+L.+Bodlaender), [Fedor V. Fomin](https://dblp.uni-trier.de/search?q=Fedor+V.+Fomin), [Tuukka Korhonen](https://dblp.uni-trier.de/search?q=Tuukka+Korhonen)

The induced matching width of a tree decomposition of a graph $G$ is the
cardinality of a largest induced matching $M$ of $G$, such that there exists a
bag that intersects every edge in $M$. The induced matching treewidth of a
graph $G$, denoted by $\mathsf{tree-}\mu(G)$, is the minimum induced matching
width of a tree decomposition of $G$. The parameter $\mathsf{tree-}\mu$ was
introduced by Yolov [SODA '18], who showed that, for example, Maximum-Weight
Independent Set can be solved in polynomial-time on graphs of bounded
$\mathsf{tree-}\mu$. Lima, Milani\v{c}, Mur\v{s}i\v{c}, Okrasa,
Rz\k{a}\.zewski, and \v{S}torgel [ESA '24] conjectured that this algorithm can
be generalized to a meta-problem called Maximum-Weight Induced Subgraph of
Bounded Treewidth, where we are given a vertex-weighted graph $G$, an integer
$w$, and a $\mathsf{CMSO}\_2$-sentence $\Phi$, and are asked to find a
maximum-weight set $X \subseteq V(G)$ so that $G[X]$ has treewidth at most $w$
and satisfies $\Phi$. They proved the conjecture for some special cases, such
as for the problem Maximum-Weight Induced Forest.
In this paper, we prove the general case of the conjecture. In particular, we
show that Maximum-Weight Induced Subgraph of Bounded Treewidth is
polynomial-time solvable when $\mathsf{tree-}\mu(G)$, $w$, and $|\Phi|$ are
bounded. The running time of our algorithm for $n$-vertex graphs $G$ with
$\mathsf{tree} - \mu(G) \le k$ is $f(k, w, |\Phi|) \cdot n^{O(k w^2)}$ for a
computable function $f$.

[Read original post](http://arxiv.org/abs/2507.07975v1)
