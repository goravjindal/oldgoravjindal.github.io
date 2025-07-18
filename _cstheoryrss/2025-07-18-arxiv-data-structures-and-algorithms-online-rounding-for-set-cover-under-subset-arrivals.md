---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Online Rounding for Set Cover under Subset Arrivals"
date: 2025-07-18T00:00:00
---

**Authors:** [Jarosław Byrka](https://dblp.uni-trier.de/search?q=Jaros%C5%82aw+Byrka), [Yongho Shin](https://dblp.uni-trier.de/search?q=Yongho+Shin)

A rounding scheme for set cover has served as an important component in
design of approximation algorithms for the problem, and there exists an
H\_s-approximate rounding scheme, where s denotes the maximum subset size,
directly implying an approximation algorithm with the same approximation
guarantee. A rounding scheme has also been considered under some online models,
and in particular, under the element arrival model used as a crucial subroutine
in algorithms for online set cover, an O(log s)-competitive rounding scheme is
known [Buchbinder, Chen, and Naor, SODA 2014]. On the other hand, under a more
general model, called the subset arrival model, only a simple O(log
n)-competitive rounding scheme is known, where n denotes the number of elements
in the ground set.
In this paper, we present an O(log^2 s)-competitive rounding scheme under the
subset arrival model, with one mild assumption that s is known upfront. Using
our rounding scheme, we immediately obtain an O(log^2 s)-approximation
algorithm for multi-stage stochastic set cover, improving upon the existing
algorithms [Swamy and Shmoys, SICOMP 2012; Byrka and Srinivasan, SIDMA 2018]
when s is small enough compared to the number of stages and the number of
elements. Lastly, for set cover with s = 2, also known as edge cover, we
present a 1.8-competitive rounding scheme under the edge arrival model.

[Read original post](http://arxiv.org/abs/2507.13159v1)
