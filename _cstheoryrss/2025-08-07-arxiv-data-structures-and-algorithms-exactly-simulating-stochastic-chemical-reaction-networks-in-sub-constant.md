---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Exactly simulating stochastic chemical reaction networks in sub-constant"
date: 2025-08-07T00:00:00
---

**Authors:** [Joshua Petrack](https://dblp.uni-trier.de/search?q=Joshua+Petrack), [David Doty](https://dblp.uni-trier.de/search?q=David+Doty)

The model of chemical reaction networks is among the oldest and most widely
studied and used in natural science. The model describes reactions among
abstract chemical species, for instance $A + B \to C$, which indicates that if
a molecule of type $A$ interacts with a molecule of type $B$ (the reactants),
they may stick together to form a molecule of type $C$ (the product). The
standard algorithm for simulating (discrete, stochastic) chemical reaction
networks is the Gillespie algorithm [JPC 1977], which stochastically simulates
one reaction at a time, so to simulate $\ell$ consecutive reactions, it
requires total running time $\Omega(\ell)$.
We give the first chemical reaction network stochastic simulation algorithm
that can simulate $\ell$ reactions, provably preserving the exact stochastic
dynamics (sampling from precisely the same distribution as the Gillespie
algorithm), yet using time provably sublinear in $\ell$. Under reasonable
assumptions, our algorithm can simulate $\ell$ reactions among $n$ total
molecules in time $O(\ell/\sqrt n)$ when $\ell \ge n^{5/4}$, and in time
$O(\ell/n^{2/5})$ when $n \le \ell \le n^{5/4}$. Our work adapts an algorithm
of Berenbrink, Hammer, Kaaser, Meyer, Penschuck, and Tran [ESA 2020] for
simulating the distributed computing model known as population protocols,
extending it (in a very nontrivial way) to the more general chemical reaction
network setting.
We provide an implementation of our algorithm as a Python package, with the
core logic implemented in Rust, with remarkably fast performance in practice.

[Read original post](http://arxiv.org/abs/2508.04079v1)
