---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: On the Complexity of the Skolem Problem at Low Orders"
date: 2025-07-16T00:00:00
---

**Authors:** [Piotr Bacik](https://dblp.uni-trier.de/search?q=Piotr+Bacik), [Joël Ouaknine](https://dblp.uni-trier.de/search?q=Jo%C3%ABl+Ouaknine), [James Worrell](https://dblp.uni-trier.de/search?q=James+Worrell)

The Skolem Problem asks to determine whether a given linear recurrence
sequence (LRS) $\langle u\_n \rangle\_{n=0}^\infty$ over the integers has a zero
term, that is, whether there exists $n$ such that $u\_n = 0$. Decidability of
the problem is open in general, with the most notable positive result being a
decision procedure for LRS of order at most 4.
In this paper we consider a bounded version of the Skolem Problem, in which
the input consists of an LRS $\langle u\_n \rangle\_{n=0}^\infty$ and a bound $N
\in \mathbb N$ (with all integers written in binary), and the task is to
determine whether there exists $n\in\{0,\ldots,N\}$ such that $u\_n=0$. We give
a randomised algorithm for this problem that, for all $d\in \mathbb N$, runs in
polynomial time on the class of LRS of order at most $d$. As a corollary we
show that the (unrestricted) Skolem Problem for LRS of order at most 4 lies in
$\mathsf{coRP}$, improving the best previous upper bound of
$\mathsf{NP}^{\mathsf{RP}}$.
The running time of our algorithm is exponential in the order of the LRS -- a
dependence that appears necessary in view of the $\mathsf{NP}$-hardness of the
Bounded Skolem Problem. However, even for LRS of a fixed order, the problem
involves detecting zeros within an exponentially large range. For this, our
algorithm relies on results from $p$-adic analysis to isolate polynomially many
candidate zeros and then test in randomised polynomial time whether each
candidate is an actual zero by reduction to arithmetic-circuit identity
testing.

[Read original post](http://arxiv.org/abs/2507.11234v1)
