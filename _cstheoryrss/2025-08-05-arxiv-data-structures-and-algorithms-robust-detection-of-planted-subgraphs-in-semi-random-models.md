---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Robust Detection of Planted Subgraphs in Semi-Random Models"
date: 2025-08-05T00:00:00
---

**Authors:** [Dor Elimelech](https://dblp.uni-trier.de/search?q=Dor+Elimelech), [Wasim Huleihel](https://dblp.uni-trier.de/search?q=Wasim+Huleihel)

Detection of planted subgraphs in Erd\"os-R\'enyi random graphs has been
extensively studied, leading to a rich body of results characterizing both
statistical and computational thresholds. However, most prior work assumes a
purely random generative model, making the resulting algorithms potentially
fragile in the face of real-world perturbations. In this work, we initiate the
study of semi-random models for the planted subgraph detection problem, wherein
an adversary is allowed to remove edges outside the planted subgraph before the
graph is revealed to the statistician. Crucially, the statistician remains
unaware of which edges have been removed, introducing fundamental challenges to
the inference task. We establish fundamental statistical limits for detection
under this semi-random model, revealing a sharp dichotomy. Specifically, for
planted subgraphs with strongly sub-logarithmic maximum density detection
becomes information-theoretically impossible in the presence of an adversary,
despite being possible in the classical random model. In stark contrast, for
subgraphs with super-logarithmic density, the statistical limits remain
essentially unchanged; we prove that the optimal (albeit computationally
intractable) likelihood ratio test remains robust. Beyond these statistical
boundaries, we design a new computationally efficient and robust detection
algorithm, and provide rigorous statistical guarantees for its performance. Our
results establish the first robust framework for planted subgraph detection and
open new directions in the study of semi-random models,
computational-statistical trade-offs, and robustness in graph inference
problems.

[Read original post](http://arxiv.org/abs/2508.02158v1)
