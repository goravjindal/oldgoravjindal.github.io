---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Towards EXPTIME One Way Functions: Bloom Filters, Succinct Graphs,"
date: 2025-08-05T00:00:00
---

**Authors:** [Shlomi Dolev](https://dblp.uni-trier.de/search?q=Shlomi+Dolev)

Consider graphs of n nodes, and use a Bloom filter of length 2 log3 n bits.
An edge between nodes i and j, with i < j, turns on a certain bit of the Bloom
filter according to a hash function on i and j. Pick a set of log n nodes and
turn on all the bits of the Bloom filter required for these log n nodes to form
a clique. As a result, the Bloom filter implies the existence of certain other
edges, those edges (x, y), with x < y, such that all the bits selected by
applying the hash functions to x and y happen to have been turned on due to
hashing the clique edges into the Bloom filter.
Constructing the graph consisting of the clique-selected edges and those
edges mapped to the turned-on bits of the Bloom filter can be performed in
polynomial time in n. Choosing a large enough polylogarithmic in n Bloom filter
yields that the graph has only one clique of size log n, the planted clique.
When the hash function is black-boxed, finding that clique is intractable and,
therefore, inverting the function that maps log n nodes to a graph is not
(likely to be) possible in polynomial time.

[Read original post](http://arxiv.org/abs/2508.01649v1)
