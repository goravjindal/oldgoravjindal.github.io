---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Sampling and Identity-Testing Without Approximate Tensorization of
  Entropy"
date: 2025-07-01T00:00:00
---

**Authors:** [William Gay](https://dblp.uni-trier.de/search?q=William+Gay), [William He](https://dblp.uni-trier.de/search?q=William+He), [Nicholas Kocurek](https://dblp.uni-trier.de/search?q=Nicholas+Kocurek), [Ryan O'Donnell](https://dblp.uni-trier.de/search?q=Ryan+O%27Donnell)

Certain tasks in high-dimensional statistics become easier when the
underlying distribution satisfies a local-to-global property called approximate
tensorization of entropy (ATE). For example, the Glauber dynamics Markov chain
of an ATE distribution mixes fast and can produce approximate samples in a
small amount of time, since such a distribution satisfies a modified
log-Sobolev inequality. Moreover, identity-testing for an ATE distribution
requires few samples if the tester is given coordinate conditional access to
the unknown distribution, as shown by Blanca, Chen, \v{S}tefankovi\v{c}, and
Vigoda (COLT 2023).
A natural class of distributions that do not satisfy ATE consists of mixtures
of (few) distributions that do satisfy ATE. We study the complexity of
identity-testing and sampling for these distributions. Our main results are the
following:
1. We show fast mixing of Glauber dynamics from a data-based initialization,
with optimal sample complexity, for mixtures of distributions satisfying
modified log-Sobolev inequalities. This extends work of Huang, Koehler, Lee,
Mohanty, Rajaraman, Vuong, and Wu (STOC 2025, COLT 2025) for mixtures of
distributions satisfying Poincar\'e inequalities.
2. Answering an open question posed by Blanca et al., we give efficient
identity-testers for mixtures of ATE distributions in the
coordinate-conditional sampling access model. We also give some simplifications
and improvements to the original algorithm of Blanca et al.