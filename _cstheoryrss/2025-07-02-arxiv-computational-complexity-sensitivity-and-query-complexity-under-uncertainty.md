---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: Sensitivity and Query Complexity under Uncertainty"
date: 2025-07-02T00:00:00
---

**Authors:** [Deepu Benson](https://dblp.uni-trier.de/search?q=Deepu+Benson), [Balagopal Komarath](https://dblp.uni-trier.de/search?q=Balagopal+Komarath), [Nikhil Mande](https://dblp.uni-trier.de/search?q=Nikhil+Mande), [Sai Soumya Nalli](https://dblp.uni-trier.de/search?q=Sai+Soumya+Nalli), [Jayalal Sarma](https://dblp.uni-trier.de/search?q=Jayalal+Sarma), [Karteek Sreenivasaiah](https://dblp.uni-trier.de/search?q=Karteek+Sreenivasaiah)

In this paper, we study the query complexity of Boolean functions in the
presence of uncertainty, motivated by parallel computation with an unlimited
number of processors where inputs are allowed to be unknown. We allow each
query to produce three results: zero, one, or unknown. The output could also
be: zero, one, or unknown, with the constraint that we should output
''unknown'' only when we cannot determine the answer from the revealed input
bits. Such an extension of a Boolean function is called its hazard-free
extension.
- We prove an analogue of Huang's celebrated sensitivity theorem [Annals of
Mathematics, 2019] in our model of query complexity with uncertainty.
- We show that the deterministic query complexity of the hazard-free
extension of a Boolean function is at most quadratic in its randomized query
complexity and quartic in its quantum query complexity, improving upon the
best-known bounds in the Boolean world.
- We exhibit an exponential gap between the smallest depth (size) of decision
trees computing a Boolean function, and those computing its hazard-free
extension.
- We present general methods to convert decision trees for Boolean functions
to those for their hazard-free counterparts, and show optimality of this
construction. We also parameterize this result by the maximum number of unknown
values in the input.
- We show lower bounds on size complexity of decision trees for hazard-free
extensions of Boolean functions in terms of the number of prime implicants and
prime implicates of the underlying Boolean function.

[Read original post](http://arxiv.org/abs/2507.00148v1)
