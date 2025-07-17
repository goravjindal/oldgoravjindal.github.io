---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: FastReChain: Highly Responsive and Low-Overhead Centralized Route
  Scheduling in Clos Datacenter Networks"
date: 2025-07-17T00:00:00
---

**Authors:** [Zihan Zhu](https://dblp.uni-trier.de/search?q=Zihan+Zhu), [Dongchao Wu](https://dblp.uni-trier.de/search?q=Dongchao+Wu), [Zhanbang Zhang](https://dblp.uni-trier.de/search?q=Zhanbang+Zhang), [Jian Yang](https://dblp.uni-trier.de/search?q=Jian+Yang)

Ever since Clos topologies were used in datacenter networks (DCNs), a
practical centralized scheduling algorithm that supports dynamic scheduling has
been absent. The introduction of optical switches in DCNs as a future-proof
solution exacerbates this problem due to several properties of optical
switches, such as the fact that they are generally bufferless and therefore
rely on centralized scheduling, and that they have long switching times and
therefore require the number of rearrangements to be minimized.
In this paper, we propose a centralized scheduling algorithm that achieves
theoretical maximum throughput even in one-rate bidirectional Clos networks,
while producing schemes with near-minimal numbers of rearrangements. It is the
only algorithm that directly supports bidirectional Clos networks and has a
time efficiency high enough to support dynamic scheduling to date. For static
minimal rewiring, its running time ranges from a fraction to a few hundredths
of other algorithms, and the number of rearrangements has also been steadily
improved, allowing for more frequent adjustments and less impact on ongoing
communications. In addition, the algorithm is very flexible and can support
various functional requirements in real-world environments. We achieve this
result through the replacement chain concept and bitset optimization.

[Read original post](http://arxiv.org/abs/2507.12265v1)
