---
layout: post
category: cstheoryrss
title: "arXiv: Computational Complexity: FormulaOne: Measuring the Depth of Algorithmic Reasoning Beyond
  Competitive Programming"
date: 2025-07-18T00:00:00
---

**Authors:** [Gal Beniamini](https://dblp.uni-trier.de/search?q=Gal+Beniamini), [Yuval Dor](https://dblp.uni-trier.de/search?q=Yuval+Dor), [Alon Vinnikov](https://dblp.uni-trier.de/search?q=Alon+Vinnikov), [Shir Granot Peled](https://dblp.uni-trier.de/search?q=Shir+Granot+Peled), [Or Weinstein](https://dblp.uni-trier.de/search?q=Or+Weinstein), [Or Sharir](https://dblp.uni-trier.de/search?q=Or+Sharir), [Noam Wies](https://dblp.uni-trier.de/search?q=Noam+Wies), [Tomer Nussbaum](https://dblp.uni-trier.de/search?q=Tomer+Nussbaum), [Ido Ben Shaul](https://dblp.uni-trier.de/search?q=Ido+Ben+Shaul), [Tomer Zekharya](https://dblp.uni-trier.de/search?q=Tomer+Zekharya), [Yoav Levine](https://dblp.uni-trier.de/search?q=Yoav+Levine), [Shai Shalev-Shwartz](https://dblp.uni-trier.de/search?q=Shai+Shalev-Shwartz), [Amnon Shashua](https://dblp.uni-trier.de/search?q=Amnon+Shashua)

Frontier AI models demonstrate formidable breadth of knowledge. But how close
are they to true human -- or superhuman -- expertise? Genuine experts can
tackle the hardest problems and push the boundaries of scientific
understanding. To illuminate the limits of frontier model capabilities, we turn
away from contrived competitive programming puzzles, and instead focus on
real-life research problems.
We construct FormulaOne, a benchmark that lies at the intersection of graph
theory, logic, and algorithms, all well within the training distribution of
frontier models. Our problems are incredibly demanding, requiring an array of
reasoning steps. The dataset has three key properties. First, it is of
commercial interest and relates to practical large-scale optimisation problems,
such as those arising in routing, scheduling, and network design. Second, it is
generated from the highly expressive framework of Monadic Second-Order (MSO)
logic on graphs, paving the way toward automatic problem generation at scale;
ideal for building RL environments. Third, many of our problems are intimately
related to the frontier of theoretical computer science, and to central
conjectures therein, such as the Strong Exponential Time Hypothesis (SETH). As
such, any significant algorithmic progress on our dataset, beyond known
results, could carry profound theoretical implications.
Remarkably, state-of-the-art models like OpenAI's o3 fail entirely on
FormulaOne, solving less than 1% of the questions, even when given 10 attempts
and explanatory fewshot examples -- highlighting how far they remain from
expert-level understanding in some domains. To support further research, we
additionally curate FormulaOne-Warmup, offering a set of simpler tasks, from
the same distribution. We release the full corpus along with a comprehensive
evaluation framework.

[Read original post](http://arxiv.org/abs/2507.13337v1)
