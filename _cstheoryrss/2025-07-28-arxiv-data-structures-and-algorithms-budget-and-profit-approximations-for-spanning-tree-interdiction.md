---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Budget and Profit Approximations for Spanning Tree Interdiction"
date: 2025-07-28T00:00:00
---

**Authors:** [Rafail Ostrovsky](https://dblp.uni-trier.de/search?q=Rafail+Ostrovsky), [Yuval Rabani](https://dblp.uni-trier.de/search?q=Yuval+Rabani), [Yoav Siman Tov](https://dblp.uni-trier.de/search?q=Yoav+Siman+Tov)

We give polynomial time logarithmic approximation guarantees for the budget
minimization, as well as for the profit maximization versions of minimum
spanning tree interdiction. In this problem, the goal is to remove some edges
of an undirected graph with edge weights and edge costs, so as to increase the
weight of a minimum spanning tree. In the budget minimization version, the goal
is to minimize the total cost of the removed edges, while achieving a desired
increase $\Delta$ in the weight of the minimum spanning tree. An alternative
objective within the same framework is to maximize the profit of interdiction,
namely the increase in the weight of the minimum spanning tree, subject to a
budget constraint. There are known polynomial time $O(1)$ approximation
guarantees for a similar objective (maximizing the total cost of the tree,
rather than the increase). However, the guarantee does not seem to apply to the
increase in cost. Moreover, the same techniques do not seem to apply to the
budget version.
Our approximation guarantees are motivated by studying the question of
minimizing the cost of increasing the minimum spanning tree by any amount. We
show that in contrast to the budget and profit problems, this version of
interdiction is polynomial time-solvable, and we give an efficient algorithm
for solving it. The solution motivates a graph-theoretic relaxation of the
NP-hard interdiction problem. The gain in minimum spanning tree weight, as a
function of the set of removed edges, is super-modular. Thus, the budget
problem is an instance of minimizing a linear function subject to a
super-modular covering constraint. We use the graph-theoretic relaxation to
design and analyze a batch greedy-based algorithm.

[Read original post](http://arxiv.org/abs/2507.19178v1)
