---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Asynchronous Collective Tree Exploration: a Distributed Algorithm, and a"
date: 2025-07-22T00:00:00
---

**Authors:** [Romain Cosson](https://dblp.uni-trier.de/search?q=Romain+Cosson), [Laurent Massoulié](https://dblp.uni-trier.de/search?q=Laurent+Massouli%C3%A9)

We study the problem of collective tree exploration in which a team of $k$
mobile agents must collectively visit all nodes of an unknown tree in as few
moves as possible. The agents all start from the root and discover adjacent
edges as they progress in the tree. Communication is distributed in the sense
that agents share information by reading and writing on whiteboards located at
all nodes. Movements are asynchronous, in the sense that the speeds of all
agents are controlled by an adversary at all times. All previous competitive
guarantees for collective tree exploration are either distributed but
synchronous, or asynchronous but centralized. In contrast, we present a
distributed asynchronous algorithm that explores any tree of $n$ nodes and
depth $D$ in at most $2n+O(k^2 2^kD)$ moves, i.e., with a regret that is linear
in $D$, and a variant algorithm with a guarantee in $O(k/\log k)(n+kD)$, i.e.,
with a competitive ratio in $O(k/\log k)$. We note that our regret guarantee is
asymptotically optimal (i.e., $1$-competitive) from the perspective of
average-case complexity. We then present a new general lower bound on the
competitive ratio of asynchronous collective tree exploration, in
$\Omega(\log^2 k)$. This lower bound applies to both the distributed and
centralized settings, and improves upon the previous lower bound in
$\Omega(\log k)$.

[Read original post](http://arxiv.org/abs/2507.15658v1)
