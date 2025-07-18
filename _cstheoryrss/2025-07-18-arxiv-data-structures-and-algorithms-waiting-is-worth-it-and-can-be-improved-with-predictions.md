---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Waiting is worth it and can be improved with predictions"
date: 2025-07-18T00:00:00
---

**Authors:** [Ya-Chun Liang](https://dblp.uni-trier.de/search?q=Ya-Chun+Liang), [Meng-Hsi Li](https://dblp.uni-trier.de/search?q=Meng-Hsi+Li), [Chung-Shou Liao](https://dblp.uni-trier.de/search?q=Chung-Shou+Liao), [Clifford Stein](https://dblp.uni-trier.de/search?q=Clifford+Stein)

We revisit the well-known online traveling salesman problem (OLTSP) and its
extension, the online dial-a-ride problem (OLDARP). A server starting at a
designated origin in a metric space, is required to serve online requests, and
return to the origin such that the completion time is minimized. The SmartStart
algorithm, introduced by Ascheuer et al., incorporates a waiting approach into
an online schedule-based algorithm and attains the optimal upper bound of 2 for
the OLTSP and the OLDARP if each schedule is optimal. Using the Christofides'
heuristic to approximate each schedule leads to the currently best upper bound
of (7 + sqrt(13)) / 4 approximately 2.6514 in polynomial time.
In this study, we investigate how an online algorithm with predictions, a
recent popular framework (i.e. the so-called learning-augmented algorithms),
can be used to improve the best competitive ratio in polynomial time. In
particular, we develop a waiting strategy with online predictions, each of
which is only a binary decision-making for every schedule in a whole route,
rather than forecasting an entire set of requests in the beginning (i.e.
offline predictions). That is, it does not require knowing the number of
requests in advance. The proposed online schedule-based algorithm can achieve
1.1514 \* lambda + 1.5-consistency and 1.5 + 1.5 / (2.3028 \* lambda -
1)-robustness in polynomial time, where lambda lies in the interval (1/theta,
1] and theta is set to (1 + sqrt(13)) / 2 approximately 2.3028. The best
consistency tends to approach to 2 when lambda is close to 1/theta. Meanwhile,
we show any online schedule-based algorithms cannot derive a competitive ratio
of less than 2 even with perfect online predictions.

[Read original post](http://arxiv.org/abs/2507.12822v1)
