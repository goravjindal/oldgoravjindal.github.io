---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Coloring 3-Colorable Graphs with Low Threshold Rank"
date: 2025-08-06T00:00:00
---

**Authors:** [Jun-Ting Hsieh](https://dblp.uni-trier.de/search?q=Jun-Ting+Hsieh)

We present a new algorithm for finding large independent sets in
$3$-colorable graphs with small $1$-sided threshold rank. Specifically, given
an $n$-vertex $3$-colorable graph whose uniform random walk matrix has at most
$r$ eigenvalues larger than $\varepsilon$, our algorithm finds a proper
$3$-coloring on at least $(\frac{1}{2}-O(\varepsilon))n$ vertices in time
$n^{O(r/\varepsilon^2)}$. This extends and improves upon the result of Bafna,
Hsieh, and Kothari on $1$-sided expanders. Furthermore, an independent work by
Buhai, Hua, Steurer, and V\'ari-Kakas shows that it is UG-hard to properly
$3$-color more than $(\frac{1}{2}+\varepsilon)n$ vertices, thus establishing
the tightness of our result.
Our proof is short and simple, relying on the observation that for any
distribution over proper $3$-colorings, the correlation across an edge must be
large if the marginals of the endpoints are not concentrated on any single
color. Notably, this property fails for $4$-colorings, which is consistent with
the hardness result of [BHK25] for $4$-colorable $1$-sided expanders.

[Read original post](http://arxiv.org/abs/2508.03093v1)
