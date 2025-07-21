---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Faster Multi-Source Reachability and Approximate Distances via"
date: 2025-07-21T00:00:00
---

**Authors:** [Michael Elkin](https://dblp.uni-trier.de/search?q=Michael+Elkin), [Chhaya Trehan](https://dblp.uni-trier.de/search?q=Chhaya+Trehan)

Given an $n$-vertex $m$-edge digraph $G = (V,E)$ and a subset $S \subseteq V$
of $|S| = n^{\sigma}$ (for some $0 \le \sigma \le 1$) designated sources, the
$S \times V$ reachability problem is to compute the sets $\mathcal V\_s$ of
vertices reachable from $s$, for every $s \in S$. Naive centralized algorithms
run BFS/DFS from each source in $O(m \cdot n^{\sigma})$ time or compute $G$'s
transitive closure in $\hat O(n^{\omega})$ time, where $\omega \le
2.371552\ldots$ is the matrix multiplication exponent. Thus, the best known
bound is $\hat O(n^{\min \{ 2 + \sigma, \omega\}})$. Leveraging shortcut
constructions by Kogan and Parter [SODA 2022, ICALP 2022], we develop a
centralized algorithm with running time $\hat O(n^{1 + \frac{2}{3}
\omega(\sigma)})$, where $\omega(\sigma)$ is the rectangular matrix
multiplication exponent. Using current estimates on $\omega(\sigma)$, our
exponent improves upon $\min \{2 + \sigma, \omega \}$ for $\tilde \sigma \leq
\sigma \leq 0.53$, where $1/3 < \tilde \sigma < 0.3336$ is a universal
constant.
In a classical result, Cohen [Journal of Algorithms, 1996] devised parallel
algorithms for $S \times V$ reachability on graphs admitting balanced recursive
separators of size $n^{\rho}$ for $\rho < 1$, requiring polylogarithmic time
and work $n^{\max \{\omega \rho, 2\rho + \sigma \} + o(1)}$. We significantly
improve, extend, and generalize Cohen's result. First, our parallel algorithm
for graphs with small recursive separators has lower work complexity than
Cohen's in boraod paramater ranges. Second, we generalize our algorithm to
graphs of treewidth at most $n^{\rho}$ ($\rho < 1$) and provide a centralized
algorithm that outperforms existing bounds for $S \times V$ reachability on
such graphs. We also do this for some other graph familes with small
separators. Finally, we extend these results to $(1 + \epsilon)$-approximate
distance computation.

[Read original post](http://arxiv.org/abs/2507.13470v1)
