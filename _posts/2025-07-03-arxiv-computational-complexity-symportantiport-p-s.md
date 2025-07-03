---
layout: post
title: "arXiv: Computational Complexity: Symport/Antiport P Systems with Membrane Separation Characterize P^(#P)"
date: 2025-07-03 13:21:53 
categories: [rss]
external_link: http://arxiv.org/abs/2507.01657v1
---

**Authors:** [Vivien Ducros](https://dblp.uni-trier.de/search?q=Vivien+Ducros), [Claudio Zandron](https://dblp.uni-trier.de/search?q=Claudio+Zandron)

Membrane systems represent a computational model that operates in a
distributed and parallel manner, inspired by the behavior of biological cells.
These systems feature objects that transform within a nested membrane
structure. This research concentrates on a specific type of these systems,
based on cellular symport/antiport communication of chemicals.
Results in the literature show that systems of this type that also allow cell
division can solve PSPACE problems. In our study, we investigate systems that
use membrane separation instead of cell division, for which only limited
results are available. Notably, it has been shown that any problem solvable by
such systems in polynomial time falls within the complexity class P^(#P).
By implementing a system solving MIDSAT, a P^(#P)-complete problem, we
demonstrate that the reverse inclusion is true as well, thus providing an exact
characterization of the problem class solvable by P systems with
symport/antiport and membrane separation.
Moreover, our implementation uses rules of length at most three. With this
limit, systems were known to be able to solve NP-complete problems, whereas
limiting the rules by length two, they characterize P.
