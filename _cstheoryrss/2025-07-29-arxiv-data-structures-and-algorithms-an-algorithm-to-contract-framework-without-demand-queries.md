---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: An Algorithm-to-Contract Framework without Demand Queries"
date: 2025-07-29T00:00:00
---

**Authors:** [Ilan Doron-Arad](https://dblp.uni-trier.de/search?q=Ilan+Doron-Arad), [Hadas Shachnai](https://dblp.uni-trier.de/search?q=Hadas+Shachnai), [Gilad Shmerler](https://dblp.uni-trier.de/search?q=Gilad+Shmerler), [Inbal Talgam-Cohen](https://dblp.uni-trier.de/search?q=Inbal+Talgam-Cohen)

Consider costly tasks that add up to the success of a project, and must be
fitted by an agent into a given time-frame. This is an instance of the classic
budgeted maximization problem, which admits an approximation scheme (FPTAS).
Now assume the agent is performing these tasks on behalf of a principal, who is
the one to reap the rewards if the project succeeds. The principal must design
a contract to incentivize the agent. Is there still an approximation scheme? In
this work, our ultimate goal is an algorithm-to-contract transformation, which
transforms algorithms for combinatorial problems (like budgeted maximization)
to tackle incentive constraints that arise in contract design. Our approach
diverges from previous works on combinatorial contract design by avoiding an
assumption of black-box access to a demand oracle.
We first show how to "lift" the FPTAS for budgeted maximization to obtain the
best-possible multiplicative and additive FPTAS for the contract design
problem. We establish this through our "local-global" framework, in which the
"local" step is to (approximately) solve a two-sided strengthened variant of
the demand problem. The "global" step then utilizes the local one to find the
approximately optimal contract. We apply our framework to a host of
combinatorial constraints including multi-dimensional budgets, budgeted
matroid, and budgeted matching constraints. In all cases we achieve an
approximation essentially matching the best approximation for the purely
algorithmic problem. We also develop a method to tackle multi-agent contract
settings, where the team of working agents must abide to combinatorial
feasibility constraints.

[Read original post](http://arxiv.org/abs/2507.20038v1)
