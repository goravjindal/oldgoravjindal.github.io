---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Triadic First-Order Logic Queries in Temporal Networks"
date: 2025-07-24T00:00:00
---

**Authors:** [Omkar Bhalerao](https://dblp.uni-trier.de/search?q=Omkar+Bhalerao), [Yunjie Pan](https://dblp.uni-trier.de/search?q=Yunjie+Pan), [C. Seshadhri](https://dblp.uni-trier.de/search?q=C.+Seshadhri), [Nishil Talati](https://dblp.uni-trier.de/search?q=Nishil+Talati)

Motif counting is a fundamental problem in network analysis, and there is a
rich literature of theoretical and applied algorithms for this problem. Given a
large input network $G$, a motif $H$ is a small "pattern" graph indicative of
special local structure. Motif/pattern mining involves finding all matches of
this pattern in the input $G$. The simplest, yet challenging, case of motif
counting is when $H$ has three vertices, often called a "triadic" query. Recent
work has focused on "temporal graph mining", where the network $G$ has edges
with timestamps (and directions) and $H$ has time constraints.
Inspired by concepts in logic and database theory, we introduce the study of
"thresholded First Order Logic (FOL) Motif Analysis" for massive temporal
networks. A typical triadic motif query asks for the existence of three
vertices that form a desired temporal pattern. An "FOL" motif query is obtained
by having both existential and thresholded universal quantifiers. This allows
for query semantics that can mine richer information from networks. A typical
triadic query would be "find all triples of vertices $u,v,w$ such that they
form a triangle within one hour". A thresholded FOL query can express "find all
pairs $u,v$ such that for half of $w$ where $(u,w)$ formed an edge, $(v,w)$
also formed an edge within an hour".
We design the first algorithm, FOLTY, for mining thresholded FOL triadic
queries. The theoretical running time of FOLTY matches the best known running
time for temporal triangle counting in sparse graphs. We give an efficient
implementation of FOLTY using specialized temporal data structures. FOLTY has
excellent empirical behavior, and can answer triadic FOL queries on graphs with
nearly 70M edges is less than hour on commodity hardware. Our work has the
potential to start a new research direction in the classic well-studied problem
of motif analysis.

[Read original post](http://arxiv.org/abs/2507.17215v1)
