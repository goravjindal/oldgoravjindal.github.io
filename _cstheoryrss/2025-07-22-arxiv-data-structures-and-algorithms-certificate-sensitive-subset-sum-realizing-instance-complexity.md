---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Certificate-Sensitive Subset Sum: Realizing Instance Complexity"
date: 2025-07-22T00:00:00
---

**Authors:** [Jesus Salas](https://dblp.uni-trier.de/search?q=Jesus+Salas)

We present, to our knowledge, the first deterministic, certificate-sensitive
algorithm for a canonical NP-complete problem whose runtime provably adapts to
the structure of each input. For a Subset-Sum instance $(S, t)$, let
$\Sigma(S)$ denote the set of distinct subset sums and define $U =
|\Sigma(S)|$. This set serves as an information-theoretically minimal witness,
the instance-complexity (IC) certificate.
Our solver, IC-SubsetSum, enumerates every element of $\Sigma(S)$ in
deterministic time $O(U \cdot n^2)$ and space $O(U \cdot n)$. A randomized
variant achieves expected runtime $O(U \cdot n)$. The algorithm's complexity is
thus directly governed by the certificate size, and this structure-sensitive
performance is paired with a guaranteed worst-case runtime of $O^\*(2^{n/2 -
\varepsilon})$ for some constant $\varepsilon > 0$, the first such result to
strictly outperform classical methods on every instance.
We revisit fine-grained reductions that rely on the classical $2^{n/2}$
hardness of SubsetSum and show that these arguments hold only for
collision-free instances where $U$ is maximal. IC-SubsetSum reframes this
barrier structurally and introduces a new paradigm for certificate-sensitive
algorithms across NP-complete problems.

[Read original post](http://arxiv.org/abs/2507.15511v1)
