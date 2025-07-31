---
layout: post
category: cstheoryrss
title: "ECCC Papers: TR25-107 | Extractors for Samplable Distributions from the Two-Source Extractor Recipe |"
date: 2025-07-30T19:51:28
---

Trevisan and Vadhan [TV00] first constructed seedless extractors for distributions samplable by poly-size circuits under the very strong complexity theoretic hardness assumption that $E=DTIME(2^{O(n)})$ is hard for exponential size circuits with oracle access to $\Sigma\_6^{P}$. Their construction works when the distribution has large min-entropy $k=(1-\gamma) \cdot n$, for small constant $\gamma>0$.
Recent works build on the approach of [TV00]. [BDGM23] obtain the same result under the weaker assumption that there is a problem in $\mathsf{E}$ that is hard for exponential size nondeterministic circuits. [BSS25] and [Sha25] improve the min-entropy threshold to $k = n^{1-\gamma}$ and $k = n^{\Omega(1)}$ respectively, reinstating oracle access to $\Sigma\_i^{P}$ for some $i$ in the assumption.
We introduce a new approach, inspired by constructions of two-source extractors [CZ16,BADTS17], using a new (and incomparable) hardness assumption that only involves deterministic circuits. Our approach reduces the task of constructing extractors for samplable distributions to constructing explicit non-malleable extractors with short seed-length.
Our new assumption has the same flavor as the classic assumption of [IW97] that $\mathsf{E}$ is hard for exponential size circuits, and similar to one recently considered in the context of fast derandomization [CT21]. Specifically, we assume that there is a constant $0<\alpha<1$ such that for every constant $C\_{hard} \ge 1$, there exists a constant $C\_{easy}$ and a problem in $DTIME(2^{C\_{easy} \cdot n})$ that is not in $DTIME(2^{C\_{hard} \cdot n})/2^{\alpha\cdot n}$. The key feature here is that we
allow the ``adversary'' to run in time larger than $2^{n}$ while still only using less than $2^n$ bits of nonuniformity.
Under this assumption, we use currently known constructions of non-malleable extractors to get the following results:
- An extractor for samplable distributions with min-entropy $k$ slightly larger than $n/2$. This is the first construction of any such extractor under an assumption that does not give the adversary nondeterminism.
- An extractor for samplable distributions with min-entropy $k=O(\log n \cdot \log \log n)$ also follows if, in addition to the new assumption, we also have the aforementioned assumption of [BDGM23], namely, that $E$ is hard for exponential size nondeterministic circuits. This is the first construction in the regime of $k \le poly log n$ under any assumption.
We also show that future improvements of the seed length of the best current non-malleable extractors [Li17] would imply the second result without the additional assumption.
Our key observation is that when a given source is samplable, the set of ``bad'' seeds to a non-malleable extractor is efficiently recognizable. We utilize this observation to show that in the constructions of two-source extractors in [CZ16,BADTS17], we can hope to replace the ``second source'' with (the truth table of) a sufficiently hard function. Thus our work reveals an unexpected connection between two-source extractors and extractors for samplable distributions, similar to Trevisan's connection between extractors and PRGs ``in the other direction.''

[Read original post](https://eccc.weizmann.ac.il/report/2025/107)
