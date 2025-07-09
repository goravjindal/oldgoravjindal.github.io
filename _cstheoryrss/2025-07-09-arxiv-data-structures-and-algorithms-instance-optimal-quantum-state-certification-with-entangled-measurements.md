---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Instance-Optimal Quantum State Certification with Entangled Measurements"
date: 2025-07-09T00:00:00
---

**Authors:** [Ryan O'Donnell](https://dblp.uni-trier.de/search?q=Ryan+O%27Donnell), [Chirag Wadhwa](https://dblp.uni-trier.de/search?q=Chirag+Wadhwa)

We consider the task of quantum state certification: given a description of a
hypothesis state $\sigma$ and multiple copies of an unknown state $\rho$, a
tester aims to determine whether the two states are equal or $\epsilon$-far in
trace distance. It is known that $\Theta(d/\epsilon^2)$ copies of $\rho$ are
necessary and sufficient for this task, assuming the tester can make entangled
measurements over all copies [CHW07,OW15,BOW19]. However, these bounds are for
a worst-case $\sigma$, and it is not known what the optimal copy complexity is
for this problem on an instance-by-instance basis. While such instance-optimal
bounds have previously been shown for quantum state certification when the
tester is limited to measurements unentangled across copies [CLO22,CLHL22],
they remained open when testers are unrestricted in the kind of measurements
they can perform.
We address this open question by proving nearly instance-optimal bounds for
quantum state certification when the tester can perform fully entangled
measurements. Analogously to the unentangled setting, we show that the optimal
copy complexity for certifying $\sigma$ is given by the worst-case complexity
times the fidelity between $\sigma$ and the maximally mixed state. We prove our
lower bounds using a novel quantum analogue of the Ingster-Suslina method,
which is likely to be of independent interest. This method also allows us to
recover the $\Omega(d/\epsilon^2)$ lower bound for mixedness testing [OW15],
i.e., certification of the maximally mixed state, with a surprisingly simple
proof.

[Read original post](http://arxiv.org/abs/2507.06010v1)
