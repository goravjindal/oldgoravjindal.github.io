---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: Testing Isomorphism of Boolean Functions over Finite Abelian Groups"
date: 2025-07-11T00:00:00
---

**Authors:** [Swarnalipa Datta](https://dblp.uni-trier.de/search?q=Swarnalipa+Datta), [Arijit Ghosh](https://dblp.uni-trier.de/search?q=Arijit+Ghosh), [Chandrima Kayal](https://dblp.uni-trier.de/search?q=Chandrima+Kayal), [Manaswi Paraashar](https://dblp.uni-trier.de/search?q=Manaswi+Paraashar), [Manmatha Roy](https://dblp.uni-trier.de/search?q=Manmatha+Roy)

Let $f$ and $g$ be Boolean functions over a finite Abelian group
$\mathcal{G}$, where $g$ is fully known, and we have {\em query access} to $f$,
that is, given any $x \in \mathcal{G}$ we can get the value $f(x)$. We study
the tolerant isomorphism testing problem: given $\epsilon \geq 0$ and $\tau >
0$, we seek to determine, with minimal queries, whether there exists an
automorphism $\sigma$ of $\mathcal{G}$ such that the fractional Hamming
distance between $f \circ \sigma$ and $g$ is at most $\epsilon$, or whether for
all automorphisms $\sigma$, the distance is at least $\epsilon + \tau$.
We design an efficient tolerant testing algorithm for this problem, with
query complexity $\mathrm{poly}\left( s, 1/\tau \right)$, where $s$ bounds the
spectral norm of $g$. Additionally, we present an improved algorithm when $g$
is Fourier sparse.
Our approach uses key concepts from Abelian group theory and Fourier
analysis, including the annihilator of a subgroup, Pontryagin duality, and a
pseudo inner-product for finite Abelian groups. We believe these techniques
will find further applications in property testing.

[Read original post](http://arxiv.org/abs/2507.07654v1)
