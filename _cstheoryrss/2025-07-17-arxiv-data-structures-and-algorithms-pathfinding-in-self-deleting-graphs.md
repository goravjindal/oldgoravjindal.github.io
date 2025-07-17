---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Pathfinding in Self-Deleting Graphs"
date: 2025-07-17T00:00:00
---

**Authors:** [Michal Dvořák](https://dblp.uni-trier.de/search?q=Michal+Dvo%C5%99%C3%A1k), [Dušan Knop](https://dblp.uni-trier.de/search?q=Du%C5%A1an+Knop), [Michal Opler](https://dblp.uni-trier.de/search?q=Michal+Opler), [Jan Pokorný](https://dblp.uni-trier.de/search?q=Jan+Pokorn%C3%BD), [Ondřej Suchý](https://dblp.uni-trier.de/search?q=Ond%C5%99ej+Such%C3%BD), [Krisztina Szilágyi](https://dblp.uni-trier.de/search?q=Krisztina+Szil%C3%A1gyi)

In this paper, we study the problem of pathfinding on traversal-dependent
graphs, i.e., graphs whose edges change depending on the previously visited
vertices. In particular, we study \emph{self-deleting graphs}, introduced by
Carmesin et al. (Sarah Carmesin, David Woller, David Parker, Miroslav Kulich,
and Masoumeh Mansouri. The Hamiltonian cycle and travelling salesperson
problems with traversal-dependent edge deletion. J. Comput. Sci.), which
consist of a graph $G=(V, E)$ and a function $f\colon V\rightarrow 2^E$, where
$f(v)$ is the set of edges that will be deleted after visiting the vertex $v$.
In the \textsc{(Shortest) Self-Deleting $s$-$t$-path} problem we are given a
self-deleting graph and its vertices $s$ and $t$, and we are asked to find a
(shortest) path from $s$ to $t$, such that it does not traverse an edge in
$f(v)$ after visiting $v$ for any vertex $v$.
We prove that \textsc{Self-Deleting $s$-$t$-path} is NP-hard even if the
given graph is outerplanar, bipartite, has maximum degree $3$, bandwidth $2$
and $|f(v)|\leq 1$ for each vertex $v$. We show that \textsc{Shortest
Self-Deleting $s$-$t$-path} is W[1]-complete parameterized by the length of the
sought path and that \textsc{Self-Deleting $s$-$t$-path} is \W{1}-complete
parameterized by the vertex cover number, feedback vertex set number and
treedepth. We also show that the problem becomes FPT when we parameterize by
the maximum size of $f(v)$ and several structural parameters. Lastly, we show
that the problem does not admit a polynomial kernel even for parameterization
by the vertex cover number and the maximum size of $f(v)$ combined already on
2-outerplanar graphs.

[Read original post](http://arxiv.org/abs/2507.12047v1)
