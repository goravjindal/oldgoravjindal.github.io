---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Does block size matter in randomized block Krylov low-rank"
date: 2025-08-11T00:00:00
---

**Authors:** [Tyler Chen](https://dblp.uni-trier.de/search?q=Tyler+Chen), [Ethan N. Epperly](https://dblp.uni-trier.de/search?q=Ethan+N.+Epperly), [Raphael A. Meyer](https://dblp.uni-trier.de/search?q=Raphael+A.+Meyer), [Christopher Musco](https://dblp.uni-trier.de/search?q=Christopher+Musco), [Akash Rao](https://dblp.uni-trier.de/search?q=Akash+Rao)

We study the problem of computing a rank-$k$ approximation of a matrix using
randomized block Krylov iteration. Prior work has shown that, for block size $b
= 1$ or $b = k$, a $(1 + \varepsilon)$-factor approximation to the best
rank-$k$ approximation can be obtained after $\tilde O(k/\sqrt{\varepsilon})$
matrix-vector products with the target matrix. On the other hand, when $b$ is
between $1$ and $k$, the best known bound on the number of matrix-vector
products scales with $b(k-b)$, which could be as large as $O(k^2)$.
Nevertheless, in practice, the performance of block Krylov methods is often
optimized by choosing a block size $1 \ll b \ll k$. We resolve this
theory-practice gap by proving that randomized block Krylov iteration produces
a $(1 + \varepsilon)$-factor approximate rank-$k$ approximation using $\tilde
O(k/\sqrt{\varepsilon})$ matrix-vector products for any block size $1\le b\le
k$. Our analysis relies on new bounds for the minimum singular value of a
random block Krylov matrix, which may be of independent interest. Similar
bounds are central to recent breakthroughs on faster algorithms for sparse
linear systems [Peng & Vempala, SODA 2021; Nie, STOC 2022].

[Read original post](http://arxiv.org/abs/2508.06486v1)
