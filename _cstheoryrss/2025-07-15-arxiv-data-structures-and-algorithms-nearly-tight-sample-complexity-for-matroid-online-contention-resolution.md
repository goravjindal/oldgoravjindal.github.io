---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Nearly Tight Sample Complexity for Matroid Online Contention Resolution"
date: 2025-07-15T00:00:00
---

**Authors:** [Moran Feldman](https://dblp.uni-trier.de/search?q=Moran+Feldman), [Ola Svensson](https://dblp.uni-trier.de/search?q=Ola+Svensson), [Rico Zenklusen](https://dblp.uni-trier.de/search?q=Rico+Zenklusen)

Due to their numerous applications, in particular in Mechanism Design,
Prophet Inequalities have experienced a surge of interest. They describe
competitive ratios for basic stopping time problems where random variables get
revealed sequentially. A key drawback in the classical setting is the
assumption of full distributional knowledge of the involved random variables,
which is often unrealistic. A natural way to address this is via sample-based
approaches, where only a limited number of samples from the distribution of
each random variable is available. Recently, Fu, Lu, Gavin Tang, Wu, Wu, and
Zhang (2024) showed that sample-based Online Contention Resolution Schemes
(OCRS) are a powerful tool to obtain sample-based Prophet Inequalities. They
presented the first sample-based OCRS for matroid constraints, which is a
heavily studied constraint family in this context, as it captures many
interesting settings. This allowed them to get the first sample-based Matroid
Prophet Inequality, using $O(\log^4 n)$ many samples (per random variable),
where $n$ is the number of random variables, while obtaining a constant
competitiveness of $\frac{1}{4}-\varepsilon$.
We present a nearly optimal sample-based OCRS for matroid constraints, which
uses only $O(\log \rho \cdot \log^2\log\rho)$ many samples, almost matching a
known lower bound of $\Omega(\log \rho)$, where $\rho \leq n$ is the rank of
the matroid. Through the above-mentioned connection to Prophet Inequalities,
this yields a sample-based Matroid Prophet Inequality using only $O(\log n +
\log\rho \cdot \log^2\log\rho)$ many samples, and matching the competitiveness
of $\frac{1}{4}-\varepsilon$, which is the best known competitiveness for the
considered almighty adversary setting even when the distributions are fully
known.

[Read original post](http://arxiv.org/abs/2507.09507v1)
