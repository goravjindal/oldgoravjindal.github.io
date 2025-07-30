---
layout: post
category: cstheoryrss
title: "arXiv: Computational Geometry: Exploring the Stratified Space Structure of an RL Game with the Volume"
date: 2025-07-30T00:00:00
---

**Authors:** [Justin Curry](https://dblp.uni-trier.de/search?q=Justin+Curry), [Brennan Lagasse](https://dblp.uni-trier.de/search?q=Brennan+Lagasse), [Ngoc B. Lam](https://dblp.uni-trier.de/search?q=Ngoc+B.+Lam), [Gregory Cox](https://dblp.uni-trier.de/search?q=Gregory+Cox), [David Rosenbluth](https://dblp.uni-trier.de/search?q=David+Rosenbluth), [Alberto Speranzon](https://dblp.uni-trier.de/search?q=Alberto+Speranzon)

In this work, we explore the structure of the embedding space of a
transformer model trained for playing a particular reinforcement learning (RL)
game. Specifically, we investigate how a transformer-based Proximal Policy
Optimization (PPO) model embeds visual inputs in a simple environment where an
agent must collect "coins" while avoiding dynamic obstacles consisting of
"spotlights." By adapting Robinson et al.'s study of the volume growth
transform for LLMs to the RL setting, we find that the token embedding space
for our visual coin collecting game is also not a manifold, and is better
modeled as a stratified space, where local dimension can vary from point to
point. We further strengthen Robinson's method by proving that fairly general
volume growth curves can be realized by stratified spaces. Finally, we carry
out an analysis that suggests that as an RL agent acts, its latent
representation alternates between periods of low local dimension, while
following a fixed sub-strategy, and bursts of high local dimension, where the
agent achieves a sub-goal (e.g., collecting an object) or where the
environmental complexity increases (e.g., more obstacles appear). Consequently,
our work suggests that the distribution of dimensions in a stratified latent
space may provide a new geometric indicator of complexity for RL games.

[Read original post](http://arxiv.org/abs/2507.22010v1)
