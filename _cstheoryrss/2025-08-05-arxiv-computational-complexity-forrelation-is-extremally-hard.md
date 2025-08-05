---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: Forrelation is Extremally Hard"
date: 2025-08-05T00:00:00
---

**Authors:** [Uma Girish](https://dblp.uni-trier.de/search?q=Uma+Girish), [Rocco Servedio](https://dblp.uni-trier.de/search?q=Rocco+Servedio)

The Forrelation problem is a central problem that demonstrates an exponential
separation between quantum and classical capabilities. In this problem, given
query access to $n$-bit Boolean functions $f$ and $g$, the goal is to estimate
the Forrelation function $\mathrm{forr}(f,g)$, which measures the correlation
between $g$ and the Fourier transform of $f$.
In this work we provide a new linear algebraic perspective on the Forrelation
problem, as opposed to prior analytic approaches. We establish a connection
between the Forrelation problem and bent Boolean functions and through this
connection, analyze an extremal version of the Forrelation problem where the
goal is to distinguish between extremal instances of Forrelation, namely
$(f,g)$ with $\mathrm{forr}(f,g)=1$ and $\mathrm{forr}(f,g)=-1$.
We show that this problem can be solved with one quantum query and success
probability one, yet requires $\tilde{\Omega}\left(2^{n/4}\right)$ classical
randomized queries, even for algorithms with a one-third failure probability,
highlighting the remarkable power of one exact quantum query. We also study a
restricted variant of this problem where the inputs $f,g$ are computable by
small classical circuits and show classical hardness under cryptographic
assumptions.

[Read original post](http://arxiv.org/abs/2508.02514v1)
