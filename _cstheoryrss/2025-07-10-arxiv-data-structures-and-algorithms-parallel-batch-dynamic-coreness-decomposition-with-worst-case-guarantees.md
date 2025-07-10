---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Parallel Batch-Dynamic Coreness Decomposition with Worst-Case Guarantees"
date: 2025-07-10T00:00:00
---

**Authors:** [Mohsen Ghaffari](https://dblp.uni-trier.de/search?q=Mohsen+Ghaffari), [Jaehyun Koo](https://dblp.uni-trier.de/search?q=Jaehyun+Koo)

We present the first parallel batch-dynamic algorithm for approximating
coreness decomposition with worst-case update times. Given any batch of edge
insertions and deletions, our algorithm processes all these updates in $
\text{poly}(\log n)$ depth, using a worst-case work bound of $b\cdot
\text{poly}(\log n)$ where $b$ denotes the batch size. This means the batch
gets processed in $\tilde{O}(b/p)$ time, given $p$ processors, which is optimal
up to logarithmic factors. Previously, an algorithm with similar guarantees was
known by the celebrated work of Liu, Shi, Yu, Dhulipala, and Shun [SPAA'22],
but with the caveat of the work bound, and thus the runtime, being only
amortized.

[Read original post](http://arxiv.org/abs/2507.06334v1)
