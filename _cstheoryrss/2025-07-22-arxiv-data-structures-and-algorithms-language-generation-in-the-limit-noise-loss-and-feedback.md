---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Language Generation in the Limit: Noise, Loss, and Feedback"
date: 2025-07-22T00:00:00
---

**Authors:** [Yannan Bai](https://dblp.uni-trier.de/search?q=Yannan+Bai), [Debmalya Panigrahi](https://dblp.uni-trier.de/search?q=Debmalya+Panigrahi), [Ian Zhang](https://dblp.uni-trier.de/search?q=Ian+Zhang)

Kleinberg and Mullainathan (2024) recently proposed a formal framework called
language generation in the limit and showed that given a sequence of example
strings from an unknown target language drawn from any countable collection, an
algorithm can correctly generate unseen strings from the target language within
finite time. This notion was further refined by Li, Raman, and Tewari (2024),
who defined stricter categories of non-uniform and uniform generation. They
showed that a finite union of uniformly generatable collections is generatable
in the limit, and asked if the same is true for non-uniform generation.
We begin by resolving the question in the negative: we give a uniformly
generatable collection and a non-uniformly generatable collection whose union
is not generatable in the limit. We then use facets of this construction to
further our understanding of several variants of language generation. The first
two, generation with noise and without samples, were introduced by Raman and
Raman (2025) and Li, Raman, and Tewari (2024) respectively. We show the
equivalence of these models for uniform and non-uniform generation, and provide
a characterization of non-uniform noisy generation. The former paper asked if
there is any separation between noisy and non-noisy generation in the limit --
we show that such a separation exists even with a single noisy string. Finally,
we study the framework of generation with feedback, introduced by Charikar and
Pabbaraju (2025), where the algorithm is strengthened by allowing it to ask
membership queries. We show finite queries add no power, but infinite queries
yield a strictly more powerful model.
In summary, the results in this paper resolve the union-closedness of
language generation in the limit, and leverage those techniques (and others) to
give precise characterizations for natural variants that incorporate noise,
loss, and feedback.

[Read original post](http://arxiv.org/abs/2507.15319v1)
