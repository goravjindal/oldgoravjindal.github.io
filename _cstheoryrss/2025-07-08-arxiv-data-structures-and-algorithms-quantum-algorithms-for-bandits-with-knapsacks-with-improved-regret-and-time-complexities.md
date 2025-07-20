---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Quantum Algorithms for Bandits with Knapsacks with Improved Regret and"
date: 2025-07-08T00:00:00
---

**Authors:** [Yuexin Su](https://dblp.uni-trier.de/search?q=Yuexin+Su), [Ziyi Yang](https://dblp.uni-trier.de/search?q=Ziyi+Yang), [Peiyuan Huang](https://dblp.uni-trier.de/search?q=Peiyuan+Huang), [Tongyang Li](https://dblp.uni-trier.de/search?q=Tongyang+Li), [Yinyu Ye](https://dblp.uni-trier.de/search?q=Yinyu+Ye)

Bandits with knapsacks (BwK) constitute a fundamental model that combines
aspects of stochastic integer programming with online learning. Classical
algorithms for BwK with a time horizon $T$ achieve a problem-independent regret
bound of ${O}(\sqrt{T})$ and a problem-dependent bound of ${O}(\log T)$. In
this paper, we initiate the study of the BwK model in the setting of quantum
computing, where both reward and resource consumption can be accessed via
quantum oracles. We establish both problem-independent and problem-dependent
regret bounds for quantum BwK algorithms. For the problem-independent case, we
demonstrate that a quantum approach can improve the classical regret bound by a
factor of $(1+\sqrt{B/\mathrm{OPT}\_\mathrm{LP}})$, where $B$ is budget
constraint in BwK and $\mathrm{OPT}\_{\mathrm{LP}}$ denotes the optimal value of
a linear programming relaxation of the BwK problem. For the problem-dependent
setting, we develop a quantum algorithm using an inexact quantum linear
programming solver. This algorithm achieves a quadratic improvement in terms of
the problem-dependent parameters, as well as a polynomial speedup of time
complexity on problem's dimensions compared to classical counterparts. Compared
to previous works on quantum algorithms for multi-armed bandits, our study is
the first to consider bandit models with resource constraints and hence shed
light on operations research.

[Read original post](http://arxiv.org/abs/2507.04438v1)
