---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: Complexity of learning matchings and half graphs via edge queries"
date: 2025-07-07T00:00:00
---

**Authors:** [Nikhil S. Mande](https://dblp.uni-trier.de/search?q=Nikhil+S.+Mande), [Swagato Sanyal](https://dblp.uni-trier.de/search?q=Swagato+Sanyal), [Viktor Zamaraev](https://dblp.uni-trier.de/search?q=Viktor+Zamaraev)

The problem of learning or reconstructing an unknown graph from a known
family via partial-information queries arises as a mathematical model in
various contexts. The most basic type of access to the graph is via \emph{edge
queries}, where an algorithm may query the presence/absence of an edge between
a pair of vertices of its choosing, at unit cost.
While more powerful query models have been extensively studied in the context
of graph reconstruction, the basic model of edge queries seems to have not
attracted as much attention. In this paper we study the edge query complexity
of learning a hidden bipartite graph, or equivalently its bipartite adjacency
matrix, in the classical as well as quantum settings. We focus on learning
matchings and half graphs, which are graphs whose bipartite adjacency matrices
are a row/column permutation of the identity matrix and the lower triangular
matrix with all entries on and below the principal diagonal being 1,
respectively.
\begin{itemize}
\item For matchings of size $n$, we show a tight deterministic bound of
$n(n-1)/2$ and an asymptotically tight randomized bound of $\Theta(n^2)$. A
quantum bound of $\Theta(n^{1.5})$ was shown in a recent work of van Apeldoorn
et al.~[ICALP'21].
\item For half graphs whose bipartite adjacency matrix is a
column-permutation of the $n \times n$ lower triangular matrix,
we give tight $\Theta(n \log n)$ bounds in both deterministic and randomized
settings, and an $\Omega(n)$ quantum lower bound. \item For general half
graphs,
we observe that the problem is equivalent to a natural generalization of the
famous nuts-and-bolts problem, leading to a tight $\Theta(n \log n)$ randomized
bound.
We also present a simple quicksort-style method that instantiates to a $O(n
\log^2 n)$ randomized algorithm and a tight $O(n \log n)$ quantum algorithm.
\end{itemize}

[Read original post](http://arxiv.org/abs/2507.03151v1)
