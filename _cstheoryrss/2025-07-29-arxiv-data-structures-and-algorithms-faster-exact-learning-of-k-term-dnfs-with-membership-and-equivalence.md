---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Faster exact learning of k-term DNFs with membership and equivalence"
date: 2025-07-29T00:00:00
---

**Authors:** [Josh Alman](https://dblp.uni-trier.de/search?q=Josh+Alman), [Shivam Nadimpalli](https://dblp.uni-trier.de/search?q=Shivam+Nadimpalli), [Shyamal Patel](https://dblp.uni-trier.de/search?q=Shyamal+Patel), [Rocco Servedio](https://dblp.uni-trier.de/search?q=Rocco+Servedio)

In 1992 Blum and Rudich [BR92] gave an algorithm that uses membership and
equivalence queries to learn $k$-term DNF formulas over $\{0,1\}^n$ in time
$\textsf{poly}(n,2^k)$, improving on the naive $O(n^k)$ running time that can
be achieved without membership queries [Val84]. Since then, many alternative
algorithms [Bsh95, Kus97, Bsh97, BBB+00] have been given which also achieve
runtime $\textsf{poly}(n,2^k)$.
We give an algorithm that uses membership and equivalence queries to learn
$k$-term DNF formulas in time $\textsf{poly}(n) \cdot 2^{\tilde{O}(\sqrt{k})}$.
This is the first improvement for this problem since the original work of Blum
and Rudich [BR92].
Our approach employs the Winnow2 algorithm for learning linear threshold
functions over an enhanced feature space which is adaptively constructed using
membership queries. It combines a strengthened version of a technique that
effectively reduces the length of DNF terms from the original work of [BR92]
with a range of additional algorithmic tools (attribute-efficient learning
algorithms for low-weight linear threshold functions and techniques for finding
relevant variables from junta testing) and analytic ingredients (extremal
polynomials and noise operators) that are novel in the context of query-based
DNF learning.

[Read original post](http://arxiv.org/abs/2507.20336v1)
