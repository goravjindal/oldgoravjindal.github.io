---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Optimized methods for composite optimization: a reduction perspective"
date: 2025-07-01T00:00:00
---

**Authors:** [Jinho Bok](https://dblp.uni-trier.de/search?q=Jinho+Bok), [Jason M. Altschuler](https://dblp.uni-trier.de/search?q=Jason+M.+Altschuler)

Recent advances in convex optimization have leveraged computer-assisted
proofs to develop optimized first-order methods that improve over classical
algorithms. However, each optimized method is specially tailored for a
particular problem setting, and it is a well-documented challenge to extend
optimized methods to other settings due to their highly bespoke design and
analysis. We provide a general framework that derives optimized methods for
composite optimization directly from those for unconstrained smooth
optimization. The derived methods naturally extend the original methods,
generalizing how proximal gradient descent extends gradient descent. The key to
our result is certain algebraic identities that provide a unified and
straightforward way of extending convergence analyses from unconstrained to
composite settings. As concrete examples, we apply our framework to establish
(1) the phenomenon of stepsize acceleration for proximal gradient descent; (2)
a convergence rate for the proximal optimized gradient method which is faster
than FISTA; (3) a new method that improves the state-of-the-art rate for
minimizing gradient norm in the composite setting.