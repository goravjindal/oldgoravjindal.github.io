---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: CleANN: Efficient Full Dynamism in Graph-based Approximate Nearest"
date: 2025-07-29T00:00:00
---

**Authors:** [Ziyu Zhang](https://dblp.uni-trier.de/search?q=Ziyu+Zhang), [Yuanhao Wei](https://dblp.uni-trier.de/search?q=Yuanhao+Wei), [Joshua Engels](https://dblp.uni-trier.de/search?q=Joshua+Engels), [Julian Shun](https://dblp.uni-trier.de/search?q=Julian+Shun)

Approximate nearest neighbor search (ANNS) has become a quintessential
algorithmic problem for various other foundational data tasks for AI workloads.
Graph-based ANNS indexes have superb empirical trade-offs in indexing cost,
query efficiency, and query approximation quality. Most existing graph-based
indexes are designed for the static scenario, where there are no updates to the
data after the index is constructed. However, full dynamism (insertions,
deletions, and searches) is crucial to providing up-to-date responses in
applications using vector databases. It is desirable that the index efficiently
supports updates and search queries concurrently. Existing dynamic graph-based
indexes suffer from at least one of the following problems: (1) the query
quality degrades as updates happen; and (2) the graph structure updates used to
maintain the index quality upon updates are global and thus expensive. To solve
these problems, we propose the CleANN system which consists of three main
components: (1) workload-aware linking of diverse search tree descendants to
combat distribution shift; (2)query-adaptive on-the-fly neighborhood
consolidation to efficiently handle deleted nodes; and (3) semi-lazy memory
cleaning to clean up stale information in the data structure and reduce the
work spent by the first two components. We evaluate CleANN on 7 diverse
datasets on fully dynamic workloads and find that CleANN has query quality at
least as good as if the index had been built statically using the corresponding
data. In the in-memory setting using 56 hyper-threads, with all types of
queries running concurrently, at the same recall level, CleANN achieves 7-1200x
throughput improvement on million-scale real-world datasets. To the best of our
knowledge, CleANN is the first concurrent ANNS index to achieve such efficiency
while maintaining quality under full dynamism.

[Read original post](http://arxiv.org/abs/2507.19802v1)
