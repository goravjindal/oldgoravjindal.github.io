---
layout: post
category: cstheoryrss
title: "ECCC Papers: TR25-108 | Efficient randomized strong 2-source non-malleable extractor for any linear min-entropy. |"
date: 2025-08-01T17:04:27
---

Randomness is a fundamental requirement in cryptographic systems, enabling secure encryption, commitments, and zero-knowledge proofs. However, real-world randomness sources often suffer from weaknesses that adversaries can exploit, leading to significant security vulnerabilities. While deterministic randomness extraction from a single min-entropy source is impossible, two-source extractors provide a robust solution by generating nearly uniform randomness from two independent weak sources. Moreover, cryptographic systems must also be resilient to leakage and tampering attacks, necessitating the development of non-malleable two-source extractors.
In this work, we construct a two-source non-malleable extractor in the Common Reference String (CRS) model, where a random low-degree polynomial is sampled once and made accessible to independent random sources, the distinguisher, and the tamperer. Our extractor requires only linear min-entropy in both sources and doesn't rely on strong computational assumptions, in contrast to prior constructions requiring computational assumptions such as sub-exponential hardness of the Decisional Diffie-Hellman (DDH) problem. Notably, our construction builds upon and relies on the recent breakthrough proof of the polynomial Freiman-Ruzsa conjecture. A connection of the Freiman-Ruzsa conjecture with two-source extractors was considered in prior work [ZBS11],[AGMR24], but their construction did not achieve non-malleability.
Our results advance the state of non-malleable cryptographic primitives, with applications in secure storage, leakage-resilient cryptography, and privacy amplification. By eliminating the need for strong computational hardness assumptions, our techniques provide a more foundational and widely applicable method for randomness extraction.
We also show, that the requirements on CRS for our application are so mild that the CRS can be sampled with 2 party computation even when one of the parties is malicious (setting in which establishing unbiased coins is impossible).

[Read original post](https://eccc.weizmann.ac.il/report/2025/108)
