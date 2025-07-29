---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Parallel Hierarchical Agglomerative Clustering in Low Dimensions"
date: 2025-07-29T00:00:00
---

**Authors:** [MohammadHossein Bateni](https://dblp.uni-trier.de/search?q=MohammadHossein+Bateni), [Laxman Dhulipala](https://dblp.uni-trier.de/search?q=Laxman+Dhulipala), [Willem Fletcher](https://dblp.uni-trier.de/search?q=Willem+Fletcher), [Kishen N Gowda](https://dblp.uni-trier.de/search?q=Kishen+N+Gowda), [D Ellis Hershkowitz](https://dblp.uni-trier.de/search?q=D+Ellis+Hershkowitz), [Rajesh Jayaram](https://dblp.uni-trier.de/search?q=Rajesh+Jayaram), [Jakub Łącki](https://dblp.uni-trier.de/search?q=Jakub+%C5%81%C4%85cki)

Hierarchical Agglomerative Clustering (HAC) is an extensively studied and
widely used method for hierarchical clustering in $\mathbb{R}^k$ based on
repeatedly merging the closest pair of clusters according to an input linkage
function $d$. Highly parallel (i.e., NC) algorithms are known for
$(1+\epsilon)$-approximate HAC (where near-minimum rather than minimum pairs
are merged) for certain linkage functions that monotonically increase as merges
are performed. However, no such algorithms are known for many important but
non-monotone linkage functions such as centroid and Ward's linkage.
In this work, we show that a general class of non-monotone linkage functions
-- which include centroid and Ward's distance -- admit efficient NC algorithms
for $(1+\epsilon)$-approximate HAC in low dimensions. Our algorithms are based
on a structural result which may be of independent interest: the height of the
hierarchy resulting from any constant-approximate HAC on $n$ points for this
class of linkage functions is at most $\operatorname{poly}(\log n)$ as long as
$k = O(\log \log n / \log \log \log n)$. Complementing our upper bounds, we
show that NC algorithms for HAC with these linkage functions in
\emph{arbitrary} dimensions are unlikely to exist by showing that HAC is
CC-hard when $d$ is centroid distance and $k = n$.

[Read original post](http://arxiv.org/abs/2507.20047v1)
