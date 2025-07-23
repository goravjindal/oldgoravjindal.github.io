---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Longest Unbordered Factors on Run-Length Encoded Strings"
date: 2025-07-23T00:00:00
---

**Authors:** [Shoma Sekizaki](https://dblp.uni-trier.de/search?q=Shoma+Sekizaki), [Takuya Mieno](https://dblp.uni-trier.de/search?q=Takuya+Mieno)

A border of a string is a non-empty proper prefix of the string that is also
a suffix. A string is unbordered if it has no border. The longest unbordered
factor is a fundamental notion in stringology, closely related to string
periodicity. This paper addresses the longest unbordered factor problem: given
a string of length $n$, the goal is to compute its longest factor that is
unbordered. While recent work has achieved subquadratic and near-linear time
algorithms for this problem, the best known worst-case time complexity remains
$O(n \log n)$ [Kociumaka et al., ISAAC 2018]. In this paper, we investigate the
problem in the context of compressed string processing, particularly focusing
on run-length encoded (RLE) strings. We first present a simple yet crucial
structural observation relating unbordered factors and RLE-compressed strings.
Building on this, we propose an algorithm that solves the problem in $O(m^{1.5}
\log^2 m)$ time and $O(m \log^2 m)$ space, where $m$ is the size of the
RLE-compressed input string. To achieve this, our approach simulates a key idea
from the $O(n^{1.5})$-time algorithm by [Gawrychowski et al., SPIRE 2015],
adapting it to the RLE setting through new combinatorial insights. When the RLE
size $m$ is sufficiently small compared to $n$, our algorithm may show
linear-time behavior in $n$, potentially leading to improved performance over
existing methods in such cases.

[Read original post](http://arxiv.org/abs/2507.16285v1)
