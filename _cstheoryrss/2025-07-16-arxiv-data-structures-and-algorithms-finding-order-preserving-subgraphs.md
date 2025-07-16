---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Finding Order-Preserving Subgraphs"
date: 2025-07-16T00:00:00
---

**Authors:** [Haruya Imamura](https://dblp.uni-trier.de/search?q=Haruya+Imamura), [Yasuaki Kobayashi](https://dblp.uni-trier.de/search?q=Yasuaki+Kobayashi), [Yota Otachi](https://dblp.uni-trier.de/search?q=Yota+Otachi), [Toshiki Saitoh](https://dblp.uni-trier.de/search?q=Toshiki+Saitoh), [Keita Sato](https://dblp.uni-trier.de/search?q=Keita+Sato), [Asahi Takaoka](https://dblp.uni-trier.de/search?q=Asahi+Takaoka), [Ryo Yoshinaka](https://dblp.uni-trier.de/search?q=Ryo+Yoshinaka)

(Induced) Subgraph Isomorphism and Maximum Common (Induced) Subgraph are
fundamental problems in graph pattern matching and similarity computation. In
graphs derived from time-series data or protein structures, a natural total
ordering of vertices often arises from their underlying structure, such as
temporal sequences or amino acid sequences. This motivates the study of problem
variants that respect this inherent ordering. This paper addresses Ordered
(Induced) Subgraph Isomorphism (O(I)SI) and its generalization, Maximum Common
Ordered (Induced) Subgraph (MCO(I)S), which seek to find subgraph isomorphisms
that preserve the vertex orderings of two given ordered graphs. Our main
contributions are threefold: (1) We prove that these problems remain
NP-complete even when restricted to small graph classes, such as trees of depth
2 and threshold graphs. (2) We establish a gap in computational complexity
between OSI and OISI on certain graph classes. For instance, OSI is
polynomial-time solvable for interval graphs with their interval orderings,
whereas OISI remains NP-complete under the same setting. (3) We demonstrate
that the tractability of these problems can depend on the vertex ordering. For
example, while OISI is NP-complete on threshold graphs, its generalization,
MCOIS, can be solved in polynomial time if the specific vertex orderings that
characterize the threshold graphs are provided.

[Read original post](http://arxiv.org/abs/2507.11115v1)
