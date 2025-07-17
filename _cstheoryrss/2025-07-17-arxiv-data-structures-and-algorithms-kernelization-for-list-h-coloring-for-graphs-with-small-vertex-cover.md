---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Kernelization for list $H$-coloring for graphs with small vertex cover"
date: 2025-07-17T00:00:00
---

**Authors:** [Marta Piecyk](https://dblp.uni-trier.de/search?q=Marta+Piecyk), [Astrid Pieterse](https://dblp.uni-trier.de/search?q=Astrid+Pieterse), [Paweł Rzążewski](https://dblp.uni-trier.de/search?q=Pawe%C5%82+Rz%C4%85%C5%BCewski), [Magnus Wahlström](https://dblp.uni-trier.de/search?q=Magnus+Wahlstr%C3%B6m)

For a fixed graph $H$, in the List $H$-Coloring problem, we are given a graph
$G$ along with list $L(v) \subseteq V(H)$ for every $v \in V(G)$, and we have
to determine if there exists a list homomorphism $\varphi$ from $(G,L)$ to $H$,
i.e., an edge preserving mapping $\varphi: V(G)\to V(H)$ that satisfies
$\varphi(v)\in L(v)$ for every $v\in V(G)$. Note that if $H$ is the complete
graph on $q$ vertices, the problem is equivalent to List $q$-Coloring. We
investigate the kernelization properties of List $H$-Coloring parameterized by
the vertex cover number of $G$: given an instance $(G,L)$ and a vertex cover of
$G$ of size $k$, can we reduce $(G,L)$ to an equivalent instance $(G',L')$ of
List $H$-Coloring where the size of $G'$ is bounded by a low-degree polynomial
$p(k)$ in $k$? This question has been investigated previously by Jansen and
Pieterse [Algorithmica 2019], who provided an upper bound, which turns out to
be optimal if $H$ is a complete graph, i.e., for List $q$-Coloring. This result
was one of the first applications of the method of kernelization via
bounded-degree polynomials. We define two new integral graph invariants,
$c^\*(H)$ and $d^\*(H)$, with $d^\*(H) \leq c^\*(H) \leq d^\*(H)+1$, and show that
for every graph $H$, List $H$-Coloring
-- has a kernel with $\mathcal{O}(k^{c^\*(H)})$ vertices,
-- admits no kernel of size $\mathcal{O}(k^{d^\*(H)-\varepsilon})$ for any
$\varepsilon > 0$, unless the polynomial hierarchy collapses.
-- Furthermore, if $c^\*(H) > d^\*(H)$, then there is a kernel with
$\mathcal{O}(k^{c^\*(H)-\varepsilon})$ vertices where $\varepsilon \geq
2^{1-c^\*(H)}$.
Additionally, we show that for some classes of graphs, including powers of
cycles and graphs $H$ where $\Delta(H) \leq c^\*(H)$ (which in particular
includes cliques), the bound $d^\*(H)$ is tight, using the polynomial method. We
conjecture that this holds in general.

[Read original post](http://arxiv.org/abs/2507.12005v1)
