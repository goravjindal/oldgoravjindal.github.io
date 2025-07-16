---
layout: post
category: cstheoryrss
title: "arXiv: Computational Geometry: Bicriteria Polygon Aggregation with Arbitrary Shapes"
date: 2025-07-16T00:00:00
---

**Authors:** [Lotte Blank](https://dblp.uni-trier.de/search?q=Lotte+Blank), [David Eppstein](https://dblp.uni-trier.de/search?q=David+Eppstein), [Jan-Henrik Haunert](https://dblp.uni-trier.de/search?q=Jan-Henrik+Haunert), [Herman Haverkort](https://dblp.uni-trier.de/search?q=Herman+Haverkort), [Benedikt Kolbe](https://dblp.uni-trier.de/search?q=Benedikt+Kolbe), [Philip Mayer](https://dblp.uni-trier.de/search?q=Philip+Mayer), [Petra Mutzel](https://dblp.uni-trier.de/search?q=Petra+Mutzel), [Alexander Naumann](https://dblp.uni-trier.de/search?q=Alexander+Naumann), [Jonas Sauer](https://dblp.uni-trier.de/search?q=Jonas+Sauer)

We study the problem of aggregating polygons by covering them with disjoint
representative regions, thereby inducing a clustering of the polygons. Our
objective is to minimize a weighted sum of the total area and the total
perimeter of the regions. This problem has applications in cartographic map
generalization and urban analytics. Here, the polygons represent building
footprints and the clusters may represent urban areas. Previous approaches
forced the boundaries of the regions to come from a fixed subdivision of the
plane, which allows the optimal solution (restricted in this way) to be found
from a minimum cut in a dual graph. It is natural to ask whether the problem
can still be solved efficiently if this restriction is removed, allowing output
regions to be bounded by arbitrary curves. We provide a positive answer in the
form of a polynomial-time algorithm. Additionally, we fully characterize the
optimal solutions by showing that their boundaries are composed of input
polygon edges and circular arcs of constant radius. Since some applications
favor straight edges, we also study two problem variants in which the output
regions must be polygons, but are not restricted to have boundaries from a
fixed subdivision. In the first variant, region vertices must lie on the
boundaries of the input polygons. The second variant requires them to be
vertices of the input polygons. We show that both variants can be approximated
up to a constant factor in polynomial time by altering an optimal solution for
the unrestricted problem. Our experimental evaluation on real-world building
footprints demonstrates that these approximate solutions are visually similar
to the optimal unrestricted ones and achieve near-optimal objective values.

[Read original post](http://arxiv.org/abs/2507.11212v1)
