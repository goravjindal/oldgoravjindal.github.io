---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Parameterized Critical Node Cut Revisited"
date: 2025-07-01T00:00:00
---

**Authors:** [Dušan Knop](https://dblp.uni-trier.de/search?q=Du%C5%A1an+Knop), [Nikolaos Melissinos](https://dblp.uni-trier.de/search?q=Nikolaos+Melissinos), [Manolis Vasilakis](https://dblp.uni-trier.de/search?q=Manolis+Vasilakis)

Given a graph $G$ and integers $k, x \geq 0$, the Critical Node Cut problem
asks whether it is possible to delete at most $k$ vertices from $G$ such that
the number of remaining pairs of connected vertices is at most $x$. This
problem generalizes Vertex Cover (when $x = 0$), and has applications in
network design, epidemiology, and social network analysis. We investigate the
parameterized complexity of Critical Node Cut under various structural
parameters. We first significantly strengthen existing hardness results by
proving W[1]-hardness even when parameterized by the combined parameter $k +
\mathrm{fes} + \Delta + \mathrm{pw}$, where $\mathrm{fes}$ is the feedback edge
set number, $\Delta$ the maximum degree, and $\mathrm{pw}$ the pathwidth of the
input graph. We then identify three structural parameters--max-leaf number,
vertex integrity, and modular-width--that render the problem fixed-parameter
tractable. Furthermore, leveraging a technique introduced by Lampis [ICALP
'14], we develop an FPT approximation scheme that, for any $\varepsilon > 0$,
computes a $(1+\varepsilon)$-approximate solution in time $(\mathrm{tw} /
\varepsilon)^{\mathcal{O}(\mathrm{tw})} n^{\mathcal{O}(1)}$, where
$\mathrm{tw}$ denotes the treewidth of the input graph. Finally, we show that
Critical Node Cut does not admit a polynomial kernel when parameterized by
vertex cover number, unless standard complexity assumptions fail. Overall, our
results significantly sharpen the known complexity landscape of Critical Node
Cut.