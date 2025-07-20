---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Distributed Approximation Algorithms for Minimum Dominating Set in"
date: 2025-07-08T00:00:00
---

**Authors:** [Marthe Bonamy](https://dblp.uni-trier.de/search?q=Marthe+Bonamy), [Cyril Gavoille](https://dblp.uni-trier.de/search?q=Cyril+Gavoille), [Timothé Picavet](https://dblp.uni-trier.de/search?q=Timoth%C3%A9+Picavet), [Alexandra Wesolek](https://dblp.uni-trier.de/search?q=Alexandra+Wesolek)

We give a new, short proof that graphs embeddable in a given Euler genus-$g$
surface admit a simple $f(g)$-round $\alpha$-approximation distributed
algorithm for Minimum Dominating Set (MDS), where the approximation ratio
$\alpha \le 906$. Using tricks from Heydt et al. [European Journal of
Combinatorics (2025)], we in fact derive that $\alpha \le 34 +\varepsilon$,
therefore improving upon the current state of the art of $24g+O(1)$ due to
Amiri et al. [ACM Transactions on Algorithms (2019)]. It also improves the
approximation ratio of $91+\varepsilon$ due to Czygrinow et al. [Theoretical
Computer Science (2019)] in the particular case of orientable surfaces.
All our distributed algorithms work in the deterministic LOCAL model. They do
not require any preliminary embedding of the graph and only rely on two things:
a LOCAL algorithm for MDS on planar graphs with ``uniform'' approximation
guarantees and the knowledge that graphs embeddable in bounded Euler genus
surfaces have asymptotic dimension $2$.
More generally, our algorithms work in any graph class of bounded asymptotic
dimension where ``most vertices'' are locally in a graph class that admits a
LOCAL algorithm for MDS with uniform approximation guarantees.

[Read original post](http://arxiv.org/abs/2507.04960v1)
