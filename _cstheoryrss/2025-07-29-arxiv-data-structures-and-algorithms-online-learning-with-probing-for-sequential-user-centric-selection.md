---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Online Learning with Probing for Sequential User-Centric Selection"
date: 2025-07-29T00:00:00
---

**Authors:** [Tianyi Xu](https://dblp.uni-trier.de/search?q=Tianyi+Xu), [Yiting Chen](https://dblp.uni-trier.de/search?q=Yiting+Chen), [Henger Li](https://dblp.uni-trier.de/search?q=Henger+Li), [Zheyong Bian](https://dblp.uni-trier.de/search?q=Zheyong+Bian), [Emiliano Dall'Anese](https://dblp.uni-trier.de/search?q=Emiliano+Dall%27Anese), [Zizhan Zheng](https://dblp.uni-trier.de/search?q=Zizhan+Zheng)

We formalize sequential decision-making with information acquisition as the
probing-augmented user-centric selection (PUCS) framework, where a learner
first probes a subset of arms to obtain side information on resources and
rewards, and then assigns $K$ plays to $M$ arms. PUCS covers applications such
as ridesharing, wireless scheduling, and content recommendation, in which both
resources and payoffs are initially unknown and probing is costly. For the
offline setting with known distributions, we present a greedy probing algorithm
with a constant-factor approximation guarantee $\zeta = (e-1)/(2e-1)$. For the
online setting with unknown distributions, we introduce OLPA, a stochastic
combinatorial bandit algorithm that achieves a regret bound
$\mathcal{O}(\sqrt{T} + \ln^{2} T)$. We also prove a lower bound
$\Omega(\sqrt{T})$, showing that the upper bound is tight up to logarithmic
factors. Experiments on real-world data demonstrate the effectiveness of our
solutions.

[Read original post](http://arxiv.org/abs/2507.20112v1)
