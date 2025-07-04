---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Indexing Tries within Entropy-Bounded Space"
date: 2025-07-04T00:00:00
---

**Authors:** [Lorenzo Carfagna](https://dblp.uni-trier.de/search?q=Lorenzo+Carfagna), [Carlo Tosoni](https://dblp.uni-trier.de/search?q=Carlo+Tosoni)

We study the problem of indexing and compressing tries using a BWT-based
approach. Specifically, we consider a succinct and compressed representation of
the XBWT of Ferragina et al.\ [FOCS '05, JACM '09] corresponding to the
analogous of the FM-index [FOCS '00, JACM '05] for tries. This representation
allows to efficiently count the number of nodes reached by a given string
pattern. To analyze the space complexity of the above trie index, we propose a
proof for the combinatorial problem of counting the number of tries with a
given symbol distribution. We use this formula to define a worst-case entropy
measure for tries, as well as a notion of k-th order empirical entropy. In
particular, we show that the relationships between these two entropy measures
are similar to those between the corresponding well-known measures for strings.
We use these measures to prove that the XBWT of a trie can be encoded within a
space bounded by our k-th order empirical entropy plus a o(n) term, with n
being the number of nodes in the trie. Notably, as happens for strings, this
space bound can be reached for every sufficiently small k simultaneously.
Finally, we compare the space complexity of the above index with that of the
r-index for tries proposed by Prezza [SODA '21] and we prove that in some cases
the FM-index for tries is asymptotically smaller.