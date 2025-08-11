---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Debiasing Polynomial and Fourier Regression"
date: 2025-08-11T00:00:00
---

**Authors:** [Chris Camaño](https://dblp.uni-trier.de/search?q=Chris+Cama%C3%B1o), [Raphael A. Meyer](https://dblp.uni-trier.de/search?q=Raphael+A.+Meyer), [Kevin Shu](https://dblp.uni-trier.de/search?q=Kevin+Shu)

We study the problem of approximating an unknown function
$f:\mathbb{R}\to\mathbb{R}$ by a degree-$d$ polynomial using as few function
evaluations as possible, where error is measured with respect to a probability
distribution $\mu$. Existing randomized algorithms achieve near-optimal sample
complexities to recover a $ (1+\varepsilon) $-optimal polynomial but produce
biased estimates of the best polynomial approximation, which is undesirable.
We propose a simple debiasing method based on a connection between polynomial
regression and random matrix theory. Our method involves evaluating
$f(\lambda\_1),\ldots,f(\lambda\_{d+1})$ where $\lambda\_1,\ldots,\lambda\_{d+1}$
are the eigenvalues of a suitably designed random complex matrix tailored to
the distribution $\mu$. Our estimator is unbiased, has near-optimal sample
complexity, and experimentally outperforms iid leverage score sampling.
Additionally, our techniques enable us to debias existing methods for
approximating a periodic function with a truncated Fourier series with
near-optimal sample complexity.

[Read original post](http://arxiv.org/abs/2508.05920v1)
