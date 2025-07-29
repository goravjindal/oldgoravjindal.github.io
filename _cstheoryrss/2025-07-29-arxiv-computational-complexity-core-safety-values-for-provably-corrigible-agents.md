---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: Core Safety Values for Provably Corrigible Agents"
date: 2025-07-29T00:00:00
---

**Authors:** [Aran Nayebi](https://dblp.uni-trier.de/search?q=Aran+Nayebi)

We introduce the first implementable framework for corrigibility, with
provable guarantees in multi-step, partially observed environments. Our
framework replaces a single opaque reward with five \*structurally separate\*
utility heads -- deference, switch-access preservation, truthfulness,
low-impact behavior via a belief-based extension of Attainable Utility
Preservation, and bounded task reward -- combined lexicographically by strict
weight gaps. Theorem 1 proves exact single-round corrigibility in the partially
observable off-switch game; Theorem 3 extends the guarantee to multi-step,
self-spawning agents, showing that even if each head is \emph{learned} to
mean-squared error $\varepsilon$ and the planner is $\varepsilon$-sub-optimal,
the probability of violating \emph{any} safety property is bounded while still
ensuring net human benefit. In contrast to Constitutional AI or RLHF/RLAIF,
which merge all norms into one learned scalar, our separation makes obedience
and impact-limits dominate even when incentives conflict. For open-ended
settings where adversaries can modify the agent, we prove that deciding whether
an arbitrary post-hack agent will ever violate corrigibility is undecidable by
reduction to the halting problem, then carve out a finite-horizon ``decidable
island'' where safety can be certified in randomized polynomial time and
verified with privacy-preserving, constant-round zero-knowledge proofs.
Consequently, the remaining challenge is the ordinary ML task of data coverage
and generalization: reward-hacking risk is pushed into evaluation quality
rather than hidden incentive leak-through, giving clearer implementation
guidance for today's LLM assistants and future autonomous systems.

[Read original post](http://arxiv.org/abs/2507.20964v1)
