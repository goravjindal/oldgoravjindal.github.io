---
layout: post
category: cstheoryrss
title: "ECCC Papers: TR25-105 | Location-Invariant Properties of Functions versus Properties of Distributions: United in Testing but Separated in Verification |"
date: 2025-07-29T15:14:57
---

A property of functions is called location-invariant (or symmetric) if it can be characterized in terms of the frequencies in which each value occurs in the function, regardless of the locations in which each value occurs.
It is known that the (query) complexity of testing location-invariant properties of functions
is closely related to the (sample) complexity of testing the (corresponding properties of the) corresponding distributions.
The main message of the current work is that this close relationship is not maintained in the context of verification.
This holds both when considering verification by general interactive proofs of proximity (i.e., IPPs) and when restricting attention to doubly-sublinear IPPs (ds-IPPs).
Alternatively, one may view this work as a subsequent step in the study of doubly-sublinear IPPs (of properties of functions), where we say that an IPP is doubly-sublinear if (1) the query complexity of the verifier is sublinear in the query complexity of testing the property, and (2) the query complexity of the honest prover is sublinear in the query complexity of learning a function in the property.
Specifically, we present doubly-sublinear IPPs for several natural location-invariant properties. Our results include:
\begin{itemize}
\item
We present doubly-sublinear IPPs for the set of functions from $[m]$ to $[n]$
in which each value occurs $m/n$ times:
For every $\alpha\in(0,0.5)$, the query complexity of the verifier is $O(n^{0.5-\alpha})$, and the query complexity of the honest prover is $\tildeO(n^{0.5+\alpha}/\eps^2)$.
\item
We present doubly-sublinear IPPs for the set of functions from $[m]$ to $[n]$ in which each value occurs either $m/k$ times or not at all:
For every $\alpha\in(0,1/3)$, the query complexity of the verifier is $\poly(1/\eps)\cdot k^{(2/3)-2\alpha}$, and the query complexity of the prover is $\poly(1/\eps)\cdot\tildeO(k^{(2/3)+\alpha})$.
\end{itemize}
In contrast, in both cases, it is known that the corresponding properties of distributions
have no doubly-sublinear IPP (see Herman and Rothblum, 2025).
Actually, the first property of distributions (i.e., uniformity over $[n]$) does not even have an IPP in which the verifier uses $o(n^{1/2})$ samples, regardless of other complexity measures.

[Read original post](https://eccc.weizmann.ac.il/report/2025/105)
