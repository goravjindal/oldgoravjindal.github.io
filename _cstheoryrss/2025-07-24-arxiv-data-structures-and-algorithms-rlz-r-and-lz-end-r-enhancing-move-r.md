---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: RLZ-r and LZ-End-r: Enhancing Move-r"
date: 2025-07-24T00:00:00
---

**Authors:** [Patrick Dinklage](https://dblp.uni-trier.de/search?q=Patrick+Dinklage), [Johannes Fischer](https://dblp.uni-trier.de/search?q=Johannes+Fischer), [Lukas Nalbach](https://dblp.uni-trier.de/search?q=Lukas+Nalbach), [Jan Zumbrink](https://dblp.uni-trier.de/search?q=Jan+Zumbrink)

In pattern matching on strings, a locate query asks for an enumeration of all
the occurrences of a given pattern in a given text. The r-index [Gagie et al.,
2018] is a recently presented compressed self index that stores the text and
auxiliary information in compressed space. With some modifications, locate
queries can be answered in optimal time [Nishimoto & Tabei, 2021], which has
recently been proven relevant in practice in the form of Move-r [Bertram et
al., 2024]. However, there remains the practical bottleneck of evaluating
function $\Phi$ for every occurrence to report. This motivates enhancing the
index by a compressed representation of the suffix array featuring efficient
random access, trading off space for faster answering of locate queries
[Puglisi & Zhukova, 2021]. In this work, we build upon this idea considering
two suitable compression schemes: Relative Lempel-Ziv [Kuruppu et al., 2010],
improving the work by Puglisi and Zhukova, and LZ-End [Kreft & Navarro, 2010],
introducing a different trade-off where compression is better than for Relative
Lempel-Ziv at the cost of slower access times. We enhance both the r-index and
Move-r by the compressed suffix arrays and evaluate locate query performance in
an experiment. We show that locate queries can be sped up considerably in both
the r-index and Move-r, especially if the queried pattern has many occurrences.
The choice between two different compression schemes offers new trade-offs
regarding index size versus query performance.

[Read original post](http://arxiv.org/abs/2507.17300v1)
