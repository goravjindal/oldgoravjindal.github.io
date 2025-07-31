---
layout: post
category: cstheoryrss
title: "arXiv: Computational Geometry: Kan Approximations of the Persistent Homology Transform"
date: 2025-07-31T00:00:00
---

**Authors:** [Shreya Arya](https://dblp.uni-trier.de/search?q=Shreya+Arya), [Justin Curry](https://dblp.uni-trier.de/search?q=Justin+Curry)

The persistent homology transform (PHT) of a subset $M \subset \mathbb{R}^d$
is a map $\text{PHT}(M):\mathbb{S}^{d-1} \to \mathbf{Dgm}$ from the unit sphere
to the space of persistence diagrams. This map assigns to each direction $v\in
\mathbb{S}^{d-1}$ the persistent homology of the filtration of $M$ in direction
$v$. In practice, one can only sample the map $\text{PHT}(M)$ at a finite set
of directions $A \subset \mathbb{S}^{d-1}$. This suggests two natural
questions: (1) Can we interpolate the PHT from this finite sample of directions
to the entire sphere? If so, (2) can we prove that the resulting interpolation
is close to the true PHT? In this paper we show that if we can sample the PHT
at the module level, where we have information about how homology from each
direction interacts, a ready-made interpolation theory due to Bubenik, de
Silva, and Nanda using Kan extensions can answer both of these questions in the
affirmative. A close inspection of those techniques shows that we can infer the
PHT from a finite sample of heights from each direction as well. Our paper
presents the first known results for approximating the PHT from finite
directional and scalar data.

[Read original post](http://arxiv.org/abs/2507.22816v1)
