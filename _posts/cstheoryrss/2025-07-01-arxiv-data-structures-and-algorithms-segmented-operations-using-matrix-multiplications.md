---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Segmented Operations using Matrix Multiplications"
date: 2025-07-01T00:00:00
---

**Authors:** [Aleksandros Sobczyk](https://dblp.uni-trier.de/search?q=Aleksandros+Sobczyk), [Giuseppe Sorrentino](https://dblp.uni-trier.de/search?q=Giuseppe+Sorrentino), [Anastasios Zouzias](https://dblp.uni-trier.de/search?q=Anastasios+Zouzias)

Specialized computational units that perform small matrix multiplications as
primitive operations are typically present in modern accelerators. However,
these units are often underutilized for many fundamental operations besides
dense matrix multiplications. The analysis of algorithms for such architectures
is currently stagnated due to the lack of a rigorous theoretical model of
computation that captures their characteristics. In this work, we propose
MMV-RAM, a computational model tailored to matrix multiplication accelerators.
MMV-RAM judiciously extends the Vector-RAM model with an additional processing
unit that multiplies two matrices of sizes $n\times s$ and $s\times s$ in a
single parallel step, where $s$ is a model parameter. We provide a detailed
theoretical analysis of the model, and carefully balance the computational
power between the matrix and vector units, guided by the circuit complexity
lower bound that parity is not in AC[0].
In MMV-RAM, we study algorithms for segmented scan and sum, two fundamental
parallel primitives. We propose a segmented scan algorithm that uses matrix
multiplications to perform speculative block-scan computations, which runs in
$O(\log\_s(n))$ steps. In contrast, we show that any algorithm that uses only
the vector unit of MMV-RAM requires
$\Omega\left(\frac{\log\_2(n)}{\log\_2\log\_2(n)}\right)$ steps. We further apply
these techniques to obtain similar theoretical speedups for element-wise vector
multiplication and matrix multiplication. Beyond the worst-case complexity
analysis, we propose algorithms for segmented operations that could lead to
highly efficient and pragmatic implementations. For example, we observe that
segmented sum is a combination of three elementary parallel primitives: scan,
compress, and vector differentiation. As a case study, we implement...