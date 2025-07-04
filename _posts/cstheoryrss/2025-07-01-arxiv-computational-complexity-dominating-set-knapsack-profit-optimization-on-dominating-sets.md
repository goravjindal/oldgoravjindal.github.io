---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: Dominating Set Knapsack: Profit Optimization on Dominating Sets"
date: 2025-07-01T00:00:00
---

**Authors:** [Sipra Singh](https://dblp.uni-trier.de/search?q=Sipra+Singh)

In a large-scale network, we want to choose some influential nodes to make a
profit by paying some cost within a limited budget so that we do not have to
spend more budget on some nodes adjacent to the chosen nodes; our problem is
the graph-theoretic representation of it. We define our problem Dominating Set
Knapsack by attaching Knapsack Problem with Dominating Set on graphs. Each
vertex is associated with a cost factor and a profit amount. We aim to choose
some vertices within a fixed budget that gives maximum profit so that we do not
need to choose their 1-hop neighbors. We show that the Dominating Set Knapsack
problem is strongly NP-complete even when restricted to Bipartite graphs but
weakly NP-complete for Star graphs. We present a pseudo-polynomial time
algorithm for Trees in time $O(n\cdot min\{s^2, (\alpha(V))^2\})$. We show that
Dominating Set Knapsack is very unlikely to be Fixed Parameter Tractable(FPT)
by proving that it is in W[2]-hard parameterized by the solution size. We
developed FPT algorithms with running time $O(4^{tw}\cdot n^{O(1)} \cdot
min\{s^2,{\alpha(V)}^2\})$ and $O(2^{vck-1}\cdot n^{O(1)} \cdot
min\{s^2,{\alpha(V)}^2\})$, where $tw$ represents the treewidth of the given
graph, $vck$ is the solution size of the Vertex Cover Knapsack, $s$ is the size
of the knapsack and $\alpha(V)=\sum\_{v\in V}\alpha(v)$.