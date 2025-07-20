---
layout: post
category: cstheoryrss
title: "ECCC Papers: TR25-089 | Chain Rules for Time-Bounded Kolmogorov Complexity |"
date: 2025-07-09T22:47:16
---

Time-bounded conditional Kolmogorov complexity of a string $x$ given $y$, $K^t(x\mid y)$, is the length of a shortest program that, given $y$, prints $x$ within $t$ steps. The Chain Rule for conditional $K^t$ with error $e$ is the following hypothesis: there is a constant $c\in\mathbb{N}$ such that, for any strings $y,x\_1,\dots,x\_{\ell}\in\{0,1\}^\*$, for any $\ell\in\mathbb{N}$, and all sufficiently large time bounds $t$,
\[
K^t(x\_1,\dots,x\_{\ell}\mid y) \geq \sum\_{i=1}^{\ell} K^{t^{c}}(x\_i \mid y, x\_1,\dots,x\_{i-1}) - \ell\cdot O(\log t) -e(N,t),
\]
where $N=\sum\_{i=1}^{\ell} |x\_i|$.
We pinpoint the complexity assumptions equivalent to Chain Rules for conditional $K^t$, and the probabilistic variant $pK^t$, where $pK^t(x\mid y)\leq s$ iff $K^t(x\mid y,r)\leq s$ for at least $2/3$ of random strings $r\in\{0,1\}^t$.
1. Chain Rule for conditional $K^t$ with error $e(N,t)\leq o(N)$ is equivalent to the conjunction of the following two statements:
(a) $E\not\subset io SIZE[2^{o(n)}]$, and
(b) $Gap McK^tP\in promise\text{-} P$, where $Gap McK^tP$ is a promise problem to distinguish between inputs $(x,y,1^s)$ with $K^t(x\mid y)\leq s$ and those with $K^{poly(t)}(x\mid y)> s + o(|x|)$.
2. Chain Rule for conditional $pK^t$ with error $e(N,t)\leq o(N)$ is equivalent to $Gap McpK^tP\in promise\text{-} BPP$, for the analog of $Gap McK^tP$ for conditional $pK^t$.
These are the first exact complexity characterizations for natural versions of Chain Rules for time-bounded Kolmogorov complexity.
Assuming $Gap McK^tP$ is $NP$-hard (which is true under cryptographic assumptions [Huang et al., STOC'23]), the equivalence above would simplify to ``the Chain Rule for conditional $K^t$ with error $e(N,t)\leq o(N)$ holds iff $NP=P$''. That is, under a plausible $NP$-hardness assumption for $Gap McK^tP$, we would get that proving $P\neq NP$ is equivalent to disproving the Chain Rule for conditional $K^t$.
Among other results, we present a natural $promise\text{-} BPP$-complete problem based on the problem of approximating $pK^t(x\mid y)$ for short inputs $x$ with $|x|\leq \log t$, and give some algorithmic consequences if $Gap McpK^TP$ were easy.

[Read original post](https://eccc.weizmann.ac.il/report/2025/089)
