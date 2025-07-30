---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Online Edge Coloring: Sharp Thresholds"
date: 2025-07-30T00:00:00
---

**Authors:** [Joakim Blikstad](https://dblp.uni-trier.de/search?q=Joakim+Blikstad), [Ola Svensson](https://dblp.uni-trier.de/search?q=Ola+Svensson), [Radu Vintan](https://dblp.uni-trier.de/search?q=Radu+Vintan), [David Wajc](https://dblp.uni-trier.de/search?q=David+Wajc)

Vizing's theorem guarantees that every graph with maximum degree $\Delta$
admits an edge coloring using $\Delta + 1$ colors. In online settings - where
edges arrive one at a time and must be colored immediately - a simple greedy
algorithm uses at most $2\Delta - 1$ colors. Over thirty years ago, Bar-Noy,
Motwani, and Naor [IPL'92] proved that this guarantee is optimal among
deterministic algorithms when $\Delta = O(\log n)$, and among randomized
algorithms when $\Delta = O(\sqrt{\log n})$. While deterministic improvements
seemed out of reach, they conjectured that for graphs with $\Delta =
\omega(\log n)$, randomized algorithms can achieve $(1 + o(1))\Delta$ edge
coloring. This conjecture was recently resolved in the affirmative: a $(1 +
o(1))\Delta$-coloring is achievable online using randomization for all graphs
with $\Delta = \omega(\log n)$ [BSVW STOC'24].
Our results go further, uncovering two findings not predicted by the original
conjecture. First, we give a deterministic online algorithm achieving $(1 +
o(1))\Delta$-colorings for all $\Delta = \omega(\log n)$. Second, we give a
randomized algorithm achieving $(1 + o(1))\Delta$-colorings already when
$\Delta = \omega(\sqrt{\log n})$. Our results establish sharp thresholds for
when greedy can be surpassed, and near-optimal guarantees can be achieved -
matching the impossibility results of [BNMN IPL'92], both deterministically and
randomly.

[Read original post](http://arxiv.org/abs/2507.21560v1)
