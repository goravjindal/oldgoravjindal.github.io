---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Space-Efficient Hierholzer: Eulerian Cycles in O(m) Time and O(n) Space"
date: 2025-08-08T00:00:00
---

**Authors:** [Ziad Ismaili Alaoui](https://dblp.uni-trier.de/search?q=Ziad+Ismaili+Alaoui), [Detlef Plump](https://dblp.uni-trier.de/search?q=Detlef+Plump), [Sebastian Wild](https://dblp.uni-trier.de/search?q=Sebastian+Wild)

We describe a simple variant of Hierholzer's algorithm that finds an Eulerian
cycle in a (multi)graph with $n$ vertices and $m$ edges using $\mathrm{O}(n \lg
m)$ bits of working memory. This substantially improves the working space
compared to standard implementations of Hierholzer's algorithm, which use
$\mathrm{O}(m \lg n)$ bits of space. Our algorithm runs in linear time, like
the classical versions, but avoids an $\mathrm{O}(m)$-size stack of vertices or
storing information for each edge. To our knowledge, this is the first
linear-time algorithm to achieve this space bound, and the method is very easy
to implement. The correctness argument, by contrast, is surprisingly subtle; we
give a detailed formal proof. The space savings are particularly relevant for
dense graphs or multigraphs with large edge multiplicities.

[Read original post](http://arxiv.org/abs/2508.05251v1)
