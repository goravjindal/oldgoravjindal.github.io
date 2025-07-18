---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: Ranking Vectors Clustering: Theory and Applications"
date: 2025-07-18T00:00:00
---

**Authors:** [Ali Fattahi](https://dblp.uni-trier.de/search?q=Ali+Fattahi), [Ali Eshragh](https://dblp.uni-trier.de/search?q=Ali+Eshragh), [Babak Aslani](https://dblp.uni-trier.de/search?q=Babak+Aslani), [Meysam Rabiee](https://dblp.uni-trier.de/search?q=Meysam+Rabiee)

We study the problem of clustering ranking vectors, where each vector
represents preferences as an ordered list of distinct integers. Specifically,
we focus on the k-centroids ranking vectors clustering problem (KRC), which
aims to partition a set of ranking vectors into k clusters and identify the
centroid of each cluster. Unlike classical k-means clustering (KMC), KRC
constrains both the observations and centroids to be ranking vectors. We
establish the NP-hardness of KRC and characterize its feasible set. For the
single-cluster case, we derive a closed-form analytical solution for the
optimal centroid, which can be computed in linear time. To address the
computational challenges of KRC, we develop an efficient approximation
algorithm, KRCA, which iteratively refines initial solutions from KMC, referred
to as the baseline solution. Additionally, we introduce a branch-and-bound
(BnB) algorithm for efficient cluster reconstruction within KRCA, leveraging a
decision tree framework to reduce computational time while incorporating a
controlling parameter to balance solution quality and efficiency. We establish
theoretical error bounds for KRCA and BnB. Through extensive numerical
experiments on synthetic and real-world datasets, we demonstrate that KRCA
consistently outperforms baseline solutions, delivering significant
improvements in solution quality with fast computational times. This work
highlights the practical significance of KRC for personalization and
large-scale decision making, offering methodological advancements and insights
that can be built upon in future studies.

[Read original post](http://arxiv.org/abs/2507.12583v1)
