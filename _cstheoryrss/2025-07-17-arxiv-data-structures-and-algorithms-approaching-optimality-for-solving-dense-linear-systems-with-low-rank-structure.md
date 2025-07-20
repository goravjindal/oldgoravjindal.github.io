---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Approaching Optimality for Solving Dense Linear Systems with Low-Rank"
date: 2025-07-17T00:00:00
---

**Authors:** [Michał Dereziński](https://dblp.uni-trier.de/search?q=Micha%C5%82+Derezi%C5%84ski), [Aaron Sidford](https://dblp.uni-trier.de/search?q=Aaron+Sidford)

We provide new high-accuracy randomized algorithms for solving linear systems
and regression problems that are well-conditioned except for $k$ large singular
values. For solving such $d \times d$ positive definite system our algorithms
succeed whp. and run in time $\tilde O(d^2 + k^\omega)$. For solving such
regression problems in a matrix $\mathbf{A} \in \mathbb{R}^{n \times d}$ our
methods succeed whp. and run in time $\tilde O(\mathrm{nnz}(\mathbf{A}) + d^2 +
k^\omega)$ where $\omega$ is the matrix multiplication exponent and
$\mathrm{nnz}(\mathbf{A})$ is the number of non-zeros in $\mathbf{A}$. Our
methods nearly-match a natural complexity limit under dense inputs for these
problems and improve upon a trade-off in prior approaches that obtain running
times of either $\tilde O(d^{2.065}+k^\omega)$ or $\tilde O(d^2 +
dk^{\omega-1})$ for $d\times d$ systems. Moreover, we show how to obtain these
running times even under the weaker assumption that all but $k$ of the singular
values have a suitably bounded generalized mean. Consequently, we give the
first nearly-linear time algorithm for computing a multiplicative approximation
to the nuclear norm of an arbitrary dense matrix. Our algorithms are built on
three general recursive preconditioning frameworks, where matrix sketching and
low-rank update formulas are carefully tailored to the problems' structure.

[Read original post](http://arxiv.org/abs/2507.11724v1)
