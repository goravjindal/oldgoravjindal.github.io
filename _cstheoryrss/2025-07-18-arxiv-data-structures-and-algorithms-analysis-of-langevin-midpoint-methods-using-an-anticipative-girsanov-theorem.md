---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Analysis of Langevin midpoint methods using an anticipative Girsanov
  theorem"
date: 2025-07-18T00:00:00
---

**Authors:** [Matthew S. Zhang](https://dblp.uni-trier.de/search?q=Matthew+S.+Zhang)

We introduce a new method for analyzing midpoint discretizations of
stochastic differential equations (SDEs), which are frequently used in Markov
chain Monte Carlo (MCMC) methods for sampling from a target measure $\pi
\propto \exp(-V)$. Borrowing techniques from Malliavin calculus, we compute
estimates for the Radon-Nikodym derivative for processes on $L^2([0, T);
\mathbb{R}^d)$ which may anticipate the Brownian motion, in the sense that they
may not be adapted to the filtration at the same time. Applying these to
various popular midpoint discretizations, we are able to improve the regularity
and cross-regularity results in the literature on sampling methods. We also
obtain a query complexity bound of $\widetilde{O}(\frac{\kappa^{5/4}
d^{1/4}}{\varepsilon^{1/2}})$ for obtaining a $\varepsilon^2$-accurate sample
in $\mathsf{KL}$ divergence, under log-concavity and strong smoothness
assumptions for $\nabla^2 V$.

[Read original post](http://arxiv.org/abs/2507.12791v1)
