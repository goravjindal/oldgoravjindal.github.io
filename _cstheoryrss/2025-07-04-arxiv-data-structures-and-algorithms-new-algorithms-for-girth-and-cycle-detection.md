---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: New algorithms for girth and cycle detection"
date: 2025-07-04T00:00:00
---

**Authors:** [Liam Roditty](https://dblp.uni-trier.de/search?q=Liam+Roditty), [Plia Trabelsi](https://dblp.uni-trier.de/search?q=Plia+Trabelsi)

Let $G=(V,E)$ be an unweighted undirected graph with $n$ vertices and $m$
edges. Let $g$ be the girth of $G$, that is, the length of a shortest cycle in
$G$. We present a randomized algorithm with a running time of
$\tilde{O}\big(\ell \cdot n^{1 + \frac{1}{\ell - \varepsilon}}\big)$ that
returns a cycle of length at most $ 2\ell \left\lceil \frac{g}{2} \right\rceil
- 2 \left\lfloor \varepsilon \left\lceil \frac{g}{2} \right\rceil
\right\rfloor, $ where $\ell \geq 2$ is an integer and $\varepsilon \in [0,1]$,
for every graph with $g = polylog(n)$.
Our algorithm generalizes an algorithm of Kadria \etal{} [SODA'22] that
computes a cycle of length at most $4\left\lceil \frac{g}{2} \right\rceil -
2\left\lfloor \varepsilon \left\lceil \frac{g}{2} \right\rceil \right\rfloor $
in $\tilde{O}\big(n^{1 + \frac{1}{2 - \varepsilon}}\big)$ time. Kadria \etal{}
presented also an algorithm that finds a cycle of length at most $ 2\ell
\left\lceil \frac{g}{2} \right\rceil $ in $\tilde{O}\big(n^{1 +
\frac{1}{\ell}}\big)$ time, where $\ell$ must be an integer. Our algorithm
generalizes this algorithm, as well, by replacing the integer parameter $\ell$
in the running time exponent with a real-valued parameter $\ell - \varepsilon$,
thereby offering greater flexibility in parameter selection and enabling a
broader spectrum of combinations between running times and cycle lengths.
We also show that for sparse graphs a better tradeoff is possible, by
presenting an $\tilde{O}(\ell\cdot m^{1+1/(\ell-\varepsilon)})$ time randomized
algorithm that returns a cycle of length at most $2\ell(\lfloor
\frac{g-1}{2}\rfloor) - 2(\lfloor \varepsilon \lfloor \frac{g-1}{2}\rfloor
\rfloor+1)$, where $\ell\geq 3$ is an integer and $\varepsilon\in [0,1)$, for
every graph with $g=polylog(n)$.
To obtain our algorithms we develop several techniques and introduce a formal
definition of hybrid cycle detection algorithms. [...]

[Read original post](http://arxiv.org/abs/2507.02061v1)
