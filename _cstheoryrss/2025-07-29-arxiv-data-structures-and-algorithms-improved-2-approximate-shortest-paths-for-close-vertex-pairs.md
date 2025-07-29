---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Improved 2-Approximate Shortest Paths for close vertex pairs"
date: 2025-07-29T00:00:00
---

**Authors:** [Manoj Gupta](https://dblp.uni-trier.de/search?q=Manoj+Gupta)

An influential result by Dor, Halperin, and Zwick (FOCS 1996, SICOMP 2000)
implies an algorithm that can compute approximate shortest paths for all vertex
pairs in $\tilde{O}(n^{2+O\left(\frac{1}{k}\right )})$ time, ensuring that the
output distance is at most twice the actual shortest path, provided the pairs
are at least $k$ apart, where $k \ge 2$. We present the first improvement on
this result in over 25 years. Our algorithm achieves roughly same
$\tilde{O}(n^{2+\frac{1}{k}})$ runtime but applies to vertex pairs merely
$O(\log k)$ apart, where $\log k \ge 1$. When $k=\log n$, the running time of
our algorithm is $\tilde{O}(n^2)$ and it works for all pairs at least $O(\log
\log n)$ apart. Our algorithm is combinatorial, randomized, and returns correct
results for all pairs with a high probability.

[Read original post](http://arxiv.org/abs/2507.19859v1)
