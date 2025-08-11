---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: The Beauty of Anisotropic Mesh Refinement: Omnitrees for Efficient"
date: 2025-08-11T00:00:00
---

**Authors:** [Theresa Pollinger](https://dblp.uni-trier.de/search?q=Theresa+Pollinger), [Masado Ishii](https://dblp.uni-trier.de/search?q=Masado+Ishii), [Jens Domke](https://dblp.uni-trier.de/search?q=Jens+Domke)

Structured adaptive mesh refinement (AMR), commonly implemented via quadtrees
and octrees, underpins a wide range of applications including databases,
computer graphics, physics simulations, and machine learning. However, octrees
enforce isotropic refinement in regions of interest, which can be especially
inefficient for problems that are intrinsically anisotropic--much resolution is
spent where little information is gained. This paper presents omnitrees as an
anisotropic generalization of octrees and related data structures. Omnitrees
allow to refine only the locally most important dimensions, providing tree
structures that are less deep than bintrees and less wide than octrees. As a
result, the convergence of the AMR schemes can be increased by up to a factor
of the dimensionality d for very anisotropic problems, quickly offsetting their
modest increase in storage overhead. We validate this finding on the problem of
binary shape representation across 4,166 three-dimensional objects: Omnitrees
increase the mean convergence rate by 1.5x, require less storage to achieve
equivalent error bounds, and maximize the information density of the stored
function faster than octrees. These advantages are projected to be even
stronger for higher-dimensional problems. We provide a first validation by
introducing a time-dependent rotation to create four-dimensional
representations, and discuss the properties of their 4-d octree and omnitree
approximations. Overall, omnitree discretizations can make existing AMR
approaches more efficient, and open up new possibilities for high-dimensional
applications.

[Read original post](http://arxiv.org/abs/2508.06316v1)
