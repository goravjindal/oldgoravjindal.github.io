---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Parameterized complexity of isometric path partition: treewidth and"
date: 2025-08-08T00:00:00
---

**Authors:** [Dibyayan Chakraborty](https://dblp.uni-trier.de/search?q=Dibyayan+Chakraborty), [Oscar Defrain](https://dblp.uni-trier.de/search?q=Oscar+Defrain), [Florent Foucaud](https://dblp.uni-trier.de/search?q=Florent+Foucaud), [Mathieu Mari](https://dblp.uni-trier.de/search?q=Mathieu+Mari), [Prafullkumar Tale](https://dblp.uni-trier.de/search?q=Prafullkumar+Tale)

We investigate the parameterized complexity of the Isometric Path Partition
problem when parameterized by the treewidth ($\mathrm{tw}$) of the input graph,
arguably one of the most widely studied parameters. Courcelle's theorem shows
that graph problems that are expressible as MSO formulas of constant size admit
FPT algorithms parameterized by the treewidth of the input graph. This
encompasses many natural graph problems. However, many metric-based graph
problems, where the solution is defined using some metric-based property of the
graph (often the distance) are not expressible as MSO formulas of constant
size. These types of problems, Isometric Path Partition being one of them,
require individual attention and often draw the boundary for the success story
of parameterization by treewidth.
In this paper, we prove that Isometric Path Partition is $W[1]$-hard when
parameterized by treewidth (in fact, even pathwidth), answering the question by
Dumas et al. [SIDMA, 2024], Fernau et al. [CIAC, 2023], and confirming the
aforementioned tendency. We complement this hardness result by designing a
tailored dynamic programming algorithm running in $n^{O(\mathrm{tw})}$ time.
This dynamic programming approach also results in an algorithm running in time
$\textrm{diam}^{O(\mathrm{tw}^2)} \cdot n^{O(1)}$, where $\textrm{diam}$ is the
diameter of the graph. Note that the dependency on treewidth is unusually high,
as most problems admit algorithms running in time $2^{O(\mathrm{tw})}\cdot
n^{O(1)}$ or $2^{O(\mathrm{tw} \log (\mathrm{tw}))}\cdot n^{O(1)}$. However, we
rule out the possibility of a significantly faster algorithm by proving that
Isometric Path Partition does not admit an algorithm running in time
$\textrm{diam}^{o(\mathrm{tw}^2/(\log^3(\mathrm{tw})))} \cdot n^{O(1)}$, unless
the Randomized-ETH fails.

[Read original post](http://arxiv.org/abs/2508.05448v1)
