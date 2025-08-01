---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Online Combinatorial Allocation with Interdependent Values"
date: 2025-08-01T00:00:00
---

**Authors:** [Michal Feldman](https://dblp.uni-trier.de/search?q=Michal+Feldman), [Simon Mauras](https://dblp.uni-trier.de/search?q=Simon+Mauras), [Divyarthi Mohan](https://dblp.uni-trier.de/search?q=Divyarthi+Mohan), [Rebecca Reiffenhäuser](https://dblp.uni-trier.de/search?q=Rebecca+Reiffenh%C3%A4user)

We study online combinatorial allocation problems in the secretary setting,
under interdependent values. In the interdependent model, introduced by Milgrom
and Weber (1982), each agent possesses a private signal that captures her
information about an item for sale, and the value of every agent depends on the
signals held by all agents. Mauras, Mohan, and Reiffenh\"auser (2024) were the
first to study interdependent values in online settings, providing
constant-approximation guarantees for secretary settings, where agents arrive
online along with their signals and values, and the goal is to select the agent
with the highest value.
In this work, we extend this framework to {\em combinatorial} secretary
problems, where agents have interdependent valuations over {\em bundles} of
items, introducing additional challenges due to both combinatorial structure
and interdependence. We provide $2e$-competitive algorithms for a broad class
of valuation functions, including submodular and XOS functions, matching the
approximation guarantees in the single-choice secretary setting. Furthermore,
our results cover the same range of valuation classes for which constant-factor
algorithms exist in classical (non-interdependent) secretary settings, while
incurring only an additional factor of $2$ due to interdependence. Finally, we
extend our study to strategic settings, and provide a $4e$-competitive truthful
mechanism for online bipartite matching with interdependent valuations, again
meeting the frontier of what is known, even without interdependence.

[Read original post](http://arxiv.org/abs/2507.23500v1)
