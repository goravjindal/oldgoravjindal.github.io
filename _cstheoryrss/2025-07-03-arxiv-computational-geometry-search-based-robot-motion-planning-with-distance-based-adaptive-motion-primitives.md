---
layout: post
category: cstheoryrss
title: "arXiv: Computational Geometry: Search-Based Robot Motion Planning With Distance-Based Adaptive Motion
  Primitives"
date: 2025-07-03T00:00:00
---

**Authors:** [Benjamin Kraljusic](https://dblp.uni-trier.de/search?q=Benjamin+Kraljusic), [Zlatan Ajanovic](https://dblp.uni-trier.de/search?q=Zlatan+Ajanovic), [Nermin Covic](https://dblp.uni-trier.de/search?q=Nermin+Covic), [Bakir Lacevic](https://dblp.uni-trier.de/search?q=Bakir+Lacevic)

This work proposes a motion planning algorithm for robotic manipulators that
combines sampling-based and search-based planning methods. The core
contribution of the proposed approach is the usage of burs of free
configuration space (C-space) as adaptive motion primitives within the graph
search algorithm. Due to their feature to adaptively expand in free C-space,
burs enable more efficient exploration of the configuration space compared to
fixed-sized motion primitives, significantly reducing the time to find a valid
path and the number of required expansions. The algorithm is implemented within
the existing SMPL (Search-Based Motion Planning Library) library and evaluated
through a series of different scenarios involving manipulators with varying
number of degrees-of-freedom (DoF) and environment complexity. Results
demonstrate that the bur-based approach outperforms fixed-primitive planning in
complex scenarios, particularly for high DoF manipulators, while achieving
comparable performance in simpler scenarios.

[Read original post](http://arxiv.org/abs/2507.01198v1)
