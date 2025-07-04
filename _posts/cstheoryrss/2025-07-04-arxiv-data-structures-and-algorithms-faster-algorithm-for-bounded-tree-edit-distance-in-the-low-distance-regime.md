---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Faster Algorithm for Bounded Tree Edit Distance in the Low-Distance
  Regime"
date: 2025-07-04T00:00:00
---

**Authors:** [Tomasz Kociumaka](https://dblp.uni-trier.de/search?q=Tomasz+Kociumaka), [Ali Shahali](https://dblp.uni-trier.de/search?q=Ali+Shahali)

The tree edit distance is a natural dissimilarity measure between rooted
ordered trees whose nodes are labeled over an alphabet $\Sigma$. It is defined
as the minimum number of node edits (insertions, deletions, and relabelings)
required to transform one tree into the other. In the weighted variant, the
edits have associated costs (depending on the involved node labels) normalized
so that each cost is at least one, and the goal is to minimize the total cost
of edits.
The unweighted tree edit distance between two trees of total size $n$ can be
computed in $O(n^{2.6857})$ time; in contrast, determining the weighted tree
edit distance is fine-grained equivalent to the All-Pairs Shortest Paths
problem and requires $n^3/2^{\Omega(\sqrt{\log n})}$ time [Nogler et al.;
STOC'25]. These super-quadratic running times are unattractive for large but
very similar trees, which motivates the bounded version of the problem, where
the runtime is parameterized by the computed distance $k$, potentially yielding
faster algorithms for $k\ll n$.
Previous best algorithms for the bounded unweighted setting run in
$O(nk^2\log n)$ time [Akmal & Jin; ICALP'21] and $O(n + k^7\log k)$ time [Das
et al.; STOC'23]. For the weighted variant, the only known running time has
been $O(n + k^{15})$.
We present an $O(n + k^6\log k)$-time algorithm for computing the bounded
tree edit distance in both the weighted and unweighted settings. Our approach
begins with an alternative $O(nk^2\log n)$-time algorithm that handles weights
and is significantly easier to analyze than the existing counterpart. We then
introduce a novel optimization that leverages periodic structures within the
input trees. To utilize it, we modify the $O(k^5)$-size $O(n)$-time universal
kernel, the central component of the prior $O(n + k^{O(1)})$-time algorithms,
so that it produces instances containing these periodic structures.