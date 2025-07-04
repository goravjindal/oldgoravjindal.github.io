---
layout: post
nav: true
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Dynamic Similarity Graph Construction with Kernel Density Estimation"
date: 2025-07-03T00:00:00
---

**Authors:** [Steinar Laenen](https://dblp.uni-trier.de/search?q=Steinar+Laenen), [Peter Macgregor](https://dblp.uni-trier.de/search?q=Peter+Macgregor), [He Sun](https://dblp.uni-trier.de/search?q=He+Sun)

In the kernel density estimation (KDE) problem, we are given a set $X$ of
data points in $\mathbb{R}^d$, a kernel function $k: \mathbb{R}^d \times
\mathbb{R}^d \rightarrow \mathbb{R}$, and a query point $\mathbf{q} \in
\mathbb{R}^d$, and the objective is to quickly output an estimate of
$\sum\_{\mathbf{x} \in X} k(\mathbf{q}, \mathbf{x})$. In this paper, we consider
$\textsf{KDE}$ in the dynamic setting, and introduce a data structure that
efficiently maintains the estimates for a set of query points as data points
are added to $X$ over time. Based on this, we design a dynamic data structure
that maintains a sparse approximation of the fully connected similarity graph
on $X$, and develop a fast dynamic spectral clustering algorithm. We further
evaluate the effectiveness of our algorithms on both synthetic and real-world
datasets.

[Read original post](http://arxiv.org/abs/2507.01696v1)
