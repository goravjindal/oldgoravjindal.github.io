---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Decoupling via Affine Spectral-Independence: Beck-Fiala and Komls"
date: 2025-08-07T00:00:00
---

**Authors:** [Nikhil Bansal](https://dblp.uni-trier.de/search?q=Nikhil+Bansal), [Haotian Jiang](https://dblp.uni-trier.de/search?q=Haotian+Jiang)

The Beck-Fiala Conjecture [Discrete Appl. Math, 1981] asserts that any set
system of $n$ elements with degree $k$ has combinatorial discrepancy
$O(\sqrt{k})$. A substantial generalization is the Koml\'os Conjecture, which
states that any $m \times n$ matrix with unit length columns has discrepancy
$O(1)$.
In this work, we resolve the Beck-Fiala Conjecture for $k \geq \log^2 n$. We
also give an $\widetilde{O}(\sqrt{k} + \sqrt{\log n})$ bound for $k \leq \log^2
n$, where $\widetilde{O}(\cdot)$ hides $\mathsf{poly}(\log \log n)$ factors.
These bounds improve upon the $O(\sqrt{k \log n})$ bound due to Banaszczyk
[Random Struct. Algor., 1998].
For the Komlos problem, we give an $\widetilde{O}(\log^{1/4} n)$ bound,
improving upon the previous $O(\sqrt{\log n})$ bound [Random Struct. Algor.,
1998]. All of our results also admit efficient polynomial-time algorithms.
To obtain these results, we consider a new notion of affine
spectral-independence in designing random walks. In particular, our algorithms
obtain the desired colorings via a discrete Brownian motion, guided by a
semidefinite program (SDP). Besides standard constraints used in prior works,
we add some extra affine spectral-independence constraints, which effectively
decouple the evolution of discrepancy across different rows, and allow us to
better control how many rows accumulate large discrepancy at any point during
the process. This technique of ``decoupling via affine spectral-independence''
is quite general and may be of independent interest.

[Read original post](http://arxiv.org/abs/2508.03961v1)
