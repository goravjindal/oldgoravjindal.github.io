---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Liar's vertex-edge domination in subclasses of chordal graphs"
date: 2025-07-08T00:00:00
---

**Authors:** [Debojyoti Bhattacharya](https://dblp.uni-trier.de/search?q=Debojyoti+Bhattacharya), [Subhabrata Paul](https://dblp.uni-trier.de/search?q=Subhabrata+Paul)

Let $G=(V, E)$ be an undirected graph. The set $N\_G[x]=\{y\in V|xy\in E\}\cup
\{x\}$ is called the closed neighbourhood of a vertex $x\in V$ and for an edge
$e=xy\in E$, the closed neighbourhood of $e$ is the set $N\_G[x]\cup N\_G[y]$,
which is denoted by $N\_G[e]$ or $N\_G[xy]$. A set $L\subseteq V$ is called
\emph{liar's vertex-edge dominating set} of a graph $G=(V,E)$ if for every
$e\_i\in E$, $|N\_G[e\_i]\cap L|\geq 2$ and for every pair of distinct edges
$e\_i,e\_j\in E$, $|(N\_G[e\_i]\cup N\_G[e\_j])\cap L|\geq 3$. The notion of liar's
vertex-edge domination arises naturally from some applications in communication
networks. Given a graph $G$, the \textsc{Minimum Liar's Vertex-Edge Domination
Problem} (\textsc{MinLVEDP}) asks to find a liar's vertex-edge dominating set
of $G$ of minimum cardinality. In this paper, we study this problem from an
algorithmic point of view. We design two linear time algorithms for
\textsc{MinLVEDP} in block graphs and proper interval graphs, respectively. On
the negative side, we show that the decision version of liar's vertex-edge
domination problem is NP-complete for undirected path graphs.

[Read original post](http://arxiv.org/abs/2507.04721v1)
