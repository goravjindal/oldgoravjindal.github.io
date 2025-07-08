---
layout: post
category: cstheoryrss
title: "arXiv: Computational Geometry: Node-neighbor subnetworks and Hk-core decomposition"
date: 2025-07-08T00:00:00
---

**Authors:** [Dinghua Shi](https://dblp.uni-trier.de/search?q=Dinghua+Shi), [Yang Zhao](https://dblp.uni-trier.de/search?q=Yang+Zhao), [Guanrong Chen](https://dblp.uni-trier.de/search?q=Guanrong+Chen)

The network homology Hk-core decomposition proposed in this article is
similar to the k-core decomposition based on node degrees of the network. The
C. elegans neural network and the cat cortical network are used as examples to
reveal the symmetry of the deep structures of such networks. First, based on
the concept of neighborhood in mathematics, some new concepts are introduced,
including such as node-neighbor subnetwork and Betti numbers of the neighbor
subnetwork, among others. Then, the Betti numbers of the neighbor subnetwork of
each node are computed, which are used to perform Hk-core decomposition of the
network homology. The construction process is as follows: the initial network
is referred to as the H0-core; the H1-core is obtained from the H0-core by
deleting some nodes of certain properties; the H2-core is obtained from the
H1-core by deleting some nodes or edges of certain properties; the H3-core is
obtained from the H2-core by deleting some nodes of certain properties or by
retaining the nodes of certain properties, and so on, which will be described
in detail in the main text. Throughout the process, the index of node involved
in deleting edge needs to be updated in every step. The Hk-core decomposition
is easy to implement in parallel. It has a wide range of applications in many
fields such as network science, data science, computational topology, and
artificial intelligence. In this article, we also show how to use it to
simplify homology calculation, e.g. for the C. elegans neural network, whereas
the results of decomposition are the H1-core, the H2-core, and the H3-core.
Thus, the simplexes consisting of four highest-order cavities in the H3-core
subnetwork can also be directly obtained.

[Read original post](http://arxiv.org/abs/2507.04948v1)
