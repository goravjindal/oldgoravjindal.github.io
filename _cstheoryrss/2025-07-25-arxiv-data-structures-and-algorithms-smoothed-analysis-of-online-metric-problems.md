---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Smoothed Analysis of Online Metric Problems"
date: 2025-07-25T00:00:00
---

**Authors:** [Christian Coester](https://dblp.uni-trier.de/search?q=Christian+Coester), [Jack Umenberger](https://dblp.uni-trier.de/search?q=Jack+Umenberger)

We study three classical online problems -- $k$-server, $k$-taxi, and chasing
size $k$ sets -- through a lens of smoothed analysis. Our setting allows
request locations to be adversarial up to small perturbations, interpolating
between worst-case and average-case models. Specifically, we show that if the
metric space is contained in a ball in any normed space and requests are drawn
from distributions whose density functions are upper bounded by $1/\sigma$
times the uniform density over the ball, then all three problems admit
polylog$(k/\sigma)$-competitive algorithms. Our approach is simple: it reduces
smoothed instances to fully adversarial instances on finite metrics and
leverages existing algorithms in a black-box manner. We also provide a lower
bound showing that no algorithm can achieve a competitive ratio
sub-polylogarithmic in $k/\sigma$, matching our upper bounds up to the exponent
of the polylogarithm. In contrast, the best known competitive ratios for these
problems in the fully adversarial setting are $2k-1$, $\infty$ and
$\Theta(k^2)$, respectively.

[Read original post](http://arxiv.org/abs/2507.17834v1)
