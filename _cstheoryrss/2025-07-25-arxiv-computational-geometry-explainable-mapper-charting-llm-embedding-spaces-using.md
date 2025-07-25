---
layout: post
category: cstheoryrss
title: "arXiv: Computational Geometry: Explainable Mapper: Charting LLM Embedding Spaces Using"
date: 2025-07-25T00:00:00
---

**Authors:** [Xinyuan Yan](https://dblp.uni-trier.de/search?q=Xinyuan+Yan), [Rita Sevastjanova](https://dblp.uni-trier.de/search?q=Rita+Sevastjanova), [Sinie van der Ben](https://dblp.uni-trier.de/search?q=Sinie+van+der+Ben), [Mennatallah El-Assady](https://dblp.uni-trier.de/search?q=Mennatallah+El-Assady), [Bei Wang](https://dblp.uni-trier.de/search?q=Bei+Wang)

Large language models (LLMs) produce high-dimensional embeddings that capture
rich semantic and syntactic relationships between words, sentences, and
concepts. Investigating the topological structures of LLM embedding spaces via
mapper graphs enables us to understand their underlying structures.
Specifically, a mapper graph summarizes the topological structure of the
embedding space, where each node represents a topological neighborhood
(containing a cluster of embeddings), and an edge connects two nodes if their
corresponding neighborhoods overlap. However, manually exploring these
embedding spaces to uncover encoded linguistic properties requires considerable
human effort. To address this challenge, we introduce a framework for
semi-automatic annotation of these embedding properties. To organize the
exploration process, we first define a taxonomy of explorable elements within a
mapper graph such as nodes, edges, paths, components, and trajectories. The
annotation of these elements is executed through two types of customizable
LLM-based agents that employ perturbation techniques for scalable and automated
analysis. These agents help to explore and explain the characteristics of
mapper elements and verify the robustness of the generated explanations. We
instantiate the framework within a visual analytics workspace and demonstrate
its effectiveness through case studies. In particular, we replicate findings
from prior research on BERT's embedding properties across various layers of its
architecture and provide further observations into the linguistic properties of
topological neighborhoods.

[Read original post](http://arxiv.org/abs/2507.18607v1)
