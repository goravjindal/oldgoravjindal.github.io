---
layout: post
title: Checking if a polynomial has real roots
date: 2023-06-13 11:12:00-0400
description:  Checking if a polynomial has real roots
tags: math
related_posts: false
---
This theme supports rendering beautiful math in inline and display modes using [MathJax 3](https://www.mathjax.org/) engine. You just need to surround your math expression with `$$`, like `$$ E = mc^2 $$`. If you leave it inside a paragraph, it will produce an inline expression, just like $$ E = mc^2 $$.

To use display mode, again surround your expression with `$$` and place it as a separate paragraph. Here is an example:

$$
\sum_{k=1}^\infty |\langle x, e_k \rangle|^2 \leq \|x\|^2
$$

You can also use `\begin{equation}...\end{equation}` instead of `$$` for display mode math.
MathJax will automatically number equations:

\begin{equation}
\label{eq:cauchy-schwarz}
\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
\end{equation}

and by adding `\label{...}` inside the equation environment, we can now refer to the equation using `\eqref`.

Note that MathJax 3 is [a major re-write of MathJax](https://docs.mathjax.org/en/latest/upgrading/whats-new-3.0.html) that brought a significant improvement to the loading and rendering speed, which is now [on par with KaTeX](http://www.intmath.com/cg5/katex-mathjax-comparison.php).

The following definition of "Discrimination Matrix" is little different
from the wellknown resultant matrix of $f(x)$ and $f^{\prime}(x)$.

Given a polynomial with general symbolic coefficients,
$$f(x)=a_{0}x^{n}+a_{1}x^{n-1}+\ldots+a_{n},$$ the following
$(2n+1)\times(2n+1)$ matrix in terms of the coefficients,
$$\left[\begin{array}{ccccccccc}
a_{0} & a_{1} & a_{2} & \cdots & a_{n}\\
0 & na_{0} & (n-1)a_{1} & \cdots & a_{n-1}\\
 & a_{0} & a_{1} & \cdots & a_{n-1} & a_{n}\\
 & 0 & na_{0} & \cdots & 2a_{n-2} & a_{n-1}\\
 &  &  & \cdots & \cdots\\
 &  &  & \cdots & \cdots\\
 &  &  &  & a_{0} & a_{1} & \cdots & a_{n}\\
 &  &  &  & 0 & na_{0} & \cdots & a_{n-1}\\
 &  &  &  &  & a_{0} & a_{1} & \cdots & a_{n}
\end{array}\right]$$ is called the discrimination matrix of $f(x)$, and
denoted by $$\operatorname{Discr}(f)$$.

By $d_{k}$ or $d_{k}(f)$ denote the determinant of the submatrix of
$\operatorname{Discr}(f)$ formed by the first $k$ rows and the first $k$
columns, for $k=1,\ldots,2n+1$. The principal minor sequence of the
discrimination matrix, $$\left\{ d_{1},d_{2},\ldots,d_{2n+1}\right\}$$
plays a very important role in this paper.

Let $D_{k}=d_{2k}$ for $k=1,\ldots,n$. We called the $n$-tuple
$$\left\{ D_{1},D_{2},\ldots,D_{n}\right\}$$ the discriminant sequence
of polynomial $f(x)$.
