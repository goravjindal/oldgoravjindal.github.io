---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Deterministic Almost-Linear-Time Gomory-Hu Trees"
date: 2025-07-29T00:00:00
---

**Authors:** [Amir Abboud](https://dblp.uni-trier.de/search?q=Amir+Abboud), [Rasmus Kyng](https://dblp.uni-trier.de/search?q=Rasmus+Kyng), [Jason Li](https://dblp.uni-trier.de/search?q=Jason+Li), [Debmalya Panigrahi](https://dblp.uni-trier.de/search?q=Debmalya+Panigrahi), [Maximilian Probst Gutenberg](https://dblp.uni-trier.de/search?q=Maximilian+Probst+Gutenberg), [Thatchaphol Saranurak](https://dblp.uni-trier.de/search?q=Thatchaphol+Saranurak), [Weixuan Yuan](https://dblp.uni-trier.de/search?q=Weixuan+Yuan), [Wuwei Yuan](https://dblp.uni-trier.de/search?q=Wuwei+Yuan)

Given an $m$-edge, undirected, weighted graph $G=(V,E,w)$, a Gomory-Hu tree
$T$ (Gomory and Hu, 1961) is a tree over the vertex set $V$ such that all-pairs
mincuts in $G$ are preserved exactly in $T$.
In this article, we give the first almost-optimal $m^{1+o(1)}$-time
deterministic algorithm for constructing a Gomory-Hu tree. Prior to our work,
the best deterministic algorithm for this problem dated back to the original
algorithm of Gomory and Hu that runs in $nm^{1+o(1)}$ time (using current
maxflow algorithms). In fact, this is the first almost-linear time
deterministic algorithm for even simpler problems, such as finding the
$k$-edge-connected components of a graph.
Our new result hinges on two separate and novel components that each
introduce a distinct set of de-randomization tools of independent interest:
- a deterministic reduction from the all-pairs mincuts problem to the
single-souce mincuts problem incurring only subpolynomial overhead, and
- a deterministic almost-linear time algorithm for the single-source mincuts
problem.

[Read original post](http://arxiv.org/abs/2507.20354v1)
