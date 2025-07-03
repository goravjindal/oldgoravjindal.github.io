---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: On the (In)Approximability of the Monitoring Edge Geodetic Set Problem"
date: 2025-07-02T00:00:00
---

**Authors:** [Davide Bilò](https://dblp.uni-trier.de/search?q=Davide+Bil%C3%B2), [Giodano Colli](https://dblp.uni-trier.de/search?q=Giodano+Colli), [Luca Forlizzi](https://dblp.uni-trier.de/search?q=Luca+Forlizzi), [Stefano Leucci](https://dblp.uni-trier.de/search?q=Stefano+Leucci)

We study the minimum \emph{Monitoring Edge Geodetic Set} (\megset) problem
introduced in [Foucaud et al., CALDAM'23]: given a graph $G$, we say that an
edge is monitored by a pair $u,v$ of vertices if \emph{all} shortest paths
between $u$ and $v$ traverse $e$; the goal of the problem consists in finding a
subset $M$ of vertices of $G$ such that each edge of $G$ is monitored by at
least one pair of vertices in $M$, and $|M|$ is minimized.
In this paper, we prove that all polynomial-time approximation algorithms for
the minimum \megset problem must have an approximation ratio of $\Omega(\log
n)$, unless \p = \np. To the best of our knowledge, this is the first
non-constant inapproximability result known for this problem. We also
strengthen the known \np-hardness of the problem on $2$-apex graphs by showing
that the same result holds for $1$-apex graphs. This leaves open the problem of
determining whether the problem remains \np-hard on planar (i.e., $0$-apex)
graphs.
On the positive side, we design an algorithm that computes good approximate
solutions for hereditary graph classes that admit efficiently computable
balanced separators of truly sublinear size. This immediately results in
polynomial-time approximation algorithms achieving an approximation ratio of
$O(n^{\frac{1}{4}} \sqrt{\log n})$ on planar graphs, graphs with bounded genus,
and $k$-apex graphs with $k=O(n^{\frac{1}{4}})$. On graphs with bounded
treewidth, we obtain an approximation ratio of $O(\log^{3/2} n)$ for any
constant $\varepsilon > 0$. This compares favorably with the best-known
approximation algorithm for general graphs, which achieves an approximation
ratio of $O(\sqrt{n \log n})$ via a simple reduction to the \textsc{Set Cover}
problem.