---
layout: post
category: cstheoryrss
title: "arXiv: Computational Geometry: A New Approach to the Construction of Subdivision Algorithms"
date: 2025-07-25T00:00:00
---

**Authors:** [Alexander Dietz](https://dblp.uni-trier.de/search?q=Alexander+Dietz)

In this thesis, a new approach for constructing subdivision algorithms for
generalized quadratic and cubic B-spline subdivision for subdivision surfaces
and volumes is presented. First, a catalog of quality criteria for these
subdivision algorithms is developed, serving as a guideline for the
construction process.
The construction begins by generating the desired subdominant eigenvectors as
the vertices of regular convex 3-polytopes for volumes using circle packings.
Subsequently, these polytopes are utilized to construct a
Colin-de-Verdiere-matrix for the generalized quadratic and a
Colin-de-Verdiere-like matrix for the generalized cubic B-spline subdivision.
These matrices are then adjusted using the matrix exponential to obtain
subdivision matrices with the desired properties.
All subdivision algorithms introduced in this paper empirically exhibit a
subdominant eigenvalue of 1/2 with the desired algebraic and geometric
multiplicity. For the quadratic case, this property can even be formally
proven. Moreover, the corresponding eigenvectors form a convex polytope in the
central region for the generalized quadratic B-spline subdivision algorithms,
while for the generalized cubic B-spline subdivision algorithms, they represent
the refinement of a convex polytope. Additionally, the constructed subdivision
algorithms fulfill various other quality criteria, such as affine invariance
and convex hull preservation and respecting all symmetries. Furthermore, it is
demonstrated that the original Catmull-Clark algorithm is not suitable for
generalization to volumetric subdivision and that the established subdivision
algorithms [Baj+02] and [JM99] do not exhibit a suitable spectrum for several
combinatorial configurations. Additionally, research approaches for the
volumetric case are proposed, aiming to generalize from hexahedral to arbitrary
structures.

[Read original post](http://arxiv.org/abs/2507.20897v1)
