---
layout: post
category: cstheoryrss
title: "Ben Recht: Are developers finally out of a job?"
date: 2025-07-11T14:11:52
---

[![](https://substackcdn.com/image/fetch/$s_!QqJZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0265a32b-a1d0-4ab4-b990-3ea8e7e3ce91_1100x219.jpeg)](https://substackcdn.com/image/fetch/$s_!QqJZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0265a32b-a1d0-4ab4-b990-3ea8e7e3ce91_1100x219.jpeg)

Yesterday, METR, one of the many budding nonprofit “AI Safety” institutes in Berkeley, released a study purportedly showing that AI tools slowed down expert developers. Here’s the plot they led with in their announcement:

[![](https://substackcdn.com/image/fetch/$s_!WKkF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0da09e40-c175-4859-94d4-3db70f5c7997_1600x972.png)](https://substackcdn.com/image/fetch/$s_!WKkF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0da09e40-c175-4859-94d4-3db70f5c7997_1600x972.png)

Because METR, like all AI Safety Institutes, is run by devout rationalists, the first four bars here are the values of predictions. Everyone asked said AI would speed up development time. The final bar is the observed result. Ackshually, AI slows down development time.

This result inevitably broke the internet. The reaction on Twitter was “Bro, that’s clearly wrong.” The reaction on Bluesky was “See, I told you so.” I didn’t check LinkedIn. I wonder if METR’s cross-posting was itself part of an ethnographic study of confirmation bias.

On Bluesky, [Akhil Rao smartly pointed](https://bsky.app/profile/akhilrao.bsky.social/post/3ltnlbqczbs26) out that the error bar on the speedup is very close to zero and hence *must* be fragile. It’s a good rule of thumb. But he didn’t want to be “the seminar standard errors guy.”

Long-time readers know that horrible standard errors guy is me. I was [ranting about AI papers and error bars last week](https://www.argmin.net/p/standard-error-of-what-now). I wrote a [whole paper](https://arxiv.org/abs/2501.03457) about inferential error bars being a silly exercise unless we are using them as part of a clear regulatory rulebook. And hey, if everyone is freaking out about a study “proving” something with frequentist statistics, I’m going to be the sicko who goes and reads the appendix. You will not be surprised that I think the error bars are made up, even if there’s some interesting ethnography we can take away from METR’s work here.

Here’s a summary of how the study worked:

* METR recruited 16 developers
* All 16 brought approximately 16 coding tasks to the study that they wanted to complete.
* METR assigned each task to one of two conditions at random. Condition 0 is “you can’t use AI.” Condition 1 is “you can use AI.”
* The developers completed their tasks in whichever order they desired. METR recorded the completion time for each task

First, I don’t like calling this study an “RCT.” There is no control group! There are 16 people and they receive *both* treatments. We’re supposed to believe that the “treated units” here are the coding assignments. We’ll see in a second that this characterization isn’t so simple.

As experimenters, our goal is to figure out how the times in Condition 0 compare to those in Condition 1. There are a couple of ways to think about how to study this. If I were to take my guide from the “potential outcomes” school, I’d say something like the following.

There is an intrinsic amount of time each task takes in each condition. Unfortunately, I can only see *one* condition for each task. I can’t complete the tasks *both* with AI and without AI. I thus have a missing data problem. I can only see half of the times I care about in each condition. Perhaps I can use some clever math to estimate the actual average time in each condition *had I seen everything*. And I can use even more clever math to estimate the uncertainty in my estimate. You know, error bars.

This isn’t that crazy if you can sample uniformly at random. Let’s say you have a bunch of playing cards face down on the table in front of you. You want to estimate the proportion of the cards that are red. If you flip half of them uniformly at random, the proportion of red cards in your sample is a reasonable estimate of the proportion of red cars in the sample you didn’t see.

The problem in this study is that there are a bunch of steps required to go from randomizing the tasks to completing the tasks that cloud the estimation problem. These intermediary steps bias your estimation problem. The developers get to choose the order in which they complete the tasks. Task completion order can affect the amount of time it takes you to complete the task. For instance, if you're an expert developer and asked to use a new tool, you'll become faster with it after using it 8 times. Similarly, you can imagine that if you do a bunch of tasks in sequence, your time on task 4 is going to be sluggish because you are tired. There are lots of stories I can tell. There are undoubtedly many conditions that affect the time measurement other than their random assignment.

These other effects are called *spillover* or *interference* effects. In randomized trials, experimentalists work their tails off to remove these effects to ensure they are isolating the effect of the intervention. The ideal experiment satisfies *SUTVA*, the Stable Unit Treatment Value Assumption, which asserts that the only thing that affects a measured outcome is the assignment to the treatment group or the control group. This is a rather strong modeling assumption, but you perhaps could convince yourself that it is close to true in a carefully controlled, blinded study comparing a drug to a placebo.

Unfortunately, SUTVA does not hold in the METR study. And that means we have to bring out the econometrics to tell the difference between the groups. Here’s where we get to wrestle in the mud with statistics. If you go to the appendix of the paper, you can bore yourself to death with regression models and robustness checks. The main model that they use to make the widely circulated plot (from Appendix D on page 27) is this one:

[![](https://substackcdn.com/image/fetch/$s_!0u1x!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7099fd3-5adc-424b-9555-06eb1758f8b8_1548x536.png)](https://substackcdn.com/image/fetch/$s_!0u1x!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7099fd3-5adc-424b-9555-06eb1758f8b8_1548x536.png)

This model more or less says the following: each developer estimates how long a task will take. The median time for each task without AI is a constant times this estimate. The median time with AI is a different constant times the developer estimate. The observed time is the predicted time multiplied by the speedup time for the condition, multiplied by a fudge factor, which is a random variable. The fudge factor is independent of the AI condition, the person’s time estimate, and all of the other fudge factors. The expected value of the fudge factor is one for all tasks. The variance of the fudge factor is the same for all tasks.

That is, if you’d prefer something that looks like code,

```
time(task) = speedup(AI_condition) * est_time(task) * fudge_factor(task)
```

Is that a reasonable model? The AI condition was assigned at random, so it should be independent of the estimated time. But the model assumes everyone experiences the same speed-up/slow-down with the AI tools. Since the fudge factor now includes the developers' choices for the order in which they perform the tasks, they can’t be probabilistically independent.

OK, so the model is not literally true, but perhaps you can convince me that it’s predictive? All models are wrong, amirite? The authors will now provide a bunch of “robustness checks” to convince you that it is close enough. Now we’re spending pages analyzing normal approximations when maybe we should accept that a precise estimate of “speedup” is impossible to measure with this experiment’s design.

After thinking about this for a day, the only data summary I’m happy with would be the following simple analysis: “there are 256 coding tasks, each has an intrinsic time inside of it, when we flip coins we get to see 128 of the times in Condition 1 and 128 of the times in Condition 2. Here are the means and standard deviations of these times.” We could then all move on. I mean, rather than boring us with these robustness checks, METR could just release a CSV with three columns (developer ID, task condition, time). Then the seminar guys can run whatever dumb check they want.[1](https://theory.report/atom.xml#footnote-1)

Let me be clear here, I don’t think METR’s analysis is better or worse than any random quantitative social science study. Measurement in quantitative social sciences is always fraught with an infinite regress of doubt. [That doesn’t mean we can’t tell reasonable qualitative stories with quantitative data.](https://www.argmin.net/p/correlations-and-stories) What we can glean from this study is that even expert developers aren’t great at predicting how long tasks will take. And despite the new coding tools being incredibly useful, people are certainly far too optimistic about the dramatic gains in productivity they will bring.

*Thanks to ‪Sam Anthony, Tilman Bayer‬, ‪Isaiah Bishop‬, ‪Robin Blythe‬, Kevin Chen, ‪Greg Faletto, Apoorva Lal‬, Jordan Nafa, Akhil Rao, Anton Strezhnev, and Stephen Wild for hashing these thoughts out on Bluesky last night.*

[Subscribe now](https://www.argmin.net/subscribe)

[1](https://theory.report/atom.xml#footnote-anchor-1)

METR, if you are reading this, please do it.

By Ben Recht

[Read original post](https://www.argmin.net/p/are-developers-finally-out-of-a-job)
