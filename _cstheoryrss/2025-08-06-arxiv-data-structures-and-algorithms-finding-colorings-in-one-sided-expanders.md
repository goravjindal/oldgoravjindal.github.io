---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Finding Colorings in One-Sided Expanders"
date: 2025-08-06T00:00:00
---

**Authors:** [Rares-Darius Buhai](https://dblp.uni-trier.de/search?q=Rares-Darius+Buhai), [Yiding Hua](https://dblp.uni-trier.de/search?q=Yiding+Hua), [David Steurer](https://dblp.uni-trier.de/search?q=David+Steurer), [Andor Vári-Kakas](https://dblp.uni-trier.de/search?q=Andor+V%C3%A1ri-Kakas)

We establish new algorithmic guarantees with matching hardness results for
coloring and independent set problems in one-sided expanders and related
classes of graphs. For example, given a $3$-colorable regular one-sided
expander, we compute in polynomial time either an independent set of relative
size at least $1/2-o(1)$ or a proper $3$-coloring for all but an $o(1)$
fraction of the vertices, where $o(1)$ stands for a function that tends to $0$
with the second largest eigenvalue of the normalized adjacency matrix. This
result improves on recent seminal work of Bafna, Hsieh, and Kothari (STOC 2025)
developing an algorithm that efficiently finds independent sets of relative
size at least $0.01$ in such graphs. We also obtain an efficient
$1.6667$-factor approximation algorithm for VERTEX COVER in sufficiently strong
regular one-sided expanders, improving over a previous $(2-\epsilon)$-factor
approximation in such graphs for an unspecified constant $\epsilon>0$.
We propose a new stratification of $k$-COLORING in terms of $k$-by-$k$
matrices akin to predicate sets for constraint satisfaction problems. We prove
that whenever this matrix has repeated rows, the corresponding coloring problem
is NP-hard for one-sided expanders under the Unique Games Conjecture. On the
other hand, if this matrix has no repeated rows, our algorithms can solve the
corresponding coloring problem on one-sided expanders in polynomial time.
As starting point for our algorithmic results, we show a property of graph
spectra that, to the best of our knowledge, has not been observed before: The
number of negative eigenvalues smaller than $-\tau$ is at most $O(1/\tau^{2})$
times the number of eigenvalues larger than $\tau^{2}/2$. While this result
allows us to bound the number of eigenvalues bounded away from $0$ in one-sided
spectral expanders, this property alone is insufficient for our algorithmic
results.

[Read original post](http://arxiv.org/abs/2508.02825v1)
