---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: An n{O(loglog n)} time approximation scheme for capacitated VRP in"
date: 2025-07-22T00:00:00
---

**Authors:** [René Sitters](https://dblp.uni-trier.de/search?q=Ren%C3%A9+Sitters)

We present a quasi polynomial time approximation scheme (Q-PTAS) for the
capacitated vehicle routing problem (CVRP) on $n$ points in the Euclidean plane
for arbitrary capacity $c$. The running time is $n^{f(\epsilon)\cdot\log\log
n}$ for any $c$, and where $f$ is a function of $\epsilon$ only. This is a
major improvement over the so far best known running time of
$n^{\log^{O(1/\epsilon)}n}$ time and a big step towards a PTAS for Euclidean
CVRP.
In our algorithm, we first give a polynomial time reduction of the CVRP in
$\mathbb{R}^d$ (for any fixed $d$) to an uncapacitated routing problem in
$\mathbb{R}^d$ that we call the $m$-paths problem. Here, one needs to find
exactly $m$ paths between two points $a$ and $b$, covering all the given points
in the Euclidean space. We then give a Q-PTAS for the $m$-paths problem in the
pane. Any PTAS for the (arguably easier to handle) Euclidean $m$-paths problem
is most likely to imply a PTAS for the Euclidean CVRP.

[Read original post](http://arxiv.org/abs/2507.15549v1)
