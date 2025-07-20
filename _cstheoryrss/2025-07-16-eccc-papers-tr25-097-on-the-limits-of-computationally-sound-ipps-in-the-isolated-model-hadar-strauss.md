---
layout: post
category: cstheoryrss
title: "ECCC Papers: TR25-097 | On the Limits of Computationally Sound IPPs in the Isolated Model |"
date: 2025-07-16T20:26:32
---

Interactive proofs of proximity (IPPs) are a relaxation of interactive proofs, analogous to property testing, in which soundness is required to hold only for inputs that are far from the property being verified. In such proof systems, the verifier has oracle access to the input, and it engages in two types of activities before making its decision: querying the input oracle and communicating with the prover. The main objective is to achieve protocols where both the query and communication complexities are extremely low.
Of particular interest are IPPs in which the querying and the interacting activities are performed independently, with no information flow from one activity to the other. Such IPPs were systematically studied by Goldreich, Rothblum, and Skverer (ITCS 2023), who introduced two variants: the pre-coordinated model, where the querying and interacting activities may use a common source of randomness, and the isolated model, where the two activities are fully independent, each operating with a separate source of randomness.
We focus on what is possible under these models when soundness is relaxed to computational soundness. Our previous work (ECCC, TR24-131) showed that the pre-coordinated model becomes significantly more powerful under this relaxation. In this work, we consider the isolated model under the same relaxation and show a separation between the two models. We consider a property that, by our previous work, has a computationally sound IPP in the pre-coordinated model with poly-logarithmic complexities (assuming the existence of collision-resistant hashing functions), and show that any computationally sound IPP in the isolated model for this property must have either query complexity or communication complexity that is $n^{\Omega(1)}$, where $n$ is the length of the input.

[Read original post](https://eccc.weizmann.ac.il/report/2025/097)
