---
layout: post
nav: true
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Numerical Linear Algebra in Linear Space"
date: 2025-07-04T00:00:00
---

**Authors:** [Yiping Liu](https://dblp.uni-trier.de/search?q=Yiping+Liu), [Hoai-An Nguyen](https://dblp.uni-trier.de/search?q=Hoai-An+Nguyen), [Junzhao Yang](https://dblp.uni-trier.de/search?q=Junzhao+Yang)

We present a randomized linear-space solver for general linear systems
$\mathbf{A} \mathbf{x} = \mathbf{b}$ with $\mathbf{A} \in \mathbb{Z}^{n \times
n}$ and $\mathbf{b} \in \mathbb{Z}^n$, without any assumption on the condition
number of $\mathbf{A}$. For matrices whose entries are bounded by
$\mathrm{poly}(n)$, the solver returns a $(1+\epsilon)$-multiplicative
entry-wise approximation to vector $\mathbf{x} \in \mathbb{Q}^{n}$ using
$\widetilde{O}(n^2 \cdot \mathrm{nnz}(\mathbf{A}))$ bit operations and $O(n
\log n)$ bits of working space (i.e., linear in the size of a vector), where
$\mathrm{nnz}$ denotes the number of nonzero entries. Our solver works for
right-hand vector $\mathbf{b}$ with entries up to $n^{O(n)}$. To our knowledge,
this is the first linear-space linear system solver over the rationals that
runs in $\widetilde{O}(n^2 \cdot \mathrm{nnz}(\mathbf{A}))$ time.
We also present several applications of our solver to numerical linear
algebra problems, for which we provide algorithms with efficient polynomial
running time and near-linear space. In particular, we present results for
linear regression, linear programming, eigenvalues and eigenvectors, and
singular value decomposition.

[Read original post](http://arxiv.org/abs/2507.02433v1)
