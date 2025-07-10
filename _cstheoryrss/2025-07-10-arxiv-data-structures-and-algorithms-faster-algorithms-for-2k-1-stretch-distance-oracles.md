---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Faster Algorithms for $(2k-1)$-Stretch Distance Oracles"
date: 2025-07-10T00:00:00
---

**Authors:** [Avi Kadria](https://dblp.uni-trier.de/search?q=Avi+Kadria), [Liam Roditty](https://dblp.uni-trier.de/search?q=Liam+Roditty)

Let $G=(V, E)$ be an undirected $n$-vertices $m$-edges graph with
non-negative edge weights. In this paper, we present three new algorithms for
constructing a $(2k-1)$-stretch distance oracle with $O(n^{1+\frac{1}{k}})$
space. The first algorithm runs in $\Ot(\max(n^{1+2/k},
m^{1-\frac{1}{k-1}}n^{\frac{2}{k-1}}))$ time, and improves upon the
$\Ot(\min(mn^{\frac{1}{k}},n^2))$ time of Thorup and Zwick [STOC 2001, JACM
2005] and Baswana and Kavitha [FOCS 2006, SICOMP 2010], for every $k > 2$ and
$m=\Omega(n^{1+\frac{1}{k}+\eps})$. This yields the first truly subquadratic
time construction for every $2 < k < 6$, and nearly resolves the open problem
posed by Wulff-Nilsen [SODA 2012] on the existence of such constructions.
The two other algorithms have a running time of the form $\Ot(m+n^{1+f(k)})$,
which is near linear in $m$ if $m=\Omega(n^{1+f(k)})$, and therefore optimal in
such graphs. One algorithm runs in $\Ot(m+n^{\frac32+\frac{3}{4k-6}})$-time,
which improves upon the $\Ot(n^2)$-time algorithm of Baswana and Kavitha [FOCS
2006, SICOMP 2010], for $3 < k < 6$, and upon the
$\Ot(m+n^{\frac{3}{2}+\frac{2}{k}+O(k^{-2})})$-time algorithm of Wulff-Nilsen
[SODA 2012], for every $k\geq 6$. This is the first linear time algorithm for
constructing a $7$-stretch distance oracle and a $9$-stretch distance oracle,
for graphs with truly subquadratic density.\footnote{with $m=n^{2-\eps}$ for
some $\eps > 0$.} The other algorithm runs in
$\Ot(\sqrt{k}m+kn^{1+\frac{2\sqrt{2}}{\sqrt{k}}})$ time, (and hence relevant
only for $k\ge 16$), and improves upon the
$\Ot(\sqrt{k}m+kn^{1+\frac{2\sqrt{6}}{\sqrt{k}}+O(k^{-1})})$ time algorithm of
Wulff-Nilsen [SODA 2012] (which is relevant only for $k\ge 96$). ...

[Read original post](http://arxiv.org/abs/2507.06721v1)
