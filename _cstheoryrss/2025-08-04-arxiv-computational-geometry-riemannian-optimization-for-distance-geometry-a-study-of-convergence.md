---
layout: post
category: cstheoryrss
title: "arXiv: Computational Geometry: Riemannian Optimization for Distance Geometry: A Study of Convergence,"
date: 2025-08-04T00:00:00
---

**Authors:** [Chandler Smith](https://dblp.uni-trier.de/search?q=Chandler+Smith), [HanQin Cai](https://dblp.uni-trier.de/search?q=HanQin+Cai), [Abiy Tasissa](https://dblp.uni-trier.de/search?q=Abiy+Tasissa)

The problem of recovering a configuration of points from partial pairwise
distances, referred to as the Euclidean Distance Geometry (EDG) problem, arises
in a broad range of applications, including sensor network localization,
molecular conformation, and manifold learning. In this paper, we propose a
Riemannian optimization framework for solving the EDG problem by formulating it
as a low-rank matrix completion task over the space of positive semi-definite
Gram matrices. The available distance measurements are encoded as expansion
coefficients in a non-orthogonal basis, and optimization over the Gram matrix
implicitly enforces geometric consistency through the triangle inequality, a
structure inherited from classical multidimensional scaling. Under a Bernoulli
sampling model for observed distances, we prove that Riemannian gradient
descent on the manifold of rank-$r$ matrices locally converges linearly with
high probability when the sampling probability satisfies $p \geq
\mathcal{O}(\nu^2 r^2 \log(n)/n)$, where $\nu$ is an EDG-specific incoherence
parameter. Furthermore, we provide an initialization candidate using a one-step
hard thresholding procedure that yields convergence, provided the sampling
probability satisfies $p \geq \mathcal{O}(\nu r^{3/2} \log^{3/4}(n)/n^{1/4})$.
A key technical contribution of this work is the analysis of a symmetric linear
operator arising from a dual basis expansion in the non-orthogonal basis, which
requires a novel application of the Hanson--Wright inequality to establish an
optimal restricted isometry property in the presence of coupled terms.
Empirical evaluations on synthetic data demonstrate that our algorithm achieves
competitive performance relative to state-of-the-art methods. Moreover, we
propose a novel notion of matrix incoherence tailored to the EDG setting and
provide robustness guarantees for our method.

[Read original post](http://arxiv.org/abs/2508.00091v1)
