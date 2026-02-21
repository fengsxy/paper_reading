---
date: 2024-01-01
layout: default
type: transcript
series: dwarkesh
episode: 112
guest: ""
title: "Scaling LLMs further is an artform - Demis Hassabis (Google DeepMind CEO)"
source_url: "https://www.youtube.com/watch?v=666XgM38jJE"
analysis_url: /transcripts/dwarkesh/112_scaling_llms_further_is_an_artform_demis_hassabis_google_deepmind_ceo.analysis/
permalink: /transcripts/dwarkesh/112_scaling_llms_further_is_an_artform_demis_hassabis_google_deepmind_ceo/
---

# Transcript: Scaling LLMs further is an artform - Demis Hassabis (Google DeepMind CEO)

Source: https://www.youtube.com/watch?v=666XgM38jJE

---

**[00:00]** go going back to Gemini I'm curious uh what the bottlenecks were in the development um like why not make it immediately one order of magnitude bigger well look first of all there are practical limits how much compute that

**[00:10]** can you actually fit in one Data Center and actually you know you're you're bumping up against very interesting distributed computing kind of challenges right we unfortunately we have some of the best people in the world on on those

**[00:20]** challenges and and you know cross data center training all these kinds of things very interesting challenges Hardware challenges and we have our tpus and so on that we're building and designing all the time as well as using

**[00:31]** gpus and so um there's all of that and then you also have to the scaling laws you know they don't they don't just work by Magic you sort of you still need to scale up the hyper parameters and various Innovations are going in all the

**[00:44]** time with each new scale it's not just about repeating the same recipe at each new scale you have to adjust the recipe and uh and that's a bit of an art form in a way and you have to sort of almost get new data points if you try and

**[00:56]** extend your predictions extrapolate them say several orders of magnitude out sometimes they don't hold anymore right because um new capabilities they can be step functions in in terms of new capabilities and and and and some things

**[01:09]** just some things hold and other things don't so often you you do need those intermediate data points actually to to correct uh uh some of your hyperparameter optimization and other things so that that the scaling law

**[01:20]** continues to be true so um so there's sort of various practical limitations onto onto that um so you know kind of one order of magnitude is is about probably the maximum that you want to you want to carry on uh you want to sort

**[01:33]** of do between each uh each era oh that's so fascinating uh you know in the gp4 technical report they say that they were able to predict the the training loss um you know tens of thousands of times less compute than gp4 they could see the

**[01:46]** curve but the point you're making is that the actual capabilities that loss implies uh may not be the downstream capabilities sometimes don't follow from the you can often predict the the core metrics like training loss or or

**[01:56]** something like that but then um it doesn't actually translate into to MML or or or some other actual uh capability that you care about they're not they're not necessarily linear all the time I think we've got to push scaling as as

**[02:10]** hard as we can and that's what we're doing here and you know it's an empirical question whether that will hit an ASM toope or brick wall and there are you know different people argue about that but actually I think we should just

**[02:20]** test it I think no one knows um and but in the meantime we should also double down on Innovation and invention and this is something that that that that that Google research and deep mind and Google brain have have have have you

**[02:33]** know we pioneered many many things over the last decade that's something that's our bread and butter and um you know you can think of half our effort is to do with scaling and half our efforts to do with inventing the next architectures

**[02:45]** the next algorithms that will be needed um knowing that you've got this scaled larger and larger model coming along the lines what's been the biggest surprise to you uh if you go back to uh yourself in 2010 when you're starting Deep Mind

**[02:56]** in terms of what AI progresses look like did you anticipate back then that it would in some large sense amount to spend us you know dumping billions of dollars into these models or did you have a different sense of what it would

**[03:05]** look like we thought that and actually you know if you I know you've interviewed my my colleague Shane and and and he he always thought that in terms of like um compute curves and and then maybe comparing roughly to like the

**[03:17]** brain and how many neurons and synapses there are very Loosely but we're actually interestingly in that kind of regime now roughly in the right order of magnitude of you know number of copses in the brain and and and and the sort of

**[03:27]** compute that we have but I think more fundamentally you know we we always thought that um we bet on generality and learning right so th those were always at the core of the any Technique we would use that's why we triangulated on

**[03:41]** reinforcement learning and search and and and and deep learning right as three types of algorithms that that would scale and um and and would be very general and and not require a lot of handcrafted human priors which we

**[03:55]** thought was the sort of failure mode really of of the efforts to build AI uh in the 90s right places like MIT where where there were very you know logic based systems expert systems you know masses of hand-coded handcrafted human

**[04:09]** information going into that turned out to be wrong or or too rigid so we wanted to move away from that and I think we spotted that Trend early and uh became you know and obviously we use games as our Proving Ground and we did very well

**[04:20]** with that you know things like Alpha go I think was a big moment for inspiring many others to think oh actually these systems are ready to scale and then of course with the Advent of transform invented by our colleagues at Google you

**[04:31]** know research and brain that was the then you know the the the type of deep learning that allowed us to ingest masses of amounts of information and that uh of course is really tpet chared where we are today so I think that's all

**[04:43]** part of the same lineage um you know we we couldn't have predicted every Twist and Turn there but I think the general direction we were going in um uh was the right one
