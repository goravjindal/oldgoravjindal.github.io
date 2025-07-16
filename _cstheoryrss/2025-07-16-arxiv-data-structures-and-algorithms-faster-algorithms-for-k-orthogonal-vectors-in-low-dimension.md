---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Faster algorithms for k-Orthogonal Vectors in low dimension"
date: 2025-07-16T00:00:00
---

**Authors:** [Anita Dürr](https://dblp.uni-trier.de/search?q=Anita+D%C3%BCrr), [Evangelos Kipouridis](https://dblp.uni-trier.de/search?q=Evangelos+Kipouridis), [Karol Węgrzycki](https://dblp.uni-trier.de/search?q=Karol+W%C4%99grzycki)

In the Orthogonal Vectors problem (OV), we are given two families $A, B$ of
subsets of $\{1,\ldots,d\}$, each of size $n$, and the task is to decide
whether there exists a pair $a \in A$ and $b \in B$ such that $a \cap b =
\emptyset$. Straightforward algorithms for this problem run in $\mathcal{O}(n^2
\cdot d)$ or $\mathcal{O}(2^d \cdot n)$ time, and assuming SETH, there is no
$2^{o(d)}\cdot n^{2-\varepsilon}$ time algorithm that solves this problem for
any constant $\varepsilon > 0$.
Williams (FOCS 2024) presented a $\tilde{\mathcal{O}}(1.35^d \cdot n)$-time
algorithm for the problem, based on the succinct equality-rank decomposition of
the disjointness matrix. In this paper, we present a combinatorial algorithm
that runs in randomized time $\tilde{\mathcal{O}}(1.25^d n)$. This can be
improved to $\mathcal{O}(1.16^d \cdot n)$ using computer-aided evaluations.
We generalize our result to the $k$-Orthogonal Vectors problem, where given
$k$ families $A\_1,\ldots,A\_k$ of subsets of $\{1,\ldots,d\}$, each of size $n$,
the task is to find elements $a\_i \in A\_i$ for every $i \in \{1,\ldots,k\}$
such that $a\_1 \cap a\_2 \cap \ldots \cap a\_k = \emptyset$. We show that for
every fixed $k \ge 2$, there exists $\varepsilon\_k > 0$ such that the $k$-OV
problem can be solved in time $\mathcal{O}(2^{(1 - \varepsilon\_k)\cdot d}\cdot
n)$. We also show that, asymptotically, this is the best we can hope for: for
any $\varepsilon > 0$ there exists a $k \ge 2$ such that $2^{(1 -
\varepsilon)\cdot d} \cdot n^{\mathcal{O}(1)}$ time algorithm for
$k$-Orthogonal Vectors would contradict the Set Cover Conjecture.

[Read original post](http://arxiv.org/abs/2507.11098v1)
