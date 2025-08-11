---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Near-Optimal Regret for Efficient Stochastic Combinatorial Semi-Bandits"
date: 2025-08-11T00:00:00
---

**Authors:** [Zichun Ye](https://dblp.uni-trier.de/search?q=Zichun+Ye), [Runqi Wang](https://dblp.uni-trier.de/search?q=Runqi+Wang), [Xutong Liu](https://dblp.uni-trier.de/search?q=Xutong+Liu), [Shuai Li](https://dblp.uni-trier.de/search?q=Shuai+Li)

The combinatorial multi-armed bandit (CMAB) is a cornerstone of sequential
decision-making framework, dominated by two algorithmic families: UCB-based and
adversarial methods such as follow the regularized leader (FTRL) and online
mirror descent (OMD). However, prominent UCB-based approaches like CUCB suffer
from additional regret factor $\log T$ that is detrimental over long horizons,
while adversarial methods such as EXP3.M and HYBRID impose significant
computational overhead. To resolve this trade-off, we introduce the
Combinatorial Minimax Optimal Strategy in the Stochastic setting (CMOSS). CMOSS
is a computationally efficient algorithm that achieves an instance-independent
regret of $O\big( (\log k)^2\sqrt{kmT}\big )$ under semi-bandit feedback, where
$m$ is the number of arms and $k$ is the maximum cardinality of a feasible
action. Crucially, this result eliminates the dependency on $\log T$ and
matches the established $\Omega\big( \sqrt{kmT}\big)$ lower bound up to
$O\big((\log k)^2\big)$. We then extend our analysis to show that CMOSS is also
applicable to cascading feedback. Experiments on synthetic and real-world
datasets validate that CMOSS consistently outperforms benchmark algorithms in
both regret and runtime efficiency.

[Read original post](http://arxiv.org/abs/2508.06247v1)
