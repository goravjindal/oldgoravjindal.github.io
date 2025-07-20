---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Mallows Model with Learned Distance Metrics: Sampling and Maximum"
date: 2025-07-14T00:00:00
---

**Authors:** [Yeganeh Alimohammadi](https://dblp.uni-trier.de/search?q=Yeganeh+Alimohammadi), [Kiana Asgari](https://dblp.uni-trier.de/search?q=Kiana+Asgari)

\textit{Mallows model} is a widely-used probabilistic framework for learning
from ranking data, with applications ranging from recommendation systems and
voting to aligning language models with human
preferences~\cite{chen2024mallows, kleinberg2021algorithmic,
rafailov2024direct}. Under this model, observed rankings are noisy
perturbations of a central ranking $\sigma$, with likelihood decaying
exponentially in distance from $\sigma$, i.e, $P (\pi) \propto \exp\big(-\beta
\cdot d(\pi, \sigma)\big),$ where $\beta > 0$ controls dispersion and $d$ is a
distance function.
Existing methods mainly focus on fixed distances (such as Kendall's $\tau$
distance), with no principled approach to learning the distance metric directly
from data. In practice, however, rankings naturally vary by context; for
instance, in some sports we regularly see long-range swaps (a low-rank team
beating a high-rank one), while in others such events are rare. Motivated by
this, we propose a generalization of Mallows model that learns the distance
metric directly from data. Specifically, we focus on $L\_\alpha$ distances:
$d\_\alpha(\pi,\sigma):=\sum\_{i=1} |\pi(i)-\sigma(i)|^\alpha$.
For any $\alpha\geq 1$ and $\beta>0$, we develop a Fully Polynomial-Time
Approximation Scheme (FPTAS) to efficiently generate samples that are
$\epsilon$- close (in total variation distance) to the true distribution. Even
in the special cases of $L\_1$ and $L\_2$, this generalizes prior results that
required vanishing dispersion ($\beta\to0$). Using this sampling algorithm, we
propose an efficient Maximum Likelihood Estimation (MLE) algorithm that jointly
estimates the central ranking, the dispersion parameter, and the optimal
distance metric. We prove strong consistency results for our estimators (for
any values of $\alpha$ and $\beta$), and we validate our approach empirically
using datasets from sports rankings.

[Read original post](http://arxiv.org/abs/2507.08108v1)
