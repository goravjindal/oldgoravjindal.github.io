---
layout: post
category: cstheoryrss
title: "Ben Recht: The unpredictability conundrum"
date: 2025-07-17T14:32:41
---

[![](https://substackcdn.com/image/fetch/$s_!Vzvq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d570f48-a2f4-4edf-b54a-e7a100501336_1100x220.jpeg)](https://substackcdn.com/image/fetch/$s_!Vzvq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d570f48-a2f4-4edf-b54a-e7a100501336_1100x220.jpeg)

Scrolling through the deluge of people advertising their ICML papers on social media, I found myself bedeviled by a philosophical question about the logical reconstruction of machine learning. In the most famous machine learning papers, the central claims take the form:

Y is predictable from X, and method M demonstrates a particular accuracy on this prediction problem.

The [AlexNet paper](https://proceedings.neurips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf) showed that ImageNet image classes were predictable from images, and a convolutional neural network achieved high accuracy. The [GPT3 paper](https://arxiv.org/abs/2005.14165) achieved high accuracy on a variety of natural language processing prediction problems with one-shot learning and transformer-based large language models. The [Support Vector Network paper](https://link.springer.com/article/10.1007/BF00994018) showed that support vector machines could recognize handwritten digits with high accuracy.

In these descriptions, I am being vague today about what precisely “X” and “Y” are. “X” could be streams of text, images, or electronic health records. “Y” could be translations, image classes, or cancer diagnoses. How papers build up these constructs and concepts also bugs me, but I will leave a full logical reconstruction of machine learning for another blog post.[1](https://theory.report/atom.xml#footnote-1)

Today, I am interested in understanding the papers that argue the negative claim and whether they ever provide useful evidence. That is, the papers that assert:

Y is not predictable from X.

I call claims of this form “unpredictability arguments.” Papers making unpredictability arguments can get a lot of temporary traction in machine learning discourse. They give fuel to the petty battles inside the community. In our current landscape, they give ammunition for lay critiques of industry. They can even help bring on AI Winters if people take them seriously enough. The problem is they are much harder to justify as stated.

Unpredictability arguments can be purely theoretical. These might say something like “under this list of assumptions about how data is generated and this list of assumptions about how you build the prediction function, Y is not predictable from X.” Such arguments can be helpful for conceptualization, but they are too strongly tied to their assumptions. Yes, simple linear perceptrons can’t build an XOR of input bits. But simple multilayer perceptrons can. Moreover, if your prediction function is allowed to include simple numerical transformations of the input data, all of a sudden XOR is predictable by linear functions (that is, just add XOR as a feature.).

Theory bounds are weak because practitioners (and theorists for that matter) can simply change the rules. Yes, you can tell me that under some very contrived scenario, I can’t build a particular computer program. But machine learning practice is the apotheosis of computer science, fully embracing a Feyerabendian zeal for *anything goes.* I can always disagree with your assessment of how data is collected, generated, and processed. And there are an infinite number of computer programs I can write in PyTorch to disprove your unpredictability assertion.

Minsky and Papert’s arguments that I’m alluding to above—about whether perceptrons can compute parity—are a notable exception that proves the rule. No one really understands their arguments, and if you believed them without really digging into the details or trying some simple alternative prediction programs, you would have abandoned supervised learning for decades (oh wait, that’s actually what happened).

Now, what about experimental bounds? If someone writes a paper saying, “I did procedure P and found transformers were really bad at predicting Y from X,” what does this tell us? I’ve seen a lot of papers make such claims concerning LLMs and transformers. You’ll have people saying, “See, LLMs are stochastic parrots,” or “See, LLMs just learn epicycles.” In these papers, the predictability of the Y value is supposed to be obvious to the reader, and we’re supposed to be shocked that some machine learning model can’t predict it.

Sure, people can say all they want. As someone who wants better critiques of predictions, I’m never convinced by these papers, no matter how frequently they capture a viral zeitgeist. In the spirit of a [Lakatosian](https://www.argmin.net/p/lakatosian-defense) [offense](https://www.argmin.net/p/strunk-and-white-for-science), I can always counter by tweeting “your procedure is pretty arbitrary, my friend,” or “i don’t think that baseline is fair,” or “skill issue.” There is no reason to believe that the code shared in such papers is the only way for a method to predict Y from X. There is an infinite regress of hyperparameters, optimization variants, and so on. You only have so many forking paths you can explore in the garden before the conference deadline.

Most people would find competitions to be more compelling evidence. Machine learning is built upon competitive testing, leading to breakthroughs in proving Y predictable from X. Everyone loves the ImageNet competition. Benchmark scores are a central part of how companies showcase their latest language models. Can competitive testing “prove” Y is unpredictable?

What do we conclude when machine learning competitions fail? A notable example of failure is the [Future of Families Challenge](https://www.pnas.org/doi/10.1073/pnas.1915006117) (formerly known as the Fragile Families Challenge). The goal here was to predict certain socioeconomic outcomes from complex, unstructured data recorded about a large birth cohort. After hundreds of researchers tried to predict the outcomes, the study concluded that the best predictions were not very accurate and were only slightly better than those from a simple benchmark model.”

What should we conclude from this competition? We could conclude that the Ys in this paper (including “material hardship,” GPA, “grit,” and eviction) are not predictable from the Xs. I could also conclude that poor predictability arises because the data is far worse than advertised (e.g., there is *[a lot](https://www.fragilefamilieschallenge.org/missing-data/)* [of missing data in the](https://www.fragilefamilieschallenge.org/missing-data/) dataset). I could conclude that the targets studied have poor construct validity. There’s a long line of objections that I can string together even when a competitive test fails to find predictability.

In any event, I don’t have good answers for how to think about this aspect of the philosophy of machine learning yet. I’m very much thinking out loud today! But I’m posting because I’d love to hear your thoughts on what would constitute compelling evidence to prove the impossibility of prediction.

[Subscribe now](https://www.argmin.net/subscribe)

[1](https://theory.report/atom.xml#footnote-anchor-1)

Really, it should be a paper. Let me know if you are soliciting invitations for special issues on the philosophy of engineering.

By Ben Recht

[Read original post](https://www.argmin.net/p/the-unpredictability-conundrum)
