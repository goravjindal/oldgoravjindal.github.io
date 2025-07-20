---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: On the Complexity of the Optimal Correlated Equilibria in Extensive-Form"
date: 2025-07-16T00:00:00
---

**Authors:** [Vincent Cheval](https://dblp.uni-trier.de/search?q=Vincent+Cheval), [Florian Horn](https://dblp.uni-trier.de/search?q=Florian+Horn), [Soumyajit Paul](https://dblp.uni-trier.de/search?q=Soumyajit+Paul), [Mahsa Shirmohammadi](https://dblp.uni-trier.de/search?q=Mahsa+Shirmohammadi)

A major open question in algorithmic game theory is whether normal-form
correlated equilibria (NFCE) can be computed efficiently in succinct games such
as extensive-form games [DFF+25,6PR24,FP23,HvS08,VSF08,PR08]. Motivated by this
question, we study the associated Threshold problem: deciding whether there
exists a correlated equilibrium whose value exceeds a given threshold. We prove
that this problem is PSPACE-hard for NFCE in multiplayer extensive-form games
with perfect recall, even for fixed thresholds. To contextualize this result,
we also establish the complexity of the Threshold problem for Nash equilibria
in this setting, showing it is ER-complete. These results uncover a surprising
complexity reversal: while optimal correlated equilibria are computationally
simpler than optimal Nash in normal-form games, the opposite holds in
extensive-form games, where computing optimal correlated equilibria is provably
harder. Building on this line of inquiry, we also address a related question by
[VSF08], who introduced the notions of extensive-form correlated equilibrium
(EFCE) and agent-form correlated equilibrium (AFCE). They asked how difficult
the Threshold problem is for AFCE; we answer this question by proving that it
is NP-hard, even in two-player games without chance nodes. Complementing our
hardness results, we establish tight complexity classifications for the
Threshold problem across several correlated equilibrium concepts - including
EFCE, AFCE, normal-form coarse, extensive-form coarse, and agent-form coarse
correlated equilibria. For each of these solution concepts in multiplayer
stochastic extensive-form games with perfect recall, we prove NP-completeness
by providing matching NP upper bounds to the previously known hardness results.
Together, our results provide the most complete landscape to date for the
complexity of optimal equilibrium computation in extensive-form games.

[Read original post](http://arxiv.org/abs/2507.11509v1)
