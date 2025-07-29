---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Fully Dynamic Spectral and Cut Sparsifiers for Directed Graphs"
date: 2025-07-29T00:00:00
---

**Authors:** [Yibin Zhao](https://dblp.uni-trier.de/search?q=Yibin+Zhao)

Recent years have seen extensive research on directed graph sparsification.
In this work, we initiate the study of fast fully dynamic spectral and cut
sparsification algorithms for directed graphs.
We introduce a new notion of spectral sparsification called degree-balance
preserving spectral approximation, which maintains the difference between the
in-degree and out-degree of each vertex. The approximation error is measured
with respect to the corresponding undirected Laplacian. This notion is
equivalent to direct Eulerian spectral approximation when the input graph is
Eulerian. Our algorithm achieves an amortized update time of
$O(\varepsilon^{-2} \cdot \text{polylog}(n))$ and produces a sparsifier of size
$O(\varepsilon^{-2} n \cdot \text{polylog}(n))$. Additionally, we present an
algorithm that maintains a constant-factor approximation sparsifier of size
$O(n \cdot \text{polylog}(n))$ against an adaptive adversary for
$O(\text{polylog}(n))$-partially symmetrized graphs, a notion introduced in
[Kyng-Meierhans-Probst Gutenberg '22]. A $\beta$-partial symmetrization of a
directed graph $\vec{G}$ is the union of $\vec{G}$ and $\beta \cdot G$, where
$G$ is the corresponding undirected graph of $\vec{G}$. This algorithm also
achieves a polylogarithmic amortized update time.
Moreover, we develop a fully dynamic algorithm for maintaining a cut
sparsifier for $\beta$-balanced directed graphs, where the ratio between
weighted incoming and outgoing edges of any cut is at most $\beta$. This
algorithm explicitly maintains a cut sparsifier of size
$O(\varepsilon^{-2}\beta n \cdot \text{polylog}(n))$ in worst-case update time
$O(\varepsilon^{-2}\beta \cdot \text{polylog}(n))$.

[Read original post](http://arxiv.org/abs/2507.19632v1)
