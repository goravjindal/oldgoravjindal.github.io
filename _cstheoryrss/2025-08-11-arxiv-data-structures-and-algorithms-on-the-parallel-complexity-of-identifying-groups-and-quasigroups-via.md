---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: On the Parallel Complexity of Identifying Groups and Quasigroups via"
date: 2025-08-11T00:00:00
---

**Authors:** [Dan Johnson](https://dblp.uni-trier.de/search?q=Dan+Johnson), [Michael Levet](https://dblp.uni-trier.de/search?q=Michael+Levet), [Petr Vojtěchovský](https://dblp.uni-trier.de/search?q=Petr+Vojt%C4%9Bchovsk%C3%BD), [Brett Widholm](https://dblp.uni-trier.de/search?q=Brett+Widholm)

In this paper, we investigate the computational complexity of isomorphism
testing for finite groups and quasigroups, given by their multiplication
tables. We crucially take advantage of their various decompositions to show the
following:
- We first consider the class $\mathcal{C}$ of groups that admit direct
product decompositions, where each indecompsable factor is $O(1)$-generated,
and either perfect or centerless. We show any group in $\mathcal{C}$ is
identified by the $O(1)$-dimensional count-free Weisfeiler--Leman (WL)
algorithm with $O(\log \log n)$ rounds, and the $O(1)$-dimensional counting WL
algorithm with $O(1)$ rounds. Consequently, the isomorphism problem for
$\mathcal{C}$ is in $\textsf{L}$. The previous upper bound for this class was
$\textsf{TC}^{1}$, using $O(\log n)$ rounds of the $O(1)$-dimensional counting
WL (Grochow and Levet, FCT 2023).
- We next consider more generally, the class of groups where each
indecomposable factor is $O(1)$-generated. We exhibit an $\textsf{AC}^{3}$
canonical labeling procedure for this class. Here, we accomplish this by
showing that in the multiplication table model, the direct product
decomposition can be computed in $\textsf{AC}^{3}$, parallelizing the work of
Kayal and Nezhmetdinov (ICALP 2009).
- Isomorphism testing between a central quasigroup $G$ and an arbitrary
quasigroup $H$ is in $\textsf{NC}$. Here, we take advantage of the fact that
central quasigroups admit an affine decomposition in terms of an underlying
Abelian group. Only the trivial bound of $n^{\log(n)+O(1)}$-time was previously
known for isomorphism testing of central quasigroups.

[Read original post](http://arxiv.org/abs/2508.06478v1)
