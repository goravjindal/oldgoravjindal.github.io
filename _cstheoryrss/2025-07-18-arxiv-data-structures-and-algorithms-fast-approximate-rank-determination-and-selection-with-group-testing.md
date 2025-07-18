---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Fast Approximate Rank Determination and Selection with Group Testing"
date: 2025-07-18T00:00:00
---

**Authors:** [Adiesha Liyanage](https://dblp.uni-trier.de/search?q=Adiesha+Liyanage), [Braeden Sopp](https://dblp.uni-trier.de/search?q=Braeden+Sopp), [Brendan Mumey](https://dblp.uni-trier.de/search?q=Brendan+Mumey)

Suppose that a group test operation is available for checking order relations
in a set, can this speed up problems like finding the minimum/maximum element,
rank determination and selection? We consider a one-sided group test to be
available, where queries are of the form $u \le\_Q V$ or $V \le\_Q u$, and the
answer is `yes' if and only if there is some $v \in V$ such that $u \le v$ or
$v \le u$, respectively. We restrict attention to total orders and focus on
query-complexity; for min or max finding, we give a Las Vegas algorithm that
makes $\mathcal{O}(\log^2 n)$ expected queries. We also give randomized
approximate algorithms for rank determination and selection; we allow a
relative error of $1 \pm \delta$ for $\delta > 0$ in the estimated rank or
selected element. In this case, we give a Monte Carlo algorithm for approximate
rank determination with expected query complexity
$\tilde{\mathcal{O}}(1/\delta^2 - \log \epsilon)$, where $1-\epsilon$ is the
probability that the algorithm succeeds. We also give a Monte Carlo algorithm
for approximate selection that has expected query complexity
$\tilde{\mathcal{O}}(-\log( \epsilon \delta^2) / \delta^4)$; it has probability
at least $\frac{1}{2}$ to output an element $x$, and if so, $x$ has the desired
approximate rank with probability $1-\epsilon$.

[Read original post](http://arxiv.org/abs/2507.12634v1)
