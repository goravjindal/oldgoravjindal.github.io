---
layout: post
category: cstheoryrss
title: "Ben Recht: An open mindset"
date: 2025-07-10T13:59:06
---

[![](https://substackcdn.com/image/fetch/$s_!cNNz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F26acc5c2-4af2-4f99-9d35-e7fa57ff6dd2_1100x219.jpeg)](https://substackcdn.com/image/fetch/$s_!cNNz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F26acc5c2-4af2-4f99-9d35-e7fa57ff6dd2_1100x219.jpeg)

Over the 4th of July weekend, Nathan Lambert wrote a thoughtful post on “[an American Deepseek Project](https://www.interconnects.ai/p/the-american-deepseek-project),” posing the challenge of building a fully open, fully performant “frontier model” in the next two years. Deepseek, in case you’ve already forgotten, is a Chinese company that released a highly performing, open-source large language model chatbot in January that could be trained from scratch for under [10 million dollars](https://imgflip.com/memegenerator/16799330/one-million-dollars). Nathan challenges the US research community to produce a similar open artifact.

Nathan’s post reminded me of what happened the last time we were told that you needed to be a hyperscaling tech company to do machine learning. In 2014, a year after paying [44 million dollars](https://www.wired.com/story/secret-auction-race-ai-supremacy-google-microsoft-baidu/) for Alex Krizhevsky, Ilya Sutskever, and Geoff Hinton, Google won the ILSVRC competition with their “GoogLeNet” model, achieving 93% top-5 accuracy.[1](https://theory.report/atom.xml#footnote-1) While the authors didn’t release the full details of how to train this model, they asserted they used Google’s internal DistBelief system, a distributed computing framework for wrangling thousands of Google CPUs. However, based on a back of the envelope calculation, [they claimed](https://arxiv.org/pdf/1409.4842v1) “ the GoogLeNet network could be trained to convergence using few high-end GPUs within a week, the main limitation being the memory usage.”

Shortly thereafter, a team at Berkeley sort of reproduced this result, showing that half a day with 128 GPUs could get to [88% top-5 accuracy with the GoogLeNet architecture](https://arxiv.org/abs/1511.00175). I imagine they could have reached 93% had they run for longer. A supercomputer with 128 GPUs was still a serious investment for any academic team, and openly trained ImageNet models still seemed to require infrastructural investments outside the reach of most labs.

In 2015, a team of researchers at Microsoft Research Asia in Beijing [won the ILSVRC competition with their architecture called the ResNet](https://arxiv.org/abs/1512.03385). ResNets were interesting because the principles of architecture were easier to understand. The repeated layers in ResNets made it easy to explore and reimplement the architecture.

Soon thereafter, the Dawn project at Stanford opened a competition, called [DawnBench](https://dawn.cs.stanford.edu/dawnbench), to see who could train ResNets the fastest. In November 2017, their baseline entry used 8 GPUs for 10.5 days to train a ResNet ImageNet classifier with 93% top-5 accuracy. This cost $1100 using Amazon cloud services. Already, this was getting somewhere, but I don’t think the Dawn team anticipated how quickly competition progress would come. By April 2018, that is, in less than six months, [competitors had the training time down to 30 minutes on a single TPU core on Google Cloud](https://dawnd9.sites.stanford.edu/news/dawnbench-v1-deep-learning-benchmark-results). That’s nearly a 500x acceleration in 6 months, and a dramatic cost reduction.

I tell this story because I’m optimistic that Nathan’s challenge is feasible. For two decades, Google and its peers have argued that you need scale to do anything. These claims are marketing. They have been proven wrong several times,[2](https://theory.report/atom.xml#footnote-2) but it required a significant community commitment to do it. What are those commitments for Nathan’s Deepseek Project?

First, it’s elevating old school computational evaluations. During the initial deep learning boom, the machine learning research community decided that worthy [common tasks](https://hdsr.mitpress.mit.edu/pub/g9mau4m0/release/2) were training time and model accessibility. These evaluations have been missing from the latest “frontier models” arms race. It’s also understandable that the computing for “frontier models” is much larger than it was for ImageNet. The hyperscalers' only advantage is to find a starting point that’s inaccessible to a researcher without an infinite cloud computing budget. The 6 million dollars needed to train DeepSeek is out of reach for almost any machine learning researcher. This means that the initial work on any fully open LLM will require large-scale collaboration or perhaps an industrial benefactor. On the other hand, a 500x improvement in training time gets these models down to costing under twenty thousand dollars, which is the sort of thing you can add as a line item in a grant proposal.

More importantly, I want to emphasize that Nathan’s challenge is for something greater than just GPU golf. When he writes “open model,” he really means *open*. The Deepseek model is “open weights,” which means you can run and tweak it, but you can’t build it from scratch. This is similar to the openness of Meta’s Llama models. Nathan’s vision calls for open data, training code, logs, and decision making too.

I will never get over how the entire machine learning community is writing papers about systems where they don’t know what the training data is. Yes, the artifacts are interesting, but no, we’re not going to learn anything by fine-tuning RL models on top and running hackneyed 1960s psychology experiments on computers. Certainly, open weight models are preferable to closed weight models. But we shouldn’t have to settle.

Open data poses its own challenges to our community. Though we generally concede that open data has been the primary means of driving machine learning research, parts of the research community are openly hostile to open data. And it’s not exactly who you’d think it would be. Some of the biggest “success stories” of the responsible AI/fairness community are based on finding “dangerous” content in open data sets, resulting in these data sets being removed from the public domain. The Netflix Prize, Tiny Images Dataset, and yes, even ImageNet, have all been either entirely removed, taken down for extended periods, or neutered in some capacity because of highly questionable arguments about “responsibility.”

This push towards prioritizing academic notions of “privacy,” “safety,” and “fairness” over all else has mostly resulted in *academic* censorship. And yet, while the hyperscalers love to pay lip service to responsible behavior, they don’t stop using this data! Recent lawsuits have revealed that [Anthropic scans millions of books](https://arstechnica.com/ai/2025/06/anthropic-destroyed-millions-of-print-books-to-build-its-ai-models/) and [Facebook trains on LibGen](https://futurism.com/the-byte/facebook-trained-ai-pirated-books). But academic researchers aren’t allowed to use the Tiny Images Dataset. The hyperscalers do whatever they want, in private, locking out competition and strengthening their oligopoly. They know they will find a favorable ruling in [Bill Alsup’s](https://www.theverge.com/2017/10/19/16503076/oracle-vs-google-judge-william-alsup-interview-waymo-uber) court because they have infinite money for their legal teams.

So while it’s undeniably essential to raise issues about the societal impacts of machine learning technology, we have to be careful not to do this in a way that solidifies corporate power. If we want fully open and accessible machine learning models, we need to figure out how to build them while accepting that the internet on which they are trained is littered with [endlessly horrific and dangerous content](https://arstechnica.com/tech-policy/2024/08/nonprofit-scrubs-illegal-content-from-controversial-ai-training-dataset/). Nathan’s challenge is thus asking the open research community to engage with uncomfortable trade-offs about what open *means.* This question is as vital as shaking the can to raise money for NVIDIA chips.

[Subscribe now](https://www.argmin.net/subscribe)

[1](https://theory.report/atom.xml#footnote-anchor-1)

For the purposes of this blog post “top-5 accuracy” is just a number between 0 and 100. Higher is better. Don’t sweat the details of what this means or actually evaluates.

[2](https://theory.report/atom.xml#footnote-anchor-2)

Naomi Saphra points me to another [example in machine translation](https://arxiv.org/abs/2311.05020).

By Ben Recht

[Read original post](https://www.argmin.net/p/an-open-mindset)
