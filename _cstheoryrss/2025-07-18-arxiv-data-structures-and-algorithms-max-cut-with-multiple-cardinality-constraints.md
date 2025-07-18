---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Max-Cut with Multiple Cardinality Constraints"
date: 2025-07-18T00:00:00
---

**Authors:** [Yury Makarychev](https://dblp.uni-trier.de/search?q=Yury+Makarychev), [Madhusudhan Reddy Pittu](https://dblp.uni-trier.de/search?q=Madhusudhan+Reddy+Pittu), [Ali Vakilian](https://dblp.uni-trier.de/search?q=Ali+Vakilian)

We study the classic Max-Cut problem under multiple cardinality constraints,
which we refer to as the Constrained Max-Cut problem. Given a graph $G=(V, E)$,
a partition of the vertices into $c$ disjoint parts $V\_1, \ldots, V\_c$, and
cardinality parameters $k\_1, \ldots, k\_c$, the goal is to select a set $S
\subseteq V$ such that $|S \cap V\_i| = k\_i$ for each $i \in [c]$, maximizing
the total weight of edges crossing $S$ (i.e., edges with exactly one endpoint
in $S$).
By designing an approximate kernel for Constrained Max-Cut and building on
the correlation rounding technique of Raghavendra and Tan (2012), we present a
$(0.858 - \varepsilon)$-approximation algorithm for the problem when $c =
O(1)$. The algorithm runs in time $O\left(\min\{k/\varepsilon,
n\}^{\poly(c/\varepsilon)} + \poly(n)\right)$, where $k = \sum\_{i \in [c]} k\_i$
and $n=|V|$. This improves upon the $(\frac{1}{2} +
\varepsilon\_0)$-approximation of Feige and Langberg (2001) for $\maxcut\_k$ (the
special case when $c=1, k\_1 = k$), and generalizes the $(0.858 -
\varepsilon)$-approximation of Raghavendra and Tan (2012), which only applies
when $\min\{k,n-k\}=\Omega(n)$ and does not handle multiple constraints.
We also establish that, for general values of $c$, it is NP-hard to determine
whether a feasible solution exists that cuts all edges. Finally, we present a
$1/2$-approximation algorithm for Max-Cut under an arbitrary matroid
constraint.

[Read original post](http://arxiv.org/abs/2507.12607v1)
