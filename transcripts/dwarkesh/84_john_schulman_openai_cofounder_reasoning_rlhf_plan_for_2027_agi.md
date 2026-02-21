---
date: 2024-01-01
layout: default
type: transcript
series: dwarkesh
episode: 84
guest: ""
title: "John Schulman (OpenAI Cofounder) — Reasoning, RLHF, & plan for 2027 AGI"
source_url: "https://www.youtube.com/watch?v=Wo95ob_s_NI"
analysis_url: /transcripts/dwarkesh/84_john_schulman_openai_cofounder_reasoning_rlhf_plan_for_2027_agi.analysis/
permalink: /transcripts/dwarkesh/84_john_schulman_openai_cofounder_reasoning_rlhf_plan_for_2027_agi/
---

# Transcript: John Schulman (OpenAI Cofounder) — Reasoning, RLHF, & plan for 2027 AGI

Source: https://www.youtube.com/watch?v=Wo95ob_s_NI

---

**[00:00]** I think even in one or [music] two years you could imagine having the models carry out a whole coding project moving away from using the model like a search engine and more towards having a whole project that I'm like doing in

**[00:10]** collaboration with the model. We might not want to jump to having AIs run whole firms immediately. Even if the models are good enough to actually run a successful business [music] themselves if there's no other bottlenecks next

**[00:22]** year or something you got AGI. What's the plan? Today I have the pleasure to speak with John Schulman who is one of the co-founders of OpenAI and leads the post training team here and um he also led the creation of Chad GBT and is the

**[00:36]** author of many of the most important and widely cited papers in AI and RL including PO and many others. So John really excited to chat with you. Thanks for coming on the podcast. Thanks for having me on the podcast. I'm

**[00:47]** a big fan. Oh thank you. Thank you for saying that. Um so the first question I had is we have these distinctions between pre-training and post-training beyond what is actually happening in

**[00:57]** terms of loss function and training regimes. I'm just curious taking a step back conceptually like what kind of thing is pre-training creating what does post-raining do on top of that? In pre-training you're basically

**[01:10]** training to imitate all of the content on um the internet on the web um including websites and code and so forth. Uh so you get a model that can basically um generate uh content that looks like random web

**[01:24]** pages from the internet and um the model is also trained to maximize likelihood where it has to put a probability on everything. So it's um the objective is uh basically predicting the next token given the previous tokens. tokens are

**[01:40]** like words or parts of words and uh since the model has to put a probability on it. Uh and it's we're training with um to maximize log probability it ends up being very calibrated. So it can not only generate all this uh the content of

**[01:54]** the web, it can also assign probabilities to everything. So so the base model can effectively take on all these different personas or generate um all these different kinds of content. And then uh when we do post-training

**[02:10]** uh we're usually targeting a narrower um range of behavior where we basically want the model to behave like this kind of chat assistant and uh it's a it's a more specific persona where it's um trying to be helpful. It's not trying to

**[02:26]** imitate a person. It's um answering your questions or doing your tasks. Um and uh we're optimizing on a different objective which is more about producing outputs that humans will like and find useful as opposed to just trying to

**[02:41]** imitate uh this raw content from the web. Yeah. Okay. I think maybe I should take a step back and ask um right now we have these models that are pretty good at act acting as chat bots. Just taking a step

**[02:53]** back from how these processes work currently. What will the models released by the end of kinds of things the models released in the end of the year will be capable of doing? What do you see the progress looking like? five, you know,

**[03:02]** carry this forward for the next five years. Oh, yeah. Five years. Yeah. I think uh the models will get quite a bit better. Um but in the course of five years, uh so I mean I think even in one or two

**[03:16]** years we'll find that uh a lot of um you can use them for a lot of um uh more like involved tasks than they can do now. So you could um so so for example right now um like you could imagine having the models

**[03:33]** do carry out a whole coding project instead of maybe giving you one suggestion on how to write a function. So uh you could imagine the model like you giving it sort of high level instructions on what to what to code up

**[03:46]** and it'll go and uh it'll um go and write uh many files and test it look at the output iterate on that a bit. So just much more complex tasks and fundamentally the unlock is that it can act coherently for long enough to

**[04:00]** write multiple files of code or what what has changed between now and then? Yeah, I would say this will come from some combination of just uh training the models to do um harder tasks like this. So um just uh like I'd say right uh the

**[04:17]** models aren't um aren't particularly uh like most of the uh training data is more like doing single steps at a time and I would expect us to do more uh for training the models to uh carry out these longer projects. Um, so I'd say

**[04:34]** any any kind of training uh any like doing RL uh to learn how to do these tasks uh however you do it whether it's whether you're supervising the final output or supervising it like each step um I think any kind of training at uh

**[04:50]** carrying out these long projects is going to make them a lot better and uh since uh the the whole um area is pretty new I'd say there's just a lot of lowhanging fruit in interesting

**[05:02]** um do in doing this kind of training. So, I'd say that's one thing. Um, also I would expect that as the models get better, they're just um better at recovering from errors or they have um just uh

**[05:16]** they're better at um at dealing with um dealing with edge cases or when things go wrong, they know how to recover from it. So, uh the models will be more sample efficient. So you don't have to collect a ton of data to uh teach them

**[05:29]** how to get back on track. Just a little bit of data or or just their like generalization from uh from other um abilities will allow them to get back onto track on track whereas current models might just get stuck and get

**[05:44]** lost. I'm not sure I understood actually how uh I want to understand more explicitly how the generalization helps you get back on track. Can you say more about that? I'm not sure I got got

**[05:55]** why those two concepts are connected, right? They're not directly uh connected. So I would say you usually have a little bit of data um that does everything. Uh so I mean if you have um yeah if you collect a diverse data set

**[06:08]** um you're going to get a little bit of everything in it. And uh and if you have models that generalize really well uh even if there's just a couple examples of getting back on track I see or even um like maybe in the pre-training

**[06:22]** there's examples of getting back on track then like the model will be able to generalize from uh those other things it's seen to the current situation. So I think uh like uh if you have uh models that are uh weaker, you might be able to

**[06:36]** get them to do almost anything with enough data, but you might have to put a lot of effort into um a particular uh domain or skill. Whereas for a stronger model, it might just do the right thing without any training data or any effort.

**[06:50]** Do you have some intuition about right now these models can maybe act coherently for 5 minutes? We want them to be able to do tasks that for a human would take an hour, then a week, then a month, and so forth to get from each of

**[07:02]** these benchmarks. Is it going to be each one takes 10x more compute uh analogous to the current scaling loss for free training or is it going to be a much more streamlined process because uh just

**[07:17]** getting to that point where you're already s more sample efficient and then you can just you just go to the years of carrying out tasks or something. Yeah, I would say at a high level I I would agree that um longer horizon tasks are

**[07:30]** going to um require more model intelligence to do well and are going to be more expensive to train for. Um I'm not sure I would expect there to be a really clean scaling law unless you um uh set it up in a very careful way or

**[07:45]** design your uh yeah design the experiment in a certain certain way because uh I I would say there might ends up being some phase transitions where um once you get to a certain level um you can deal with

**[08:03]** um you can deal with much longer tasks. So for example, people um uh like I think when people um like think when people do planning for uh at different time scales, I'm not sure they use completely different mechanisms. So

**[08:20]** uh we probably use the same uh mental machinery if we're thinking about one month from now, one year from now. Yeah. Uh or like a hundred years from now. uh it's um so we're not actually doing some kind of reinforcement learning that uh

**[08:36]** where we need to worry about a discount factor that covers that time scale and so forth. So I think uh I think using language you can describe all of these different time scales and then you can do things like uh plan to uh in the

**[08:50]** moment you can try to make progress towards your goal whether it's a month away or 10 years away. So I might expect the same out of models where there um some kind of um I don't know if it's a phase transition but uh like there's

**[09:05]** some capabilities that work at multiple scales. Yeah. Well, okay. So, correct me if this is wrong, but it seems like that implies right now we have models that are on a per token basis pretty smart. Like they

**[09:17]** might be as smart as humans on a per token basis, the smartest humans. And the the thing that prevents them from being as useful as they could be is that 5 minutes from now they're not going to be still writing your code in a way

**[09:29]** that's coherent and aligns with the broader goals you have for your project or something. If it's the case that once you start this long horizon RL training regime, it immediately unlocks your ability to be coherent for longer

**[09:43]** periods of time, should we be predicting something that is human level as soon as that regime is unlocked or and if not then what what is remaining after we can plan for a year and execute projects that take that long?

**[09:55]** Yeah, it's not totally clear what we're going to see once we get into that regime and [snorts] um how fast progress will be. So that's uh that's still uncertain. Um I would say I would expect there to be um um I I would I wouldn't

**[10:11]** expect everything to be immediately solved by doing any training like this. I would think uh there will be other um like miscellaneous deficits that the models have that um cause them to get stuck or not make progress or make um

**[10:24]** worse decisions than humans. So, uh I I wouldn't say I expect that this one little thing will unlock every all capabilities, but I um yeah, it's not clear. Uh but it might uh like some improvement in the ability to do long

**[10:38]** horizon tasks might go quite far. Would you say it's plausible or is it seems quite likely that there will be other reasons why there might be bottlenecks? And I'm also kind of curious like what what would be the nature of the

**[10:49]** bottlenecks? So, it has all these representations of pre-training. Now it can do act coherently for a long period of time because of long horizon RL. What's remaining? Yeah. Um maybe there's some uh

**[11:03]** there's some other um experience that human experts bring to different tasks like um having some uh taste uh or dealing with ambiguity better. Um so I could imagine that if we want to do something like research uh like those

**[11:18]** those kind of considerations come into play. Um yeah, obviously there's uh um they're going to be just uh sort of mundane limitations around uh like affordances of the model like whether it

**[11:33]** can um whether it can use UIs and obviously the physical world um or h having access to things. So, I think there might be a lot of um uh like mundane uh barriers that are probably not going to last that long, but would

**[11:49]** initially um like slow down um progress? The websites that are designed for these AIs once they're much more multimodal um or at least train on more multimodal data, will they be in any way different from the ones we have for humans? like

**[12:03]** the UIs that will be needed, what uh how compensating for their strengths and weaknesses, how would that look different from the current, you know, UIs we have for humans? Yeah, that's that's an interesting

**[12:14]** question. I mean um I would expect that models will be able to use uh websites that are designed for humans uh just by using vision uh like when the vision capabilities get a bit better. Um so there wouldn't be an immediate need to

**[12:27]** change them. Um, on the other hand, some websites uh that are going to benefit a lot from AI AIS being able to use them will probably want to uh design to be better UX's for AIS. So, um I'm not sure exactly what that would mean, but

**[12:44]** probably uh like assuming that our um our models are still better at in text mode um than like reading text out of images, uh you'd probably want to have a good textbased representation for the models. So, uh and also um just uh a

**[13:01]** good uh like indication of what are all the things that can be interacted with. Um but I guess I wouldn't expect the web to get um like totally redesigned to have APIs everywhere because I I would expect that we can get models to use the

**[13:15]** same kind of UIs that humans use, right? I mean I guess that's been the big lesson of language models, right? That they can they can act in the similar affordances that humans have. Mh. Um,

**[13:25]** so the point you made earlier about this process could be more sample efficient because it could generalize from its experiences in pre-training of how to get unstuck in different scenarios. Uh, I'm curious what the strongest evidence

**[13:39]** of this kind of generalization and transfer you've seen is. Uh, the yeah like because the big question it seems about the future abilities as models is like how how much generalization there is

**[13:52]** happening. Is there something that feels really compelling to you? Like you really learn something that you wouldn't expected to learn from the generalization here? There's uh definitely been some

**[14:02]** interesting um uh instance of generalization in post- training like um uh one well-known phenomenon is if you uh do all your fine-tuning with English data uh you'll automatically um you'll have the model also um uh behave

**[14:19]** behaving well in other languages. So if you train the assistant on English data, it'll also um do something reasonable in Spanish say and uh sometimes you might get um you might get the wrong behavior in terms of whether it replies in

**[14:32]** English or replies in Spanish but uh you usually you get the you get the the right behavior there as well like you get it to respond in Spanish to Spanish queries. So that's one one uh kind of interesting instance of generalization

**[14:45]** that you just sort of latch on to the right uh helpful persona and then you automatically do the right thing in different languages. We've seen some versions of this with um multimodal data where uh if you do um texton fine-tuning

**[14:59]** you also get reasonable behavior with images. M um uh early on in um chat GBT we uh we were trying to fix some issues in terms of the model uh understanding its own uh

**[15:14]** limitations like um like early versions of the model would think that uh could like send you an email or call you call an Uber or something like uh the model would try to play the assistant and it would say oh yeah of course I I sent

**[15:27]** that email and obviously it didn't. So we uh we started collecting a little some data to fix those problems and we found that a tiny amount of data did the trick even when you mix it together with everything else. So I don't remember

**[15:40]** exactly how many examples but something like 30 30 example well we had a I don't know pretty small number of examples showing this general uh behavior of um like explaining that the model can't doesn't have this capability and that

**[15:55]** generalized pretty well to all sorts of capabilities we didn't train for. Okay. So, I I still want to go back to this because I'm not sure I understood uh like if you have uh this model that is trained on to be coherent for longer

**[16:10]** periods of time. Does that imply that unless there are these other bottlenecks which they may or may not be by next year you could have models that are potentially like human level in terms of acting like like you're interacting with

**[16:24]** this as a colleague and it's like it's like as good as interacting with a human colleague. you can tell them to go do stuff and they go get it done. Uh what seems wrong with that picture if this is the capabilities you think might

**[16:35]** be possible? Yeah, it's hard to say exactly what will be the deficit. I mean, I would say that uh when you talk to the models today, they have various um uh weaknesses besides uh long-term coherence in terms

**[16:48]** of also like um like really uh thinking hard about things or paying attention to what you ask them. Uh so um I would say um I wouldn't expect um like just improving the uh coherence a little bit to like um to be all it takes to get to

**[17:08]** AGI, but um I guess I wouldn't be able to articulate exactly what the main weakness is that'll stop them from uh like being a fully functional uh colleague. It seems like then you should be

**[17:21]** planning for the possibility you would have AGI very soon. Yeah, I think it's uh I think that would be reasonable. So, what's the plan if like if there's no other bottlenecks next year or something? You got AGI. What's the plan?

**[17:33]** Well, I would say that if AGI came way sooner than expected, uh we would definitely want to we would want to be careful about it and we would uh we might want to um like uh slow down a little bit on uh training

**[17:46]** and deployment until we're pretty sure we know uh we we can deal with it safely. Um, and we we have a um a pretty good handle on what it's going to do, what it what it can do. So, I think uh yeah, we would have to be we'd have to

**[18:02]** be very careful um if it happened way sooner than expected because I think uh our understanding is rudimentary in a lot of ways still. And what would what would being careful mean? Like because presumably you are

**[18:14]** already careful, right? you do these evaluations before you're um yeah, I would say just like uh u maybe not um not training the even smarter version, not like being really careful when you do train it that it's not uh

**[18:30]** it's um like properly sandboxed and everything. Um maybe not deploying it at scale um or yeah being uh yeah being care careful about what um what scale you deploy it. Um yeah, I guess I'm not okay. So, let's just play with the

**[18:49]** scenario like it happens next year and then uh you're you're not training a smarter system but and then you're you're deploying somewhat in a measured way. Um I yeah I'm I'm wondering

**[19:07]** presumably if this is just this isn't particular to AI but this is just intelligence was just much easier than we expected and this is why it happened. Um and so you wait to deploy a little bit now other companies have the similar

**[19:20]** level of capabilities. What what happens next? So you you've waited to deploy. What are you waiting for? What what are you talking with these what what is every company doing in this scenario? Yeah. Yeah. The game theory is a little

**[19:31]** tough to think through. So Oh yeah. So first of all, I don't think this is going to happen next year, but it's still useful to have the conversation. Maybe it's like two or three years instead.

**[19:40]** But um yeah, I guess two or three years is still pretty soon. Still pretty soon. I do think uh you probably need some coordination like uh everyone needs to agree on some uh on some reasonable uh like limits to

**[19:54]** deployment or to further training uh for this to work otherwise uh otherwise you have the the race dynamics where everyone's trying to everyone's trying to stay ahead and uh like everyone's uh like and that might require compromising

**[20:09]** on safety. So I think you would probably need some coordination among the uh larger entities that are doing this kind of training. And so you're coordinating to um I guess pause deployment until until

**[20:23]** what exactly like until you figure out what's happening in the model like pause uh either uh further training, pause deployment, uh like uh avoid certain types of training that we think might be riskier. Uh so just uh

**[20:37]** like setting up some reasonable rules for uh um like uh what what everyone should do to yeah having everyone somewhat limit uh limit these things and but uh limit to what end because I guess at some point then you're going to have

**[20:53]** to like the the potential energy that's within this intelligence will uh you know it'll be only show uh what what what what is a plan to do like suppose in two years we get the AGI and Now everybody's freaking out and so now the

**[21:08]** AI companies have paused. Um and now what is or what what would be the plan to wait till or Yeah, that's uh I don't have a good answer to that. I mean I would say um if we can if everyone is going to coordinate like that uh I think

**[21:25]** we would be that would be an okay scenario. That would be a pretty good scenario because I do think uh like um building these models is very capital intensive and uh there are a lot of complex pieces. So it's not like

**[21:39]** everyone's going to go and recreate the stuff at home. Uh so I think it is possible to do given the relatively small number of entities who could train the largest models. It does seem possible to coordinate. So, I'm not sure

**[21:52]** how uh how you would maintain this uh this equilibrium for a long uh period of time, but I think if we got to that point um we would be in an okay position. Or would we? I guess I'm curious like um uh I'm not sure what

**[22:09]** happens next cuz like fundamentally the problem or the benefit is that like we we've got a ton of like you you like push it to the server and now we've got a bunch of intelligences or they can push themselves to the server. Um, and

**[22:21]** I'm now we got everybody coordinated, but I'm not sure what what we do next in this in this world. We're like why that why that sets us up for a good outcome. Yeah, I would say if we had everyone um reasonably coordinated, we could uh

**[22:34]** figure out some and we felt like we had solved the technical problems around alignment well enough to be able to uh deploy like really smart AIs that um can like uh like act as an extension of people's will but also uh prevent uh

**[22:52]** them from being misused in some way that would cause a catastrophe catastrophe. I think then uh then that would be great like we could uh go ahead and uh like safely deploy these systems and uh it would um it would usher in a lot of uh

**[23:06]** prosperity and a new uh like much uh more rapid phase of scientific advancement and so forth. So I think that would be what the good scenario would look like. Okay. So that's that makes sense. But

**[23:19]** I'm curious like how would you know in a couple of years if uh you you like all these uh actors even in the best case scenario they've agreed to pause until we've figured out that we're building alliance systems that uh uh are not

**[23:35]** themselves going to attempt to take over a coup or not going to enable somebody else to do that. How what would proof of that look like or what would evidence of that look like? Well, I would say if we um if we can

**[23:47]** deploy uh like uh systems incrementally that are successively smarter than the ones before, then I think that's uh safer. So, I hope the way things play out is is it's not this scenario where everyone has to coordinate and lock

**[24:00]** things down and safely release things uh like because it would like lead to this big buildup in potential energy potentially. So, I would rather some scenario where we're just um continually releasing things that are a little

**[24:14]** better than what came before and then we uh while like making sure we're um confident that each um diff is right like improving uh improving the safety and alignment uh in like uh correspondence to the improvement in

**[24:31]** capability. So, and if if things started to look a little bit scary, then we would be able to uh slow things down. So, that's what I would hope for. Um I would say um if there's more of a discontinuous jump and the question is

**[24:46]** how do you know if the thing you've got is safe to release? Um, I would say I can't give a a generic answer like I would want to but um like the type of thing you might want to do to make that more uh more acceptable would be you

**[25:04]** would want to do um a lot of uh testing like simulated deployment um uh you where that you expect so red teaming of sorts like you'd want to do that in a way that you feel is like uh much less favorable than uh or much uh

**[25:22]** more likely to fail than the thing you're planning to do in the real world. Uh you'd want to have a really good monitoring system so that you can uh like if something does start to go go wrong with the deployed system, you can

**[25:35]** uh you feel like it's going to be uh detectable immediately, like you've got maybe you've got something watching over uh the deployed AIS and what they're doing and looking for signs of trouble. So I so I would want to um yeah I would

**[25:49]** say just um you'd want some defense in depth like you'd want to have some combination of uh like the model itself uh seems to be um like really well be behaved and have like impeccable uh moral compass and everything and you're

**[26:05]** pretty confident that it's it's extremely resistant to any kind of takeover attempt or something or like severe misuse. And then you'd also want to have like uh really good monitoring on top of it. So yeah, you could detect

**[26:18]** any kind of any trouble. What are you keeping track of while you're doing long horizon RL or when you eventually start doing it that uh you you could notice this sort of discontinuous jump before you deployed

**[26:31]** these systems broadly? I would say you would want to have a lot of eval during the training process. And like what specifically would it how would you notice something like Yeah. And I mean I mean does it make sense to

**[26:43]** train on a long horizon RL knowing that this is something that could happen or is it just like a very low possibility? How do you think about this? You'd want to be pretty careful when you do this kind of training if you see um

**[26:54]** uh a lot of um potentially scary capabilities um if those seem close. I mean like uh I would say it's not something uh we would want to we have to be scared of right now because uh right now it's hard to get the models to do

**[27:09]** anything co like coherent but if they started to get really good I think um yeah I think we would want to um we would have to take some of these questions seriously and we would want to have a lot of val uh like sort of uh

**[27:24]** test them for um misbehavior and the most or I guess that's like for the alignment of the models. We want to check uh we want to check that um they're not going to um they're not going to sort of turn against us or

**[27:40]** something. Uh but you you might also want to look for uh like discontinuous jumps in capabilities like um uh you you'd want to have lots of valves for the capabilities of the models. I mean also I guess you you'd also want to

**[27:55]** make sure that whatever you're training on doesn't uh have any reason to make the model turn against you which itself I I think isn't um I would say there's uh like um that doesn't seem like the hardest

**[28:09]** thing to do. I mean if uh like the way we train them with RLHF uh that that does feel even though the models are very smart it does feel very safe because the model is just trying to produce a message that is uh pleasing to

**[28:23]** a human and it has no um concern about anything else in the world other than whether this text it produces is uh is approved. Um so obviously if you were doing something where there's uh where the model has um yeah it's carrying out

**[28:39]** a long sequence of actions which involve tools and everything then it might have some incentive to do a lot of wacky like wacky things that wouldn't make sense to a human in the process of producing its final result. Uh but I guess um it

**[28:53]** wouldn't necessarily have an incentive to do anything other than produce a very high quality um output at the end. So it um like it's not um yeah. So I guess you have these old uh points about like instrumental convergence like the

**[29:07]** model's going to want to take over the world so it can produce this awesome piece of code at the end. Like if you ask it to write you the a flask app it'll be like oh yeah first I need to take over the world and then I I

**[29:19]** need to I don't know. But at a certain point, it's a little bit um it's a little hard to imagine why um for some like fairly well specified task like that, you would want to first take over the world. Um but of course uh yeah, if

**[29:33]** you had a task like make money uh then maybe uh that would lead to some nefarious behavior as a um instrumental goal. Yeah. Okay. So before we get back to that, I think let's step back and talk

**[29:46]** about like uh today's um RHF systems and everything. Um but I I don't want to follow on that thread at some point. It's kind of interesting. Um okay so today's RHF the way in which it influences these models is would you

**[30:01]** characterize it as in terms of human psychology is it a drive? Is it a goal? Is it an impulse? Like psychologically what kind of thing in what way is it being changed? and not not just like the persona of a chatbot, but just like

**[30:17]** don't talk that way, talk this other way or don't don't put those kind of outputs. Yeah, I would say there are probably some analogies with a drive or a goal in humans. So, in that um you have um

**[30:29]** you're trying to steer towards a certain set of states rather than some other states. Um and so I would I would think that our concept of a drive or a goal has um other um elements like uh like the feeling of satisfaction you get for

**[30:44]** achieving it. And uh and those things might um be more like have more to do with the learning algorithm than uh what the model does at runtime uh when you just have a fixed model. So I would say I would say there are probably some

**[30:58]** analogies though um it's uh I don't know exactly um like how how close it is but I would say to some extent it is um the models um do have drives and goals in some meaningful way and in in the case of RHF where you're trying to um

**[31:16]** maximize um human approval as measured by a reward model the model is just trying to produce something that people are going to like and pe and is they're going to judge is correct. I've heard two ideas in terms of using that

**[31:29]** internal monologue type of thing to get better at reasoning at least publicly the kinds of things I've seen and I'm curious which you think is more promising. One is that the model learns from it outputs a bunch

**[31:43]** of potential trains of thought and it learns to follow the one that leads to the correct answer and is trained on that before deployment. And the other one is you use a bunch of compute to do inference in deployment which involves

**[31:58]** the model talking to itself, you know, while while it's deployed. Which one do you expect it to be closer to when it's like really good at reasoning? Is it because it's doing just a bunch of inference calls or is it just

**[32:09]** because you've trained it to do well at that? Well, I would say you could define reasoning as um tasks that require some kind of uh uh like computation um at test time or maybe some kind of uh deduction. Um so, so by definition,

**[32:26]** reasoning would be tasks that require um like some test time computation and uh like step-by-step computation. Um on the other hand I would also um expect to gain a lot out of um like doing some kind of um training time computation or

**[32:44]** practice at training time. Uh so so I would think that um you get the best results by combining uh combining these two things. Right now you know you have these two ways in which the model learns. It's

**[32:58]** either in training, whether it's pre-training or with the post- training, but it's like most of the compute in training is spent on pre-training and it's just glossing over trillions of tokens just like standing by as a you

**[33:11]** know like almost like skimming trillions of tokens worth of information which if a human was subjected to that would just be totally confused, right? It's like not a very efficient way to learn. And the other way is in context learning,

**[33:24]** but of course that is is more sample efficient there, but it's destroyed with each instance. I'm curious if you think that there's a path for something in between those where it's not destroyed with each instance, but it's also not as

**[33:40]** um uh uh not as sort of frivolous as just seeing trillions of tokens where it's more deliberate and active. Yeah. So, do you mean um models having some kind of uh medium-term memory? So, uh too much to fit in context, but um

**[33:56]** like much smaller scale than pre-training. I'm not sure if memory it might be memory. I don't have context, but certainly like when I when I'm trying to prepare for this conversation, uh it

**[34:08]** feels like I I think of like what I should understand this. So, I look it up and I like read it carefully and I maybe think about it as I'm reading it and I'm not sure what it naturally corresponds to in terms of models, but I'm what

**[34:20]** would that look like? I'm curious. I see. So, it's not just memory, but it's also somewhat like specializing to a task that um specializing to a certain task or putting a lot of effort into like some particular project.

**[34:32]** And I'm not sure specialization more so um I'm thinking about I don't understand this part so let me look into this part deeper. I already understand this. I'm going to like specializing to your existing knowledge base. Um, yeah, I

**[34:45]** see. So, it's not just about uh finding like uh I don't know training on a bunch of sources that are relevant, fine-tuning on some special domain. It's also about like uh like reasoning about like developing some knowledge through

**[34:57]** your own reasoning and also using some sort of uh introspection and self-nowledge to figure out what you need to learn. Yeah. Um yeah, I would say that does feel like

**[35:09]** um something that's missing from today's systems. I mean I would say um people haven't really pushed too hard on this middle ground between uh like large scale training like where you produce the like this snapshot model that's

**[35:26]** supposed to do everything like a deployed model and then like on the other hand like in context learning and I think part of that is that we've just been uh increasing context length so much that there hasn't been an incentive

**[35:37]** for it. So if you can go to like a 100 thousand or a million context, then that's actually quite a lot and uh it's not um it's not actually the bottleneck in a lot of cases. But I agree that um you'd probably also want to supplement

**[35:53]** that by some kind of fine-tuning like the uh the capabilities you get from fine-tuning and in context learning are probably somewhat complimentary. So I would expect us to want to build systems that do some kind of online learning and

**[36:08]** also have some of these uh cognitive skills of uh like introspecting on their own knowledge and uh seeking out new new knowledge that fills in the holes. Uh is this all happening at the same time? like uh is it just like a new

**[36:25]** training regime where all these things can happen at once or whether it's the long horizon training or whether it's this kind of training are they separate or are they just because like the model is smart enough so they can both

**[36:35]** introspect and it can act on longer horizons and you can get adequate reward on long horizon tasks yeah I would say if you're doing some kind of long horizon task uh well I would uh you're learning while

**[36:50]** you do the task right so the only way to do something that involves uh a lot of steps is to um like to have learning and memory that gets updated during the task. So like there's a continuum between um like uh like short-term

**[37:06]** memory um between short-term and long-term memory. So, um I would say uh yeah, I would expect uh I would expect this uh capability would start to become uh like the need

**[37:23]** for it would start to become clear when we start to uh look at long horizon tasks more and uh and to some extent just um putting um a lot of stuff into context will pro will take you pretty far because we have really long context

**[37:38]** now. But you probably also want things like fine-tuning. And as for like introspection and the ability to do active learning, um that might uh like automatically fall out of the models abilities to know what they know because

**[37:53]** they have some like um models have some calibration um regarding what they know. And that's why like that's why um models don't hallucinate that badly. uh because yeah they have some understanding of the their their own limitations. So I think

**[38:11]** that like same kind of ability could be used for something like active learning and how so uh there's all these complicating RL procedures uh that many of whom you've pioneered how many of them will be relevant when you get to

**[38:30]** the point where the uh the model itself is this smart that it can act as its own environment and interact in a more online and stable way. um is it is is it is a path for progress going to be more

**[38:43]** straightforward than the kinds of solutions that were required for RL in the past? Well, I think policy gradient algorithms are not the most sample efficient algorithms. So that's probably not what

**[38:54]** you want to do at test time if you want to learn really fast. Um but though who knows? I mean maybe it's not that bad. Um so I think um something like um like motor learning in animals is probably something like a policy grading

**[39:09]** algorithm and uh so for example you're like learning how to um shoot baskets. Uh I think you probably uh like that takes uh maybe thousands of tries to um get more accurate and I think you probably

**[39:23]** there's probably some something that's uh like a policy grading algorithm underneath. Um but uh that's not going to be the fastest way to learn in um like if if you have a model trying to do a project or some kind of task. Um so I

**[39:38]** would think we would want to rely more on like in context learning. um where uh you effectively have a learned algorithm like you've learned how to explore uh like you've learned how to try all the possibilities exhaustively um and uh

**[39:55]** instead of doing the same thing over and over again making the same mistake. So yeah, I would say we'll be able to do things that look more like learned search algorithms and and that'll be the kind of thing that uh gets used in a

**[40:08]** particular task. Interesting. All right. I I I want to uh step back and ask about your own history. So um at least at OpenAI. So uh you you led the creation of CHBT. At what point do you did you realize first

**[40:24]** of all these LLMs are the path to go and then a chatbot would be or some way to instruct them would be a useful thing to do? Just walk me through the whole lineage from like when this became the your main focus and yeah how what yeah

**[40:37]** what the process was like. Yeah. So early um so we had um uh before chatbt uh we had um open AAI had these instruction following models and uh that was b the idea there was um we had base models and people can um prompt them in

**[40:56]** elaborate ways um but uh they're also kind of hard to prompt you had to uh they basically do autocomplete so you have to set up a very good prompt with some examples so uh uh so uh people at OpenAI uh were working on um just taking

**[41:13]** the base models and making them easier to prompt so that if you just wrote a question it would answer the question instead of giving you more questions or something. Uh so that was uh so so we had these instruction following models

**[41:25]** which were kind of like base models but a little easier to use. Um and those were the original ones deployed in the API or after um GPD3 those were the next uh generation of models. Um then at the same time there were definitely a lot of

**[41:40]** people thinking about um chat. So uh so Google had some papers uh like they had uh lambda and um earlier Mina. So they had these chat bots and it was more like um uh like you had a it was more like a base model that was really specialized

**[41:57]** to um the task of chat really good at chat and uh like I think at least looking at the examples from the paper. It was more uh used for sort of fun applications like um where the model would uh like take on some persona and

**[42:11]** pretend to be that persona. It was not so functional like um like help me refactor my code. Um so yeah there are definitely people thinking about chat. I had worked on a project before uh looking at chat called uh web GPT which

**[42:28]** was more about doing question answering with the help of web browsing and retrieval and well when you do question answering uh it really wants to be in a chat because um you always uh want to ask follow-up questions or sometimes you

**[42:44]** need a clar the the model should ask a clarifying question because the question's ambiguous. So it was kind of clear after we did the first version of that that we should the next version should be conversational. So anyway, we

**[42:56]** started working on uh like the conversational chat assistant. Um and uh we uh this was built on top of GPD 3.5 which was done training at the beginning of 2022 and uh that model was quite good at language and code. So we quickly

**[43:14]** realized that it was actually uh quite good at coding help and that was one of the things we were excited about. So yeah, we worked on that uh we worked on that for for most of the year and uh we had we had browsing um as another

**[43:28]** feature in it though we ended up uh like deemphasizing that later on because the like the model's internal knowledge was so good that we didn't that the browsing wasn't the most interesting thing about it. Um, and then uh we were thinking

**[43:42]** about we had it out for beta testing or to friends and family for a while and uh we were thinking about doing a public release. Um, but um at that time uh actually GPD4 finished training in August or um yeah in August that year.

**[44:00]** And um actually the um like the flagship RL effort at OpenAI was the instruction following effort because that was the models that were being deployed into production. So um like the first fine tunes of GBD4 used that um that whole

**[44:16]** stack and that was um yeah those models were really good and everyone got really excited about that after seeing the uh like instruct fine-tune GP4s. Uh but so they were really really good. But they would occasionally give you amazing

**[44:29]** outputs, but they were also like a little bit the model was clearly like pretty unreliable. Like it would sometimes hallucinate a lot and it was like pretty it would sometimes give you pretty unhinged outputs. So it was

**[44:41]** clearly not quite ready for prime time, but it was like obviously very good. Um and uh yeah, so I guess that um people forgot about chat for a little while after that about this like alternative branch. Uh but then we we ended up um we

**[44:58]** pushed it further and we ended up like mixing together all the data sets like the instruct and the chat data and to try to get something that was the best of both worlds. And uh I think the yeah the models we the chat models were like

**[45:10]** uh were clearly more um like it was an easy easier to use. It was sort of more um it sort of uh like automatically had much more sensible behavior in terms of like the model knowing its own limitations.

**[45:24]** That was actually one of the things that uh I got excited about as we were developing it that uh like I realized a lot of the things that um people thought were flaws in language models like just like blatantly hallucinating uh could be

**[45:39]** not completely fixed but you could make a lot of progress with pretty straightforward methods. Uh oh yeah and also the um the other thing about chat was that uh like when we had these instruct models uh like the task of uh

**[45:56]** complete this text but in a nice way or in a helpful way that's like a pretty poorly defined task. So I think uh like I think that task is like both confusing for the model and for the human who's supposed to do the data labeling.

**[46:07]** Whereas for chat um I think people had an intuitive sense of uh like what a helpful robot should be like. So I think it was uh just much easier to tell people uh like uh to to give for people to get the idea of what what the model

**[46:22]** was supposed to do. Yeah. Um and uh so that so as a result I think the um like the model had a much more coherent personality and uh like it was much like easier to get um like rob like

**[46:35]** pretty sensible behavior um robustly. Interesting. Uh, is it the case that anybody could have made Chad GBT using your publicly available fine-tuning API? Um, not exactly. I mean, uh, they could

**[46:52]** have, um, I don't remember the status of which models were available available for fine-tuning. uh you assuming we had 3.5 available for fine-tuning at the time, you could have made something pretty decently close, but I'm not sure

**[47:07]** you would have um I don't think you would have been able to do just one iteration of fine-tuning where you have like p purely human written data and you fine tune on that. I think you would want like you would want to do several

**[47:18]** iterations like if you're not going to do RL um which which we did um you'd want to do some kind of iterative supervised fine-tuning where you have like humans edit the model generated

**[47:30]** outputs because it's really hard to get people to like if you train on human generated data even if it's really high quality it's just hard for a model to fit that data perfectly because it might not be like it might not be something a

**[47:43]** model is capable of outputting. Uh so you need to do something iterative that looks a little bit more like RL. Uh so I think if you had done that you could have gotten something pretty close but um that would have been kind of

**[47:56]** non-trivial. Um but we also had another uh like instruction following model trained with RL that was released a little before chat GBT. So I think if you put a chat

**[48:08]** like wrapper on that you would get something decently close. Uh but it like that model um like if you just prompted it with chat. Um so but that model had some uh differences in uh strengths like it was like that model was pretty good

**[48:24]** at writing and poetry and so forth but it wasn't uh it sort of it wasn't as good at knowing its limitations and uh at factuality and so forth. Um, so stepping back from 3.5, I I think I heard you somewhere say GPD2, you're

**[48:39]** super impressed. Compared to your expectations in 2019, has AI progressed faster or slower than you would have expected? I would say uh faster than I would have expected since GPD2.

**[48:51]** Yeah. Um, I was pretty um like bought into um scaling and uh yeah, pre-training and so forth being a good idea. Um but um when GBD2 was done I was I would say I wasn't completely uh sold on it um being uh

**[49:08]** revolutionizing everything. Um like I only really pivoted what I was working on and what yeah what my team was working on in um after GPD3. So after that uh we kind of got together and said oh yeah let's uh

**[49:22]** uh let's u this language model stuff works really well. Let's see what we can do here. But uh yeah, after GBD2, I wasn't quite sure yet. Uh especially if the stuff we were talking about earlier with RL starts

**[49:36]** working better with the smarter models, will the fraction of compute that is spent on training that is pre-training versus post- training change significantly in favor of post-training in the future?

**[49:48]** Yeah, there are some arguments for that. I mean, right now it's a pretty lopsided ratio, but you could argue that the uh output generated by the model is like high quality compared to or higher quality than what much most of what's on

**[50:02]** the web. So, uh it sort of makes more sense for the model to uh think by itself um instead of just um like training to uh imitate what's on the web. So I think there's a first principles argument for that and um I

**[50:18]** would say we found a lot of gains through post-raining. So um I'm not sure. So I would expect us to keep um like pushing this methodology and probably increasing the amount of compute we put into it.

**[50:31]** The current GPD4 has a ELO score ELO score that is like a 100 points higher than the original one that was released. And is that all because of what you're talking about with these improvements that are brought on by post- training or

**[50:47]** Yeah, I would say that we've um I would say that most of that is post-training. Interesting. Um so there are a lot of um there are a lot of different uh separate axes for improvement like you can uh yeah so we think about um like data

**[51:03]** quality data quantity just doing more iterations of the whole uh process of deploying and collecting new data and like changing what you're what kind of annotations you're collecting. So there's a lot of uh a lot of things that

**[51:16]** stack up but together they give you a pretty good um like effective compute increase. Yeah, I mean that that's a huge increase. That's like really interesting that there's this much uh this much room for improvement uh from

**[51:31]** post training. What is uh what what makes for somebody who's really good at doing this sort of R research? Uh I hear it's super finicky, but like what is the sort of intuitions that you have that enable you to find these ways to mess

**[51:46]** with the data and set up these environments? I'd say I just um have a decent amount of experience at this point from uh like the different parts of the stack from like uh RL algorithms obviously since I've worked on those

**[52:03]** since uh grad school uh to like uh the data collection um like the annotation process uh to um like language playing with language models. So I I mean I'd say I' just dabbled with these things and uh I'd say the people who um do well

**[52:22]** at this kind of research uh have some view of the whole stack and have a lot of curiosity about the different parts of it and uh also sort of think about um well you want to be both empirical um and uh like use experiment let

**[52:38]** experiments update your views but you also want to think from first principles somewhat like uh what um uh like assuming that um like learning works like what would be the ideal type of data to collect and that sort of

**[52:53]** thing. So because there doesn't seem to be a model released since GP4 that seems to be significantly better, there's seems to be uh the hypothesis that potentially we're hitting some sort of plateau and that these models aren't

**[53:07]** actually generalizing that well and you're going to hit some sort of data wall beyond which point the abilities that are unlocked by memorizing a vast corpus of pre-training data won't actually help you get

**[53:20]** something much smarter than GP4. Um, what do you think of that hypothesis? Is that wrong? And like I I think we've talked about some examples generically about generalization, the Spanish to English and so forth, but is there Yeah.

**[53:35]** is I mean, okay, so maybe this is a runon question, but [clears throat] um one one example I was thinking of was the idea that there's transfer from langu code reasoning and code. If you

**[53:50]** train a bunch of code, it gets better reasoning in language. And if that's is that actually the case, do you see things like that which suggests that there's all this kind of positive transfer between different modalities?

**[54:00]** So once you try training on a bunch of videos and images, it'll get smarter and it'll get smarter from synthetic data. Or does it seem like the abilities that are unlocked are extremely local to the exact kind of labels and data you put

**[54:13]** into the the training corpus? Yeah. Okay. Yeah, I'll try to respond to all that. So first um are we about to hit the data wall? I mean I wouldn't draw too much from uh the uh time since GPD4 was released because I mean it does

**[54:30]** um um yeah it takes a while to um like train these models and to um like get all the uh do all the prep to um train a new model like generation of models. So uh yeah I wouldn't draw too much from

**[54:46]** from that fact. Um I would say um there are definitely some challenges from the limited amount of data. Um but I wouldn't expect us to immediately hit the data wall. Um but I would expect uh the nature of um pre-training to

**[55:02]** somewhat change over time as we get close closer to it. Um, in terms of like uh generalization from different types of pre-training data, um, I would say it's pretty hard to um, do science uh, on this type of question

**[55:20]** because you can't do that create that many pre-trained models. So maybe uh, you can't train a like a GPD4sized model. You can't do ablation studies at GBD4 scale. Uh maybe you can do like train a ton of um GPD2 size models or

**[55:35]** maybe even a GPD3 size model with different data blends and see what you get. Uh so I'm not like um aware of any results uh like public like public results on um like ablations um involving code data and reasoning

**[55:49]** performance and so forth. Um so that would be I'd be very interested to know about those results. But I'm I'm actually curious about uh I mean if one of the things is that the model gets murder as it's bigger would an

**[56:03]** ablation on a GPT2 level model which suggests that there isn't that much transfer how much evidence does that provide for the level of transfer on a similar set of domains in a GP4 level model

**[56:16]** right you might not be able to conclude that uh if transfer fails at GBD2 size then it's also going to fail at a higher scale So it might be that um like for uh the smaller models um you uh yeah for the larger models you learn these better

**[56:33]** shared representations um or the smaller models have to lean uh too much on memorization whereas the larger models can learn how to do the right computation. So I would expect uh this to be true to some extent. This might

**[56:47]** have a very simple answer but so bigger models you train them on the same amount of data and they become smarter or conversely they can to get the same amount of smarts you you have to train them on less data what why why is that

**[57:02]** the case like it's got more parameters it saw less things and now it's equally as smart why did that why is that the case uh I don't think anyone has a good answer for a good explanation of the uh

**[57:14]** scaling law with um parameter count. I mean, there's some uh I don't even know what the be uh what the best um sort of mental model is for this. Like clearly you have more capacity if you have a bigger model, but

**[57:29]** uh so like you should be able to eventually get uh lower loss, but I guess why are bigger models more sample efficient? Um, I guess you could um I can give you some like very sketchy uh explanations like uh like they have um

**[57:47]** like you could say that the model is uh like uh sort of an uh an ensemble of a bunch of different circuits that do the computation. So it has like um you could imagine that it's doing um it has a bunch of uh like computations that it's

**[58:00]** doing in parallel and it's uh like doing some like the output is a weighted combination of them. uh and uh if you have more um just width of the M or if you just have I mean actually width is somewhat similar to depth because uh

**[58:16]** like with residual networks uh you end up like the depth can do something similar to width in terms of like updating what's in the residual stream. But uh if you yeah you could argue that uh you're learning all these things in

**[58:31]** parallel uh you're learning all these different computations in parallel and you just have more of them with a bigger model. So you have more chance that uh one of them is lucky and uh ends up um like uh having high um like like winning

**[58:46]** guessing correctly a lot and getting upweighted. So that's kind of like a um uh what would be the Yeah, there's some algorithms uh that work this way like that um like mixture uh what is it mixture uh some kind of mixture model um

**[59:05]** or multiplicative weight update algorithm. Yeah, there's some algorithms that kind of work like this. So uh where you have like a um some kind of mixture of uh I don't want to say mixture of experts because it means something

**[59:17]** different but uh like basically a weighted combination of experts with some learned gating uh and uh um actually anyway I said something slightly wrong but anyway uh yeah you can imagine something like that

**[59:30]** and just having a bigger model get gives you more chances to get the right uh function. So that would be um and then of course it's not just like you have a bunch of uh like totally disjoint like functions that have uh you're taking a

**[59:46]** linear combination of it's more like a library where uh you might chain the functions together in some way. So uh you you like it's there's some composability. M um so yeah, so I would just say there's

**[59:58]** like um the bigger model has a bigger library of different uh computations including lots of stuff that's kind of dormant and only being used some of the time. Uh but those things but it has like more space to look for the uh like

**[1:00:11]** look for the circuits to do something useful. I want to ask you about um uh stepping back from the current uh research questions. Just stepping back, I want to understand your sort of like modal scenario of what happens over the

**[1:00:28]** next few years. I think uh towards the beginning of the conversation, we were talking about the case in which it progresses really fast, but just let's just take like the modal scenario. Um you're unlocking long horizon RL at some

**[1:00:40]** point, but then as you said, there's potentially other bottlenecks. So what's happening you know uh how good are these models? How are they being deployed? What other modalities are part of them? At what at what stage are these being

**[1:00:53]** unlocked and so forth? You just kind of want to understand your broader picture of what the next few years look like. Yeah, I would expect um I would expect things like okay new modalities to be added uh like um over time or uh pretty

**[1:01:08]** soon. Um I would yeah I would expect the capabilities to generally keep getting better through a combination of pre-training and post-raining and that'll open up new use cases. So right now um AI is still um not a huge uh part

**[1:01:24]** of the economy like there's a pretty small fraction of uh jobs that it can help with at all. Um, so I'd expect that to be higher over time and not just from the models uh improving also from people just figuring out how to integrate them

**[1:01:38]** into different processes. So even even if we just um froze the models at their current uh state, um I think you would still see a lot of growth in how they're being used. Um, so I would expect there to be a lot of um like I would expect AI

**[1:01:55]** to be um used much more widely and um I would expect it to be used for more um kind of techni like technically sophisticated tasks like um yeah like I gave the programming example earlier um of doing like longer projects but also

**[1:02:15]** helping with um various kinds of uh research. So I would hope that uh we can use um AI to accelerate science in various ways and uh just um like because you can potentially have the the models like understand all the literature in a

**[1:02:32]** given field and be able to like uh be able to sift through tons of data um like more than a person would have patience to do. So I would hope that we can basically uh like you have um well I hope the form factor

**[1:02:49]** would basically be that people are uh still driving all of this and you have your uh like helpful assistance that you can use you can sort of direct and point to lots of different problems that are useful to you and everyone sort of h has

**[1:03:01]** all these uh AIS helping them uh helping them do more get more done. Hey everybody, real quick I want to tell you about a tool that I wish more applications used. So obviously you've noticed every single company is trying

**[1:03:17]** to add an AI chatbot to their website. But as a user I usually find them really annoying cuz they give these long generic often useless answers. CommandBar is a user assistant that you can just embed into your website or

**[1:03:31]** application. And it feels like you're talking to a friendly human support agent who is browsing with you and for you. And it's much more personalized than a regular chatbot. It can actually look up users history and respond

**[1:03:44]** differently based on that. It can use APIs to perform actions. It can even proactively nudge users to explore new features. One thing that I think is really cool is that instead of just outputting text, command bar can kind of

**[1:03:58]** just say here, let me show you and start browsing alongside the user. Anyways, they're in a bunch of great products already. You can learn more about them at commandbar.com. Thanks to them for sponsoring this

**[1:04:11]** episode, but obviously at some point they're going to be better than uh everyone at what whatever they want to do. So, um uh yeah, what will that process look like? right now they're clearly only helping you. At some point

**[1:04:24]** they're able to just do things for you and maybe like run entire firms for you or whatever. Um at that point is it yeah is it just going to be a smooth process and at that point the hope is that we have systems

**[1:04:38]** that are aligned with the user enough that they can count on the firm being run in the way they expect and so forth. Yeah, I think um well we might not want to jump to having AIs run whole firms immediately. I mean uh we might want to

**[1:04:54]** have people uh like overseeing um uh like overseeing these uh like important decisions and uh calling the shots. So uh even even if the models are good enough to uh like to actually run a successful business themselves. Um so uh

**[1:05:13]** yeah to some extent there might be uh choices there. Um and uh I think people will still have different interests uh and what they want to different ideas for what kind of uh interesting pursuits they want to direct their ais and uh

**[1:05:28]** like they can people people could uh like um yeah do a lot of um AI doesn't necessarily have an intrinsic uh like um any kind of intrinsic desire of its own unless we put we put it in uh the

**[1:05:45]** system. So I think uh so people can still end up being even if AI's uh like become extremely capable. Uh I would hope that people are still the drivers uh of like what the AIs end up doing. Yeah. But I wonder if the economic

**[1:06:01]** equilibrium is so far from that where um you have sort of the equivalent of Amdall's law in a firm. The slowest part of the process is the one that's going to bottleneck you. And so even if the AI makes all the non-human parts of the

**[1:06:15]** firm 10x more efficient, the firm can no long, you know, it's it's still bottlenecked by that step. And so um if in the if like one company decides to proceed by keeping humans in the loop on all the things that you really want um

**[1:06:28]** human oversight on, then they'll just be out competed by other companies. If one country decides to go this route, other countries will beat it. this doesn't seem I hope this is like yeah I wonder if this is a sort of a sustainable uh

**[1:06:40]** plan for keeping humans in the loop right so I think if you um if we wanted to keep uh humans in the loop uh which seems reasonable um and uh it turned out that um firms with any humans in the loop were out competed with by firms

**[1:06:56]** that didn't have any humans then I think then you would obviously need some kind of regulation that uh like disallowed um having no humans in the loop for running a whole company but there's so many companies in the

**[1:07:10]** world in well I guess in any country but let alone the world but yeah I wonder if it's better to do the regulation on companies and to say like you got to keep you in the loop on important processes but then you got to define

**[1:07:23]** what important processes are you got to monitor every single company um and you also got to get collaboration in every single country which has firms in it versus if this is a problem, should it be solved before the model is even

**[1:07:37]** deployed such that hopefully you would get into a situation where if you did decide to build a firm end to end on these models, it's basically does what you want it to do and you don't need a human in loop. Does that question make

**[1:07:50]** sense? Like I guess I'm just wondering in this situation, how do we actually monitor every single firm as a human in the loop and what happens if like China doesn't decide to do that and so forth, right? Um

**[1:08:01]** yeah, you would either e either have to have uh like um every country uh agree to this regulatory regime or you would need every um you need all of the model infrastructure or the model providers to agree to this uh kind of requirement. Um

**[1:08:16]** so it's definitely uh going to be non-trivial. Um so uh I guess uh yeah this is looking a ways ahead so it's a little hard to imagine uh to imagine this world um before seeing

**[1:08:32]** anything anything like it um but uh so for example uh like there's some questions like would uh are we actually confident that uh AI run companies are uh better in every way or do we think they're better most of the time But

**[1:08:49]** occasionally they um malfunction because AIS are still like they're still less sample efficient in certain ways like dealing with very wacky situations. So um so actually uh AI run firms have higher tail risk because they're more

**[1:09:04]** likely to malfunction in a big way. So I guess that there might be some question practical questions like that that would that would also determine how things play off like play out like maybe uh maybe if you just require people to um

**[1:09:17]** be accountable for various like liability this would also change the incentives a bit. Um, so if it turned out that uh like AIS are better at running everything and they're also completely benevolent and we've like

**[1:09:31]** totally solved alignment and we can like they're better at um being accountable to uh like their uh to people than people are, then I would say uh maybe maybe it's okay having the AIs run the firms. But I think that's uh that might

**[1:09:47]** be pretty far out. And I think we we're more likely to be in a situation where they look better uh like in the short term, but they still have some problem like the AI run entities still have some serious problems and uh it's actually

**[1:10:00]** like practical considerations that push you more towards having humans in the loop at least for the near future. Okay. So, this is a problem you have to deal with today with RLHF where you have to aggregate preferences across a lot of

**[1:10:12]** different humans. Um, and it'll be maybe more marked with future more powerful systems. But when you say, well, we want these eventual AI systems that are going to fully replace humans as part of these firms to be aligned, what what does that

**[1:10:26]** mean? Like, will it mean that they basically do what the user wants them to do? Does it mean that they have to result in some sort of global outcome that we're happy with as the kind of people with the stakeholders in open

**[1:10:40]** like what concretely would the would that mean? If the models are being used um it like uh for these um higher stakes uh use cases then we would have to think about RHF in a much different way than we are

**[1:10:54]** right now. Um so I would say we're not quite um yeah we're not quite ready for that or the current methods um might not be completely sufficient but I would say um I would say we would need to make compromises between uh the uh needs of

**[1:11:12]** the different stakeholders involved. So, so we have this uh this document that uh that we're releasing called the spec uh model spec and um it's about how we want our models to behave in um in the API and in chat GBT and we sort of we try to

**[1:11:29]** uh talk about this issue where there are different stakeholders involved and sometimes there are conflicts between what they might want like uh like the uh in our case we were thinking of the stakeholders as uh the user uh there or

**[1:11:44]** the end user that means like someone sitting in front of chatbt or or some other app. Um the developer so this is like someone using the API um who might be serving other end users with their app like the um the platform um which is

**[1:12:01]** open AI like um we don't want the models to um expose like expose us to legal risk and so forth. Um and then uh the rest of the human of humanity uh including people not uh part of the like who might not be users or customers or

**[1:12:18]** anything. So obviously uh like the user might ask uh uh ask the model to do something that we think is uh like actively harmful to other people. Um and uh so we might have to refuse that. Um by the way this isn't

**[1:12:33]** the order of uh priority necessarily. [clears throat] So this is just like we have these uh four or so classes of stakeholder. Actually, you could also say maybe in the future we'll say the model itself, the model itself. So I

**[1:12:46]** would say we're not going there yet. Um but anyway, they um yeah, we have these different stakeholders. Sometimes they have conflicting demands and uh we have to make some call on how to resolve those conflicts and it's not always

**[1:13:01]** obvious how to do that. Um so uh I would say we had to think through um yeah we we just had to think through the trade-offs and basically the uh like the rough heristic is that we mostly want the models to uh follow your

**[1:13:16]** instructions and be helpful uh to the user and the developer. Um but uh when this impinges on other people's uh on um other people's happiness or uh or way of life, this becomes a problem and we we have to block certain kinds of uh usage.

**[1:13:35]** Uh but we don't want to be too um we we mostly want the models to just be an extension of people's will and do what they say. We don't want to be too paternalistic. We want to be kind of neutral uh and not like impose our

**[1:13:47]** opinions on people. Uh yeah, we we want to most mostly uh let people do do what the they want with uh the models. I got a chance to read the spec beforehand and it it was uh I I guess it's a question of how well that transfers over to how

**[1:14:05]** the model itself behaves, but the I was impressed with how sensible the trade-offs were. like it made sense that this is the it was like explicitly stated the actual edge cases rather than the kinds of things where everybody can

**[1:14:19]** which are obvious like in this case you really are going after the edge cases. Yeah. We wanted it to be very actionable so that it wasn't just a bunch of nice sounding principles but it was like each uh each example kind of tells you

**[1:14:30]** something about some non-obvious uh situation and reasons through that situation. Yeah. Okay. Now I have a couple questions about the uh uh the state of the research itself. So

**[1:14:42]** famously in the social sciences things are really hard to replicate and it's a question about how much of the science there is real versus these uh manufactured bespoke sorts of experiments. When you look at the

**[1:14:55]** average ML paper does it feel like the like a really solid piece of literature or does it feel often like it's the equivalent of what p hacking is in the social sciences? Everyone has their complaints about the

**[1:15:09]** ML literature, but I would say overall I think it's um a relatively healthy field compared to some other ones like in the social sciences um just because uh well it's grounded uh it's largely grounded in practicality and getting things to

**[1:15:26]** work and uh um if you uh if you publish something that can't be uh replicated easily then people will just forget about it. So uh and it's like accepted that often you um you don't just report someone's uh

**[1:15:42]** number from their paper, you also try to reimplement their method and compare it to your method on the same uh say on the same training data set. So I think pe if you if you publish methods that are um like really hard to implement or uh

**[1:15:55]** don't or are really finicky um they'll tend to get um forgotten and as a result people actually try to open source their work a lot. I guess there's also there's various um um like incentives uh that there's various unfavorable incentives

**[1:16:13]** like um yeah people are incentivized to uh make the baseline methods like the methods they're comparing to worse and uh like there are other um like mild pathologies like trying to make your methods seem sophisticated

**[1:16:27]** mathematically. Um but I would say overall uh I feel like the field makes progress and I would probably like to see a little bit more um science and uh trying to understand things rather than more like uh hill climbing on benchmarks

**[1:16:43]** and trying to propose new methods and there's been a decent amount of that recently but uh yeah I think it's uh we could use more of that and I think that's a good thing for like academics to work on. Um, oh yeah, on the social

**[1:16:58]** sciences, uh, on a slightly different note, uh, I think actually, um, I would be really excited to see more research on, uh, using, um, base models to do, um, simulated social science. Uh, because, uh, these models have a a

**[1:17:15]** probabilistic model of the whole world. And you can uh set up like a simulated questionnaire or um like a conversation and um like and you can look at how any anything is correlated like any um any traits that you might imagine. You can

**[1:17:31]** see how they might be correlated with other traits. So it would be pretty cool to see if people could replicate some of the like more notable results in the social sciences like like moral foundations and that sort of thing by

**[1:17:44]** just like uh prompting base models in different ways and seeing what's correlated. What what is that Stanford experiment? The um the the one where they the Ash conformity test, right? It' be fun if that replicated with language

**[1:17:57]** models as well. Um that would be interesting. with the rest of the research that happens at big labs, how much of it is increasing the uh or decreasing the amount of compute you need to get uh a

**[1:18:11]** certain result as an actual computer multiplier versus how much of it is things that are just making the learning more stable and just building out the infrastructure. I guess the broader question I'm trying to ask is since GPD4

**[1:18:23]** does it feel like with the same amount of comput we can train a much better model or does it feel like oh we've like made sure the learning can happen better and in a more scalable scalable way with GPD5 but it's not like uh we can train

**[1:18:35]** GP4 with like GP 3.5 budget now or something like that. Yeah. Well um definitely there's always progress in improving the efficiency. um whenever you have a 1D u performance metric, you're going to find that uh

**[1:18:49]** like uh different improvements um can kind of substitute for each other. Uh so you might find like uh you might find that you uh post-training and um pre-training both improve the metrics or uh like improve uh they they'll have a

**[1:19:06]** different slightly different profile of which metrics they improve but uh if if at the end of the day you have a single number they're both going to they're going to substitute for each other. Yeah.

**[1:19:15]** Uh somewhat. So I would say for something like a like a human evaluation like what do humans prefer? uh we've definitely made a lot of progress on both sides like pre-training and post- trainining and improving that.

**[1:19:29]** Okay, a couple of rapid fire questions about RHF. So obviously RHF is important to make these models useful. So maybe the labbotomized description is inaccurate but there is a sense in which all these models once they're put in a

**[1:19:46]** chatbot form have a very similar way of speaking. They really want to delve into things. They want to turn things into bullet points. They often seem sort of have this formal and dull way of speaking. Uh, and there's complaints

**[1:20:00]** that they're not as creative like what we're talking about before with it can only do rhyming poetry and not not rhyming until recently. I guess is that a result of the particular way in which RHF happens now? And if so, like is it

**[1:20:14]** because of who the raiders are? Is it because of what the loss function is? Why is this the way all chatbots look? Yeah, I would say there's a decent amount of room for variation in exactly uh how you do the training process. And

**[1:20:25]** uh I think we have a lot of um I'd say we're um actively trying to improve this and make the writing more lively and uh and more fun. And I think we've made some progress like improving the personality of chatbt. So it is um it is

**[1:20:39]** more fun and like you it's it's better when you're uh trying to chitchat with it and so forth. Uh it's less robotic. Um, I would say, um, yes, it's a kind of interesting question how some of the the ticks came about

**[1:20:54]** like, um, like the word delve. I've actually caught myself using the word a bit [laughter] recently. Um, so I don't know if it rubbed off on me from from the model or what. Uh but um actually I think there's also there

**[1:21:08]** might be some funny effects going on where there's like unintentional distillation uh happening between the language model providers where like if you hire someone to um go do a labeling task, they might just be feeding uh

**[1:21:23]** feeding it into a model. They might just be pulling up their favorite uh chatbot and uh like feeding it in and having the model do the task and then copy and pasting it back. So there might be uh that that might account for some of the

**[1:21:36]** convergence, but also I think some of the things we're seeing are just what uh what people like. I mean I think people do like bullet points. They like the structured uh responses. Uh people do often like the big info dumps that they

**[1:21:49]** get uh from the models. Uh so yeah I think there's um so it's not completely clear um how much is just a quirk of uh the uh particular uh like choices and uh like design design of the um post- trainining processes and how much is

**[1:22:13]** actually intrinsic to uh like what people actually want. It does seem persistently more verbose than um some people want and maybe just because during the labeling stage the raiders will uh prefer the more verbose answer

**[1:22:29]** but um I I wonder if it's if it's inherent to because of the how it's free trading the stop sequence doesn't come up that often and like it really wants to just keep going or there might be some biases in the

**[1:22:40]** labeling that lead to verbosity like the fact that we tend to um train for one message at a time rather than the full interaction. So, uh, like if you only see one message, um, then something that just has like a clarifying question or

**[1:22:56]** maybe a short response with an invitation to follow up is going to be, um, it's going to look less complete than something that, um, covers all possibilities. Um, there's also a question of what people uh, whether

**[1:23:09]** people's preferences would change depending on how fast the model is streaming its output. uh like uh like clearly if you're sitting there waiting for it to waiting for the tokens to come out, you're gonna prefer that it gets to

**[1:23:21]** the point. Yeah. But if it just gives you a um like a a dump of text instantly, maybe you don't actually care if there's a bunch of boilerplate or uh like if there's a bunch of stuff you're going to skim, you'd rather just have it

**[1:23:32]** all there. Yeah. Um the the reward model is I think such an interesting artifact because it's the closest thing we have to an aggregation of what people want, what preferences they have. um

**[1:23:48]** when you think about models that are much smarter, the kind of way in which we'll um I mean one hope would be that you could just give a sort of like list of things we want um that are not sort of trivial and

**[1:24:04]** obvious kinds of like UN declaration of rights things. Um, on the other hand, I think I heard you make the point that well, a lot of our preferences and values are very subtle and so that they might be best represented through these

**[1:24:17]** pair wise preferences. When you think of a GPD6 or GBD7 level model, are we giving it more of like a written instructions or are we still doing which kind you know these sorts of like subliminal preferences?

**[1:24:31]** Yeah, that's that's a good question. So I think uh like these preference models do learn a lot of subtleties um of uh yeah subtleties about what uh what people prefer um that are would be hard to articulate in a like in an

**[1:24:46]** instruction manual. Yeah. Um maybe if you um like uh obviously you can write an uh like an instruction manual that has lots of examples of comparisons. Um and that's like that's what the model spec has. it has a lot of

**[1:25:01]** examples with some explanation. Um so uh it's not clear what the optimal uh format is for um describing uh preferences. I would guess that whatever you can get out of uh like a big data set that captures fuzzy preferences, you

**[1:25:19]** can uh distill it down to a like a smaller a shorter document that mostly captures the ideas. And uh and I would think that the big uh like like the bigger models are like they do um like uh learn a lot of these concepts

**[1:25:36]** automatically of what people might find uh like they'll have some uh uh they'll just learn from all the pre-training data what uh people would find useful and helpful and uh what they'll have uh like some there'll be

**[1:25:51]** some complex uh like uh like moral theories uh that they can they have and they can uh but of course there's still a lot of uh um room to latch on to a different uh like different style or a different morality. So I think like when

**[1:26:06]** we have um like if we were to write a um a doc or if we're going to align these models, what we're doing is latching on to a specific uh like specific style, a specific um morality. And there's still like a decent you still need a decent uh

**[1:26:24]** decently long document to uh to capture exactly what you want. Yeah. Uh how much of a mode is better post training? Currently companies that distinguish themselves by well how big is our model

**[1:26:36]** and so forth? Will it be a big moat who has figured out all the finickiness that you were talking about earlier with regards to uh all this data? I think there's something of a moat because it's just a very complex uh operation and

**[1:26:49]** there's uh so it takes uh you have to have a lot of uh skilled people doing it and uh so there's a lot of tacid knowledge and uh um there's uh a lot of organizational knowledge uh that's required. So um so I

**[1:27:06]** think um yeah I think post- training uh like to create a model that actually um like has all the need the functionality people care about um uh is a pretty complicated uh requires a pretty complicated effort. Um so and this um

**[1:27:24]** requires a lot of this is basically an accumulation of a lot of R&D. Um, so I would say um I I would say that makes it somewhat of a mo that it's not trivial to spin this up immediately. Uh it does seem like um like the same

**[1:27:42]** companies that are putting together the most serious uh pre-training efforts are also putting together the serious post-training efforts. So, uh it seems like uh it is uh it is somewhat um somewhat

**[1:27:56]** possible to copy or to to spin up more of these efforts. Um there's also like one force uh that sort of makes it less of a mode is that you can uh like distill the models or you can take someone else's model and clone the

**[1:28:10]** outputs or you can uh use someone else's model as a judge uh to like do comparisons. So, I think uh like the more big league people probably aren't doing that because it goes against uh terms of service policies, but and it

**[1:28:25]** would also be a sort of hurt hit to their pride, but I would expect some of the smaller players are doing that to get off the ground and that catches you up to a large extent.

**[1:28:35]** I guess it helps clear them out. What What is the media radar like? Where are they based? What are their politics? Uh what is their sort of knowledge level? I would say it's um it varies a lot. So we've definitely um hired uh raiders

**[1:28:50]** with different um skills uh or for different kinds of tasks or um projects. Um so I would say um like a decent um a decent mental model is uh just look at people who are on Upwork and other platforms like that like who's doing um

**[1:29:09]** sort of odd odd jobs with remote work. Um so it's um yeah it's a pretty international group there. There's a decent number of people in the US. Uh we hire different um people uh like different um groups of people for

**[1:29:26]** different types of labeling like whether we're more f focused on uh writing um or like STEM tasks. So uh people doing STEM tasks are more likely to be in India or other sort of um like uh middle or lower middle inome countries uh whereas people

**[1:29:44]** um doing more like English writing and composition tend more to be like US-based. Um so yeah and I'd say there there have been times when we needed to um hire different experts for some of our

**[1:29:58]** campaigns. uh some of the people are very some of them are very talented and uh like we even find that they're like at least as good as as us the researchers at doing these tasks and they're like much more careful than us.

**[1:30:11]** So I would say uh I would say the people uh we have now are um quite skilled and uh conscientious. M um with with regards to the sort of plateau narrative, one of the things I've heard is that a lot of the abilities these models have to help

**[1:30:28]** you with specific things is related to the having very closely matched labels within the uh supervised fine-tuning data set. Uh is that true? like if if it can teach me how to use ffmpeg

**[1:30:42]** correctly, like there's somebody who's like doing figuring out seeing the inputs and seeing what flags you need to add and some human is figuring that out and smashing to that and is yeah, do you need to hire like all these labelers who

**[1:30:58]** have domain expertise in all these different domains? Um because if that's the case, it seems like it would be a much bigger slog to get these models to be smarter and smarter over time, right? You don't exactly need that. Um

**[1:31:09]** because uh yeah, you can get quite a bit out of generalization. Um so if you um like uh like the base model has already um been trained on tons of documentation, tons of code with shell scripts and so forth. So it it's already

**[1:31:25]** seen all the ffmpeg man pages and uh lots of bash scripts and everything. And uh it's um so uh like the base even just giving the base model a good fuchia prompt you can get it to uh answer queries like this and uh just training a

**[1:31:43]** preference model uh like for helpfulness will um uh even if you don't train it on um probably even if you don't train it on any stem it'll somewhat generalize to stem and uh uh like um so so Not only do you not need uh like examples of how to

**[1:32:03]** use f ofmpeg, you might not even need anything with programming uh to get some reasonable behavior in uh the programming domain. Maybe final question is we've touched on this in different ways but to put it

**[1:32:16]** together. So you say you're turning on much more multimodal data presumably like these things understand what screens look like and we'll be able to interact interact with it in a much more coherent way. And also you're going to

**[1:32:29]** do this along Horizon RL. So they'll be able to act as agents in the systems who can be part of your workflow in a much more integrated way. What what do you expect that to look like and what will be the next steps

**[1:32:44]** from there? So suppose by the end of the year or next year you have something that's like an assistant who can work with you on your screen. Does that seem like first of all a sensible thing to expect and then where does it go from

**[1:32:54]** there? I would definitely um yeah, I would expect uh things to move in that direction. Um it's unclear what's going to be the best form factor, whether it's like uh something that's uh it's like a

**[1:33:07]** Clippy that's on your computer and helping you with something or if it's more like a um like helpful colleague in the cloud. So, we'll see uh which kinds of form factors um work the best. And I would expect people to try all of them

**[1:33:21]** out. Um, yeah, I would expect more uh like Yeah, I would expect something like a um yeah, the mental model of a like a um helpful assistant or helpful colleague to become more real. Um where you can

**[1:33:36]** share more of your uh everyday work or have it uh like instead of just giving it one-off queries, you would have a whole project that you're doing and it knows about everything you've done on that project so far. you can tell it uh

**[1:33:49]** it can um like even proactively um make suggestions like uh maybe you can tell it oh yeah like remember to um ask me about this and if I've made any progress on it. So I think like proactivity is one thing that's

**[1:34:03]** been missing. Uh yeah, I'd really love to see um better um like um a more uh like moving away from sort of one-off queries uh like using the model kind of like a search engine. Yeah. A smarter search engine and more towards

**[1:34:20]** uh like having a whole project that um I'm like doing in collaboration with the model and it knows everything I've done. it's proactively uh like um suggesting things for me to try or it's going and doing

**[1:34:32]** work in the background. Yeah, that's that's that's really interesting. What by the way, it's a final question. What is your what is your median timeline? You know, replaces your job.

**[1:34:41]** Yeah. Oh, replaces my job. Uh maybe like uh five years. Yeah, pretty soon. Yeah. Um interesting. Okay. Well, John, this is super interesting. Uh um yeah, thanks

**[1:34:56]** so much for making the time. I think this like seems like one of the parts of the AI process that are super important and people don't uh understand that much about. So it was super interesting to delve into it and get your thoughts on

**[1:35:08]** it. But yeah, thanks for having me on the podcast. It was uh fun to talk about all this stuff. Hey everybody, I hope you enjoyed that episode. John, he's just a very

**[1:35:17]** thoughtful guy and it's super interesting to learn about the way in which these models become the kind of shaga that they are. Anyways, as you can see, I'm now doing ads on the podcast. So, if you'd like to advertise, you can

**[1:35:28]** reach out at the link in the description. And of course, if you enjoyed the episode, it's really helpful if you can share it with other people who you think might enjoy it, your friends, group chats, Twitter, whatever

**[1:35:37]** else. See you on the next one. Cheers. [music]
