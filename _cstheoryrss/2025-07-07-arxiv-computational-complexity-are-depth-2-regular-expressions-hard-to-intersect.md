---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: Are Depth-2 Regular Expressions Hard to Intersect?"
date: 2025-07-07T00:00:00
---

**Authors:** [Rocco Ascone](https://dblp.uni-trier.de/search?q=Rocco+Ascone), [Giulia Bernardini](https://dblp.uni-trier.de/search?q=Giulia+Bernardini), [Alessio Conte](https://dblp.uni-trier.de/search?q=Alessio+Conte), [Veronica Guerrini](https://dblp.uni-trier.de/search?q=Veronica+Guerrini), [Giulia Punzi](https://dblp.uni-trier.de/search?q=Giulia+Punzi)

We study the basic regular expression intersection testing problem, which
asks to determine whether the intersection of the languages of two regular
expressions is nonempty. A textbook solution to this problem is to construct
the nondeterministic finite automaton that accepts the language of both
expressions. This procedure results in a $\Theta(mn)$ running time, where $m$
and $n$ are the sizes of the two expressions, respectively. Following the
approach of Backurs and Indyk [FOCS'16] and Bringmann, Gr{\o}nlund, and Larsen
[FOCS'17] on regular expression matching and membership testing, we study the
complexity of intersection testing for homogeneous regular expressions of
bounded depth involving concatenation, OR, Kleene star, and Kleene plus.
Specifically, we consider all combinations of types of depth-2 regular
expressions and classify the time complexity of intersection testing as either
linear or quadratic, assuming SETH. The most interesting result is a quadratic
conditional lower bound for testing the intersection of a ''concatenation of
+s'' expression with a ''concatenation of ORs'' expression: this is the only
hard case that does not involve the Kleene star operator and is not implied by
existing lower bounds for the simpler membership testing problem.

[Read original post](http://arxiv.org/abs/2507.03593v1)
