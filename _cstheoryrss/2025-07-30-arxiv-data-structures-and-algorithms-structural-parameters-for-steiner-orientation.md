---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Structural Parameters for Steiner Orientation"
date: 2025-07-30T00:00:00
---

**Authors:** [Tesshu Hanaka](https://dblp.uni-trier.de/search?q=Tesshu+Hanaka), [Michael Lampis](https://dblp.uni-trier.de/search?q=Michael+Lampis), [Nikolaos Melissinos](https://dblp.uni-trier.de/search?q=Nikolaos+Melissinos), [Edouard Nemery](https://dblp.uni-trier.de/search?q=Edouard+Nemery), [Hirotaka Ono](https://dblp.uni-trier.de/search?q=Hirotaka+Ono), [Manolis Vasilakis](https://dblp.uni-trier.de/search?q=Manolis+Vasilakis)

We consider the \textsc{Steiner Orientation} problem, where we are given as
input a mixed graph $G=(V,E,A)$ and a set of $k$ demand pairs $(s\_i,t\_i)$,
$i\in[k]$. The goal is to orient the undirected edges of $G$ in a way that the
resulting directed graph has a directed path from $s\_i$ to $t\_i$ for all
$i\in[k]$. We adopt the point of view of structural parameterized complexity
and investigate the complexity of \textsc{Steiner Orientation} for standard
measures, such as treewidth. Our results indicate that \textsc{Steiner
Orientation} is a surprisingly hard problem from this point of view. In
particular, our main contributions are the following: (1) We show that
\textsc{Steiner Orientation} is NP-complete on instances where the underlying
graph has feedback vertex number 2, treewidth 2, pathwidth 3, and vertex
integrity 6; (2) We present an XP algorithm parameterized by vertex cover
number $\mathrm{vc}$ of complexity $n^{\mathcal{O}(\mathrm{vc}^2)}$.
Furthermore, we show that this running time is essentially optimal by proving
that a running time of $n^{o(\mathrm{vc}^2)}$ would refute the ETH; (3) We
consider parameterizations by the number of undirected or directed edges ($|E|$
or $|A|$) and we observe that the trivial $2^{|E|}n^{\mathcal{O}(1)}$-time
algorithm for the former parameter is optimal under the SETH. Complementing
this, we show that the problem admits a
$2^{\mathcal{O}(|A|)}n^{\mathcal{O}(1)}$-time algorithm. In addition to the
above, we consider the complexity of \textsc{Steiner Orientation} parameterized
by $\mathrm{tw}+k$ (FPT), distance to clique (FPT), and $\mathrm{vc}+k$ (FPT
with a polynomial kernel).

[Read original post](http://arxiv.org/abs/2507.21445v1)
