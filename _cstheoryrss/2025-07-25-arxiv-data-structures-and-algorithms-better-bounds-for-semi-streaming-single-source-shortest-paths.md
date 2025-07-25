---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Better Bounds for Semi-Streaming Single-Source Shortest Paths"
date: 2025-07-25T00:00:00
---

**Authors:** [Sepehr Assadi](https://dblp.uni-trier.de/search?q=Sepehr+Assadi), [Gary Hoppenworth](https://dblp.uni-trier.de/search?q=Gary+Hoppenworth), [Janani Sundaresan](https://dblp.uni-trier.de/search?q=Janani+Sundaresan)

In the semi-streaming model, an algorithm must process any $n$-vertex graph
by making one or few passes over a stream of its edges, use $O(n \cdot
\text{polylog }n)$ words of space, and at the end of the last pass, output a
solution to the problem at hand. Approximating (single-source) shortest paths
on undirected graphs is a longstanding open question in this model. In this
work, we make progress on this question from both upper and lower bound fronts:
We present a simple randomized algorithm that for any $\epsilon > 0$, with
high probability computes $(1+\epsilon)$-approximate shortest paths from a
given source vertex in \[
O\left(\frac{1}{\epsilon} \cdot n \log^3 n \right)~\text{space} \quad
\text{and} \quad O\left(\frac{1}{\epsilon} \cdot \left(\frac{\log n}{\log\log
n} \right) ^2\right) ~\text{passes}.
\] The algorithm can also be derandomized and made to work on dynamic streams
at a cost of some extra $\text{poly}(\log n, 1/\epsilon)$ factors only in the
space. Previously, the best known algorithms for this problem required
$1/\epsilon \cdot \log^{c}(n)$ passes, for an unspecified large constant $c$.
We prove that any semi-streaming algorithm that with large constant
probability outputs any constant approximation to shortest paths from a given
source vertex (even to a single fixed target vertex and only the distance, not
necessarily the path) requires \[ \Omega\left(\frac{\log n}{\log\log n}\right)
~\text{passes}. \] We emphasize that our lower bound holds for any
constant-factor approximation of shortest paths. Previously, only constant-pass
lower bounds were known and only for small approximation ratios below two.
Our results collectively reduce the gap in the pass complexity of
approximating single-source shortest paths in the semi-streaming model from
$\text{polylog } n$ vs $\omega(1)$ to only a quadratic gap.

[Read original post](http://arxiv.org/abs/2507.17841v1)
