---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: A Randomized Rounding Approach for DAG Edge Deletion"
date: 2025-07-11T00:00:00
---

**Authors:** [Sina Kalantarzadeh](https://dblp.uni-trier.de/search?q=Sina+Kalantarzadeh), [Nathan Klein](https://dblp.uni-trier.de/search?q=Nathan+Klein), [Victor Reis](https://dblp.uni-trier.de/search?q=Victor+Reis)

In the DAG Edge Deletion problem, we are given an edge-weighted directed
acyclic graph and a parameter $k$, and the goal is to delete the minimum weight
set of edges so that the resulting graph has no paths of length $k$. This
problem, which has applications to scheduling, was introduced in 2015 by
Kenkre, Pandit, Purohit, and Saket. They gave a $k$-approximation and showed
that it is UGC-Hard to approximate better than $\lfloor 0.5k \rfloor$ for any
constant $k \ge 4$ using a work of Svensson from 2012. The approximation ratio
was improved to $\frac{2}{3}(k+1)$ by Klein and Wexler in 2016.
In this work, we introduce a randomized rounding framework based on
distributions over vertex labels in $[0,1]$. The most natural distribution is
to sample labels independently from the uniform distribution over $[0,1]$. We
show this leads to a $(2-\sqrt{2})(k+1) \approx 0.585(k+1)$-approximation. By
using a modified (but still independent) label distribution, we obtain a
$0.549(k+1)$-approximation for the problem, as well as show that no independent
distribution over labels can improve our analysis to below $0.542(k+1)$.
Finally, we show a $0.5(k+1)$-approximation for bipartite graphs and for
instances with structured LP solutions. Whether this ratio can be obtained in
general is open.

[Read original post](http://arxiv.org/abs/2507.07943v1)
