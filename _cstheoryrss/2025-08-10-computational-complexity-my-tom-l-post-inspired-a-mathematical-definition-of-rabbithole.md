---
layout: post
category: cstheoryrss
title: "Computational Complexity: My Tom L post inspired a mathematical definition of Rabbithole"
date: 2025-08-10T19:41:00
---

NICK: I read and enjoyed your blog post on Tom L (see [here](https://blog.computationalcomplexity.org/2025/07/tom-lehrer-passed-away-at-age-of-97.html)). I then spent 40 minutes down a rabbithole listening to his music on YouTube.

BILL: You call that a rabbit hole?!  A while back I spent 3 hours reading questions and answers on quora ranging from is *Michelle Obama actually a man?* to *Is Donald Trump the Anti-Christ?* (The answer to both is no.) THATS a rabbithole. Listening to Tom L is not.

NICK: SO... what is and isn't a rabbit hole? Also, is it rabbithole or rabbit hole?

BILL: Spellcheck is happy with rabbithole, hence so am I. As to your question,  we need a function \(f\) and a threshold \(T\) such that

if you spend \(x\) minutes on A, and

you get y enjoyment out of it, where \(0\le y\le 10\), and

\(f(x,y)\ge T\)

then A is a  rabbithole.

(Note- I was kidding. There can't possibly be a function f that works.)

ONE DAY LATER

NICK: I asked Gemini  what \(f\) and \(T\) are  and it told me:

\(f(x,y) = \frac{x}{y+1} \) and

\(T=20\).

It also gave me some examples:

1) The Tom L. Example: 40 mins, 8/10 enjoyment. Score 4.44. NOT a Rabbit Hole!

2) Doomscrolling: 90 mins, 1/10 enjoyment. Score  45. Rabbit Hole!

3) Binge-Watching Mediocre TV: 3 hours (180 mins), 4/10 enjoyment. Score = 36. Rabbit Hole!

4) Incredible Documentary: 3 hours (180 mins), 9/10 enjoyment.  18. Worthwhile but its close.

Gemini also output a heatmap, see [here](https://www.cs.umd.edu/~gasarch/BLOGPAPERS/rabbithole.png).

BILL: Uh- I was only kidding.

NICK: Well, the jokes on you.

By gasarch

[Read original post](https://blog.computationalcomplexity.org/2025/08/my-tom-l-post-inspired-mathematical.html)
