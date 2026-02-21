---
date: 2024-01-01
layout: default
type: transcript
series: dwarkesh
episode: 98
guest: ""
title: "AI progress is about to rapidly accelerate in 2025 – Sholto Douglas & Trenton Bricken"
source_url: "https://www.youtube.com/watch?v=UeI29-AdhQI"
analysis_url: /transcripts/dwarkesh/98_ai_progress_is_about_to_rapidly_accelerate_in_2025_sholto_douglas_trenton_bricke.analysis/
permalink: /transcripts/dwarkesh/98_ai_progress_is_about_to_rapidly_accelerate_in_2025_sholto_douglas_trenton_bricke/
---

# Transcript: AI progress is about to rapidly accelerate in 2025 – Sholto Douglas & Trenton Bricken

Source: https://www.youtube.com/watch?v=UeI29-AdhQI

---

**[00:00]** in the model of the intelligence explosion what happens is you replace the AI researchers and then there's like a a bunch of automated AI researchers who can speed up progress make more AI researchers make further progress we

**[00:12]** should just ask the AI researchers about whether they think this is plausible so let me just ask you like if I have a thousand Asian chotos or Asian Trenton are they just do you think that you get an intelligence explosion I think we are

**[00:25]** less at the moment Bound by the sheer engineering work of of making these things than we are by compute to run and get signal and uh and taste in terms of what the actual like right thing to do it and that like making those difficult

**[00:42]** inferences on imperfect information so compute and taste that's interesting to think about because at least the compute part is not bottl NE on more intelligence it just bottl NE on Stam 7 trillion or whatever right so if I gave

**[00:57]** you 10x the h100s to run your experiments how much more effective a researcher are you please how much more effective a researcher are you uh I think the Gemini program would

**[01:10]** probably be like maybe five times faster with 10 times more compute or something like that so that's pretty good elasticity like 0. five wait that's insane yeah I think like more compute would just like directly convert into

**[01:23]** progress so you have some um some fixed size of compute and some of it goes to INF some of it goes to running the experiments for the full model yeah that's right shouldn't then the fraction

**[01:35]** goes to experiments be higher given that you would just be like like the bottleneck is research and research is bottleneck by compute one of the Strategic decisions that every pre-training team has to make is like

**[01:45]** exactly what amount of compute do you allocate to your different training runs uh like to your your research program versus like scaling the last best I like you know thing that you landed on one of the reasons why you need to still keep

**[01:59]** training big models is that you get information there that you don't get otherwise um so scale has all these emerg properties uh which you want to understand better and if you like are always doing research you're not sure

**[02:11]** what's going to like fall off the curve right yeah um if you like keep doing research in this regime yeah uh and like keep on getting more and more computer efficient you may never you you may have actually like gone off the path that

**[02:26]** actually eventually scales so you need to constantly be investing in doing big runs too at the frontier of what you sort of expect to work okay so then tell me what it looks like to be in the world where AI has significantly sped up AI

**[02:39]** research because from this it doesn't really sound like the AIS are going off and writing the code from scratch and that's leading to faster output it sounds like they're really augmenting the top researchers in some way like

**[02:50]** yeah tell me concretely are they doing the experiments are they coming up with the ideas are they just like evaluating the outputs of the experiments what's happening so I think there's there's like two walls you need to consider here

**[03:00]** one is where AI has meaningfully sped up our ability to make algorithmic progress right and one is where the output of the AI itself is the thing that's like the crucial ingredient towards uh like model capability progress and like

**[03:13]** specifically what I mean there is synthe synthetic data right um and in the first world where it's meaningfully speeding up algorithmic progress I think a necessary component of that is more compute that

**[03:26]** and and you probably like Reach This elasticity point like AI maybe at some point are easier to speed up and get on context than yourself than other people um and so AI meaningfully speed up your work because they're like a fantastic

**[03:42]** co-pilot basically that helps you code like multiple times faster um and that seems like actually quite reasonable um super long context super smart model um it's on boarded immediately and you can like send them off uh and to like

**[03:55]** complete subtasks and sub goals for you walk me through like a day in the life of show like you're working on an experiment or project that's going to make the model quote unquote better right like what is happening from

**[04:08]** observation to experiment to Theory to like writing the code what is happening I think the most important like part to illustrate is this cycle of coming up with an idea proving it out at different points in scale um and uh the and like

**[04:25]** interpreting understanding what goes wrong and I think most people would be surprised to learn just how much much goes into interpret like interpreting and understanding what goes what goes wrong because the ideas people have long

**[04:36]** lists of ideas that they want to try not every idea that you think should work will work and trying to understand why that is is quite difficult and like working out what exactly you need to do to interrogate it um so so much of it is

**[04:46]** like introspection about what's going on it's not pumping out thousands and thousands and thousands of line of code it's not um like the difficulty in coming up with ideas even I think many people have a long list of ideas that

**[04:58]** they want to try pairing that down and shot calling Under very imperfect information what the right ideas to explore further is really hard tell me more about what do you mean by imperfect information are these early experiments

**[05:13]** are these like what is the information that you're like scaling LW increments you can see like in the GPD 4 paper they have like a bunch of like dots right where they say we can estimate the performance of our final model like

**[05:22]** using all of these dots and there's a nice curve that like flows through them concretely why do why is that imperfect information is you never know if the trend will hold for certain architectures the trend has held really

**[05:34]** well and for certain changes it's held really well but that isn't always the case and things which can help at smaller scales can actually hurt at larger scales um so making guesses based on what the trend lines look like and

**[05:50]** based on like your intuitive feeling of okay this this is actually something that's going to matter that's interesting to consider that for every chart you see in a release paper Tech that shows that smooth Cur there

**[06:02]** graveyard of like first runs and then like there's all these other lines that go in like different directions ta it's yeah it's crazy both like as a grad student and then also here like the number of experiments that you have to

**[06:15]** run and then intuiting what went wrong is actually really hard like working out what like this is in many respects the problem that the team the Trenton is on is trying to better understand is like what is going on inside these models we

**[06:27]** have inferences and understanding and like head Cannon for why certain things work but it's not an exact science um and so you have to constantly be making guesses about why something might have happened what experiment might reveal

**[06:38]** whether that is or isn't true and that's probably the most complex part yeah I I agree with a lot of that but even on the interpretability team I mean especially with Chris Ola leading it there are just so many ideas that we

**[06:51]** want to test and it's really just having the engineering skill but I'll put Engineering in quotes because a lot of it is research to like very quickly iterate on an experiment look at the results interpret it try the next thing

**[07:06]** communicate them um and then just ruthlessly prioritizing what the highest priority things to do are and this is really important like the ruthless prioritization is something which I think separates uh a lot of like quality

**[07:17]** research from um research that doesn't necessarily succeed as much we're in this funny field where uh so many of our theoretical initial theoretical understanding is like broken down basically um and so you need to have

**[07:30]** this Simplicity bias and like ruthless prioritization over what's actually going wrong and I think that's one of the things that separates the most effective people is they don't necessarily get like too attached to

**[07:41]** solving using a given like a solution that they're necessarily familiar with um but rather they attack the problem directly um you see this a lot uh in like maybe people come in with like specific academic background they try

**[07:54]** and solve problems with that toolbox um and the best people are people who expand the toolbox dramatically they're you know they're running around in there and taking ideas from reinforcement larning but also from optimization

**[08:05]** Theory and also they have a great understanding of systems and so they know what the sort of constraints that bound the problem are and they're good Engineers they can iterate and try ideas fast like by far the best researchers

**[08:14]** I've seen uh they all have the ability to try experiments really really really really really fast um and that is that cycle time and at smaller scales cycle time separates people I mean machine learning research is just so empirical

**[08:27]** yeah and and this is honestly one reason why I think uh our Solutions might end up looking more brain-like than otherwise uh it's like even though we wouldn't want to admit it the whole Community is kind of doing like a greedy

**[08:41]** evolutionary optimization over the landscape of like possible Ai architectures and everything else uh it's like no better than evolution
