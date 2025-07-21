---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: An Efficient Massively Parallel Constant-Factor Approximation Algorithm"
date: 2025-07-21T00:00:00
---

**Authors:** [Vincent Cohen-Addad](https://dblp.uni-trier.de/search?q=Vincent+Cohen-Addad), [Fabian Kuhn](https://dblp.uni-trier.de/search?q=Fabian+Kuhn), [Zahra Parsaeian](https://dblp.uni-trier.de/search?q=Zahra+Parsaeian)

In this paper, we present an efficient massively parallel approximation
algorithm for the $k$-means problem. Specifically, we provide an MPC algorithm
that computes a constant-factor approximation to an arbitrary $k$-means
instance in $O(\log\log n \cdot \log\log\log n)$ rounds. The algorithm uses
$O(n^\sigma)$ bits of memory per machine, where $\sigma > 0$ is a constant that
can be made arbitrarily small. The global memory usage is
$O(n^{1+\varepsilon})$ bits for an arbitrarily small constant $\varepsilon >
0$, and is thus only slightly superlinear. Recently, Czumaj, Gao, Jiang,
Krauthgamer, and Vesel\'{y} showed that a constant-factor bicriteria
approximation can be computed in $O(1)$ rounds in the MPC model. However, our
algorithm is the first constant-factor approximation for the general $k$-means
problem that runs in $o(\log n)$ rounds in the MPC model.
Our approach builds upon the foundational framework of Jain and Vazirani. The
core component of our algorithm is a constant-factor approximation for the
related facility location problem. While such an approximation was already
achieved in constant time in the work of Czumaj et al.\ mentioned above, our
version additionally satisfies the so-called Lagrangian Multiplier Preserving
(LMP) property. This property enables the transformation of a facility location
approximation into a comparably good $k$-means approximation.

[Read original post](http://arxiv.org/abs/2507.14089v1)
