---
layout: post
title: "arXiv: Data Structures and Algorithms: Lazy B-Trees"
date: 2025-07-03 13:21:53 
categories: [rss]
external_link: http://arxiv.org/abs/2507.00277v1
---

**Authors:** [Casper Moldrup Rysgaard](https://dblp.uni-trier.de/search?q=Casper+Moldrup+Rysgaard), [Sebastian Wild](https://dblp.uni-trier.de/search?q=Sebastian+Wild)

Lazy search trees (Sandlund & Wild FOCS 2020, Sandlund & Zhang SODA 2022) are
sorted dictionaries whose update and query performance smoothly interpolates
between that of efficient priority queues and binary search trees -
automatically, depending on actual use; no adjustments are necessary to the
data structure to realize the cost savings. In this paper, we design lazy
B-trees, a variant of lazy search trees suitable for external memory that
generalizes the speedup of B-trees over binary search trees wrt. input/output
operations to the same smooth interpolation regime.
A key technical difficulty to overcome is the lack of a (fully satisfactory)
external variant of biased search trees, on which lazy search trees crucially
rely. We give a construction for a subset of performance guarantees sufficient
to realize external-memory lazy search trees, which we deem of independent
interest.
As one special case, lazy B-trees can be used as an external-memory priority
queue, in which case they are competitive with some tailor-made heaps; indeed,
they offer faster decrease-key and insert operations than known data
structures.
