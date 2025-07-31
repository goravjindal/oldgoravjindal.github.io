---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: BlockFIFO & MultiFIFO: Scalable Relaxed Queues"
date: 2025-07-31T00:00:00
---

**Authors:** [Stefan Koch](https://dblp.uni-trier.de/search?q=Stefan+Koch), [Peter Sanders](https://dblp.uni-trier.de/search?q=Peter+Sanders), [Marvin Williams](https://dblp.uni-trier.de/search?q=Marvin+Williams)

FIFO queues are a fundamental data structure used in a wide range of
applications. Concurrent FIFO queues allow multiple execution threads to access
the queue simultaneously. Maintaining strict FIFO semantics in concurrent
queues leads to low throughput due to high contention at the head and tail of
the queue. By relaxing the FIFO semantics to allow some reordering of elements,
it becomes possible to achieve much higher scalability. This work presents two
orthogonal designs for relaxed concurrent FIFO queues, one derived from the
MultiQueue and the other based on ring buffers. We evaluate both designs
extensively on various micro-benchmarks and a breadth-first search application
on large graphs. Both designs outperform state-of-the-art relaxed and strict
FIFO queues, achieving higher throughput and better scalability.

[Read original post](http://arxiv.org/abs/2507.22764v1)
