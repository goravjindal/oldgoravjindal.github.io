---
layout: post
category: cstheoryrss
title: "arXiv: Data Structures and Algorithms: Access Control for Information-Theoretically Secure Key-Document Stores"
date: 2025-07-16T00:00:00
---

**Authors:** [Yin Li](https://dblp.uni-trier.de/search?q=Yin+Li), [Sharad Mehrota](https://dblp.uni-trier.de/search?q=Sharad+Mehrota), [Shantanu Sharma](https://dblp.uni-trier.de/search?q=Shantanu+Sharma), [Komal Kumari](https://dblp.uni-trier.de/search?q=Komal+Kumari)

This paper presents a novel key-based access control technique for secure
outsourcing key-value stores where values correspond to documents that are
indexed and accessed using keys. The proposed approach adopts Shamir's
secret-sharing that offers unconditional or information-theoretic security. It
supports keyword-based document retrieval while preventing leakage of the data,
access rights of users, or the size (\textit{i}.\textit{e}., volume of the
output that satisfies a query). The proposed approach allows servers to detect
(and abort) malicious clients from gaining unauthorized access to data, and
prevents malicious servers from altering data undetected while ensuring
efficient access -- it takes 231.5ms over 5,000 keywords across 500,000 files.

[Read original post](http://arxiv.org/abs/2507.10730v1)
