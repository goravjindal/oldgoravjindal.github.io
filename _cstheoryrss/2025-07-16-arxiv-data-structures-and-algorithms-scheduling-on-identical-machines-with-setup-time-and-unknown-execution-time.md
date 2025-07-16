---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Scheduling on Identical Machines with Setup Time and Unknown Execution
  Time"
date: 2025-07-16T00:00:00
---

**Authors:** [Yasushi Kawase](https://dblp.uni-trier.de/search?q=Yasushi+Kawase), [Kazuhisa Makino](https://dblp.uni-trier.de/search?q=Kazuhisa+Makino), [Vinh Long Phan](https://dblp.uni-trier.de/search?q=Vinh+Long+Phan), [Hanna Sumita](https://dblp.uni-trier.de/search?q=Hanna+Sumita)

In this study, we investigate a scheduling problem on identical machines in
which jobs require initial setup before execution. We assume that an algorithm
can dynamically form a batch (i.e., a collection of jobs to be processed
together) from the remaining jobs. The setup time is modeled as a known
monotone function of the set of jobs within a batch, while the execution time
of each job remains unknown until completion. This uncertainty poses
significant challenges for minimizing the makespan. We address these challenges
by considering two scenarios: each job batch must be assigned to a single
machine, or a batch may be distributed across multiple machines. For both
scenarios, we analyze settings with and without preemption. Across these four
settings, we design online algorithms that achieve asymptotically optimal
competitive ratios with respect to both the number of jobs and the number of
machines.

[Read original post](http://arxiv.org/abs/2507.11311v1)
