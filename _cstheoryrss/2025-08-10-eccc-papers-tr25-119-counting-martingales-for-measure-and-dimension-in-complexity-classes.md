---
layout: post
category: cstheoryrss
title: "ECCC Papers: TR25-119 | Counting Martingales for Measure and Dimension in Complexity Classes |"
date: 2025-08-10T11:06:31
---

This paper makes two primary contributions. First, we introduce the concept of counting martingales and use it to define counting measures, counting dimensions, and counting strong dimensions. Second, we apply these new tools to strengthen previous circuit lower bounds.
Resource-bounded measure and dimension have traditionally focused on deterministic time and space bounds. We use counting complexity classes to develop resource-bounded counting measures and dimensions. Counting martingales are constructed using functions from the #P, SpanP, and GapP complexity classes. We show that counting martingales capture many martingale constructions in complexity theory. The resulting counting measures and dimensions are intermediate in power between the standard time-bounded and space-bounded notions, enabling finer-grained analysis where space-bounded measures are known, but time-bounded measures remain open.
For example, we show that BPP has #P-dimension 0 and BQP has GapP-dimension 0, whereas the P-dimensions of these classes remain open.
As our main application, we improve circuit-size lower bounds. Lutz (1992) strengthened Shannon's classic $(1-\epsilon)\frac{2^n}{n}$ lower bound (1949) to $\pspace$-measure, showing that almost all problems require circuits of size $\frac{2^n}{n}\left(1+\frac{\alpha \log n}{n}\right)$, for any $\alpha < 1$. We extend this result to SpanP-measure, with a proof that uses a connection through the Minimum Circuit Size Problem (MCSP) to construct a counting martingale. Our results imply that the stronger lower bound holds within the third level of the exponential-time hierarchy, whereas previously, it was only known in ESPACE. Under a derandomization hypothesis, this lower bound holds within the second level of the exponential-time hierarchy, specifically in the class $E^{NP}$. We study the #P-dimension of classical circuit complexity classes and the GapP-dimension of quantum circuit complexity classes. We also show that if one-way functions exist, then #P-dimension is strictly more powerful than P-dimension.

[Read original post](https://eccc.weizmann.ac.il/report/2025/119)
