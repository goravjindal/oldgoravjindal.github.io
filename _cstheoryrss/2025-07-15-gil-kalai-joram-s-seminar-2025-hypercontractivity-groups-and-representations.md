---
layout: post
category: cstheoryrss
title: "Gil Kalai: Jorams seminar 2025: Hypercontractivity, Groups and Representations"
date: 2025-07-15T15:34:21
---

### Joram’s seminar 2025

Here is my summary of the recent Joram’s seminar that took place on July 9 and 10 in Jerusalem. Much of the seminar was about the the paper [Product Mixing in Compact Lie Groups](https://arxiv.org/abs/2401.15456) by David Ellis, Guy Kindler, Noam Lifshitz, and Dor Minzer.

## Lecture I: Noam Lifshitz

[![](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/screenshot_20250710_074320_gallery.jpg?w=640)](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/screenshot_20250710_074320_gallery.jpg)

Noam Lifshitz (HUJI): Product mixing in groups (Special Colloquium)

**Abstract:** Let ![A, B, C](https://s0.wp.com/latex.php?latex=A%2C+B%2C+C&bg=ffffff&fg=333333&s=0&c=20201002) be subsets of the special unitary group ![SU(n)](https://s0.wp.com/latex.php?latex=SU%28n%29&bg=ffffff&fg=333333&s=0&c=20201002) of Haar measure ![\ge e^{-n^{1/3}}](https://s0.wp.com/latex.php?latex=%5Cge+e%5E%7B-n%5E%7B1%2F3%7D%7D&bg=ffffff&fg=333333&s=0&c=20201002). Then ![ABC = SU(n)](https://s0.wp.com/latex.php?latex=ABC+%3D+SU%28n%29&bg=ffffff&fg=333333&s=0&c=20201002). In fact, the product ![abc](https://s0.wp.com/latex.php?latex=abc&bg=ffffff&fg=333333&s=0&c=20201002) of random elements ![a \sim A,b\sim B, c\sim C](https://s0.wp.com/latex.php?latex=a+%5Csim+A%2Cb%5Csim+B%2C+c%5Csim+C&bg=ffffff&fg=333333&s=0&c=20201002) is equidistributed in ![SU(n).](https://s0.wp.com/latex.php?latex=SU%28n%29.&bg=ffffff&fg=333333&s=0&c=20201002) This makes progress on a question that was posed independently by Gowers studying nonabelian variants of questions from additive combinatorics and settles a conjecture of physicists studying quantum communication complexity. To prove our results we introduce a tool known as ‘hypercontractivity’ to the study of high rank compact Lie groups. We then show that it synergies with their representation theory to obtain our result.

My summary

### The Babai–Sós Problem

In 1985, László Babai and Vera Sós posed the following question: *What is the largest possible size of a product-free subset of a finite group ![G](https://s0.wp.com/latex.php?latex=G&bg=ffffff&fg=333333&s=0&c=20201002)?*

For abelian groups, one can always find a sum-free set of positive density. However, the situation in the non-commutative case is quite different—and turns out to be very interesting.

### Gowers’ Work and the Sarnak–Xue–Gowers Lemma

In his 2008 paper [quasirandom groups](https://arxiv.org/abs/0710.3877), Tim Gowers proved that if the dimension of the smallest non-trivial representation of a finite group is ![D](https://s0.wp.com/latex.php?latex=D&bg=ffffff&fg=333333&s=0&c=20201002), then any product-free subset has density at most ![cD^{-1/3}](https://s0.wp.com/latex.php?latex=cD%5E%7B-1%2F3%7D&bg=ffffff&fg=333333&s=0&c=20201002) for some constant ![c](https://s0.wp.com/latex.php?latex=c&bg=ffffff&fg=333333&s=0&c=20201002).   
Gowers also obtained an analogous result for compact Lie groups, showing that the Haar measure of a product-free set is similarly bounded. For example, for the group ![SU(n)](https://s0.wp.com/latex.php?latex=SU%28n%29&bg=ffffff&fg=333333&s=0&c=20201002), any product-free set has measure at most ![O(n^{-1/3})](https://s0.wp.com/latex.php?latex=O%28n%5E%7B-1%2F3%7D%29&bg=ffffff&fg=333333&s=0&c=20201002).

Gowers’ argument relies (among other things) on ideas reminiscent of a 1991 result by Sarnak and Xue, which established a beautiful connection between spectral gaps and the dimensions of irreducible representations.

### “Gowers’s enemies are low dimensional representation”

Improving on Gowers’ bound requires a more refined analysis of characteristic functions of sets, made possible by hypercontractive estimates. Hypercontractivity enables one to strengthen the upper bound for product-free sets from ![\displaystyle n^{-1/3}](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle+n%5E%7B-1%2F3%7D&bg=ffffff&fg=333333&s=0&c=20201002) to ![\displaystyle e^{-n^{1/3}}](https://s0.wp.com/latex.php?latex=%5Cdisplaystyle+e%5E%7B-n%5E%7B1%2F3%7D%7D&bg=ffffff&fg=333333&s=0&c=20201002). Further improvements might still be achievable—an intriguing open direction. However, for the stronger statement concerning the equidistribution of products, this new bound is sharp.

### One Clean Qubit Suffices

Noam also described a related problem in quantum communication complexity, which was resolved using similar methods. This result appears in the paper [*One Clean Qubit Suffices for Quantum Communication Advantage*](https://arxiv.org/abs/2310.02406) by Srinivasan Arunachalam, Uma Girish, and Noam Lifshitz.

### Hypercontractivity

Noam concluded his talk by highlighting hypercontractivity—the key new ingredient in this line of work—and the associated ![d](https://s0.wp.com/latex.php?latex=d&bg=ffffff&fg=333333&s=0&c=20201002)-level inequalities. The proof of the main theorem, to be developed over four additional lectures, combines representation theory for ![SU(n)](https://s0.wp.com/latex.php?latex=SU%28n%29&bg=ffffff&fg=333333&s=0&c=20201002) with the establishment and use of hypercontractive estimates.

[![](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/20250709_170544.jpg?w=640)](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/20250709_170544.jpg)

## Lecture II: Dor Minzer

Dor Minzer (MIT): On CSPs, Inverse Theorems and Friends

**Abstract:** Constraint satisfaction problems (CSPs in short) are among the most important computational problems studied in Theoretical Computer Science. In this talk we will discuss a recent line of study addressing the complexity of approximating satisfiable instances of CSPs.  
We will focus on connections to analytic inverse-type theorems for correlations that generalize the ![U_2](https://s0.wp.com/latex.php?latex=U_2&bg=ffffff&fg=333333&s=0&c=20201002)-Gowers norm, and show how these results can be used in other areas, such as property testing and extremal combinatorics.

Based mostly on joint works with Amey Bhangale, Subhash Khot and Yang P. Liu.

My summary:

### CSPs and the difference between 3LIN and 3SAT

It is NP-hard to find a satisfying assignment for a 3-SAT instance—and even to satisfy a large fraction of clauses when a perfect assignment exists. The case of 3-LIN (systems of linear equations mod 2 with three variables per equation) is very different: here it is easy to find a satisfying assignment, but hard to find an assignment that satisfies *many* equations.

Both problems fall under the general framework of **constraint satisfaction problems (CSPs)**. Understanding the source of this difference is a deep and challenging question in computational complexity.

Amey Bhangale, Subhash Khot, and Dor Minzer (recently joined by Yang P. Liu) have written a remarkable series of (so far) seven papers developing a theory to address this question; Here is a link to [On Approximability of Satisfiable k-CSPs:VII](https://arxiv.org/abs/2411.15136).  As it turns out, combinatorial objects like **combinatorial lines** are special cases of a much broader family of structures arising from CSPs. This connection works both ways:

* The general theory applies to long-standing problems in additive combinatorics.
* At the same time, advances in additive combinatorics—via more sophisticated mathematical tools—feed back into the general CSP theory.

### Better Bounds for Density Hales–Jewett

Dor highlighted a striking application of this theory (we already mentioned it in this post):

[Reasonable Bounds for Combinatorial Lines of Length Three,](https://arxiv.org/abs/2411.15137) by Amey Bhangale, Subhash Khot, Yang P. Liu, Dor Minzer

The paper proves that any subset ![A \subseteq [3]^n](https://s0.wp.com/latex.php?latex=A+%5Csubseteq+%5B3%5D%5En&bg=ffffff&fg=333333&s=0&c=20201002) with ![3^{-n}|A| \ge (\log \log \log \log n)^{-c}](https://s0.wp.com/latex.php?latex=3%5E%7B-n%7D%7CA%7C+%5Cge+%28%5Clog+%5Clog+%5Clog+%5Clog+n%29%5E%7B-c%7D&bg=ffffff&fg=333333&s=0&c=20201002)  contains a combinatorial line of length 3. This dramatically improves on the previous best bound of ![3^{-n}|A|\ge \Omega ((\log ^*n)^{-1/2})](https://s0.wp.com/latex.php?latex=3%5E%7B-n%7D%7CA%7C%5Cge+%5COmega+%28%28%5Clog+%5E%2An%29%5E%7B-1%2F2%7D%29&bg=ffffff&fg=333333&s=0&c=20201002)  of [D.H.J. Polymath, [Ann. of Math. 2012](https://annals.math.princeton.edu/2012/175-3/p06)] (DHJ[3] was the goal of the first [polymath project.](https://gowers.wordpress.com/category/polymath1/))

Dor also mentioned general algebraic norms in this theory, reminiscent of Gowers norms, as well as inverse theorems for these new norms.

[![](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/20250710_092905.jpg?w=640)](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/20250710_092905.jpg)

## Lecture III: Nathan Keller

Nathan Keller (BIU): Intersection theorems and improved covering results for the symmetric group, via hypercontractivity

In this talk we describe two seemingly unrelated results on the symmetric group ![S_n](https://s0.wp.com/latex.php?latex=S_n&bg=ffffff&fg=333333&s=0&c=20201002).  
A family ![F](https://s0.wp.com/latex.php?latex=F&bg=ffffff&fg=333333&s=0&c=20201002) of permutations is called *t*-intersecting if any two permutations in *F* agree on at least *t* values. In 1977, Deza and Frankl conjectured that for all ![n>n_o(t)](https://s0.wp.com/latex.php?latex=n%3En_o%28t%29&bg=ffffff&fg=333333&s=0&c=20201002) , the maximal size of a *t*-intersecting subfamily of S\_n is (n-t)!. Ellis, Friedgut and Pilpel (JAMS, 2011) proved the conjecture for all  *n>exp(exp(t))* and conjectured that it holds for all *n>2t*. We prove that the conjecture holds for all *n>ct* for some constant *c*.

A well-known problem asks for characterizing subsets *A* of ![S_n](https://s0.wp.com/latex.php?latex=S_n&bg=ffffff&fg=333333&s=0&c=20201002) whose square ![A^2](https://s0.wp.com/latex.php?latex=A%5E2&bg=ffffff&fg=333333&s=0&c=20201002) contains (=”covers”) the alternating group ![A_n](https://s0.wp.com/latex.php?latex=A_n&bg=ffffff&fg=333333&s=0&c=20201002). We show that if *A* is a union of conjugacy classes of density at least ![exp(-n^{2/5-\epsilon})](https://s0.wp.com/latex.php?latex=exp%28-n%5E%7B2%2F5-%5Cepsilon%7D%29&bg=ffffff&fg=333333&s=0&c=20201002) then ![A^2](https://s0.wp.com/latex.php?latex=A%5E2&bg=ffffff&fg=333333&s=0&c=20201002) covers ![A_n.](https://s0.wp.com/latex.php?latex=A_n.&bg=ffffff&fg=333333&s=0&c=20201002) This extends a seminal result of Larsen and Shalev (Inventiones Math., 2008) who obtained the same with 1/4 in the double exponent.

The two results boil down to the understanding of independent sets in certain Cayley graphs, and turn out to be related. We shall focus on the main new tool we use in the proof of both results – hypercontractive inequalities for global functions, developed by Keevash, Lifshitz, Long and Minzer (JAMS, 2024).

The talk was based on joint works with Noam Lifshitz, Dor Minzer, and Ohad Sheinfeld.

Nathan’s talk is based on these two papers:

[Improved covering results for conjugacy classes of symmetric groups via hypercontractivity](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/improved-covering-results-for-conjugacy-classes-of-symmetric-groups-via-hypercontractivity/ED9440FB38271646948AAC96D95251F7), by Nathan Keller, Noam Lifshitz, and Ohad Sheinfeld

[On t-intersecting families of permutations](https://www.sciencedirect.com/science/article/pii/S0001870824001658?casa_token=cMVyV_Badx4AAAAA:2iXURvUaFO2srOo1A09DNUwRhQdVIJ1ijxtbMfc4mZXFrJuoXHccj5NLShMIZyNOaLJPcIAZFA) by Nathan Keller, Noam Lifshitz, and Ohad Sheinfeld

Nathan explained how Erdős–Ko–Rado-type problems about permutations in combinatorics and problems about products of conjugacy classes in group theory can both be formulated in terms of combinatorial properties of Cayley graphs of normal subsets (unions of conjugacy classes) in groups. (This explanation was quite stunning for me.) He then outlined how **hypercontractive inequalities for global functions**— (that we mentioned [here](https://gilkalai.wordpress.com/2020/05/08/to-cheer-you-up-in-difficult-times-3-a-guest-post-by-noam-lifshitz-on-the-new-hypercontractivity-inequality-of-peter-keevash-noam-lifshitz-eoin-long-and-dor-minzer/) and [here](https://gilkalai.wordpress.com/2020/07/24/noam-lifshitz-a-new-hypercontractivity-inequality-the-proof/)) yield major advances in both of these areas.  We discussed Ellis, Friedgut and Pilpel’s Erdős–Ko–Rado result for permutations in [this 2009 post](https://gilkalai.wordpress.com/2009/03/13/extremal-combinatorics-on-permutations/).

## 

## Lectures IV,V,VI,VII: Guy Kindler and Noam Lifshitz

Hypercontractivity and product mixing in compact Lie groups (Four lectures)  Guy Kindler (HUJI) and Noam Lifshitz (HUJI)

**Abstract:** The study of geometric properties of Cayley graphs associated with non-abelian groups is a rich area of research with wide ranging applications. Here, key questions concern properties such as expansion, mixing, diameter, etc. While remarkable progress was made in this area by applying deep results in character theory, such methods seem to be limited to the case of normal Cayley graphs (those generated by unions of conjugacy classes).

In this mini-course we explore a recent approach which seems to sidestep such limitations. Inspired by techniques originally introduced in the study of the (abelian) Boolean Cube, we use a synergy between hypercontractive inequalities and dimensional lower bounds from representation theory to make progress on various problems. In particular, we will present a significant improvement of a bound of Gowers on the measure of product-free subsets in the unitary group SU(n).

My comments: I will not give a detailed summary of the lectures by Guy and Noam. They described a subtle coupling method to prove hypercontractivity  for ![SU(n)](https://s0.wp.com/latex.php?latex=SU%28n%29&bg=ffffff&fg=333333&s=0&c=20201002) and mentioned another method based on curvature. They got quite deeply into the representation theory of SU(n) and mentioned notions of “degree” (analogous to “Juntas” for Boolean functions) that plays a role. Related notions appeared in works of Shamgar Gurevich and  Roger Howe (e.g. [this paper](https://arxiv.org/pdf/2105.12369)) and of Bob Guralnik, Michael Larsen, and Pham Huu Tiep (e.g., [this paper](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/character-levels-and-character-bounds/77A6CCCB36F94337FD1DAA7F67B40379)). The proof presented by Noam for bounding the eigenvalues was actually a simplification discovered right before the lecture!

## More

[![](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/screenshot_20250709_200312_whatsapp.jpg?w=473)](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/screenshot_20250709_200312_whatsapp.jpg)

### On Joram

Elon Lindenstrauss shared a few moving words about his father, emphasizing Joram’s deep commitment to the Israeli mathematical community. The format of Joram’s seminar—aiming not only to present high-level ideas but also to dive into the gory details of major mathematical advances—was something he greatly valued.

I vividly recall a seminar Joram organized back in 1981 on the newly published book by Gromov, *Structures métriques pour les variétés riemanniennes*.

(See also [this post](https://gilkalai.wordpress.com/2013/05/29/jorams-memorial-conference/) about Joram Lindenstrauss. Here is a link to [previous seminars](https://mathematics.huji.ac.il/joram-seminar-0) in the series.)

[![](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/20250428_110742.jpg?w=640)](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/20250428_110742.jpg)

### David Ellis

The fourth author of the paper, our dear friend David Ellis, visited Jerusalem in May.

### Videoes

Videoes for the lectures are [Lecture 1](https://huji.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=ba316395-bf51-4ae1-a804-b315009cac8f), [lecture 2](https://huji.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=0d297cf2-4af7-4960-9341-b315009d7191), [lecture 3](https://huji.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=08d4df2b-ad51-460c-b7e3-b315009e079d), [lecture 4](https://huji.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=0bbe7d4a-071b-4999-babd-b315009e9080), [lecture 5](https://huji.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=9ea8f90d-dcac-4b7e-be50-b315009f0933), [lecture 6](https://huji.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=cca90b8e-0f8f-4c2c-9cce-b315009fe933), [lecture 7](https://huji.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=e939ce08-ffc5-4f80-a6e8-b31500a099b2). (The links may not be stable).

### Kazhdan’s seminar on hypercontractivity – Spring 2026

Back in 2003–2004, David Kazhdan and I ran a seminar on **polytopes, toric varieties**, and related topics in combinatorics and algebra. (Much has happened since then—Karim Adiprasito even organized another Kazhdan seminar on a related theme in 2018.)

In 2012, David and I thought it might be time to run a similar event in 2014 and perhaps start a tradition of a decennial joint seminar. This plan materialized only in 2019 when Leonid Polterovich, Dorit Aharonov, Guy Kindler, Michael Ben-Or, and I dedicated one of David’s Sunday seminars to **computation, quantumness, symplectic geometry, and information**.   
  
Now, we’re planning a **Kazhdan seminar on hypercontractivity** for **Spring 2026**. Since many of Kazhdan’s seminars focus on representation theory, the new connections between hypercontractivity and representations make this an especially natural fit.

### Plans for my blog

I have plenty of material I’d love to share—from the Combinatorial Colloquium in London, the events of the Czech Learned Society in Prague, and several lectures and meetings in Israel. This summary of the very recent Joram seminar does *not* mean I’ve abandoned plans to write about earlier events. Stay tuned!

### High-degree representations and physics.

It is an interesting (meta) question why representations that occur in particle physics are (very) low dimensional. Is the Sarnak-Xue lemma related to this phenomenon?

By Gil Kalai

[Read original post](https://gilkalai.wordpress.com/2025/07/15/jorams-seminar-2025-hypercontractivity-groups-and-representations/)
