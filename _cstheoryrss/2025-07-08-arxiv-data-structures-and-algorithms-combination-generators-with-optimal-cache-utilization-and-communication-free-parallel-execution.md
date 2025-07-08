---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Combination generators with optimal cache utilization and communication
  free parallel execution"
date: 2025-07-08T00:00:00
---

**Authors:** [Xi He](https://dblp.uni-trier.de/search?q=Xi+He), [Max. A. Little](https://dblp.uni-trier.de/search?q=Max.+A.+Little)

We introduce an efficient and elegant combination generator for producing all
combinations of size less than or equal to K, designed for exhaustive
generation and combinatorial optimization tasks. This generator can be
implemented to achieve what we define as optimal efficiency: constant amortized
time, optimal cache utilization, embarrassingly parallel execution, and a
recursive structure compatible with pruning-based search. These properties are
difficult to satisfy simultaneously in existing generators. For example,
classical Gray code or lexicographic generators are typically list-based and
sequentially defined, making them difficult to vectorized, inefficient in cache
usage, and inherently hard to parallelize. Generators based on unranking
methods, while easy to parallelize, are non-recursive. These limitations reduce
their applicability in our target applications, where both computational
efficiency and recursion are crucial. We adapt Bird's algebra of
programming-style calculation to derive our algorithms, a formalism for
developing correct-by-construction programs from specifications. As a result,
all generators in this paper are first formulated in their clearest
specification, and efficient definitions are derived constructively through
equational reasoning, resulting in concise and elegant divide-and-conquer
definitions. Beyond presenting a combination generator, we extend our approach
to construct generators for K-permutations, nested combinations of
combinations, and nested permutation-combination structures. To the best of our
knowledge, the literature has not previously reported generators for these
nested structures. We also develop sequential variants that produce
configurations in Gray code-compatible orders -- such as the revolving door
ordering -- which are particularly useful for constructing nested generators.

[Read original post](http://arxiv.org/abs/2507.03980v1)
