---
layout: post
category: cstheoryrss
title: "Ben Recht: You keep using that word"
date: 2025-07-07T14:23:51
---

[![](https://substackcdn.com/image/fetch/$s_!grJj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32cf3954-ce09-4e38-977b-352c36994717_1100x219.jpeg)](https://substackcdn.com/image/fetch/$s_!grJj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32cf3954-ce09-4e38-977b-352c36994717_1100x219.jpeg)

A friend sent me a fun article in [FT Alphaville](https://www.ft.com/content/89d88cbf-a92c-43d2-b8af-88ae26529be0) by Bryce Elder showing how dogma doesn’t need to make sense to make money. The article hooked me from the get-go:

> “The Virtue of Complexity in Return Prediction — co-authored by Bryan Kelly with Semyon Malamud and Kangying Zhou — found that complex machine-learning models were better than simple ones at predicting stock prices and building portfolios.”

> “The finding was a big deal because it contradicted one of machine learning’s guiding principles, the bias-variance trade-off, which says the predictive power of models weakens as they grow beyond some optimum level. Given too many parameters to play with, a bot will tend to overfit its output to random noise in the training data.”

Oh, [I’ve written about this before](https://www.argmin.net/p/overfitting-to-theories-of-overfitting), arguing we should remove the bias-variance tradeoff from the machine learning curriculum. Much love to everyone who references the ye olde argmin blog in the comments over on Alphville. I appreciate the shoutouts! However, many of my friends in finance have told me that their data was where statistical overfitting, the type of overfitting we teach in our undergraduate classes, was a real phenomenon. Here is a paper that apparently refutes their claims. According to Kelly et al., even in finance, the bias-variance tradeoff isn’t real. Elder continues:

> “The finding was rooted in an AI concept known as double descent, which says deep learning algorithms make fewer mistakes when they have more variable parameters than training data points.”

Double descent, you say? Hmm. At this point in the article, I got a bit worried because that’s… not what double descent says. Well, now I had to go and [download the paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3984925) from SSRN. It checks in at a crisp 141 pages.

Once you skip past the laborious theoretical analysis of a linear Gaussian model, you get to the experiments on page 41. The authors want to predict next month's prices from a set of 15 indicators. They use a window of past pairs of indicators and prices from the last 12 months to make this prediction. They propose applying standard supervised learning to solve this problem. Translating their setup into machine learning language: their training dataset has 12 examples, each with 15 features. Yes, 12.

What do they conclude? They find that if they use *[random Fourier features](https://archives.argmin.net/2017/12/05/kitchen-sinks/),* then the training error continues to decrease as they add more and more features. In particular, using 12,000 random Fourier features still gives good performance.

Oh my. I know it’s been twenty years since Ali and I first wrote up our paper on random features, and our point seems to have been lost in time.[1](https://theory.report/atom.xml#footnote-1) The motivation was finding computationally efficient ways to approximate machine learning in *kernel spaces*. I realize no one learns about kernel methods anymore, but you can read about them in [Chapter 4](https://mlstory.org/features.html) of *[Patterns, Predictions, and Actions](http://mlstory.org)*. For the purpose of this post: kernel methods give you a computationally efficient way to compute a prediction model that uses an *infinite* number of features. Through some fun linear algebra, it turns out you only need to solve a linear system with one variable for every training example. Kernel methods transform infinite-dimensional learning problems into finite-dimensional linear algebra problems.

Still, kernel methods require more computation than standard linear regression methods (and deep learning methods for that matter). The time needed to solve a linear system scales with the *cube* of the number of data points. The time required to solve linear regression scales *linearly* with the number of data points. Ali and I initially stumbled upon random features as a way to approximate kernel methods by solving linear regression problems.

But you know folks, kernel methods aren’t *that* computationally expensive. Cubic time is still polynomial time. And high-dimensional linear regression has its own scaling issues. The solution time of a random Fourier features problem scales with the *square* of the number of features.[2](https://theory.report/atom.xml#footnote-2) Since random features approximate kernel methods, the prediction performance of kernel methods should always be as good or better.[3](https://theory.report/atom.xml#footnote-3)

To reiterate, kernel ridge regression solves an *infinite-dimensional* regression problem. It is going to get you the solution promised by the asymptote of that double descent curve you are all so enamored with. Infinity is more than 12,000, and moar is always better, right? If you find yourself using 1000 times more random features than data points, you might want to consider reading a few tutorials on kernel regression. It’s not hard to implement! In Python on my laptop, I can solve a 12 example kernel ridge regression problem in microseconds.

The argmin blog is here to help you save money on GPU cloud credits.

Now you might ask, would “ridgeless kernel regression,” that is, kernel regression that ignores the warnings of the bias-variance tradeoff, work well for time series analysis? This is a good question, and one asked by Emmanuel Parzen in his landmark *1961* paper, “[An Approach to Time Series Analysis](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-32/issue-4/An-Approach-to-Time-Series-Analysis/10.1214/aoms/1177704840.full).”[4](https://theory.report/atom.xml#footnote-4) Parzen’s paper is one of the first to explicitly use reproducing kernels in prediction problems. In Section 6, he proposes using ridgeless kernel regression to solve the exact same problem studied by Kelly and coauthors.

I’m not the first person to recognize this, as Elder notes in Alphaville. Stefan Nagel wrote a [convincing rebuttal](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5335012) to Kelly et al., posted last week. Nagel notes that random Fourier features are approximating kernel regression. He also notes that the prediction function computed by kernel regression looks a lot like *kernel smoothing*. This means the data points that most influence the prediction will be the ones most recent in time. Nagel thus argues that Kelly et al. are making a bunch of appeals to deep learning hype to reinvent momentum investing.

And about that bias-variance tradeoff? If you slog through Kelly et al, you’ll see that their theoretical analysis *has a bias-variance tradeoff!* And the optimum setting requires tuning the tradeoff!

> “We show that machine learning portfolios tend to incrementally benefit from moving away from the ridgeless limit by introducing nontrivial shrinkage.”

Sigh.

I realize that everyone has jumped on the deep learning train now, but cargo culting isn’t in your interest. For small problems (like training sets of size 12), you don’t need neural networks. You can use them, I guess. But you can get more understanding out of these small, infinite-dimensional models that people have been studying for seventy years.

Sadly, the hype cycle gets everyone confused. It’s hilarious that stylized statistical learning theory stories now find their way into the mainstream press. The Alphaville title is even confused here: “Are bigger AI models better stock pickers? Maybe, but probably not. Complexity ain’t all that, wonks say.” I mean, this contradicts the rest of the story. First, calling ordinary least squares “AI” is a bit of a stretch. Second, Nagel’s results show that in this restricted class of models, bigger models *are* indeed better. Moreover, those *infinitely large* models recover well-known, naive momentum strategies.

Kelly and his fund, AQR, weren’t happy about Elder’s article. They wrote a rebuttal, proclaiming:

> “The empirical dominance of large models has been shown in every area of ML by heavyweight ML academics’ research, which has been conducted throughout the natural and applied sciences. Language and image modeling are most well-known applications that exemplify the success of large models. Do we really think that finance, economics, or other social sciences are special? The work of Kelly and team shows otherwise.”

This heavyweight ML academic offers a very reasonable consulting fee if you are at a hedge fund and need assistance understanding double descent and the no true Scotsman fallacy.

[Subscribe now](https://www.argmin.net/subscribe)

[1](https://theory.report/atom.xml#footnote-anchor-1)

…like tears in rain.

[2](https://theory.report/atom.xml#footnote-anchor-2)

Yeah, you can do some stochastic gradient stuff to get that square down to linear, but let me not bore everyone with flop counting. We can save that for a more technical post.

[3](https://theory.report/atom.xml#footnote-anchor-3)

I realize theory and practice don’t always align, but in my experience, this is always true.

[4](https://theory.report/atom.xml#footnote-anchor-4)

What a title. Such modesty with indefinite articles would get you immediately desk rejected at NeurIPS.

By Ben Recht

[Read original post](https://www.argmin.net/p/you-keep-using-that-word)
