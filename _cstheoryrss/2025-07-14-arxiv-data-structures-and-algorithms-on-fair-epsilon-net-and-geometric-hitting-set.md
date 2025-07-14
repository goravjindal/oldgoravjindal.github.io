---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: On Fair Epsilon Net and Geometric Hitting Set"
date: 2025-07-14T00:00:00
---

**Authors:** [Mohsen Dehghankar](https://dblp.uni-trier.de/search?q=Mohsen+Dehghankar), [Stavros Sintos](https://dblp.uni-trier.de/search?q=Stavros+Sintos), [Abolfazl Asudeh](https://dblp.uni-trier.de/search?q=Abolfazl+Asudeh)

Fairness has emerged as a formidable challenge in data-driven decisions. Many
of the data problems, such as creating compact data summaries for approximate
query processing, can be effectively tackled using concepts from computational
geometry, such as $\varepsilon$-nets. However, these powerful tools have yet to
be examined from the perspective of fairness. To fill this research gap, we add
fairness to classical geometric approximation problems of $\varepsilon$-net,
$\varepsilon$-sample, and geometric hitting set. We introduce and address two
notions of group fairness: demographic parity, which requires preserving group
proportions from the input distribution, and custom-ratios fairness, which
demands satisfying arbitrary target ratios. We develop two algorithms to
enforce fairness: one based on sampling and another on discrepancy theory. The
sampling-based algorithm is faster and computes a fair $\varepsilon$-net of
size which is only larger by a $\log(k)$ factor compared to the standard
(unfair) $\varepsilon$-net, where $k$ is the number of demographic groups. The
discrepancy-based algorithm is slightly slower (for bounded VC dimension), but
it computes a smaller fair $\varepsilon$-net. Notably, we reduce the fair
geometric hitting set problem to finding fair $\varepsilon$-nets. This results
in a $O(\log \mathsf{OPT} \times \log k)$ approximation of a fair geometric
hitting set. Additionally, we show that under certain input distributions,
constructing fair $\varepsilon$-samples can be infeasible, highlighting
limitations in fair sampling. Beyond the theoretical guarantees, our
experimental results validate the practical effectiveness of the proposed
algorithms. In particular, we achieve zero unfairness with only a modest
increase in output size compared to the unfair setting.

[Read original post](http://arxiv.org/abs/2507.08758v1)
