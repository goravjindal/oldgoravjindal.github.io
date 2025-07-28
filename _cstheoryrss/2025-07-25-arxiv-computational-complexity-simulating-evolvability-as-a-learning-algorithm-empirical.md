---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: Simulating Evolvability as a Learning Algorithm: Empirical"
date: 2025-07-25T00:00:00
---

**Authors:** [Nicholas Fidalgo](https://dblp.uni-trier.de/search?q=Nicholas+Fidalgo), [Puyuan Ye](https://dblp.uni-trier.de/search?q=Puyuan+Ye)

The theory of evolvability, introduced by Valiant (2009), formalizes
evolution as a constrained learning algorithm operating without labeled
examples or structural knowledge. While theoretical work has established the
evolvability of specific function classes under idealized conditions, the
framework remains largely untested empirically. In this paper, we implement a
genetic algorithm that faithfully simulates Valiant's model and conduct
extensive experiments across six Boolean function classes: monotone
conjunctions, monotone disjunctions, parity, majority, general conjunctions,
and general disjunctions. Our study examines evolvability under uniform and
non-uniform distributions, investigates the effects of fixed initial hypotheses
and the removal of neutral mutations, and highlights how these constraints
alter convergence behavior. We validate known results (e.g., evolvability of
monotone conjunctions, non-evolvability of parity) and offer the first
empirical evidence on the evolvability of majority and general Boolean classes.
Our findings reveal sharp performance drops at intermediate dimensions and
expose the essential role of neutral mutations in escaping fitness plateaus. We
also demonstrate that evolvability can depend strongly on the input
distribution. These insights clarify practical limits of evolutionary search
and suggest new directions for theoretical work, including potential
refinements to evolvability definitions and bounds. Our implementation provides
a rigorous, extensible framework for empirical analysis and serves as a testbed
for future explorations of learning through evolution.

[Read original post](http://arxiv.org/abs/2507.18666v1)
