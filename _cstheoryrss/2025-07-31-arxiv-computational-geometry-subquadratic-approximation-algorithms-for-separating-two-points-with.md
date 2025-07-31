---
layout: post
category: cstheoryrss
title: "arXiv: Computational Geometry: Subquadratic Approximation Algorithms for Separating Two Points with"
date: 2025-07-31T00:00:00
---

**Authors:** [Jayson Lynch](https://dblp.uni-trier.de/search?q=Jayson+Lynch), [Jack Spalding-Jamieson](https://dblp.uni-trier.de/search?q=Jack+Spalding-Jamieson)

The (unweighted) point-separation} problem asks, given a pair of points $s$
and $t$ in the plane, and a set of candidate geometric objects, for the
minimum-size subset of objects whose union blocks all paths from $s$ to $t$.
Recent work has shown that the point-separation problem can be characterized as
a type of shortest-path problem in a geometric intersection graph within a
special lifted space. However, all known solutions to this problem essentially
reduce to some form of APSP, and hence take at least quadratic time, even for
special object types.
In this work, we consider the unweighted form of the problem, for which we
devise subquadratic approximation algorithms for many special cases of objects,
including line segments and disks. In this paradigm, we are able to devise
algorithms that are fundamentally different from the APSP-based approach. In
particular, we will give Monte Carlo randomized additive $+1$ approximation
algorithms running in $\widetilde{\mathcal{O}}(n^{\frac32})$ time for disks as
well as axis-aligned line segments and rectangles, and
$\widetilde{\mathcal{O}}(n^{\frac{11}6})$ time for line segments and
constant-complexity convex polygons. We will also give deterministic
multiplicative-additive approximation algorithms that, for any value
$\varepsilon>0$, guarantee a solution of size $(1+\varepsilon)\text{OPT}+1$
while running in $\widetilde{\mathcal{O}}\left(\frac{n}{\varepsilon^2}\right)$
time for disks as well as axis-aligned line segments and rectangles, and
$\widetilde{\mathcal{O}}\left(\frac{n^{4/3}}{\epsilon^2}\right)$ time for line
segments and constant-complexity convex polygons.

[Read original post](http://arxiv.org/abs/2507.22293v1)
