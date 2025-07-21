---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Improved girth approximation in weighted undirected graphs"
date: 2025-07-21T00:00:00
---

**Authors:** [Avi Kadria](https://dblp.uni-trier.de/search?q=Avi+Kadria), [Liam Roditty](https://dblp.uni-trier.de/search?q=Liam+Roditty), [Aaron Sidford](https://dblp.uni-trier.de/search?q=Aaron+Sidford), [Virginia Vassilevska Williams](https://dblp.uni-trier.de/search?q=Virginia+Vassilevska+Williams), [Uri Zwick](https://dblp.uni-trier.de/search?q=Uri+Zwick)

Let $G = (V,E,\ell)$ be a $n$-node $m$-edge weighted undirected graph, where
$\ell: E \rightarrow (0,\infty)$ is a real \emph{length} function defined on
its edges, and let $g$ denote the girth of $G$, i.e., the length of its
shortest cycle. We present an algorithm that, for any input, integer $k \geq
1$, in $O(kn^{1+1/k}\log{n} + m(k+\log{n}))$ expected time finds a cycle of
length at most $\frac{4k}{3}g$. This algorithm nearly matches a
$O(n^{1+1/k}\log{n})$-time algorithm of \cite{KadriaRSWZ22} which applied to
unweighted graphs of girth $3$. For weighted graphs, this result also improves
upon the previous state-of-the-art algorithm that in $O((n^{1+1/k}\log n+m)\log
(nM))$ time, where $\ell: E \rightarrow [1, M]$ is an integral length function,
finds a cycle of length at most $2kg$~\cite{KadriaRSWZ22}. For $k=1$ this
result improves upon the result of Roditty and Tov~\cite{RodittyT13}.

[Read original post](http://arxiv.org/abs/2507.13869v1)
