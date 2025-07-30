---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Towards Tight Bounds for Estimating Degree Distribution in Streaming and"
date: 2025-07-30T00:00:00
---

**Authors:** [Arijit Bishnu](https://dblp.uni-trier.de/search?q=Arijit+Bishnu), [Debarshi Chanda](https://dblp.uni-trier.de/search?q=Debarshi+Chanda), [Gopinath Mishra](https://dblp.uni-trier.de/search?q=Gopinath+Mishra)

The degree distribution of a graph $G=(V,E)$, $|V|=n$, $|E|=m$ is one of the
most fundamental objects of study in the analysis of graphs as it embodies
relationship among entities. In particular, an important derived distribution
from degree distribution is the complementary cumulative degree histogram
(ccdh). The ccdh is a fundamental summary of graph structure, capturing, for
each threshold $d$, the number of vertices with degree at least $d$. For
approximating ccdh, we consider the $(\varepsilon\_D,\varepsilon\_R)$-BiCriteria
Multiplicative Approximation, which allows for controlled multiplicative slack
in both the domain and the range. The exact complexity of the problem was not
known and had been posed as an open problem in WOLA 2019 [Sublinear.info,
Problem 98].
In this work, we first design an algorithm that can approximate ccdh if a
suitable vertex sample and an edge sample can be obtained and thus, the
algorithm is independent of any sublinear model. Next, we show that in the
streaming and query models, these samples can be obtained efficiently. On the
other end, we establish the first lower bounds for this problem in both query
and streaming models, and (almost) settle the complexity of the problem across
both the sublinear models.

[Read original post](http://arxiv.org/abs/2507.21784v1)
