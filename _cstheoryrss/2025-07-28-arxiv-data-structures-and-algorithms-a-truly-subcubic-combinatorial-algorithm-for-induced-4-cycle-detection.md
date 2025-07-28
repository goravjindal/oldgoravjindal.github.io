---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: A Truly Subcubic Combinatorial Algorithm for Induced 4-Cycle Detection"
date: 2025-07-28T00:00:00
---

**Authors:** [Amir Abboud](https://dblp.uni-trier.de/search?q=Amir+Abboud), [Shyan Akmal](https://dblp.uni-trier.de/search?q=Shyan+Akmal), [Nick Fischer](https://dblp.uni-trier.de/search?q=Nick+Fischer)

We present the first truly subcubic, combinatorial algorithm for detecting an
induced $4$-cycle in a graph. The running time is $O(n^{2.84})$ on $n$-node
graphs, thus separating the task of detecting induced $4$-cycles from detecting
triangles, which requires $n^{3-o(1)}$ time combinatorially under the popular
BMM hypothesis.
Significant work has gone into characterizing the exact time complexity of
induced $H$-detection, relative to the complexity of detecting cliques of
various sizes. Prior work identified the question of whether induced $4$-cycle
detection is triangle-hard as the only remaining case towards completing the
lowest level of the classification, dubbing it a "curious" case [Dalirrooyfard,
Vassilevska W., FOCS 2022]. Our result can be seen as a negative resolution of
this question.
Our algorithm deviates from previous techniques in the large body of subgraph
detection algorithms and employs the trendy topic of graph decomposition that
has hitherto been restricted to more global problems (as in the use of expander
decompositions for flow problems) or to shaving subpolynomial factors (as in
the application of graph regularity lemmas). While our algorithm is slower than
the (non-combinatorial) state-of-the-art $\tilde{O}(n^{\omega})$-time algorithm
based on polynomial identity testing [Vassilevska W., Wang, Williams, Yu, SODA
2014], combinatorial advancements often come with other benefits. In
particular, we give the first nontrivial deterministic algorithm for detecting
induced $4$-cycles.

[Read original post](http://arxiv.org/abs/2507.18845v1)
