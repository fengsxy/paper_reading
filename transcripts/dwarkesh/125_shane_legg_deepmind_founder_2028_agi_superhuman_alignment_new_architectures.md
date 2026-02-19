---
layout: default
type: transcript
series: dwarkesh
episode: 125
guest: ""
title: "Shane Legg (DeepMind Founder) — 2028 AGI, superhuman alignment, new architectures"
source_url: "https://www.youtube.com/watch?v=Kc1atfJkiJU"
analysis_url: /transcripts/dwarkesh/125_shane_legg_deepmind_founder_2028_agi_superhuman_alignment_new_architectures.analysis/
permalink: /transcripts/dwarkesh/125_shane_legg_deepmind_founder_2028_agi_superhuman_alignment_new_architectures/
---

# Transcript: Shane Legg (DeepMind Founder) — 2028 AGI, superhuman alignment, new architectures

Source: https://www.youtube.com/watch?v=Kc1atfJkiJU

---

**[00:00]** okay today I have the pleasure of interviewing Shane leg who is a founder and the chief AGI scientist of Google Deep Mind Shane welcome to the podcast thank you it's pleasure to be here so first question how do we measure

**[00:16]** progress towards AGI concretely so we have these loss numbers and we can see how the loss improves from one model to another but it's just a number how do we interpret this how do we see how much progress we're actually making that's

**[00:28]** that's a hard question um AGI by its definition is about generality so it's not about doing a specific thing it's much easier to measure performance when you have a very specific thing in mind because you can

**[00:42]** construct a test around that well maybe I should first explain what do I mean by AGI because there are a few different Notions when I say AGI I mean um a machine that can do the sorts of uh cognitive things that people can

**[00:55]** typically do possibly more but that's to be an AGI that's kind kind of the the buy you need to meet so if we want to test whether we're we're meeting this threshold or we're getting close to the threshold what we actually need then is

**[01:09]** um a lot of different kinds of measurements and tests of all that spans the bread of all the sorts of cognitive tasks that people can do and then to have a sense of what is human performance you know on on these sorts

**[01:24]** of tasks and that then allows us to sort of Judge whether or not we're we're there it's difficult because you'll never have a complete set of everything that people can do because it's you know such a large set but I think that if you

**[01:36]** ever get to the point where you have a have a have a pretty good range of tests of all sorts of different things that people do cognitive things people do and you have an AI system which can meet Human Performance and all those things

**[01:50]** and with some effort you can't actually come up with new examples of cognitive tasks where the machine is below Human Performance then at that point it's conceptually possible that there is something that the um the machine can't

**[02:05]** do that people can do but if you can't find it with some effort I think practical purposes you now have an AGI so uh let's get more concrete um and you know we measure the performance of these large language models on mlu or

**[02:18]** something and maybe you can explain what all these different benchmarks are but the ones we use right now that you might see in a paper what what are they missing what aspect of human cognition do they not measure adequately o yeah

**[02:32]** another that hard question these These are quite big areas so they don't measure things like uh understanding streaming video for example because these are language models and people can do things like understanding streaming

**[02:44]** video um they don't do things like humans have what we call episodic memory all right so we have a working memory which are things that have happened quite recently and then we have sort of uh cortical memory so these are things

**[02:58]** that have sort of been you know in in our cortex that would be but there's also a system in between which is episodic memory which is a hippocampus and so this is about learning um specific things very very rapidly so

**[03:09]** some of the things I say to you today if you remember them tomorrow that will be your your your episodic memory hamus our models don't really have that kind of thing and we don't really test for that kind of thing we just sort of try to

**[03:20]** make the context Windows which is I think more like a working memory longer and longer to sort of compensate for this but yeah we don't we don't really test for that kind of a thing um so there is there is all sorts of

**[03:32]** bits and pieces but you know it is it is a difficult question because you really need to as I said intelligence the generality of human intelligence is very very broad so you really have to start going into the weeds of trying to find

**[03:44]** you know if there's specific types of things that are missing from existing benchmarks or different categories of benchmarks that you know aren't don't currently exist or something yeah uh the the thing you're referring to with

**[03:56]** episodic memory would it be fair to call that sample efficiency or is that a different uh it's it's very much related to sample efficiency it's it's one of the things that enables humans to be very sample efficient right um large

**[04:08]** language models have a certain kind of sample efficiency because when something's in their context window they can then that that sort of biases the distribution to to behave in a different way and so that's a very rapid kind of

**[04:21]** learning so there are multiple kinds of learning and the existing systems have some of them but not others so it's a little bit complicated so this kind of memory or we call it sample efficiency whatever uh is is it a fatal flaw of

**[04:37]** these deep learning models that it just takes trillions of tokens far more many Ms of magnitude more than a human will see throughout their lifetime or is this something that just solved over time so the models can learn things immediately

**[04:49]** when it's in a context window and then they have the sort of this longer process of when you actually train the base model and so on um and that's they're learning over trillions of tokens but they sort of miss something

**[04:59]** in the middle right that's sort of what I'm getting out here um I don't think it's a fundamental limitation um I think what's happened with uh large language models is something fundamental has changed we know how to build models now

**[05:14]** that have some degree of I would say understanding of of what's going on and that did not exist in the past and because we got a scalable way to do this now that unlocks lots and lots of lots of new things now we can then look at

**[05:30]** things which are missing such as the sort of episodic memory type thing and we can then start to imagine ways to address that so my feeling is that the there are kind of relatively clear paths forwards now to address most the

**[05:46]** shortcomings we see in existing models whether it's about delusions factuality the the type of memory and learning that they have or understanding video or all sorts of things like that so I I'm not actually I don't see there

**[05:59]** are big blockers here I don't see big walls in front of us I just see there's more research and work and these things will improve and and probably be adequately solved but going back to the original question uh how do you measure

**[06:12]** When U human level AI is arrived over Beyond it you as you mentioned there's these other sorts of benchmarks you can use and other sorts of traits but concretely if there is what what would it have to do for you to be like okay

**[06:24]** we've reached human level would it have to beat Minecraft from start to finish would it have to get 100% on MML you what would have to do there is no one thing that would do it because I think that's the nature of

**[06:35]** it it's about general intelligence I would have to make sure it could do lots and lots of different things and it didn't have a gap we already have systems that can do very impressive categories of things to human level or

**[06:47]** even Beyond so I would want a a whole Suite of tests that I felt was very comprehensive and then furthermore when people come and say okay so it's passing our big sweet of test let's try to find examples let's be take

**[07:03]** an adversarial approach to this let's deliberately try to find examples where people can clearly typically do this but the machine fails and when those people cannot succeed I'll go okay we're probably there a lot of your early

**[07:17]** research at least on that's z i find emphasized the that AI should be able to manipulate and succeed in a variety of open-ended environments it kind of sounds like a video game almost is that where your head is still at now or do

**[07:31]** you think about it differently yeah it's evolves a bit when when I did my thesis work around Universal intelligence and so on um I was trying to come up with a sort of extremely Universal General mathematically clean framework for

**[07:49]** defining and measuring intelligence um and I I think there were aspects of that that were successful I think it in my own mind it clarified um the nature of Intelligence being able has been able to perform well

**[08:05]** in lots of different domains and different tasks and so on it's about that sort of capability of performance and and the breadth of performance um so I found that was that was quite helpful and lightening there

**[08:18]** was always the issue of the reference machine because you in in the um in the framework you have a a a waiting of things according to the complexity it's like an oam's razor type of thing where you wait um tasks environments which are

**[08:35]** simpler more highly in this sort of because you get you get an infinite it's a it's countable space of of different uh computable environments or semi computable environments um and that comar complexity measure has something

**[08:51]** built into it which is called a reference machine and that's a free parameter so that means that the the intelligent measure has a free parameter in it and as you change that free parameter it

**[09:03]** changes the weighting and the distribution over the space of all the different tasks and environments so this is sort of an unresolved part of the whole problem so what reference machine should we ideally

**[09:17]** use there isn't really a there's no Universal like one specific reference machine people will usually put a universal cheerwing machine in there but there are many kinds of universal cheerwing machines you have to put sorry

**[09:29]** a universal sh machine there are many different ones so I think given that it's a free parameter I think the most natural thing to do is say okay let's think about what's meaningful to us in terms of intelligence uh I

**[09:45]** think human intelligence is Meaningful to us and the environment that we live in we we know what human intelligence is we are human we interact with other people who have human intelligence we know that human intelligence is possible

**[09:57]** obviously because you know it exists in the world world we know that human intelligence is very very powerful because it's affected the world profoundly in countless ways um and we know if human level intelligence was

**[10:10]** achieved that would be economically transformative because the types of cognitive task people do in the economy would could be done by machines then and it would be uh philosophically important because this is sort of a how we often

**[10:23]** think about you know intelligence and I think historically would be a key point so I think that human intelligence is quite in in a humanlike environment as quite a natural sort of reference point so you could

**[10:34]** imagine sort of setting your un your reference machine um to be such that it emphasizes the kinds of environments that we live in as opposed to some abstract mathematical environment or something like that and so that's how

**[10:49]** I've kind of gone on this journey of let's try to define a completely Universal clean mathematical notion of intelligence to well is has got a free parameter one way of thinking about it is say okay let's think more concretely

**[11:03]** now about human intelligence and can we build sh machines that can match human intelligence because we we understand what that is we know that that is a very powerful thing and it has you know economic philosophical historical kind

**[11:16]** of importance so that's kind of the the and the other aspect of course is that you know in this pure formulation of comor complexity it's actually not computable and you know I obviously knew that there was a there was a limitation

**[11:28]** at the time but it a it was an effort to say okay can we just even very theoretically come up with a clean definition I think we can sort of get there we have this issue of a of a of a reference machine which is unspecified

**[11:41]** so before we move on I do want to ask uh on the original point you made about these machines or these llms need um episodic memory well you said that these are problems that we can solve these are

**[11:56]** not fundamental impediments but are when you say that do you think they'll just be solved by scale or do each of these Need A fine grain specific solution that is architectural in nature I I I think it'll be architectural in nature because

**[12:09]** the well the current architectures they they they don't really have what you need to do this they basically have a context window which is very very fluid of course and they have the weights which things get

**[12:21]** baked into very slowly so to my mind that feels like working memory which is like the the activations uh in your brain and then the weights the sinapsis and so on in your cortex now the the brain separates these things out it has

**[12:33]** a separate mechanism for rapidly learning spec specific information because that's a different type of optimization problem compared to slowly learning deep generalities all right that sort of there's a there's a there's

**[12:47]** a tension between the two but you want to be able to do both you want to be able to I don't know hear someone's name and remember the next day and you also want to be able to integrate information over lifetime so you start to see deeper

**[13:00]** patterns in the world these are these are quite different different um optimization targets different you know processes but a comprehensive system should be able to do both and so I think it's it's conceivable you could

**[13:15]** build one system does both but you can see because they're quite different things that it makes sense for them to different I think that's why the brain does it separately I'm curious about how concretely you think that would be

**[13:24]** achieved and I'm specifically curious um I gu you're can to answer this is part of the answer you know deep mine has been working on these domain specific reinforcement learning type setups Alpha fold Alpha code and so on how does that

**[13:39]** fit into what you see as a path to AGI have these just been orthogonal domain specific models or do they feed into the eventual AGI uh things like Alpha fold are not really feeding into AGI um you know we

**[13:55]** may learn things in the process uh that that may end up being being relevant but I I don't see them as being likely being on the path to AGI um but yeah we're you know we're a big group we've got you hundreds and

**[14:08]** hundreds and hundreds of phds working on lots of different projects so you know when we find um you know what we see like opportunities to to do something significant like Alpha fold we'll go and do it it's not like we we only do AI

**[14:21]** type work we we we work on Fusion reactors and um you know uh uh various things in sustainability energy we've got people looking at um you know satellite images of um of uh deforestation we have people looking at

**[14:39]** U weather forecasting we tons of people lots of things on the point you made earlier about what the the reference class or the reference machine is human intelligence it's interesting because in your 2008 thesis one of the things you

**[14:51]** mentioned almost as a side note is how well how would you measure intelligence and you said well you could do a compression test and you could see if it feel fills in words and a sample of text and that could measure intelligence and

**[15:03]** funnily enough that's basically how LMS are trained at the time did it stick out to you as especially fruitful thing to train for well yeah I mean in a seem what's happened is actually very aligned with um what I write about my thesis

**[15:19]** which are the ideas from Marcus hter um with a where uh you take Solomon of induction which is this incomputable but s of theoretically very elegant and extremely uh sample efficient uh prediction system

**[15:36]** um and then once you have that you can build a a general agent on top of it by basically adding um search and uh reinforcement signal that's what you do with ax um but what that sort of tells you is

**[15:49]** that if you have a fantastically good sequence predictor some approximation of solomo induction then going from that to a very powerful very general AI AGI system is is just sort of another step you know it's is you've actually solved

**[16:07]** a lot of the problem already and I think that's what we're seeing today actually that these incredibly powerful Foundation models are incredibly good sequence Proctors they're compressing the world based on all this data and

**[16:20]** then you could will be able to extend these in different ways and build very very powerful agents out of them okay let me ask you more about that so Richard su's bitter at lesson essay says that there's

**[16:30]** two things you can scale um search and learning and I guess you could say that llms are about the learning aspect um the the search stuff which you've worked on throughout your career where you have an agent that is act you know

**[16:43]** interacting with this environment and is that is that the direction that needs to be explored again or is that something that needs to be added to LMS where they can actually interact with their data or the world in some way yeah um I I I

**[16:56]** think that's on the right track I think there was these Foundation models are World models of a kind and to do really creative um problem solving you need to start searching so if I think about

**[17:11]** something like alphago in the move 37 famous move 37 where did that come from did that come from all its data that it's seen of human games or something like that no it didn't it came from it identifying a move as being quite un

**[17:28]** likely but you know possible and then via process of search coming to understand that the that was actually a very very good move so you need to you to get real creativity you need to search through spaces of possibilities

**[17:42]** and find these sort of hidden gems that's what creativity is I think current language models they don't really do that kind of a thing they really are mimicking the data they are mimicking all the human Ingenuity and

**[17:56]** everything which they have seen from all this data that's coming from the internet that's originally derived from humans if you want a system that can go be truly beyond that and not just generalize in novel ways so it can you

**[18:09]** know these models can blend things they can do you know Harry Potter in the style of a Kan West WAP or something even though it's never happened they can blend things together but to do something that's truly creative that

**[18:21]** there is not just a blending with existing things that requires searching through a space of possibilities and finding these hidden gems that that that are sort of the hidden away in there somewhere and that requires search so I

**[18:33]** don't think we'll see systems that truly Step Beyond their training data until we have powerful search in the process so there are rumors that Google Deep Mind is training your models and you don't have to comment on those specifically

**[18:49]** but when you do that if it's if it's the case that search or something like that is required to go to the next level are you training in a completely different way than say gp4 other Transformers are trained I can't say much about how we're

**[19:03]** training um I think it's fair to say we're doing the sorts of scaling and training roughly that you see many people in the in the field doing um but we have you know our own take on it and own different tricks and techniques okay

**[19:19]** maybe we'll come back to it and get another answer on that but let's talk about alignment briefly so what will it take to align human level and superhuman um AIS and you know it's interesting because the sorts of reinforcement

**[19:34]** learning and selfplay kinds of setups that are popular now like Constitution AI or rhf Deep Mind obviously has expertise in it for for more decades longer so I'm curious what you think of the current landscape and how Deep

**[19:46]** Mind pursues that problem of safety towards human level models so do you want to know about what we're currently doing or would you want me to have a stab at what I think we needs to be done needs to be done needs to be done so I

**[19:57]** mean what in terms of what we we're currently doing we're doing lots of things we're doing interpretability we're doing uh process supervision we're doing red teaming we're doing evaluation for Dangerous capabilities we're doing

**[20:08]** work on institutions and governance and you know tons of stuff right there's lots of different things anyway what do I think needs to be done so I think I think that powerful machine learning powerful AGI is coming in some

**[20:24]** sometime right and if the system is really capable really intelligent really powerful trying to somehow contain it or limit it is probably not a winning strategy because these systems

**[20:37]** ultimately will be very very cable so what you have to do is you have to align it you have to get it so it's fundamentally a highly ethical value aligned system from the get-go right how do you do that

**[20:55]** well I I I have a maybe this is slightly naive but this is this is my take on it how do people do it right if you have a really difficult ethical decision in front of you what do you do right well you don't just do the first thing

**[21:12]** that comes to mind right because you know there could be a lot of emotions involved and other things right it's a difficult problem so what you have to do is you have to calm yourself down you got to sit down and you got to think

**[21:22]** about it you got to think well okay what what could I do I could do this I could do this I could do this if I do each of these things what will happen right and then you have to think about so that requires a model of the

**[21:35]** world and then you have to think about ethically how do I view each of these different actions and the possibilities and what may happen from it right what is the right thing to do and as you think about all the different

**[21:51]** possibilities and your actions and what can follow from them and and and how it aligns with your values and your ethics you can then come to some conclusion of what is really you know the best choice that you should be making if you want to

**[22:03]** be you know really ethical about this I think AI systems need to essentially do the same thing so when you sample from a foundational model at the moment it's like it's blurting out the first thing it's like system one if

**[22:19]** you like from Psychology from gamman right um that's that's not good enough and if we do rhf or um what's it called I can't remember anyway it's the AI version without the the human feedback R A if is

**[22:33]** that what it is oh gosh I'm confusing myself anyway constitutional AI tries to do that sort of thing you're trying to fix the underlying system one in a sense right and that can shift the distribution and that can be very

**[22:45]** helpful but it's a very high dimensional distribution and you're sort of poking it in a whole lot of points and so it's not likely to be a very robust solution right it's like trying to train yourself out of a bad habit you know you can sort

**[22:59]** of do it eventually what you need to do is you need to have a system too you need the system to not just sample from the model you need the system to go okay I'm going to reason this through I'm going to do

**[23:12]** like step-by-step reasoning what are the options in front of me I'm going to use my world model now and I'm going to use a good World model to understand what's likely to happen from each of these options and then reason about each of

**[23:25]** these from an ethical perspective so you need a system which has a a a deep understanding of the world has a good World model it has a good understanding of people it has a good understanding of ethics and it has robust and very

**[23:37]** reliable reasoning and then you set it up in such a way that it applies this reasoning and this understanding of Ethics to analyze the different options which are in front of it and then execute on which is the most ethical um

**[23:51]** way forwards but I think when uh a lot of people think about the fundamental alignment problem the worry is not that it's not going to have a world model necessary to understand its actions or sorry to understand the effects of its

**[24:04]** actions I guess it's one worry but not the main worry the the main worry is that the effects that this cares about are not the ones we will care about and so even if you improve it systems you're thinking and do better planning the

**[24:17]** fundamental problem of we have this really nuanced values about what we want how do we communicate those values and make sure they're reinforced in the uh AI it needs not just a good model of the world but it needs to have really good

**[24:29]** understanding of ethics and we need to communicate to the system what ethics and values it should be following and how do we do that in a way that's we can be confident that a human level or eventually superh human level

**[24:41]** model will preserve those values or learned them in the first place well it should preserve them because if it's making all its decisions based on a good understanding of ethics and values and it's consistent in doing this it

**[24:55]** shouldn't take actions which undermine that there would be they would be inconsistent right so then how do we get to the point where it's learned them in the first place yeah that's the challenge yeah we need to have systems

**[25:05]** the way I think about it is this to have a profoundly ethical AI system it also has to be very very capable it needs a really good World model a really good understanding of ethics and it needs really good reasoning because if you

**[25:18]** don't have any of those things how can you possibly be consistently profoundly ethical you can't so we actually need better reasoning better understanding of the world and better better understanding of Ethics in our systems

**[25:33]** right so it seems to me the former two would just come along for the right as these models get more powerful yeah so that's a nice property because it's actually a capabilities thing to some extent but then if the third one is a

**[25:43]** bottleneck or if the third one is a thing that doesn't come along with the AI itself what is the actual technique to make sure that that happens the third one sorry the ethical model what what do humans value we well we've got we got a

**[25:56]** couple problems first of all of all we need to decide we we should train the system on ethics generally I mean there's a lot of you know lectures and papers and books and all sorts of things so it understands human ethics well

**[26:08]** right and we need to make sure it understands human's ethics well right because that's important at least as well as a you know very good ethicist and we then need to decide okay of this sort of General

**[26:23]** understanding of Ethics what do we want the system to actually value and and what sort of Ethics do we want it to apply now that's not a technical problem that's a problem for society and ethicist and so on to come up with now

**[26:40]** you know I'm not sure there's such a thing as true or correct optimal ethics or something like that but I'm pretty sure that it's possible to come up with a set of Ethics which is much better than the you know what the so-called

**[26:56]** doomers uh worry about in terms of the behavior of of these AGI systems and then what you do is you engineer the system to actually follow yeah um these these things so every time it makes a decision it does an analysis using a you

**[27:12]** know deep understanding of the world and of ethics and very robust and precise reasoning to do an ethical analysis of of what it's doing and of course we'd want lots of other things we want people checking these processes of reasoning

**[27:25]** we'd want people you know verifying that it's it's it's behaving itself in terms of um you know how it reaches these conclusions but I still feel like I don't understand how that fundamental problem of making sure it follows that

**[27:37]** ethic because presumably you know it it has MA little book so understands maest ethics and understands all these other ethics you know um how do we make sure the ethic that we say this is the this is the one we've decided ethicist in

**[27:48]** society so on today that is the one that ends up following and not the other ones that understands right so you have to specify to the system these are the ethical principles that you should follow and how do we make sure it does

**[27:58]** that we have to check it as it's doing it we have to assure ourselves that it is consistently following these ethical principles at least I mean I'm not sure there's such thing as as optimally but at least as well as a a group of human

**[28:13]** experts are you worried that if you do the default way which is just reinforcing it uh whenever it seems to be following them you could be training deception as well that a straight rein reinforcement has some some some dang

**[28:27]** Danger aspects to it yeah um I think it's actually more robust to do you know check the process of reasoning and check its understanding of Ethics so you know to to reassure ourselves that the system has a really good understanding of

**[28:42]** Ethics it should be you know grilled for for for some time to try to really pull apart its understanding make sure it has a very robust and then also if it's deployed we should have people constantly looking for how you know the

**[28:57]** decisions is making and the reasoning process it goes into those decisions to try to understand how that is correctly reasoning about these types of things speaking of which um do you at Google Deep Mind have some sort of

**[29:10]** framework for no this is this is this is this is not so much a Google Deep Mind perspective on this this is this is my take on how I think we need to do this kind of thing there are there are many different views within and there there

**[29:23]** are different variants on on these sorts of ideas as well so then do you personally think needs to be some sort of framework for as you arrive at certain capabilities these are the concrete safety benchmarks that you must

**[29:34]** have instated at this point or you should you know pause or slow down or something uh I I think that's a sensible thing to do it's actually quite hard to do uh there are some people thinking about I know anthropics is put out some

**[29:45]** things like that we we're thinking about similar things actually you know putting concrete things down is actually quite a hard thing to do so I think it's an important problem and I certainly encourage people to work on it yeah yeah

**[29:58]** um so you know it's you have it's interesting because you have these blog posts that you wrote when you started Deep Mind um you know back in 2008 where you talk about um the motivation was to accelerate safety on net what do you

**[30:12]** think the impact of deep mind has been on safety versus capabilities o interesting I don't know it's hard to hard to judge actually

**[30:28]** you know back in the I I've been worried about AGI safety for a long time well before Deep Mind um but it was it was always really hard to hire people actually particularly in the early days to work

**[30:43]** on AGI safety um thinking back in 201 like 13 or so I think we had the first hire and he only agreed to do it part-time because he didn't want to you know drop all the capabilities work because you know the impact we could

**[30:58]** have as a career and so and this was someone who had already previously been P publishing an A so yeah I don't know it's hard to hard to know what is the counterfactual if we if we weren't weren't there doing it um

**[31:14]** I think you know we have been we've been a group that's been um you know talked about this openly I've I've I've talked about this on many occasions the importance of it um we've been you know hiring people to

**[31:27]** to work on these topics um you know I know a lot of other people in the area and I've talked to them over many many years I've known Dario since 2005 or something around rather you know we've talked on and off about AGI safety

**[31:40]** and so on so I don't know the the impact that deep minders had you know we I guess we were the first I'd say the first AGI company and as a first AGI company we we you know we always had an AGI safety group um we we

**[31:57]** we've been publishing papers in this for many years I think that's lend some credibility to the area when people see oh here's a AGI I mean AGI was a you know there was a fringe term not that long ago and this person doing AGI

**[32:09]** safety well they're a deep mind oh okay I I hope that sort of you know creates some space for people and where do you think AI progress itself would have been without Deep Mind and this is not just a point that people make about de mind I

**[32:23]** think this is a general Point people make about opening eye in anthropic as well that these people went into the business to accelerate safety and sort of the net effect might have been to accelerate capabilities far more right

**[32:33]** right right I think we have accelerated capabilities but again the counterfactuals are quite quite difficult I mean we we didn't do image net for example and image net I think was very influential in in attracting

**[32:47]** investment to the field um we did do Al AO um and that changed some people's minds um but you know the the community is a lot bigger than just deep mind I mean we we have well not so much now but because there

**[33:03]** are a number of other you know players with significant resources but if you went back more than five years in the future we were able to do um bigger projects with bigger teams and take on more ambitious things than than a lot of

**[33:18]** the smaller academic groups right and so the sort of nature of the type of work we could do was a bit different um and that I think that affected the Dynamics in some ways but you know the the the community is much much bigger than say

**[33:31]** deep lines so maybe we've sped things up a bit but I think a lot of these things would have happened before too long anyway I think I think these of often good ideas are kind of in the air and you know as a as

**[33:47]** a researcher you know when sometimes you publish something or you're about to publish something you see somebody else who's got a very similar idea coming out with some good results um I think often it's the time is right right for things

**[33:58]** so you know it's I find it very hard to reason about the counterfactuals there speaking of the early years it's really interesting that in um 2009 you had a blog post where you say my modal expectation of when we get human level

**[34:11]** AI is 2025 expected value is 2028 and this is before deep learning this is when nobody's talking about Ai and it turns out like if you if the trends continue this this is not an unreasonable prediction this was uh how

**[34:24]** did you I mean before all these Trends came into effect how did you have that accurate an estimate well first I'd say it's not before deep learning um deep learning was getting started around 2008 oh sorry I meant to say before image net

**[34:38]** before image net that was 2012 yeah um so well I first formed those beliefs in about 2001 after reading Ray csols the age of spiritual machines and I I came to the conclusion he was he was there was two really important points that in

**[34:59]** in in his book that I I came to believe is true one is that I uh computational Power would grow exponentially for at least a few decades and that the quantity of data in the world would grow exponentially for a few

**[35:12]** decades and when you have exponentially increasing quantities of computation and data then the value of Highly scalable algorithms gets higher and higher so then there's a lot of incentive to make it more scalable algorithm to harness

**[35:28]** all this Computing data and so I thought it would be very likely that we'll start to discover scalable algorithms to do this and then there's a positive feedback between all these things because if your algorithm

**[35:40]** gets better at harnessing Computing data then the value of the data in the compute goes up because it can be more effectively used and so that drives more investment into these areas if your compute performance goes up then the

**[35:53]** value of the data goes up because you can utilize more dat so there are positive of feedback loops between all these things so that was that was the first thing and then the second thing was just looking at the

**[36:03]** trends if these scalable algorithms were were to be discovered then during the 2020s it should be possible to start training models on significantly more data than a human would experience in a lifetime and I figured that that would

**[36:20]** be a time where where big things would start to happen and that would eventually unlock AGI so that was that was my reasoning process and I think we're now at that first part I think we can start training models now where the

**[36:33]** scale of the data is beyond what a human can experience in lifetime so I think this is the first unlocking step and so yeah I think there's a 50% chance that so 2028 now it's just a 50% chance I mean I'm I'm sure what's going to happen

**[36:47]** is going to get to you know 2029 and someone's going to say oh Shane you were wrong it's like come on it's 50 P chance so yeah I I I I think it's it's entirely plausible you it's 50% chance it could happen by 2028 um but

**[37:02]** I'm not going to be surprised if it doesn't happen by then maybe maybe you know the you often hit um unexpected problems and in research and Sciences and sometimes things take longer than you expect if there was a problem that

**[37:14]** caused it if we're in 2029 and it hasn't happened yet looking back what would be the most likely reason that would be the case I don't know I don't know I at the moment it looks to me like all the problems are likely

**[37:34]** solvable with a number of years of research that that's my current sense and what does a time from here to 2028 look like if the 2028 ends up being the year is it is it just we have trillions of dollars of economic impact in the

**[37:47]** meantime and the world gets crazy or what happens I think what you'll see is um the existing models maturing um there'll be less delusional much more factual they'll be more up to dat on what's

**[38:01]** currently going on when they answer questions um they'll become multimodal much more than they currently are um and this will just make them much more useful so I think probably what we'll see more than anything is just um loads

**[38:17]** of great applications um for the for the coming years I think that'll be the there can be some misuse cases as well but I'm sure somebody will come up with you know some something to do with these these

**[38:29]** models that is um quite unhelpful but my expectation for the coming years is mostly a positive one we'll see all kinds of really impressive really amazing applications um for the for the for the

**[38:41]** coming years yeah and on the safety point you mentioned these different research directions that are out there and that you are doing internally in Deep Mind as well in durability rif and so on which are you most optimistic

**[38:55]** about [Music] um I don't know I don't want to pick favorites it's hard picking favorites I know the people working on all these areas

**[39:09]** um I think I think things of the sort of system too flavor um there's there's a there's a um a work we have going on that Jeffrey Irving um leads um called deliberative dialogue which kind of has

**[39:22]** the system to flavor where you have um the sort of um debate takes place about um the actions that an agent could take or what's the correct answer to something or something like this and people then can sort of review these

**[39:38]** these debates and so on and they they use these sort of these AI algorithms to help them judge the the correct outcomes and so on and so this is sort of meant to be a way in which to try to scale um the the alignment um to sort of

**[39:53]** increasingly powerful systems so I think things of that kind of flavor um I think have quite a lot of Promise in in in my opinion but that's kind of quite a broad category res there are many different topics within that that's interesting so

**[40:07]** you mentioned two two two areas in which LM need to improve one is thetic memory and the other is assistant to thinking are those two related or are they two separate are are they two separate um

**[40:22]** drawbacks I I think they're fairly separate but they they can can be somewhat related so you can learn different ways of thinking through problems and actually learn about this rapidly using your episodic memory so

**[40:36]** all these different systems and subsystems interact so they they're never completely separate but I think conceptually you can probably think of them as as quite quite separate things I think delusions and factuality is

**[40:46]** another area uh that's that's going to be quite important um and particularly important in lots of applications you know if you want a model that writes you know creative poetry then that's fine because you want to be able to be very

**[40:59]** free to suggest all kinds of possibilities and so you're not really constrained by a specific reality whereas if you want something that's in a in a in a particular application normally you have to be quite concrete

**[41:11]** about you know what's currently going on and what is true and what is not true and so on and models are a little bit sort of freewheeling when it comes to um you know truth and creativity at the moment and that I think limits their

**[41:22]** applications in many ways so final question is this you've been in this field for over a decade much longer than many others um and you've seen these different landmarks image net Transformers what do you think the next

**[41:38]** Landmark will look like I think the next Landmark that people will REM will think back to and remember is going much more fully multimodal I think because I think that will that'll open out the the sort of

**[41:57]** understanding that you see in language models into a much larger space of possibilities and when people think back they'll think about oh those oldfashioned models they they just did like chat they just did text you know it

**[42:09]** was it just felt like a very narrow thing whereas now they you know they understand when you talk to them and they they understand images and pictures and video and and you can show them things or things like that and they they

**[42:20]** will have much more understanding of what's going on and it'll feel like the system's kind of opened up into the world and and in in in a much more powerful way do you mind if f a follow up on that so Chad GPT just released

**[42:32]** their multimodal feature and then you in Deep Mind you had the GTO paper where you know you can you have this one model you can images even actions video games whatever you can throw in there um and so far it doesn't seem to have been it

**[42:45]** hasn't percolated as much as even like Chad GPT initially from gpt3 or something what explains that is it just that people haven't learned to use multimodality they're not powerful enough yet uh I think it's early days um

**[42:56]** um I think there's you can see promise there understanding images and things more and more but I think it's yeah it's early days in this transition uh is when you start really digesting a lot of video and other things like that that

**[43:09]** the systems will start having a much more grounded understanding of the world and all kinds of other aspects and then when that works well that will open up naturally lots and lots of new new applications and all sorts of new

**[43:22]** possibilities because you're not confined to text chat anymore the new AB of training data as well right yeah new training data new and all kinds of different applications that aren't just purely textual anymore um and you know

**[43:35]** what are those applications well probably a lot of them we can't even imagine at the moment because there are just so many so many possibilities once you can start dealing with all sorts of different modalities in a consistent way

**[43:46]** awesome Shane I think that's actually place to leave it off thank you so much for coming on the podcast thank you hey everybody I hope you enjoy that episode as always the most helpful thing you can do is just share the podcast send it to

**[43:59]** people you think might enjoy it put it in Twitter your group chats Etc just splits the world appreciate you listening I'll see you next time [Music] cheers
