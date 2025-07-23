---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: The Cost of Compression: Tight Quadratic Black-Box Attacks on Sketches"
date: 2025-07-23T00:00:00
---

**Authors:** [Sara Ahmadian](https://dblp.uni-trier.de/search?q=Sara+Ahmadian), [Edith Cohen](https://dblp.uni-trier.de/search?q=Edith+Cohen), [Uri Stemmer](https://dblp.uni-trier.de/search?q=Uri+Stemmer)

Dimensionality reduction via linear sketching is a powerful and widely used
technique, but it is known to be vulnerable to adversarial inputs. We study the
black-box adversarial setting, where a fixed, hidden sketching matrix A in
$R^{k X n}$ maps high-dimensional vectors v $\in R^n$ to lower-dimensional
sketches A v in $R^k$, and an adversary can query the system to obtain
approximate ell2-norm estimates that are computed from the sketch.
We present a universal, nonadaptive attack that, using tilde(O)($k^2$)
queries, either causes a failure in norm estimation or constructs an
adversarial input on which the optimal estimator for the query distribution
(used by the attack) fails. The attack is completely agnostic to the sketching
matrix and to the estimator: It applies to any linear sketch and any query
responder, including those that are randomized, adaptive, or tailored to the
query distribution.
Our lower bound construction tightly matches the known upper bounds of
tilde(Omega)($k^2$), achieved by specialized estimators for Johnson
Lindenstrauss transforms and AMS sketches. Beyond sketching, our results
uncover structural parallels to adversarial attacks in image classification,
highlighting fundamental vulnerabilities of compressed representations.

[Read original post](http://arxiv.org/abs/2507.16345v1)
