---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: To buy or not to buy: deterministic rent-or-buy problems on"
date: 2025-07-14T00:00:00
---

**Authors:** [Sander Borst](https://dblp.uni-trier.de/search?q=Sander+Borst), [Moritz Venzin](https://dblp.uni-trier.de/search?q=Moritz+Venzin)

We study the rent-or-buy variant of the online Steiner forest problem on
node- and edge-weighted graphs. For $n$-node graphs with at most $\bar{n}$
non-zero node-weights, and at most $\tilde{k}$ different arriving terminal
pairs, we obtain a deterministic, $O(\log n \log \bar{n})$-competitive
algorithm. This improves on the previous best, $O(\log^4 n)$-competitive
algorithm obtained by the black-box reduction from (Bartal et al. 2021)
combined with the previously best deterministic algorithms for the simpler
'buy-only' setting. We also obtain a deterministic, $O(\bar{n}\log
\tilde{k})$-competitive algorithm. This generalizes the $O(\log
\tilde{k})$-competitive algorithm for the purely edge-weighted setting from
(Umboh 2015). We also obtain a randomized, $O(\log \tilde{k} \log
\bar{n})$-competitive algorithm. All previous approaches were based on the
randomized, black-box reduction from~\cite{AwerbuchAzarBartal96} that achieves
a $O(\log \tilde{k} \log n)$-competitive ratio when combined with an algorithm
for the 'buy-only' setting. Our key technical ingredient is a novel charging
scheme to an instance of \emph{online prize-collecting set cover}. This allows
us to extend the witness-technique of (Umboh 2015) to the node-weighted setting
and obtain refined guarantees with respect to $\bar{n}$, already in the much
simpler 'buy-only' setting.

[Read original post](http://arxiv.org/abs/2507.08698v1)
