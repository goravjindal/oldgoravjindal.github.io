---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Improved Algorithms for Effective Resistance Computation on Graphs"
date: 2025-07-08T00:00:00
---

**Authors:** [Yichun Yang](https://dblp.uni-trier.de/search?q=Yichun+Yang), [Rong-Hua Li](https://dblp.uni-trier.de/search?q=Rong-Hua+Li), [Meihao Liao](https://dblp.uni-trier.de/search?q=Meihao+Liao), [Guoren Wang](https://dblp.uni-trier.de/search?q=Guoren+Wang)

Effective Resistance (ER) is a fundamental tool in various graph learning
tasks. In this paper, we address the problem of efficiently approximating ER on
a graph $\mathcal{G}=(\mathcal{V},\mathcal{E})$ with $n$ vertices and $m$
edges. First, we focus on local online-computation algorithms for ER
approximation, aiming to improve the dependency on the approximation error
parameter $\epsilon$. Specifically, for a given vertex pair $(s,t)$, we propose
a local algorithm with a time complexity of $\tilde{O}(\sqrt{d}/\epsilon)$ to
compute an $\epsilon$-approximation of the $s,t$-ER value for expander graphs,
where $d=\min \{d\_s,d\_t\}$. This improves upon the previous state-of-the-art,
including an $\tilde{O}(1/\epsilon^2)$ time algorithm based on random walk
sampling by Andoni et al. (ITCS'19) and Peng et al. (KDD'21). Our method
achieves this improvement by combining deterministic search with random walk
sampling to reduce variance. Second, we establish a lower bound for ER
approximation on expander graphs. We prove that for any $\epsilon\in (0,1)$,
there exist an expander graph and a vertex pair $(s,t)$ such that any local
algorithm requires at least $\Omega(1/\epsilon)$ time to compute the
$\epsilon$-approximation of the $s,t$-ER value. Finally, we extend our
techniques to index-based algorithms for ER computation. We propose an
algorithm with $\tilde{O}(\min \{m+n/\epsilon^{1.5},\sqrt{nm}/\epsilon\})$
processing time, $\tilde{O}(n/\epsilon)$ space complexity and $O(1)$ query
complexity, which returns an $\epsilon$-approximation of the $s,t$-ER value for
any $s,t\in \mathcal{V}$ for expander graphs. Our approach improves upon the
state-of-the-art $\tilde{O}(m/\epsilon)$ processing time by Dwaraknath et al.
(NeurIPS'24) and the $\tilde{O}(m+n/\epsilon^2)$ processing time by Li and
Sachdeva (SODA'23).

[Read original post](http://arxiv.org/abs/2507.04674v1)
