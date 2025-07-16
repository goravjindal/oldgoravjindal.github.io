---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Multipass Linear Sketches for Geometric LP-Type Problems"
date: 2025-07-16T00:00:00
---

**Authors:** [N. Efe Çekirge](https://dblp.uni-trier.de/search?q=N.+Efe+%C3%87ekirge), [William Gay](https://dblp.uni-trier.de/search?q=William+Gay), [David P. Woodruff](https://dblp.uni-trier.de/search?q=David+P.+Woodruff)

LP-type problems such as the Minimum Enclosing Ball (MEB), Linear Support
Vector Machine (SVM), Linear Programming (LP), and Semidefinite Programming
(SDP) are fundamental combinatorial optimization problems, with many important
applications in machine learning applications such as classification,
bioinformatics, and noisy learning. We study LP-type problems in several
streaming and distributed big data models, giving $\varepsilon$-approximation
linear sketching algorithms with a focus on the high accuracy regime with low
dimensionality $d$, that is, when ${d < (1/\varepsilon)^{0.999}}$. Our main
result is an $O(ds)$ pass algorithm with $O(s( \sqrt{d}/\varepsilon)^{3d/s})
\cdot \mathrm{poly}(d, \log (1/\varepsilon))$ space complexity in words, for
any parameter $s \in [1, d \log (1/\varepsilon)]$, to solve
$\varepsilon$-approximate LP-type problems of $O(d)$ combinatorial and VC
dimension. Notably, by taking $s = d \log (1/\varepsilon)$, we achieve space
complexity polynomial in $d$ and polylogarithmic in $1/\varepsilon$, presenting
exponential improvements in $1/\varepsilon$ over current algorithms. We
complement our results by showing lower bounds of $(1/\varepsilon)^{\Omega(d)}$
for any $1$-pass algorithm solving the $(1 + \varepsilon)$-approximation MEB
and linear SVM problems, further motivating our multi-pass approach.

[Read original post](http://arxiv.org/abs/2507.11484v1)
