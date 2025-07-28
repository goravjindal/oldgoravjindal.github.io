---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Downward self-reducibility in the total function polynomial hierarchy"
date: 2025-07-28T00:00:00
---

**Authors:** [Karthik Gajulapalli](https://dblp.uni-trier.de/search?q=Karthik+Gajulapalli), [Surendra Ghentiyala](https://dblp.uni-trier.de/search?q=Surendra+Ghentiyala), [Zeyong Li](https://dblp.uni-trier.de/search?q=Zeyong+Li), [Sidhant Saraogi](https://dblp.uni-trier.de/search?q=Sidhant+Saraogi)

A problem $\mathcal{P}$ is considered downward self-reducible, if there
exists an efficient algorithm for $\mathcal{P}$ that is allowed to make queries
to only strictly smaller instances of $\mathcal{P}$. Downward self-reducibility
has been well studied in the case of decision problems, and it is well known
that any downward self-reducible problem must lie in $\mathsf{PSPACE}$. Harsha,
Mitropolsky and Rosen [ITCS, 2023] initiated the study of downward self
reductions in the case of search problems. They showed the following
interesting collapse: if a problem is in $\mathsf{TFNP}$ and also downward
self-reducible, then it must be in $\mathsf{PLS}$. Moreover, if the problem
admits a unique solution then it must be in $\mathsf{UEOPL}$.
We demonstrate that this represents just the tip of a much more general
phenomenon, which holds for even harder search problems that lie higher up in
the total function polynomial hierarchy ($\mathsf{TF\Sigma\_i^P}$). In fact,
even if we allow our downward self-reduction to be much more powerful, such a
collapse will still occur.
We show that any problem in $\mathsf{TF\Sigma\_i^P}$ which admits a randomized
downward self-reduction with access to a $\mathsf{\Sigma\_{i-1}^P}$ oracle must
be in $\mathsf{PLS}^{\mathsf{\Sigma\_{i-1}^P}}$. If the problem has
\textit{essentially unique solutions} then it lies in
$\mathsf{UEOPL}^{\mathsf{\Sigma\_{i-1}^P}}$.
As one (out of many) application of our framework, we get new upper bounds
for the problems $\mathrm{Range Avoidance}$ and $\mathrm{Linear Ordering
Principle}$ and show that they are both in $\mathsf{UEOPL}^{\mathsf{NP}}$.

[Read original post](http://arxiv.org/abs/2507.19108v1)
