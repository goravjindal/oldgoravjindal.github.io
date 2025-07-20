---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Multi-Queue SSD I/O Modeling & Its Implications for Data Structure"
date: 2025-07-10T00:00:00
---

**Authors:** [Erin Ransom](https://dblp.uni-trier.de/search?q=Erin+Ransom), [Andrew Lim](https://dblp.uni-trier.de/search?q=Andrew+Lim), [Michael Mitzenmacher](https://dblp.uni-trier.de/search?q=Michael+Mitzenmacher)

Understanding the performance profiles of storage devices and how best to
utilize them has always been non-trivial due to factors such as seek times,
caching, scheduling, concurrent access, flash wear-out, and garbage collection.
However, analytical frameworks that provide simplified abstractions of storage
performance can still be accurate enough to evaluate external memory algorithms
and data structures at the design stage. For example, the Disk Access Machine
(DAM) model assumes that a storage device transfers data in fixed-size blocks
of size B and that all transfers have unit latency. This abstraction is already
sufficient to explain some of the benefits of data structures such as B-trees
and Log-Structured Merge trees (LSM trees); however, storage technology
advances have significantly reduced current models' accuracy and utility.
This paper introduces the Multi-Queue Solid State Drive (MQSSD) model, a new
storage abstraction. This model builds upon previous models and aims to more
accurately represent the performance characteristics of modern storage
hardware. We identify key performance-critical aspects of modern multi-queue
solid-state drives on which we base our model and demonstrate these
characteristics on actual hardware. We then show how our model can be applied
to LSM-tree-based storage engines to optimize them for modern storage hardware.
We highlight that leveraging concurrent access is crucial for fully utilizing
the high throughput of multi-queue SSDs, enabling designs that may appear
counterintuitive under traditional paradigms We then validate these insights
through experiments using Facebook's LSM-tree-based key-value store, RocksDB.
We conclude that the MQSSD model offers a more accurate abstraction of modern
hardware than previous models, allowing for greater insight and optimization.

[Read original post](http://arxiv.org/abs/2507.06349v1)
