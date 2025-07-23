---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Best-of-Both-Worlds Guarantees with Fairer Endings"
date: 2025-07-23T00:00:00
---

**Authors:** [Telikepalli Kavitha](https://dblp.uni-trier.de/search?q=Telikepalli+Kavitha), [Surya Panchapakesan](https://dblp.uni-trier.de/search?q=Surya+Panchapakesan), [Rohit Vaish](https://dblp.uni-trier.de/search?q=Rohit+Vaish), [Vignesh Viswanathan](https://dblp.uni-trier.de/search?q=Vignesh+Viswanathan), [Jatin Yadav](https://dblp.uni-trier.de/search?q=Jatin+Yadav)

Fair allocation of indivisible goods is a fundamental problem at the
interface of economics and computer science. Traditional approaches focus
either on randomized allocations that are fair in expectation or deterministic
allocations that are approximately fair. Recent work reconciles both these
approaches via best-of-both-worlds guarantees, wherein one seeks randomized
allocations that are fair in expectation (ex-ante fair) while being supported
on approximately fair allocations (ex-post fair). Prior work has shown that
under additive valuations, there always exists a randomized allocation that is
ex-ante stochastic-dominance envy-free (sd-EF) and ex-post envy-free up to one
good (EF1).
Our work is motivated by the goal of achieving stronger ex-post fairness
guarantees such as envy-freeness up to any good (EFX) along with meaningful
ex-ante guarantees. We make the following contributions:
1) We first consider lexicographic preferences, a subdomain of additive
valuations where ex-post EFX allocations always exist and can be computed
efficiently. On the negative side, we show that ex-ante sd-EF is fundamentally
incompatible with ex-post EFX, prompting a relaxation of the ex-ante benchmark.
We then present a poly. time algorithm that achieves ex-post EFX and PO
together with ex-ante 9/10-EF. Our algorithm uses dependent rounding and
leverages structural properties of EFX and PO allocations.
2)For monotone valuations, we study EFX-with-charity: a relaxation of EFX
where some goods remain unallocated, with no agent envying the unallocated
pool. We show that ex-post EFX-with-charity can be achieved alongside ex-ante
0.5-EF.
3)Finally, for subadditive valuations, we strengthen our previous ex-post
guarantee to EFX-with-bounded-charity, where at most n-1 goods (n= no. of
agents) remain unallocated, at the price of weakening the ex-ante guarantee to
0.5-proportionality.

[Read original post](http://arxiv.org/abs/2507.16209v1)
