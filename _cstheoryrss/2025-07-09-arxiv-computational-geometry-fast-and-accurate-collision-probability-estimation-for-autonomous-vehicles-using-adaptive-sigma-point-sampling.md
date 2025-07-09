---
layout: post
category: cstheoryrss
title: "arXiv: Computational Geometry: Fast and Accurate Collision Probability Estimation for Autonomous
  Vehicles using Adaptive Sigma-Point Sampling"
date: 2025-07-09T00:00:00
---

**Authors:** [Charles Champagne Cossette](https://dblp.uni-trier.de/search?q=Charles+Champagne+Cossette), [Taylor Scott Clawson](https://dblp.uni-trier.de/search?q=Taylor+Scott+Clawson), [Andrew Feit](https://dblp.uni-trier.de/search?q=Andrew+Feit)

A novel algorithm is presented for the estimation of collision probabilities
between dynamic objects with uncertain trajectories, where the trajectories are
given as a sequence of poses with Gaussian distributions. We propose an
adaptive sigma-point sampling scheme, which ultimately produces a fast, simple
algorithm capable of estimating the collision probability with a median error
of 3.5%, and a median runtime of 0.21ms, when measured on an Intel Xeon Gold
6226R Processor. Importantly, the algorithm explicitly accounts for the
collision probability's temporal dependence, which is often neglected in prior
work and otherwise leads to an overestimation of the collision probability.
Finally, the method is tested on a diverse set of relevant real-world
scenarios, consisting of 400 6-second snippets of autonomous vehicle logs,
where the accuracy and latency is rigorously evaluated.

[Read original post](http://arxiv.org/abs/2507.06149v1)
