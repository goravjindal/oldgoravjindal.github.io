---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Solving Linear Programs with Differential Privacy"
date: 2025-07-16T00:00:00
---

**Authors:** [Alina Ene](https://dblp.uni-trier.de/search?q=Alina+Ene), [Huy Le Nguyen](https://dblp.uni-trier.de/search?q=Huy+Le+Nguyen), [Ta Duy Nguyen](https://dblp.uni-trier.de/search?q=Ta+Duy+Nguyen), [Adrian Vladu](https://dblp.uni-trier.de/search?q=Adrian+Vladu)

We study the problem of solving linear programs of the form $Ax\le b$,
$x\ge0$ with differential privacy. For homogeneous LPs $Ax\ge0$, we give an
efficient $(\epsilon,\delta)$-differentially private algorithm which with
probability at least $1-\beta$ finds in polynomial time a solution that
satisfies all but
$O(\frac{d^{2}}{\epsilon}\log^{2}\frac{d}{\delta\beta}\sqrt{\log\frac{1}{\rho\_{0}}})$
constraints, for problems with margin $\rho\_{0}>0$. This improves the bound of
$O(\frac{d^{5}}{\epsilon}\log^{1.5}\frac{1}{\rho\_{0}}\mathrm{poly}\log(d,\frac{1}{\delta},\frac{1}{\beta}))$
by [Kaplan-Mansour-Moran-Stemmer-Tur, STOC '25]. For general LPs $Ax\le b$,
$x\ge0$ with potentially zero margin, we give an efficient
$(\epsilon,\delta)$-differentially private algorithm that w.h.p drops
$O(\frac{d^{4}}{\epsilon}\log^{2.5}\frac{d}{\delta}\sqrt{\log dU})$
constraints, where $U$ is an upper bound for the entries of $A$ and $b$ in
absolute value. This improves the result by Kaplan et al. by at least a factor
of $d^{5}$. Our techniques build upon privatizing a rescaling perceptron
algorithm by [Hoberg-Rothvoss, IPCO '17] and a more refined iterative procedure
for identifying equality constraints by Kaplan et al.

[Read original post](http://arxiv.org/abs/2507.10946v1)
