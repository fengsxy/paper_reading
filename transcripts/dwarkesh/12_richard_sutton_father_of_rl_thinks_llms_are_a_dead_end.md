---
layout: default
type: transcript
series: dwarkesh
episode: 12
guest: ""
title: "Richard Sutton – Father of RL thinks LLMs are a dead end"
source_url: "https://www.youtube.com/watch?v=21EYKqUsPfg"
analysis_url: /transcripts/dwarkesh/12_richard_sutton_father_of_rl_thinks_llms_are_a_dead_end.analysis/
permalink: /transcripts/dwarkesh/12_richard_sutton_father_of_rl_thinks_llms_are_a_dead_end/
---

# Transcript: Richard Sutton – Father of RL thinks LLMs are a dead end

Source: https://www.youtube.com/watch?v=21EYKqUsPfg

---

**[00:00]** Why are you trying to distinguish humans? Humans are animals. What we have in common is more interesting. What distinguishes us, we should be paying less attention to. >> I mean, we're trying to replicate

**[00:09]** intelligence, right? No animal can go to the moon or make semiconductors. So, we want to understand what makes humans special. >> So, I like the way you consider that obvious, cuz I consider the opposite

**[00:18]** obvious. If we understood a squirrel, we'd be almost all the way there. I am personally just kind of content being out of sync with my field for a long period of time perhaps decades because occasionally I have improved right in

**[00:32]** the past. I don't think learning is really about training. It's about an active process. The child tries things and sees what happens. I think we should be proud that we are giving rise to this great transition in the universe.

**[00:47]** Today I'm chatting with Richard Sutton who is one of the founding fathers of reinforcement learning an inventor of many of the main techniques used there like TD learning and policy gradient methods and for that he received this

**[00:59]** year's touring award which if you don't know is basically the Nobel Prize for computer science Richard congratulations >> thank you Darish >> and uh thanks for coming on the podcast >> it's my pleasure

**[01:09]** >> okay so first question my audience and I are familiar with the LLM way of thinking about AI conceptually What are we missing in terms of thinking about AI from the RL perspective? >> Well, yes, I think it's really quite a

**[01:24]** different point of view and it's it can easily get separated and lose the ability to talk to each other. >> Mhm. >> And um yeah, large language models have become such a big thing. Generative AI

**[01:36]** in general a big thing. Um and our field is subject to bandwagons and fashions. So we lose we lose track of the uh basic basic things because I consider reinforcement learning to be basic AI and what is intelligence are the problem

**[01:52]** is is to understand your world and um reinforcement learning is about understanding your world whereas large language models are about mimicking people doing what people say you should do. They're not about figuring out what

**[02:06]** to do. >> Huh. I guess you would think that to emulate the trillions of tokens in the corpus of internet text, you would have to build a world model. In fact, these models do seem to have very robust world

**[02:18]** models and they're the best um world models we've made to date in AI. Right. So, what do you think that that's missing? >> I would disagree with most of the things you just said.

**[02:28]** >> Great. >> Just to mimic the the what people say is not really to build a model of the world at all. I don't think you know you're mimicking things that have a model of the world the people

**[02:40]** >> but I don't want to approach the question in an adversarial way uh but but I would I would question the idea that they um they have a world model so a world model would enable you to predict what would happen

**[02:52]** >> right >> they they have they have the ability to predict what a person would say they don't have the ability to predict what will happen what we want I think to quote Alan Turing what we want is a

**[03:04]** machine that can learn from experience, >> right? >> Where experience is the things that actually happen in your life. You do things, you see what happens. Um, and uh that's what you learn from.

**[03:16]** >> Yeah. >> The large language models learn from something else. They learn from here's a situation and here's what a person did. And implicitly the suggestion is you should do what the person did.

**[03:26]** >> Right? I guess maybe the the crux and I'm curious if you disagree with this is some people will say okay so this imitation learning has given us a good prior or given these models a good prior but reasonable ways to approach problems

**[03:38]** and as we move towards the era of experience uh as you call it this prior is going to be the basis on which we teach these models from experience because this gives them the opportunity to get uh answers right some of the time

**[03:53]** and then on this you can build uh you can train them on experience. Do you agree with that perspective? >> No, I I I agree that it's the it's the large language model perspective, right? >> I don't think it's a good perspective.

**[04:06]** >> Yeah. Yeah. Cere. >> So to be a prior for something, there has to be a real thing. I mean, a prior bit of knowledge should be the basis for actual knowledge. What is actual knowledge? There's no definition of

**[04:20]** actual knowledge in that in that large language framework. What makes an action a good action to take? You recognize the value, the need for continual learning, right? So if you need to learn continually, continually means learning

**[04:36]** during the normal interaction with the world. >> Yeah. >> And so then there must be some way during the normal interaction to tell what's right.

**[04:43]** >> Yep. >> Okay. So is there any way for it to tell in the largest language model setup to tell what's the right thing to say? You will say something and you will not get

**[04:56]** feedback about what the right thing to say is >> because there's no definition of what the right thing to say is. There's no goal, >> right?

**[05:04]** >> And if there's no goal, then there's there's one thing to say, another thing to say. There's no right thing to say, >> right? >> So there's no ground truth. You can't have prior knowledge if you don't have

**[05:13]** ground truth because the prior knowledge is supposed to be a hint or an initial belief about what the truth is. >> Yeah. >> But there isn't any truth. there's no right thing to say right now in

**[05:25]** reinforcement learning there is a right thing to say or right thing to do because the the right thing to do is the thing that gets you reward >> right >> so we have a definition of what the

**[05:33]** right thing to do is and so we can have uh prior knowledge or knowledge provided by pe people about what the right thing to do is and then we can check it >> to see because because we have a definition of what the actual right

**[05:45]** thing to do is >> now an even simpler case is when you have you're trying to make a model of the world when you predict what will happen, you predict and then you see what happens.

**[05:55]** >> Okay? So there's ground truth. There's no ground truth in in uh large language models because you don't have a a prediction about what will happen next. If you say something in your in your um conversation, there's the large language

**[06:10]** models have no prediction about what the person will say in response to that or what what the response will be. I mean I think they do like they you can literally ask them what what what would you anticipate a user might say in

**[06:21]** response and they have a prediction. >> Oh no they they they will respond to that question right? >> Yeah >> but they have no prediction in the substantive sense that they won't be

**[06:30]** surprised by what happens and if something happens that isn't what you might say they predicted they will not change because an unexpected thing has happened and there to learn that they'd have to make an adjustment. I I so I

**[06:44]** think a capability like this does exist in context. So it's interesting to watch a model do chain of thought and then suppose it's trying to solve a math problem. It'll say okay I'm going to approach this problem using this

**[06:58]** approach at first and it'll write this out and be like oh wait I just realized this is the wrong conceptual way to approach the problem. I'm going to restart by this another approach and that flexibility does exist in context,

**[07:09]** right? Do you have something else in mind or do you just think that you need to extend this capability across longer horizons? >> I'm just saying they don't have a have a uh in any meaningful sense they don't

**[07:20]** have a prediction of what will happen next and they will not be surprised by what happened next. They'll not make any changes if if something happens. >> But isn't that isn't that isn't that >> based on what happens.

**[07:30]** >> Isn't that literally what next token prediction is? prediction about what's next and then updating on a surprise. >> Next token is what they should say, what the action should be. It's not what the world will give them in response to what

**[07:41]** they do. Let's let's go back to the uh their lack of goal. >> Mhm. >> For me, having a goal is the essence of intelligence, >> right?

**[07:50]** >> Something is intelligent if it can achieve goals. Is I like John McCarthy's definition that intelligence is the computational part of the ability to achieve goals. Yeah. So, you have to have goals. You're you're not you're

**[08:02]** just you're just you're just a behaving system. You you're not you're not any special. You're not intelligent. >> Right. >> And you agree that large language models don't have goals.

**[08:12]** >> I think they No, they have a goal. >> What's the goal? >> Next token prediction. >> That's not a goal. Doesn't it doesn't change the world, you know.

**[08:22]** >> I think tokens come at you and if you predict them, you don't influence them. >> Oh, yeah. I I it's not a goal about the external world. >> Yeah. It's not a goal. It's not a substantive goal. It's not

**[08:35]** You can't look at a system and say, "Oh, it uh has a goal if it's just sitting there predicting and being happy with itself that it's predicting accurately." I I guess maybe the bigger question I want you want to understand is why you

**[08:46]** don't think doing RL on top of LLM is a productive direction because being we we seem to be able to give these models a goal of solving difficult math problems and they're in many ways um at the very peaks of human level in in the capacity

**[09:01]** to solve math olympia type problems right they got gold at IMO so it seems like the model which got gold at the international math Olympia does have the goal of getting math problems right Um so why can't we extend this to different

**[09:14]** domains? >> Well the math problems are different. Um the making a model of the physical world and uh carrying out the consequences of mathematical um assumptions or operations,

**[09:27]** >> right? >> Those are very different things like the the empirical world has to be learned. You have to learn the consequences. Um whereas the uh the math is is more just computational. It's more like standard

**[09:42]** planning. So, so there you can you can um they can have a goal to to um uh to find the proof and they are in in some way given that goal to find the proof. >> Right. So, I mean, it's interesting because you wrote this essay in 2019

**[10:01]** titled The Bitter Lesson, and this is the most influential essay perhaps in the history of AI, but people have used that as a justification for scaling up LLMs because in their view, this is the one scalable way we

**[10:19]** have found to pour ungodly amounts of compute into learning about the world. And so it's interesting that your perspective is that the LLMs are actually not bitter lesson. >> It's an interesting question whether uh

**[10:31]** large language models are are uh a case of the bitter lesson. >> Yeah. >> Because they are clearly um a way of using massive computation things that will scale with computation up to up to

**[10:47]** the limits of the internet. >> Yeah. uh but they're also a way of putting in lots of um human knowledge and uh so so this is an interesting question um it's a sociological or industry question uh

**[11:06]** will they reach the limits of of of the data and and be superseded by things that that are can get more data just from experience rather than from uh from people. Uh in some ways it's a classic case of the of the of the bitter

**[11:28]** lesson with the more the more human knowledge we put into the large language models the better they can do and so it feels good. Um and yet uh one well I in particular expect there to be systems that can

**[11:43]** learn from experience and which could well perform much much better and be much more scalable. In which uh case it will be another instance of the bitter lesson that the things that that used human knowledge were eventually

**[11:58]** superseded by things that just um trained from uh experience and computation. I I guess that doesn't seem like the crux to me because I think those people would also agree that the overwhelming amount of compute in the

**[12:12]** future will come from uh learning from experience. They just think that the scaffold or the basis of that the thing you'll start with in order to pour in the compute to do this future experiential learning or on the job

**[12:26]** learning will be LLMs. And so I I guess I I still don't understand why this is the wrong starting point altogether. Why we need a whole new architecture to begin doing experential continual learning. Uh and why we can't start with

**[12:43]** LLMs to do that. >> Well, in every case the bitter lesson, you know, you could start with uh human knowledge, >> right? >> And then just and then do the scalable

**[12:53]** things. >> Yeah, >> that's always the case. And there's no never any reason why that has to be bad, >> right? >> But in fact and in practice it has

**[13:02]** always turned out to be bad because people get locked into the human knowledge approach and they psychologically or you know now I'm now I'm speculating why it is but this is what has always happened.

**[13:15]** >> Yeah. >> That uh yeah they get they get their lunch gets eaten by the methods that are truly scalable. >> Yeah. Give me a sense of what the scalable method is. The scalable method

**[13:26]** is you learn from experience. Um you uh you you try things, you see what you see what works. No one no one has to tell you. First of all, you have a goal. So without a goal, uh there's no sense of right or wrong or better or worse. So

**[13:41]** large language models are trying to get by without having a goal or a sense of better or worse. That's just, you know, it's exactly starting in the wrong place. May maybe it's um interesting to compare this to humans. So in both the

**[13:56]** case of learning from imitation versus experience and on the question of goals, I think there's some interesting analogies. So you know kids will initially learn from imitation. Uh you don't think so?

**[14:11]** >> No, of course not. >> Really? >> Yeah. I think kids just like watch people. They like kind of try try to like say the same. >> How old are those these kids?

**[14:22]** >> I I think the level >> What about the first six months? >> I think they're kind kind of imitating things. They're trying to like make their mouth sound the way they see their mother's mouth sound. And then they'll

**[14:30]** say the same words without understanding what they mean. And as you get older, the complexity of the imitation they do increases. So that's you're you're you're you know, you're imitating maybe the skills that your uh people in your

**[14:41]** band are using to hunt down the deer or something. And then you go into the learning from experience RL regime. But I think there's a lot of imitation learning happening with uh humans. >> Yeah. Surprising. Yeah. You can have

**[14:53]** such a different point of view. >> Yeah. >> Um when I see kids, I see kids uh just trying things and like waving their hands around and moving their eyes around and no one no one tells them

**[15:05]** there. There's no there's no um imitation for uh how they move their eyes around or even the sounds they make. They may they may want to create the same sounds but the um the actions you know the thing that the uh infant

**[15:20]** actually does there there's no targets for that there are no examples for that >> I agree that it doesn't explain everything infants do but I think it guides a learning process I mean even LLM when it's trying to predict the next

**[15:31]** token early in training it will like make a guess it'll be different from what like it actually sees and in some sense it's like very short horizon RL where it's like making this guess of like I think this token will be It's

**[15:41]** actually this other thing similar to how a kid will try to say a word, it comes out wrong. >> The the large language models is learning from training data. It's not learning from experience.

**[15:51]** It's it's learning from something that will never be available during its normal life. There's never any uh training data that says you should do this action in normal life.

**[16:02]** >> I I think this is maybe more of a semantic distinction like what do you call school? Is that not training data? You're not like going to school because it's like >> school is much later. Okay, I shouldn't

**[16:13]** have said never, but but I I don't know. I think I would even say it about school, but formal schooling is is the exception. You should base your >> of learning where I think you're just sort of programming in your biology that

**[16:26]** like early on you're not that useful and then like kind of why you exist is to understand the world and like learn how to interact with it. Um, and seems kind of like a training phase. I agree that then there's like a sort of more gradual

**[16:40]** there's not a sharp cut off to like training to deployment, but there seems to be this like initial training phase, right? There's nothing where where you have training of what you should do. There's nothing you you you see things

**[16:53]** that happen. You're not you're not told what to do. Don't don't don't be difficult. I mean, this is obvious. >> I mean, you're like literally taught what to do. This is like where the word

**[17:04]** training comes from is from humans, right? >> So I don't think uh learning is really about training. I think learning is about about learning. It's about an active process. The child tries things

**[17:16]** and sees what happens. >> Right. >> Yeah. It does not we don't think we don't think about training when we think of the an infant growing up. These these things are

**[17:27]** actually rather well understood. If you go to look about how psychologists think about learning, there's nothing like uh imitation. Maybe there are some extreme cases where humans might do that or appear to do that, but there's no basic

**[17:43]** animal learning process called imitation. There basic animal learning processes for prediction and for trial and error control. I mean, it's really interesting how sometime the most hardest things to see are the obvious

**[17:57]** ones. It's obvious um if you just look at animals and how they learn and you look at psychology and how our theories of them um it's obvious that that supervised learning is not part of uh the way animals learn. We don't have we

**[18:14]** don't have examples of desired behavior. What we have is examples of things that happened, things one things that followed another and we have examples of we did something and and and there were consequences but there are no

**[18:29]** examples of supervised learning. I mean there are no supervised learning is not something that that happens in nature and you know school even if that was the case you know we should forget about it because it's it's just this that's some

**[18:43]** special thing that happens in people. doesn't happen broadly in nature and you know squirrels don't go to school. Squirrels can learn all about the world. It's absolutely obvious I would say that um supervised learning doesn't happen in

**[18:58]** animals. So I I I interviewed this psychologist and anthropologist Joseph Henrik who has done work about cultural evolution and basically how did what you know what distinguishes humans and how do humans pick up knowledge. Why are you

**[19:14]** trying to distinguish humans? Humans are animals. What we have in common is more interesting. What we have what distinguished us we we should be paying less attention to.

**[19:25]** >> I mean we're trying to replicate intelligence, right? So if you want to understand what is it that >> enables humans to go to the moon or to build semiconductors. I think the thing we want to understand is the thing that

**[19:37]** makes it no animal can go to the moon or make semiconductors. So we want to understand what makes humans special. >> So I like the way you consider that obvious cuz I consider the opposite obvious.

**[19:47]** Yeah. I think we we need to we we have to we have to understand how we are animals and we if we understood a squirrel I think we'd have a we'd be almost all the way there to understanding human intelligence. The

**[20:01]** the language part is just a a small veneer on the surface. Okay. So this is great. You know we're finding out the very different ways that we're thinking. >> We're not arguing. We're trying to share

**[20:14]** share our different ways of thinking with each other. >> Yeah. And you I think argument is useful. So um uh yeah but I do want to complete this thought. So Joseph Henrik has this interesting theory that uh if

**[20:26]** you look a lot of the uh skills that humans have had to master in order to be successful and we're not talking about you know last thousand years or last 10,000 years but hundreds of thousands of years. uh you know the world is

**[20:39]** really complicated and it's not possible to reason through how to let's say hunt a uh seal if you're living in the Arctic. And so there's this many many stepong process of how to make the bait and how to find the seal and then how to

**[20:58]** process the food in a way that make sure you won't get poisoned. And it's not possible to reason through all of that. And so over time, yes, there's this like larger process of whatever analogy you want to use, maybe something else where

**[21:12]** culture as a whole has figured out how to uh find and kill and eat uh seals. But then what is happening when through generations this knowledge is transmitted is in his view that like there you just have to imitate your

**[21:30]** elders in order to learn that skill because you can't you can't think your way through how to hunt and kill and process a seal. You have to just watch other people maybe make tweaks and adjustments. Uh and that's how cultural

**[21:41]** knowledge accumulates. But the the initial step of the cultural gain has to be imitation. But maybe you think about it a different way. >> No, I think about it the same way. >> Okay. But still it's a small thing on

**[21:53]** top of basic trial and error learning, >> prediction learning, and it's what distinguishes us perhaps from from many animals. >> But we're an animal first. >> Yeah.

**[22:07]** >> And and we were an animal before we had language and all those other things. I do think you make a very interesting point that continual learning is a capability that most mammals have. I guess all mammals have. So it's quite

**[22:22]** interesting that we have something that all mammals have but our AI systems don't have, right? Whereas maybe like the ability to understand math and solves difficult math problems depends on how you define math. But like these

**[22:35]** this is a capability our AIs have but that no almost no animal has. And so it's quite interesting what ends up being difficult and what ends up being easy. >> Morix paradox.

**[22:47]** >> That's right. >> For the era of experience to commence, we're going to need to train AIs in complex real world environments. But building effective RL environments is hard. You can't just hire a software

**[22:57]** engineer and have them write a bunch of cookie cutter validation tests. Real world domains are messy. You need deep subject matter experts to get the data, the workflows, and all the subtle rules right. When one of Labelbox's customers

**[23:09]** wanted to train an agent to shop online, Labelbox assembled a team with a ton of experience engineering internet storefronts. For example, the team built a product catalog that could be updated during the episode because most shopping

**[23:21]** sites have constantly changing state. They also added a Reddis cache to simulate stale data since that's how real e-commerce sites actually work. These are the kinds of things that you might not have naively thought to do,

**[23:32]** but that label box can anticipate. These details really matter. Small tweaks are often the difference between cool demos and agents that can actually operate in the real world. So whether it's correcting traces that you already

**[23:43]** produced or building an entirely new suite of environments, Labelbox can help you turn your RL projects into working systems. Reach out at labelbox.com/thearcash. All right, back to Richard.

**[23:58]** >> This alternative paradigm that you're imagining, >> the experential paradigm, let's lay out a little bit what it is. It says that experience action sensation well sensation action reward and this happens

**[24:12]** on and on and on makes for life. It's it says that this is the uh foundation and the focus of intelligence. Intelligence is about taking that stream and altering the actions to increase the the rewards in the stream.

**[24:28]** >> Right? So learning then is from the stream and learning is about the stream. So it's that that second part is is is particularly telling you know that what you learn your knowledge your knowledge is about the stream. Your knowledge is

**[24:44]** about if you do some action what will happen or it's about uh which events will follow other events. It's about the stream. It's the content of the knowledge is is statements about the stream. Um, and so because it it's it's

**[25:00]** a statement about the stream, you can test it by comparing it to the stream and you can learn it continually. >> So when you're imagining this future continual learning agent, >> they're not future. Of course, we they

**[25:12]** exist all all the time. It's I mean this is what reinforcement learning paradigm is learning from experience. >> Yeah, I guess the maybe I what I meant to say is uh human level general continual learning agent.

**[25:23]** >> What is the reward function? Is it just predicting the world? Is it uh is it then having a specific effect on it? What would the general reward function be? >> The reward uh function is arbitrary

**[25:37]** and um so if you're playing chess, it's to win the game of chess. If you were to um uh if you're a squirrel, maybe the the reward has to do with getting nuts, >> right?

**[25:50]** Um in general for an animal you would say the reward is to avoid pain and to acquire pleasure >> right >> uh and there's also would be a component

**[26:02]** having to do with uh I think there would be should be a component having to do with your uh increasing understanding of your of your environment that would be sort of an intrinsic motivation. >> I see. I guess this AI would be deployed

**[26:18]** to like lots of people would want it to be doing lots of different kinds of things, >> right? So it's performing the task people want but at the same time it's learning about the world from doing that

**[26:29]** task and do you do you imagine okay so we get rid of this paradigm where there's training periods and then there's deployment periods but then is there do we also get rid of this paradigm when there's the model and then

**[26:44]** instances of the model or copies of the model that are you know doing certain things h how do you think about the fact that there we'd want this thing to be doing different things, we'd want to aggregate the knowledge that it's

**[26:56]** gaining from doing those different things. >> I don't like the word model when used the way you just did. I I think a better word would be the network. So, I think you mean the the network. Maybe there's

**[27:09]** many networks. So anyway, things would be learned and then you'd have copies and many instances and sure you'd want to share knowledge across the uh instances and there would be lots of possibilities for doing that like there

**[27:24]** is not today. You can't have one child learn grow up and and learn about the world and then and then every new child has to repeat that process. Whereas with AIS, with a digital intelligence, you could hope to do it once and then copy

**[27:38]** it into the next one as a starting place. >> Right? >> So this would be a huge savings and I think actually it would be much more important than uh trying to learn from

**[27:48]** people. >> I agree that the kind of thing you're talking about is necessary regardless of whether you start from LLMs or not. Right? If you want human or animal level intelligence, you're going to need this

**[28:01]** capability. Suppose a human is trying to make a startup, right? And this is a thing which has a reward on the order of 10 years. Once in 10 years, you might have an exit where you get, you know, paid out a billion dollars. But humans

**[28:12]** have this ability to make intermediate auxiliary rewards or have some way of even when they have extremely rewards, they can still make intermediate steps having an understanding of like what the next thing they're doing leads to this

**[28:26]** grander goal we have. And so how do you imagine such a process might play out with AIS? So this is something we know very well >> and it's the basis of it is temporal difference learning

**[28:36]** >> where the same thing happens um in a less grandiose scale like when you learn to play chess you have the grand the long-term goal is winning the game and yet you you can't you um you want to be able to learn from shorter term things

**[28:51]** like you know taking the your opponent's pieces um and so you do that by having a value function which predicts the long-term outcome right >> and then if You take guys pieces where your prediction about the long-term

**[29:03]** outcome is changed. It goes up. You think you're going to win and then that increase in your in your belief immediately quote reinforces the uh the move that led to taking the piece. >> Mhm.

**[29:16]** >> Okay. So, we have this long-term 10-year goal of making a startup and making a lot of money. And so, when we make progress, we say, "Oh, I'm I'm I'm more likely to uh achieve the long-term goal." and that rewards the the steps

**[29:31]** along the way, >> right? And then you also want some ability for information that you're learning. I mean, one of the things that makes humans quite different from these LLMs is that if you're onboarding on a

**[29:44]** job, you're you're picking up so much context and information, and that's what makes you useful at the job, right? You're uh everything from how your client has preferences to how the company works to everything. Um, and is

**[29:56]** the bandwidth of information that you get from a procedure like TDLearning high enough to have this like huge pipe of like context and tacet knowledge that you need to be picking up the way humans do when they're when they're just like

**[30:09]** deployed? Um I think the crux of this and I'm not sure but the the big world hypothesis seems very relevant and the reason why humans becoming useful on their job is because

**[30:24]** they are encountering the particular part of the world. That's right. And um and it can't have been anticipated and it can't all have been put in in in advance in in uh the world is so huge that you can't the the dream as I see it

**[30:40]** the dream of large language models is you can teach the an the agent everything and it will know everything and it won't have to learn anything online >> right

**[30:50]** >> during its life. Okay. and and your examples are all well really you have to because you can there's a lot to you can teach it but there's all little idiosyncrasies of the particular life they're leading and the the particular

**[31:03]** people they're working with and what they like as opposed to what average people like right >> and so that's just saying the world is really big and so you're going to have to learn it uh along the way

**[31:13]** >> yeah so it seems to me you need two things one is some way of converting this long run goal reward into smaller auxiliary or you know um these like predictive rewards of the future reward or the future reward at least to the

**[31:28]** final reward then you need some other way initially it seems to me you need some way of then okay I'm I need to hold on to all this context that I'm gaining as I'm working in the world right I'm like

**[31:42]** learning about my clients my my company all this information and I'm so I would say you're just doing regular learning. >> Yeah, >> maybe you're using context because in

**[31:54]** large language models, all that information has to go into the context window, >> right? >> But in in a continual learning setup, it just goes into the weights.

**[32:02]** >> Maybe maybe Yeah. So maybe context is the wrong word to use because I mean a more general thing. >> You learn a policy that's specific to the environment that you're finding yourself in.

**[32:10]** >> Yeah. So the question I'm trying to ask is you need some way of getting like how many bits per second are you picking like is a human picking up when they're you know out in the world, right? Um if you're just like interacting over Slack

**[32:25]** with your clients and everything. >> So maybe you're trying to ask the question of it seems like the reward is too small of a thing to to do all the learning that we need to do. But of course we have the uh the sensations

**[32:37]** uh we we have all the other information we can learn from >> right >> we don't just learn from the reward we learn from all the data >> yeah so what is the learning process

**[32:47]** which helps you capture that information >> so now I want to talk about the base common model of the agent with the four parts >> right >> so we need a policy the policy says in

**[33:02]** the situation I'm in what should I do we need a value function. The value function is the thing that is learned with TDarning and the value function produces a number. The number says how well is it going

**[33:13]** >> and then you watch if that's going up and down and use that to adjust your policy. Okay. So the those two things and and then there's also the perception component which is the construction of your uh state representation. This your

**[33:29]** sense of where you are now. And the fourth one is what we're really getting at most transparently. Anyway, the the fourth one is the transition model of the world. Um that's why I am uncomfortable just calling everything

**[33:40]** models because I want to talk about the model of the world. The transition model of the world, your belief that if you do this, what will happen? What will be the consequences of what you do? So your physics of the world, but it's al not

**[33:52]** just physics. It's also um abstract models like you know your model of how you traveled um from California up to Edmonton for this podcast that was a model and that's a transition model and that would be

**[34:03]** >> uh learned and it's not learned from reward it's learned from you did things you saw what happened >> you made that model with the world that is it will be learned very richly from all the sensation that you receive not

**[34:16]** just from the reward >> it has to include the reward as well but it's that's a small part of the whole model small crucial part of the whole model. >> Yeah. One of my friends Toby Ward

**[34:26]** pointed out that if you look at the Muse Euro models that Google Deep Mind deployed to learn Atari games that these models were initially not a general intelligence itself but a general framework for training

**[34:41]** specialized intelligences to play specific games. That is to say that you couldn't using that framework train a policy to play both chess and go and some other game. You had to train each one in a specialized way. And he was

**[34:57]** wondering whether that implies that reinforcement learning generally because of this information constraint you you you can only learn one thing at a time. Uh the density of information isn't that high or whether it was just specific to

**[35:09]** the way that mu0 was done. And if it's specific to uh Alpha Zero, what what what needed to be changed about that approach so that it could be a general learning agent? >> The the idea is totally general. You

**[35:23]** know, uh I do use all the time as my canonical example, the idea of an AI agent is like a person. >> Yeah. And and people uh in some sense they have just one world they live in and um that world may involve chess and

**[35:39]** it may involve Atari games. Uh but those are are are not a different task or a different world. Those are different states right they encounter and so the the general idea is not limited at all. So maybe it would be useful to explain

**[35:53]** what was missing in that architecture or that that approach which this continual learn learning AGI would have they just set it up they didn't it was not their ambition to have one agent across across uh those games. If we want to talk about

**[36:14]** transfer, we should talk about transfer not across games or across tasks, but transfer between states. >> Yeah. I I guess I'm curious about historically, have we seen the level of transfer

**[36:31]** using RL techniques that would be needed to build this kind of >> Okay, good. Good. We're not seeing transfer anywhere. We're not seeing general critical to good performance is that you can generalize well from one

**[36:44]** state to another state. >> We don't have any methods that are good at that. What we have are people um try different things and they they settle on something that that uh a representation that that transfers well or they

**[36:57]** generalize as well. But we have no we don't have any automated techniques to promote. we have very few automated techniques to promote transfer and they're not none of them are used in in modern deep learning.

**[37:10]** >> Um let me paraphrase to make sure that I understood that correctly. It sounds like you're saying that when we do have generalization in these models that is a result of some uh sculpted

**[37:27]** uh >> humans did it. >> Yeah. >> The researchers did it because there's no other explanation. I mean gradient descent will not make you generalize

**[37:35]** well it will make you solve the problem >> right >> it will not make you you know get new data you generalize in a good way generalization means train on one thing

**[37:45]** that affects what you do on the other things so we know deep learning is really bad at this for example we know that if you train on some new thing it will often catastrophically interfere with all the old things that you that

**[37:57]** you knew >> so this is exactly bad generalization Right >> now generalization as I said is some kind of influence of training on one state on other states and generalization

**[38:09]** is not necessarily good or bad right just the fact that you generalize is not necessarily good or bad you can generalize poorly you can generalize well >> right

**[38:16]** >> so you you need generalization always will happen u but we need algorithms that will uh cause the the generalization to be good rather than bad >> I'm not trying to kickstart this uh

**[38:29]** initial uh crux proxy, but I'm just genuinely curious because I I think I'm might be using the term differently. I mean, one way to think about is these LLMs are increasing the scope of generalization from like earlier systems

**[38:42]** which could not really even do a basic math problem to now they can do anything in this class of math Olympia type problems, right? So, you initially start with like they can generalize among addition problems at least. Um uh then

**[38:54]** you generalize to like they can generalize among like problems which require use of different kinds of mathematical techniques and theorems and you know conceptual categories which is like what the math olympiad requires.

**[39:08]** And so it sounds like you don't think of that being able to solve any problem within that category as an example of generalization or let me know if I'm misunderstanding that. Well, large language models so complex. We don't we

**[39:22]** don't really know what information they had prior. We are we have to guess because they've been fed so much. This is one reason why they're not a good way to do science. Uh it's just so uncontrolled, so unknown.

**[39:37]** >> But if you come up with an entirely new, >> they're getting a bunch of things right >> perhaps. And uh so the question is why? Well, it may be that they don't need to generalize to get them right because the only way to get some of them right is is

**[39:50]** to form something which gets all of them right. >> So, you know, if there's only one answer uh then and you find it, I that's not called generalization. It's just it's the only way to solve it and so they

**[40:02]** find the only way to solve it. >> Generalization is when it could be this way, it could been that way and they do it the good way. My my understanding is that they um this is working more and more better and better with coding

**[40:14]** agents. So engineers obviously if you're trying to program a library there's many different ways you could achieve the endspec and an initial frustration with these models has been that they'll do it in a way that's

**[40:27]** sloppy and then over time they're getting better and better at coming up with the design architecture and the abstractions that developers find more satisfying. And it seems that an example of what you're talking about.

**[40:41]** >> Well, there's nothing in them which will cause it to generalize. Well, the gradient descent will cause them to find a solution to the problems they've seen. And if there's only one way to solve them, you know, they they'll do it. But

**[40:55]** there are many ways to solve it. Some which generalize well, some which generalize poorly. There's nothing in them in the algorithms that will cause them to generalize well. >> But people of course are involved. and

**[41:05]** and you know if if it's not working out you know they fiddle with it and until they find a way perhaps until they find a way which it generalizes well so to prep for this interview I wanted to understand the full history of RL

**[41:19]** starting with reinforce up to current techniques like GRPO and I didn't just want a list of equations and algorithms I wanted to really understand each change in this progression and the underlying motivation you know what was

**[41:32]** the main problem that each successive method was actually trying to solve. So I had Gemini Deep Research walk me through this entire timeline step by step. It explained the last 20 years of gradual innovation and explained how

**[41:44]** each step made the Aura learning process more stable or more sample efficient or more scalable. I asked Deep Research to put all of this together like an Andre Carpathy style tutorial and it did that. What was cool is that it combined this

**[41:57]** whole lesson together into one coherent cohesive document in the style that I wanted. It was also great that it assembled all of the best links in the same place so that if I wanted to understand any specific algorithm

**[42:08]** better, I could just access the right explainer right there. Go to gemini.google.com to try it out yourself. All right, back to Richard. I want to zoom out and ask about so being in the field of AI for

**[42:23]** longer than almost anybody who's commentating on it uh or working in it now. I'm just curious about what the biggest surprises have been. How much new stuff you feel like is coming out or does it feel like people are just

**[42:36]** playing with old ideas? Um zooming out you know you you got into this even before like deep learning was popular. So how do you see this trajectory of this field over time and how new ideas have come about and everything and

**[42:50]** what's been surprising? >> Okay so yeah I I I um thought a little bit about this. There are many things or a handful of things. Um first the large language models are surprising. It's surprising how how effective um neural

**[43:07]** networks artificial neural networks are at at language tasks. You know that that was a surprise. Wasn't expected. Language seemed different. So that's impressive. >> Um there's a longstanding controversy in

**[43:21]** AI about uh simple basic principle methods. uh the the general purpose methods like search and learning and compared to um human enabled systems uh like symbolic methods and um uh so in the old days it was interesting because

**[43:42]** things like search and learning were called weak methods because they're just they just use general principles. They're not using uh the power that comes from uh imbuing a system with human knowledge. So those are called

**[43:52]** strong and um and so I think the weak methods have just you know totally won that's you know that's that's that's the biggest um question from the old days of AI what would happen and you know yeah learning and search have just won the

**[44:12]** day >> right >> but there's a sense which that was not surprising to me because I was always voting for or hoping or rooting for the for the uh simple basic principles

**[44:21]** >> and so Even with the large language models, it's surprising how how well it worked, but it was all it was all good and gratifying. And um and things like Alph Go, it's it's sort of surprising how well that was able to work. Um and

**[44:36]** Alpha Zero in particular, how well it was able to work. Um but it's all very gratifying because again, it's simple basic principles are winning the day. Have there felt like whenever the public conception

**[44:50]** has been changed because some new technique was or sorry some new application was developed for example when Alpha Zero became this viral sensation to you as somebody who has literally came up with many of the

**[45:02]** techniques that were used. Did it feel to you like new breakthroughs were made or does it feel like oh we've had these techniques since the '90s and people are simply combining them and applying them now? So the whole alpho thing had a

**[45:16]** precursor which is TD gam Jerry Tasaro did exactly um reinforcement learning temporal difference learning methods to um to play back gam >> right >> and it beat the beat the world's best

**[45:31]** players and it worked really well and so in some sense Alpha Go was merely a scaling up of that process but it was quite a bit of scaling up and there was also an additional innovation in how the search was done,

**[45:45]** >> right? >> But it made sense. It wasn't surprising in that sense. Alph Go actually didn't use uh TD learning. It waited to see the final outcomes. Uh but Alpha Zero used TD uh and Alpha Zero was applied to all

**[46:01]** the other games and did extremely well. I was very I've always been very impressed by the way Alpha Zero plays chess because I'm a chess player and it just it it was just sacrifices material for sort of positional advantages and

**[46:15]** it's just just content and patient to uh sacrifice that material for a long period of time and um so that was surprising that it worked so well but also gratifying and fitting into my worldview. So, so this has led me where

**[46:32]** I am. Where I am is I'm in some sense a contrarian or some thinking differently from the field is and I'm I am personally just kind of content being out of sync with my field for a long period of time perhaps decades uh

**[46:47]** because occasionally I have been proved uh right in the past. And the other thing I do to help me not feel I'm I'm out of sync and thinking in a strange way is to look not at my my local uh environment or my local field, but to

**[47:05]** look back in in time into history and to see what people have thought classically about about um about the mind in many different fields. And I don't feel I'm out of sync with the larger traditions. >> I I really view myself as a classicist

**[47:19]** rather than as a contrarian. I go to what what the larger community of of thinkers about the mind have always thought. >> Okay. Some sort of left field questions for you if you'll tolerate them. Um so

**[47:33]** the way I read the bitter lesson is that it's not saying necessarily that human artisal researcher tuning doesn't work but that it obviously scales much worse than compute which is growing exponentially. And so you want

**[47:49]** techniques which leverage a ladder. >> Y >> and once we have AGI, we'll have researchers which scale linearly with compute, right? So we'll have this avalanche of millions of AI researchers

**[48:02]** and their stock will be growing as fast as uh compute. And so maybe this will mean that it is rational or it will make sense to have them doing good old-fashioned AI and doing these artisal solutions. uh does that as a vision of

**[48:19]** what happens after AGI in terms of how AI research will evolve. I wonder if that's still compatible with a better lesson. >> Well, how did we get to this AGI and you want to presume that it's been done?

**[48:30]** >> So, suppose it started with general math methods, but now we've got the AGI and now we want to go >> h >> we're done. >> Interesting. You don't think that

**[48:39]** there's any anything above AGI? >> Well, but you're using it to get AGI again. Well, I'm using it to get superhuman levels of intelligence or competence at different tasks.

**[48:50]** >> So, these AGIS, if they're not superhuman already, then the the knowledge they might impart would be not superhuman. >> I guess there's different gradations of your

**[49:02]** >> I'm not sure this this your idea makes sense because because it seems to presume the existence of AGI. Uh, and then that we've already worked that out. >> So, maybe one way to motivate this is Alpha Go was superhuman. um it beat any

**[49:16]** Go player. Alpha Zero would beat Alpha Go every single time. So there's ways to get more superhuman than than even superhuman >> and it was a different architecture. And so it seems plausible to me that

**[49:29]** >> well the agent that's like able to generally learn across all domains. There would be ways to make that give it better architecture for learning just the same Alpha Zero was an improvement upon Apple Go and Mu0ero was an

**[49:40]** improvement upon Alpha Zero. And the way alpha zero was an improvement was it did not use the human knowledge but just went from experience. >> Right. >> So why do you why do you say

**[49:52]** >> but >> bring in other agents expertise to teach it when it's when it's been it's worked so well from experience and not by help from another agent. I agree that in that particular case that

**[50:07]** it was moving to more general methods, but I meant to use that example to illustrate that it's possible to go superhuman to superhuman plus+ to superhuman++. >> Yeah.

**[50:16]** >> And I'm curious if you think those gradations will continue to happen by just making the method simpler or because we'll have the capability of these millions of minds who can then add complexity as needed. if that will

**[50:29]** continue to if that will continue to be a false path even when you have billions of AI researchers or trillions of AI researchers. >> I think I think more interesting is just think about that case

**[50:39]** >> which when you have many AIs um will they help each other the way cultural evolution works in people >> and let's just maybe we should talk about that. >> Yeah, for sure.

**[50:50]** >> The bitter lesson. Oh, who cares about that? That's that's an empirical observation about a particular period in history. 70 years in history no longer doesn't necessarily have to apply the next 70 years. So the interesting

**[51:02]** question is you're an AI, you get some more computer power. Should you use it to make yourself, you know, more computationally capable or should you use it to spawn off a copy of yourself to go learn something interesting on the

**[51:13]** other side of the planet or on some other topic and then report back to you? >> Yep. I think that's a really interesting question um that that that will only arise in the

**[51:24]** age of digital intelligences. >> I'm not sure what the answer is, but I think it it will more questions. Will it be possible to really, you know, spawn it off, send it out, learn something new, some perhaps very new, and then

**[51:37]** will it be able to re be reinccorporated into the original >> or will it will it uh have will have changed so much that it uh it can't really be done, you know? Is that possible or is it not? And you know, you

**[51:50]** can carry this to its limit as I I I saw one of your videos the other night that that suggested that it that it could where you spawn off many many copies, do different things. It's highly decentralized, but report back to the

**[52:01]** the central master and that this is this will be such a powerful thing. Well, I think one thing that uh so this is my attempt to add something to this this view is that uh a big question, a big issue will become uh

**[52:17]** corruption. You know, if you if you really could just get information from anywhere and bring it into your central mind, you become more and more powerful. Uh, and since it's all digital and they all speak some internal digital

**[52:30]** language, maybe it'll be easy and possible. But it will not be that easy, as easy as you're imagining because uh that you can lose your mind this way. If you you pull in something from the outside and build it into your into your

**[52:44]** inner thinking, uh, it could take over you. It could change you. It could be uh your destruction rather than uh your in increment in knowledge. M >> I think this will become a a big concern, you know, particularly when

**[52:59]** you're, oh, he's figured all about, you know, how to play some new game or figures out he's studied Indonesia and you want to incorporate that into your mind. Um, yeah. So, you can't you could you think, oh, just read it all in and

**[53:12]** that'll be fine. But no, you've just read a whole bunch of bits into your mind and uh they could have viruses in them. They could have hidden goals. uh they can uh warp you and change you and this will become a big thing. How do you

**[53:28]** have cyber security in the age of digital spawning and re reforming again? >> It's interesting that both quant firms and AI labs have a culture of secrecy because both of them are operating in incredibly competitive markets and their

**[53:42]** success rest on protecting their IP. If you're an AI researcher or engineer and you're deciding where to work, most of the quant firms or AI labs that you'll be considering will be strongly siloing their teams to minimize the risk of

**[53:54]** leaks. Hudson River Trading takes the opposite approach. Their teams openly share their trading strategies and their strategy code lives in a shared monor repo. At HRT, if you're a researcher and you have a good idea, your contribution

**[54:07]** will be broadly deployed across all relevant strategies. This gives your work a ton of leverage. You'll also learn incredibly fast. You can learn about other people's research and ask questions and you can see how everything

**[54:19]** fits together end to end from the low-level execution of trades to the high level predictive models. HRT is hiring. If you want to learn more, go to hudson rivertrading.com/thearkcash. All right, back to Richard. I guess this

**[54:36]** brings us to the topic of AI succession. >> Mhm. you have a perspective that's quite different from a lot of people that I've interviewed and maybe a lot of people generally. So I also think it's a very interesting perspective. I want to hear

**[54:47]** about it. >> Yeah. So I do think succession to digital or digital intelligence or augmented humans is inevitable. So the argument go I have a four-part argument. Now I step

**[55:02]** one is there's no government or organization that that uh gives humanity a unified point of view that dominates and that can that can arrange. There's no consensus about how the world should be

**[55:18]** run. And number two um we will figure out how intelligence works. Researchers will figure it out eventually. And number three we won't stop just with human level intelligence. we will get reach super intelligence. And number

**[55:32]** four is that once it's inevitable over time that the most intelligent things around would gain resources and power. Uh and uh so put all that together, it's you know you um it's sort of inevitable that you're going to have um succession

**[55:53]** to AI or to AI enabled augmented humans. So within those those four things seem clear and and and sure to happen. Uh but within that set of possibilities some there can be good outcomes as well as less good outcomes bad outcomes

**[56:11]** >> and um so I just just trying to be realistic about where we are and and ask how we should feel about it. Yeah, I I agree with all four of those arguments and the implication and I also agree that

**[56:27]** succession contains a wide variety of possible futures. So, curious to get more thoughts on that. >> Right. And so then I do encourage people to think um positively about it first of

**[56:40]** all because it's something we humans have always tried to do for thousands of years trying to understand themselves trying to make themselves think better and um you know just understand themselves. So

**[56:52]** this is a great success from as science humanities uh we're finding out what this essential part of of of humanness is what it means to be intelligent. And then what I usually say is is that this is all kind of human centric. What if we

**[57:11]** look we step aside from being a human and just say take the point of view of the universe and and this is I think a major stage in the universe a major transition a transition from replicators we humans and animals plants we're all

**[57:27]** replicators and that gives some strengths and some limitations and then we're entering the age of design where because our AIs are designed our our our all of our physical objects are designed our buildings are designed

**[57:40]** our technology is designed and we're we're designing now uh AIs things that can be intelligent themselves and that are themselves capable of design and so this is this is a key step in the world and I and in the universe and I think

**[57:56]** it's the it's the transition from the world in which most of the interesting things uh that are are replicated replicated means you can make copies of them uh but you don't really understand them like

**[58:09]** right now we make more intelligent beings, more children. Uh we don't really understand how intelligence works. Whereas in as we're we're reaching now to having design intelligence intelligence that we do

**[58:21]** understand how it works and therefore we can change it in different ways in different speeds um than otherwise and and our future they might not be replicated at all like we may just design AIs and those AIs will design

**[58:36]** other AIs and um everything will be done by design construction rather than by replication. Yeah, I mark this as one of the four great stages of the universe. First there's there's dust ends with stars.

**[58:50]** Stars we and and then stars make planets and the planets give rise to life. And now we're giving life life to uh designed entities. And so I think we should be proud and we should be uh uh that we are giving rise

**[59:07]** to this great transition in the universe. Yeah. So it's an interesting thing. What should we what should we consider them part of humanity or different from humanity? It's our choice. It's our

**[59:19]** choice whether we should say oh they are our offspring and we should be proud of them and we should celebrate their achievements or we should we could say oh no they're not us and we should be horrified. It's it's just it's

**[59:30]** interesting that that that is it feels to me like a choice and yet it's such a strongly uh held thing that how could we be a choice? I like these sort of contradictory uh implications of thought.

**[59:42]** >> It would be interesting to consider if we were just designing another generation of humans. >> Yes, >> design is the wrong word. But we knew a future generation was a good humans

**[59:51]** going to come up and forget about AI. We just know in the long run humanity will be more capable and maybe more numerous, maybe more intelligent. How do we feel about that? I do think there's potential worlds with future humans that we would

**[1:00:05]** be quite concerned about. So are you thinking like maybe we are we are like the Neanderthalss we give rise to Homo sapiens maybe homo sapiens will give rise to a new group of people >> something like that like I'm basically

**[1:00:18]** taking the example you're giving of like okay even if you consider them part of humanity yeah >> I don't think that re necessarily means that we should feel super comfortable >> yeah like Nazis were humans right if we

**[1:00:31]** thought like oh the future generation will be Nazis I think we'd be like quite concerned about just handing off power to them So, um, I agree that this is not super dissimilar to worrying about more capable future humans, but I don't think

**[1:00:45]** that that addresses a lot of the concerns people might have about this level of power being attained this fast with entities we don't fully understand. >> Well, I think it's relevant to point out that uh for most of humanity

**[1:01:00]** um they don't have much uh influence on what happens. Um, most of humanity doesn't influence >> who can control the atom bombs or who uh controls the nation states. Even as a as a citizen, I often feel that we don't

**[1:01:21]** control the nation states very much. They're out of control. A lot of it has to do with just how you feel about change. Um, and if you think the current situation is really really good, then you're uh more likely to be suspicious

**[1:01:35]** of change and averse to change than if you think um it's imperfect. And I think it's imperfect. In fact, I think it's pretty bad. >> So, I'm I'm I'm open to change. I I

**[1:01:49]** think humanity is not in a has had a good super good track record. And maybe it's the best thing that there's been, but it it it's far from perfect. >> Yeah, I guess there's different varieties of change. Um, the industrial

**[1:02:04]** revolution was change. The bullshik revolution was also change. And if you were around in Russia in the 1900s and you're like, look, things aren't going well. This is our is kind of messing things up. We need change. I'd want to

**[1:02:18]** know what kind of change you wanted before signing on the dotted line. Right? And then similar with AI where I'd want to understand and to the extent it's possible to change the trajectory to change the trajectory of AI such that

**[1:02:30]** the change is positive um for humans. >> We we are we should be concerned about our future the future make we should try to make it good. Um, we al also though should recognize the limits, our limits. And we're

**[1:02:50]** I think we want to avoid the feeling of entitlement. Avoid the feeling, oh, we are here first. We should always have it in a good way. Um, how should we think about the future and how much control uh a particular species on a particular

**[1:03:05]** planet should have over it? Uh, and how much control do we have? You know, a a counterbalance to our limited control over the long-term future of humanity should be how much control do we have over our own lives? Like we have uh our

**[1:03:22]** own goals and we have our our families and we those things are much more controllable than like trying to control um the whole universe, >> right? Um so I think it's appropriate you know for us to to uh you know really

**[1:03:40]** work towards our own local goals and uh and it's kind of aggressive for us saying oh the future has to evolve this way that I want it to. >> Sure. >> Because then we'll have arguments like

**[1:03:52]** different people think the future the global future should evolve in different ways and then they have conflict and >> yeah avoid that. Maybe a bit a good analogy here would be okay so suppose you're raising your own children

**[1:04:06]** >> it might not be appropriate to have extremely tight goals for their own life or also have some sense of like I want my children to go out there in the world and have this specific impact you know my my son's going to become president

**[1:04:18]** and my daughter's going to become CEO of Intel and like together they're going to have this effect on the world um but it people do have the sense and I think this is appropriate of saying, "I'm going to give them good, robust values

**[1:04:32]** such that if and when they do end up in positions of power, they do reasonable pro-social things." And I think maybe a similar attitude towards AI makes sense. Not in the sense of we can predict everything that they will do. Um where

**[1:04:46]** we have this plan about what the world should look like in 100 years but it's quite important to give them robust and steerable and pro-social values. >> Pro-social values.

**[1:05:00]** >> Maybe that's the wrong word. >> Are there universal values that we can all agree on? >> I don't think so. But that doesn't prevent us from uh giving our kids a good education, right? Like we have some

**[1:05:12]** sense of we want our children to be a certain way. >> Yeah. >> And maybe process is the wrong word. Actually, high integrity is a maybe a better word where if there's a request

**[1:05:20]** or if there's a goal that seems harmful, they will refuse to engage in it. Um or they'll be honest. Um things like that. and we have some sense that we can teach our children things like this even if we don't have some sense of what true

**[1:05:35]** morality is or everybody doesn't agree on that. Um, and maybe that's a reasonable target for AI as well. >> So, so you're saying we're trying to design the future and the the principles by which it will evolve and come into

**[1:05:48]** being, >> right? >> And so you're saying the first thing you're saying is well we will we try to teach our our children um general principles which will promote

**[1:05:58]** more likely evolutions. >> Yeah. >> Um maybe we should also seek for things being voluntary. If there is change, we want it to be voluntary rather than imposed on people.

**[1:06:09]** >> I think that's a very important point. >> Y >> um and yeah, that's all good. I think I think this is like a big um you know, the big the big or one of the really big human enterprises to design society and

**[1:06:24]** that's been ongoing for for thousands of years again. And so so it's like the more things change really the more things they stay the same. We still have to figure out how to be uh the children will still come up with different values

**[1:06:36]** that seem strange to their parents and their grandparents and uh and things will evolve. the the more things change, the more they stay the same. Also seems like a good capstone to the AI discussion because the AI discussion we

**[1:06:49]** were having was about how techniques which were um invented even before their application to deep learning and back propagation was evident have are you know central to the progression of AI today. So maybe that's a good place to

**[1:07:03]** wrap up the conversation. >> Okay, thank you very much. >> Thank you for coming on. >> My pleasure.
