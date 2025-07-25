---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Zeroth-order log-concave sampling"
date: 2025-07-25T00:00:00
---

**Authors:** [Yunbum Kook](https://dblp.uni-trier.de/search?q=Yunbum+Kook)

We study the zeroth-order query complexity of log-concave sampling,
specifically uniform sampling from convex bodies using membership oracles. We
propose a simple variant of the proximal sampler that achieves the query
complexity with matched R\'enyi orders between the initial warmness and output
guarantee. Specifically, for any $\varepsilon>0$ and $q\geq2$, the sampler,
initialized at $\pi\_{0}$, outputs a sample whose law is $\varepsilon$-close in
$q$-R\'enyi divergence to $\pi$, the uniform distribution over a convex body in
$\mathbb{R}^{d}$, using
$\widetilde{O}(qM\_{q}^{q/(q-1)}d^{2}\,\lVert\operatorname{cov}\pi\rVert\log\frac{1}{\varepsilon})$
membership queries, where
$M\_{q}=\lVert\text{d}\pi\_{0}/\text{d}\pi\rVert\_{L^{q}(\pi)}$.
We further introduce a simple annealing scheme that produces a warm start in
$q$-R\'enyi divergence (i.e., $M\_{q}=O(1)$) using
$\widetilde{O}(qd^{2}R^{3/2}\,\lVert\operatorname{cov}\pi\rVert^{1/4})$
queries, where $R^{2}=\mathbb{E}\_{\pi}[|\cdot|^{2}]$. This interpolates between
known complexities for warm-start generation in total variation and
R\'enyi-infinity divergence. To relay a R\'enyi warmness across the annealing
scheme, we establish hypercontractivity under simultaneous heat flow and
translate it into an improved mixing guarantee for the proximal sampler under a
logarithmic Sobolev inequality. These results extend naturally to general
log-concave distributions accessible via evaluation oracles, incurring
additional quadratic queries.

[Read original post](http://arxiv.org/abs/2507.18021v1)
