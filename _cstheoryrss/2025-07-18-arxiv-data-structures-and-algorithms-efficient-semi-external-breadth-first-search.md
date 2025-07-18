---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Efficient Semi-External Breadth-First Search"
date: 2025-07-18T00:00:00
---

**Authors:** [Xiaolong Wan](https://dblp.uni-trier.de/search?q=Xiaolong+Wan), [Xixian Han](https://dblp.uni-trier.de/search?q=Xixian+Han)

Breadth-first search (BFS) is known as a basic search strategy for learning
graph properties. As the scales of graph databases have increased tremendously
in recent years, large-scale graphs G are often disk-resident. Obtaining the
BFS results of G in semi-external memory model is inevitable, because the
in-memory BFS algorithm has to maintain the entire G in the main memory, and
external BFS algorithms consume high computational costs. As a good trade-off
between the internal and external memory models, semi-external memory model
assumes that the main memory can at least reside a spanning tree of G.
Nevertheless, the semi-external BFS problem is still an open issue due to its
difficulty. Therefore, this paper presents a comprehensive study for processing
BFS in semi-external memory model. After discussing the naive solutions based
on the basic framework of semi-external graph algorithms, this paper presents
an efficient algorithm, named EP-BFS, with a small minimum memory space
requirement, which is an important factor for evaluating semi-external
algorithms. Extensive experiments are conducted on both real and synthetic
large-scale graphs, where graph WDC-2014 contains over 1.7 billion nodes, and
graph eu-2015 has over 91 billion edges. Experimental results confirm that
EP-BFS can achieve up to 10 times faster.

[Read original post](http://arxiv.org/abs/2507.12925v1)
