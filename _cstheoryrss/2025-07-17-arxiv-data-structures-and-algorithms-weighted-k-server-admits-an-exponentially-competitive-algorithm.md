---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Weighted $k$-Server Admits an Exponentially Competitive Algorithm"
date: 2025-07-17T00:00:00
---

**Authors:** [Adithya Bijoy](https://dblp.uni-trier.de/search?q=Adithya+Bijoy), [Ankit Mondal](https://dblp.uni-trier.de/search?q=Ankit+Mondal), [Ashish Chiplunkar](https://dblp.uni-trier.de/search?q=Ashish+Chiplunkar)

The weighted $k$-server is a variant of the $k$-server problem, where the
cost of moving a server is the server's weight times the distance through which
it moves. The problem is famous for its intriguing properties and for evading
standard techniques for designing and analyzing online algorithms. Even on
uniform metric spaces with sufficiently many points, the deterministic
competitive ratio of weighted $k$-server is known to increase doubly
exponentially with respect to $k$, while the behavior of its randomized
competitive ratio is not fully understood. Specifically, no upper bound better
than doubly exponential is known, while the best known lower bound is singly
exponential in $k$. In this paper, we close the exponential gap between these
bounds by giving an $\exp(O(k^2))$-competitive randomized online algorithm for
the weighted $k$-server problem on uniform metrics, thus breaking the doubly
exponential barrier for deterministic algorithms for the first time. This is
achieved by a recursively defined notion of a phase which, on the one hand,
forces a lower bound on the cost of any offline solution, while, on the other
hand, also admits a randomized online algorithm with bounded expected cost. The
algorithm is also recursive; it involves running several algorithms virtually
and in parallel and following the decisions of one of them in a random order.
We also show that our techniques can be lifted to construct an
$\exp(O(k^2))$-competitive randomized online algorithm for the generalized
$k$-server problem on weighted uniform metrics.

[Read original post](http://arxiv.org/abs/2507.12130v1)
