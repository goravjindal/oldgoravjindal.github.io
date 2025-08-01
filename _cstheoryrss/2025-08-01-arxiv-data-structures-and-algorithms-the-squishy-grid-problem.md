---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: The Squishy Grid Problem"
date: 2025-08-01T00:00:00
---

**Authors:** [Zixi Cai](https://dblp.uni-trier.de/search?q=Zixi+Cai), [Kuowen Chen](https://dblp.uni-trier.de/search?q=Kuowen+Chen), [Shengquan Du](https://dblp.uni-trier.de/search?q=Shengquan+Du), [Arnold Filtser](https://dblp.uni-trier.de/search?q=Arnold+Filtser), [Seth Pettie](https://dblp.uni-trier.de/search?q=Seth+Pettie), [Daniel Skora](https://dblp.uni-trier.de/search?q=Daniel+Skora)

In this paper we consider the problem of approximating Euclidean distances by
the infinite integer grid graph. Although the topology of the graph is fixed,
we have control over the edge-weight assignment $w:E\to \mathbb{R}\_{\ge 0}$,
and hope to have grid distances be asymptotically isometric to Euclidean
distances, that is, for all grid points $u,v$, $\mathrm{dist}\_w(u,v) = (1\pm
o(1))\|u-v\|\_2$. We give three methods for solving this problem, each
attractive in its own way.
\* Our first construction is based on an embedding of the recursive,
non-periodic pinwheel tiling of Radin and Conway into the integer grid.
Distances in the pinwheel graph are asymptotically isometric to Euclidean
distances, but no explicit bound on the rate of convergence was known. We prove
that the multiplicative distortion of the pinwheel graph is
$(1+1/\Theta(\log^\xi \log D))$, where $D$ is the Euclidean distance and
$\xi=\Theta(1)$. The pinwheel tiling approach is conceptually simple, but can
be improved quantitatively.
\* Our second construction is based on a hierarchical arrangement of
"highways." It is simple, achieving stretch $(1 + 1/\Theta(D^{1/9}))$, which
converges doubly exponentially faster than the pinwheel tiling approach.
\* The first two methods are deterministic. An even simpler approach is to
sample the edge weights independently from a common distribution $\mathscr{D}$.
Whether there exists a distribution $\mathscr{D}^\*$ that makes grid distances
Euclidean, asymptotically and in expectation, is major open problem in the
theory of first passage percolation. Previous experiments show that when
$\mathscr{D}$ is a Fisher distribution, grid distances are within 1\% of
Euclidean. We demonstrate experimentally that this level of accuracy can be
achieved by a simple 2-point distribution that assigns weights 0.41 or 4.75
with probability 44\% and 56\%, respectively.

[Read original post](http://arxiv.org/abs/2507.23105v1)
