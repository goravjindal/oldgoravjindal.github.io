---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Parallel Batch-Dynamic Algorithms for Spanners, and Extensions"
date: 2025-07-10T00:00:00
---

**Authors:** [Mohsen Ghaffari](https://dblp.uni-trier.de/search?q=Mohsen+Ghaffari), [Jaehyun Koo](https://dblp.uni-trier.de/search?q=Jaehyun+Koo)

This paper presents the first parallel batch-dynamic algorithms for computing
spanners and sparsifiers. Our algorithms process any batch of edge insertions
and deletions in an $n$-node undirected graph, in $\text{poly}(\log n)$ depth
and using amortized work near-linear in the batch size. Our concrete results
are as follows:
- Our base algorithm maintains a spanner with $(2k-1)$ stretch and
$\tilde{O}(n^{1+1/k})$ edges, for any $k\geq 1$.
- Our first extension maintains a sparse spanner with only $O(n)$ edges, and
$\tilde{O}(\log n)$ stretch.
- Our second extension maintains a $t$-bundle of spanners -- i.e., $t$
spanners, each of which is the spanner of the graph remaining after removing
the previous ones -- and allows us to maintain cut/spectral sparsifiers with
$\tilde{O}(n)$ edges.

[Read original post](http://arxiv.org/abs/2507.06338v1)
