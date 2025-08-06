---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: When is String Reconstruction using de Bruijn Graphs Hard?"
date: 2025-08-06T00:00:00
---

**Authors:** [Ben Bals](https://dblp.uni-trier.de/search?q=Ben+Bals), [Sebastiaan van Krieken](https://dblp.uni-trier.de/search?q=Sebastiaan+van+Krieken), [Solon P. Pissis](https://dblp.uni-trier.de/search?q=Solon+P.+Pissis), [Leen Stougie](https://dblp.uni-trier.de/search?q=Leen+Stougie), [Hilde Verbeek](https://dblp.uni-trier.de/search?q=Hilde+Verbeek)

The reduction of the fragment assembly problem to (variations of) the
classical Eulerian trail problem [Pevzner et al., PNAS 2001] has led to
remarkable progress in genome assembly. This reduction employs the notion of de
Bruijn graph $G=(V,E)$ of order $k$ over an alphabet $\Sigma$. A single
Eulerian trail in $G$ represents a candidate genome reconstruction. Bernardini
et al. have also introduced the complementary idea in data privacy [ALENEX
2020] based on $z$-anonymity.
The pressing question is: How hard is it to reconstruct a best string from a
de Bruijn graph given a function that models domain knowledge? Such a function
maps every length-$k$ string to an interval of positions where it may occur in
the reconstructed string. By the above reduction to de Bruijn graphs, the
latter function translates into a function $c$ mapping every edge to an
interval where it may occur in an Eulerian trail. This gives rise to the
following basic problem on graphs: Given an instance $(G,c)$, can we
efficiently compute an Eulerian trail respecting $c$? Hannenhalli et
al.~[CABIOS 1996] formalized this problem and showed that it is NP-complete.
We focus on parametrization aiming to capture the quality of our domain
knowledge in the complexity. Ben-Dor et al. developed an algorithm to solve the
problem on de Bruijn graphs in $O(m \cdot w^{1.5} 4^{w})$ time, where $m=|E|$
and $w$ is the maximum interval length over all edges. Bumpus and Meeks
[Algorithmica 2023] rediscovered the same algorithm on temporal graphs,
highlighting the relevance of this problem in other contexts. We give
combinatorial insights that lead to exponential-time improvements over the
state-of-the-art. For the important class of de Bruijn graphs, we develop an
algorithm parametrized by $w (\log w+1) /(k-1)$. Our improved algorithm shows
that it is enough when the range of positions is small relative to $k$.

[Read original post](http://arxiv.org/abs/2508.03433v1)
