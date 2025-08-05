---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Near-Optimal Differentially Private Graph Algorithms via the"
date: 2025-08-05T00:00:00
---

**Authors:** [Laxman Dhulipala](https://dblp.uni-trier.de/search?q=Laxman+Dhulipala), [Monika Henzinger](https://dblp.uni-trier.de/search?q=Monika+Henzinger), [George Z. Li](https://dblp.uni-trier.de/search?q=George+Z.+Li), [Quanquan C. Liu](https://dblp.uni-trier.de/search?q=Quanquan+C.+Liu), [A. R. Sricharan](https://dblp.uni-trier.de/search?q=A.+R.+Sricharan), [Leqi Zhu](https://dblp.uni-trier.de/search?q=Leqi+Zhu)

Many differentially private and classical non-private graph algorithms rely
crucially on determining whether some property of each vertex meets a
threshold. For example, for the $k$-core decomposition problem, the classic
peeling algorithm iteratively removes a vertex if its induced degree falls
below a threshold. The sparse vector technique (SVT) is generally used to
transform non-private threshold queries into private ones with only a small
additive loss in accuracy. However, a naive application of SVT in the graph
setting leads to an amplification of the error by a factor of $n$ due to
composition, as SVT is applied to every vertex. In this paper, we resolve this
problem by formulating a novel generalized sparse vector technique which we
call the Multidimensional AboveThreshold (MAT) Mechanism which generalizes SVT
(applied to vectors with one dimension) to vectors with multiple dimensions. As
an application, we solve a number of important graph problems with better
bounds than previous work.
We apply our MAT mechanism to obtain a set of improved bounds for a variety
of problems including $k$-core decomposition, densest subgraph, low out-degree
ordering, and vertex coloring. We give a tight local edge DP algorithm for
$k$-core decomposition with $O(\epsilon^{-1}\log n)$ additive error and no
multiplicative error in $O(n)$ rounds. We also give a new $(2+\eta)$-factor
multiplicative, $O(\epsilon^{-1}\log n)$ additive error algorithm in $O(\log^2
n)$ rounds for any constant $\eta > 0$. Both of these results are
asymptotically tight against our new lower bound of $\Omega(\log n)$ for any
constant-factor approximation algorithm for $k$-core decomposition. Our new
algorithms for $k$-core also directly lead to new algorithms for densest
subgraph and low out-degree ordering. Our novel private defective coloring
algorithms uses number of colors proportional to the arboricity of the graph.

[Read original post](http://arxiv.org/abs/2508.02182v1)
