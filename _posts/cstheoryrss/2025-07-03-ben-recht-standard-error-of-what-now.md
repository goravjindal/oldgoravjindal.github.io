---
layout: post
category: cstheoryrss
title: "Ben Recht: Standard error of what now?"
date: 2025-07-03T14:23:53
---

[![](https://substackcdn.com/image/fetch/$s_!gTgG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe477d1e0-64c9-4d2a-991f-441f3a12485d_1100x219.jpeg)](https://substackcdn.com/image/fetch/$s_!gTgG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe477d1e0-64c9-4d2a-991f-441f3a12485d_1100x219.jpeg)

Scrolling through discourse about the evil vector, I stumbled across a group of people dismayed that the papers they were reviewing for NeurIPS didn’t include proper error bars. In fact, I learned that there’s a [checklist](https://neurips.cc/public/guides/PaperChecklist) that authors must fill out and attach to every NeurIPS submission. You can still learn things on social media.

The NeurIPS program chairs introduced the checklist [in 2021](https://blog.neurips.cc/2021/03/26/introducing-the-neurips-2021-paper-checklist/). They argued that the community wanted “both more guidance around how to perform machine learning research responsibly and more flexibility in how they discuss this in their papers.” They came to this conclusion after listening at the “NeurIPS 2020 broader impacts workshop,” a fully remote workshop held during the cold, dark winter of the second wave of the covid pandemic. They argued that they would experiment with a checklist as a way to facilitate more responsible machine learning.

They called the checklist “experimental,” though there is no control group.[1](https://theory.report/atom.xml#footnote-1) They hoped that “future Program Chairs will continue to improve and evolve the checklist in subsequent years.” You don’t have to be a bureaucracy scholar to know that checklists “improve and evolve” by metastasizing in length and complexity. And that’s precisely what we’ve seen.

[The NeurIPS paper checklist](https://neurips.cc/public/guides/PaperChecklist) is now 3800 words long. This is twice as long as the original [checklist](https://neurips.cc/Conferences/2021/PaperInformation/PaperChecklist), and has 3 times as many items to check off. It’s a lot of ridiculous infantilizing boilerplate. Item 1: “Do the main claims made in the abstract and introduction accurately reflect the paper's contributions and scope?” Come on, folks. You are required to check that you have read the code of ethics (another 2000 words [here](https://neurips.cc/public/EthicsGuidelines)). You are asked to check whether you obtained the appropriate IRB approvals. Of course, this only applies if you are at a university. There’s a call out to the AI Safety dorks: “Do you have safeguards in place for responsible release of models with a high risk for misuse (e.g., pretrained language models)?” Come on, folks!

But I’m particularly fascinated by the weird obsession with statistics. I imagine Leo Breiman is chuckling up in heaven that one of the [two cultures](https://projecteuclid.org/journals/statistical-science/volume-16/issue-3/Statistical-Modeling--The-Two-Cultures-with-comments-and-a/10.1214/ss/1009213726.full) is trying to strangle the more successful one.[2](https://theory.report/atom.xml#footnote-2) In 2021, there was a single line about statistics:

> 2021: Did you report error bars (e.g., with respect to the random seed after running experiments multiple times)?

Honestly, not the worst question in the world. So much of machine learning and AI is based on randomized algorithms, and it’s good to check whether you have a stable result (i.e., training a neural net for classification) or a wildly variable result (i.e., [using reinforcement learning to game a robotics simulator](https://arxiv.org/abs/1709.06560)). But someone on the steering committee decided we needed a longer rule set and more statistics. The statistics creep began in 2023:

> 2023: If you ran experiments, did you report error bars (e.g., with respect to the random seed after running experiments multiple times), or other information about the statistical significance of your experiments?

And eventually, due to some unknown person’s lobbying, these were expanded further in 2024:

> 2024: “The factors of variability that the error bars are capturing should be clearly stated (for example, train/test split, initialization, random drawing of some parameter, or overall run with given experimental conditions). The method for calculating the error bars should be explained (closed form formula, call to a library function, bootstrap, etc.). The assumptions made should be given (e.g., Normally distributed errors). It should be clear whether the error bar is the standard deviation or the standard error of the mean. It is OK to report 1-sigma error bars, but one should state it. The authors should preferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesis of Normality of errors is not verified. For asymmetric distributions, the authors should be careful not to show in tables or figures symmetric error bars that would yield results that are out of range (e.g. negative error rates). If error bars are reported in tables or plots, the authors should explain in the text how they were calculated and reference the corresponding figures or tables in the text.”

What does this have to do with anything? If I run my code ten times, why should you care if I properly account for normal approximations? Who does this help?

Anyway, I love that NeurIPS is proving my central thesis about statistics: [Statistics is a bunch of arbitrary rules we use for approval](https://arxiv.org/abs/2501.03457). These arbitrary rules have now found their way into the machine learning publication machine. Whereas I understand why we require statistical tests when approving pharmaceuticals, no one has provided an explanation for why (or if) these statistical guidelines improve the quality of the thirty thousand NeurIPS submissions.

Indeed, I can’t figure out *why* people have become so obsessed with error bars in machine learning. I have been told that it’s because data sets are “small” now. For example, some of the “can LLM solve human tests” data sets have a few dozen questions. The [AIME benchmark](https://www.vals.ai/benchmarks/aime-2025-03-11) has 15. But what do frequentist error bars buy you here? This isn’t like Fisher’s friend who tastes tea. If a machine can solve a single one of these problems, it’s interesting! LLM answers are variable by design. Trying to gauge this variability with “Gaussian approximations to the standard errors of the mean” misses the forest for the trees. Indeed, if you only have 15 questions in a dataset, you don’t need statistics. Just look at the answers! We’re not grading the LLM on a curve here.

The obsession with statistics is particularly ironic because the advances in machine learning from the past 15 years have been entirely based on optimaxxing vibes. While program committees and responsible ethics boards fixate on procedure, the big ideas have come from “this feels right,” whether they be bigger convnets, ADAM optimizers, attention mechanisms, or anything in RL. Do you think recent trends in transformer architectures like using RMSNorm instead of Layernorm or SwiGLU instead of ReLU are undergirded by deep statistical grounding?[3](https://theory.report/atom.xml#footnote-3)

What gives away the whole checklist charade here is bullet 4. The rules say that you must disclose the normal approximations in your error bars, but *you don’t have to release code*.

> "While NeurIPS does not require releasing code, we do require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution.“

Why no code? It’s because a substantial fraction of NeurIPS papers come from private companies. The biggest models come from private companies. The conference exists to enrich Sam Altman. There’s no recruiting fair, no late-night parties, no signing bonuses based on Google Scholar profiles without the corporate commitment. So we can pat ourselves on the back and tell ourselves we’re being responsible researchers as we fill out our checklists and format our error bars. But let’s not kid ourselves about what we’re participating in.

[Subscribe now](https://www.argmin.net/subscribe)

[1](https://theory.report/atom.xml#footnote-anchor-1)

I couldn’t find the preregistration plan.

[2](https://theory.report/atom.xml#footnote-anchor-2)

There is still no statistically significant evidence to support the existence of heaven.

[3](https://theory.report/atom.xml#footnote-anchor-3)

Like you, I don’t know what any of these things are.

By Ben Recht