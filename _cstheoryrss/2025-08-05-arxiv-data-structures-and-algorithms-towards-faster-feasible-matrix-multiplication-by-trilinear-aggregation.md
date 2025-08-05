---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Towards Faster Feasible Matrix Multiplication by Trilinear Aggregation"
date: 2025-08-05T00:00:00
---

**Authors:** [Oded Schwartz](https://dblp.uni-trier.de/search?q=Oded+Schwartz), [Eyal Zwecher](https://dblp.uni-trier.de/search?q=Eyal+Zwecher)

Matrix multiplication is a fundamental kernel in high performance computing.
Many algorithms for fast matrix multiplication can only be applied to enormous
matrices ($n>10^{100}$) and thus cannot be used in practice. Of all algorithms
applicable to feasible input, Pan's $O(n^{2.773372})$ algorithm (1982) is
asymptotically the fastest. We obtain an $O(n^{2.773203})$ algorithm applicable
to the same input sizes as Pan's algorithm. This algorithm is the fastest
matrix multiplication algorithm with base case smaller than $1000$. Further,
our method obtains the best asymptotic complexity for many small base cases,
starting at $n\_0=28$. We also obtain better exponents for larger base cases. To
construct our algorithm, we use the trilinear aggregation method. We find parts
of the algorithms that are equivalent to matrix multiplication with smaller
base case, and use the de Groote equivalence to replace these parts in a way
that allows further optimization of our algorithms. Finally, we improve the
additive complexity of our algorithms by finding a sparse decomposition and
reducing the leading coefficient. These mark a fundamental step towards
outperforming existing fast matrix multiplication algorithms in practice.

[Read original post](http://arxiv.org/abs/2508.01748v1)
