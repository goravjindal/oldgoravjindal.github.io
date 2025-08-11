---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: On the Classical Hardness of the Semidirect Discrete Logarithm Problem"
date: 2025-08-08T00:00:00
---

**Authors:** [Mohammad Ferry Husnil Arif](https://dblp.uni-trier.de/search?q=Mohammad+Ferry+Husnil+Arif), [Muhammad Imran](https://dblp.uni-trier.de/search?q=Muhammad+Imran)

The semidirect discrete logarithm problem (SDLP) in finite groups was
proposed as a foundation for post-quantum cryptographic protocols, based on the
belief that its non-abelian structure would resist quantum attacks. However,
recent results have shown that SDLP in finite groups admits efficient quantum
algorithms, undermining its quantum resistance. This raises a fundamental
question: does the SDLP offer any computational advantages over the standard
discrete logarithm problem (DLP) against classical adversaries? In this work,
we investigate the classical hardness of SDLP across different finite group
platforms. We establish that the group-case SDLP can be reformulated as a
generalized discrete logarithm problem, enabling adaptation of classical
algorithms to study its complexity. We present a concrete adaptation of the
Baby-Step Giant-Step algorithm for SDLP, achieving time and space complexity
$O(\sqrt{r})$ where $r$ is the period of the underlying cycle structure.
Through theoretical analysis and experimental validation in SageMath, we
demonstrate that the classical hardness of SDLP is highly platform-dependent
and does not uniformly exceed that of standard DLP. In finite fields
$\mathbb{F}\_p^\*$, both problems exhibit comparable complexity. Surprisingly, in
elliptic curves $E(\mathbb{F}\_p)$, the SDLP becomes trivial due to the bounded
automorphism group, while in elementary abelian groups $\mathbb{F}\_p^n$, the
SDLP can be harder than DLP, with complexity varying based on the eigenvalue
structure of the automorphism. Our findings reveal that the non-abelian
structure of semidirect products does not inherently guarantee increased
classical hardness, suggesting that the search for classically hard problems
for cryptographic applications requires more careful consideration of the
underlying algebraic structures.

[Read original post](http://arxiv.org/abs/2508.05048v1)
