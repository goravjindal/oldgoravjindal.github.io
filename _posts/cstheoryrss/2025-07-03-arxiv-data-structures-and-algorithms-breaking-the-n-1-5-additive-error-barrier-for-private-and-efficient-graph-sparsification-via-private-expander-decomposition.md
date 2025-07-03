---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Breaking the $n^{1.5}$ Additive Error Barrier for Private and Efficient
  Graph Sparsification via Private Expander Decomposition"
date: 2025-07-03T00:00:00
---

**Authors:** [Anders Aamand](https://dblp.uni-trier.de/search?q=Anders+Aamand), [Justin Y. Chen](https://dblp.uni-trier.de/search?q=Justin+Y.+Chen), [Mina Dalirrooyfard](https://dblp.uni-trier.de/search?q=Mina+Dalirrooyfard), [Slobodan Mitrović](https://dblp.uni-trier.de/search?q=Slobodan+Mitrovi%C4%87), [Yuriy Nevmyvaka](https://dblp.uni-trier.de/search?q=Yuriy+Nevmyvaka), [Sandeep Silwal](https://dblp.uni-trier.de/search?q=Sandeep+Silwal), [Yinzhan Xu](https://dblp.uni-trier.de/search?q=Yinzhan+Xu)

We study differentially private algorithms for graph cut sparsification, a
fundamental problem in algorithms, privacy, and machine learning. While
significant progress has been made, the best-known private and efficient cut
sparsifiers on $n$-node graphs approximate each cut within
$\widetilde{O}(n^{1.5})$ additive error and $1+\gamma$ multiplicative error for
any $\gamma > 0$ [Gupta, Roth, Ullman TCC'12]. In contrast, "inefficient"
algorithms, i.e., those requiring exponential time, can achieve an
$\widetilde{O}(n)$ additive error and $1+\gamma$ multiplicative error
[Eli{\'a}{\v{s}}, Kapralov, Kulkarni, Lee SODA'20]. In this work, we break the
$n^{1.5}$ additive error barrier for private and efficient cut sparsification.
We present an $(\varepsilon,\delta)$-DP polynomial time algorithm that, given a
non-negative weighted graph, outputs a private synthetic graph approximating
all cuts with multiplicative error $1+\gamma$ and additive error $n^{1.25 +
o(1)}$ (ignoring dependencies on $\varepsilon, \delta, \gamma$).
At the heart of our approach lies a private algorithm for expander
decomposition, a popular and powerful technique in (non-private) graph
algorithms.