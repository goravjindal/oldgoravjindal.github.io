---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: Hardness of Quantum Distribution Learning and Quantum Cryptography"
date: 2025-07-03T00:00:00
---

**Authors:** [Taiga Hiroka](https://dblp.uni-trier.de/search?q=Taiga+Hiroka), [Min-Hsiu Hsieh](https://dblp.uni-trier.de/search?q=Min-Hsiu+Hsieh), [Tomoyuki Morimae](https://dblp.uni-trier.de/search?q=Tomoyuki+Morimae)

The existence of one-way functions (OWFs) forms the minimal assumption in
classical cryptography. However, this is not necessarily the case in quantum
cryptography. One-way puzzles (OWPuzzs), introduced by Khurana and Tomer,
provide a natural quantum analogue of OWFs. The existence of OWPuzzs implies
$PP\neq BQP$, while the converse remains open. In classical cryptography, the
analogous problem-whether OWFs can be constructed from $P \neq NP$-has long
been studied from the viewpoint of hardness of learning. Hardness of learning
in various frameworks (including PAC learning) has been connected to OWFs or to
$P \neq NP$. In contrast, no such characterization previously existed for
OWPuzzs. In this paper, we establish the first complete characterization of
OWPuzzs based on the hardness of a well-studied learning model: distribution
learning. Specifically, we prove that OWPuzzs exist if and only if proper
quantum distribution learning is hard on average. A natural question that
follows is whether the worst-case hardness of proper quantum distribution
learning can be derived from $PP \neq BQP$. If so, and a worst-case to
average-case hardness reduction is achieved, it would imply OWPuzzs solely from
$PP \neq BQP$. However, we show that this would be extremely difficult: if
worst-case hardness is PP-hard (in a black-box reduction), then $SampBQP \neq
SampBPP$ follows from the infiniteness of the polynomial hierarchy. Despite
that, we show that $PP \neq BQP$ is equivalent to another standard notion of
hardness of learning: agnostic. We prove that $PP \neq BQP$ if and only if
agnostic quantum distribution learning with respect to KL divergence is hard.
As a byproduct, we show that hardness of agnostic quantum distribution learning
with respect to statistical distance against $PPT^{\Sigma\_3^P}$ learners
implies $SampBQP \neq SampBPP$.