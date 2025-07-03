---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Moving Matter: Using a Single, Simple Robot to Reconfigure a Connected
  Set of Building Blocks"
date: 2025-07-01T00:00:00
---

**Authors:** [Javier Garcia](https://dblp.uni-trier.de/search?q=Javier+Garcia), [Jonas Friemel](https://dblp.uni-trier.de/search?q=Jonas+Friemel), [Ramin Kosfeld](https://dblp.uni-trier.de/search?q=Ramin+Kosfeld), [Michael Yannuzzi](https://dblp.uni-trier.de/search?q=Michael+Yannuzzi), [Peter Kramer](https://dblp.uni-trier.de/search?q=Peter+Kramer), [Christian Rieck](https://dblp.uni-trier.de/search?q=Christian+Rieck), [Christian Scheffer](https://dblp.uni-trier.de/search?q=Christian+Scheffer), [Arne Schmidt](https://dblp.uni-trier.de/search?q=Arne+Schmidt), [Harm Kube](https://dblp.uni-trier.de/search?q=Harm+Kube), [Dan Biediger](https://dblp.uni-trier.de/search?q=Dan+Biediger), [Sándor P. Fekete](https://dblp.uni-trier.de/search?q=S%C3%A1ndor+P.+Fekete), [Aaron T. Becker](https://dblp.uni-trier.de/search?q=Aaron+T.+Becker)

We implement and evaluate different methods for the reconfiguration of a
connected arrangement of tiles into a desired target shape, using a single
active robot that can move along the tile structure. This robot can pick up,
carry, or drop off one tile at a time, but it must maintain a single connected
configuration at all times.
Becker et al. (CCCG 2025) recently proposed an algorithm that uses histograms
as canonical intermediate configurations, guaranteeing performance within a
constant factor of the optimal solution if the start and target configuration
are well-separated. We implement and evaluate this algorithm, both in a
simulated and practical setting, using an inchworm type robot to compare it
with two existing heuristic algorithms.