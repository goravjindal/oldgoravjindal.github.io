---
layout: post
category: cstheoryrss
title: "Ben Recht: Metascience of pull requests"
date: 2025-07-15T14:52:55
---

[![](https://substackcdn.com/image/fetch/$s_!l7uc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb56681ca-3f69-437d-8d94-eb4ddb9920d2_1100x219.jpeg)](https://substackcdn.com/image/fetch/$s_!l7uc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb56681ca-3f69-437d-8d94-eb4ddb9920d2_1100x219.jpeg)

Last week, I wrote two posts on a related theme, but didn’t fully connect them to my earlier thoughts on the topic. I have a particular drum I’ve been beating consistently on this blog since I moved to Substack (and I have even [older posts](http://archives.argmin.net) on it, too):

1. Though machine learning is statistical prediction, [classical inferential statistics has nothing interesting to say about the field](https://www.argmin.net/p/i-dont-know-what-ive-been-trying).
2. In fact, lessons from classical inferential statistics have [historically provided poor, misleading guidance](https://www.argmin.net/p/thou-shalt-not-overfit) for machine learning practice.
3. A culture of frictionless reproducibility has been the primary driver of [machine learning progress.](https://hdsr.mitpress.mit.edu/pub/g9mau4m0/release/2)

I use the term classical inferential statistics loosely here, and Siva Balakrishnan is going to get mad at me about it. He and I cannot agree on a term to describe the narrow statistical subfield that I want to call out: frequentist claims about out-of-sample behavior derived from laws of large numbers and the union bound. This includes statistical significance, null hypothesis significance testing, and error bars.[1](https://theory.report/atom.xml#footnote-1)

I’ve decided to try out “classical” because Jessica Hullman used it in her [blog post advocating for more statistics in machine learning.](https://statmodeling.stat.columbia.edu/2025/07/11/opportunities-for-interpretable-statistics-for-large-language-models) I always find Jessica thought-provoking, and she links to me and asks at the end of the post.

> “But others refer to attempts to incentivize more thorough reporting of uncertainty in ML evaluation as “a weird obsession with statistics. What’s up with that, I wonder?”

I’ll reply here, though most of what I wanted to say was already written in the comments under Jessica’s post by frequent stat modeling interlocutor Anoneuoid:

* Mandating null hypothesis significance testing and related ideas is a fast way to stifle progress.
* Systematic errors are more important than sampling errors.
* Since everyone started deep learning, machine learning papers have been reduced to advertisements of pull requests.
* You don’t need 90 pages of robustness checks or proofs, since you can simply try the code and decide for yourself whether to accept it.

I swear I am not Anoneuoid. We just happen to strongly agree about everything.

But yes, I have made the same arguments on the blog many times. If the machine learning community had listened to the guidelines from classical inferential statistics, nothing would have ever gotten built. Machine learning was largely developed without the use of classical inferential statistics. In fact, the influence has gone in the opposite direction: since 1960, statistically minded researchers have been trying to bootstrap a “statistical learning theory” by chasing practice.

The problem is that theories derived by shoe-horning practice into classical statistical footwear haven’t been productive. Every time this narrow view of classical statistics is applied, it gives the wrong advice! It’s been actively harmful to the field. It makes incorrect predictions and obsesses about the wrong type of error.

The part of practice that most resembles classical statistics is the train-test paradigm.[2](https://theory.report/atom.xml#footnote-2) [Statistics doesn’t explain why this is successful at all!](https://www.argmin.net/p/the-adaptivity-paradox) If anything, this has polarized me against other conclusions drawn from statistical theory. Indeed, it makes me believe that claims about the scientific detriment of p-hacking and uncorrected multiple hypothesis testing are wildly overstated.

Another post critiquing statistics is all well and good, but I have a more important point to make here about what we might consider doing instead. Jessica writes to Anoneuoid:

> “But I guess part of what I find confusing about dismissing attempts to hold people accountable for what they are claiming (like the crazy long NeurIPS checklist that the linked post complains about) is that in the absence of suggesting an alternative way to better align the claims and the evidence, it reads as though we’re saying all is ok as is and uncertainty can continue to be an afterthought when presenting evaluation results.”

I often feel like the solutionist burden placed on critics is an easy way to wave off critique. But on this issue, I am actually proposing an alternative! Open models, open data, and open code are a clear, feasible alternative requirement. These are not major asks. As I said in a previous post, the only reason we don’t require these is that there are still a lot of corporate interests at the big machine learning conferences, and these places always have some argument for why they can’t release code and data. David Pfau noted on Twitter that this is rapidly changing with the LLM arms race, with the companies moving towards abandoning publishing altogether. He might be right, but that doesn’t mean we have to encourage their nefarious behavior by embracing their move to proprietary secrecy.

Jessica admits the problem herself in her review of Weijie Su’s argument for more statistics in machine learning research.

> "Something a bit cringey that becomes clearer when you see the various statistical challenges laid out like this is that sometimes they arise not just because LLMs are too complex for us to understand, but also because they are proprietary objects.”

The frustration with most modern published LLM papers is industrial closedness reduces open research to ephemeral flailing. If you are taking a proprietary, closed model and doing some prompt engineering to elicit funny answers, you are doing HCI research on proprietary software. If you train a transformer model from scratch on the orbits of planets and don’t use all of the language on the internet, your result says *nothing* about LLMs. Even if you are fine-tuning an open weights model, there’s only so much we can learn because you have no idea what the training corpus is.

Machine learning has thrived in its embrace of frictionless reproducibility— Open, shareable data. The ability to re-execute code. Competitive Testing. These are powerful tools to mitigate uncertainty. [I’ve written some thoughts about why this is](https://hdsr.mitpress.mit.edu/pub/8dqgwqiu), drawing analogies to distributed optimization. I still think this is an excellent direction for meta-scientific study. But for whatever reason, many in the orbit of machine learning seem more interested in developing more statistical tests than in understanding why exactly this practice works so well.

Let me close with quoting Andrew Gelman, who replied to Jessica,

> “On the other side, Recht presents a very reasonable engineering perspective that is anti-bureaucratic: we've already made a lot of progress and continue to do so, so don't tell us what to do. Or, to put it more carefully, you can tell us what to do for safety or public policy reasons, but it seems like a mistake to try to restrict researchers' freedom in the belief that this will improve research progress. This general position makes sense to me, and it is similar to many things I've said and written regarding science reform: I don't want to tell people what to do, and I also don't want criticism to be suppressed. That doesn't mean that science-reform proposals are necessarily bad. For example, I find preregistration to be valuable (for the science, not the p-values), but I wouldn't want it to be a requirement.”

I agree strongly here with Andrew. Our mandates should be few and far between. I advocate for only one: stronger norms about openness in code, data, and models.

[Subscribe now](https://www.argmin.net/subscribe)

[1](https://theory.report/atom.xml#footnote-anchor-1)

I’ll leave the Bayesians alone today because no one is yet proposing LDA to be on the NeurIPS checklist yet.

[2](https://theory.report/atom.xml#footnote-anchor-2)

Though the train test paradigm was [invented by practice](https://www.argmin.net/p/holding-out-for-an-explanation), not by a careful application of statistics.

By Ben Recht

[Read original post](https://www.argmin.net/p/metascience-of-pull-requests)
