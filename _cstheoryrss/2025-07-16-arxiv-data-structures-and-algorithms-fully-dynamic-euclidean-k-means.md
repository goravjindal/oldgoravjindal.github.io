---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Fully Dynamic Euclidean k-Means"
date: 2025-07-16T00:00:00
---

**Authors:** [Sayan Bhattacharya](https://dblp.uni-trier.de/search?q=Sayan+Bhattacharya), [Martín Costa](https://dblp.uni-trier.de/search?q=Mart%C3%ADn+Costa), [Ermiya Farokhnejad](https://dblp.uni-trier.de/search?q=Ermiya+Farokhnejad), [Shaofeng H. -C. Jiang](https://dblp.uni-trier.de/search?q=Shaofeng+H.+-C.+Jiang), [Yaonan Jin](https://dblp.uni-trier.de/search?q=Yaonan+Jin), [Jianing Lou](https://dblp.uni-trier.de/search?q=Jianing+Lou)

We consider the fundamental Euclidean $k$-means clustering problem in a
dynamic setting, where the input $X \subseteq \mathbb{R}^d$ evolves over time
via a sequence of point insertions/deletions. We have to explicitly maintain a
solution (a set of $k$ centers) $S \subseteq \mathbb{R}^d$ throughout these
updates, while minimizing the approximation ratio, the update time (time taken
to handle a point insertion/deletion) and the recourse (number of changes made
to the solution $S$) of the algorithm.
We present a dynamic algorithm for this problem with
$\text{poly}(1/\epsilon)$-approximation ratio, $\tilde{O}(k^{\epsilon})$ update
time and $\tilde{O}(1)$ recourse. In the general regime, where the dimension
$d$ cannot be assumed to be a fixed constant, our algorithm has almost optimal
guarantees across all these three parameters. Indeed, improving our update time
or approximation ratio would imply beating the state-of-the-art static
algorithm for this problem (which is widely believed to be the best possible),
and the recourse of any dynamic algorithm must be $\Omega(1)$.
We obtain our result by building on top of the recent work of [Bhattacharya,
Costa, Farokhnejad; STOC'25], which gave a near-optimal dynamic algorithm for
$k$-means in general metric spaces (as opposed to in the Euclidean setting).
Along the way, we design several novel geometric data structures that are of
independent interest. Specifically, one of our main contributions is designing
the first consistent hashing scheme [Czumaj, Jiang, Krauthgamer, Vesel\'y,
Yang; FOCS'22] that achieves $\text{poly}(d)$ running time per point evaluation
with competitive parameters.

[Read original post](http://arxiv.org/abs/2507.11256v1)
