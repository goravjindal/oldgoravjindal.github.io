---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Prediction-Augmented Mechanism Design for Weighted Facility Location"
date: 2025-07-10T00:00:00
---

**Authors:** [Yangguang Shi](https://dblp.uni-trier.de/search?q=Yangguang+Shi), [Zhenyu Xue](https://dblp.uni-trier.de/search?q=Zhenyu+Xue)

Facility location is fundamental in operations research, mechanism design,
and algorithmic game theory, with applications ranging from urban
infrastructure planning to distributed systems. Recent research in this area
has focused on augmenting classic strategyproof mechanisms with predictions to
achieve an improved performance guarantee against the uncertainty under the
strategic environment. Previous work has been devoted to address the trade-off
obstacle of balancing the consistency (near-optimality under accurate
predictions) and robustness (bounded inefficiency under poor predictions)
primarily in the unweighted setting, assuming that all agents have the same
importance. However, this assumption may not be true in some practical
scenarios, leading to research of weighted facility location problems.
The major contribution of the current work is to provide a prediction
augmented algorithmic framework for balancing the consistency and robustness
over strategic agents with non-uniform weights. In particular, through a
reduction technique that identifies a subset of \emph{representative} instances
and maps the other given locations to the representative ones, we prove that
there exists a \emph{strategyproof} mechanism achieving a bounded consistency
guarantee of $\frac{\sqrt{(1+c)^2W^2\_{\min}+(1-c)^2W^2\_{\max}}}{(1+c)W\_{\min}}$
and a bounded robustness guarantee of
$\frac{\sqrt{(1-c)^2W^2\_{\min}+(1+c)^2W^2\_{\max}}}{(1-c)W\_{\min}}$ in weighted
settings, where $c$ can be viewed as a parameter to make a trade-off between
the consistency and robustness and $W\_{\min}$ and $W\_{\max}$ denote the minimum
and maximum agents' weight. We also proved that there is no strategyproof
deterministic mechanism that reach $1$-consistency and $O\left( n \cdot
\frac{W\_{\max}}{W\_{\min}} \right)$-robustness in weighted FLP, even with fully
predictions of all agents.

[Read original post](http://arxiv.org/abs/2507.06509v1)
