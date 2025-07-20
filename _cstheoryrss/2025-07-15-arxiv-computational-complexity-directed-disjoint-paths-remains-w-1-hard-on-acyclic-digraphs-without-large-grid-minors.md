---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: Directed disjoint paths remains W[1]-hard on acyclic digraphs without"
date: 2025-07-15T00:00:00
---

**Authors:** [Ken-ichi Kawarabayashi](https://dblp.uni-trier.de/search?q=Ken-ichi+Kawarabayashi), [Nicola Lorenz](https://dblp.uni-trier.de/search?q=Nicola+Lorenz), [Marcelo Garlet Milani](https://dblp.uni-trier.de/search?q=Marcelo+Garlet+Milani), [Jacob Stegemann](https://dblp.uni-trier.de/search?q=Jacob+Stegemann)

In the Vertex Disjoint Paths with Congestion problem, the input consists of a
digraph $D$, an integer $c$ and $k$ pairs of vertices $(s\_i, t\_i)$, and the
task is to find a set of paths connecting each $s\_i$ to its corresponding
$t\_i$, whereas each vertex of $D$ appears in at most $c$ many paths. The case
where $c = 1$ is known to be NP-complete even if $k = 2$ [Fortune, Hopcroft and
Wyllie, 1980] on general digraphs and is W[1]-hard with respect to $k$
(excluding the possibility of an $f(k)n^{O(1)}$-time algorithm under standard
assumptions) on acyclic digraphs [Slivkins, 2010]. The proof of [Slivkins,
2010] can also be adapted to show W[1]-hardness with respect to $k$ for every
congestion $c \geq 1$.
We strengthen the existing hardness result by showing that the problem
remains W[1]-hard for every congestion $c \geq 1$ even if:
- the input digraph $D$ is acyclic,
- $D$ does not contain an acyclic $(5, 5)$-grid as a butterfly minor,
- $D$ does not contain an acyclic tournament on 9 vertices as a butterfly
minor, and
- $D$ has ear-anonymity at most 5.
Further, we also show that the edge-congestion variant of the problem remains
W[1]-hard for every congestion $c \geq 1$ even if:
- the input digraph $D$ is acyclic,
- $D$ has maximum undirected degree 3,
- $D$ does not contain an acyclic $(7, 7)$-wall as a weak immersion and
- $D$ has ear-anonymity at most 5.

[Read original post](http://arxiv.org/abs/2507.09868v1)
