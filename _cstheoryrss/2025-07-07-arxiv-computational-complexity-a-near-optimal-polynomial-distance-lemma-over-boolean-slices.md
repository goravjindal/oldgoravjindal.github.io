---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: A Near-Optimal Polynomial Distance Lemma Over Boolean Slices"
date: 2025-07-07T00:00:00
---

**Authors:** [Prashanth Amireddy](https://dblp.uni-trier.de/search?q=Prashanth+Amireddy), [Amik Raj Behera](https://dblp.uni-trier.de/search?q=Amik+Raj+Behera), [Srikanth Srinivasan](https://dblp.uni-trier.de/search?q=Srikanth+Srinivasan), [Madhu Sudan](https://dblp.uni-trier.de/search?q=Madhu+Sudan)

The celebrated Ore-DeMillo-Lipton-Schwartz-Zippel (ODLSZ) lemma asserts that
n-variate non-zero polynomial functions of degree d over a field $\mathbb{F}$
are non-zero over any "grid" $S^n$ for finite subset $S \subseteq \mathbb{F}$,
with probability at least $\max\{|S|^{-d/(|S|-1)},1-d/|S|\}$ over the choice of
random point from the grid. In particular, over the Boolean cube ($S = \{0,1\}
\subseteq \mathbb{F}$), the lemma asserts non-zero polynomials are non-zero
with probability at least $2^{-d}$. In this work we extend the ODLSZ lemma
optimally (up to lower-order terms) to "Boolean slices" i.e., points of Hamming
weight exactly $k$. We show that non-zero polynomials on the slice are non-zero
with probability $(t/n)^{d}(1 - o\_{n}(1))$ where $t = \min\{k,n-k\}$ for every
$d\leq k\leq (n-d)$. As with the ODLSZ lemma, our results extend to polynomials
over Abelian groups. This bound is tight (upto the error term) as evidenced by
degree d multilinear monomials. A particularly interesting case is the
"balanced slice" ($k=n/2$) where our lemma asserts that non-zero polynomials
are non-zero with roughly the same probability on the slice as on the whole
cube.
The behaviour of low-degree polynomials over Boolean slices has received much
attention in recent years. However, the problem of proving a tight version of
the ODLSZ lemma does not seem to have been considered before, except for a
recent work of Amireddy, Behera, Paraashar, Srinivasan and Sudan (SODA 2025)
who established a sub-optimal bound of approximately $((k/n)\cdot(1-(k/n)))^d$
using a proof similar to that of the standard ODLSZ lemma.
While the statement of our result mimics that of the ODLSZ lemma, our proof
is significantly more intricate and involves spectral reasoning which is
employed to show that a natural way of embedding a copy of the Boolean cube
inside a balanced Boolean slice is a good sampler.

[Read original post](http://arxiv.org/abs/2507.03193v1)
