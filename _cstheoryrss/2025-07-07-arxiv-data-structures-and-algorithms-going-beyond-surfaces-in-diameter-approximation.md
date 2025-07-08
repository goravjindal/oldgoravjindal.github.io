---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Going Beyond Surfaces in Diameter Approximation"
date: 2025-07-07T00:00:00
---

**Authors:** [Michał Włodarczyk](https://dblp.uni-trier.de/search?q=Micha%C5%82+W%C5%82odarczyk)

Calculating the diameter of an undirected graph requires quadratic running
time under the Strong Exponential Time Hypothesis and this barrier works even
against any approximation better than 3/2. For planar graphs with positive edge
weights, there are known $(1+\varepsilon)$-approximation algorithms with
running time $poly(1/\epsilon, \log n) \cdot n$. However, these algorithms rely
on shortest path separators and this technique falls short to yield efficient
algorithms beyond graphs of bounded genus.
In this work we depart from embedding-based arguments and obtain diameter
approximations relying on VC set systems and the local treewidth property. We
present two orthogonal extensions of the planar case by giving
$(1+\varepsilon)$-approximation algorithms with the following running times:
1. $O\_h((1/\varepsilon)^{O(h)} \cdot n \log^2 n)$-time algorithm for graphs
excluding an apex graph of size h as a minor,
2. $O\_d((1/\varepsilon)^{O(d)} \cdot n \log^2 n)$-time algorithm for the
class of d-apex graphs.
As a stepping stone, we obtain efficient (1+\varepsilon)-approximate distance
oracles for graphs excluding an apex graph of size h as a minor. Our oracle has
preprocessing time $O\_h((1/\varepsilon)^8\cdot n \log n \log W)$ and query time
$O((1/\varepsilon)^2 \* \log n \log W)$, where $W$ is the metric stretch. Such
oracles have been so far only known for bounded genus graphs. All our
algorithms are deterministic.

[Read original post](http://arxiv.org/abs/2507.03447v1)
