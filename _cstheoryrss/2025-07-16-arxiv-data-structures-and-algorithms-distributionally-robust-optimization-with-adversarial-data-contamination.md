---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Distributionally Robust Optimization with Adversarial Data Contamination"
date: 2025-07-16T00:00:00
---

**Authors:** [Shuyao Li](https://dblp.uni-trier.de/search?q=Shuyao+Li), [Ilias Diakonikolas](https://dblp.uni-trier.de/search?q=Ilias+Diakonikolas), [Jelena Diakonikolas](https://dblp.uni-trier.de/search?q=Jelena+Diakonikolas)

Distributionally Robust Optimization (DRO) provides a framework for
decision-making under distributional uncertainty, yet its effectiveness can be
compromised by outliers in the training data. This paper introduces a
principled approach to simultaneously address both challenges. We focus on
optimizing Wasserstein-1 DRO objectives for generalized linear models with
convex Lipschitz loss functions, where an $\epsilon$-fraction of the training
data is adversarially corrupted. Our primary contribution lies in a novel
modeling framework that integrates robustness against training data
contamination with robustness against distributional shifts, alongside an
efficient algorithm inspired by robust statistics to solve the resulting
optimization problem. We prove that our method achieves an estimation error of
$O(\sqrt{\epsilon})$ for the true DRO objective value using only the
contaminated data under the bounded covariance assumption. This work
establishes the first rigorous guarantees, supported by efficient computation,
for learning under the dual challenges of data contamination and distributional
shifts.

[Read original post](http://arxiv.org/abs/2507.10718v1)
