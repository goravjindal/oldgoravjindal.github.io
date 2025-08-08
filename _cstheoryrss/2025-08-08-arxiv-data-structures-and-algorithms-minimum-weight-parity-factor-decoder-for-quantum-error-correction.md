---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Minimum-Weight Parity Factor Decoder for Quantum Error Correction"
date: 2025-08-08T00:00:00
---

**Authors:** [Yue Wu](https://dblp.uni-trier.de/search?q=Yue+Wu), [Binghong Li](https://dblp.uni-trier.de/search?q=Binghong+Li), [Kathleen Chang](https://dblp.uni-trier.de/search?q=Kathleen+Chang), [Shruti Puri](https://dblp.uni-trier.de/search?q=Shruti+Puri), [Lin Zhong](https://dblp.uni-trier.de/search?q=Lin+Zhong)

Fast and accurate quantum error correction (QEC) decoding is crucial for
scalable fault-tolerant quantum computation. Most-Likely-Error (MLE) decoding,
while being near-optimal, is intractable on general quantum Low-Density
Parity-Check (qLDPC) codes and typically relies on approximation and
heuristics. We propose HyperBlossom, a unified framework that formulates MLE
decoding as a Minimum-Weight Parity Factor (MWPF) problem and generalizes the
blossom algorithm to hypergraphs via a similar primal-dual linear programming
model with certifiable proximity bounds. HyperBlossom unifies all the existing
graph-based decoders like (Hypergraph) Union-Find decoders and Minimum-Weight
Perfect Matching (MWPM) decoder, thus bridging the gap between heuristic and
certifying decoders.
We implement HyperBlossom in software, namely Hyperion. Hyperion achieves a
4.8x lower logical error rate compared to the MWPM decoder on the distance-11
surface code and 1.6x lower logical error rate compared to a fine-tuned BPOSD
decoder on the $[[90, 8, 10]]$ bivariate bicycle code under code-capacity
noise. It also achieves an almost-linear average runtime scaling on both the
surface code and the color code, with numerical results up to sufficiently
large code distances of 99 and 31 for code-capacity noise and circuit-level
noise, respectively.

[Read original post](http://arxiv.org/abs/2508.04969v1)
