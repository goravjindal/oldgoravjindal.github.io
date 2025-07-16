---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Improved sampling algorithms and Poincaré inequalities for
  non-log-concave distributions"
date: 2025-07-16T00:00:00
---

**Authors:** [Yuchen He](https://dblp.uni-trier.de/search?q=Yuchen+He), [Zhehan Lei](https://dblp.uni-trier.de/search?q=Zhehan+Lei), [Jianan Shao](https://dblp.uni-trier.de/search?q=Jianan+Shao), [Chihao Zhang](https://dblp.uni-trier.de/search?q=Chihao+Zhang)

We study the problem of sampling from a distribution $\mu$ with density
$\propto e^{-V}$ for some potential function $V:\mathbb R^d\to \mathbb R$ with
query access to $V$ and $\nabla V$. We start with the following standard
assumptions:
(1) The potential function $V$ is $L$-smooth.
(2) The second moment $\mathbf{E}\_{X\sim \mu}[\|X\|^2]\leq M$.
Recently, He and Zhang (COLT'25) showed that the query complexity of sampling
from such distributions is at least
$\left(\frac{LM}{d\epsilon}\right)^{\Omega(d)}$ where $\epsilon$ is the desired
accuracy in total variation distance, and the Poincar\'e constant can be
arbitrarily large.
Meanwhile, another common assumption in the study of diffusion based samplers
(see e.g., the work of Chen, Chewi, Li, Li, Salim and Zhang (ICLR'23))
strengthens the smoothness condition (1) to the following:
(1\*) The potential function of \*every\* distribution along the
Ornstein-Uhlenbeck process starting from $\mu$ is $L$-smooth.
We show that under the assumptions (1\*) and (2), the query complexity of
sampling from $\mu$ can be $\mathrm{poly}(L,d)\cdot
\left(\frac{Ld+M}{\epsilon^2}\right)^{\mathcal{O}(L+1)}$, which is polynomial
in $d$ and $\frac{1}{\epsilon}$ when $L=\mathcal{O}(1)$ and
$M=\mathrm{poly}(d)$. This improves the algorithm with quasi-polynomial query
complexity developed by Huang et al. (COLT'24). Our results imply that the
seemly moderate strengthening of the smoothness condition (1) to (1\*) can lead
to an exponential gap in the query complexity of sampling algorithms.
Moreover, we show that together with the assumption (1\*) and the stronger
moment assumption that $\|X\|$ is $\lambda$-sub-Gaussian for $X\sim\mu$, the
Poincar\'e constant of $\mu$ is at most $\mathcal{O}(\lambda)^{2(L+1)}$. As an
application of our technique, we obtain improved estimate of the Poincar\'e
constant for mixture of Gaussians with the same covariance.

[Read original post](http://arxiv.org/abs/2507.11236v1)
