---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Minimum-Peak-Cost Flows Over Time"
date: 2025-07-15T00:00:00
---

**Authors:** [Mariia Anapolska](https://dblp.uni-trier.de/search?q=Mariia+Anapolska), [Emma Ahrens](https://dblp.uni-trier.de/search?q=Emma+Ahrens), [Christina Büsing](https://dblp.uni-trier.de/search?q=Christina+B%C3%BCsing), [Felix Engelhardt](https://dblp.uni-trier.de/search?q=Felix+Engelhardt), [Timo Gersing](https://dblp.uni-trier.de/search?q=Timo+Gersing), [Corinna Mathwieser](https://dblp.uni-trier.de/search?q=Corinna+Mathwieser), [Sabrian Schmitz](https://dblp.uni-trier.de/search?q=Sabrian+Schmitz), [Sophia Wrede](https://dblp.uni-trier.de/search?q=Sophia+Wrede)

When planning transportation whose operation requires non-consumable
resources, the peak demand for allocated resources is often of higher interest
than the duration of resource usage. For instance, it is more cost-effective to
deliver parcels with a single truck over eight hours than to use two trucks for
four hours, as long as the time suffices. To model such scenarios, we introduce
the novel minimum peak cost flow over time problem, whose objective is to
minimise the maximum cost at all points in time rather than minimising the
integral of costs. We focus on minimising peak costs of temporally repeated
flows. These are desirable for practical applications due to their simple
structure. This yields the minimum-peak-cost Temporally Repeated flow problem
(MPC-TRF).
We show that the simple structure of temporally repeated flows comes with the
drawback of arbitrarily bad approximation ratios compared to general flows over
time. Furthermore, our complexity analysis shows the integral version of
MPC-TRF is strongly NP-hard, even under strong restrictions. On the positive
side, we identify two benign special cases: unit-cost series-parallel networks
and networks with time horizon at least twice as long as the longest path in
the network (with respect to the transit time). In both cases, we show that
integral optimal flows if the desired flow value equals the maximum flow value
and fractional optimal flows for arbitrary flow values can be found in
polynomial time. For each of these cases, we provide an explicit algorithm that
constructs an optimal solution.

[Read original post](http://arxiv.org/abs/2507.09688v1)
