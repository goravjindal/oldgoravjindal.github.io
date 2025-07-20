---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Tight Guarantees for Cut-Relative Survivable Network Design via a"
date: 2025-07-08T00:00:00
---

**Authors:** [Nikhil Kumar](https://dblp.uni-trier.de/search?q=Nikhil+Kumar), [JJ Nan](https://dblp.uni-trier.de/search?q=JJ+Nan), [Chaitanya Swamy](https://dblp.uni-trier.de/search?q=Chaitanya+Swamy)

In the classical \emph{survivable-network-design problem} (SNDP), we are
given an undirected graph $G = (V, E)$, non-negative edge costs, and some
$(s\_i,t\_i,r\_i)$ tuples, where $s\_i,t\_i\in V$ and $r\_i\in\mathbb{Z}\_+$. We seek
a minimum-cost subset $H \subseteq E$ such that each $s\_i$-$t\_i$ pair remains
connected even if any $r\_i-1$ edges fail. It is well-known that SNDP can be
equivalently modeled using a weakly-supermodular \emph{cut-requirement
function} $f$, where we seek a minimum-cost edge-set containing at least $f(S)$
edges across every cut $S \subseteq V$.
Recently, Dinitz et al. proposed a variant of SNDP that enforces a
\emph{relative} level of fault tolerance with respect to $G$, where the goal is
to find a solution $H$ that is at least as fault-tolerant as $G$ itself. They
formalize this in terms of paths and fault-sets, which gives rise to
\emph{path-relative SNDP}. Along these lines, we introduce a new model of
relative network design, called \emph{cut-relative SNDP} (CR-SNDP), where the
goal is to select a minimum-cost subset of edges that satisfies the given
(weakly-supermodular) cut-requirement function to the maximum extent possible,
i.e., by picking $\min\{f(S),|\delta\_G(S)|\}$ edges across every cut
$S\subseteq V$.
Unlike SNDP, the cut-relative and path-relative versions of SNDP are not
equivalent. The resulting cut-requirement function for CR-SNDP (as also
path-relative SNDP) is not weakly supermodular, and extreme-point solutions to
the natural LP-relaxation need not correspond to a laminar family of tight cut
constraints. Consequently, standard techniques cannot be used directly to
design approximation algorithms for this problem. We develop a \emph{novel
decomposition technique} to circumvent this difficulty and use it to give a
\emph{tight $2$-approximation algorithm for CR-SNDP}. We also show new hardness
results for these relative-SNDP problems.

[Read original post](http://arxiv.org/abs/2507.04473v1)
