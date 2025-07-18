---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Efficiently Constructing Sparse Navigable Graphs"
date: 2025-07-18T00:00:00
---

**Authors:** [Alex Conway](https://dblp.uni-trier.de/search?q=Alex+Conway), [Laxman Dhulipala](https://dblp.uni-trier.de/search?q=Laxman+Dhulipala), [Martin Farach-Colton](https://dblp.uni-trier.de/search?q=Martin+Farach-Colton), [Rob Johnson](https://dblp.uni-trier.de/search?q=Rob+Johnson), [Ben Landrum](https://dblp.uni-trier.de/search?q=Ben+Landrum), [Christopher Musco](https://dblp.uni-trier.de/search?q=Christopher+Musco), [Yarin Shechter](https://dblp.uni-trier.de/search?q=Yarin+Shechter), [Torsten Suel](https://dblp.uni-trier.de/search?q=Torsten+Suel), [Richard Wen](https://dblp.uni-trier.de/search?q=Richard+Wen)

Graph-based nearest neighbor search methods have seen a surge of popularity
in recent years, offering state-of-the-art performance across a wide variety of
applications. Central to these methods is the task of constructing a sparse
navigable search graph for a given dataset endowed with a distance function.
Unfortunately, doing so is computationally expensive, so heuristics are
universally used in practice.
In this work, we initiate the study of fast algorithms with provable
guarantees for search graph construction. For a dataset with $n$ data points,
the problem of constructing an optimally sparse navigable graph can be framed
as $n$ separate but highly correlated minimum set cover instances. This yields
a naive $O(n^3)$ time greedy algorithm that returns a navigable graph whose
sparsity is at most $O(\log n)$ higher than optimal. We improve significantly
on this baseline, taking advantage of correlation between the set cover
instances to leverage techniques from streaming and sublinear-time set cover
algorithms. Combined with problem-specific pre-processing techniques, we
present an $\tilde{O}(n^2)$ time algorithm for constructing an $O(\log
n)$-approximate sparsest navigable graph under any distance function.
The runtime of our method is optimal up to logarithmic factors under the
Strong Exponential Time Hypothesis via a reduction from Monochromatic Closest
Pair. Moreover, we prove that, as with general set cover, obtaining better than
an $O(\log n)$-approximation is NP-hard, despite the significant additional
structure present in the navigable graph problem. Finally, we show that our
techniques can also beat cubic time for the closely related and practically
important problems of constructing $\alpha$-shortcut reachable and
$\tau$-monotonic graphs, which are also used for nearest neighbor search. For
such graphs, we obtain $\tilde{O}(n^{2.5})$ time or better algorithms.

[Read original post](http://arxiv.org/abs/2507.13296v1)
