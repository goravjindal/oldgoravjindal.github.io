---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: NP-Hardness and ETH-Based Inapproximability of Communication Complexity"
date: 2025-08-08T00:00:00
---

**Authors:** [Serge Gaspers](https://dblp.uni-trier.de/search?q=Serge+Gaspers), [Zixu He](https://dblp.uni-trier.de/search?q=Zixu+He), [Simon Mackenzie](https://dblp.uni-trier.de/search?q=Simon+Mackenzie)

We prove that computing the deterministic communication complexity D(f) of a
Boolean function is NP-hard, even when protocols are limited to a constant
number of alternations, resolving a question first posed by Yao (1979). Our
reduction builds and expands on a suite of structural "interlacing" lemmas
introduced by Mackenzie and Saffidine (arXiv:2505.12345); these lemmas can be
reused as black boxes in future lower-bound constructions.
The instances produced by our reduction admit optimal protocols that use only
constant alternations, so NP-hardness holds under stronger restrictions than
those considered in concurrent and independent work by Hirahara, Ilango, and
Loff (arXiv:2507.06789), whose proof requires unbounded alternations.
Because the gadgets in our construction are self-similar, they can be
recursively embedded. We sketch how this yields, under the Exponential-Time
Hypothesis, an additive inapproximability gap that grows without bound, and we
outline a route toward NP-hardness of approximating D(f) within a fixed
constant additive error. Full details of the ETH-based inapproximability
results will appear in a future version.
Beyond settling the complexity of deterministic communication complexity
itself, the modular framework we develop opens the door to a wider class of
reductions and, we believe, will prove useful in tackling other long-standing
questions in communication complexity.

[Read original post](http://arxiv.org/abs/2508.05597v1)
