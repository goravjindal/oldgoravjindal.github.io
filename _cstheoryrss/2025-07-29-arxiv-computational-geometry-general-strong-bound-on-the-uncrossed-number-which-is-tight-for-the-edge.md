---
layout: post
category: cstheoryrss
title: "arXiv: Computational Geometry: General Strong Bound on the Uncrossed Number which is Tight for the Edge"
date: 2025-07-29T00:00:00
---

**Authors:** [Gaspard Charvy](https://dblp.uni-trier.de/search?q=Gaspard+Charvy), [Tomáš Masařík](https://dblp.uni-trier.de/search?q=Tom%C3%A1%C5%A1+Masa%C5%99%C3%ADk)

We investigate a very recent concept for visualizing various aspects of a
graph in the plane using a collection of drawings introduced by Hlin\v{e}n\'y
and Masa\v{r}\'ik [GD 2023]. Formally, given a graph $G$, we aim to find an
uncrossed collection containing drawings of $G$ in the plane such that each
edge of $G$ is not crossed in at least one drawing in the collection. The
uncrossed number of $G$ ($unc(G)$) is the smallest integer $k$ such that an
uncrossed collection for $G$ of size $k$ exists. The uncrossed number is
lower-bounded by the well-known thickness, which is an edge-decomposition of
$G$ into planar graphs. This connection gives a trivial lower-bound
$\lceil\frac{|E(G)|}{3|V(G)|-6}\rceil \le unc(G)$. In a recent paper, Balko,
Hlin\v{e}n\'y, Masa\v{r}\'ik, Orthaber, Vogtenhuber, and Wagner [GD 2024]
presented the first non-trivial and general lower-bound on the uncrossed
number. We summarize it in terms of dense graphs (where
$|E(G)|=\epsilon(|V(G)|)^2$ for some $\epsilon>0$):
$\lceil\frac{|E(G)|}{c\_\epsilon|V(G)|}\rceil \le unc(G)$, where $c\_\epsilon\ge
2.82$ is a constant depending on $\epsilon$.
We improve the lower-bound to state that
$\lceil\frac{|E(G)|}{3|V(G)|-6-\sqrt{2|E(G)|}+\sqrt{6(|V(G)|-2)}}\rceil \le
unc(G)$. Translated to dense graphs regime, the bound yields a multiplicative
constant $c'\_\epsilon=3-\sqrt{(2-\epsilon)}$ in the expression
$\lceil\frac{|E(G)|}{c'\_\epsilon|V(G)|+o(|V(G)|)}\rceil \le unc(G)$. Hence, it
is tight (up to low-order terms) for $\epsilon \approx \frac{1}{2}$ as
warranted by complete graphs.
In fact, we formulate our result in the language of the maximum uncrossed
subgraph number, that is, the maximum number of edges of $G$ that are not
crossed in a drawing of $G$ in the plane. In that case, we also provide a
construction certifying that our bound is asymptotically tight (up to low-order
terms) on dense graphs for all $\epsilon>0$.

[Read original post](http://arxiv.org/abs/2507.20937v1)
