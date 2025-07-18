---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Maintaining Routing Structures under Deletions via Self-Pruning"
date: 2025-07-18T00:00:00
---

**Authors:** [Bernhard Haeupler](https://dblp.uni-trier.de/search?q=Bernhard+Haeupler), [Antti Roeyskoe](https://dblp.uni-trier.de/search?q=Antti+Roeyskoe)

Expanders are powerful algorithmic structures with two key properties: they
are
a) routable: for any multi-commodity flow unit demand, there exists a routing
with low congestion over short paths, where a demand is unit if the amount of
demand sent / received by any vertex is at most the number of edges adjacent to
it.
b) stable / prunable: for any (sequence of) edge failures, there exists a
proportionally small subset of vertices that can be disabled, such that the
graph induced on the remaining vertices is an expander.
Two natural algorithmic problems correspond to these two existential
guarantees: expander routing, i.e. computing a low-congestion routing for a
unit multi-commodity demand on an expander, and expander pruning, i.e.,
maintaining the subset of disabled vertices under a sequence of edge failures.
This paper considers the combination of the two problems: maintaining a
routing for a unit multi-commodity demand under pruning steps. This is done
through the introduction of a family of expander graphs that, like hypercubes,
are easy to route in, and are self-pruning: for an online sequence of edge
deletions, a simple self-contained algorithm can find a few vertices to prune
with each edge deletion, such that the remaining graph always remains an
easy-to-route-in expander in the family.
Notably, and with considerable technical work, this self-pruning can be made
worst-case, i.e., such that every single adversarial deletion only causes a
small number of additional deletions. Our results also allow tight
constant-factor control over the length of routing paths (with the usual
trade-offs in congestion and pruning ratio) and therefore extend to
constant-hop and length-constrained expanders in which routing over constant
length paths is crucial.

[Read original post](http://arxiv.org/abs/2507.13044v1)
