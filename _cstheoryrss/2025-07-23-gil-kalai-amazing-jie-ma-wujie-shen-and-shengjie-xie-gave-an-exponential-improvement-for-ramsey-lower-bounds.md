---
layout: post
category: cstheoryrss
title: "Gil Kalai: Amazing: Jie Ma, Wujie Shen, and Shengjie Xie Gave an Exponential Improvement for Ramsey Lower Bounds"
date: 2025-07-23T11:10:27
---

h/t Benny Sudakov

The Ramsey number *R(ℓ,k)* is the smallest integer *n* such that in any two-coloring of the edges of the complete graph on *n* vertices, ![K_n](https://s0.wp.com/latex.php?latex=K_n&bg=ffffff&fg=333333&s=0&c=20201002), by red and blue, there is either a red ![K_\ell](https://s0.wp.com/latex.php?latex=K_%5Cell&bg=ffffff&fg=333333&s=0&c=20201002) (a complete graph on *![\ell](https://s0.wp.com/latex.php?latex=%5Cell&bg=ffffff&fg=333333&s=0&c=20201002)* vertices with all edges colored red) or a blue ![K_k](https://s0.wp.com/latex.php?latex=K_k&bg=ffffff&fg=333333&s=0&c=20201002). Erdős’ original 1947 lower bound was obtained by coloring the edges of $K\_n$ at random: each edge is colored red with probability ![p](https://s0.wp.com/latex.php?latex=p&bg=ffffff&fg=333333&s=0&c=20201002) and blue otherwise. When ![k=C\ell](https://s0.wp.com/latex.php?latex=k%3DC%5Cell&bg=ffffff&fg=333333&s=0&c=20201002), the best known lower bound until a few days ago was due to Spencer (1975)—an improvement by a constant factor over Erdős’ original bound—using the Lovász Local Lemma.

A new paper on the arXiv represents an amazing progress

### [An exponential improvement for Ramsey lower bounds](https://arxiv.org/abs/2507.12926),

### by Jie Ma, Wujie Shen, and Shengjie Xie

> ***Abstract:** We prove a new lower bound on the Ramsey number ![r(\ell, C\ell)](https://s0.wp.com/latex.php?latex=r%28%5Cell%2C+C%5Cell%29&bg=ffffff&fg=333333&s=0&c=20201002) for any constant ![C > 1](https://s0.wp.com/latex.php?latex=C+%3E+1&bg=ffffff&fg=333333&s=0&c=20201002) and sufficiently large ![\ell](https://s0.wp.com/latex.php?latex=%5Cell&bg=ffffff&fg=333333&s=0&c=20201002), showing that there exists ![\epsilon=\epsilon(C)>0](https://s0.wp.com/latex.php?latex=%5Cepsilon%3D%5Cepsilon%28C%29%3E0&bg=ffffff&fg=333333&s=0&c=20201002) such that*
>
> *![\displaystyle r(\ell, C\ell) \geq \left(p_C^{-1/2} + \epsilon\right)^\ell,](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle+r%28%5Cell%2C+C%5Cell%29+%5Cgeq+%5Cleft%28p_C%5E%7B-1%2F2%7D+%2B+%5Cepsilon%5Cright%29%5E%5Cell%2C&bg=ffffff&fg=333333&s=0&c=20201002)*
>
> *where ![p_C \in (0, 1/2)](https://s0.wp.com/latex.php?latex=p_C+%5Cin+%280%2C+1%2F2%29&bg=ffffff&fg=333333&s=0&c=20201002) is the unique solution to ![C = \frac{\log p_C}{\log(1 - p_C)}](https://s0.wp.com/latex.php?latex=C+%3D+%5Cfrac%7B%5Clog+p_C%7D%7B%5Clog%281+-+p_C%29%7D&bg=ffffff&fg=333333&s=0&c=20201002). This provides the first exponential improvement over the classical lower bound obtained by Erdős in 1947.*

Before making a few comments on the new lower bounds, let me mention that there where several improvements over the years on the upper bound

![\displaystyle R(\ell,k) \le {{k+\ell-2} \choose {\ell-1}}](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle+R%28%5Cell%2Ck%29+%5Cle+%7B%7Bk%2B%5Cell-2%7D+%5Cchoose+%7B%5Cell-1%7D%7D&bg=ffffff&fg=333333&s=0&c=20201002),

and, most recently, exponential improvements were proved by Marcelo Campos, Simon Griffiths, Robert Morris, and Julian Sahasrabudhe. Further improvement and simplification were achieved in a paper by Paul Balister, Béla Bollobás, Marcelo Campos, Simon Griffiths, Eoin Hurley, Robert Morris, Julian Sahasrabudhe, and Marius Tiba. [See this post](https://gilkalai.wordpress.com/2023/03/16/some-news-from-a-seminar-in-cambridge/).

The paper by Jie Ma, Wujie Shen, and Shengjie Xie introduces and analyzes **geometric random models of graphs** that are of considerable independent interest. As the authors note, it remains open to find improvements when ![C=1](https://s0.wp.com/latex.php?latex=C%3D1&bg=ffffff&fg=333333&s=0&c=20201002).  It is interesting what is the situation when ![C \to 1](https://s0.wp.com/latex.php?latex=C+%5Cto+1&bg=ffffff&fg=333333&s=0&c=20201002) and how ![\epsilon](https://s0.wp.com/latex.php?latex=%5Cepsilon&bg=ffffff&fg=333333&s=0&c=20201002) depends on ![C](https://s0.wp.com/latex.php?latex=C&bg=ffffff&fg=333333&s=0&c=20201002). For ![C=1](https://s0.wp.com/latex.php?latex=C%3D1&bg=ffffff&fg=333333&s=0&c=20201002) is there any gain over the 1947 construction?

The random model considered in the paper is striking:

* Choose ![n](https://s0.wp.com/latex.php?latex=n&bg=ffffff&fg=333333&s=0&c=20201002) points at random on a ![d](https://s0.wp.com/latex.php?latex=d&bg=ffffff&fg=333333&s=0&c=20201002)-dimensional sphere.
* Set a threshold and color the edges between nearby points (those at distance below the threshold) blue or red, depending on which side of the threshold they fall.
* The threshold is chosen so that the probability an edge is red is ![p](https://s0.wp.com/latex.php?latex=p&bg=ffffff&fg=333333&s=0&c=20201002) (and thus the edge is blue with probability ![1-p](https://s0.wp.com/latex.php?latex=1-p&bg=ffffff&fg=333333&s=0&c=20201002)).

This is somewhat similar to the Erdős–Rényi model ![G(n,p)](https://s0.wp.com/latex.php?latex=G%28n%2Cp%29&bg=ffffff&fg=333333&s=0&c=20201002), but with additional subtle dependencies. It will be interesting to understand heuristically why these subtle dependencies cause the expected numbers (or just the probabilities) of large red and blue cliques to diminish compared to ![G(n,p)](https://s0.wp.com/latex.php?latex=G%28n%2Cp%29&bg=ffffff&fg=333333&s=0&c=20201002).

The paper’s crucial contribution lies in the involved analysis required to choose the dimension ![d](https://s0.wp.com/latex.php?latex=d&bg=ffffff&fg=333333&s=0&c=20201002) and compute the sizes of the largest red and blue cliques.

 Amazing!

[![](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/rsg.png?w=640)](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/rsg.png)

By Gil Kalai

[Read original post](https://gilkalai.wordpress.com/2025/07/23/amazing-jie-ma-wujie-shen-and-shengjie-xie-gave-an-exponential-improvement-for-ramsey-lower-bounds/)
