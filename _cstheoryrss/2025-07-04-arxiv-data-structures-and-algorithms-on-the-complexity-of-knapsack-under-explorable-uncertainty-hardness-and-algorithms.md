---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: On the Complexity of Knapsack under Explorable Uncertainty: Hardness and
  Algorithms"
date: 2025-07-04T00:00:00
---

**Authors:** [Jens Schlöter](https://dblp.uni-trier.de/search?q=Jens+Schl%C3%B6ter)

In the knapsack problem under explorable uncertainty, we are given a knapsack
instance with uncertain item profits. Instead of having access to the precise
profits, we are only given uncertainty intervals that are guaranteed to contain
the corresponding profits. The actual item profit can be obtained via a query.
The goal of the problem is to adaptively query item profits until the revealed
information suffices to compute an optimal (or approximate) solution to the
underlying knapsack instance. Since queries are costly, the objective is to
minimize the number of queries.
In the offline variant of this problem, we assume knowledge of the precise
profits and the task is to compute a query set of minimum cardinality that a
third party without access to the profits could use to identify an optimal (or
approximate) knapsack solution. We show that this offline variant is complete
for the second-level of the polynomial hierarchy, i.e., $\Sigma\_2^p$-complete,
and cannot be approximated within a non-trivial factor unless $\Sigma\_2^p =
\Delta\_2^p$. Motivated by these strong hardness results, we consider a
resource-augmented variant of the problem where the requirements on the query
set computed by an algorithm are less strict than the requirements on the
optimal solution we compare against. More precisely, a query set computed by
the algorithm must reveal sufficient information to identify an approximate
knapsack solution, while the optimal query set we compare against has to reveal
sufficient information to identify an optimal solution. We show that this
resource-augmented setting allows interesting non-trivial algorithmic results.

[Read original post](http://arxiv.org/abs/2507.02657v1)
