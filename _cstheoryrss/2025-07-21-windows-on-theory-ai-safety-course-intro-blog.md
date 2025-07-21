---
layout: post
category: cstheoryrss
title: "Windows on Theory: AI Safety Course Intro Blog"
date: 2025-07-21T02:34:35
---

I am teaching [CS 2881: AI Safety](https://boazbk.github.io/mltheoryseminar/) this fall at Harvard. This blog is primarily aimed at students at Harvard or MIT (where we have a cross-registering agreement) who are considering taking the course. However, it may be of interest to others as well. For more of my thoughts on AI safety, see the blogs [Six Thoughts on AI safety](https://windowsontheory.org/2025/01/24/six-thoughts-on-ai-safety/) and [Machines of Faithful Obedience](https://windowsontheory.org/2025/06/24/machines-of-faithful-obedience/).

**IMPORTANT:** At the end of this blog is **Homework Zero**. If you are a Harvard or MIT student that is interested in taking the course, then you will need to submit this homework to apply for a seat. See details below.

## Why AI Safety?

If you are considering taking this course, you are probably aware that there is a significant chance that AI will cause profound changes to our world over the next years and decades. However, there is significant disagreement about the magnitude of these changes, as well as whether they will be positive or negative.  
  
Here is an illustrative plot of various potential scenarios for the next decade that people had predicted. (The GDP and life expectancy numbers are just illustrative- these were not explicitly predicted by the cited people, but are o3’s interpretations of the scenarios, see appendix below.)

[![](https://windowsontheory.org/wp-content/uploads/2025/07/scenarios.jpg?w=656)](https://windowsontheory.org/wp-content/uploads/2025/07/scenarios.jpg)

As the saying goes, predictions are hard, especially about the future. Even the most AI-hawkish predictors sometimes underestimate its advances. For example, Paul Christiano has [predicted](https://www.lesswrong.com/posts/sWLLdG6DWJEy3CH7n/imo-challenge-bet-with-eliezer) a less than 8% chance of AI achieving [IMO gold performance by 2025](https://x.com/OpenAI/status/1946594928945148246). (You can decide what this means for interpreting his [predictions](https://www.dwarkesh.com/p/paul-christiano) of a 15% chance for a [Dyson Sphere](https://en.wikipedia.org/wiki/Dyson_sphere) by 2030 and 40% by 2040.)  
  
Anything between utopia and catastrophe has been predicted. Clearly, we would like the impact of AI in 2035 to be up and to the right in this plot. This course will focus on what we know about the technical aspects of how we can get there,  and particularly on avoiding the bottom left quadrant.

We will have a particular focus on two aspects: **measurement** and **scale**.

There is a famous saying, “You can’t improve what you don’t measure.” In AI, we often encounter the converse as well; time and again, we have found that once we can measure an objective, we can also improve upon it. Alignment and safety often make the measurement task more complex: the phenomena we deal with could involve worst-case behavior, complex interactions of multiple components (both human and AI), behaviors such as “cheating” that are not always easy to define. Hence, measurements and evaluations will play a significant part in this course.

The other component is *scale*. The fundamental property of current AI systems is that they are not static – they constantly grow in the resources they use (data, compute), their capabilities, and their scope of implementation and influence. For every type of safety concern, we need to ask ourselves, is this a problem that would get better or worse with scale. Similarly, for every safety intervention we need to ask whether this is a method that would work better or worse with scale.

## Topics

A list of questions that we may\* consider in this course includes:

* What are the potential risks and benefits of AI?
* What potential capabilities of AI could lead to catastrophic risks? For which ones do we think that AI can also be used to help defend against the risk?
* What lessons can we learn from other fields, including aviation and transportation safety, computer security, and others.
* Is there a tension between capabilities and safety? Which current safety methods become better as capabilities improve, and which ones become worse?
* How can we obtain “leading indicators” to measure potential for catastrophic risk before it happens?
* What aspects of AI training process can lead to increased risk? This includes phenomena such as reward hacking, scheming, alignment faking, etc..
* When AI behaves in “bad” ways, can we always trace it back to either their dataset or the objectives they trained on?
* How do we even define precisely notions such as “scheming”, “sandbagging”, “reward hacking”, “unfaithfulness”?
* What is the goal for alignment – AI following instructions by humans? AI having good values? Something else?
* What are the ways to evaluate AIs for safety?
* Can we make AI models robust to adversaries who can modify their inputs? Are there fundamental limitations to this? Does making models adversarially robust requires making them less capable on non-adversarial inputs?
* What are the unique safety aspects that arise when AI is being used to build future versions of itself?
* What are ways to understand the reasoning of why models provide certain outputs – white box, black box, and intermediate (e.g., access to privileged outputs such as “chain of thought”) methods? Are there ways that only white-box methods can achieve and not black-box ones?
* What is the role of “model organisms” – specific examples designed to exhibit specific behavior.
* How will AI impact individual freedoms?  mass surveillance, etc..
* How will AI impact warfare?  international stability.
* How can we do “unlearning” for either safety or privacy.
* As AI tools become more capable, how does this translate into an increase in need for model weight security?
* What are prompt injection attacks and how can we defend against them.

\* We will likely not get to many of those, and we will see what we cover as we go along.

## Homework Zero

In order to maintain the ability for effective discussion, as well as due to compute limitations, we will cap the number of students in the course. If you are a Harvard or MIT student and are interested in the course, you will need to submit the following “homework zero” to apply to join. Submitting homework zero does not guarantee you a place in the course, but hopefully, you will find doing it interesting and rewarding regardless.  You will be reimbursed up to $40 for compute expenses in doing this project.

The homework will be to replicate a variant of the “[emergent misalignment](https://arxiv.org/abs/2502.17424)” paper by Betley et al., specifically following the work of [Turner et al](https://arxiv.org/abs/2506.11613).  
  
If you are a Harvard or MIT student that. have filled out the [course interest form](https://forms.gle/csF2BAwviLMNt48J7) then you will get an invite to the repository with code and instructions for submissions.. Please sign up to it with the same email you use for registering to courses (your Harvard key email address). The homework will be due on **11:59pm eastern Monday August 4 2025**.

---

## Appendix: o3’s summary of predictions

Following is o3’s summary of AI forecasters predictions. (I’ve used multiple prompts/conversations to get it in the right format, which makes it less convenient to share the conversation. Hence I just copy pasted here the bottom line and some links that o3 came up with)

### **• AI Stagnation (“New AI Winter / Plateau”)**

* **Predictors & docs** – Centre for Future Generations *Plateau* scenario; FT “bear‑case for AI” analysis.[Centre for Future Generations](https://cfg.eu/advanced-ai-possible-futures/) [Financial Times](https://www.ft.com/content/42bad56f-02cc-4b32-b9ac-1af5dbc7bc83?utm_source=chatgpt.com)
* **GDP (% y/y)** 2  2  2  2  1.8  1.8  1.7  1.7  1.6  1.6 → **+19.8 % cum** *“AI capabilities hit a hard ceiling … throwing more resources at them yields sharply diminishing returns.”* [Centre for Future Generations](https://cfg.eu/advanced-ai-possible-futures/)
* **Life‑expectancy (yr)** +0.10 each year → **+1.0 yr**
* **Employment (% of global jobs)** little net change; automation plateaus (<0.3 % loss p.a.).
* **Deaths by violence (2036‑‑45)** ≈ 3 M, unchanged from 2010s average (no major AI wars).
* **Other QoL** Incremental health/ed tech; freedoms unchanged.

---

### **• AI Utopia (“Machines of Loving Grace”)**

* **Predictors & docs** – Dario Amodei essay; Goldman Sachs research (+1.5 pp prod. boost); Ray Kurzweil longevity claims.[darioamodei.com](https://www.darioamodei.com/essay/machines-of-loving-grace?utm_source=chatgpt.com) [Goldman Sachs](https://www.goldmansachs.com/insights/articles/generative-ai-could-raise-global-gdp-by-7-percent?utm_source=chatgpt.com) [Fortune](https://fortune.com/well/article/a-i-radically-lengthen-lifespan-ray-kurzweil/?utm_source=chatgpt.com)
* **GDP (% y/y)** 4.5 ×10 → **+55 % cum** (baseline 34 % +21 pp)  
  *“Generative AI could lift productivity growth by 1.5 percentage‑points over a decade.”* [Goldman Sachs](https://www.goldmansachs.com/insights/articles/generative-ai-could-raise-global-gdp-by-7-percent?utm_source=chatgpt.com)
* **Life‑expectancy (yr)** +0.80 each yr → **+8 yr** *Kurzweil: “by the end of the 2030s we will largely overcome diseases and the aging process.”* [Fortune](https://fortune.com/well/article/a-i-radically-lengthen-lifespan-ray-kurzweil/?utm_source=chatgpt.com)
* **Employment** creative expansion; net +0.5 % jobs p.a. (WEF “Jobs of Tomorrow” on trainer/explainer roles).[World Economic Forum](https://www.weforum.org/stories/2023/09/jobs-ai-will-create/?utm_source=chatgpt.com)
* **Violent deaths** < 1 M / decade (AI‑enabled early‑warning & mediation).
* **Other QoL** Universal AI tutors & doctors, near‑zero cost goods, high civil liberties.

---

### **• AI Catastrophe (“Unaligned Power‑Seeker”)**

* **Predictors & docs** – Geoffrey Hinton extinction warnings; Carlsmith existential‑risk report.[The Guardian](https://www.theguardian.com/technology/2024/dec/27/godfather-of-ai-raises-odds-of-the-technology-wiping-out-humanity-over-next-30-years?utm_source=chatgpt.com) [arXiv](https://arxiv.org/abs/2206.13353?utm_source=chatgpt.com)
* **GDP** +3 % first 3 yrs then ‑20 %, ‑10 %, ‑2 % … ⇒ **‑30 % cum** (global collapse).
* **Life‑expectancy** ‑3 yr p.a. from year‑4 ⇒ **‑30 yr**.
* **Employment** Irrelevant after takeover; human economic agency ≈ 0.
* **Deaths** Up to 7 Bn (existential level).  
  *Hinton: “10–20 % chance AI could wipe out humanity within 30 years.”* [The Guardian](https://www.theguardian.com/technology/2024/dec/27/godfather-of-ai-raises-odds-of-the-technology-wiping-out-humanity-over-next-30-years?utm_source=chatgpt.com)
* **Other QoL** Human rights & freedom → zero.

---

### **• Technofeudal Oligarchy**

* **Predictors & docs** – Scott Alexander et al. “AI 2027” technofeudal path; Stiefenhofer 2025 paper on AGI & inequality.[Astral Codex Ten](https://www.astralcodexten.com/p/ama-with-ai-futures-project-team?utm_source=chatgpt.com) [arXiv](https://arxiv.org/abs/2503.14283?utm_source=chatgpt.com)
* **GDP** 6 % p.a. → **+79 % cum**
* **Life‑expectancy** +0.50 yr p.a. → **+5 yr** (but unequal access).
* **Employment** ‑3 % p.a. (‑26 % cum); wealth captured by <0.1 % elite.
* **Deaths** < 2 M (stable order, high surveillance).
* **Other QoL** Top‑tier healthcare and education for elites; mass population under tight algorithmic control, low civil liberties.

---

### **• AI Arms Race & Hot Conflict**

* **Predictors & docs** – CFG *Arms race* narrative; European‑Parliament brief on “AI war lab” in Ukraine; New Yorker war‑games piece.[Centre for Future Generations](https://cfg.eu/advanced-ai-possible-futures/) [European Parliament](https://www.europarl.europa.eu/RegData/etudes/BRIE/2025/769580/EPRS_BRI%282025%29769580_EN.pdf?utm_source=chatgpt.com) [The New Yorker](https://www.newyorker.com/magazine/2025/07/21/is-the-us-ready-for-the-next-war?utm_source=chatgpt.com)
* **GDP (% y/y)** 3  3  3  0  ‑2  ‑2  1  1  2  2 → **+11 % cum**
* **Life‑expectancy** flat then ‑0.2 yr in war yrs ⇒ **‑1 yr**.
* **Employment** initial militarised boom (+1 %) then ‑4 % per war year; net ‑6 % decade.
* **Deaths** Major‑power war: 30–50 M combat & civilian casualties (RAND/ICRC autonomy escalation warnings).[RAND Corporation](https://www.rand.org/pubs/commentary/2020/06/the-risks-of-autonomous-weapons-systems-for-crisis.html?utm_source=chatgpt.com)
* **Other QoL** Civil liberties curtailed; R&D diverted from health/education to defence.

---

### **• Global Co‑operation on Safe AI**

* **Predictors & docs** – CFG *Diplomacy* scenario; OECD foresight note; 2024 Council‑of‑Europe AI Treaty.[Centre for Future Generations](https://cfg.eu/advanced-ai-possible-futures/) [OECD](https://www.oecd.org/content/dam/oecd/en/about/programmes/strategic-foresight/GSG%20Background%20Note_GSG%282024%291en.pdf/_jcr_content/renditions/original./GSG%20Background%20Note_GSG%282024%291en.pdf?utm_source=chatgpt.com) [Illinois Law Review](https://illinoislawreview.org/online/the-first-global-ai-treaty/?utm_source=chatgpt.com)
* **GDP** 4 % p.a. → **+48 %**
* **Life‑expectancy** +0.60 yr p.a. → **+6 yr** (shared breakthroughs).
* **Employment** managed transition; net ‑0.5 % first half, +0.5 % later ⇒ flat overall.
* **Deaths** < 1.5 M (arms‑control lowers risks).
* **Other QoL** Robust human‑rights guard‑rails, broad access to AI medicine & education.

---

### **• Mass Automation Shock**

* **Predictors & docs** – McKinsey 400‑800 M displacement; WEF April 2025 entry‑level job concerns.[McKinsey & Company](https://www.mckinsey.com/featured-insights/future-of-work/jobs-lost-jobs-gained-what-the-future-of-work-will-mean-for-jobs-skills-and-wages) [World Economic Forum](https://www.weforum.org/stories/2025/04/ai-jobs-international-workers-day/?utm_source=chatgpt.com)
* **GDP** 4 % p.a. → **+48 %** (higher prod.)
* **Life‑expectancy** +0.30 yr p.a. → **+3 yr** (cheap AI health, but stress/inequality).
* **Employment** ‑2.3 % p.a. ⇒ **‑21 %** decade (roughly 600 M net jobs lost).
* **Deaths** 2–4 M from unrest & indirect effects.
* **Other QoL** Sharp inequality spike; possible UBI debates; mental‑health strains.

---

### **• Digital Authoritarianism**

* **Predictors & docs** – Lawfare “Authoritarian risks of AI surveillance”; Bulletin piece on erosion of democracy; Euro‑Parl study on AI repression.[Lawfare](https://www.lawfaremedia.org/article/the-authoritarian-risks-of-ai-surveillance?utm_source=chatgpt.com) [Bulletin of the Atomic Scientists](https://thebulletin.org/2024/06/how-ai-surveillance-threatens-democracy-everywhere/?utm_source=chatgpt.com) [European Parliament](https://www.europarl.europa.eu/RegData/etudes/IDAN/2024/754450/EXPO_IDA%282024%29754450_EN.pdf?utm_source=chatgpt.com)
* **GDP** 4 % p.a. → **+48 %** (tech‑driven growth)
* **Life‑expectancy** +0.35 yr p.a. → **+3.5 yr**
* **Employment** ‑0.5 % p.a. (state‑run economy, limited labour voice).
* **Deaths** State violence + AI policing ≈ 5 M over decade.
* **Other QoL** Pervasive facial‑recog & social‑credit; freedoms very low despite material gains.

---

### **• AI Chaos & Decentralised Disruption**

* **Predictors & docs** – IBM on open‑source risks; DHS report on adversarial Gen‑AI; ENISA 2030 cyber threat foresight; Tom’s‑Hardware malware demo.[IBM](https://www.ibm.com/think/insights/unregulated-generative-ai-dangers-open-source?utm_source=chatgpt.com) [U.S. Department of Homeland Security](https://www.dhs.gov/sites/default/files/2025-01/25_0110_st_impacts_of_adversarial_generative_aI_on_homeland_security_0.pdf?utm_source=chatgpt.com) [ENISA](https://www.enisa.europa.eu/sites/default/files/publications/ENISA%20Foresight%20Cybersecurity%20Threats%20for%202030.pdf?utm_source=chatgpt.com) [Tom’s Hardware](https://www.tomshardware.com/tech-industry/cyber-security/ai-malware-can-now-evade-microsoft-defender-open-source-llm-outsmarts-tool-around-8-percent-of-the-time-after-three-months-of-training?utm_source=chatgpt.com)
* **GDP** 3  3  2.5  2  1.5  1  1  1.5  2  2 → **+22 %**
* **Life‑expectancy** +0.25 yr p.a. minus 0.5 yr lost to crises ⇒ **+(-0.8) yr net**
* **Employment** volatile; cyber‑crime & trust collapses cost 10 % of jobs by 2035.
* **Deaths** 10–15 M from scattered AI‑aided terror, bio‑incidents & infrastructure failures.
* **Other QoL** Fragmented internet, high misinformation; governments swing between over‑regulation and impotence.

By Boaz Barak

[Read original post](https://windowsontheory.org/2025/07/20/ai-safety-course-intro-blog/)
