---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Better Models and Algorithms for Learning Ising Models from Dynamics"
date: 2025-07-22T00:00:00
---

**Authors:** [Jason Gaitonde](https://dblp.uni-trier.de/search?q=Jason+Gaitonde), [Ankur Moitra](https://dblp.uni-trier.de/search?q=Ankur+Moitra), [Elchanan Mossel](https://dblp.uni-trier.de/search?q=Elchanan+Mossel)

We study the problem of learning the structure and parameters of the Ising
model, a fundamental model of high-dimensional data, when observing the
evolution of an associated Markov chain. A recent line of work has studied the
natural problem of learning when observing an evolution of the well-known
Glauber dynamics [Bresler, Gamarnik, Shah, IEEE Trans. Inf. Theory 2018,
Gaitonde, Mossel STOC 2024], which provides an arguably more realistic
generative model than the classical i.i.d. setting. However, this prior work
crucially assumes that all site update attempts are observed, \emph{even when
this attempt does not change the configuration}: this strong observation model
is seemingly essential for these approaches. While perhaps possible in
restrictive contexts, this precludes applicability to most realistic settings
where we can observe \emph{only} the stochastic evolution itself, a minimal and
natural assumption for any process we might hope to learn from. However,
designing algorithms that succeed in this more realistic setting has remained
an open problem [Bresler, Gamarnik, Shah, IEEE Trans. Inf. Theory 2018,
Gaitonde, Moitra, Mossel, STOC 2025].
In this work, we give the first algorithms that efficiently learn the Ising
model in this much more natural observation model that only observes when the
configuration changes. For Ising models with maximum degree $d$, our algorithm
recovers the underlying dependency graph in time $\mathsf{poly}(d)\cdot n^2\log
n$ and then the actual parameters in additional $\widetilde{O}(2^d n)$ time,
which qualitatively matches the state-of-the-art even in the i.i.d. setting in
a much weaker observation model. Our analysis holds more generally for a
broader class of reversible, single-site Markov chains that also includes the
popular Metropolis chain by leveraging more robust properties of reversible
Markov chains.

[Read original post](http://arxiv.org/abs/2507.15173v1)
