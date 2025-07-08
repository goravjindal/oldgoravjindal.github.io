---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Heights of butterfly trees"
date: 2025-07-08T00:00:00
---

**Authors:** [John Peca-Medlin](https://dblp.uni-trier.de/search?q=John+Peca-Medlin), [Chenyang Zhong](https://dblp.uni-trier.de/search?q=Chenyang+Zhong)

Binary search trees (BSTs) are fundamental data structures whose performance
is largely governed by tree height. We introduce a block model for constructing
BSTs by embedding internal BSTs into the nodes of an external BST -- a
structure motivated by parallel data architectures -- corresponding to
composite permutations formed via Kronecker or wreath products. Extending
Devroye's result that the height $h\_n$ of a random BST satisfies $h\_n / \log n
\to c^\* \approx 4.311$, we show that block BSTs with $nm$ nodes and fixed
external size $m$ satisfy $h\_{n,m} / \log n \to c^\* + h\_m$ in distribution. We
then analyze height growth under iterated products. For simple butterfly trees
(from iterated Kronecker products of $S\_2$), we give a full distributional
description showing polynomial height growth: $\mathbb{E}
h\_n^{\operatorname{B}} = \Theta(N^\alpha)$ with $\alpha \approx 0.58496$. For
nonsimple butterfly trees (from wreath products), we prove power-law bounds:
$cN^\alpha\cdot (1 + o(1)) \le \mathbb{E} h\_n^{\operatorname{B}} \le
dN^\beta\cdot (1 + o(1))$, with $\beta \approx 0.913189$.

[Read original post](http://arxiv.org/abs/2507.04505v1)
