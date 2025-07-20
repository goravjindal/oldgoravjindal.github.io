---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: A Critique of Deng's P=NP"
date: 2025-07-15T00:00:00
---

**Authors:** [Isabel Humphreys](https://dblp.uni-trier.de/search?q=Isabel+Humphreys), [Matthew Iceland](https://dblp.uni-trier.de/search?q=Matthew+Iceland), [Harry Liuson](https://dblp.uni-trier.de/search?q=Harry+Liuson), [Dylan McKellips](https://dblp.uni-trier.de/search?q=Dylan+McKellips), [Leo Sciortino](https://dblp.uni-trier.de/search?q=Leo+Sciortino)

In this paper, we critically examine Deng's "P=NP" [Den24]. The paper claims
that there is a polynomial-time algorithm that decides 3-coloring for graphs
with vertices of degree at most 4, which is known to be an NP-complete problem.
Deng presents a semidefinite program with an objective function that is
unboundedly negative if the graph is not 3-colorable, and a minimum of 0 if the
graph is 3-colorable. Through detailed analysis, we find that Deng conflates
subgraphs with induced subgraphs, leading to a critical error which thereby
invalidates Deng's proof that $\text{P}=\text{NP}$.

[Read original post](http://arxiv.org/abs/2507.09018v1)
