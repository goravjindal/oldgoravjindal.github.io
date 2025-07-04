---
layout: post
nav: true
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Online Conformal Prediction with Efficiency Guarantees"
date: 2025-07-04T00:00:00
---

**Authors:** [Vaidehi Srinivas](https://dblp.uni-trier.de/search?q=Vaidehi+Srinivas)

We study the problem of conformal prediction in a novel online framework that
directly optimizes efficiency. In our problem, we are given a target
miscoverage rate $\alpha > 0$, and a time horizon $T$. On each day $t \le T$ an
algorithm must output an interval $I\_t \subseteq [0, 1]$, then a point $y\_t \in
[0, 1]$ is revealed. The goal of the algorithm is to achieve coverage, that is,
$y\_t \in I\_t$ on (close to) a $(1 - \alpha)$-fraction of days, while
maintaining efficiency, that is, minimizing the average volume (length) of the
intervals played. This problem is an online analogue to the problem of
constructing efficient confidence intervals.
We study this problem over arbitrary and exchangeable (random order) input
sequences. For exchangeable sequences, we show that it is possible to construct
intervals that achieve coverage $(1 - \alpha) - o(1)$, while having length
upper bounded by the best fixed interval that achieves coverage in hindsight.
For arbitrary sequences however, we show that any algorithm that achieves a
$\mu$-approximation in average length compared to the best fixed interval
achieving coverage in hindsight, must make a multiplicative factor more
mistakes than $\alpha T$, where the multiplicative factor depends on $\mu$ and
the aspect ratio of the problem. Our main algorithmic result is a matching
algorithm that can recover all Pareto-optimal settings of $\mu$ and number of
mistakes. Furthermore, our algorithm is deterministic and therefore robust to
an adaptive adversary.
This gap between the exchangeable and arbitrary settings is in contrast to
the classical online learning problem. In fact, we show that no single
algorithm can simultaneously be Pareto-optimal for arbitrary sequences and
optimal for exchangeable sequences. On the algorithmic side, we give an
algorithm that achieves the near-optimal tradeoff between the two cases.

[Read original post](http://arxiv.org/abs/2507.02496v1)
