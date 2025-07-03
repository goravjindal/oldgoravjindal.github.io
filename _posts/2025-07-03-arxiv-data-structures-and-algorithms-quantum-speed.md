---
layout: post
title: "arXiv: Data Structures and Algorithms: Quantum Speedups for Polynomial-Time Dynamic Programming Algorithms"
date: 2025-07-03 13:21:53 
categories: [rss]
external_link: http://arxiv.org/abs/2507.00823v1
---

**Authors:** [Susanna Caroppo](https://dblp.uni-trier.de/search?q=Susanna+Caroppo), [Giordano Da Lozzo](https://dblp.uni-trier.de/search?q=Giordano+Da+Lozzo), [Giuseppe Di Battista](https://dblp.uni-trier.de/search?q=Giuseppe+Di+Battista), [Michael T. Goodrich](https://dblp.uni-trier.de/search?q=Michael+T.+Goodrich), [Martin Nöllenburg](https://dblp.uni-trier.de/search?q=Martin+N%C3%B6llenburg)

We introduce a quantum dynamic programming framework that allows us to
directly extend to the quantum realm a large body of classical dynamic
programming algorithms. The corresponding quantum dynamic programming
algorithms retain the same space complexity as their classical counterpart,
while achieving a computational speedup. For a combinatorial (search or
optimization) problem $\mathcal P$ and an instance $I$ of $\mathcal P$, such a
speedup can be expressed in terms of the average degree $\delta$ of the
dependency digraph $G\_{\mathcal{P}}(I)$ of $I$, determined by a recursive
formulation of $\mathcal P$. The nodes of this graph are the subproblems of
$\mathcal P$ induced by $I$ and its arcs are directed from each subproblem to
those on whose solution it relies. In particular, our framework allows us to
solve the considered problems in $\tilde{O}(|V(G\_{\mathcal{P}}(I))|
\sqrt{\delta})$ time. As an example, we obtain a quantum version of the
Bellman-Ford algorithm for computing shortest paths from a single source vertex
to all the other vertices in a weighted $n$-vertex digraph with $m$ edges that
runs in $\tilde{O}(n\sqrt{nm})$ time, which improves the best known classical
upper bound when $m \in \Omega(n^{1.4})$.
