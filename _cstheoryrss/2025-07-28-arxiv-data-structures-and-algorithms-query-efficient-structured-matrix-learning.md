---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Query Efficient Structured Matrix Learning"
date: 2025-07-28T00:00:00
---

**Authors:** [Noah Amsel](https://dblp.uni-trier.de/search?q=Noah+Amsel), [Pratyush Avi](https://dblp.uni-trier.de/search?q=Pratyush+Avi), [Tyler Chen](https://dblp.uni-trier.de/search?q=Tyler+Chen), [Feyza Duman Keles](https://dblp.uni-trier.de/search?q=Feyza+Duman+Keles), [Chinmay Hegde](https://dblp.uni-trier.de/search?q=Chinmay+Hegde), [Cameron Musco](https://dblp.uni-trier.de/search?q=Cameron+Musco), [Christopher Musco](https://dblp.uni-trier.de/search?q=Christopher+Musco), [David Persson](https://dblp.uni-trier.de/search?q=David+Persson)

We study the problem of learning a structured approximation (low-rank,
sparse, banded, etc.) to an unknown matrix $A$ given access to matrix-vector
product (matvec) queries of the form $x \rightarrow Ax$ and $x \rightarrow
A^Tx$. This problem is of central importance to algorithms across scientific
computing and machine learning, with applications to fast multiplication and
inversion for structured matrices, building preconditioners for first-order
optimization, and as a model for differential operator learning. Prior work
focuses on obtaining query complexity upper and lower bounds for learning
specific structured matrix families that commonly arise in applications.
We initiate the study of the problem in greater generality, aiming to
understand the query complexity of learning approximations from general matrix
families. Our main result focuses on finding a near-optimal approximation to
$A$ from any finite-sized family of matrices, $\mathcal{F}$. Standard results
from matrix sketching show that $O(\log|\mathcal{F}|)$ matvec queries suffice
in this setting. This bound can also be achieved, and is optimal, for
vector-matrix-vector queries of the form $x,y\rightarrow x^TAy$, which have
been widely studied in work on rank-$1$ matrix sensing.
Surprisingly, we show that, in the matvec model, it is possible to obtain a
nearly quadratic improvement in complexity, to
$\tilde{O}(\sqrt{\log|\mathcal{F}|})$. Further, we prove that this bound is
tight up to log-log factors.Via covering number arguments, our result extends
to well-studied infinite families. As an example, we establish that a
near-optimal approximation from any \emph{linear matrix family} of dimension
$q$ can be learned with $\tilde{O}(\sqrt{q})$ matvec queries, improving on an
$O(q)$ bound achievable via sketching techniques and vector-matrix-vector
queries.

[Read original post](http://arxiv.org/abs/2507.19290v1)
