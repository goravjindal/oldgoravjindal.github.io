---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: Proof complexity of Mal'tsev CSP"
date: 2025-08-04T00:00:00
---

**Authors:** [Azza Gaysin](https://dblp.uni-trier.de/search?q=Azza+Gaysin)

Constraint Satisfaction Problems (CSPs) form a broad class of combinatorial
problems, which can be formulated as homomorphism problems between relational
structures. The CSP dichotomy theorem classifies all such problems over finite
domains into two categories: NP-complete and polynomial-time, see Zhuk (2017),
Bulatov (2017). Polynomial-time CSPs can be further subdivided into smaller
subclasses. Mal'tsev CSPs are defined by the property that every relation in
the problem is invariant under a Mal'tsev operation, a ternary operation $\mu$
satisfying $\mu(x, y, y) = \mu(y, y, x) = x$ for all $x, y$. Bulatov and Dalmau
proved that Mal'tsev CSPs are solvable in polynomial time, presenting an
algorithm for such CSPs (2006). The negation of an unsatisfiable CSP instance
can be expressed as a propositional tautology. We formalize the algorithm for
Mal'tsev CSPs within bounded arithmetic $V^1$, which captures polynomial-time
reasoning and corresponds to the extended Frege proof system. We show that
$V^1$ proves the soundness of Mal'tsev algorithm, implying that tautologies
expressing the non-existence of a solution for unsatisfiable instances of
Mal'tsev CSPs admit short extended Frege proofs. In addition, with small
adjustments, we achieved an analogous result for Dalmau's algorithm that solves
generalized majority-minority CSPs -- a common generalization of near-unanimity
operations and Mal'tsev operations.

[Read original post](http://arxiv.org/abs/2508.00396v1)
