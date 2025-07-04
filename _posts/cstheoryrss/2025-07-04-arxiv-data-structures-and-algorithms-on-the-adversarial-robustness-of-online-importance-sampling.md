---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: On the Adversarial Robustness of Online Importance Sampling"
date: 2025-07-04T00:00:00
---

**Authors:** [Yotam Kenneth-Mordoch](https://dblp.uni-trier.de/search?q=Yotam+Kenneth-Mordoch), [Shay Sapir](https://dblp.uni-trier.de/search?q=Shay+Sapir)

This paper studies the adversarial-robustness of importance-sampling (aka
sensitivity sampling); a useful algorithmic technique that samples elements
with probabilities proportional to some measure of their importance. A
streaming or online algorithm is called adversarially-robust if it succeeds
with high probability on input streams that may change adaptively depending on
previous algorithm outputs. Unfortunately, the dependence between stream
elements breaks the analysis of most randomized algorithms, and in particular
that of importance-sampling algorithms. Previously, Braverman et al. [NeurIPS
2021] suggested that streaming algorithms based on importance-sampling may be
adversarially-robust; however, they proved it only for well-behaved inputs.
We focus on the adversarial-robustness of online importance-sampling, a
natural variant where sampling decisions are irrevocable and made as data
arrives. Our main technical result shows that, given as input an adaptive
stream of elements $x\_1,\ldots,x\_T\in \mathbb{R}\_+$, online importance-sampling
maintains a $(1\pm\epsilon)$-approximation of their sum while matching (up to
lower order terms) the storage guarantees of the oblivious (non-adaptive) case.
We then apply this result to develop adversarially-robust online algorithms for
two fundamental problems: hypergraph cut sparsification and $\ell\_p$ subspace
embedding.