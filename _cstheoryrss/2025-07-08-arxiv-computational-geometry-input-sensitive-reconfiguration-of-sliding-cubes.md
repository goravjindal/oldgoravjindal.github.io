---
layout: post
category: cstheoryrss
title: "arXiv: Computational Geometry: Input-Sensitive Reconfiguration of Sliding Cubes"
date: 2025-07-08T00:00:00
---

**Authors:** [Hugo Akitaya](https://dblp.uni-trier.de/search?q=Hugo+Akitaya), [Matias Korman](https://dblp.uni-trier.de/search?q=Matias+Korman), [Frederick Stock](https://dblp.uni-trier.de/search?q=Frederick+Stock)

A configuration of $n$ unit-cube-shaped \textit{modules} (or \textit{robots})
is a lattice-aligned placement of the $n$ modules so that their union is
face-connected. The reconfiguration problem aims at finding a sequence of moves
that reconfigures the modules from one given configuration to another. The
sliding cube model (in which modules are allowed to slide over the face or edge
of neighboring modules) is one of the most studied theoretical models for
modular robots.
In the sliding cubes model we can reconfigure between any two shapes in
$O(n^2)$ moves ([Abel \textit{et al.} SoCG 2024]). If we are interested in a
reconfiguration algorithm into a \textit{compact configuration}, the number of
moves can be reduced to the sum of coordinates of the input configuration (a
number that ranges from $\Omega(n^{4/3})$ to $O(n^2)$, [Kostitsyna \textit{et
al.} SWAT 2024]). We introduce a new algorithm that combines both universal
reconfiguration and an input-sensitive bound on the sum of coordinates of both
configurations, with additional advantages, such as $O(1)$ amortized
computation per move.

[Read original post](http://arxiv.org/abs/2507.04170v1)
