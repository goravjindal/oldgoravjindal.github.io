---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Counting Distinct Square Substrings in Sublinear Time"
date: 2025-08-07T00:00:00
---

**Authors:** [Panagiotis Charalampopoulos](https://dblp.uni-trier.de/search?q=Panagiotis+Charalampopoulos), [Manal Mohamed](https://dblp.uni-trier.de/search?q=Manal+Mohamed), [Jakub Radoszewski](https://dblp.uni-trier.de/search?q=Jakub+Radoszewski), [Wojciech Rytter](https://dblp.uni-trier.de/search?q=Wojciech+Rytter), [Tomasz Waleń](https://dblp.uni-trier.de/search?q=Tomasz+Wale%C5%84), [Wiktor Zuba](https://dblp.uni-trier.de/search?q=Wiktor+Zuba)

We show that the number of distinct squares in a packed string of length $n$
over an alphabet of size $\sigma$ can be computed in $O(n/\log\_\sigma n)$ time
in the word-RAM model. This paper is the first to introduce a sublinear-time
algorithm for counting squares in the packed setting. The packed representation
of a string of length $n$ over an alphabet of size $\sigma$ is given as a
sequence of $O(n/\log\_\sigma n)$ machine words in the word-RAM model (a machine
word consists of $\omega \ge \log\_2 n$ bits). Previously, it was known how to
count distinct squares in $O(n)$ time [Gusfield and Stoye, JCSS 2004], even for
a string over an integer alphabet [Crochemore et al., TCS 2014; Bannai et al.,
CPM 2017; Charalampopoulos et al., SPIRE 2020]. We use the techniques for
extracting squares from runs described by Crochemore et al. [TCS 2014].
However, the packed model requires novel approaches.
We need an $O(n/\log\_\sigma n)$-sized representation of all long-period runs
(runs with period $\Omega(\log\_\sigma n)$) which allows for a sublinear-time
counting of the -- potentially linearly-many -- implied squares. The
long-period runs with a string period that is periodic itself (called layer
runs) are an obstacle, since their number can be $\Omega(n)$. The number of all
other long-period runs is $O(n/\log\_\sigma n)$ and we can construct an implicit
representation of all long-period runs in $O(n/\log\_\sigma n)$ time by
leveraging the insights of Amir et al. [ESA 2019]. We count squares in layer
runs by exploiting combinatorial properties of pyramidally-shaped groups of
layer runs. Another difficulty lies in computing the locations of Lyndon roots
of runs in packed strings, which is needed for grouping runs that may generate
equal squares. To overcome this difficulty, we introduce sparse-Lyndon roots
which are based on string synchronizers [Kempa and Kociumaka, STOC 2019].

[Read original post](http://arxiv.org/abs/2508.03930v1)
