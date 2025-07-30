---
layout: post
category: cstheoryrss
title: "Gil Kalai: Some Questions from Recent Quantum Events"
date: 2025-07-29T23:00:53
---

Over the past few years, I have given several lectures about quantum computation, presenting my argument for why quantum computing—and even significant early milestones toward it—are fundamentally impossible. Recently, I participated in a debate with [Matthias Christandl](https://researchprofiles.ku.dk/en/persons/matthias-christandl) on the [possibility of quantum computing](https://www.learned.cz/en/activities/news/quantum-duel-quantum-computers-do-they-exist-20-may-2025.html), which took place in Prague. During these events, people raised many insightful questions. (Additional questions are welcome.)

Below are (with some overlap) questions from talks at the Perimeter Institute, Rutgers University, The “[quantum duel”](https://www.learned.cz/en/activities/news/quantum-duel-quantum-computers-do-they-exist-20-may-2025.html) with Matthias hosted by the Czech Learned Society, NextSilicon, and the Ethereum Foundation. (The lecture in Ethereum Foundation was in connection with the company’s hesitation about post-quantum cryptography; and some questions were related to this matter.) I conclude with a recent question (over FB) from Aram Harrow, who was my partner in a year-long debate in 2012.

### Perimeter Institute, Dec. 2022 [(video)](https://pirsa.org/22120066); Three questions by Ray Laflamme.

I recently heard the sad news that Ray Laflamme passed away. Ray Laflamme was an eminent researcher in both the theoretical and the experimental aspects of quantum computing. Here are  links to beautiful tributes to Ray by [Scott Aaronson](https://scottaaronson.blog/?p=8949), and by [Nicole Yunger Halpern.](https://quantumfrontiers.com/2025/07/27/little-ray-of-sunshine/)  I met Ray in person [only once](https://scottaaronson.blog/?p=8949#comment-2011830), at a 2013 conference *QSTART,* which we organized in Jerusalem to inaugurate our Quantum Science Center.

In my [lecture at PI](https://pirsa.org/22120066) (click for abstract and video), Ray  (at 55:10) started the discussion with the following three questions:

**Q1**: In your “goal number three,” you mentioned surface codes, and and there were very nice experiments from the summer (2022) that Google published with surface codes of distance 3 with 17 qubits and another one of distance 5 with 49 qubits. They showed that by using distance 5 they had a slight improvement of the effective error rate. Would this experiment, if it becomes better and go to distance 7 and 9, shed doubts on your argument that quantum computers are impossible?

**Q2**: About the lowest realistic possible rate of noise that you refer to as a fundamental constant of nature ( ![🙂](https://s0.wp.com/wp-content/mu-plugins/wpcom-smileys/twemoji/2/72x72/1f642.png)  ); do you have a number for that?

**Q3**: Does this putative “constant of nature” tells us there is something wrong with quantum mechanics?

There were a several follow-up questions and comments including by Lee Smolin and by Debbie Leung (for Ray’s Q3) and by Latham Boyle (who hosted the lecture) and others (for Ray’s Q2). Latham asked about the details of the argument that I presented in the lecture in order to verify that it is not circular—namely, he questioned whether the argument implicitly assumes that gate errors cannot be decreased below the threshold in order to derive this as a conclusion. (I explained why the argument is indeed not circular.)

[![](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/rl13-8.png?w=640)](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/rl13-8.png)

A question from me to Ray Laflamme in our [QSTART](https://gilkalai.wordpress.com/2013/04/12/qstart/) conference, July 2013; Ray gave a beautiful [opening talk](https://youtu.be/F4K1qL44icw?si=I3vrpp-PttP19RCJ) on experimental quantum error correction.

### [Physics colloquium](https://www.physics.rutgers.edu/colloqvid/GMT20221019.mp4) hosted by Daniel Friedan in Rutgers University, 2022

In October 2022, I gave the [physics colloquium](https://physics.rutgers.edu/events/events-calendar/icalrepeat.detail/2022/10/19/8148/-/the-argument-against-quantum-computers) at Rutgers University. Here is [the video recording](https://www.physics.rutgers.edu/colloqvid/GMT20221019.mp4).

**Q4** [Pierre [Coleman]:](https://www.physics.rutgers.edu/~coleman/) The crucial test for any theory in physics is whether it can be falsified. I did not see in all your proposals how we can test if your theory is correct or false. Do you have a proposed experiment?

**Q5** [Scott [Thomas]](https://physics.rutgers.edu/people/faculty-list/faculty-profile/thomas-scott): How do your ideas impact proposals for topological quantum computers?

**Q6** [Tom Banks](https://physics.rutgers.edu/people/faculty-list/faculty-profile/banks-tom): Why is it hard to compute permanents (in view of techniques that apply to Gaussian ensembles and are used for quantum field theory)?

**Q7** [Ananda Roy](https://sites.rutgers.edu/ananda-roy/): Isn’t [the bulb](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/ldp2.jpg) describing your computational class LDP getting larger and larger with smaller error rates?

**Q8** [Daniel Friedan](https://en.wikipedia.org/wiki/Daniel_Friedan): Physicists have a tendency to regard any mathematical theorem referring to their work as a challenge to evade the theorem’s assumptions. In this spirit, would a very special local form of noise for boson sampling evade the conclusion of your theorem?

## The Quantum Duel with Matthias Christandl

[![](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/duel1.jpg?w=640)](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/duel1.jpg)

Here are some questions from the duel. The [quantum duel with Matthias](https://www.learned.cz/en/activities/news/quantum-duel-quantum-computers-do-they-exist-20-may-2025.html) and the entire week organized by the [Czech Learned Society](https://www.learned.cz/en/) were thought-provoking, and I will devote a special post to it. **Q9-Q23** below were raised and discussed in the second hour of the debate.

**Q9** (from the audience to Gil): You claimed that there is a fundamental obstacle to quantum computation; it was not concrete, what is the nature of your objection.

**Q10**  (Matthias to Gil): You claim that noise will remain above a certain constant. If true this will be an obstacle. What is the number?! (Once we have the number, we have it now on tape, we can see in a few years if we beat this number, yes or no!

**Q10** (Follow-up question from Matthias): Now, that I got this number, how does this constant come from quantum physics (or from some modification of quantum mechanics)?!

**Q11** ([Martin Loebl](https://kam.mff.cuni.cz/~loebl/), our host, addressed  to both of us): Why do these quantum computers (and quantum error-correction) not exist in nature?

**Q12** [Ronald de Wolf](https://en.wikipedia.org/wiki/Ronald_de_Wolf) to Gil (from chat): Noisy classical circuits are a special class of noisy quantum circuits. If noisy quantum circuits can only compute some low level complexity class then the same should be true for noisy classical circuits.  (In other words, if quantum computation is not possible why is classical computation possible?)

**Q13** (from chat to Mathias): Do you believe that Majorana Zero Modes can generate topological quantum qubits?

**Q14**: (Alexander Zykov): Let’s assume that the noisy quantum circuits will always remain noisy (above the threshold). Can we still use them for accelerating classical computation or achieving useful approximations?

**Q15** (to Gil): Do Google’s 2024 error correcting codes falsify your argument?

**Q16** to Matthias: Earlier you claimed that we are quantum computers. Can you please factor 1522605027922533360535618378132637429718068114961380688657908494580122963258952897654000350692006139?

**Q17** Implementations are energy-inefficient, at least for ion trapped quantum computation.  Wouldn’t this be a problem for scaling?

**Q18** Can “expectation bias”  cause researchers and the community to misjudge the quality of experiments?

**Q19** How large numbers can we factor in 10 years?

**Q20** ([Marc Mézard](https://en.wikipedia.org/wiki/Marc_M%C3%A9zard)): We do have efficient quantum devices; Is it possible, then, that QC in the next 50 years will achieve only niche computation and not universal quantum computation?

**Q21** Given Gil’s argument about  NISQ systems,  Why isn’t it considered an open and shut case? Why do we still have debate? Why is this argument dismissed by the experts?

**Q22**  (to Gil:) What is the significance of the intermediate scale in your argument?

**Q23** (to Matthias) With quantum computers will we observe superposition of macroscopic systems?

Some [additional questions](https://app.sli.do/event/arNRx6NJFsqSrPbdsk5UYZ/live/questions) were asked in chat during the live streaming but we did not get to them in the debate itself. (I wrote my answers to some of them and they are presented in the [debate’s website](https://www.learned.cz/en/activities/news/quantum-duel-gil-kalai-matthias-christandl-a-recording-of-the-debate.html).)

**Q 24** (Addressed to both Gil and Matthias, from chat): Why do both of you regard the claims about quantum topological qubits as unconvincing.

**Q25** (to Gil): From what I understand, you believe this is an engineering challenge and not exactly a matter of physics (theoretical, to be precise). If yes, should not the debate involve a quantum engineer?

**Q26** (to both): Could you both debate more about where your models of quantum computers differ? How is it possible that you reach different conclusions?

**Q27**  (Addressed to both participants): Two-qubit gates always involve non-computational states, introducing a tradeoff between speed, leakage and errors (when “fixing” the leakage). That might be a microscopic origin of irreducible noise. Do we have definite knowledge about the impact of non-computational states on the error rates?

**Q28**   to Gil: in your answer to Ronald you mentioned that LDP of NISQ is not an obstacle to harder classical computation. Why may it also NOT be an obstacle to fault-tolerant quantum computation? What is your precise argument for why easiness of NISQ implies impossibility of quantum fault-tolerance?

**Q29** Jiří Kolafa to both: If we combine n physical qubits into one logical qubit, how does the noise reduce? As poly(1/n) or exp(-kn)? In the 2nd case, I believe q computing…

**Q30** “Dulwich Quantum” to both: Will quantum computers solve climate change?

**Q31** (to Gil):  Do I understand correctly that the claim that NISQ devices are limited to some computational class is based on experimental results from NISQ devices? Does this necessarily apply to all possible quantum hardware? Why would this imply that a fault tolerant computer couldn’t be built at all?

**Q32:** Prof. Kalai, I understand your argument as follows: because of an assumed complexity barrier, there is an engineering barrier. Is that correct? If so, assuming that fault-tolerant CQ are built, will it imply fundamental progress in complexity theory?

**Q33** (to Gil)**:** Large parts of computational complexity are based on certain computational complexity hypotheses. Isn’t it too brave to dismiss the existence of quantum computers based on something we are not sure is actually correct?

### NextSilicon

I gave a lecture on the quantum computing debate at [NextSilicon](https://www.nextsilicon.com/), hosted by [Jonathan Devor](https://www.linkedin.com/in/jdevor/?original_referer=https%3A%2F%2Fwww%2Egoogle%2Ecom%2F&originalSubdomain=il) and [Oded Margalit](https://codeguru.co.il/classic/oded.html), and there were many good questions both during the official (recorded) question period and afterwards. [The video of the lecture is here](https://drive.google.com/file/d/1vc-6cgeJFN0GaGKK4KyKXBT1NZfv-D2-/view?usp=gmail). Since I neglected to send a title and abstract, my hosts generously filled the gap with the dramatic headline: *“Doomed to Fail: Why Quantum Supremacy Is Not the Future of Computing.”* When [I saw it](https://gilkalai.wordpress.com/wp-content/uploads/2025/07/nson.png) I suggested a more neutral title, but, apparently, for a few days, this title caused some small panic and led to protests from technology funds with investments in quantum computing.

**Q34:** Can you say a word or two on the Fourier analysis?

**Q35:** What about the recent declarations of experiments using the Google Willow quantum computers

**Q36:** Most of the applications of classical computers are based on heuristics. Do you expect heuristics that will allow further applications of quantum computers.

Another question (**Q37**) that I was asked after the lecture was whether Gentry’s fully homomorphic encryption scheme can be a basis for quantum fault-tolerance methods.

### Ethereum Foundation’s lecture

Usually my policy is not to get involved in policy matters about quantum computation and let my papers speak for themselves. (I did make a small exception [in this post](https://gilkalai.wordpress.com/2022/05/26/waging-war-on-quantum/) where I proposed to wait before any implementation of post-quantum cryptography until there is a firm demonstration of DiVincenzo stages 3–4.) However, when [Matan Prasma](https://sites.google.com/view/matanprasmashomepage/about) asked me to talk at the [Ethereum Foundation](https://ethereum.foundation/) in connection with the company’s hesitation about post-quantum cryptography, I decided to make another exception, largely because of my appreciation for Matan from his days as a brilliant student at HUJI. The lecture titled [A Critical Look on Quantum Computing](https://www.youtube.com/live/HhWWkTkaXSI) (click for You Tube) briefly described both my assessment of where we stand now and my argument regarding what we can expect in the future.

**Q38:** When do you expect we will know with high assurance whether quantum computers are possible?

**Q39:** What is your opinion on recent progress on squeezing states and error correction?

**Q40:** More generally, from a risk management point of view, how should existing crypto systems prepare (or should they not) for quantum computing (being akin to meteorite risk: low probability, high impact)?”

**Q41:** Is it possible to build quantum computers outside the NISQ paradigm?

**Q42:** What would a compelling experiment look like to you, one that might start challenge your current beliefs?

**Q43:** what about the possibility of fantastic achievements that are kept secret for national security reasons?

**Q44:** Can you repeat the argument that NISQ systems are confined to a low complexity class LDP?

**Q45:** Can error-pruned noisy quantum computers still reduce the amount of work needed to break certain crypto systems or be useful for some other computational purposes? Can NISQ computers be useful before fault-tolerant quantum computers?

**Q46:** We heard that the progress in quantum computing depends on the engineering effort invested in the project and once we pass a certain limit we can expect a “Manhattan-type” investment. What do you think about that?

**Q47:** Gil, why do you think people working in this field disagree with you?   
Why is it the case that experts in quantum computations are not convinced by your argument?

### A blast from the past: Facebook discussion with [Aram Harrow](https://en.wikipedia.org/wiki/Aram_Harrow) (July, 2025)

Aram and I conducted a year-long debate in 2012 about quantum fault tolerance and later met in 2013 at MIT. We recently “met” in a Facebook discussion comparing randomness and quantumness and ended with a cozy exchange of remarks.

**Q48** (Aram to Gil): Are you saying that [1409.3093](https://arxiv.org/abs/1409.3093) [Kalai-Kindler 2014] proved a lower bound on the achievable noise rate of linear optics?

(Gil to Aram, abbreviated): **Yes!**

By Gil Kalai

[Read original post](https://gilkalai.wordpress.com/2025/07/30/some-questions-from-recent-quantum-events/)
