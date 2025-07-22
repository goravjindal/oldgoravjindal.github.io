---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Job Scheduling under Base and Additional Fees, with Applications to"
date: 2025-07-22T00:00:00
---

**Authors:** [Yi-Ting Hsieh](https://dblp.uni-trier.de/search?q=Yi-Ting+Hsieh), [Mong-Jen Kao](https://dblp.uni-trier.de/search?q=Mong-Jen+Kao), [Jhong-Yun Liu](https://dblp.uni-trier.de/search?q=Jhong-Yun+Liu), [Hung-Lung Wang](https://dblp.uni-trier.de/search?q=Hung-Lung+Wang)

We are concerned with the problem of scheduling $n$ jobs onto $m$ identical
machines. Each machine has to be in operation for a prescribed time, and the
objective is to minimize the total machine working time. Precisely, let $c\_i$
be the prescribed time for machine $i$, where $i\in[m]$, and $p\_j$ be the
processing time for job $j$, where $j\in[n]$. The problem asks for a schedule
$\sigma\colon\, J\to M$ such that $\sum\_{i=1}^m\max\{c\_i,
\sum\_{j\in\sigma^{-1}(i)}p\_j\}$ is minimized, where $J$ and $M$ denote the sets
of jobs and machines, respectively. We show that First Fit Decreasing (FFD)
leads to a $1.5$-approximation, and this problem admits a polynomial-time
approximation scheme (PTAS). The idea is further applied to mixed-criticality
system scheduling to yield improved approximation results.

[Read original post](http://arxiv.org/abs/2507.15434v1)
