---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: A 1/2-Approximation for Budgeted k-Submodular Maximization"
date: 2025-07-18T00:00:00
---

**Authors:** [Chenhao Wang](https://dblp.uni-trier.de/search?q=Chenhao+Wang)

A $k$-submodular function naturally generalizes submodular functions by
taking as input $k$ disjoint subsets, rather than a single subset. Unlike
standard submodular maximization, which only requires selecting elements for
the solution, $k$-submodular maximization adds the challenge of determining the
subset to which each selected element belongs. Prior research has shown that
the greedy algorithm is a 1/2-approximation for the monotone $k$-submodular
maximization problem under cardinality or matroid constraints. However, whether
a firm 1/2-approximation exists for the budgeted version (i.e., with a knapsack
constraint) has remained open for several years. We resolve this question
affirmatively by proving that the 1-Guess Greedy algorithm, which first guesses
an appropriate element from an optimal solution before proceeding with the
greedy algorithm, achieves a 1/2-approximation. This result is asymptotically
tight as $((k+1)/(2k)+\epsilon)$-approximation requires exponentially many
value oracle queries even without constraints (Iwata et al., SODA 2016). We
further show that 1-Guess Greedy is 1/3-approximation for the non-monotone
problem. This algorithm is both simple and parallelizable, making it
well-suited for practical applications. Using the thresholding technique from
(Badanidiyuru and Vondrak, SODA 2014), it runs in nearly $\tilde O(n^2k^2)$
time.
The proof idea is simple: we introduce a novel continuous transformation from
an optimal solution to a greedy solution, using the multilinear extension to
evaluate every fractional solution during the transformation. This continuous
analysis approach yields two key extensions. First, it enables improved
approximation ratios of various existing algorithms. Second, our method
naturally extends to $k$-submodular maximization problems under broader
constraints, offering a more flexible and unified analysis framework.

[Read original post](http://arxiv.org/abs/2507.12875v1)
