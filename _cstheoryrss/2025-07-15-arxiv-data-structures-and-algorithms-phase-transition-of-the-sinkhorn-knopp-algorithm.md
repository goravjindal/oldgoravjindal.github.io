---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Phase transition of the Sinkhorn-Knopp algorithm"
date: 2025-07-15T00:00:00
---

**Authors:** [Kun He](https://dblp.uni-trier.de/search?q=Kun+He)

The matrix scaling problem, particularly the Sinkhorn-Knopp algorithm, has
been studied for over 60 years. In practice, the algorithm often yields
high-quality approximations within just a few iterations. Theoretically,
however, the best-known upper bound places it in the class of
pseudopolynomial-time approximation algorithms. Meanwhile, the lower-bound
landscape remains largely unexplored. Two fundamental questions persist: what
accounts for the algorithm's strong empirical performance, and can a tight
bound on its iteration count be established?
For an $n\times n$ matrix, its normalized version is obtained by dividing
each entry by its largest entry. We say that a normalized matrix has a density
$\gamma$ if there exists a constant $\rho > 0$ such that one row or column has
exactly $\lceil \gamma n \rceil$ entries with values at least $\rho$, and every
other row and column has at least $\lceil \gamma n \rceil$ such entries.
For the upper bound, we show that the Sinkhorn-Knopp algorithm produces a
nearly doubly stochastic matrix in $O(\log n - \log \varepsilon)$ iterations
and $\widetilde{O}(n^2)$ time for all nonnegative square matrices whose
normalized version has a density $\gamma > 1/2$. Such matrices cover both the
algorithm's principal practical inputs and its typical theoretical regime, and
the $\widetilde{O}(n^2)$ runtime is optimal.
For the lower bound, we establish a tight bound of
$\widetilde{\Omega}\left(n^{1/2}/\varepsilon\right)$ iterations for positive
matrices under the $\ell\_2$-norm error measure. Moreover, for every $\gamma <
1/2$, there exists a matrix with density $\gamma$ for which the algorithm
requires $\Omega\left(n^{1/2}/\varepsilon\right)$ iterations.
In summary, our results reveal a sharp phase transition in the Sinkhorn-Knopp
algorithm at the density threshold $\gamma = 1/2$.

[Read original post](http://arxiv.org/abs/2507.09711v1)
