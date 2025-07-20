---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Color Distance Oracles and Snippets: Separation Between Exact and"
date: 2025-07-08T00:00:00
---

**Authors:** [Noam Horowicz](https://dblp.uni-trier.de/search?q=Noam+Horowicz), [Tsvi Kopelowitz](https://dblp.uni-trier.de/search?q=Tsvi+Kopelowitz)

In the snippets problem, the goal is to preprocess text $T$ so that given two
patterns $P\_1$ and $P\_2$, one can locate the occurrences of the two patterns in
$T$ that are closest to each other, or report their distance. Kopelowitz and
Krauthgamer [CPM2016] showed upper bound tradeoffs and conditional lower bounds
tradeoffs for the snippets problem, by utilizing connections between the
snippets problem and the problem of constructing a color distance oracle (CDO),
which is a data structure that preprocess a set of points with associated
colors so that given two colors $c$ and $c'$ one can quickly find the (distance
between the) closest pair of points with colors $c$ and $c'$. However, the
existing upper bound and lower bound curves are not tight.
Inspired by recent advances by Kopelowitz and Vassilevska-Williams
[ICALP2020] regarding Set-disjointness data structures, we introduce new
conditionally optimal algorithms for $(1+\varepsilon)$ approximation versions
of the snippets problem and the CDO problem, by applying fast matrix
multiplication. For example, for CDO on $n$ points in an array with
preprocessing time $\tilde{O}(n^a)$ and query time $\tilde{O}(n^b)$, assuming
that $\omega=2$ (where $\omega$ is the exponent of $n$ in the runtime of the
fastest matrix multiplication algorithm on two squared matrices of size
$n\times n$), we show that approximate CDO can be solved with the following
tradeoff
$$ a + 2b = 2 \text{ if } 0 \leq b \leq \frac1 3$$ $$ 2a + b = 3 \text{ if }
\frac13\leq b \leq 1.$$
Moreover, we prove that for exact CDO on points in an array, the algorithm of
Kopelowitz and Krauthgamer [CPM2016], is essentially optimal assuming that the
strong APSP hypothesis holds for randomized algorithms. Thus, the exact version
of CDO is strictly harder than the approximate version.

[Read original post](http://arxiv.org/abs/2507.04578v1)
