---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Permutation patterns in streams"
date: 2025-07-16T00:00:00
---

**Authors:** [Benjamin Aram Berendsohn](https://dblp.uni-trier.de/search?q=Benjamin+Aram+Berendsohn)

Permutation patterns and pattern avoidance are central, well-studied concepts
in combinatorics and computer science. Given two permutations $\tau$ and $\pi$,
the pattern matching problem (PPM) asks whether $\tau$ contains $\pi$. This
problem arises in various contexts in computer science and statistics and has
been studied extensively in exact-, parameterized-, approximate-,
property-testing- and other formulations.
In this paper, we study pattern matching in a \emph{streaming setting}, when
the input $\tau$ is revealed sequentially, one element at a time. There is
extensive work on the space complexity of various statistics in streams of
integers. The novelty of our setting is that the input stream is \emph{a
permutation}, which allows inferring some information about future inputs. Our
algorithms crucially take advantage of this fact, while existing lower bound
techniques become difficult to apply.
We show that the complexity of the problem changes dramatically depending on
the pattern~$\pi$. The space requirement is: $\Theta(k\log{n})$ for the
monotone patterns $\pi = 12\dots k$, or $\pi = k\dots21$, $O(\sqrt{n\log{n}})$
for $\pi \in \{312,132\}$, $O(\sqrt{n} \log n)$ for $\pi \in \{231,213\}$, and
$\widetilde{\Theta}\_{\pi}(n)$ for all other $\pi$. If $\tau$ is an arbitrary
sequence of integers (not necessary a permutation), we show that the complexity
is $\widetilde{\Theta}\_{\pi}(n)$ in all except the first (monotone) cases.

[Read original post](http://arxiv.org/abs/2507.11291v1)
