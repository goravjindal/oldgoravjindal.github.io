---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Computational-Statistical Tradeoffs from NP-hardness"
date: 2025-07-18T00:00:00
---

**Authors:** [Guy Blanc](https://dblp.uni-trier.de/search?q=Guy+Blanc), [Caleb Koch](https://dblp.uni-trier.de/search?q=Caleb+Koch), [Carmen Strassle](https://dblp.uni-trier.de/search?q=Carmen+Strassle), [Li-Yang Tan](https://dblp.uni-trier.de/search?q=Li-Yang+Tan)

A central question in computer science and statistics is whether efficient
algorithms can achieve the information-theoretic limits of statistical
problems. Many computational-statistical tradeoffs have been shown under
average-case assumptions, but since statistical problems are average-case in
nature, it has been a challenge to base them on standard worst-case
assumptions.
In PAC learning where such tradeoffs were first studied, the question is
whether computational efficiency can come at the cost of using more samples
than information-theoretically necessary. We base such tradeoffs on
$\mathsf{NP}$-hardness and obtain:
$\circ$ Sharp computational-statistical tradeoffs assuming $\mathsf{NP}$
requires exponential time: For every polynomial $p(n)$, there is an $n$-variate
class $C$ with VC dimension $1$ such that the sample complexity of
time-efficiently learning $C$ is $\Theta(p(n))$.
$\circ$ A characterization of $\mathsf{RP}$ vs. $\mathsf{NP}$ in terms of
learning: $\mathsf{RP} = \mathsf{NP}$ iff every $\mathsf{NP}$-enumerable class
is learnable with $O(\mathrm{VCdim}(C))$ samples in polynomial time. The
forward implication has been known since (Pitt and Valiant, 1988); we prove the
reverse implication.
Notably, all our lower bounds hold against improper learners. These are the
first $\mathsf{NP}$-hardness results for improperly learning a subclass of
polynomial-size circuits, circumventing formal barriers of Applebaum, Barak,
and Xiao (2008).

[Read original post](http://arxiv.org/abs/2507.13222v1)
