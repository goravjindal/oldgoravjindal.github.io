---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Improved Directed Expander Decompositions"
date: 2025-07-15T00:00:00
---

**Authors:** [Henry Fleischmann](https://dblp.uni-trier.de/search?q=Henry+Fleischmann), [George Z. Li](https://dblp.uni-trier.de/search?q=George+Z.+Li), [Jason Li](https://dblp.uni-trier.de/search?q=Jason+Li)

We obtain faster expander decomposition algorithms for directed graphs,
matching the guarantees of Saranurak and Wang (SODA 2019) for expander
decomposition on undirected graphs. Our algorithms are faster than prior work
and also generalize almost losslessly to capacitated graphs. In particular, we
obtain the first directed expander decomposition algorithm for capacitated
graphs in near-linear time with optimal dependence on $\phi$.
To obtain our result, we provide the first implementation and analysis of the
non-stop cut-matching game for directed, capacitated graphs. All existing
directed expander decomposition algorithms instead temporarily add ''fake
edges'' before pruning them away in a final cleanup step. Our result shows that
the natural undirected approach applies even to directed graphs. The difficulty
is in its analysis, which is technical and requires significant modifications
from the original setting of undirected graphs.

[Read original post](http://arxiv.org/abs/2507.09729v1)
