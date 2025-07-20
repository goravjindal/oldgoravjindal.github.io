---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: On the Approximability of Train Routing and the Min-Max Disjoint Paths"
date: 2025-07-07T00:00:00
---

**Authors:** [Umang Bhaskar](https://dblp.uni-trier.de/search?q=Umang+Bhaskar), [Katharina Eickhoff](https://dblp.uni-trier.de/search?q=Katharina+Eickhoff), [Lennart Kauther](https://dblp.uni-trier.de/search?q=Lennart+Kauther), [Jannik Matuschke](https://dblp.uni-trier.de/search?q=Jannik+Matuschke), [Britta Peis](https://dblp.uni-trier.de/search?q=Britta+Peis), [Laura Vargas Koch](https://dblp.uni-trier.de/search?q=Laura+Vargas+Koch)

In train routing, the headway is the minimum distance that must be maintained
between successive trains for safety and robustness. We introduce a model for
train routing that requires a fixed headway to be maintained between trains,
and study the problem of minimizing the makespan, i.e., the arrival time of the
last train, in a single-source single-sink network. For this problem, we first
show that there exists an optimal solution where trains move in convoys, that
is, the optimal paths for any two trains are either the same or are
arc-disjoint. Via this insight, we are able to reduce the approximability of
our train routing problem to that of the min-max disjoint paths problem, which
asks for a collection of disjoint paths where the maximum length of any path in
the collection is as small as possible. While min-max disjoint paths inherits a
strong inapproximability result on directed acyclic graphs from the multi-level
bottleneck assignment problem, we show that a natural greedy composition
approach yields a logarithmic approximation in the number of disjoint paths for
series-parallel graphs. We also present an alternative analysis of this
approach that yields a guarantee depending on how often the decomposition tree
of the series-parallel graph alternates between series and parallel
compositions on any root-leaf path.

[Read original post](http://arxiv.org/abs/2507.03687v1)
