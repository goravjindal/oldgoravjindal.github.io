---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Tight Bounds for Answering Adaptively Chosen Concentrated Queries"
date: 2025-07-21T00:00:00
---

**Authors:** [Emma Rapoport](https://dblp.uni-trier.de/search?q=Emma+Rapoport), [Edith Cohen](https://dblp.uni-trier.de/search?q=Edith+Cohen), [Uri Stemmer](https://dblp.uni-trier.de/search?q=Uri+Stemmer)

Most work on adaptive data analysis assumes that samples in the dataset are
independent. When correlations are allowed, even the non-adaptive setting can
become intractable, unless some structural constraints are imposed. To address
this, Bassily and Freund [2016] introduced the elegant framework of
concentrated queries, which requires the analyst to restrict itself to queries
that are concentrated around their expected value. While this assumption makes
the problem trivial in the non-adaptive setting, in the adaptive setting it
remains quite challenging. In fact, all known algorithms in this framework
support significantly fewer queries than in the independent case: At most
$O(n)$ queries for a sample of size $n$, compared to $O(n^2)$ in the
independent setting.
In this work, we prove that this utility gap is inherent under the current
formulation of the concentrated queries framework, assuming some natural
conditions on the algorithm. Additionally, we present a simplified version of
the best-known algorithms that match our impossibility result.

[Read original post](http://arxiv.org/abs/2507.13700v1)
