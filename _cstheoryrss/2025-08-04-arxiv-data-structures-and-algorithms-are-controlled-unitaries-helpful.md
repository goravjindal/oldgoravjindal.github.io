---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Are controlled unitaries helpful?"
date: 2025-08-04T00:00:00
---

**Authors:** [Ewin Tang](https://dblp.uni-trier.de/search?q=Ewin+Tang), [John Wright](https://dblp.uni-trier.de/search?q=John+Wright)

Many quantum algorithms, to compute some property of a unitary $U$, require
access not just to $U$, but to $cU$, the unitary with a control qubit. We show
that having access to $cU$ does not help for a large class of quantum problems.
For a quantum circuit which uses $cU$ and $cU^\dagger$ and outputs
$|\psi(U)\rangle$, we show how to ``decontrol'' the circuit into one which uses
only $U$ and $U^\dagger$ and outputs $|\psi(\varphi U)\rangle$ for a uniformly
random phase $\varphi$, with a small amount of time and space overhead. When we
only care about the output state up to a global phase on $U$, then the
decontrolled circuit suffices. Stated differently, $cU$ is only helpful because
it contains global phase information about $U$.
A version of our procedure is described in an appendix of Sheridan, Maslov,
and Mosca [SMM09]. Our goal with this work is to popularize this result by
generalizing it and investigating its implications, in order to counter
negative results in the literature which might lead one to believe that
decontrolling is not possible. As an application, we give a simple proof for
the existence of unitary ensembles which are pseudorandom under access to $U$,
$U^\dagger$, $cU$, and $cU^\dagger$.

[Read original post](http://arxiv.org/abs/2508.00055v1)
