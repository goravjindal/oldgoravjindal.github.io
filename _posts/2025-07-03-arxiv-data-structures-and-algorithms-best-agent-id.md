---
layout: post
title: "arXiv: Data Structures and Algorithms: Best Agent Identification for General Game Playing"
date: 2025-07-03 13:21:53 
categories: [rss]
external_link: http://arxiv.org/abs/2507.00451v1
---

**Authors:** [Matthew Stephenson](https://dblp.uni-trier.de/search?q=Matthew+Stephenson), [Alex Newcombe](https://dblp.uni-trier.de/search?q=Alex+Newcombe), [Eric Piette](https://dblp.uni-trier.de/search?q=Eric+Piette), [Dennis Soemers](https://dblp.uni-trier.de/search?q=Dennis+Soemers)

We present an efficient and generalised procedure to accurately identify the
best performing algorithm for each sub-task in a multi-problem domain. Our
approach treats this as a set of best arm identification problems for
multi-armed bandits, where each bandit corresponds to a specific task and each
arm corresponds to a specific algorithm or agent. We propose an optimistic
selection process based on the Wilson score interval (Optimistic-WS) that ranks
each arm across all bandits in terms of their potential regret reduction. We
evaluate the performance of Optimistic-WS on two of the most popular general
game domains, the General Video Game AI (GVGAI) framework and the Ludii general
game playing system, with the goal of identifying the highest performing agent
for each game within a limited number of trials. Compared to previous best arm
identification algorithms for multi-armed bandits, our results demonstrate a
substantial performance improvement in terms of average simple regret. This
novel approach can be used to significantly improve the quality and accuracy of
agent evaluation procedures for general game frameworks, as well as other
multi-task domains with high algorithm runtimes.
