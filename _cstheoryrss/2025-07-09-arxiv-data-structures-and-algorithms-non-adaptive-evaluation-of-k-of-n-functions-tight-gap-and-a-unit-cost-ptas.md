---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Non-Adaptive Evaluation of k-of-n Functions: Tight Gap and a"
date: 2025-07-09T00:00:00
---

**Authors:** [Mads Anker Nielsen](https://dblp.uni-trier.de/search?q=Mads+Anker+Nielsen), [Lars Rohwedder](https://dblp.uni-trier.de/search?q=Lars+Rohwedder), [Kevin Schewior](https://dblp.uni-trier.de/search?q=Kevin+Schewior)

We consider the Stochastic Boolean Function Evaluation (SBFE) problem in the
well-studied case of $k$-of-$n$ functions: There are independent Boolean random
variables $x\_1,\dots,x\_n$ where each variable $i$ has a known probability $p\_i$
of taking value $1$, and a known cost $c\_i$ that can be paid to find out its
value. The value of the function is $1$ iff there are at least $k$ $1$s among
the variables. The goal is to efficiently compute a strategy that, at minimum
expected cost, tests the variables until the function value is determined.
While an elegant polynomial-time exact algorithm is known when tests can be
made adaptively, we focus on the non-adaptive variant, for which much less is
known.
First, we show a clean and tight lower bound of $2$ on the adaptivity gap,
i.e., the worst-case multiplicative loss in the objective function caused by
disallowing adaptivity, of the problem. This improves the tight lower bound of
$3/2$ for the unit-cost variant.
Second, we give a PTAS for computing the best non-adaptive strategy in the
unit-cost case, the first PTAS for an SBFE problem. At the core, our scheme
establishes a novel notion of two-sided dominance (w.r.t. the optimal solution)
by guessing so-called milestone tests for a set of carefully chosen buckets of
tests. To turn this technique into a polynomial-time algorithm, we use a
decomposition approach paired with a random-shift argument.

[Read original post](http://arxiv.org/abs/2507.05877v1)
