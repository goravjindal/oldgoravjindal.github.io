---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Improved bicriteria approximation for $k$-edge-connectivity"
date: 2025-07-15T00:00:00
---

**Authors:** [Zeev Nutov](https://dblp.uni-trier.de/search?q=Zeev+Nutov)

In the $k$-Edge Connected Spanning Subgraph ($k$-ECSS) problem we are given a
(multi-)graph $G=(V,E)$ with edge costs and an integer $k$, and seek a min-cost
$k$-edge-connected spanning subgraph of $G$. The problem admits a
$2$-approximation algorithm and no better approximation ratio is
known.Hershkowitz, Klein, and Zenklusen [STOC 24] gave a bicriteria
$(1,k-10)$-approximation algorithm that computes a $(k-10)$-edge-connected
spanning subgraph of cost at most the optimal value of a standard Cut-LP for
$k$-ECSS. This LP bicriteria approximation was recently improved by Cohen and
Nutov [ESA 25] to $(1,k-4)$, where also was given a bicriteria approximation
$(3/2,k-2)$. In this paper we improve the bicriteria approximation to $(1,k-2)$
for $k$ even and to $\left(1-\frac{1}{k},k-3\right)$ for $k$ is odd, and also
give another bicriteria approximation $(3/2,k-1)$.
The $k$-Edge-Connected Spanning Multi-subgraph ($k$-ECSM) problem is almost
the same as $k$-ECSS, except that any edge can be selected multiple times at
the same cost. The previous best approximation ratio for $k$-ECSM was $1+4/k$.
Our result improves this to $1+\frac{2}{k}$ for $k$ even and to $1+\frac{3}{k}$
for $k$ odd, where for $k$ odd the computed subgraph is in fact
$(k+1)$-edge-connected.

[Read original post](http://arxiv.org/abs/2507.10125v1)
