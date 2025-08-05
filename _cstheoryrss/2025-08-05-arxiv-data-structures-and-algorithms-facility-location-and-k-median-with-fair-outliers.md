---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Facility Location and k-Median with Fair Outliers"
date: 2025-08-05T00:00:00
---

**Authors:** [Rajni Dabas](https://dblp.uni-trier.de/search?q=Rajni+Dabas), [Samir Khuller](https://dblp.uni-trier.de/search?q=Samir+Khuller), [Emilie Rivkin](https://dblp.uni-trier.de/search?q=Emilie+Rivkin)

Classical clustering problems such as \emph{Facility Location} and
\emph{$k$-Median} aim to efficiently serve a set of clients from a subset of
facilities -- minimizing the total cost of facility openings and client
assignments in Facility Location, and minimizing assignment (service) cost
under a facility count constraint in $k$-Median. These problems are highly
sensitive to outliers, and therefore researchers have studied variants that
allow excluding a small number of clients as outliers to reduce cost. However,
in many real-world settings, clients belong to different demographic or
functional groups, and unconstrained outlier removal can disproportionately
exclude certain groups, raising fairness concerns.
We study \emph{Facility Location with Fair Outliers}, where each group is
allowed a specified number of outliers, and the objective is to minimize total
cost while respecting group-wise fairness constraints. We present a bicriteria
approximation with a $O(1/\epsilon)$ approximation factor and $(1+ 2\epsilon)$
factor violation in outliers per group. For \emph{$k$-Median with Fair
Outliers}, we design a bicriteria approximation with a $4(1+\omega/\epsilon)$
approximation factor and $(\omega + \epsilon)$ violation in outliers per group
improving on prior work by avoiding dependence on $k$ in outlier violations. We
also prove that the problems are W[1]-hard parameterized by $\omega$, assuming
the Exponential Time Hypothesis.
We complement our algorithmic contributions with a detailed empirical
analysis, demonstrating that fairness can be achieved with negligible increase
in cost and that the integrality gap of the standard LP is small in practice.

[Read original post](http://arxiv.org/abs/2508.02572v1)
