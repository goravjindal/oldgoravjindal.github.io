---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: On the Parallel Complexity of Finding a Matroid Basis"
date: 2025-07-14T00:00:00
---

**Authors:** [Sanjeev Khanna](https://dblp.uni-trier.de/search?q=Sanjeev+Khanna), [Aaron Putterman](https://dblp.uni-trier.de/search?q=Aaron+Putterman), [Junkai Song](https://dblp.uni-trier.de/search?q=Junkai+Song)

A fundamental question in parallel computation, posed by Karp, Upfal, and
Wigderson (FOCS 1985, JCSS 1988), asks: \emph{given only independence-oracle
access to a matroid on $n$ elements, how many rounds are required to find a
basis using only polynomially many queries?} This question generalizes, among
others, the complexity of finding bases of linear spaces, partition matroids,
and spanning forests in graphs. In their work, they established an upper bound
of $O(\sqrt{n})$ rounds and a lower bound of $\widetilde{\Omega}(n^{1/3})$
rounds for this problem, and these bounds have remained unimproved since then.
In this work, we make the first progress in narrowing this gap by designing a
parallel algorithm that finds a basis of an arbitrary matroid in
$\tilde{O}(n^{7/15})$ rounds (using polynomially many independence queries per
round) with high probability, surpassing the long-standing $O(\sqrt{n})$
barrier. Our approach introduces a novel matroid decomposition technique and
other structural insights that not only yield this general result but also lead
to a much improved new algorithm for the class of \emph{partition matroids}
(which underlies the $\widetilde\Omega(n^{1/3})$ lower bound of Karp, Upfal,
and Wigderson). Specifically, we develop an $\tilde{O}(n^{1/3})$-round
algorithm, thereby settling the round complexity of finding a basis in
partition matroids.

[Read original post](http://arxiv.org/abs/2507.08194v1)
