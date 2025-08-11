---
layout: post
category: cstheoryrss
title: "ECCC Papers: TR25-121 | Downward self-reducibility in the total function polynomial hierarchy |"
date: 2025-08-10T11:08:03
---

A problem $\mathcal{P}$ is considered downward self-reducible, if there exists an efficient algorithm for $\mathcal{P}$ that is allowed to make queries to only strictly smaller instances of $\mathcal{P}$. Downward self-reducibility has been well studied in the case of decision problems, and it is well known that any downward self-reducible problem must lie in ${PSPACE}$. Harsha, Mitropolsky and Rosen [ITCS, 2023] initiated the study of downward self reductions in the case of search problems. They showed the following interesting collapse: if a problem is in ${TFNP}$ and also downward self-reducible, then it must be in ${PLS}$. Moreover, if the problem admits a unique solution then it must be in ${UEOPL}$.
We demonstrate that this represents just the tip of a much more general phenomenon, which holds for even harder search problems that lie higher up in the total function polynomial hierarchy (${TF\Sigma\_i^P}$). In fact, even if we allow our downward self-reduction to be much more powerful, such a collapse will still occur.
We show that any problem in ${TF\Sigma\_i^P}$ which admits a randomized downward self-reduction with access to a ${\Sigma\_{i-1}^P}$ oracle must be in ${PLS}^{{\Sigma\_{i-1}^P}}$. If the problem has essentially unique solutions then it lies in ${UEOPL}^{{\Sigma\_{i-1}^P}}$.
As one (out of many) application of our framework, we get new upper bounds for the problems $\mathrm{Range Avoidance}$ and $\mathrm{Linear Ordering Principle}$ and show that they are both in ${UEOPL}^{{NP}}$.

[Read original post](https://eccc.weizmann.ac.il/report/2025/121)
