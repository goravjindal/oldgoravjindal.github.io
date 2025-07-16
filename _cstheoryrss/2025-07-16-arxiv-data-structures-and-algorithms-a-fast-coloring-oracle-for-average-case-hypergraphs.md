---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: A Fast Coloring Oracle for Average Case Hypergraphs"
date: 2025-07-16T00:00:00
---

**Authors:** [Cassandra Marcussen](https://dblp.uni-trier.de/search?q=Cassandra+Marcussen), [Edward Pyne](https://dblp.uni-trier.de/search?q=Edward+Pyne), [Ronitt Rubinfeld](https://dblp.uni-trier.de/search?q=Ronitt+Rubinfeld), [Asaf Shapira](https://dblp.uni-trier.de/search?q=Asaf+Shapira), [Shlomo Tauber](https://dblp.uni-trier.de/search?q=Shlomo+Tauber)

Hypergraph $2$-colorability is one of the classical NP-hard problems. Person
and Schacht [SODA'09] designed a deterministic algorithm whose expected running
time is polynomial over a uniformly chosen $2$-colorable $3$-uniform
hypergraph. Lee, Molla, and Nagle recently extended this to $k$-uniform
hypergraphs for all $k\geq 3$. Both papers relied heavily on the regularity
lemma, hence their analysis was involved and their running time hid tower-type
constants.
Our first result in this paper is a new simple and elementary deterministic
$2$-coloring algorithm that reproves the theorems of Person-Schacht and
Lee-Molla-Nagle while avoiding the use of the regularity lemma. We also show
how to turn our new algorithm into a randomized one with average expected
running time of only $O(n)$.
Our second and main result gives what we consider to be the ultimate evidence
of just how easy it is to find a $2$-coloring of an average $2$-colorable
hypergraph. We define a coloring oracle to be an algorithm which, given vertex
$v$, assigns color red/blue to $v$ while inspecting as few edges as possible,
so that the answers to any sequence of queries to the oracle are consistent
with a single legal $2$-coloring of the input. Surprisingly, we show that there
is a coloring oracle that, on average, can answer every vertex query in time
$O(1)$.

[Read original post](http://arxiv.org/abs/2507.10691v1)
