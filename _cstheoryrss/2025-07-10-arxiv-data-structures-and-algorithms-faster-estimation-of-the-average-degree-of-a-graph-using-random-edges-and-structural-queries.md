---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Faster Estimation of the Average Degree of a Graph Using Random Edges"
date: 2025-07-10T00:00:00
---

**Authors:** [Lorenzo Beretta](https://dblp.uni-trier.de/search?q=Lorenzo+Beretta), [Deeparnab Chakrabarty](https://dblp.uni-trier.de/search?q=Deeparnab+Chakrabarty), [C. Seshadhri](https://dblp.uni-trier.de/search?q=C.+Seshadhri)

We revisit the problem of designing sublinear algorithms for estimating the
average degree of an $n$-vertex graph. The standard access model for graphs
allows for the following queries: sampling a uniform random vertex, the degree
of a vertex, sampling a uniform random neighbor of a vertex, and ``pair
queries'' which determine if a pair of vertices form an edge. In this model,
original results [Goldreich-Ron, RSA 2008; Eden-Ron-Seshadhri, SIDMA 2019] on
this problem prove that the complexity of getting
$(1+\varepsilon)$-multiplicative approximations to the average degree, ignoring
$\varepsilon$-dependencies, is $\Theta(\sqrt{n})$. When random edges can be
sampled, it is known that the average degree can estimated in
$\widetilde{O}(n^{1/3})$ queries, even without pair queries
[Motwani-Panigrahy-Xu, ICALP 2007; Beretta-Tetek, TALG 2024].
We give a nearly optimal algorithm in the standard access model with random
edge samples. Our algorithm makes $\widetilde{O}(n^{1/4})$ queries exploiting
the power of pair queries. We also analyze the ``full neighborhood access"
model wherein the entire adjacency list of a vertex can be obtained with a
single query; this model is relevant in many practical applications. In a
weaker version of this model, we give an algorithm that makes
$\widetilde{O}(n^{1/5})$ queries. Both these results underscore the power of
{\em structural queries}, such as pair queries and full neighborhood access
queries, for estimating the average degree. We give nearly matching lower
bounds, ignoring $\varepsilon$-dependencies, for all our results.
So far, almost all algorithms for estimating average degree assume that the
number of vertices, $n$, is known. Inspired by [Beretta-Tetek, TALG 2024], we
study this problem when $n$ is unknown and show that structural queries do not
help in estimating average degree in this setting.

[Read original post](http://arxiv.org/abs/2507.06925v1)
