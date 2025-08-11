---
layout: post
category: cstheoryrss
title: "ECCC Papers: TR25-120 | Asymptotically Optimal Inapproximability of Ek-SAT Reconfiguration |"
date: 2025-08-10T11:07:30
---

In the Maxmin E$k$-SAT Reconfiguration problem, we are given a satisfiable $k$-CNF formula $\varphi$ where each clause contains exactly $k$ literals, along with a pair of its satisfying assignments. The objective is transform one satisfying assignment into the other by repeatedly flipping the value of a single variable, while maximizing the minimum fraction of satisfied clauses of $\varphi$ throughout the transformation. In this paper, we demonstrate that the optimal approximation factor for Maxmin E$k$-SAT Reconfiguration is $1 - \Theta\left(\frac{1}{k}\right)$. On the algorithmic side, we develop a deterministic $\left(1-\frac{1}{k-1}-\frac{1}{k}\right)$-factor approximation algorithm for every $k \geq 3$. On the hardness side, we show that it is PSPACE-hard to approximate this problem within a factor of $1-\frac{1}{10k}$ for every sufficiently large $k$. Note that an “NP analogue” of Maxmin E$k$-SAT Reconfiguration is Max E$k$-SAT, whose approximation threshold is $1-\frac{1}{2^k}$ shown by Håstad (JACM 2001). To the best of our knowledge, this is the first reconfiguration problem whose approximation threshold is (asymptotically) worse than that of its NP analogue. To prove the hardness result, we introduce a new “non-monotone” test, which is specially tailored to reconfiguration problems, despite not being helpful in the PCP regime.

[Read original post](https://eccc.weizmann.ac.il/report/2025/120)
