---
layout: post
category: cstheoryrss
title: "ECCC Papers: TR25-095 |  Godel in Cryptography: Effectively Zero-Knowledge Proofs for NP with No Interaction, No Setup, and Perfect Soundness | 

	Rahul Ilango"
date: 2025-07-15T18:51:51
---

A zero-knowledge proof demonstrates that a fact (like that a Sudoku puzzle has a solution) is true while, counterintuitively, revealing nothing else (like what the solution actually is). This remarkable guarantee is extremely useful in cryptographic applications, but it comes at a cost. A classical impossibility result by Goldreich and Oren [J. Cryptol. '94] shows that zero-knowledge proofs must necessarily sacrifice basic properties of traditional mathematical proofs --- namely perfect soundness (that no proof of a false statement exists) and non-interactivity (that a proof can be transmitted in a single message).
Contrary to this impossibility, we show that zero-knowledge with perfect soundness and no interaction is effectively possible. We do so by defining and constructing a powerful new relaxation of zero-knowledge. Intuitively, while the classical zero-knowledge definition requires that an object called a simulator actually exists, our new definition only requires that one cannot rule out that a simulator exists (in a particular logical sense). Using this, we show that \*\*every falsifiable security property of (classical) zero-knowledge can be achieved with no interaction, no setup, and perfect soundness.\*\* This enables us to remove interaction and setup from (classical) zero-knowledge in essentially all of its applications in the literature, at the relatively mild cost that such applications now have security that is "game-based" instead of "simulation-based."
Our construction builds on the work of Kuykendall and Zhandry [TCC '20] and relies on two central, longstanding, and well-studied assumptions that we show are also necessary. The first is the existence of non-interactive witness indistinguishable proofs, which follows from standard assumptions in cryptography. The second is Krajícek and Pudlak's 1989 conjecture that no optimal proof system exists. This is one of the main conjectures in the field of proof complexity and is the natural finitistic analogue of the impossibility of Hilbert's second problem (and, hence, also Gödel's incompleteness theorem). Our high-level idea is to use these assumptions to construct a prover and verifier where no simulator exists, but the non-existence of a simulator is independent (in the logical sense of unprovability) of an arbitrarily strong logical system. One such logical system is the standard axioms of mathematics: ZFC.

[Read original post](https://eccc.weizmann.ac.il/report/2025/095)
