---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: Fantastic Flips and Where to Find Them: A General Framework for
  Parameterized Local Search on Partitioning Problem"
date: 2025-07-01T00:00:00
---

**Authors:** [Niels Grüttemeier](https://dblp.uni-trier.de/search?q=Niels+Gr%C3%BCttemeier), [Nils Morawietz](https://dblp.uni-trier.de/search?q=Nils+Morawietz), [Frank Sommer](https://dblp.uni-trier.de/search?q=Frank+Sommer)

Parameterized local search combines classic local search heuristics with the
paradigm of parameterized algorithmics. While most local search algorithms aim
to improve given solutions by performing one single operation on a given
solution, the parameterized approach aims to improve a solution by performing
$k$ simultaneous operations. Herein, $k$ is a parameter called search radius
for which the value can be chosen by a user. One major goal in the field of
parameterized local search is to outline the trade-off between the size of $k$
and the running time of the local search step. In this work, we introduce an
abstract framework that generalizes natural parameterized local search
approaches for a large class of partitioning problems: Given $n$ items that are
partitioned into $b$ bins and a target function that evaluates the quality of
the current partition, one asks whether it is possible to improve the solution
by removing up to $k$ items from their current bins and reassigning them to
other bins. Among others, our framework applies for the local search versions
of problems like Cluster Editing, Vector Bin Packing, and Nash Social Welfare.
Motivated by a real-world application of the problem Vector Bin Packing, we
introduce a parameter called number of types $\tau \le n$ and show that all
problems fitting in our framework can be solved in $\tau^k 2^{O(k)} |I|^{O(1)}$
time, where $|I|$ denotes the total input size. In case of Cluster Editing, the
parameter $\tau$ generalizes the well-known parameter neighborhood diversity of
the input graph. We complement this by showing that for all considered
problems, an algorithm significantly improving over our algorithm with running
time $\tau^k 2^{O(k)} |I|^{O(1)}$ would contradict the ETH. Additionally, we
show that even on very restricted instances, all considered problems are
W[1]-hard when parameterized by the search radius $k$ alone.