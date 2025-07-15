---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Computing the probability of intersection"
date: 2025-07-15T00:00:00
---

**Authors:** [Alexander Barvinok](https://dblp.uni-trier.de/search?q=Alexander+Barvinok)

Let $\Omega\_1, \ldots, \Omega\_m$ be probability spaces, let $\Omega=\Omega\_1
\times \cdots \times \Omega\_m$ be their product and let $A\_1, \ldots, A\_n
\subset \Omega$ be events. Suppose that each event $A\_i$ depends on $r\_i$
coordinates of a point $x \in \Omega$, $x=\left(\xi\_1, \ldots, \xi\_m\right)$,
and that for each event $A\_i$ there are $\Delta\_i$ of other events $A\_j$ that
depend on some of the coordinates that $A\_i$ depends on. Let $\Delta=\max\{5,\
\Delta\_i: i=1, \ldots, n\}$ and let $\mu\_i=\min\{r\_i,\ \Delta\_i+1\}$ for $i=1,
\ldots, n$. We prove that if $P(A\_i) < (3\Delta)^{-3\mu\_i}$ for all $I$, then
for any $0 < \epsilon < 1$, the probability $P\left( \bigcap\_{i=1}^n
\overline{A}\_i\right)$ of the intersection of the complements of all $A\_i$ can
be computed within relative error $\epsilon$ in polynomial time from the
probabilities $P\left(A\_{i\_1} \cap \ldots \cap A\_{i\_k}\right)$ of $k$-wise
intersections of the events $A\_i$ for $k = e^{O(\Delta)} \ln (n/\epsilon)$.

[Read original post](http://arxiv.org/abs/2507.10329v1)
