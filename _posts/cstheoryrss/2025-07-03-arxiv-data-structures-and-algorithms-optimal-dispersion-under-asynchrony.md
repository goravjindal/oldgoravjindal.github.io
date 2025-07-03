---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Optimal Dispersion Under Asynchrony"
date: 2025-07-03T00:00:00
---

**Authors:** [Debasish Pattanayak](https://dblp.uni-trier.de/search?q=Debasish+Pattanayak), [Ajay D. Kshemkalyani](https://dblp.uni-trier.de/search?q=Ajay+D.+Kshemkalyani), [Manish Kumar](https://dblp.uni-trier.de/search?q=Manish+Kumar), [Anisur Rahaman Molla](https://dblp.uni-trier.de/search?q=Anisur+Rahaman+Molla), [Gokarna Sharma](https://dblp.uni-trier.de/search?q=Gokarna+Sharma)

We study the dispersion problem in anonymous port-labeled graphs: $k \leq n$
mobile agents, each with a unique ID and initially located arbitrarily on the
nodes of an $n$-node graph with maximum degree $\Delta$, must autonomously
relocate so that no node hosts more than one agent. Dispersion serves as a
fundamental task in distributed computing of mobile agents, and its complexity
stems from key challenges in local coordination under anonymity and limited
memory.
The goal is to minimize both the time to achieve dispersion and the memory
required per agent. It is known that any algorithm requires $\Omega(k)$ time in
the worst case, and $\Omega(\log k)$ bits of memory per agent. A recent result
[SPAA'25] gives an optimal $O(k)$-time algorithm in the synchronous setting and
an $O(k \log k)$-time algorithm in the asynchronous setting, both using
$O(\log(k+\Delta))$ bits.
In this paper, we close the complexity gap in the asynchronous setting by
presenting the first dispersion algorithm that runs in optimal $O(k)$ time
using $O(\log(k+\Delta))$ bits of memory per agent. Our solution is based on a
novel technique we develop in this paper that constructs a port-one tree in
anonymous graphs, which may be of independent interest.