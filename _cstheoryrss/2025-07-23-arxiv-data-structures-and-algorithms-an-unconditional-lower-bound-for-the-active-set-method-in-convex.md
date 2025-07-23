---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: An unconditional lower bound for the active-set method in convex"
date: 2025-07-23T00:00:00
---

**Authors:** [Eleon Bach](https://dblp.uni-trier.de/search?q=Eleon+Bach), [Yann Disser](https://dblp.uni-trier.de/search?q=Yann+Disser), [Sophie Huiberts](https://dblp.uni-trier.de/search?q=Sophie+Huiberts), [Nils Mosis](https://dblp.uni-trier.de/search?q=Nils+Mosis)

We prove that the active-set method needs an exponential number of iterations
in the worst-case to maximize a convex quadratic function subject to linear
constraints, regardless of the pivot rule used. This substantially improves
over the best previously known lower bound [IPCO 2025], which needs objective
functions of polynomial degrees $\omega(\log d)$ in dimension $d$, to a bound
using a convex polynomial of degree 2. In particular, our result firmly
resolves the open question [IPCO 2025] of whether a constant degree suffices,
and it represents significant progress towards linear objectives, where the
active-set method coincides with the simplex method and a lower bound for all
pivot rules would constitute a major breakthrough.
Our result is based on a novel extended formulation, recursively constructed
using deformed products. Its key feature is that it projects onto a polygonal
approximation of a parabola while preserving all of its exponentially many
vertices. We define a quadratic objective that forces the active-set method to
follow the parabolic boundary of this projection, without allowing any
shortcuts along chords corresponding to edges of its full-dimensional preimage.

[Read original post](http://arxiv.org/abs/2507.16648v1)
