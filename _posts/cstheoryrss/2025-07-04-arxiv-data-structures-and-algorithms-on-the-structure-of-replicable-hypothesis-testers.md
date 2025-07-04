---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: On the Structure of Replicable Hypothesis Testers"
date: 2025-07-04T00:00:00
---

**Authors:** [Anders Aamand](https://dblp.uni-trier.de/search?q=Anders+Aamand), [Maryam Aliakbarpour](https://dblp.uni-trier.de/search?q=Maryam+Aliakbarpour), [Justin Y. Chen](https://dblp.uni-trier.de/search?q=Justin+Y.+Chen), [Shyam Narayanan](https://dblp.uni-trier.de/search?q=Shyam+Narayanan), [Sandeep Silwal](https://dblp.uni-trier.de/search?q=Sandeep+Silwal)

A hypothesis testing algorithm is replicable if, when run on two different
samples from the same distribution, it produces the same output with high
probability. This notion, defined by by Impagliazzo, Lei, Pitassi, and Sorell
[STOC'22], can increase trust in testing procedures and is deeply related to
algorithmic stability, generalization, and privacy. We build general tools to
prove lower and upper bounds on the sample complexity of replicable testers,
unifying and quantitatively improving upon existing results.
We identify a set of canonical properties, and prove that any replicable
testing algorithm can be modified to satisfy these properties without worsening
accuracy or sample complexity. A canonical replicable algorithm computes a
deterministic function of its input (i.e., a test statistic) and thresholds
against a uniformly random value in $[0,1]$. It is invariant to the order in
which the samples are received, and, if the testing problem is ``symmetric,''
then the algorithm is also invariant to the labeling of the domain elements,
resolving an open question by Liu and Ye [NeurIPS'24]. We prove new lower
bounds for uniformity, identity, and closeness testing by reducing to the case
where the replicable algorithm satisfies these canonical properties.
We systematize and improve upon a common strategy for replicable algorithm
design based on test statistics with known expectation and bounded variance.
Our framework allow testers which have been extensively analyzed in the
non-replicable setting to be made replicable with minimal overhead. As direct
applications of our framework, we obtain constant-factor optimal bounds for
coin testing and closeness testing and get replicability for free in a large
parameter regime for uniformity testing.
We also give state-of-the-art bounds for replicable Gaussian mean testing,
and, unlike prior work, our algorithm runs in polynomial time.