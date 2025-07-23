---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Online Combinatorial Optimization with Graphical Dependencies"
date: 2025-07-23T00:00:00
---

**Authors:** [Zhimeng Gao](https://dblp.uni-trier.de/search?q=Zhimeng+Gao), [Evangelia Gergatsouli](https://dblp.uni-trier.de/search?q=Evangelia+Gergatsouli), [Kalen Patton](https://dblp.uni-trier.de/search?q=Kalen+Patton), [Sahil Singla](https://dblp.uni-trier.de/search?q=Sahil+Singla)

Most existing work in online stochastic combinatorial optimization assumes
that inputs are drawn from independent distributions -- a strong assumption
that often fails in practice. At the other extreme, arbitrary correlations are
equivalent to worst-case inputs via Yao's minimax principle, making good
algorithms often impossible. This motivates the study of intermediate models
that capture mild correlations while still permitting non-trivial algorithms.
In this paper, we study online combinatorial optimization under Markov Random
Fields (MRFs), a well-established graphical model for structured dependencies.
MRFs parameterize correlation strength via the maximum weighted degree
$\Delta$, smoothly interpolating between independence ($\Delta = 0$) and full
correlation ($\Delta \to \infty$). While na\"ively this yields
$e^{O(\Delta)}$-competitive algorithms and $\Omega(\Delta)$ hardness, we ask:
when can we design tight $\Theta(\Delta)$-competitive algorithms?
We present general techniques achieving $O(\Delta)$-competitive algorithms
for both minimization and maximization problems under MRF-distributed inputs.
For minimization problems with coverage constraints (e.g., Facility Location
and Steiner Tree), we reduce to the well-studied $p$-sample model. For
maximization problems (e.g., matchings and combinatorial auctions with XOS
buyers), we extend the "balanced prices" framework for online allocation
problems to MRFs.

[Read original post](http://arxiv.org/abs/2507.16031v1)
