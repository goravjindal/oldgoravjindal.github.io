---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Benchmarking Filtered Approximate Nearest Neighbor Search Algorithms on"
date: 2025-07-30T00:00:00
---

**Authors:** [Patrick Iff](https://dblp.uni-trier.de/search?q=Patrick+Iff), [Paul Bruegger](https://dblp.uni-trier.de/search?q=Paul+Bruegger), [Marcin Chrapek](https://dblp.uni-trier.de/search?q=Marcin+Chrapek), [Maciej Besta](https://dblp.uni-trier.de/search?q=Maciej+Besta), [Torsten Hoefler](https://dblp.uni-trier.de/search?q=Torsten+Hoefler)

Advances in embedding models for text, image, audio, and video drive progress
across multiple domains, including retrieval-augmented generation,
recommendation systems, vehicle/person reidentification, and face recognition.
Many applications in these domains require an efficient method to retrieve
items that are close to a given query in the embedding space while satisfying a
filter condition based on the item's attributes, a problem known as Filtered
Approximate Nearest Neighbor Search (FANNS). In this work, we present a
comprehensive survey and taxonomy of FANNS methods and analyze how they are
benchmarked in the literature. By doing so, we identify a key challenge in the
current FANNS landscape: the lack of diverse and realistic datasets,
particularly ones derived from the latest transformer-based text embedding
models. To address this, we introduce a novel dataset consisting of embedding
vectors for the abstracts of over 2.7 million research articles from the arXiv
repository, accompanied by 11 real-world attributes such as authors and
categories. We benchmark a wide range of FANNS methods on our novel dataset and
find that each method has distinct strengths and limitations; no single
approach performs best across all scenarios. ACORN, for example, supports
various filter types and performs reliably across dataset scales but is often
outperformed by more specialized methods. SeRF shows excellent performance for
range filtering on ordered attributes but cannot handle categorical attributes.
Filtered-DiskANN and UNG excel on the medium-scale dataset but fail on the
large-scale dataset, highlighting the challenge posed by transformer-based
embeddings, which are often more than an order of magnitude larger than earlier
embeddings. We conclude that no universally best method exists.

[Read original post](http://arxiv.org/abs/2507.21989v1)
