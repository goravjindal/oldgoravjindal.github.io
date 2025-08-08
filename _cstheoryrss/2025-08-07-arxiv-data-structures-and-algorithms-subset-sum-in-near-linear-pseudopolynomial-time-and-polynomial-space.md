---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Subset Sum in Near-Linear Pseudopolynomial Time and Polynomial Space"
date: 2025-08-07T00:00:00
---

**Authors:** [Thejas Radhika Sajith](https://dblp.uni-trier.de/search?q=Thejas+Radhika+Sajith)

Given a multiset $A = \{a\_1, \dots, a\_n\}$ of positive integers and a target
integer $t$, the Subset Sum problem asks if there is a subset of $A$ that sums
to $t$. Bellman's [1957] classical dynamic programming algorithm runs in
$O(nt)$ time and $O(t)$ space. Since then, there have been multiple
improvements in both time and space complexity.
Notably, Bringmann [SODA 2017] uses a two-step color-coding technique to
obtain a randomized algorithm that runs in $\tilde{O}(n+t)$ time and
$\tilde{O}(t)$ space. On the other hand, there are polynomial space algorithms
-- for example, Jin, Vyas and Williams [SODA 2021] build upon the algorithm
given by Bringmann, using a clever algebraic trick first seen in Kane's
Logspace algorithm, to obtain an $\tilde{O}(nt)$ time and $\tilde{O}(\log(nt))$
space algorithm. A natural question, asked by Jin et al. is if there is an
$\tilde{O}(n+t)$ time algorithm running in poly$(n, \log t)$ space. Another
natural question is whether it is possible to construct a deterministic
polynomial space algorithm with time complexity comparable to that of
Bellman's.
In this paper, we answer both questions affirmatively. We build on the
framework given by Jin et al., using a multipoint evaluation-based approach to
speed up a bottleneck step in their algorithm. We construct a deterministic
algorithm that runs in $\tilde{O}(nt)$ time and $\tilde{O}(n \log^2 t)$ space
and a randomized algorithm that runs in $\tilde{O}(n+t)$ time and
$\tilde{O}(n^2 + n \log^2 t)$ space.

[Read original post](http://arxiv.org/abs/2508.04726v1)
