---
layout: post
category: cstheoryrss
title: "arXiv: Computational Geometry: On Tight Robust Coresets for k-Medians Clustering"
date: 2025-07-16T00:00:00
---

**Authors:** [Lingxiao Huang](https://dblp.uni-trier.de/search?q=Lingxiao+Huang), [Zhenyu Jiang](https://dblp.uni-trier.de/search?q=Zhenyu+Jiang), [Yi Li](https://dblp.uni-trier.de/search?q=Yi+Li), [Xuan Wu](https://dblp.uni-trier.de/search?q=Xuan+Wu)

This paper considers coresets for the robust $k$-medians problem with $m$
outliers, and new constructions in various metric spaces are obtained.
Specifically, for metric spaces with a bounded VC or doubling dimension $d$,
the coreset size is $O(m) + \tilde{O}(kd\varepsilon^{-2})$, which is optimal up
to logarithmic factors. For Euclidean spaces, the coreset size is
$O(m\varepsilon^{-1}) +
\tilde{O}(\min\{k^{4/3}\varepsilon^{-2},k\varepsilon^{-3}\})$, improving upon a
recent result by Jiang and Lou (ICALP 2025). These results also extend to
robust $(k,z)$-clustering, yielding, for VC and doubling dimension, a coreset
size of $O(m) + \tilde{O}(kd\varepsilon^{-2z})$ with the optimal linear
dependence on $m$. This extended result improves upon the earlier work of Huang
et al. (SODA 2025). The techniques introduce novel dataset decompositions,
enabling chaining arguments to be applied jointly across multiple components.

[Read original post](http://arxiv.org/abs/2507.11260v1)
