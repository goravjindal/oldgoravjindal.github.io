---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Fast One-Pass Sparse Approximation of the Top Eigenvectors of Huge"
date: 2025-07-24T00:00:00
---

**Authors:** [Edem Boahen](https://dblp.uni-trier.de/search?q=Edem+Boahen), [Simone Brugiapaglia](https://dblp.uni-trier.de/search?q=Simone+Brugiapaglia), [Hung-Hsu Chou](https://dblp.uni-trier.de/search?q=Hung-Hsu+Chou), [Mark Iwen](https://dblp.uni-trier.de/search?q=Mark+Iwen), [Felix Krahmer](https://dblp.uni-trier.de/search?q=Felix+Krahmer)

Motivated by applications such as sparse PCA, in this paper we present
provably-accurate one-pass algorithms for the sparse approximation of the top
eigenvectors of extremely massive matrices based on a single compact linear
sketch. The resulting compressive-sensing-based approaches can approximate the
leading eigenvectors of huge approximately low-rank matrices that are too large
to store in memory based on a single pass over its entries while utilizing a
total memory footprint on the order of the much smaller desired sparse
eigenvector approximations. Finally, the compressive sensing recovery algorithm
itself (which takes the gathered compressive matrix measurements as input, and
then outputs sparse approximations of its top eigenvectors) can also be
formulated to run in a time which principally depends on the size of the sought
sparse approximations, making its runtime sublinear in the size of the large
matrix whose eigenvectors one aims to approximate. Preliminary experiments on
huge matrices having $\sim 10^{16}$ entries illustrate the developed theory and
demonstrate the practical potential of the proposed approach.

[Read original post](http://arxiv.org/abs/2507.17036v1)
