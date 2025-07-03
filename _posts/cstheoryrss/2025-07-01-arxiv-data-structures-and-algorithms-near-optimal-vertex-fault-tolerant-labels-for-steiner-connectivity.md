---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Near-Optimal Vertex Fault-Tolerant Labels for Steiner Connectivity"
date: 2025-07-01T00:00:00
---

**Authors:** [Koustav Bhanja](https://dblp.uni-trier.de/search?q=Koustav+Bhanja), [Asaf Petruschka](https://dblp.uni-trier.de/search?q=Asaf+Petruschka)

We present a compact labeling scheme for determining whether a designated set
of terminals in a graph remains connected after any $f$ (or less) vertex
failures occur. An $f$-FT Steiner connectivity labeling scheme for an
$n$-vertex graph $G=(V,E)$ with terminal set $U \subseteq V$ provides labels to
the vertices of $G$, such that given only the labels of any subset $F \subseteq
V$ with $|F| \leq f$, one can determine if $U$ remains connected in $G-F$. The
main complexity measure is the maximum label length.
The special case $U=V$ of global connectivity has been recently studied by
Jiang, Parter, and Petruschka, who provided labels of $n^{1-1/f} \cdot
\mathrm{poly}(f,\log n)$ bits. This is near-optimal (up to
$\mathrm{poly}(f,\log n)$ factors) by a lower bound of Long, Pettie and
Saranurak. Our scheme achieves labels of $|U|^{1-1/f} \cdot \mathrm{poly}(f,
\log n)$ for general $U \subseteq V$, which is near-optimal for any given size
$|U|$ of the terminal set. To handle terminal sets, our approach differs from
Jiang et al. We use a well-structured Steiner tree for $U$ produced by a
decomposition theorem of Duan and Pettie, and bypass the need for
Nagamochi-Ibaraki sparsification.