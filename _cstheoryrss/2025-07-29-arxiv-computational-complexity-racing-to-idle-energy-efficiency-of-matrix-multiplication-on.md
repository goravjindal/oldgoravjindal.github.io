---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: Racing to Idle: Energy Efficiency of Matrix Multiplication on"
date: 2025-07-29T00:00:00
---

**Authors:** [Mufakir Qamar Ansari](https://dblp.uni-trier.de/search?q=Mufakir+Qamar+Ansari), [Mudabir Qamar Ansari](https://dblp.uni-trier.de/search?q=Mudabir+Qamar+Ansari)

The paradigm shift towards multi-core and heterogeneous computing, driven by
the fundamental power and thermal limits of single-core processors, has
established energy efficiency as a first-class design constraint in
high-performance computing (HPC). Heterogeneous systems, integrating
traditional multi-core CPUs with specialized accelerators like discrete (dGPU)
and integrated (iGPU) graphics processing units, offer a compelling path to
navigating the trade-offs between performance and power. However, quantifying
these trade-offs on widely accessible hardware remains a critical area of
study. This paper presents a direct, empirical measurement of the performance
and energy-to-solution of a canonical HPC workload -- a 4096x4096 matrix-matrix
multiplication -- on three distinct compute architectures within a single
consumer-grade laptop: a multi-core AMD Ryzen 7 5800H CPU, a discrete NVIDIA
GeForce GTX 1650 GPU, and an integrated AMD Radeon Vega GPU. Using standard,
validated, and minimally intrusive tools such as Linux perf and nvidia-smi, we
find that the discrete GPU is not only the performance leader, achieving a
93.5x speedup over the CPU, but is also the most energy-efficient, consuming
only 2% of the energy used by the CPU, resulting in a 50-fold improvement in
energy efficiency. These findings provide a practical demonstration of the
"race to idle" principle and offer clear, quantitative guidance on
architectural choices for energy-aware software development.

[Read original post](http://arxiv.org/abs/2507.20063v1)
