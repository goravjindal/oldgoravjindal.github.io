---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Bounded Weighted Edit Distance: Dynamic Algorithms and Matching Lower
  Bounds"
date: 2025-07-04T00:00:00
---

**Authors:** [Itai Boneh](https://dblp.uni-trier.de/search?q=Itai+Boneh), [Egor Gorbachev](https://dblp.uni-trier.de/search?q=Egor+Gorbachev), [Tomasz Kociumaka](https://dblp.uni-trier.de/search?q=Tomasz+Kociumaka)

The edit distance $ed(X,Y)$ of two strings $X,Y\in \Sigma^\*$ is the minimum
number of character edits (insertions, deletions, and substitutions) needed to
transform $X$ into $Y$. Its weighted counterpart $ed^w(X,Y)$ minimizes the
total cost of edits, which are specified using a function $w$, normalized so
that each edit costs at least one. The textbook dynamic-programming procedure,
given strings $X,Y\in \Sigma^{\le n}$ and oracle access to $w$, computes
$ed^w(X,Y)$ in $O(n^2)$ time. Nevertheless, one can achieve better running
times if the computed distance, denoted $k$, is small: $O(n+k^2)$ for unit
weights [Landau and Vishkin; JCSS'88] and $\tilde{O}(n+\sqrt{nk^3})$ for
arbitrary weights [Cassis, Kociumaka, Wellnitz; FOCS'23].
In this paper, we study the dynamic version of the weighted edit distance
problem, where the goal is to maintain $ed^w(X,Y)$ for strings $X,Y\in
\Sigma^{\le n}$ that change over time, with each update specified as an edit in
$X$ or $Y$. Very recently, Gorbachev and Kociumaka [STOC'25] showed that the
unweighted distance $ed(X,Y)$ can be maintained in $\tilde{O}(k)$ time per
update after $\tilde{O}(n+k^2)$-time preprocessing; here, $k$ denotes the
current value of $ed(X,Y)$. Their algorithm generalizes to small integer
weights, but the underlying approach is incompatible with large weights.
Our main result is a dynamic algorithm that maintains $ed^w(X,Y)$ in
$\tilde{O}(k^{3-\gamma})$ time per update after $\tilde{O}(nk^\gamma)$-time
preprocessing. Here, $\gamma\in [0,1]$ is a real trade-off parameter and $k\ge
1$ is an integer threshold fixed at preprocessing time, with $\infty$ returned
whenever $ed^w(X,Y)>k$. We complement our algorithm with conditional lower
bounds showing fine-grained optimality of our trade-off for $\gamma \in
[0.5,1)$ and justifying our choice to fix $k$.

[Read original post](http://arxiv.org/abs/2507.02548v1)
