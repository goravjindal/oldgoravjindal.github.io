---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: A Simple PTAS for Weighted k-means and Sensor Coverage"
date: 2025-08-11T00:00:00
---

**Authors:** [Akash Pareek](https://dblp.uni-trier.de/search?q=Akash+Pareek), [Supratim Shit](https://dblp.uni-trier.de/search?q=Supratim+Shit)

Clustering is a fundamental technique in data analysis, with the $k$-means
being one of the widely studied objectives due to its simplicity and broad
applicability. In many practical scenarios, data points come with associated
weights that reflect their importance, frequency, or confidence. Given a
weighted point set $P \subset R^d$, where each point $p \in P$ has a positive
weight $w\_p$, the goal is to compute a set of $k$ centers $C = \{ c\_1, c\_2,
\ldots, c\_k \} \subset R^d$ that minimizes the weighted clustering cost:
$\Delta\_w(P,C) = \sum\_{p \in P} w\_p \cdot d(p,C)^2$, where $d(p,C)$ denotes the
Euclidean distance from $p$ to its nearest center in $C$. Although most
existing coreset-based algorithms for $k$-means extend naturally to the
weighted setting and provide a PTAS, no prior work has offered a simple,
coreset-free PTAS designed specifically for the weighted $k$-means problem.
In this paper, we present a simple PTAS for weighted $k$-means that does not
rely on coresets. Building upon the framework of Jaiswal, Kumar, and Sen (2012)
for the unweighted case, we extend the result to the weighted setting by using
the weighted $D^2$-sampling technique. Our algorithm runs in time $n d \cdot
2^{O\left(\frac{k^2}{\epsilon}\right)}$ and outputs a set of $k$ centers whose
total clustering cost is within a $(1 + \epsilon)$-factor of the optimal cost.
As a key application of the weighted $k$-means, we obtain a PTAS for the sensor
coverage problem, which can also be viewed as a continuous locational
optimization problem. For this problem, the best-known result prior to our work
was an $O(\log k)$-approximation by Deshpande (2014), whereas our algorithm
guarantees a $(1 + \epsilon)$-approximation to the optimal coverage cost even
before applying refinement steps like Lloyd desent.

[Read original post](http://arxiv.org/abs/2508.06460v1)
