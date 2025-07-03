---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Faster Algorithm for Second (s,t)-mincut and Breaking Quadratic barrier
  for Dual Edge Sensitivity for (s,t)-mincut"
date: 2025-07-03T00:00:00
---

**Authors:** [Surender Baswana](https://dblp.uni-trier.de/search?q=Surender+Baswana), [Koustav Bhanja](https://dblp.uni-trier.de/search?q=Koustav+Bhanja), [Anupam Roy](https://dblp.uni-trier.de/search?q=Anupam+Roy)

We study (s,t)-cuts of second minimum capacity and present the following
algorithmic and graph-theoretic results.
1. Vazirani and Yannakakis [ICALP 1992] designed the first algorithm for
computing an (s,t)-cut of second minimum capacity using $O(n^2)$ maximum
(s,t)-flow computations. For directed integer-weighted graphs, we significantly
improve this bound by designing an algorithm that computes an $(s,t)$-cut of
second minimum capacity using $O(\sqrt{n})$ maximum (s,t)-flow computations
w.h.p. To achieve this result, a close relationship of independent interest is
established between $(s,t)$-cuts of second minimum capacity and global mincuts
in directed weighted graphs.
2. Minimum+1 (s,t)-cuts have been studied quite well recently [Baswana,
Bhanja, and Pandey, ICALP 2022], which is a special case of second
(s,t)-mincut.
(a) For directed multi-graphs, we design an algorithm that, given any maximum
(s,t)-flow, computes a minimum+1 (s,t)-cut, if it exists, in $O(m)$ time.
(b) The existing structures for storing and characterizing all minimum+1
(s,t)-cuts occupy $O(mn)$ space. For undirected multi-graphs, we design a DAG
occupying only $O(m)$ space that stores and characterizes all minimum+1
(s,t)-cuts.
3. The study of minimum+1 (s,t)-cuts often turns out to be useful in
designing dual edge sensitivity oracles -- a compact data structure for
efficiently reporting an (s,t)-mincut after insertion/failure of any given pair
of query edges. It has been shown recently [Bhanja, ICALP 2025] that any dual
edge sensitivity oracle for (s,t)-mincut in undirected multi-graphs must occupy
${\Omega}(n^2)$ space in the worst-case, irrespective of the query time. For
simple graphs, we break this quadratic barrier while achieving a non-trivial
query time.