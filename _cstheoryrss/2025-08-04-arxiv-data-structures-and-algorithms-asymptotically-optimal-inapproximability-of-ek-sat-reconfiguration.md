---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Asymptotically Optimal Inapproximability of Ek-SAT Reconfiguration"
date: 2025-08-04T00:00:00
---

**Authors:** [Shuichi Hirahara](https://dblp.uni-trier.de/search?q=Shuichi+Hirahara), [Naoto Ohsaka](https://dblp.uni-trier.de/search?q=Naoto+Ohsaka)

In the Maxmin E$k$-SAT Reconfiguration problem, we are given a satisfiable
$k$-CNF formula $\varphi$ where each clause contains exactly $k$ literals,
along with a pair of its satisfying assignments. The objective is transform one
satisfying assignment into the other by repeatedly flipping the value of a
single variable, while maximizing the minimum fraction of satisfied clauses of
$\varphi$ throughout the transformation. In this paper, we demonstrate that the
optimal approximation factor for Maxmin E$k$-SAT Reconfiguration is $1 -
\Theta\left(\frac{1}{k}\right)$. On the algorithmic side, we develop a
deterministic $\left(1-\frac{1}{k-1}-\frac{1}{k}\right)$-factor approximation
algorithm for every $k \geq 3$. On the hardness side, we show that it is
$\mathsf{PSPACE}$-hard to approximate this problem within a factor of
$1-\frac{1}{10k}$ for every sufficiently large $k$. Note that an
``$\mathsf{NP}$ analogue'' of Maxmin E$k$-SAT Reconfiguration is Max E$k$-SAT,
whose approximation threshold is $1-\frac{1}{2^k}$ shown by H\r{a}stad (JACM
2001). To the best of our knowledge, this is the first reconfiguration problem
whose approximation threshold is (asymptotically) worse than that of its
$\mathsf{NP}$ analogue. To prove the hardness result, we introduce a new
``non-monotone'' test, which is specially tailored to reconfiguration problems,
despite not being helpful in the PCP regime.

[Read original post](http://arxiv.org/abs/2508.00276v1)
