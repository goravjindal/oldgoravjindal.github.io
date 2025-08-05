---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Efficient Direct-Access Ranked Retrieval"
date: 2025-08-05T00:00:00
---

**Authors:** [Mohsen Dehghankar](https://dblp.uni-trier.de/search?q=Mohsen+Dehghankar), [Raghav Mittal](https://dblp.uni-trier.de/search?q=Raghav+Mittal), [Suraj Shetiya](https://dblp.uni-trier.de/search?q=Suraj+Shetiya), [Abolfazl Asudeh](https://dblp.uni-trier.de/search?q=Abolfazl+Asudeh), [Gautam Das](https://dblp.uni-trier.de/search?q=Gautam+Das)

We study the problem of Direct-Access Ranked Retrieval (DAR) for interactive
data tooling, where evolving data exploration practices, combined with
large-scale and high-dimensional datasets, create new challenges. DAR concerns
the problem of enabling efficient access to arbitrary rank positions according
to a ranking function, without enumerating all preceding tuples. To address
this need, we formalize the DAR problem and propose a theoretically efficient
algorithm based on geometric arrangements, achieving logarithmic query time.
However, this method suffers from exponential space complexity in high
dimensions. Therefore, we develop a second class of algorithms based on
$\varepsilon$-sampling, which consume a linear space. Since exactly locating
the tuple at a specific rank is challenging due to its connection to the range
counting problem, we introduce a relaxed variant called Conformal Set Ranked
Retrieval (CSR), which returns a small subset guaranteed to contain the target
tuple. To solve the CSR problem efficiently, we define an intermediate problem,
Stripe Range Retrieval (SRR), and design a hierarchical sampling data structure
tailored for narrow-range queries. Our method achieves practical scalability in
both data size and dimensionality. We prove near-optimal bounds on the
efficiency of our algorithms and validate their performance through extensive
experiments on real and synthetic datasets, demonstrating scalability to
millions of tuples and hundreds of dimensions.

[Read original post](http://arxiv.org/abs/2508.01108v1)
