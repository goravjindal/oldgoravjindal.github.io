---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Fast and Efficient Merge of Sorted Input Lists in Hardware Using List"
date: 2025-07-14T00:00:00
---

**Authors:** [Robert B. Kent](https://dblp.uni-trier.de/search?q=Robert+B.+Kent), [Marios S. Pattichis](https://dblp.uni-trier.de/search?q=Marios+S.+Pattichis)

A new set of hardware merge sort devices are introduced here, which merge
multiple sorted input lists into a single sorted output list in a fast and
efficient manner. In each merge sorter, the values from the sorted input lists
are arranged in an input 2-D setup array, but with the order of each sorted
input list offset from the order of each of the other sorted input lists. In
these new devices, called List Offset Merge Sorters (LOMS), a minimal set of
column sort stages alternating with row sort stages process the input setup
array into a final output array, now in the defined sorted order. LOMS 2-way
sorters, which merge 2 sorted input lists, require only 2 merge stages and are
significantly faster than Kenneth Batcher's previous state-of-the-art 2-way
merge devices, Bitonic Merge Sorters and Odd-Even Merge Sorters. LOMS 2-way
sorters utilize the recently-introduced Single-Stage 2-way Merge Sorters (S2MS)
in their first stage. Both LOMS and S2MS devices can merge any mixture of input
list sizes, while Batcher's merge sorters are difficult to design unless the 2
input lists are equal, and a power-of-2. By themselves, S2MS devices are the
fastest 2-way merge sorters when implemented in this study's target FPGA
devices, but they tend to use a large number of LUT resources. LOMS 2-way
devices use fewer resources than comparable S2MS devices, enabling some large
LOMS devices to be implemented in a given FPGA when comparable S2MS devices
cannot fit in that FPGA. A List Offset 2-way sorter merges 2 lists, each with
32 values, into a sorted output list of those 64 values in 2.24 nS, a speedup
of 2.63 versus a comparable Batcher device. A LOMS 3-way merge sorter, merging
3 sorted input lists with 7 values, fully merges the 21 values in 3.4 nS, a
speedup of 1.36 versus the comparable state-of-the-art 3-way merge device.

[Read original post](http://arxiv.org/abs/2507.08658v1)
