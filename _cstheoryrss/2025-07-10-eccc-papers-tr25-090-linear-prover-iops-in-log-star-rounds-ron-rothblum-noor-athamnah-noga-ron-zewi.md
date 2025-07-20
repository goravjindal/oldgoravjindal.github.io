---
layout: post
category: cstheoryrss
title: "ECCC Papers: TR25-090 | Linear Prover IOPs in Log Star Rounds |"
date: 2025-07-10T12:23:56
---

Interactive Oracle Proofs (IOPs) form the backbone of some of the most efficient general-purpose cryptographic proof-systems. In an IOP, the prover can interact with the verifier over multiple rounds, where in each round the prover sends a long message, from which the verifier only queries a few symbols.
State-of-the-art IOPs achieve a linear-size prover and a poly-logarithmic verifier but require a relatively large, logarithmic, number of rounds. While Fiat-Shamir heuristic can be used to eliminate the need for actual interaction, in modern highly-parallelizable computer architectures such as GPUs, the large number of rounds still translates into a major bottleneck for the prover, since it needs to alternate between computing the IOP messages and the Fiat-Shamir hashes. Motivated by this fact, in this work we study the round complexity of linear-prover IOPs.
Our main result is an IOP for a large class of Boolean circuits, with only $O(\log^\*(S))$ rounds, where $\log^\*$ denotes the iterated logarithm function (and $S$ is the circuit size). The prover has linear size $O(S)$ and the verifier runs in time $\mathrm{polylog}(S)$ and has query complexity $O(\log^\*(S))$. The protocol is both conceptually simpler, and strictly more efficient, than prior linear prover IOPs for Boolean circuits.

[Read original post](https://eccc.weizmann.ac.il/report/2025/090)
