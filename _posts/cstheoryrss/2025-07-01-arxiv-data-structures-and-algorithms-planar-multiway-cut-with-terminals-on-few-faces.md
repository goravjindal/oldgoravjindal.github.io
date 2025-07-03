---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Planar Multiway Cut with Terminals on Few Faces"
date: 2025-07-01T00:00:00
---

**Authors:** [Sukanya Pandey](https://dblp.uni-trier.de/search?q=Sukanya+Pandey), [Erik Jan van Leeuwen](https://dblp.uni-trier.de/search?q=Erik+Jan+van+Leeuwen)

We consider the \textsc{Edge Multiway Cut} problem on planar graphs. It is
known that this can be solved in $n^{O(\sqrt{t})}$ time [Klein, Marx, ICALP
2012] and not in $n^{o(\sqrt{t})}$ time under the Exponential Time Hypothesis
[Marx, ICALP 2012], where $t$ is the number of terminals. A stronger parameter
is the number $k$ of faces of the planar graph that jointly cover all
terminals. For the related {\sc Steiner Tree} problem, an $n^{O(\sqrt{k})}$
time algorithm was recently shown [Kisfaludi-Bak et al., SODA 2019]. By a
completely different approach, we prove in this paper that \textsc{Edge
Multiway Cut} can be solved in $n^{O(\sqrt{k})}$ time as well.
Our approach employs several major concepts on planar graphs, including
homotopy and sphere-cut decomposition. We also mix a global treewidth dynamic
program with a Dreyfus-Wagner style dynamic program to locally deal with large
numbers of terminals.