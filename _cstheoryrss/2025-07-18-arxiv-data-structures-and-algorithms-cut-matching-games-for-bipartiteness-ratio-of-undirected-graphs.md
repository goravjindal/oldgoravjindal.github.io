---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Cut-Matching Games for Bipartiteness Ratio of Undirected Graphs"
date: 2025-07-18T00:00:00
---

**Authors:** [Tasuku Soma](https://dblp.uni-trier.de/search?q=Tasuku+Soma), [Mingquan Ye](https://dblp.uni-trier.de/search?q=Mingquan+Ye), [Yuichi Yoshida](https://dblp.uni-trier.de/search?q=Yuichi+Yoshida)

We propose an $O(\log n)$-approximation algorithm for the bipartiteness ratio
for undirected graphs introduced by Trevisan (SIAM Journal on Computing, vol.
41, no. 6, 2012), where $n$ is the number of vertices. Our approach extends the
cut-matching game framework for sparsest cut to the bipartiteness ratio. Our
algorithm requires only $\mathrm{poly}\log n$ many single-commodity undirected
maximum flow computations. Therefore, with the current fastest undirected
max-flow algorithms, it runs in nearly linear time. Along the way, we introduce
the concept of well-linkedness for skew-symmetric graphs and prove a novel
characterization of bipartitness ratio in terms of well-linkedness in an
auxiliary skew-symmetric graph, which may be of independent interest.
As an application, we devise an $\tilde{O}(mn)$-time algorithm that given a
graph whose maximum cut deletes a $1-\eta$ fraction of edges, finds a cut that
deletes a $1 - O(\log n \log(1/\eta)) \cdot \eta$ fraction of edges, where $m$
is the number of edges.

[Read original post](http://arxiv.org/abs/2507.12847v1)
