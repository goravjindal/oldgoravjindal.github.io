---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Improved Algorithms for Kernel Matrix-Vector Multiplication Under"
date: 2025-08-01T00:00:00
---

**Authors:** [Piotr Indyk](https://dblp.uni-trier.de/search?q=Piotr+Indyk), [Michael Kapralov](https://dblp.uni-trier.de/search?q=Michael+Kapralov), [Kshiteej Sheth](https://dblp.uni-trier.de/search?q=Kshiteej+Sheth), [Tal Wagner](https://dblp.uni-trier.de/search?q=Tal+Wagner)

Motivated by the problem of fast processing of attention matrices, we study
fast algorithms for computing matrix-vector products for asymmetric Gaussian
Kernel matrices $K\in \mathbb{R}^{n\times n}$. $K$'s columns are indexed by a
set of $n$ keys $k\_1,k\_2\ldots, k\_n\in \mathbb{R}^d$, rows by a set of $n$
queries $q\_1,q\_2,\ldots,q\_n\in \mathbb{R}^d $, and its $i,j$ entry is $K\_{ij} =
e^{-\|q\_i-k\_j\|\_2^2/2\sigma^2}$ for some bandwidth parameter $\sigma>0$. Given
a vector $x\in \mathbb{R}^n$ and error parameter $\epsilon>0$, our task is to
output a $y\in \mathbb{R}^n$ such that $\|Kx-y\|\_2\leq \epsilon \|x\|\_2$ in
time subquadratic in $n$ and linear in $d$. Our algorithms rely on the
following modelling assumption about the matrices $K$: the sum of the entries
of $K$ scales linearly in $n$, as opposed to worst case quadratic growth. We
validate this assumption experimentally, for Gaussian kernel matrices
encountered in various settings such as fast attention computation in LLMs. We
obtain the first subquadratic-time algorithm that works under this assumption,
for unrestricted vectors.

[Read original post](http://arxiv.org/abs/2507.23539v1)
