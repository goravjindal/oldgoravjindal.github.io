---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Instance-Optimal Uniformity Testing and Tracking"
date: 2025-08-05T00:00:00
---

**Authors:** [Guy Blanc](https://dblp.uni-trier.de/search?q=Guy+Blanc), [Clément L. Canonne](https://dblp.uni-trier.de/search?q=Cl%C3%A9ment+L.+Canonne), [Erik Waingarten](https://dblp.uni-trier.de/search?q=Erik+Waingarten)

In the uniformity testing task, an algorithm is provided with samples from an
unknown probability distribution over a (known) finite domain, and must decide
whether it is the uniform distribution, or, alternatively, if its total
variation distance from uniform exceeds some input distance parameter. This
question has received a significant amount of interest and its complexity is,
by now, fully settled. Yet, we argue that it fails to capture many scenarios of
interest, and that its very definition as a gap problem in terms of a
prespecified distance may lead to suboptimal performance.
To address these shortcomings, we introduce the problem of uniformity
tracking, whereby an algorithm is required to detect deviations from uniformity
(however they may manifest themselves) using as few samples as possible, and be
competitive against an optimal algorithm knowing the distribution profile in
hindsight. Our main contribution is a
$\operatorname{polylog}(\operatorname{opt})$-competitive uniformity tracking
algorithm. We obtain this result by leveraging new structural results on
Poisson mixtures, which we believe to be of independent interest.

[Read original post](http://arxiv.org/abs/2508.02637v1)
