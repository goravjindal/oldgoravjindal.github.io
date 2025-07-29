---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Adaptive BSTs for Single-Source and All-to-All Requests: Algorithms and"
date: 2025-07-29T00:00:00
---

**Authors:** [Maryam Shiran](https://dblp.uni-trier.de/search?q=Maryam+Shiran)

Adaptive binary search trees are a fundamental data structure for organizing
hierarchical information. Their ability to dynamically adjust to access
patterns makes them particularly valuable for building responsive and efficient
networked and distributed systems.
We present a unified framework for adaptive binary search trees with fixed
restructuring cost, analyzed under two models: the single-source model, where
the cost of querying a node is proportional to its distance from a fixed
source, and the all-to-all model, where the cost of serving a request depends
on the distance between the source and destination nodes. We propose an offline
algorithm for the single-source model and extend it to the all-to-all model.
For both models, we prove upper bounds on the cost incurred by our algorithms.
Furthermore, we show the existence of input sequences for which any offline
algorithm must incur a cost comparable to ours.
In the online setting, we develop a general mathematical framework for
deterministic online adaptive binary search trees and propose a deterministic
online strategy for the single-source case, which naturally extends to the
all-to-all model. We also establish lower bounds on the competitive ratio of
any deterministic online algorithm, highlighting fundamental limitations of
online adaptivity.

[Read original post](http://arxiv.org/abs/2507.20228v1)
