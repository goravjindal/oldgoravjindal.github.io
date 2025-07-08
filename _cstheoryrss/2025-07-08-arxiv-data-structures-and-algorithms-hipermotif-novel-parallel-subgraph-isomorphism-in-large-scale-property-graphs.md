---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: HiPerMotif: Novel Parallel Subgraph Isomorphism in Large-Scale Property
  Graphs"
date: 2025-07-08T00:00:00
---

**Authors:** [Mohammad Dindoost](https://dblp.uni-trier.de/search?q=Mohammad+Dindoost), [Oliver Alvarado Rodriguez](https://dblp.uni-trier.de/search?q=Oliver+Alvarado+Rodriguez), [Bartosz Bryg](https://dblp.uni-trier.de/search?q=Bartosz+Bryg), [Ioannis Koutis](https://dblp.uni-trier.de/search?q=Ioannis+Koutis), [David A. Bader](https://dblp.uni-trier.de/search?q=David+A.+Bader)

Subgraph isomorphism, essential for pattern detection in large-scale graphs,
faces scalability challenges in attribute-rich property graphs used in
neuroscience, systems biology, and social network analysis. Traditional
algorithms explore search spaces vertex-by-vertex from empty mappings, leading
to extensive early-stage exploration with limited pruning opportunities. We
introduce HiPerMotif, a novel hybrid parallel algorithm that fundamentally
shifts the search initialization strategy. After structurally reordering the
pattern graph to prioritize high-degree vertices, HiPerMotif systematically
identifies all possible mappings for the first edge (vertices 0,1) in the
target graph, validates these edge candidates using efficient vertex and edge
validators, and injects the validated partial mappings as states at depth 2.
The algorithm then continues with traditional vertex-by-vertex exploration from
these pre-validated starting points, effectively pruning the expensive early
search tree branches while enabling natural parallelization over edge
candidates. Our contributions include the edge-centric initialization paradigm
with state injection, a structural reordering strategy achieving up to 5x
speedup, rapid edge and vertex validators for attribute-rich graphs, and
efficient parallel enumeration over target graph edges. Implemented in the
open-source Arachne framework, HiPerMotif achieves up to 66x speedup over
state-of-the-art baselines (VF2-PS, VF3P, Glasgow) on diverse datasets where
baselines successfully complete execution. Additionally, HiPerMotif
successfully processes massive datasets such as the H01 connectome with 147
million edges, which existing methods cannot handle due to memory constraints.
Comprehensive evaluation across synthetic and real-world graphs demonstrates
HiPerMotif's scalability, enabling advanced analysis in computational
neuroscience and beyond.

[Read original post](http://arxiv.org/abs/2507.04130v1)
