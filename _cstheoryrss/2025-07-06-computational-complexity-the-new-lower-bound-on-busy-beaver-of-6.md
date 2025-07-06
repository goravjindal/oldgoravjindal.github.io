---
layout: post
category: cstheoryrss
title: "Computational Complexity: The New Lower Bound on Busy Beaver of 6."
date: 2025-07-06T12:51:00
---

 We denote the busy beaver function by BB.

BB(n) is the max time a Turing machine of size n takes to halt on the empty string.

(A particular model of TM and a notion of size has become standardized.)

BB(n) grows faster than any computable function. That is obviously interesting. What is less obvious (and  some of my co-bloggers disagree) the pursuit of actual values of BB is interesting. For an excellent overview of the BB numbers, written in 2020 (that is relevant) by Scott Aaronson, see [here](https://www.cs.umd.edu/~gasarch/open/busybeaver.pdf). (Computable and Aaronson are flagged by my spell check but I think they are spelled correctly.)

When Scott's article appeared, BB(5) was not known. In June 2024 the value of BB(5) was discovered.  See Scott's blog on this, [her](https://scottaaronson.blog/?p=8088)e. The value of BB(5) isn't even that big- its just 47,176,870. That's one of those numbers that is SMALL now but would have been LARGE in (say) 1964 (see my blog about a different number of that type [here](https://blog.computationalcomplexity.org/2019/05/ronald-grahams-other-large-number-well.html)).

What about BB(6)?

No, I am not going to announce that Scott announced it is now known.

I am going to announced that Scott announced better *lower bounds* for BB(6) are now known.

I won't restate the lower bounds since (a) Scott already has, and (b) typesetting the bounds is hard (for me).

SO, what to make of all this?

1) At the time of Scott's article it looked like BB(6) was large. How large was hard to say. Intuitions about how large BB(6) would be are hard to come by, so the new result is neither surprising nor unsurprising.

2) We will never know BB(6). Shucky Darns!

3) Many of the results on BB are not published in refereed journals. However, the ones mentioned in the context of BB(5) and BB(6) were verified in Coq.  I doubt other parts of math could take this approach;  however, it is interesting that results can be verified via computer in this field. Indeed- I doubt  referee could verify the results without a computer aid.

4) Why the interest in BB? Some speculation

a) Computing power is such that one can actually get out some results (read Scott's blog on BB(5) for more on that).

b) The internet: there are not that many people working on BB but those that are can easily communicate with each other.

c) Scott's article and his blog posts on it helped generate interest. Since I asked Scott to write the article for my open problems column, I get some credit here also (very little).

d) Results generate interest, and interest generates results.

e) Items a,b,c,d,e all help to reinforce each other.

By gasarch

[Read original post](https://blog.computationalcomplexity.org/2025/07/the-new-lower-bound-on-busy-beaver-of-6.html)
