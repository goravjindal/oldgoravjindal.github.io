---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: A Simple Algorithm for Trimmed Multipoint Evaluation"
date: 2025-07-02T00:00:00
---

**Authors:** [Nick Fischer](https://dblp.uni-trier.de/search?q=Nick+Fischer), [Melvin Kallmayer](https://dblp.uni-trier.de/search?q=Melvin+Kallmayer), [Leo Wennmann](https://dblp.uni-trier.de/search?q=Leo+Wennmann)

Evaluating a polynomial on a set of points is a fundamental task in computer
algebra. In this work, we revisit a particular variant called trimmed
multipoint evaluation: given an $n$-variate polynomial with bounded individual
degree $d$ and total degree $D$, the goal is to evaluate it on a natural class
of input points. This problem arises as a key subroutine in recent algorithmic
results [Dinur; SODA '21], [Dell, Haak, Kallmayer, Wennmann; SODA '25]. It is
known that trimmed multipoint evaluation can be solved in near-linear time [van
der Hoeven, Schost; AAECC '13] by a clever yet somewhat involved algorithm. We
give a simple recursive algorithm that avoids heavy computer-algebraic
machinery, and can be readily understood by researchers without specialized
background.