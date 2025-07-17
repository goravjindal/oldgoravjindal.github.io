---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: Which graph motif parameters count?"
date: 2025-07-17T00:00:00
---

**Authors:** [Markus Bläser](https://dblp.uni-trier.de/search?q=Markus+Bl%C3%A4ser), [Radu Curticapean](https://dblp.uni-trier.de/search?q=Radu+Curticapean), [Julian Dörfler](https://dblp.uni-trier.de/search?q=Julian+D%C3%B6rfler), [Christian Ikenmeyer](https://dblp.uni-trier.de/search?q=Christian+Ikenmeyer)

For a fixed graph H, the function #IndSub(H,\*) maps graphs G to the count of
induced H-copies in G; this function obviously "counts something" in that it
has a combinatorial interpretation. Linear combinations of such functions are
called graph motif parameters and have recently received significant attention
in counting complexity after a seminal paper by Curticapean, Dell and Marx
(STOC'17). We show that, among linear combinations of functions #IndSub(H,\*)
involving only graphs H without isolated vertices, precisely those with
positive integer coefficients maintain a combinatorial interpretation. It is
important to note that graph motif parameters can be nonnegative for all inputs
G, even when some coefficients are negative.
Formally, we show that evaluating any graph motif parameter with a negative
coefficient is impossible in an oracle variant of #P, where an implicit graph
is accessed by oracle queries. Our proof follows the classification of the
relativizing closure properties of #P by Hertrampf, Vollmer, and Wagner
(SCT'95) and the framework developed by Ikenmeyer and Pak (STOC'22), but our
application of the required Ramsey theorem turns out to be more subtle, as
graphs do not have the required Ramsey property.
Our techniques generalize from graphs to relational structures, including
colored graphs. Vastly generalizing this, we introduce motif parameters over
categories that count occurrences of sub-objects in the category. We then prove
a general dichotomy theorem that characterizes which such parameters have a
combinatorial interpretation. Using known results in Ramsey theory for
categories, we obtain a dichotomy for motif parameters of finite vector spaces
as well as parameter sets.

[Read original post](http://arxiv.org/abs/2507.12244v1)
