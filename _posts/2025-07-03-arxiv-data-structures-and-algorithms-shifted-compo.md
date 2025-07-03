---
layout: post
title: "arXiv: Data Structures and Algorithms: Shifted Composition IV: Underdamped Langevin and Numerical
  Discretizations with Partial Acceleration"
date: 2025-07-03 13:21:53 
categories: [rss]
external_link: http://arxiv.org/abs/2506.23062v1
---

**Authors:** [Jason M. Altschuler](https://dblp.uni-trier.de/search?q=Jason+M.+Altschuler), [Sinho Chewi](https://dblp.uni-trier.de/search?q=Sinho+Chewi), [Matthew S. Zhang](https://dblp.uni-trier.de/search?q=Matthew+S.+Zhang)

Quantifying the convergence rate of the underdamped Langevin dynamics (ULD)
is a classical topic, in large part due to the possibility for
diffusive-to-ballistic speedups -- as was recently established for the
continuous-time dynamics via space-time Poincare inequalities. A central
challenge for analyzing ULD is that its degeneracy necessitates the development
of new analysis approaches, e.g., the theory of hypocoercivity. In this paper,
we give a new coupling-based framework for analyzing ULD and its numerical
discretizations. First, in the continuous-time setting, we use this framework
to establish new parabolic Harnack inequalities for ULD. These are the first
Harnack inequalities that decay to zero in contractive settings, thereby
reflecting the convergence properties of ULD in addition to just its regularity
properties.
Second, we build upon these Harnack inequalities to develop a local error
framework for analyzing discretizations of ULD in KL divergence. This extends
our framework in part III from uniformly elliptic diffusions to degenerate
diffusions, and shares its virtues: the framework is user-friendly, applies to
sophisticated discretization schemes, and does not require contractivity.
Applying this framework to the randomized midpoint discretization of ULD
establishes (i) the first ballistic acceleration result for log-concave
sampling (i.e., sublinear dependence on the condition number), and (ii) the
first $d^{1/3}$ iteration complexity guarantee for sampling to constant total
variation error in dimension $d$.
