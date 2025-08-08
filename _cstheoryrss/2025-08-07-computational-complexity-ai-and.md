---
layout: post
category: cstheoryrss
title: "Computational Complexity: AI and ..."
date: 2025-08-07T19:08:00
---

**AI and Vacation**

I'm back from my German vacation. This was my first AI vacation, by which I mean how I used AI to navigate a foreign country. Taking a picture of a hand-written menu board, not just to translate the dishes, but to get a description of each. Visiting a palace with a German-speaking tour guide and translating in real time. Even the more mundane taking pictures of buildings to learn about them.

On the TV I saw something about Künstliche Intelligenz, and Chatty told me it was German for Artificial Intelligence. The Germans use KI instead of AI partly because AI can be confused with Ei (egg). At least that's what AI tells me, so it must be true.

**AI and Math**

At the beginning of my vacation, Google [announced](https://www.nytimes.com/2025/07/21/technology/google-ai-international-mathematics-olympiad.html?unlocked_article_code=1.bk8.du0a.8hQe_TtmUf2T&smid=url-share) that they achieved gold medal status in the International Mathematical Olympiad. An impressive achievement though Terry Tao makes a [good point](https://mathstodon.xyz/@tao/114881418225852441) that comparing an AI system to a time-constrained high-school students is not an apples-to-apples comparison.

I already find talking to AI about math topics quite useful, though it's like talking to an early PhD student. Sometimes they just say things that aren't correct, but usually they are. The reasoning models are particularly good at finding holes in P v NP proofs. For example here's the conclusion of ChatGPT o3-pro's [review](https://chatgpt.com/share/689217d5-a76c-800e-ba24-a64863aef446) of the paper from [Eric's guest post](https://blog.computationalcomplexity.org/2025/08/some-thoughts-on-journals-refereeing.html).

> The paper is a reminder that lower‑bound proofs live or die on the exact breadth of the algorithmic model they exclude—too narrow and the result is unsurprising, too broad and the proof tends to break. At present this work sits in the first category.

What I want to see is AI come up with a solution to an open math problem, a true new insight beyond just some optimized search. I'm not looking for P ≠ NP, just some result that would be publishable in a respectable conference or journal, even just a new completeness result. We haven't really seen that yet, but I suspect we will soon and then we can figure out where math goes from there.

**AI and Bill**

In his presidents [question](https://blog.computationalcomplexity.org/2025/07/a-prez-question-can-ai-do-it-can-you.html) and [solution](https://blog.computationalcomplexity.org/2025/07/answer-to-my-group-onegroup-two-prez.html), Bill states that AI had failed to find the right answer to his problem. Back in June, I saw Bill's draft post and tried AI to solve it.

AI initially failed the test but for a good reason. Bill's initial draft post had Ford and Dole in Group Two because they received LLBs instead of JDs. In the past the LLB was the professional law degree. Yale didn't change to JD until 1971. Ford got his LLB from Yale in 1941.

When I removed Ford and Dole, ChatGPT o3-pro correctly gave the reason for the partition, though it did take over 13 minutes.

> Every name in **Group One** spent time in a law school—most completed a J.D. or LL.B., and the two exceptions (Al Gore and, in some accounts, Lloyd Bentsen) still enrolled in law studies.
>
> * examples – Walter Mondale (University of Minnesota Law) [en.wikipedia.org](https://en.wikipedia.org/wiki/Lloyd_Bentsen?utm_source=chatgpt.com),  
>   JD Vance (Yale Law) [en.wikipedia.org](https://en.wikipedia.org/wiki/JD_Vance?utm_source=chatgpt.com),  
>   Al Gore (attended Vanderbilt Law) [en.wikipedia.org](https://en.wikipedia.org/wiki/Al_Gore?utm_source=chatgpt.com).
>
> No one in **Group Two** ever attended a law school; their highest formal education is in fields such as engineering (Jimmy Carter), economics (George H. W. Bush), business (Donald Trump), political science (Paul Ryan), or acting (Ronald Reagan) [en.wikipedia.org](https://en.wikipedia.org/wiki/Paul_Ryan?utm_source=chatgpt.com)[en.wikipedia.org](https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States_by_education?utm_source=chatgpt.com).
>
> So the distinguishing property is **legal education: every Group One figure went to law school, while none in Group Two did.**

Another [commentor](https://blog.computationalcomplexity.org/2025/07/a-prez-question-can-ai-do-it-can-you.html?showComment=1754336642580#c5249985238648602271) got a similar result for ChatGPT o4-mini-high. I just tried it on Gemini 2.5-Pro and it also gave the correct response, this time in seconds.

On the other hand, E tried several base models and [none of them succeeded](https://blog.computationalcomplexity.org/2025/07/a-prez-question-can-ai-do-it-can-you.html?showComment=1753126370843#c4116460899917207500). The lesson: You want to solve a tricky problem, pony up the $20/month and use a reasoning model.

By Lance Fortnow

[Read original post](https://blog.computationalcomplexity.org/2025/08/ai-and.html)
