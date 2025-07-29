---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: TIMEST: Temporal Information Motif Estimator Using Sampling Trees"
date: 2025-07-29T00:00:00
---

**Authors:** [Yunjie Pan](https://dblp.uni-trier.de/search?q=Yunjie+Pan), [Omkar Bhalerao](https://dblp.uni-trier.de/search?q=Omkar+Bhalerao), [C. Seshadhri](https://dblp.uni-trier.de/search?q=C.+Seshadhri), [Nishil Talati](https://dblp.uni-trier.de/search?q=Nishil+Talati)

The mining of pattern subgraphs, known as motifs, is a core task in the field
of graph mining. Edges in real-world networks often have timestamps, so there
is a need for temporal motif mining. A temporal motif is a richer structure
that imposes timing constraints on the edges of the motif. Temporal motifs have
been used to analyze social networks, financial transactions, and biological
networks.
Motif counting in temporal graphs is particularly challenging. A graph with
millions of edges can have trillions of temporal motifs, since the same edge
can occur with multiple timestamps. There is a combinatorial explosion of
possibilities, and state-of-the-art algorithms cannot manage motifs with more
than four vertices.
In this work, we present TIMEST: a general, fast, and accurate estimation
algorithm to count temporal motifs of arbitrary sizes in temporal networks. Our
approach introduces a temporal spanning tree sampler that leverages weighted
sampling to generate substructures of target temporal motifs. This method
carefully takes a subset of temporal constraints of the motif that can be
jointly and efficiently sampled. TIMEST uses randomized estimation techniques
to obtain accurate estimates of motif counts.
We give theoretical guarantees on the running time and approximation
guarantees of TIMEST. We perform an extensive experimental evaluation and show
that TIMEST is both faster and more accurate than previous algorithms. Our CPU
implementation exhibits an average speedup of 28x over state-of-the-art GPU
implementation of the exact algorithm, and 6x speedup over SOTA approximate
algorithms while consistently showcasing less than 5% error in most cases. For
example, TIMEST can count the number of instances of a financial fraud temporal
motif in four minutes with 0.6% error, while exact methods take more than two
days.

[Read original post](http://arxiv.org/abs/2507.20441v1)
