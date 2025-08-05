---
layout: post
category: cstheoryrss
title: "Computational Complexity: Some thoughts on journals, refereeing, and the P vs NP problem"
date: 2025-08-04T16:46:00
---

*A guest post by Eric Allender prompted by an**(incorrect) P ≠ NP proof**[recently published](https://doi.org/10.1007/s11704-025-50231-4) in Springer Nature's Frontiers of Computer Science.*

For a time, I served as Editor-in-Chief of ACM Transactions on Computation Theory, and in this role I had to deal regularly with submissions that claimed to resolve the P vs NP problem. Finding referees for these papers was sometimes challenging, so I frequently ended up reviewing them myself.  Dealing with such submissions involves enough overhead that ToCT, J.ACM and ACM Transactions on Algorithms limit the frequency with which authors can submit work of this sort.  But for every submission, on any topic, the overall process was the same: Find someone on the Editorial Board who has sufficient expertise to find referees and make knowledgeable use of their recommendations.  If there was no such person on the Editorial Board, then it was always the case that the submission was out of scope for the journal.

These thoughts are brought to mind by a recent case, where it seems to me that the editorial process broke down.

Springer publishes several high-quality academic journals that deal with Theoretical Computer Science.  One Springer journal, Frontiers of Computer Science, recently published an article entitled [SAT Requires Exhaustive Search](https://doi.org/10.1007/s11704-025-50231-4), where one of the authors is a Deputy Editor-in-Chief of the journal.  The abstract of the article states that it proves a result that is stronger than P not equal to NP.  The Editorial Board of the journal has some members who are expert in computational complexity theory.  However, all the ones whom I know personally have asserted that they had no knowledge of this paper, and that they were not involved at all in handling the paper.

When Ryan Williams and I learned about the publication of this article, we drafted a [comment](https://people.cs.rutgers.edu/~allender/papers/allender.williams.pdf), which we sent to the Editor-in-Chief.  We recommended that the paper be retracted, in which case there would be no need to publish our comment.  However, the Editor-in-Chief declined to retract the article, saying that he could find no evidence of misconduct, and thus we have been assured that an edited version of our comment will appear in the journal.

Our comment calls attention to some shortcomings in the proof of the main theorem (similar to shortcomings in several other failed attempts to separate P from NP).  But we were able to say more.  Often, when one is looking for bugs in a purported proof, one has to deal with the situation where the claimed theorem is probably true, and the only problem is that the proof is not convincing.  However, the main theorem in their paper (Theorem 3.2) states that a particular constraint satisfaction problem requires time more than \(d^{cn}\) for any constant \(c<1\) (where \(d\) is the domain size, and \(n\) is the number of variables).  In particular, their purported proof claims that this holds even when \(k=2\) (meaning that each constraint has at most 2 variables).  However, Ryan Williams [presented an algorithm](https://doi.org/10.1016/j.tcs.2005.09.023) more than two decades ago that runs in time \(O(d^{(0.8)n})\) in this special case, contradicting the lower bound claimed in the article.

The article contains an appendix, with glowing testimonies from various researchers; the lead-in to the appendix also contains enthusiastic comments from Gregory Chaitin.  I contacted Gregory Chaitin, and he asserts that he did not read the paper, and that he was quoted out of context.

The edited version of the [comment](https://people.cs.rutgers.edu/~allender/papers/allender.williams.pdf) that Ryan Williams and I wrote, which will supposedly appear in Frontiers of Computer Science soon, differs from the version linked here (our original submission) primarily in one respect:  Our closing paragraph was removed.  Here is that paragraph:

> Finally, it is our opinion that the publication of this article is a complete embarrassment to this journal and its publisher. We believe that, at the very least, the paper should be withdrawn, and Springer should conduct an investigation to understand how such a paper could have made it through the peer review process.

By Lance Fortnow

[Read original post](https://blog.computationalcomplexity.org/2025/08/some-thoughts-on-journals-refereeing.html)
