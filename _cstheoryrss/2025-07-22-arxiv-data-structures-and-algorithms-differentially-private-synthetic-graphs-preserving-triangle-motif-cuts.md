---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Differentially Private Synthetic Graphs Preserving Triangle-Motif Cuts"
date: 2025-07-22T00:00:00
---

**Authors:** [Pan Peng](https://dblp.uni-trier.de/search?q=Pan+Peng), [Hangyu Xu](https://dblp.uni-trier.de/search?q=Hangyu+Xu)

We study the problem of releasing a differentially private (DP) synthetic
graph $G'$ that well approximates the triangle-motif sizes of all cuts of any
given graph $G$, where a motif in general refers to a frequently occurring
subgraph within complex networks. Non-private versions of such graphs have
found applications in diverse fields such as graph clustering, graph
sparsification, and social network analysis. Specifically, we present the first
$(\varepsilon,\delta)$-DP mechanism that, given an input graph $G$ with $n$
vertices, $m$ edges and local sensitivity of triangles $\ell\_{3}(G)$, generates
a synthetic graph $G'$ in polynomial time, approximating the triangle-motif
sizes of all cuts $(S,V\setminus S)$ of the input graph $G$ up to an additive
error of $\tilde{O}(\sqrt{m\ell\_{3}(G)}n/\varepsilon^{3/2})$. Additionally, we
provide a lower bound of $\Omega(\sqrt{mn}\ell\_{3}(G)/\varepsilon)$ on the
additive error for any DP algorithm that answers the triangle-motif size
queries of all $(S,T)$-cut of $G$. Finally, our algorithm generalizes to
weighted graphs, and our lower bound extends to any $K\_h$-motif cut for any
constant $h\geq 2$.

[Read original post](http://arxiv.org/abs/2507.14835v1)
