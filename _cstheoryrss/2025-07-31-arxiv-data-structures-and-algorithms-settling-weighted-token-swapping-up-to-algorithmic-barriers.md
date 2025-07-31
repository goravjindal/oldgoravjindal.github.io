---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Settling Weighted Token Swapping up to Algorithmic Barriers"
date: 2025-07-31T00:00:00
---

**Authors:** [Nicole Wein](https://dblp.uni-trier.de/search?q=Nicole+Wein), [Guanyu](https://dblp.uni-trier.de/search?q=Guanyu), [Zhang](https://dblp.uni-trier.de/search?q=Zhang)

We study the weighted token swapping problem, in which we are given a graph
on $n$ vertices, $n$ weighted tokens, an initial assignment of one token to
each vertex, and a final assignment of one token to each vertex. The goal is to
find a minimum-cost sequence of swaps of adjacent tokens to reach the final
assignment from the initial assignment, where the cost is the sum over all
swaps of the sum of the weights of the two swapped tokens. Unweighted token
swapping has been extensively studied: it is NP-hard to approximate to a factor
better than $14/13$, and there is a polynomial-time 4-approximation, along with
a tight "barrier" result showing that the class of locally optimal algorithms
cannot achieve a ratio better than 4. For trees, the problem remains NP-hard to
solve exactly, and there is a polynomial-time 2-approximation, along with a
tight barrier result showing that the class of $\ell$-straying algorithms
cannot achieve a ratio better than 2. Weighted token swapping with $\{0,1\}$
weights is much harder to approximation: it is NP-hard to approximate even to a
factor of $(1-\varepsilon) \cdot \ln n$ for any constant $\varepsilon>0$.
Restricting to positive weights, no approximation algorithms are known, and the
only known lower bounds are those inherited directly from the unweighted
version. We provide the first approximation algorithms for weighted token
swapping on both trees and general graphs, along with tight barrier results.
Letting $w$ and $W$ be the minimum and maximum token weights, our approximation
ratio is $2+2W/w$ for general graphs and $1+W/w$ for trees.

[Read original post](http://arxiv.org/abs/2507.22450v1)
