---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Treedepth Inapproximability and Exponential ETH Lower Bound"
date: 2025-07-21T00:00:00
---

**Authors:** [Édouard Bonnet](https://dblp.uni-trier.de/search?q=%C3%89douard+Bonnet), [Daniel Neuen](https://dblp.uni-trier.de/search?q=Daniel+Neuen), [Marek Sokołowski](https://dblp.uni-trier.de/search?q=Marek+Soko%C5%82owski)

Treedepth is a central parameter to algorithmic graph theory. The current
state-of-the-art in computing and approximating treedepth consists of a
$2^{O(k^2)} n$-time exact algorithm and a polynomial-time $O(\text{OPT}
\log^{3/2} \text{OPT})$-approximation algorithm, where the former algorithm
returns an elimination forest of height $k$ (witnessing that treedepth is at
most $k$) for the $n$-vertex input graph $G$, or correctly reports that $G$ has
treedepth larger than $k$, and $\text{OPT}$ is the actual value of the
treedepth. On the complexity side, exactly computing treedepth is NP-complete,
but the known reductions do not rule out a polynomial-time approximation scheme
(PTAS), and under the Exponential Time Hypothesis (ETH) only exclude a running
time of $2^{o(\sqrt n)}$ for exact algorithms.
We show that 1.0003-approximating treedepth is NP-hard, and that exactly
computing the treedepth of an $n$-vertex graph requires time $2^{\Omega(n)}$,
unless the ETH fails. We further derive that there exist absolute constants
$\delta, c > 0$ such that any $(1+\delta)$-approximation algorithm requires
time $2^{\Omega(n / \log^c n)}$. We do so via a simple direct reduction from
Satisfiability to Treedepth, inspired by a reduction recently designed for
Treewidth [STOC '25].

[Read original post](http://arxiv.org/abs/2507.13818v1)
