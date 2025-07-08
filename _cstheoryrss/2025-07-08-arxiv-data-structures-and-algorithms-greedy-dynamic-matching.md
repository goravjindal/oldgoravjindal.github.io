---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Greedy Dynamic Matching"
date: 2025-07-08T00:00:00
---

**Authors:** [Nick Arnosti](https://dblp.uni-trier.de/search?q=Nick+Arnosti), [Felipe Simon](https://dblp.uni-trier.de/search?q=Felipe+Simon)

We study a foundational model of dynamic matching market with abandonment.
This model has been studied by Collina et al (2020) and Aouad and Saritac
(2022), and many other papers have considered special cases. We compare the
performance of greedy policies -- which identify a set of "acceptable" matches
up front, and perform these matches as soon as possible -- to that of an
omniscient benchmark which knows the full arrival and departure sequence.
We use a novel family of linear programs ($LP^{ALG}$) to identify which
greedy policy to follow. We show that the value of $LP^ALG$ is a \*lower bound\*
on the value of the greedy policy that it identifies in two settings of
interest:
-When all types have the same departure rate.
-The bipartite case where types on the same side of the market have the same
departure rate.
The proofs of these results use a new result (Lemma 1), which relates the
\*probability\* that at least one agent from a set of types is present in the
system to the expected number of such agents.
We also show that the value of $LP^{ALG}$ is at least 1/2 of the reward rate
earned by the omniscient policy (Proposition 4). Therefore, for both settings
above, our greedy policy provably earns at least half of the omniscient reward
rate. This improves upon the bound of 1/8 from Collina (2020). In both settings
our competitive ratio of 1/2 is the best possible: no online policy can provide
a better guarantee (Theorem 2).
To show these results we introduce a new linear program that upper bounds the
objective value of the omniscient policy (Proposition 3). This improves upon
the upper bounds presented by Collina et al (2020) and Kessel et al (2022).

[Read original post](http://arxiv.org/abs/2507.04551v1)
