---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Optimal antimatroid sorting"
date: 2025-07-21T00:00:00
---

**Authors:** [Benjamin Aram Berendsohn](https://dblp.uni-trier.de/search?q=Benjamin+Aram+Berendsohn)

The classical comparison-based sorting problem asks us to find the underlying
total order of a given set of elements, where we can only access the elements
via comparisons. In this paper, we study a restricted version, where, as a
hint, a set $T$ of possible total orders is given, usually in some compressed
form.
Recently, an algorithm called topological heapsort with optimal running time
was found for the case where $T$ is the set of topological orderings of a given
directed acyclic graph, or, equivalently, $T$ is the set of linear extensions
of a given partial order [Haeupler et al. 2024]. We show that a simple
generalization of topological heapsort is applicable to a much broader class of
restricted sorting problems, where $T$ corresponds to a given antimatroid.
As a consequence, we obtain optimal algorithms for the following restricted
sorting problems, where the allowed total orders are restricted by: a given set
of monotone precedence formulas; the perfect elimination orders of a given
chordal graph; or the possible vertex search orders of a given connected rooted
graph.

[Read original post](http://arxiv.org/abs/2507.13994v1)
