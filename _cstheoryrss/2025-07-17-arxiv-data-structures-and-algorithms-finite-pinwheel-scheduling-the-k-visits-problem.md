---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Finite Pinwheel Scheduling: the k-Visits Problem"
date: 2025-07-17T00:00:00
---

**Authors:** [Sotiris Kanellopoulos](https://dblp.uni-trier.de/search?q=Sotiris+Kanellopoulos), [Christos Pergaminelis](https://dblp.uni-trier.de/search?q=Christos+Pergaminelis), [Maria Kokkou](https://dblp.uni-trier.de/search?q=Maria+Kokkou), [Euripides Markou](https://dblp.uni-trier.de/search?q=Euripides+Markou), [Aris Pagourtzis](https://dblp.uni-trier.de/search?q=Aris+Pagourtzis)

Pinwheel Scheduling is a fundamental scheduling problem, in which each task
$i$ is associated with a positive integer $d\_i$, and the objective is to
schedule one task per time slot, ensuring each task perpetually appears at
least once in every $d\_i$ time slots. Although conjectured to be
PSPACE-complete, it remains open whether Pinwheel Scheduling is NP-hard (unless
a compact input encoding is used) or even contained in NP.
We introduce k-Visits, a finite version of Pinwheel Scheduling, where given n
deadlines, the goal is to schedule each task exactly k times. While we observe
that the 1-Visit problem is trivial, we prove that 2-Visits is strongly
NP-complete through a surprising reduction from Numerical 3-Dimensional
Matching (N3DM). As intermediate steps in the reduction, we define NP-complete
variants of N3DM which may be of independent interest. We further extend our
strong NP-hardness result to a generalization of k-Visits $k\geq 2$ in which
the deadline of each task may vary throughout the schedule, as well as to a
similar generalization of Pinwheel Scheduling, thus making progress towards
settling the complexity of Pinwheel Scheduling.
Additionally, we prove that 2-Visits can be solved in linear time if all
deadlines are distinct, rendering it one of the rare natural problems which
exhibit the interesting dichotomy of being in P if their input is a set and
NP-complete if the input is a multiset. We achieve this through a Turing
reduction from 2-Visits to a variation of N3DM, which we call Position
Matching. Based on this reduction, we also show an FPT algorithm for 2-Visits
parameterized by a value related to how close the input deadlines are to each
other, as well as a linear-time algorithm for instances with up to two distinct
deadlines.

[Read original post](http://arxiv.org/abs/2507.11681v1)
