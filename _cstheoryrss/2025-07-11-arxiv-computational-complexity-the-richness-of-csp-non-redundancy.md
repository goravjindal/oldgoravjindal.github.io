---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: The Richness of CSP Non-redundancy"
date: 2025-07-11T00:00:00
---

**Authors:** [Joshua Brakensiek](https://dblp.uni-trier.de/search?q=Joshua+Brakensiek), [Venkatesan Guruswami](https://dblp.uni-trier.de/search?q=Venkatesan+Guruswami), [Bart M. P. Jansen](https://dblp.uni-trier.de/search?q=Bart+M.+P.+Jansen), [Victor Lagerkvist](https://dblp.uni-trier.de/search?q=Victor+Lagerkvist), [Magnus Wahlström](https://dblp.uni-trier.de/search?q=Magnus+Wahlstr%C3%B6m)

In the field of constraint satisfaction problems (CSP), a clause is called
redundant if its satisfaction is implied by satisfying all other clauses. An
instance of CSP$(P)$ is called non-redundant if it does not contain any
redundant clause. The non-redundancy (NRD) of a predicate $P$ is the maximum
number of clauses in a non-redundant instance of CSP$(P)$, as a function of the
number of variables $n$. Recent progress has shown that non-redundancy is
crucially linked to many other important questions in computer science and
mathematics including sparsification, kernelization, query complexity,
universal algebra, and extremal combinatorics. Given that non-redundancy is a
nexus for many of these important problems, the central goal of this paper is
to more deeply understand non-redundancy.
Our first main result shows that for every rational number $r \ge 1$, there
exists a finite CSP predicate $P$ such that the non-redundancy of $P$ is
$\Theta(n^r)$. Our second main result explores the concept of conditional
non-redundancy first coined by Brakensiek and Guruswami [STOC 2025]. We
completely classify the conditional non-redundancy of all binary predicates
(i.e., constraints on two variables) by connecting these non-redundancy
problems to the structure of high-girth graphs in extremal combinatorics.
Inspired by these concrete results, we build off the work of Carbonnel [CP
2022] to develop an algebraic theory of conditional non-redundancy. As an
application of this algebraic theory, we revisit the notion of Mal'tsev
embeddings, which is the most general technique known to date for establishing
that a predicate has linear non-redundancy. For example, we provide the first
example of predicate with a Mal'tsev embedding that cannot be attributed to the
structure of an Abelian group, but rather to the structure of the quantum Pauli
group.

[Read original post](http://arxiv.org/abs/2507.07942v1)
