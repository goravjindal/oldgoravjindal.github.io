---
layout: post
category: cstheoryrss
title: "arXiv: Computational Geometry: Topolow: Force-Directed Euclidean Embedding of Dissimilarity Data with"
date: 2025-08-05T00:00:00
---

**Authors:** [Omid Arhami](https://dblp.uni-trier.de/search?q=Omid+Arhami), [Pejman Rohani](https://dblp.uni-trier.de/search?q=Pejman+Rohani)

The problem of embedding a set of objects into a low-dimensional Euclidean
space based on a matrix of pairwise dissimilarities is fundamental in data
analysis, machine learning, and statistics. However, the assumptions of many
standard analytical methods are violated when the input dissimilarities fail to
satisfy metric or Euclidean axioms. We present the mathematical and statistical
foundations of Topolow, a physics-inspired, gradient-free optimization
framework for such embedding problems. Topolow is conceptually related to
force-directed graph drawing algorithms but is fundamentally distinguished by
its goal of quantitative metric reconstruction. It models objects as particles
in a physical system, and its novel optimization scheme proceeds through
sequential, stochastic pairwise interactions, which circumvents the need to
compute a global gradient and provides robustness against convergence to local
optima, especially for sparse data. Topolow maximizes the likelihood under a
Laplace error model, robust to outliers and heterogeneous errors, and properly
handles censored data. Crucially, Topolow does not require the input
dissimilarities to be metric, making it a robust solution for embedding
non-metric measurements into a valid Euclidean space, thereby enabling the use
of standard analytical tools. We demonstrate the superior performance of
Topolow compared to standard Multidimensional Scaling (MDS) methods in
reconstructing the geometry of sparse and non-Euclidean data. This paper
formalizes the algorithm, first introduced as Topolow in the context of
antigenic mapping in (Arhami and Rohani, 2025) (open access), with emphasis on
its metric embedding and mathematical properties for a broader audience. The
general-purpose function Euclidify is available in the R package topolow.

[Read original post](http://arxiv.org/abs/2508.01733v1)
