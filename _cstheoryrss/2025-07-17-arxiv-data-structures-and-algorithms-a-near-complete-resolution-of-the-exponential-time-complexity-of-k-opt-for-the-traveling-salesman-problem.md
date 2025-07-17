---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: A near-complete resolution of the exponential-time complexity of k-opt
  for the traveling salesman problem"
date: 2025-07-17T00:00:00
---

**Authors:** [Sophia Heimann](https://dblp.uni-trier.de/search?q=Sophia+Heimann), [Hung P. Hoang](https://dblp.uni-trier.de/search?q=Hung+P.+Hoang), [Stefan Hougardy](https://dblp.uni-trier.de/search?q=Stefan+Hougardy)

The $k$-opt algorithm is one of the simplest and most widely used heuristics
for solving the traveling salesman problem. Starting from an arbitrary tour,
the $k$-opt algorithm improves the current tour in each iteration by exchanging
up to $k$ edges. The algorithm continues until no further improvement of this
kind is possible. For a long time, it remained an open question how many
iterations the $k$-opt algorithm might require for small values of $k$,
assuming the use of an optimal pivot rule. In this paper, we resolve this
question for the cases $k = 3$ and $k = 4$ by proving that in both these cases
an exponential number of iterations may be needed even if an optimal pivot rule
is used. Combined with a recent result from Heimann, Hoang, and Hougardy (ICALP
2024), this provides a complete answer for all $k \geq 3$ regarding the number
of iterations the $k$-opt algorithm may require under an optimal pivot rule. In
addition we establish an analogous exponential lower bound for the 2.5-opt
algorithm, a variant that generalizes 2-opt and is a restricted version of
3-opt. All our results hold for both the general and the metric traveling
salesman problem.

[Read original post](http://arxiv.org/abs/2507.12304v1)
