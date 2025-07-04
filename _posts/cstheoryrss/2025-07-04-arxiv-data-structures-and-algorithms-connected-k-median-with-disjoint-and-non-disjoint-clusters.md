---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Connected k-Median with Disjoint and Non-disjoint Clusters"
date: 2025-07-04T00:00:00
---

**Authors:** [Jan Eube](https://dblp.uni-trier.de/search?q=Jan+Eube), [Kelin Luo](https://dblp.uni-trier.de/search?q=Kelin+Luo), [Dorian Reineccius](https://dblp.uni-trier.de/search?q=Dorian+Reineccius), [Heiko Röglin](https://dblp.uni-trier.de/search?q=Heiko+R%C3%B6glin), [Melanie Schmidt](https://dblp.uni-trier.de/search?q=Melanie+Schmidt)

The connected $k$-median problem is a constrained clustering problem that
combines distance-based $k$-clustering with connectivity information. The
problem allows to input a metric space and an unweighted undirected
connectivity graph that is completely unrelated to the metric space. The goal
is to compute $k$ centers and corresponding clusters such that each cluster
forms a connected subgraph of $G$, and such that the $k$-median cost is
minimized.
The problem has applications in very different fields like geodesy
(particularly districting), social network analysis (especially community
detection), or bioinformatics. We study a version with overlapping clusters
where points can be part of multiple clusters which is natural for the use case
of community detection. This problem variant is $\Omega(\log n)$-hard to
approximate, and our main result is an $\mathcal{O}(k^2 \log n)$-approximation
algorithm for the problem. We complement it with an
$\Omega(n^{1-\epsilon})$-hardness result for the case of disjoint clusters
without overlap with general connectivity graphs, as well as an exact algorithm
in this setting if the connectivity graph is a tree.