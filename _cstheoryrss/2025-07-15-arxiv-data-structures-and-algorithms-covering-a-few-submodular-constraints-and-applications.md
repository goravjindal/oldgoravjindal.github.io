---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Covering a Few Submodular Constraints and Applications"
date: 2025-07-15T00:00:00
---

**Authors:** [Tanvi Bajpai](https://dblp.uni-trier.de/search?q=Tanvi+Bajpai), [Chandra Chekuri](https://dblp.uni-trier.de/search?q=Chandra+Chekuri), [Pooja Kulkarni](https://dblp.uni-trier.de/search?q=Pooja+Kulkarni)

We consider the problem of covering multiple submodular constraints. Given a
finite ground set $N$, a cost function $c: N \rightarrow \mathbb{R}\_+$, $r$
monotone submodular functions $f\_1,f\_2,\ldots,f\_r$ over $N$ and requirements
$b\_1,b\_2,\ldots,b\_r$ the goal is to find a minimum cost subset $S \subseteq N$
such that $f\_i(S) \ge b\_i$ for $1 \le i \le r$. When $r=1$ this is the
well-known Submodular Set Cover problem. Previous work
\cite{chekuri2022covering} considered the setting when $r$ is large and
developed bi-criteria approximation algorithms, and approximation algorithms
for the important special case when each $f\_i$ is a weighted coverage function.
These are fairly general models and capture several concrete and interesting
problems as special cases. The approximation ratios for these problem are at
least $\Omega(\log r)$ which is unavoidable when $r$ is part of the input. In
this paper, motivated by some recent applications, we consider the problem when
$r$ is a \emph{fixed constant} and obtain two main results. For covering
multiple submodular constraints we obtain a randomized bi-criteria
approximation algorithm that for any given integer $\alpha \ge 1$ outputs a set
$S$ such that $f\_i(S) \ge$ $(1-1/e^\alpha -\epsilon)b\_i$ for each $i \in [r]$
and $\mathbb{E}[c(S)] \le (1+\epsilon)\alpha \cdot \sf{OPT}$. Second, when the
$f\_i$ are weighted coverage functions from a deletion-closed set system we
obtain a $(1+\epsilon)$ $(\frac{e}{e-1})$ $(1+\beta)$-approximation where
$\beta$ is the approximation ratio for the underlying set cover instances via
the natural LP. These results show that one can obtain nearly as good an
approximation for any fixed $r$ as what one would achieve for $r=1$. We mention
some applications that follow easily from these general results and anticipate
more in the future.

[Read original post](http://arxiv.org/abs/2507.09879v1)
