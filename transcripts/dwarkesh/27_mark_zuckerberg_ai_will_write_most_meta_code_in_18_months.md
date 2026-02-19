---
layout: default
type: transcript
series: dwarkesh
episode: 0
guest: ""
title: "Mark Zuckerberg — AI will write most Meta code in 18 months"
source_url: "https://www.youtube.com/watch?v=rYXeQbTuVl0"
analysis_url: /transcripts/dwarkesh/27_mark_zuckerberg_ai_will_write_most_meta_code_in_18_months.analysis/
permalink: /transcripts/dwarkesh/27_mark_zuckerberg_ai_will_write_most_meta_code_in_18_months/
---

# Transcript: Mark Zuckerberg — AI will write most Meta code in 18 months

Source: https://www.youtube.com/watch?v=rYXeQbTuVl0

---

**[00:00]** I would guess that the world is going to get a lot more like a lot funnier and like weirder if you think that something someone is doing is bad and they think it's really valuable. Most of the time in my experience they're right and

**[00:11]** you're wrong. I am worried that we're just removing all the friction between getting totally reward hacked by our technology. We're trying to build a coding agent that advances llama research. I would guess that like

**[00:24]** sometime in the next 12 to 18 months we'll reach the point where like most of the code that's going towards these efforts is written by AI. I tend to think that for at least the foreseeable future this is going to lead towards

**[00:35]** more demand for people doing work not less. If you've gotten the cost of providing that service down to onetenth of what it would have otherwise been maybe now that actually makes sense to go do.

**[00:46]** All right Mark thanks for coming on the podcast again. Yeah, happy to do it. Good to see you. You too. Last time you were here, um, you had launched Llama 3. Yeah. Now you've launched Llama 4. Well, the first version. That's right. What's

**[00:58]** new? What's exciting? What's changed? Oh, well, I mean, the whole field's so dynamic. So, I mean, I feel like a ton has changed since the last time that we talked. Um, Meta AI has almost a billion people using it now monthly. So, that's

**[01:11]** um that's pretty wild. Um, and you know, I think that this is going to be a really big year on all of this because, um, especially once you start getting the personalization loop going, um, which we're just starting to build in

**[01:23]** now really, um, from both the context that all the algorithms have about what you're interested in feed and all your profile information, all the social graph information, but also just what you're interacting with the AI about, I

**[01:35]** think that's just going to be kind of the next thing that's um, that's going to be super exciting. So really big on that. The modeling stuff continues to make really impressive advances too as as you know. Um the Llama 4 stuff, I I'm

**[01:50]** pretty happy with the first set of releases. You know, we announced the um we announced four models and we released the first two, the Scout and Maverick ones, which are kind of like the midsize models, midsize to small. Um it's not

**[02:03]** like you actually the most popular Llama 3 model was um was the the 8 billion parameter model. So we're we we've got one of those coming in the llama 4 series 2. Um our internal code name for it is little llama. But um but that

**[02:19]** that's that's that's coming probably you know over the over the next over the coming months. But the um the scout and maverick ones um and I mean they're good. They're there's some of the highest intelligence per cost that you

**[02:32]** can get of any model that's out there. Natively multimodal, very efficient, run on one host, um designed to just be very efficient and low latency for a lot of the use cases that we're building for internally. And you know, that's our all

**[02:48]** thing. We we basically build what we're what we want and then we open source it so other people can use it too. So I'm excited about that. Um I'm also excited about the behemoth model which is is coming up. Um that's going to be our

**[03:01]** first model that is uh sort of at the frontier. I mean it's like more than two trillion parameters. So it is I mean it's you know as as the name says it's it's quite quite big. Um so we're kind of trying to figure out how

**[03:16]** we make that useful for people. It's so big that we've had to build a bunch of infrastructure um just to be able to post train it ourselves. And we're kind of trying to wrap our head around how does the like the average developer out

**[03:27]** there, how are they going to be able to use something like this and how do we make it so it can be useful for um distilling into models that are of reasonable size to run because you're you're obviously not going to want to

**[03:35]** run um you know something like that in a consumer model. But um but yeah, I mean it's there there's a lot to go. I mean as you saw with the with the Llama 3 stuff last year, the initial Llama 3 launch was um was exciting and then we

**[03:49]** just kind of built on that over the year. 3.1 was when we released the 405 billion model. 3.2 was when we got all the multimodal stuff in. Um so we basically have a road map like that for this year too. So lot going on. I'm

**[04:01]** interested to hear more about it. uh there's this impression that the gap between the best closed source and the best open source models has increased over the last year where I know the full family of llama 4 models isn't out yet

**[04:13]** but um llama for Maverick is 35 on uh Chabat Arena and then on a bunch of major benchmarks it seems like 04 mini or GP Gemini 2.5 flash are um beating Maverick which is in the same class. What do you make of that impression?

**[04:27]** Yeah, well okay there there's a few things. I actually think that this has been a very good year for open source overall. Right? If you go back to the like where we were last year, um what we were doing with Llama was like the only

**[04:39]** real um super innovative open- source model. Now you have a bunch of them in the field. And I think in general the prediction that this would be the year where open- source um generally overtakes closed sources, the most used

**[04:52]** model models out there um I think is is generally on track to be true. I think the thing that's been um sort of a an interesting surprise, I think positive in in some ways, negative in others, but but I think overall good, is that it's

**[05:05]** not just llama. There there are a lot of good ones out there. Um so I think that that's quite good. Um then there's the reasoning phenomenon which which you basically are are are alluding to with talking about 03 and 04 and and and some

**[05:19]** of the other models. And I do think that there is this specialization that is um that's happening where if you want a model that is sort of the best at math problems or coding or different things like that. Um I I do think that these

**[05:34]** reasoning models with um a lot of uh the ability to just consume more test time or inference time compute um in order to provide more intelligence is a really compelling paradigm. But for a lot of the applications that and and we're

**[05:50]** going to do that too. We're building a llama for reasoning model and that that'll come out at at some point. Um for a lot of the things that we care about um latency and good intelligence per

**[06:03]** cost are actually much more important product attributes. um if you're if you're primarily designing for you know a consumer product u people don't necessarily want it to wait like half a minute to go think through the answer.

**[06:19]** If you can provide an answer that's generally quite good too in like half a second then that's great and that's a good trade-off. So I think that both of these are going to end up being important directions. Um I I am

**[06:31]** optimistic about integrating the reasoning models with um kind of the the core language models over time. And I think that's sort of the direction that um Google has gone in with um with some of the more recent um Gemini models. And

**[06:43]** I think that that that's really promising. But um but I think that there's just going to be a bunch of different stuff that goes on. Um you also mentioned the whole um chatbot arena thing which I think is interesting

**[06:53]** and it goes to this challenge around how do you do the benchmarking, right? And and basically how do you know what models are good for which things? And one of the things that we've generally tried to do over the last year is anchor

**[07:07]** more of our models in um our meta product northstar use cases because the the the issue with both kind of open- source benchmarks and you know any given thing like like the um LM arena stuff is it's just it's they're often skewed for

**[07:24]** a either a very specific um set of use cases which are often not actually what any normal person does and in in your product. Um they are often weighted um kind of the portfolio of things that they're trying to measure is different

**[07:40]** uh from what people care about in any given pro um product. And um because of that, we've found that trying to optimize too much for that stuff has often um led us astray and actually not led towards the highest quality products

**[07:57]** and the most usage and best feedback within meta as people use our stuff. So, we're trying to anchor our northstar in um in basically the product value that that people um kind of report to us and what they say that they want and what

**[08:14]** their revealed preferences are and using um the experiences that that that we have. So, sometimes I think um you sometimes these things just don't quite line up and and I think that a lot of them are are quite easily um gameable,

**[08:27]** right? So, I mean, I think on on the um arena, you'll see stuff like uh like Sonnet 37. It's like a great model, right? And it's it's like not near the top. Um and it was relatively easy for our team to tune a version of Llama 4

**[08:40]** Maverick um that basically was way at the top. Um whereas the one that we released that's the the kind of the pure model actually has no tuning for that at all. So, it so it's further down. I I I think you just need to be careful with

**[08:53]** with with some of the benchmarks and and we're going to we're going to index primarily on the products. Is do you feel like there is some benchmark which captures what you see as a northstar of value to the user which can be sort of

**[09:05]** objectively measured between their different models and you're like I I I need Llama 4 to come out on top on this. Well, I mean our benchmark is basically um user value in metai, right? So it's but you can't compare other models. Um

**[09:18]** um well we might be able to because we might be able to run other models in that and and be able to tell and I think that that's one of the advantages of open source is basically you have a good community of folks who can like poke

**[09:28]** holes at okay where is your model not not good and where where is it good. Um but I think the reality at this point is that all these models are optimized for slightly different mixes of things. I mean everyone is trying to I think go

**[09:42]** towards the same um you know I think all the leading labs are trying to create general intelligence right and um super intelligence whatever you call it right like basically AI that can lead towards a world of abundance where like everyone

**[09:54]** has these superhuman tools to create whatever they want and that leads to just dramatically empowering people and creating all these economic benefits. I think that that's sort of however you define that, I think that that's kind of

**[10:05]** what what a lot of the labs are are going for. And um but there's no doubt that different folks have sort of optimized towards different things. I think the anthropic folks have really focused on kind of coding and and agents

**[10:18]** around that. You know, the OpenAI folks, I think, have gone a little more towards reasoning um recently. And I think that there is a space which if I had to guess I think will end up probably being the most used one which um which is quick is

**[10:37]** very natural to interact with um is very natively multimodal um that fits into kind of throughout your day the ways that you want to interact with it. Um, and I think you got a chance to play around with um with uh the new Meta AI

**[10:51]** app that we're that we're releasing. And you know, one of the fun things that we put in there is the um the demo for the full duplex voice. And it's I mean, it's early, right? I mean, it's not um you know, there's a reason why we haven't

**[11:02]** made that the default voice model in the app, but there's something about how naturally conversational it is that I think is just like really fun and compelling and and I I think being able to mix kind of that in

**[11:15]** um with the right personalization is is going to lead towards a product experience where, you know, I I would basically just guess that you go forward a few years, like we're just going to be talking to AI

**[11:26]** throughout the day about different things that we're wondering and um You know, it's like you'll um you'll you'll have your phone, you'll talk you'll talk to on your phone, you'll talk to it while you're browsing your feed apps.

**[11:35]** It'll give you context about different stuff. You'll be able to answer questions. It'll help you as you're interacting with people in messaging apps. Um you know, eventually I think we'll we'll walk through our our daily

**[11:44]** lives and we'll either have glasses or um you know, other kinds of AI devices and and just be able to kind of seamlessly interact with it all day long. So I I think that that is that's kind of the north star and whatever the

**[12:00]** benchmarks are that lead towards people feeling like the the quality is like that's what they want to interact with that I think is actually the thing that is ultimately going to matter the most to us. I got a chance to play around

**[12:12]** with both and also the meta app and the voice mode was super smooth. It was quite impressive. I on the point of what the different labs are optimizing for to steelman their view. I think a lot of them think that once you fully automate

**[12:26]** software engineering and AI research then you can kick off an intelligence explosion where you have millions of copies of these software engineers replicating the research that happened between Llama 1 and Llama 4. That scale

**[12:39]** of improvement again in the matter of weeks or months rather than years. Um, and so it really matters to just have close the loop on the software engineer and then you can h be the first to ASI. What do you make of that? Well, well, I

**[12:50]** mean I I personally think that's pretty compelling. Um, and and that's why we have a big coding effort, too. I we're working on um a number of coding agents inside Meta. Um, you know, because we're not really a um an enterprise software

**[13:05]** company. We're primarily building it for ourselves. So, so again, you know, we we go kind of like for for um you know, the specific goal. We're not trying to build a general developer tool. We are trying to build a coding agent and an AI

**[13:19]** research agent that um that basically advances Llama research specifically and um and it's like just fully kind of plugged into our tool chain and all this. So I I think that that's important and um and I think is going to end up

**[13:35]** being an important part of how this stuff gets done. I would guess that like sometime in the next 12 to 18 months um will reach the point where like most of the code that's going towards these efforts is written by AI and I don't

**[13:49]** mean like autocomplete. I mean right today you have like you have kind of you know good autocomplete like you start writing something that can complete the the kind of section of code. I'm talking more like you give it a goal, it can run

**[14:01]** tests, right? It can it can kind of improve things. Um, it can find issues. Um, it writes higher quality code than like the the average very good person on on the team already. Um, and and like I think that that's going to be a really

**[14:19]** important part of this for sure. But I don't know if that's the whole game. I mean, I think that that's that I think is going to be a big industry. Um, and I think that that's going to be um, an important part of how AI gets developed.

**[14:31]** But I think that there are still guys I I think I mean, look, I guess one one way to think about this is this is a massive space, right? So I don't think that there's just going to be like one company with one optimization function

**[14:43]** that serves everyone as best as possible. I think that there are a bunch of different labs that are going to be doing leading work towards different domains. Some are going to be more kind of enterprise focused or coding focused.

**[14:53]** Some are going to be um more productivity focused. Some are going to be more social or entertainment focused. Um within the assistant space, I think there are going to be some that are much more kind of informational or

**[15:04]** productivity, some are going to be more companion focused. Um it's going to be a lot of the stuff that's just like fun and entertaining and like shows up in your feed. Um and I think that that's so I think that there's just like a huge

**[15:15]** amount of space. And part of what's fun about this is like it's like going towards this AGI future. there are a bunch of common threads for what needs to get invented, but there are a lot of things at the end of the day that need

**[15:27]** to get created. And I I think that that's um I think you'll start to see a little more specialization between the groups if I had to guess. It's it's really interesting to me that you basically agree with the premise that

**[15:39]** there will be an intelligence explosion and something like super intelligence on the other end. But then if that's the case, but don't tell me I'm misunderstanding you. If that's the case, why even bother with personal

**[15:48]** assistance and whatever? Why not just get get to superhuman intelligence first and then deal with everything else? I think that that's just one aspect of the flywheel, right? So part of what what I generally disagree with on the fast

**[16:00]** takeoff thing is it takes time to build out physical infrastructure, right? So if you want to build like a gigawatt cluster of compute, that just is going to take some time, right? But it like takes Nvidia a bunch of time to like

**[16:15]** stabilize their new generation of of of the systems and then you need to figure out the networking around it and then you need to like build the building. You need to get permitting and you need to get the energy and then like okay you

**[16:28]** want like some whether it's gas turbines or um or green energy you need to like there's a whole supply chain of that stuff. So I think that there's like a lot of and we talked about this a bunch on the last time that I was that I was

**[16:39]** on the the podcast with you and I think some of these are just like physical world human time things that as you start getting more intelligence in one part of the stack um you'll basically just run into a

**[16:53]** different set of bottlenecks. I mean that's sort of the way that engineering always works. It's like you solve one bottleneck, you get another bottleneck. Yeah. Um, another bottleneck in the system or another ingredient that's

**[17:03]** going to make this like work well is basically people getting used to and learning and having a a feedback loop with um with using the system. So, I don't think like like these systems don't tend

**[17:20]** to be the type of thing where like something just shows up fully formed and then people magically fully know how to use it. Um, and that's the end. I think that there is this co-evolution that happens where people

**[17:36]** are learning how to best use these AI assistants. on the same side, the AI assistants are learning what those people care about and the developers of those AI assistants are able to make the the kind of AI assistants better. Um,

**[17:50]** and then you're also building up this base of context. So now you wake up and you're like a year or two into it and now the AI assistant can reference things that you talked about a couple years ago and like that's pretty cool,

**[18:01]** but you couldn't do that if it just you just launched the perfect thing on day one. There's no way that it could reference what you talked about two years ago if it didn't exist two years ago. So um so I guess my view is like

**[18:11]** there's this huge intelligence growth. Mhm. There's a a very rapid curve on the uptake of people interacting with the AI assistants and like the learning feedback and and kind of data flywheel around that. Um and then there

**[18:28]** is also the buildout of the supply chains and infrastructure and regulatory frameworks to enable the scaling of a lot of the physical infrastructure. But I think at some level all of those are going to be

**[18:42]** necessary and not just the coding piece. M um I guess one one specific example of this that I think is interesting actually even if you go back a few years ago we had a project on I think it was on our ads team to

**[18:57]** automate ranking experiments right that's like a pretty constrained environment it's not like write open-ended code it's basically look at the whole history of the company every experiment that any engineer has ever

**[19:09]** done in the ad system and look at what worked what didn't what the results of those and basically formulate new hypotheses for different tests that we should run that could improve the the

**[19:22]** performance of the ad system. And what we basically found was um we were bottlenecked on compute to run tests uh based on the number of hypotheses. It turns out even with just the the humans that we have right now um on the ads

**[19:37]** team, we already have more good ideas to test than you actually have either kind of compute or really cohorts of people to test them with, right? Because I mean even if you have like three and a half billion people using your products, you

**[19:54]** still want each, you know, each test needs to be statistically significant. So it needs to have, you know, some number of whatever it is, hundreds of thousands or millions of people. and um and there only there's some there's kind

**[20:06]** of only so much throughput that you can get on testing through that. So we're already at the point even with just like the people we have that um that we already can't really test everything that we want. Um so now just

**[20:21]** being able to test more things is not necessarily going to be additive to that. We need to get to the point where the average quality of the hypotheses that the AI is generating is better than what the all the things above the line

**[20:33]** that we're actually able to test that like sort of the best humans on the team have been able to do before it'll even be marginally useful for it. So I I think that there's like it we'll get there. We'll get there I think pretty

**[20:44]** quickly. But um but it's not like okay cool the thing can write code all of a sudden everything is just improving massively. There there are like these real world constraints that um that that basically it needs to first it needs to

**[20:57]** be able to kind of do a reasonable job then it needs to um be able to you need to have the compute and the the kind of people to test and and then over time as the quality creeps up I don't know are we here in like five or 10 years and

**[21:09]** it's like no set of people can generate a hypothesis as good as the AI system I don't know maybe right it's then I think in that world obviously that's that's going to be how all the value is created but but That's not the first step.

**[21:22]** Publicly available data is running out. So major AI labs like Meta, Google Deep Mind, and OpenAI all partner with Scale to push the boundaries of what's possible. Through Scales data foundry, major labs get access to highquality

**[21:34]** data to fuel post training, including advanced reasoning capabilities. Scale's research team, Seal, is creating the foundations for integrating advanced AI into society through practical AI safety frameworks and public leaderboards

**[21:47]** around safety and alignment. Their latest leaderboards include humanity's last exam, Enigma, Eval, Multi- Challenge, and Vista, which test a range of capabilities from expert level reasoning to multimodal puzzle solving

**[22:01]** to performance on multi-turn conversations. Scale also just released scale evaluation, which helps diagnose model limitations. Leading frontier model developers rely on scale evaluation to improve the reasoning

**[22:13]** capabilities of their best models. If you're an AI researcher or engineer and you want to learn more about how scales data foundry and research lab can help you go beyond the current frontier of capabilities, go to

**[22:26]** scale.com/thwarkcash. So if you buy this view that um this is where intelligence is headed, the reason to be bullish on meta is obviously that you have all this distribution and which you can also use to learn more things

**[22:42]** that can be useful for training with the you mentioned the meta app is now has a um billion active users. Not the app, not the app. The app is is a is a standalone thing that we're just launching now. Um it'll I think it's fun

**[22:53]** for people who want to use it. It's a cool experience. We could talk about that for we we're we're kind of experimenting with some new ideas in there that I think are are are novel and worth talking through but I'm talking

**[23:03]** mostly about our apps. Meta AI is actually most used in WhatsApp. Got it. So it's um and WhatsApp is mostly used outside of the US. We we just passed like 100 million people in the US but it's not the primary messaging system in

**[23:15]** the US iMessage. So, um, so I think people in the US probably tend to underestimate the meta AI use, um, somewhat, but it's also part of the reason why the standalone app is going to be so important is the US is, you

**[23:29]** know, for a lot of reasons, one of the the the most important country and like and you know, the fact that WhatsApp is the main way that people are using Met AI and that's not the main messaging system in the US means that we need a

**[23:40]** another um, way to to kind of build a first class experience that's in front of people. And I I guess uh to finish the question, the bearish case would be that if the future of AI is less about just answering your questions and more

**[23:53]** so just being a virtual co-orker, it's not clear how meta AI instead inside of WhatsApp gives you the relevant training data to make, you know, like a fully autonomous programmer remote worker. So um yeah, in that case, does it not

**[24:10]** matter that much who has more distribution right now with LLMs? Well, again, I just think that there are going to be different things, right? It's like if you were s sitting at the beginning of the kind of the development of the

**[24:20]** internet and it's like, well, what's going to be the main internet thing, is it going to be knowledge work or is it going to be like massive consumer apps? It's like, I don't know, you get both, right? It's like you don't have to

**[24:31]** choose one, right? And now the world is big and complicated and does one company build all that stuff? I think normally the answer is no. Um but um but yeah no to to your question I people do not code in WhatsApp for the most part and I

**[24:47]** don't foresee that that's going to be like that people starting to write code in WhatsApp is going to be like a major major use case although I do think that people are going to ask AI to do a lot of things that result in the AI coding

**[24:57]** without them necessarily knowing it. Um so that that's a that's a separate thing but um but we do have a lot of people who are writing code at Meta and they use Meta AI. We we have this internal thing that we call Metamate and and

**[25:10]** basically in and a number of different um coding and AI research agents that we're building around that and that has you know quite its own feedback loop and I think can get good for accelerating those efforts. But again I just think

**[25:24]** that there are going to be a bunch of things. I think AI is almost certainly going to unlock this massive um you know revolution in knowledge work and code. Um, I also think it's going to be kind of the next generation of search and how

**[25:38]** people get information um and do more complex information tasks. Um, I also think it's going to be fun. I think people are going to use it to be entertained. Um, and um, and you know, a lot of the internet is like memes and

**[25:54]** humor, right? Right? And we have this like amazing technology at our fingertips. And it is sort of amazing and kind of funny when you think about it how much of human energy just goes towards entertaining ourselves and

**[26:04]** design and pushing culture forward and finding humorous ways to explain cultural phenomenon that we observe and um I think that that's almost certainly going to be the case in the future. Right? If you look at like the evolution

**[26:17]** of things like Instagram and Facebook, you know, if you go back 10, 15, 20 years ago, right? It was like text. Then then we all got phones with cameras. Most of the content became photos. Then the mobile networks got

**[26:31]** good enough that you you know if you wanted to watch a video on your phone, it wasn't just like buffering. So that got good. So over the last like 10 years, um most of the content has moved, you know, basically towards video at

**[26:41]** this point. Most of the time spent in Facebook and Instagram is video. But like I don't know, do you think in 5 years we're just going to be like sitting in our feed and consuming media that's video? It's like, no, it's going

**[26:52]** to be interactive, right? It's like you'll be scrolling through your feed and there will be content that is um is basically I don't know, maybe it looks like a real to start, but then like you talk to it or you interact with it and

**[27:03]** it talks back or it changes what it's doing or you can jump into it like a game and interact with it and that's all going to be like AI, right? So, um so I guess my point is there's just all these different things and um and I guess

**[27:15]** we're we're we're ambitious so we're working on a bunch of them. Um, but I don't think anyone company is going to do all of it. Okay. So, on this point of AI generated content or AI interactions, already people have meaningful

**[27:28]** relationships with AI therapists, AI friends, you know, maybe more. Um, and this is just going to get more intense as these AIs become more unique and more personable, more intelligent, more spontaneous and funny and so forth. How

**[27:42]** do we make sure people are going to have relationships with AI? How do we make sure that these are healthy relationships? Well, I think there are a lot of questions that you only really can answer as you start seeing the

**[27:53]** behaviors. So, probably the most important upfront thing is just like ask that question and care about it at each step along the way. But, but I think also being too prescriptive upfront and saying we think these things are not

**[28:04]** good. Um, often cuts off value, right? Because I don't know people use stuff that's valuable for them. I I one of my core guiding principles in designing products is like people are smart, right? They know what is valuable in

**[28:19]** their lives. Um you know every once in a while um you know something can something bad happens in a product and you want to make sure that you design your products well um to to minimize that. But if if if you think that

**[28:31]** something someone is doing is bad and they think it's really valuable, most of the time in my experience they're right and you're wrong and you just haven't come up with the framework yet for understanding why the thing that you're

**[28:43]** doing is is valuable and helpful in their life. Um yeah, so so that's kind of the main way that that I that I think about it. I do think that people are going to use um AI for a lot of these social tasks already. One of the main

**[28:57]** things that we see people using met AI for is kind of talking through difficult conversations that they need to have with um with people in their life. It's like okay my you know my my I'm having this issue with my girlfriend or

**[29:10]** whatever like help me have this conversation or like I need to have this hard conversation with my boss at work like how do I have that conversation? Um that's pretty helpful. And then I think as the personalization loop kicks in and

**[29:22]** the AI just starts to get to know you better and better um I think that will just be really compelling. Um you know one thing just from working on social media for a long time is um there's the stat that I

**[29:40]** always think is crazy. The the average American I think has I think it's fewer than three friends. M three people that they'd consider friends and and the average person has demand for meaningfully more. I think it's like 15

**[29:53]** friends or something, right? I guess there's probably some point where you're like, "All right, I'm just too busy. I can't deal with more people." But but the average person wants more connectivity connection than they have.

**[30:03]** Um, so you know, there's a lot of questions that people ask of stuff like, okay, is this going to replace kind of in-person connections or real life connections? And my default is that the answer to that is probably no. I think

**[30:21]** it it it it you know I think that there are all these things that are better about kind of physical connections when you can have them. But the reality is that people just don't have the connection and they feel more alone um a

**[30:34]** lot of the time than they would like. So I think that a lot of these things that today there might be a little bit of a stigma around um I would guess that over time we will find the vocabulary as a

**[30:48]** society to be able to articulate why that is valuable and why the people who are doing these things are like why they are rational for doing it and like and how it is adding value for their for their lives. But but also I think that

**[31:00]** the field is very early. So, um I mean it's like I I think you know there are a handful of companies and stuff who are doing virtual therapists and you know there's like virtual girlfriend type stuff but it's um it's very early right.

**[31:13]** It's I mean the the embodiment in the things is is pretty weak. A lot of them like you you open it up and it's just like a an image of of like of the therapist or the person you're talking to or whatever. I mean sometimes there's

**[31:24]** some very rough animation but it's not like an embodiment. I mean, you've seen the stuff that we're working on in reality labs where like you have the codec avatars and it like feels like it's a real person. I think that's kind

**[31:34]** of where it's going. You're going to, you know, you you'll be able to um basically have like an always on video chat where it's like, oh, and also the the the um the uh the AI will be able to, you know, the gestures are

**[31:47]** important, too. Like more than half of communication when you're actually having a conversation is not the words that you speak. It's all the non-verbal stuff. Yeah. I I did get a chance to check out um Orion the other day and I

**[31:57]** thought it was super impressive and I'm mostly optimistic about the technology just because generally I'm as you as you mentioned like libertarian about if people are doing something probably think it's good for them. Although I

**[32:07]** actually don't know if it's the case that if somebody is using Tik Tok they would say that they're happy with how much time they're spending on Tik Tok or something. So I'm mostly optimistic about it also in the sense that if we're

**[32:15]** going to be living in this future world of AGI we need to be in order to keep up with it humans need to be upgrading our capabilities as well with tools like this. Um, and just generally there gonna be more beauty in the world if you can

**[32:24]** see Studio Giblly everywhere or something. I was worried that one of the flagship use cases that your your team showed me was I'm sitting at the breakfast table and on the periphery of my vision is just a bunch of reels that

**[32:36]** are scrolling by. Um, maybe in the future my AI girlfriend is on the other side of the screen or something. Um, and so I I am worried that we're just removing all the friction between getting totally reward hacked by our

**[32:50]** technology. Um yeah, how do we make sure like I don't know this is not what ends up happening in 5 years? I mean again I think I think people have have a good sense of what they want. I mean that that experience that you saw was that

**[33:02]** was a demo just to show multitasking and holograms, right? So I mean I I agree that like I don't think that the the future is like you have stuff that's trying to compete for your attention in the corner of your vision all the time.

**[33:15]** I don't think people would like that too much. M um so it's actually it's one of the things as we're designing these glasses that we're really mindful of is like probably the number one thing that

**[33:28]** glasses need to do is get out of the way and be good glasses, right? And um as an aside, I think that's part of the reason why the Rayban Meta product has done so well is like all right, it's like great for listening to music and taking phone

**[33:45]** calls and taking photos and videos and the AI is there when you want it, but when you don't, it's like a great, you know, good-looking pair of glasses that that that that people like and and it kind of gets out of the way. Well, um I

**[34:00]** would guess that that's going to be a very important design principle for for the um the augmented reality future, right? The main thing that I that I see here is, you know, I think it's kind of crazy that for how important the digital

**[34:18]** world is in all of our lives, the only way we can access it is through these like physical, you know, digital screens, right? It's like you you have like a phone, you have your your your computer,

**[34:32]** you can put a big TV. It's like this huge physical thing. Um it just seems like we're at the point with technology where the physical and the digital world should really be fully blended and that's what the holographic overlays

**[34:48]** allow you to do. Um but I agree. I think a a big part of the design principles around that are going to be okay, you'll you'll be interacting with with people and you'll be able to bring digital artifacts into those interactions and be

**[35:01]** able to do cool things like very seamlessly, right? It's like if I want to show you something here, like here's a screen. Okay, here it is. I can show you. You can interact with it. It can be 3D. Um we can kind of play with it. Um

**[35:14]** you want to, you know, like play a card game or whatever. It's like all right, here's like a deck of cards. We can play with it. It's like two of us are here physically like you have a a third friend who's just hologramming in,

**[35:25]** right? And that they can they can kind of participate too. Um but but I think that in that world people are going to be you know just like you don't want your physical space to be cluttered. It's sort of like a you know it it just

**[35:37]** kind of has like a it wears on you psychologically. I don't think people are going to want the digital kind of physical space to to feel that way either. So, I don't know that that's more of an aesthetic and and and and one

**[35:48]** of these norms that I think will have to get worked out. But, um, but I I I I think I think we'll figure that out. Going back to the AI conversation, you're mentioning how big of a bottleneck um the physical

**[36:01]** infrastructure can be. Related to other open source models like Deepseek and so forth. Deepseek right now has less compute uh than a lab like Meta and you could argue that it's competitive with the llama models. Um, if China is better

**[36:14]** at, you know, physical infrastructure, industrial scaleups, um, getting more power and more data centers online, how worried are you that this will they might beat us here? I I mean, I think it's a it's like a real competition. I

**[36:26]** mean, I think that you're seeing the the industrial policies really play out. um where yeah I mean I think China's bringing online more power and because of that I think that the US really needs to focus on streamlining the ability to

**[36:44]** build data centers and build and produce energy um or or I think we will be at a significant disadvantage. Um, at the same time, I think some of the export controls on things like chips, I think you can see how they're

**[36:58]** clearly working in a way because, you know, there was all the conversation with DeepSeek about, oh, they did all these like very impressive low-level optimizations. And the reality is they did, and that is impressive, but then

**[37:14]** you ask why did they have to do that when none of the like American labs did it? And it's like, well, because they're using like partially nerfed chips that are the only thing that Nvidia is allowed to sell in China because of the

**[37:25]** ex export controls. So, so Deepsee basically had to go spend a bunch of their calories in time doing low-level infrastructure optimizations that the American labs didn't have to do. Now, they produced a good result on text,

**[37:43]** right? It's like I mean, Deepseek is text only. Um, so the infrastructure is impressive, the text result is is impressive. Um, but every new major model that comes out now is multimodal, right? It's image,

**[37:59]** um, it's voice and and and and theirs isn't. And now the question is why is that the case? I don't think it's because they're not capable of doing it. I think that they basically had to spend their calories on doing these

**[38:11]** infrastructure optimizations to overcome the fact that there were these export controls. Um, but when you compare like Llama 4 with DeepSeek, I mean, our reasoning model isn't out yet. So, I think that the the kind of R1 comparison

**[38:23]** isn't isn't isn't clear yet, but um, but we're basically like effectively same ballpark on all the tech stuff is what DeepS is doing, but with a smaller model. So it's it's much more kind of efficient per um the

**[38:38]** the kind of cost per intelligence is lower with what we're doing for llama on text and then all the multimodal stuff we're effectively leading at and it just doesn't even exist in their stuff. So um so I think that the llama 4 models when

**[38:51]** you compare them to what they're doing are are good and and I think generally people are going to prefer to use the llama 4 models. Um, but I think that there is this interesting contour where like it's clearly a good team that's

**[39:06]** doing stuff over there and I think you're right to ask about the um accessibility of power, the accessibility of compute and chips and things like that. Um, because I think what the the kind of work that you're

**[39:16]** seeing the different labs do and play out I I think is somewhat downstream of that. Premium products attract a ton of fake account signups, bot traffic, and free tier abuse. And AI is so good now that it's basically useless to just have

**[39:28]** a capture of six squiggly numbers on your signup page. Take Cursor. People were going to insane lengths to take advantage of Cursor's free credits, creating and deleting thousands of accounts, sharing login, even

**[39:41]** coordinating through Reddit. And all this was costing Cursor a ton of money in terms of inference compute and LLM API calls. Then they plugged in work OS Radar. Radar distinguishes humans from bots. It looks at over 80 different

**[39:56]** signals from your IP address to your browser to even the fonts installed on your computer to ensure that only real users can get through. Radar currently runs millions of checks per week. And when you plug Radar into your own

**[40:11]** product, you immediately benefit from the millions of training examples that Radar has already seen through other top companies. Previously, building this level of advanced protection in-house was only possible for huge companies.

**[40:24]** But now with Work OS Radar, advanced security is just an API call away. Learn more at workos.com/raar. All right, back to Zuck. So Sam Alman recently tweeted that OpenAI is going to release an

**[40:38]** open-source uh soda reasoning model. I think part of the tweet was that we will not do anything silly like um say that you you can only use it if you have less than 700 million users. Um, DeepSseek has the MIT license. Uh, whereas Llama,

**[40:54]** I think a couple of the contingencies in the llama license require you to say built with llama on applications using it or any model that you train using llama has to begin with the word llama. Yeah. What do you think about the

**[41:04]** license? Should it be less ownorous for developers? I mean, look, I mean, I we've basically pioneered like the open- source LLM thing. So, I mean, I I I don't I don't consider the the license to be ownorous. I I kind of, you know,

**[41:19]** think that when we were starting to push on open source, it was this it was this big debate in the industry of like is this even a reasonable thing to do? Like can you do something that is safe and trustworthy with open source? Like is um

**[41:36]** will open source be ever be able to be competitive enough that anyone will even care? and and basically when we were answering those questions which you know a lot of the hard work that you know I think a lot of the teams at Meta

**[41:48]** although there there are other folks in the industry but really the llama models were the ones that I think broke open this whole open source um AI thing in a in a huge way um you know we were very focused on okay if we're going to put

**[42:00]** all this energy into it then at a minimum you know if you're going to have these large cloud companies like Microsoft and Amazon and Google turn around and sell our model that we should at least be able to have a conversation

**[42:15]** with them before they do that around um around basically like okay what kind of business arrangement should we have but but our goal with the with the license isn't um you we're generally not trying to stop people from using the model we

**[42:29]** we just think like okay if you're like one of those companies or you know if you're Apple um you know just come talk to us about what you want to do and and let's find like a productive way to to do it together. So I think that that's

**[42:40]** generally been fine. Now um if the whole open source part of the industry evolves in a direction where you know there's like a lot of other great options and if if like the you know the license ends up being a reason why people don't want to

**[42:56]** use Llama then I don't know we we'll have to reevaluate the strategy whether you know what it makes sense to do at that point. But I I just don't think we're there. That's not in practice a thing that we've seen um companies

**[43:08]** coming to us and saying we don't want to use this because your your license says that if you're if you reach 700 million people you have to come talk to us. So, um, it's at least so far it's a little bit more of something that we've heard

**[43:21]** from like kind of open-source purists, like is this as clean of an open source model as you we as as you'd like it to be? And and look, I mean, I think that debate has existed since the beginning of open source with like um, you know,

**[43:38]** the you know, just all the GPL license stuff versus other things. And it's like okay does like does it need to be the case that anything that touches open source can has to has to be open source or can people just take it and use it in

**[43:49]** different ways and I'm sure there will continue being debates around this but I don't know if you're if you're spending many many billions of dollars training these models I think asking the other companies that um are also huge and

**[44:02]** similar in size and can easily kind of afford to have a a relationship with us to talk to us before they use it. I think it seems like a pretty reasonable thing if it turns out that you you know other models are also you know there's

**[44:15]** like a bunch of good open source models so that part of your mission is fulfilled and maybe other models are better at coding. Is there a world where you just say look o open source system ecosystem is healthy there's plenty of

**[44:27]** competition we're happy to just use some other model whether it's for internal um software engineering at meta or deploying to our apps we don't necessarily need to build with llama um well again I mean we do a lot of things

**[44:40]** so it's possible that you know I I guess let's take a step back the reason why we're building our own big models is because we want to be able to like build exact ly what we want, right? And and none of the other models in the world

**[44:55]** are sort of exactly what we want. If they're open source, then you can take them and you can fine-tune them in different ways, but you still have to deal with the model architectures and, you know, they make different size

**[45:06]** tradeoffs around um that affect the latency and inference cost of the models. And it's like, okay, the scale that we operate at um that stuff really matters. Like we made the Llama Scout and Maverick models certain sizes for a

**[45:20]** specific reason because they fit on a host and we wanted certain latency especially for the voice models that we're that we're working on that we want to just basically have perveyed and and be across everything that we're doing

**[45:31]** from the glasses to all of our apps to the Meta AI app and and all this stuff. So um so I think that there's a level of kind of control of your own destiny that you only get when you when you build the stuff yourself. That said, there are a

**[45:45]** lot of things that like AI is going to be used in every single thing that every company does. When we build a big model, we also need to choose which things which use cases internally we're going to optimize for. So, does that mean that

**[45:56]** for certain things, we're not going to, you know, think that like, okay, maybe Claude is better for building this specific development tool that this team is using. All right, cool. Then, like, use that. Fine, great. Um, I don't think

**[46:07]** we don't want to fight with, you know, one hand tied behind our back. Um, we're doing a lot of different stuff. Um, you also asked would we maybe would it not be important because other people are doing open source.

**[46:20]** Um, I don't know on this I'm a little more worried because I think you have to ask for anyone who shows up now and is doing open source now that we have done it. There's a question which is would they

**[46:33]** still be doing open source if we weren't doing it? And like I think that there are a handful of folks who see the trend that more and more development is going towards um towards open source and they're like a crap like we kind of need

**[46:45]** to be on this train or else we're going to lose like we have some closed model API and like increasingly a lot of developers that's not what they want. Um, so, so I think you're seeing a bunch of the other players start to do some

**[46:58]** work in open source, but it's just unclear if it's dabbling or fundamental for them in the way that it has been for us. And, you know, a good example is like what's going on with like Android, right? It's like Android started off as

**[47:12]** the open source thing. There's not really like any open source alternative. Like I think over time Android has just been kind of getting more and more closed. Um, so I think if you're us, you'd kind of need to worry that if

**[47:27]** we stopped pushing the industry in this direction that like all these other people maybe are only really doing it because they're trying to kind of compete with us and the direction that we're pushing things and you know

**[47:41]** they've they already have their revealed preference for what they would build if open source didn't exist and um and it wasn't open source, right? So um so I I I just think we need to be careful about relying on that continued behavior for

**[47:55]** the future of the technology that we're going to build at the company. I mean another thing I've heard you mention is that it's important that the standard gets built around American models like Llama. Um I guess I wanted to understand

**[48:07]** your logic there because it seems like with certain kinds of networks it is the case that the Apple App Store just has a big contingency around what it's built around. Um, but it doesn't seem like, you know, you if you build some sort of

**[48:19]** scaffold for DeepSeek, you couldn't have easily just switched it over to Llama 4, especially since between generations, like Llama 3 wasn'te, Llama 4 is. So, things are changing between generations of models as well. So, what's the reason

**[48:30]** for thinking things will get built out in this contingent way on a specific standard? I'm I'm not sure what do you mean by contingent? Oh, as in like it's important that people are building for Lama rather than for LLMs in general

**[48:41]** because that will determine what the standard is for sure. Well, look, I mean, I think these models encode values and ways of thinking about the world. Mhm. And you know, we had this interesting experience early on

**[48:54]** where we took an early version of Llama and we translated it. I think it was it might have been into French or some other language. And the feedback that we got um I think it was I think it was French

**[49:09]** from from French people was this sounds like an American who learned to speak French. like it doesn't sound like a French person. It's like, well, what do you mean? Does it not speak French? Well, it's like, no, it speaks French

**[49:18]** fine. It's just like the way that it thinks about the world is like seems slightly American. So, I think there's like these subtle things that kind of get built into it. Um, over time, as the models get more sophisticated, they

**[49:33]** should be able to embody different value sets across the world. So maybe that's like a very kind of um you know not particularly sophisticated example, but I think it sort of illustrates the point.

**[49:45]** Um and you know some of the stuff that we've seen in testing some of the models especially coming out of China is like they sort of have certain values encoded in them and um and it's not just like a light fine-tune to get that to feel the

**[50:04]** way that you want. Now the stuff is different, right? So I think language models um or something that has like a kind of like a world model embedded into it have more values. Reasoning I think

**[50:15]** is I mean I guess there there are kind of values or ways to think about reasoning but one of the things that's nice about the reasoning models is they're trained on verifiable problems. So do you need to be worried about like

**[50:27]** cultural bias if your model is doing math? Probably not. Right? I think that that's, you know, I think it's like the the chance that like some reasoning model that was built elsewhere is like going to kind of incept you by like

**[50:44]** solving a math problem in a way that's that's um devious seems low. Um there's a whole set of different issues I think around coding um which is the other verifiable domain which is you know I think you you kind of need to be worried

**[50:57]** about like waking up one day and like does a model that have some tie to another government like can it embed all kinds of different vulnerabilities and code that then like the intelligence organizations associated with that

**[51:12]** government can then go exploit. So now you sort of like all right like in some future version where you have you know some model from some other country that we're using to like secure or build out a lot of our systems and then all of a

**[51:26]** sudden you wake up and it's like everything is just vulnerable to um in a way that like that country knows about but but like you don't or or it turns on a vulnerability at some point. Those are real issues. Um, so what we've basically

**[51:40]** found is um, you know, I mean, I'm I'm very interested in studying this because I think one of the main things that's interesting about open source is the ability to distill models. Um, you know, most people the the primary value isn't

**[51:54]** just like taking a model off the shelf and saying like, okay, like Meta built this version of Llama. I'm going to take it and I'm going to run it exactly in my application. It's like, no, well, your application isn't doing anything

**[52:02]** different if you're just running our thing. you're at least going to fine-tune it or try to distill it into a different model. And when we get to stuff like the behemoth model, like the whole value in that is being able to

**[52:13]** basically take this very high amount of intelligence and distill it down into a smaller model that you're actually going to want to run. But this is like the beauty of distillation. And it's like one of the things that I think has

**[52:23]** really emerged as a very powerful technique in the last year since the last time we we sat down is um and I think it's worked better than most people would predict is you can basically take a model that is much

**[52:34]** bigger and take probably like 90 or 95% of its intelligence and run it in something that's 10% the size. Now do you get 100% of the intelligence? No. But like 95% of the intelligence at 10% of the cost is like pretty good for for

**[52:49]** a lot of things. Um, the other thing that's interesting is now with this like more varied open- source community where you it's not just Llama, you have other models, you have the ability to distill from multiple

**[53:02]** sources. So now you can basically say, okay, Llama's really good at this, like maybe the architecture is really good because it's fundamentally multimodal and fundamentally more um inference friendly and more efficient. But like

**[53:15]** let's say this other model is better at coding. Okay, well just you can distill from both of them and then build something that's better than either of them for your own use case. Um, so that's cool, but you do need to solve

**[53:26]** the security problem of knowing that you can distill it in a way that is safe and secure. And so this is something that that we've been researching and have put a lot of time into. And what we've basically come to is like look, anything

**[53:39]** that's kind of like language is is quite fraught because there's like a lot of values embedded in that. So unless you don't care about having the values from whatever the model is that you got, you probably don't want to like distill a

**[53:51]** straight like language world model. um on reasoning. I think you can get a lot of the way there by limiting it to verifiable domains, running um kind of code cleanliness and security filters like like whether it's like the Lamag

**[54:10]** Guard open source or the code shield open source things that we've done that basically um allow you to incorporate different different um input into your models and make sure that the that both the input and the output um are secure

**[54:22]** and then just a lot of red teaming to make sure that you're you're um like you you just have people who are experts who are looking at this it's like all right is this model doing anything that isn't what I want after distilling from

**[54:32]** something and I think with a combination of those techniques you can probably distill on the reasoning side for verifiable domains quite securely that's something I'm I'm pretty confident about and it's

**[54:46]** something that that we've done a lot of research around but I think this is a very big question is like how do you do good distillation because there's just so much value to be unlocked but at the same time I Do you just think that there

**[54:57]** is some fundamental bias in the different models? Speaking of value to be unlocked, what do you think the right way to monetize AI will be? Because obviously digital ads are quite lucrative, but as a fraction of total

**[55:08]** GDP, it's small in comparison to like all remote work. Um, uh, like even if you can increase it productivity and not replace work, that's still worth tens of trillions of dollars. So, is it possible that ads might not be or Yeah. How do

**[55:22]** you think about this? I I mean like we were talking about before, there's going to be all these different applications and different applications tend towards different things. Um ads is great when you want to offer people a free service,

**[55:32]** right? Because it's free. You need to cover it somehow. Ads is like, okay, it's ads solves this problem of like a person does not need to pay for something and they can get something that is like amazing for free. Um and

**[55:46]** also, by the way, with modern ad systems, a lot of the time people think that the ads add value to the thing if you do it well, right? It's a um you know, you need to get be good at ranking and and you need to be good at having

**[55:56]** enough liquidity of advertising inventory. Um so that way, you know, if you only have five advertisers in the system, no matter how good you are at ranking, you may not be able to show something to someone that they're

**[56:06]** interested in. But if you have a million advertisers in the system, then you're probably going to be able to find something pretty compelling if you're good at at picking out, you know, the different needles in the haststack that

**[56:16]** that person's going to be interested in. So, I think that definitely has its place, but there are also clearly going to be other business models as well, including ones that

**[56:29]** um just have higher costs, so it doesn't even make sense to offer them for free. Um, which by the way, there have always been business models like this. there's a reason why social media is free and ad supported, but then if you want to watch

**[56:42]** Netflix um or like ESPN or something, you need to pay for that. It's okay because the content that's going into that like they need to produce it and that's very expensive for them to produce and they probably could not have

**[56:54]** enough ads in the service in order to make up for the the cost of producing the content. So basically, you just need to pay to to access it. Um then the trade-off is fewer people do it, right? right? It's like they're talking about

**[57:05]** hundreds of millions of people using those instead of billions. So, it's there's kind of a a value switch there. Um, I think similar here, you know, not everyone is going to want like a software engineer or a thousand software

**[57:18]** engineering agents or whatever it is, but if you do, that's something that you you are probably going to be willing to pay thousands or tens of thousands or hundreds of thousands of dollars for. Um, so I I think that this just speaks

**[57:31]** to the diversity of different things that need to get created is like there are going to be business models at each point along the spectrum and at Meta. Um, yeah, for the consumer piece, we

**[57:43]** definitely want to have a free thing and I'm sure that will will end up being ad supported. But I also think we're going to want to have a business model that supports people using arbitrary amounts of compute to do like really even more

**[57:57]** amazing things than what it would make sense to be able to offer with a free service and for that I'm sure we'll end up having a premium service. But but I mean I think our our basic you know values on this are we want to serve as

**[58:08]** many people in the world. Lambda is the cloud for AI developers. They have over 50,000 Nvidia GPUs ready to go for startups, enterprises, and hypersailers. Compute seems like a commodity though, so why use Lambda over anybody else?

**[58:23]** Well, unlike other cloud providers, Lambda's only focus is AI. This means their GPU instances and ondemand clusters have all the tools that AI developers need pre-installed. No need to manually install CUDA drivers or

**[58:38]** manage Kubernetes. And if you only need GPU compute, you can save a ton of money by not paying for the overhead of general purpose cloud architectures. Lambda even has contracts that let enterprises use any type of GPU in their

**[58:49]** portfolio and easily upgrade to the next generation. For all of you wanting to build with Llama 4, Lambda has a serverless API without rate limits. It's built with rapid scaling in mind. Users have 1,00x their inference consumption

**[59:02]** without ever having to apply for a quota or even speak to a human. Head to lambda.ai/dark AI/DLCH for a free trial of their inference API featuring the best open source models like DeepSeek and Llama at

**[59:15]** the lowest prices in the industry. All right, back to Zach. How do you keep track of um you've got all these different projects, some of which we've talked about today. I'm sure there's many I don't even know about.

**[59:26]** um as the CEO overseeing everything there's a big spectrum between like you know going to the llama team and here's the hyperparameters you should use to just giving like a mandate like go make the AI better and there's many different

**[59:38]** projects how do you think about the way in which you can best deliver your value ad um and oversee all these things well I mean a lot of what I spend my time on is trying to get awesome people onto the teams right I mean it's um

**[59:50]** so there's that and then there's stuff that cuts across teams it's like all right you build Meta AI and you want to get it into WhatsApp or Instagram, it's like, okay, then now I need to get those teams to talk together. And then there's

**[1:00:04]** a bunch of questions like, okay, I was um you know, it's like, okay, do you want the thread for Meta AI and WhatsApp to feel like other WhatsApp threads or do you want it to feel like other kind of like AI chat experiences? There's

**[1:00:20]** like different idioms for for those. And so I think that there's like all these interesting questions that sort of need to get answered around like how does this stuff basically fit into all of what we're doing. Then there's a whole

**[1:00:30]** other part of what we're doing which is basically pushing on the infrastructure. If you're if you want to stand up a gigawatt cluster then first of all that has a lot of implications for um for the way that we're doing infrastructure

**[1:00:43]** buildouts. It has sort of political implications for how you engage with the different states where you're building that stuff. Um it has financial implications for the company in terms of all right there's like a lot of economic

**[1:00:55]** uncertainty in the world. Do we like go double down on infrastructure right now? Um and and if so what other trade-offs do we want to make around the company? And those are things that like it's tough for other people to really make

**[1:01:08]** those kind of decisions. Um, and then and then I think that there's this question around like taste and quality, which is like when is something good enough that we want to ship it? And and I I do feel

**[1:01:22]** like in general I'm the steward of that for the company, although you know, we have a lot of other people I think have good taste as well who are also filters for for different things. But um but yeah, I think that those are

**[1:01:35]** those are basically the areas. But I think um AI is interesting because more than some of the other stuff that we do, it is more research and modelled than really productled. Like you can't just

**[1:01:47]** like design the product that you want and then try to build the model to fit into it. You really need to like design the model first and like the capabilities that you want and then you get some emergent properties. Then it's

**[1:01:59]** like, oh, you can build some different stuff because this kind of turned out in this way. And I think at the end of the day like like people want to use the best model, right? So that's partially why, you know, when we're talking about

**[1:02:10]** building the most like personal AI, um the best voice, the best personalization, um and like also a very smart experience with very low latency. Those are the things that we basically need to design

**[1:02:25]** the whole system to build which is why we're working on full duplex voice which is why we're working on like the personalization to both both have like good memory extraction from your interaction with AI but also be able to

**[1:02:36]** plug into all the other meta systems and why we design the um specific models that we design to have the kind of size and latency parameters that they do. M speaking of politics, um there there's been this perception

**[1:02:51]** that some tech leaders have been aligning with Trump. You and others have donated to his inaugural event and we're on stage with him and I think you settled like a lawsuit which gave resulted them getting $25 million. I

**[1:03:02]** wonder um what's going on here. Is it does it does it feel like the cost of doing business with administration or Yeah. What's the best way to think about this? My my view on this is like he's the

**[1:03:14]** president of the United States. Our default as an American company should be to try to have a productive relationship with whoever is running the government. Um I would do this, you know, like we we've tried to offer to support um

**[1:03:26]** previous administrations as well. I've I've been pretty public with some of my frustrations with the previous administration, how they basically did not engage with us or the business community more broadly, which I think

**[1:03:39]** frankly I think is going to be necessary to make progress on some of these things. Like we're not going to be able to build the level of energy um that we need if there if you don't have a dialogue and they're not prioritizing

**[1:03:50]** trying to do those things. So, um, but fundamentally, you know, look, I mean, I think a lot of people want to write the story about like like, you know, what direction are people going? I like I just think it's like we're trying to

**[1:04:03]** build great stuff. We want to work with have a productive relationship with people and that's sort of that's how I see it and it is also how I would guess most others see it. Um, but obviously I can't speak for them. um you've spoken

**[1:04:21]** out about how you've rethought some of the ways in which you um engage and defer to the government in terms of moderation stuff in the past. How how are you thinking about AI governance? Because if AI is as powerful as we think

**[1:04:33]** it might be, the government will want to get involved. What what is like the most productive approach to take there and what should the government be thinking about here? Yeah, I guess in the past I I probably just um I mean most of the

**[1:04:45]** comments that I made I think were in the context of content moderation, right? where um you know it's been an interesting journey over the last 10 years on this where there it's obviously been an interesting time in history.

**[1:04:56]** There have been novel questions raised about online content moderation. Um some of those have led to I think productive um new systems getting built like our AI systems to be able to detect nation states trying to interfere in each

**[1:05:11]** other's elections. I think we we'll continue building that stuff out and that that I think has been net positive. I think other stuff We went down some bad paths. Like I just think the facteing thing Yeah. was not

**[1:05:22]** as effective as community notes because it's not an internet scale solution. There weren't enough fact checkers and like people didn't trust the specific fact checkers. They like you you wanted a more robust system. So I I think where

**[1:05:33]** we got with community notes is the right one on that. But um but my point on this was was more that um that I think historically I probably deferred a little bit too much to um either the media in and kind of their critiques or

**[1:05:52]** the government on things that they did not really have authority over but just as like a central figure. Um, like I I I I think we tried to build systems that where maybe we could not have to make all of the content

**[1:06:09]** moderation decisions ourselves or something. And I I guess I just think part of the the growth process over the last 10 years is just okay, like we're a meaningful company. We need to own the decisions that we need to make. we

**[1:06:22]** should listen to feedback from people but shouldn't defer too much to people who are not who do not actually have authority over this because at the end of the day we're like we're in the seat and we need to like own the decisions

**[1:06:33]** that we make and um so I think we probably you know it's it's been a maturation process and um in some ways painful but but I I you know I think we're we're probably a better company for it. Will tariffs increase the cost

**[1:06:47]** of building data centers in the US and shift buildouts to Europe and Asia? It is really hard to know how that plays out. Um I think we're probably in the the early innings on that and um it's very hard to know. Got it. Um

**[1:07:01]** what is your single highest leverage hour in a week? What are you doing in that hour? I don't know. I mean every week is a little bit different. Um, I mean, it's probably got to be the case that the most leveraged thing that you

**[1:07:13]** do in a week is not the same thing each week, or else by definition, you should probably spend more than one hour doing that thing every week. Um, but yeah, I don't know. It's it's part of the fun of of

**[1:07:25]** of both, I guess, this job, but also the industry being so dynamic is like things really move around, right? and like and the world is very different now than it was at the beginning of the year than it was 6 months into the

**[1:07:40]** middle of last year. Um, you know, I think a lot has sort of has really advanced meaningfully and like a lot of cards have been turned over since the last time that we sat down. I think that was about a year ago, right? Yeah. Yeah.

**[1:07:49]** I guess you were saying earlier that recruiting people is a super high leverage thing you do. It's very high leverage. Yeah. Yeah. What would be possible if you know you've talked about these models being mid-level software

**[1:07:59]** engineers by the end of the year or um what would be possible if say software productivity increased like 100x in two years what kinds of things could we build that we can't build right now what kinds of things well well I it's an

**[1:08:13]** interesting question um I think one theme of this conversation is that the like amount of creativity that's going to be unlocked is going to be massive Um, and if you look at like the overall arc

**[1:08:28]** of kind of human society and the economy over 100 or 150 years, it's basically people going from being primarily agrarian and most of human energy going towards just feeding ourselves to that has become a kind of

**[1:08:46]** smaller and smaller percent and the things that take care of like our basic physical needs are a smaller and smaller % of human energy which has led to two impacts. One is more people are doing kind of creative

**[1:09:00]** and cultural pursuits and two is that more people on in general spend less time working and more time on entertainment and culture. Um I think that that is almost certainly

**[1:09:13]** going to continue as as this goes on. This isn't like the one to twoyear thing of what happens when you have a a like a super powerful software engineer, but I think over time, you know, if you like everyone is going to have these

**[1:09:25]** superhuman tools um to be able to create a ton of different stuff. I think you're going to get this incredible diversity. Um, part of it is going to be solving like things that we hold up as like these like hard problems like solving

**[1:09:39]** diseases or like solving different things around science or um or just like different technology that makes our lives better. But I would guess that a lot of it is going to end up being kind of cultural and social pursuit and

**[1:09:55]** entertainment. And like I would guess that the world is going to get a lot more like a like a lot funnier and like weirder and and quirkier in a way that like the memes on the internet have sort of gotten over the last 10 years. And um

**[1:10:10]** and I think that that adds a certain kind of richness and depth as well that in kind of funny ways I think it actually helps you connect better with people because now like I don't know it's like all day long I just find

**[1:10:23]** interesting stuff on the internet and like send it in group chats to the people I care about who I think are going to find it funny. And it's like like the the media that people can produce today to express very very

**[1:10:33]** nuance specific cultural ideas. Um I don't know. It's it's it's cool and I think that'll continue to get built out and I think it does advance society in a bunch of ways even if it's not like the hard science way of curing a disease.

**[1:10:50]** But I guess this is sort of if you think about it like the the like meta social media view of the world is like yeah I think people are going to spend a lot more time doing that stuff in the future. Um and and it's going to be a

**[1:11:01]** lot better and it's going to help you connect because it's like going to help express different ideas um is the world's going to get more complicated but like our technology our cultural technology to kind of express these very

**[1:11:11]** complicated things um in like a very kind of funny little clip or something um are going to just get so much better. So, I know that's all great. Um, I don't know, next year for I I tend to I mean, just I guess one other

**[1:11:29]** thought that I think is interesting to cover is um I tend to think that for at least the foreseeable future, this is going to lead towards more demand for people doing work, not less. Now, people have a

**[1:11:44]** choice of how much time they want to spend working. Um but like I'll give you one interesting example of something that that we were talking about recently. We um so we have like three almost three and a half

**[1:11:56]** billion people use our services every day. And one question that we've struggled with forever is like how do we provide customer support right today like you can you can write an email. Um but we've never seriously been

**[1:12:07]** able to contemplate having um you know having like voice support where someone can just call in. And I guess that's maybe one of the artifacts of having a free service, right? Is like the the revenue per person is not so high that

**[1:12:19]** you can have an economic model that people can can kind of call in, but also with three and a half billion people using your service every day. I mean, you there would be like a massive massive number of people like some like

**[1:12:29]** like the biggest call center in the world type of thing. Yeah. Um but it would be like 10 20 billion something ridiculous a year to kind of staff that. So we we've never really kind of like thought too seriously about it because

**[1:12:42]** it was always just like no, there's no way that this kind of makes sense. But now as the AI gets better, you you're going to get to this place where the AI can handle a bunch of people's issues, not all of them, right? Because um maybe

**[1:12:58]** 10 years from now or something it can handle all of them. But when we're thinking about like a 3 to 5 year time horizon, um it'll be able to handle a bunch. Kind of like self-driving cars can handle a

**[1:13:09]** bunch of terrain, but in general, they're not like doing the whole route by themselves yet in in in most cases, right? It's like people thought truck driving jobs were going to go away. There's actually more truck driving jobs

**[1:13:20]** now than there were like when we started talking about self-driving cars um in whatever it was almost 20 years ago. Um, and I think for going back to this customer support thing, it's like, all

**[1:13:33]** right, it wouldn't make sense for us to staff out um calling for everyone. But let's say the AI can handle 90% of that then like and then if you if it can't handle it, then

**[1:13:46]** it kicks it off to a person. Okay. Now, like if you've gotten the cost of providing that service down to onetenth of what it would have otherwise been, then all right, maybe now that actually makes sense to go do and that would be

**[1:13:59]** kind of cool. So, the net result is like I actually think we're probably going to go hire more customer support people, right? It's like like the the common knowledge or like the the kind of common belief that people have is that like,

**[1:14:11]** oh, this is clearly just going to automate jobs and like all these jobs are going to go away. I I actually just that has not really been how the history of technology has worked. It's it's been you know you you can you like create

**[1:14:22]** things that take away 90% of the work and that leads you to want more people not less. Final question. Who is the one person in the world today who you most seek out for advice? Oh man. Well, I feel like it's part of my style is I

**[1:14:36]** like having a breadth of advisors. So, it's it's not just it's not just one person, but it's um we've got a great team. I mean, it's uh you know, I'm I'm think there's people at the

**[1:14:51]** company, people on our board. Um and there's a lot of people in the industry who are doing new stuff. I there's there's not there's not like a single person. Um, but it's uh I don't

**[1:15:04]** know, it's fun and and also as when the world is dynamic, um, just having a reason to work with people you like on cool stuff. Um, to me, like that's what life is about. Yep. All right, great note to close on. Awesome. Thanks for

**[1:15:17]** doing this. Yeah, thank you. I hope you enjoyed this episode. If you did, the most helpful thing you can do is just share it with other people who you think might enjoy it. Send it to your friends, your group chats, Twitter, wherever

**[1:15:28]** else. Just let the word go forth. Other than that, super helpful if you can subscribe on YouTube and leave a five-star review on Apple Podcast and Spotify. Check out the sponsors in the description below. If you want to

**[1:15:39]** sponsor a future episode, go to dwarcash.com/advertise. Thank you for tuning in. I'll see you on the next one.
