---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Scalable contribution bounding to achieve privacy"
date: 2025-08-01T00:00:00
---

**Authors:** [Vincent Cohen-Addad](https://dblp.uni-trier.de/search?q=Vincent+Cohen-Addad), [Alessandro Epasto](https://dblp.uni-trier.de/search?q=Alessandro+Epasto), [Jason Lee](https://dblp.uni-trier.de/search?q=Jason+Lee), [Morteza Zadimoghaddam](https://dblp.uni-trier.de/search?q=Morteza+Zadimoghaddam)

In modern datasets, where single records can have multiple owners, enforcing
user-level differential privacy requires capping each user's total
contribution. This "contribution bounding" becomes a significant combinatorial
challenge. Existing sequential algorithms for this task are computationally
intensive and do not scale to the massive datasets prevalent today. To address
this scalability bottleneck, we propose a novel and efficient distributed
algorithm. Our approach models the complex ownership structure as a hypergraph,
where users are vertices and records are hyperedges. The algorithm proceeds in
rounds, allowing users to propose records in parallel. A record is added to the
final dataset only if all its owners unanimously agree, thereby ensuring that
no user's predefined contribution limit is violated. This method aims to
maximize the size of the resulting dataset for high utility while providing a
practical, scalable solution for implementing user-level privacy in large,
real-world systems.

[Read original post](http://arxiv.org/abs/2507.23432v1)
