---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: MTASet: A Tree-based Set for Efficient Range Queries in Update-heavy"
date: 2025-07-29T00:00:00
---

**Authors:** [Daniel Manor](https://dblp.uni-trier.de/search?q=Daniel+Manor), [Mor Perry](https://dblp.uni-trier.de/search?q=Mor+Perry), [Moshe Sulamy](https://dblp.uni-trier.de/search?q=Moshe+Sulamy)

In concurrent data structures, the efficiency of set operations can vary
significantly depending on the workload characteristics. Numerous concurrent
set implementations are optimized and fine-tuned to excel in scenarios
characterized by predominant read operations. However, they often perform
poorly when confronted with workloads that heavily prioritize updates.
Additionally, current leading-edge concurrent sets optimized for update-heavy
tasks typically lack efficiency in handling atomic range queries. This study
introduces the MTASet, which leverages a concurrent (a,b)-tree implementation.
Engineered to accommodate update-heavy workloads and facilitate atomic range
queries, MTASet surpasses existing counterparts optimized for tasks in range
query operations by up to 2x. Notably, MTASet ensures linearizability.

[Read original post](http://arxiv.org/abs/2507.20041v1)
