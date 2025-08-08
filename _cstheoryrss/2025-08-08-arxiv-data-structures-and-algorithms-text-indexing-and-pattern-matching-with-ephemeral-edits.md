---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Text Indexing and Pattern Matching with Ephemeral Edits"
date: 2025-08-08T00:00:00
---

**Authors:** [Solon P. Pissis](https://dblp.uni-trier.de/search?q=Solon+P.+Pissis)

A sequence $e\_0,e\_1,\ldots$ of edit operations in a string $T$ is called
ephemeral if operation $e\_i$ constructing string $T^i$, for all $i=2k$ with
$k\in\mathbb{N}$, is reverted by operation $e\_{i+1}$ that reconstructs $T$.
Such a sequence arises when processing a stream of independent edits or testing
hypothetical edits.
We introduce text indexing with ephemeral substring edits, a new version of
text indexing. Our goal is to design a data structure over a given text that
supports subsequent pattern matching queries with ephemeral substring
insertions, deletions, or substitutions in the text; we require insertions and
substitutions to be of constant length. In particular, we preprocess a text
$T=T[0\mathinner{.\,.} n)$ over an integer alphabet $\Sigma=[0,\sigma)$ with
$\sigma=n^{\mathcal{O}(1)}$ in $\mathcal{O}(n)$ time. Then, we can preprocess
any arbitrary pattern $P=P[0\mathinner{.\,.} m)$ given online in
$\mathcal{O}(m\log\log m)$ time and $\mathcal{O}(m)$ space and allow any
ephemeral sequence of edit operations in $T$. Before reverting the $i$th
operation, we report all Occ occurrences of $P$ in $T^i$ in
$\mathcal{O}(\log\log n + \text{Occ})$ time.
We also introduce pattern matching with ephemeral edits. In particular, we
preprocess two strings $T$ and $P$, each of length at most $n$, over an integer
alphabet $\Sigma=[0,\sigma)$ with $\sigma=n^{\mathcal{O}(1)}$ in
$\mathcal{O}(n)$ time. Then, we allow any ephemeral sequence of edit operations
in $T$. Before reverting the $i$th operation, we report all Occ occurrences of
$P$ in $T^i$ in the optimal $\mathcal{O}(\text{Occ})$ time. Along our way to
this result, we also give an optimal solution for pattern matching with
ephemeral block deletions.

[Read original post](http://arxiv.org/abs/2508.05124v1)
