---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Faster Distributed -Coloring via a Reduction to MIS"
date: 2025-08-05T00:00:00
---

**Authors:** [Yann Bourreau](https://dblp.uni-trier.de/search?q=Yann+Bourreau), [Sebastian Brandt](https://dblp.uni-trier.de/search?q=Sebastian+Brandt), [Alexandre Nolin](https://dblp.uni-trier.de/search?q=Alexandre+Nolin)

Recent improvements on the deterministic complexities of fundamental graph
problems in the LOCAL model of distributed computing have yielded
state-of-the-art upper bounds of $\tilde{O}(\log^{5/3} n)$ rounds for maximal
independent set (MIS) and $(\Delta + 1)$-coloring [Ghaffari, Grunau, FOCS'24]
and $\tilde{O}(\log^{19/9} n)$ rounds for the more restrictive
$\Delta$-coloring problem [Ghaffari, Kuhn, FOCS'21; Ghaffari, Grunau, FOCS'24;
Bourreau, Brandt, Nolin, STOC'25]. In our work, we show that $\Delta$-coloring
can be solved deterministically in $\tilde{O}(\log^{5/3} n)$ rounds as well,
matching the currently best bound for $(\Delta + 1)$-coloring.
We achieve our result by developing a reduction from $\Delta$-coloring to MIS
that guarantees that the (asymptotic) complexity of $\Delta$-coloring is at
most the complexity of MIS, unless MIS can be solved in sublogarithmic time, in
which case, due to the $\Omega(\log n)$-round $\Delta$-coloring lower bound
from [BFHKLRSU, STOC'16], our reduction implies a tight complexity of
$\Theta(\log n)$ for $\Delta$-coloring. In particular, any improvement on the
complexity of the MIS problem will yield the same improvement for the
complexity of $\Delta$-coloring (up to the true complexity of
$\Delta$-coloring).
Our reduction yields improvements for $\Delta$-coloring in the randomized
LOCAL model and when complexities are parameterized by both $n$ and $\Delta$.
We obtain a randomized complexity bound of $\tilde{O}(\log^{5/3} \log n)$
rounds (improving over the state of the art of $\tilde{O}(\log^{8/3} \log n)$
rounds) on general graphs and tight complexities of $\Theta(\log n)$ and
$\Theta(\log \log n)$ for the deterministic, resp.\ randomized, complexity on
bounded-degree graphs. In the special case of graphs of constant clique number
(which for instance include bipartite graphs), we also give a reduction to the
$(\Delta+1)$-coloring problem.

[Read original post](http://arxiv.org/abs/2508.01762v1)
