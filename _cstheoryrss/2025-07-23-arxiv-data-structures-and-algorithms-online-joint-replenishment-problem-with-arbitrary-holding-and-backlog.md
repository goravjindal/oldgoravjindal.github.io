---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Online Joint Replenishment Problem with Arbitrary Holding and Backlog"
date: 2025-07-23T00:00:00
---

**Authors:** [Yossi Azar](https://dblp.uni-trier.de/search?q=Yossi+Azar), [Shahar Lewkowicz](https://dblp.uni-trier.de/search?q=Shahar+Lewkowicz)

In their seminal paper Moseley, Niaparast, and Ravi introduced the Joint
Replenishment Problem (JRP) with holding and backlog costs that models the
trade-off between ordering costs, holding costs, and backlog costs in supply
chain planning systems. Their model generalized the classical the make-to-order
version as well make-to-stock version. For the case where holding costs
function of all items are the same and all backlog costs are the same, they
provide a constant competitive algorithm, leaving designing a constant
competitive algorithm for arbitrary functions open. Moreover, they noticed that
their algorithm does not work for arbitrary (request dependent) holding costs
and backlog costs functions. We resolve their open problem and design a
constant competitive algorithm that works for arbitrary request dependent
functions. Specifically, we establish a 4-competitive algorithm for the
single-item case and a 16-competitive for the general (multi-item) version. The
algorithm of Moseley, Niaparast, and Ravi is based on fixed priority on the
requests to items, and request to an item are always served by order of
deadlines. In contrast, we design an algorithm with dynamic priority over the
requests such that instead of servicing a prefix by deadline of requests, we
may need to service a general subset of the requests.

[Read original post](http://arxiv.org/abs/2507.16096v1)
