---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Amplitude amplification and estimation require inverses"
date: 2025-08-01T00:00:00
---

**Authors:** [Ewin Tang](https://dblp.uni-trier.de/search?q=Ewin+Tang), [John Wright](https://dblp.uni-trier.de/search?q=John+Wright)

We prove that the generic quantum speedups for brute-force search and
counting only hold when the process we apply them to can be efficiently
inverted. The algorithms speeding up these problems, amplitude amplification
and amplitude estimation, assume the ability to apply a state preparation
unitary $U$ and its inverse $U^\dagger$; we give problem instances based on
trace estimation where no algorithm which uses only $U$ beats the naive,
quadratically slower approach. Our proof of this is simple and goes through the
compressed oracle method introduced by Zhandry. Since these two subroutines are
responsible for the ubiquity of the quadratic "Grover" speedup in quantum
algorithms, our result explains why such speedups are far harder to come by in
the settings of quantum learning, metrology, and sensing. In these settings,
$U$ models the evolution of an experimental system, so implementing $U^\dagger$
can be much harder -- tantamount to reversing time within the system. Our
result suggests a dichotomy: without inverse access, quantum speedups are
scarce; with it, quantum speedups abound.

[Read original post](http://arxiv.org/abs/2507.23787v1)
