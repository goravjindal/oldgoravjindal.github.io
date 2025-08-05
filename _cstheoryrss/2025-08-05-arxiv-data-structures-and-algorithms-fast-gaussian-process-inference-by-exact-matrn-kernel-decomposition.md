---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Fast Gaussian process inference by exact Matrn kernel decomposition"
date: 2025-08-05T00:00:00
---

**Authors:** [Nicolas Langrené](https://dblp.uni-trier.de/search?q=Nicolas+Langren%C3%A9), [Xavier Warin](https://dblp.uni-trier.de/search?q=Xavier+Warin), [Pierre Gruet](https://dblp.uni-trier.de/search?q=Pierre+Gruet)

To speed up Gaussian process inference, a number of fast kernel matrix-vector
multiplication (MVM) approximation algorithms have been proposed over the
years. In this paper, we establish an exact fast kernel MVM algorithm based on
exact kernel decomposition into weighted empirical cumulative distribution
functions, compatible with a class of kernels which includes multivariate
Mat\'ern kernels with half-integer smoothness parameter. This algorithm uses a
divide-and-conquer approach, during which sorting outputs are stored in a data
structure. We also propose a new algorithm to take into account some linear
fixed effects predictor function. Our numerical experiments confirm that our
algorithm is very effective for low-dimensional Gaussian process inference
problems with hundreds of thousands of data points. An implementation of our
algorithm is available at
https://gitlab.com/warin/fastgaussiankernelregression.git.

[Read original post](http://arxiv.org/abs/2508.01864v1)
