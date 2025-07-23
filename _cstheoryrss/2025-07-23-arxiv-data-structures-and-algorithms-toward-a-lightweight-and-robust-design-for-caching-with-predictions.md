---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Toward a Lightweight and Robust Design for Caching with Predictions"
date: 2025-07-23T00:00:00
---

**Authors:** [Peng Chen](https://dblp.uni-trier.de/search?q=Peng+Chen), [Hailiang Zhao](https://dblp.uni-trier.de/search?q=Hailiang+Zhao), [Jiaji Zhang](https://dblp.uni-trier.de/search?q=Jiaji+Zhang), [Xueyan Tang](https://dblp.uni-trier.de/search?q=Xueyan+Tang), [Yixuan Wang](https://dblp.uni-trier.de/search?q=Yixuan+Wang), [Shuiguang Deng](https://dblp.uni-trier.de/search?q=Shuiguang+Deng)

The online caching problem aims to minimize cache misses when serving a
sequence of requests under a limited cache size. While naive learning-augmented
caching algorithms achieve ideal $1$-consistency, they lack robustness
guarantees. Existing robustification methods either sacrifice $1$-consistency
or introduce significant computational overhead. In this paper, we introduce
\textsc{Guard}, a lightweight robustification framework that enhances the
robustness of a broad class of learning-augmented caching algorithms to $2H\_k +
2$, while preserving their $1$-consistency. \textsc{Guard} achieves the current
best-known trade-off between consistency and robustness, with only
$\mathcal{O}(1)$ additional per-request overhead, thereby maintaining the
original time complexity of the base algorithm. Extensive experiments across
multiple real-world datasets and prediction models validate the effectiveness
of \textsc{Guard} in practice.

[Read original post](http://arxiv.org/abs/2507.16242v1)
