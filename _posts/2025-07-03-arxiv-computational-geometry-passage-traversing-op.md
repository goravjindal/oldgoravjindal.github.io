---
layout: post
title: "arXiv: Computational Geometry: Passage-traversing optimal path planning with sampling-based algorithms"
date: 2025-07-03 13:21:53 
categories: [rss]
external_link: http://arxiv.org/abs/2506.23614v1
---

**Authors:** [Jing Huang](https://dblp.uni-trier.de/search?q=Jing+Huang), [Hao Su](https://dblp.uni-trier.de/search?q=Hao+Su), [Kwok Wai Samuel Au](https://dblp.uni-trier.de/search?q=Kwok+Wai+Samuel+Au)

This paper introduces a new paradigm of optimal path planning, i.e.,
passage-traversing optimal path planning (PTOPP), that optimizes paths'
traversed passages for specified optimization objectives. In particular, PTOPP
is utilized to find the path with optimal accessible free space along its
entire length, which represents a basic requirement for paths in robotics. As
passages are places where free space shrinks and becomes constrained, the core
idea is to leverage the path's passage traversal status to characterize its
accessible free space comprehensively. To this end, a novel passage detection
and free space decomposition method using proximity graphs is proposed,
enabling fast detection of sparse but informative passages and environment
decompositions. Based on this preprocessing, optimal path planning with
accessible free space objectives or constraints is formulated as PTOPP problems
compatible with sampling-based optimal planners. Then, sampling-based
algorithms for PTOPP, including their dependent primitive procedures, are
developed leveraging partitioned environments for fast passage traversal check.
All these methods are implemented and thoroughly tested for effectiveness and
efficiency validation. Compared to existing approaches, such as clearance-based
methods, PTOPP demonstrates significant advantages in configurability, solution
optimality, and efficiency, addressing prior limitations and incapabilities. It
is believed to provide an efficient and versatile solution to accessible free
space optimization over conventional avenues and more generally, to a broad
class of path planning problems that can be formulated as PTOPP.
