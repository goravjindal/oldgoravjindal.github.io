---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Beer Path Problems in Temporal Graphs"
date: 2025-07-14T00:00:00
---

**Authors:** [Andrea D'Ascenzo](https://dblp.uni-trier.de/search?q=Andrea+D%27Ascenzo), [Giuseppe F. Italiano](https://dblp.uni-trier.de/search?q=Giuseppe+F.+Italiano), [Sotiris Kanellopoulos](https://dblp.uni-trier.de/search?q=Sotiris+Kanellopoulos), [Anna Mpanti](https://dblp.uni-trier.de/search?q=Anna+Mpanti), [Aris Pagourtzis](https://dblp.uni-trier.de/search?q=Aris+Pagourtzis), [Christos Pergaminelis](https://dblp.uni-trier.de/search?q=Christos+Pergaminelis)

Computing paths in graph structures is a fundamental operation in a wide
range of applications, from transportation networks to data analysis. The beer
path problem, which captures the option of visiting points of interest, such as
gas stations or convenience stops, prior to reaching the final destination, has
been recently introduced and extensively studied in static graphs. However,
existing approaches do not account for temporal information, which is often
crucial in real-world scenarios. For instance, transit services may follow
fixed schedules, and shops may only be accessible during certain hours.
In this work, we introduce the notion of beer paths in temporal graphs, where
edges are time-dependent and certain vertices (beer vertices) are active only
at specific time instances. We formally define the problems of computing
earliest-arrival, latest-departure, fastest, and shortest temporal beer paths
and propose efficient algorithms for these problems under both edge stream and
adjacency list representations. The time complexity of each of our algorithms
is aligned with that of corresponding temporal pathfinding algorithms, thus
preserving efficiency.
Additionally, we present preprocessing techniques that enable efficient query
answering under dynamic conditions, for example new openings or closings of
shops. We achieve this through appropriate precomputation of selected paths or
by transforming a temporal graph into an equivalent static graph.

[Read original post](http://arxiv.org/abs/2507.08685v1)
