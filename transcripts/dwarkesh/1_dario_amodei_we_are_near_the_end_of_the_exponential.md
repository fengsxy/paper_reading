---
layout: default
type: transcript
series: dwarkesh
episode: 1
guest: ""
title: "Dario Amodei — “We are near the end of the exponential”"
source_url: "https://www.youtube.com/watch?v=n1E9IZfvGMA"
analysis_url: /transcripts/dwarkesh/1_dario_amodei_we_are_near_the_end_of_the_exponential.analysis/
permalink: /transcripts/dwarkesh/1_dario_amodei_we_are_near_the_end_of_the_exponential/
---

# Transcript: EP0 - Dario Amodei — “We are near the end of the exponential”

Source: https://www.youtube.com/watch?v=n1E9IZfvGMA

---

**[00:00]** So, we talked three years ago.
**[00:02]** I'm curious, in your view,
**[00:03]** what has been the biggest update of the last three years?
**[00:05]** What has been the biggest difference between
**[00:06]** what it felt like last three years versus now?
**[00:08]** Yeah. I would say, actually,
**[00:10]** the underlying technology,
**[00:12]** like the exponential of the technology,
**[00:14]** has gone, broadly speaking,
**[00:17]** I would say, about as I expected it to go.
**[00:19]** I mean, there's plus or minus a couple.
**[00:22]** There's plus or minus a year or two here.
**[00:24]** There's plus or minus a year or two there.
**[00:26]** I don't know that I would have predicted
**[00:27]** the specific direction of code.
**[00:30]** But actually, when I look at the exponential,
**[00:33]** it is roughly what I
**[00:36]** expected in terms of the march of the models,
**[00:38]** from smart high school student to smart college student,
**[00:41]** to beginning to do PhD and professional stuff,
**[00:44]** and in the case of code, reaching beyond that.
**[00:47]** So, the frontier is a little bit uneven.
**[00:49]** It's roughly what I expected.
**[00:50]** I will tell you, though, what
**[00:52]** the most surprising thing has been.
**[00:53]** The most surprising thing has been
**[00:55]** the lack of public recognition of
**[00:58]** how close we are to the end of the exponential.
**[01:01]** To me, it is absolutely wild that you have people,
**[01:07]** within the bubble and outside the bubble,
**[01:09]** but you have people talking about these,
**[01:12]** just the same tired old hot button political issues,
**[01:16]** and around us, we're near the end of the exponential.
**[01:21]** I want to understand what
**[01:23]** that exponential looks like right now,
**[01:25]** because the first question I asked you,
**[01:26]** when we recorded three years ago,
**[01:28]** was what's up with scaling?
**[01:29]** How does it work? I have a similar question now,
**[01:33]** but I feel like it's a more complicated question
**[01:34]** because at least from the public's point of view.
**[01:36]** Yes. Three years ago, there were
**[01:38]** these well-known public trends
**[01:41]** where across many orders of magnitude of compute,
**[01:43]** you could see how the loss improves.
**[01:44]** Now, we have RL scaling,
**[01:46]** and there's no publicly known scaling law for it.
**[01:49]** It's not even clear what exactly the story is of,
**[01:52]** is it supposed to be teaching the model skills?
**[01:54]** Is it supposed to be teaching meta-learning?
**[01:55]** What is the scaling hypothesis at this point?
**[01:58]** Yes. I have actually the same hypothesis that I
**[02:02]** had even all the way back in 2017.
**[02:05]** In 2017, I think I talked about it last time,
**[02:07]** but I wrote a doc called The Big Blob of Compute Hypothesis.
**[02:12]** It wasn't about the scaling of language models in particular.
**[02:15]** When I wrote it, GPT-1 had just come out.
**[02:19]** That was one among many things.
**[02:22]** Back in those days, there was robotics.
**[02:24]** People tried to work on reasoning as
**[02:26]** a separate thing from language models.
**[02:28]** There was scaling of the RL that happened in AlphaGo,
**[02:33]** and that happened at Dota, at OpenAI,
**[02:36]** and people remember StarCraft at DeepMind, the AlphaStar.
**[02:42]** It was written as a more general document.
**[02:45]** The specific thing I said was the following.
**[02:49]** Rich Sutton put out the bitter lesson a couple of years later,
**[02:53]** but the hypothesis is basically the same.
**[02:57]** What it says is all the cleverness,
**[03:00]** all the techniques,
**[03:01]** all the we need a new method to do something like that,
**[03:05]** doesn't matter very much.
**[03:06]** There are only a few things that matter,
**[03:08]** and I think I listed seven of them.
**[03:10]** One is how much raw compute you have.
**[03:13]** The other is the quantity of data that you have.
**[03:16]** Then the third is the quality and distribution of data.
**[03:20]** It needs to be a broad distribution of data.
**[03:23]** The fourth is, I think,
**[03:24]** how long you train for.
**[03:26]** The fifth is you need
**[03:28]** an objective function that can scale to the moon.
**[03:31]** The pre-training objective function
**[03:33]** is one such objective function.
**[03:36]** Another objective function is the RL objective function
**[03:41]** that says you have a goal,
**[03:42]** you're going to go out and reach the goal.
**[03:44]** Within that, of course, there's objective rewards
**[03:47]** like you see in math and coding,
**[03:49]** and there's more subjective rewards
**[03:51]** like you see in RL from human feedback
**[03:53]** or higher-order versions of that.
**[03:56]** Then the sixth and seventh were things
**[03:59]** around normalization or conditioning,
**[04:02]** like just getting the numerical stability
**[04:04]** so that the big blob of compute flows
**[04:07]** in this laminar way instead of running into problems.
**[04:11]** That was the hypothesis,
**[04:13]** and it's a hypothesis I still hold.
**[04:15]** I don't think I've seen very much
**[04:17]** that is not in line with that hypothesis.
**[04:20]** And so the pre-training scaling laws
**[04:22]** were one example of kind of what we see there.
**[04:26]** And indeed, those have continued going.
**[04:29]** Like, you know, I think now it's been widely reported,
**[04:33]** like, you know, we feel good about pre-training,
**[04:35]** like pre-training is continuing to give us gains.
**[04:39]** What has changed is that now
**[04:41]** we're also seeing the same thing for RL, right?
**[04:44]** So we're seeing a pre-training phase,
**[04:46]** and then we're seeing like an RL phase on top of that.
**[04:50]** And with RL, it's actually just the same.
**[04:54]** Like, you know, even other companies have published,
**[04:59]** like, you know, in some of their releases
**[05:02]** have published things that say,
**[05:04]** look, you know, we train the model on math contests,
**[05:06]** you know, AIME or the kind of other things,
**[05:10]** and, you know, how well the model does
**[05:13]** is log linear and how long we've trained it.
**[05:15]** And we see that as well.
**[05:17]** And it's not just math contests,
**[05:18]** it's a wide variety of RL tasks.
**[05:21]** And so we're seeing the same scaling in RL
**[05:24]** that we saw for pre-training.
**[05:27]** You mentioned Richard Sutton and the bitter lesson.
**[05:29]** Yeah.
**[05:30]** I interviewed him last year,
**[05:31]** and he is actually very non-LLM-pilled.
**[05:35]** And if I'm, I don't know if this is his perspective,
**[05:38]** but one way to paraphrase this objection
**[05:41]** is something like, look,
**[05:42]** something which possesses the true core of human learning
**[05:45]** would not require all these billions of dollars
**[05:48]** of data and compute and these bespoke environments
**[05:51]** to learn how to use Excel or how to use PowerPoint,
**[05:56]** how to navigate a web browser.
**[05:57]** And the fact that we have to build in these skills
**[06:00]** using these RL environments hints
**[06:03]** that we're actually lacking this core human learning
**[06:08]** algorithm, and so we're scaling the wrong thing.
**[06:12]** And so, yeah, that does raise the question,
**[06:13]** why are we doing all this RL scaling
**[06:14]** if we do think there's something that's going to be human
**[06:16]** like in its ability to learn on the fly?
**[06:18]** Yeah, yeah.
**[06:19]** So I think this kind of puts together several things
**[06:23]** that should be kind of thought of differently.
**[06:25]** Yeah.
**[06:26]** I think there is a genuine puzzle here,
**[06:29]** but it may not matter.
**[06:31]** In fact, I would guess it probably doesn't matter.
**[06:34]** So let's take the RL out of it for a second,
**[06:37]** because I actually think RL,
**[06:38]** and it's a red herring to say that RL
**[06:40]** is any different from pre-training in this matter.
**[06:43]** So if we look at pre-training scaling,
**[06:46]** it was very interesting back in 2017
**[06:50]** when Alec Radford was doing GPT-1.
**[06:53]** If you look at the models before GPT-1,
**[06:56]** they were trained on these datasets
**[06:59]** that didn't represent a wide distribution of text, right?
**[07:04]** You had like these very standard
**[07:07]** kind of language modeling benchmarks,
**[07:09]** and GPT-1 itself was trained on a bunch of,
**[07:11]** I think it was fan fiction actually,
**[07:14]** but it was like literary, it was like literary text,
**[07:17]** which is a very small fraction of the text that you get.
**[07:19]** And what we found with that,
**[07:21]** and in those days it was like a billion words or something,
**[07:23]** so small datasets
**[07:25]** and represented a pretty narrow distribution, right?
**[07:29]** Like a narrow distribution of kind of what you can see
**[07:33]** in the world.
**[07:34]** And it didn't generalize well.
**[07:35]** If you did better on, you know,
**[07:40]** I forgot what it was,
**[07:41]** some kind of fan fiction corpus,
**[07:43]** it wouldn't generalize that well
**[07:45]** to kind of the other tasks.
**[07:46]** You know, we had all these measures of like,
**[07:48]** you know, how well does the model do
**[07:51]** at predicting all of these other kinds of texts?
**[07:53]** You really didn't see the generalization.
**[07:55]** It was only when you trained over all the tasks
**[07:58]** on the internet,
**[07:59]** when you kind of did a general internet scrape, right?
**[08:02]** From something like, you know,
**[08:04]** common crawl or scraping links on Reddit,
**[08:06]** which is what we did for GPT-2.
**[08:08]** It's only when you do that,
**[08:09]** that you kind of started to get generalization.
**[08:13]** And I think we're seeing the same thing on RL,
**[08:15]** that we're starting with first very simple RL tasks,
**[08:19]** like training on math competitions.
**[08:21]** Then we're kind of moving to, you know,
**[08:23]** kind of broader training
**[08:25]** that involves things like code as a task.
**[08:27]** And now we're moving to do kind of many other tasks.
**[08:31]** And then I think we're going
**[08:32]** to increasingly get generalization.
**[08:35]** So that kind of takes out the RL
**[08:37]** versus the pre-training side of it.
**[08:39]** But I think there is a puzzle here either way,
**[08:41]** which is that on pre-training,
**[08:43]** when we train the model on pre-training,
**[08:47]** you know, we use like trillions of tokens, right?
**[08:50]** And humans don't see trillions of words.
**[08:52]** So there is an actual sample efficiency difference here.
**[08:55]** There is actually something different
**[08:57]** that's happening here,
**[08:59]** which is that the models start from scratch
**[09:01]** and, you know, they have to get much more training.
**[09:06]** But we also see that once they're trained,
**[09:08]** if we give them a long context length,
**[09:10]** the only thing blocking a long context length
**[09:12]** is like inference.
**[09:13]** But if we give them like a context length of a million,
**[09:16]** they're very good at learning
**[09:17]** and adapting within that context length.
**[09:19]** And so I don't know the full answer to this,
**[09:23]** but I think there's something going on that pre-training,
**[09:26]** it's not like the process of humans learning.
**[09:30]** It's somewhere between the process of humans learning
**[09:32]** and the process of human evolution.
**[09:34]** It's like, it's somewhere between,
**[09:36]** like we get many of our priors from evolution.
**[09:39]** Our brain isn't just a blank slate, right?
**[09:41]** Whole books have been written about.
**[09:42]** I think the language models, they're much more blank slates.
**[09:45]** They literally start as like random weights.
**[09:47]** Whereas the human brain starts with all these regions,
**[09:50]** it's connected to all these inputs and outputs.
**[09:53]** And so maybe we should think of pre-training
**[09:56]** and for that matter, RL as well,
**[09:59]** as being something that exists in the middle space
**[10:02]** between human evolution and kind of human on the spot learning
**[10:08]** and as the in-context learning that the models do
**[10:13]** as something between long-term human learning
**[10:16]** and short-term human learning.
**[10:17]** So there's this hierarchy of like there's evolution,
**[10:21]** there's long-term learning, there's short-term learning
**[10:23]** and there's just human reaction.
**[10:25]** The LOM phases exist along this spectrum
**[10:28]** but not necessarily exactly at the same points.
**[10:32]** There's no analog to some of the human modes of learning.
**[10:35]** The LOMs are kind of falling between the points.
**[10:38]** Does that make sense?
**[10:39]** Yes, although some things are still a bit confusing.
**[10:42]** For example, if the analogy is that this is like evolution,
**[10:45]** so it's fine that it's not that sample efficient,
**[10:47]** then like, well, if we're gonna get
**[10:49]** the kind of super sample efficient agent
**[10:51]** from in-context learning,
**[10:53]** why are we bothering to build in,
**[10:55]** there's RL environment companies which are,
**[10:57]** it seems like what they're doing
**[10:58]** is they're teaching it how to use this API,
**[11:00]** how to use Slack, how to use whatever.
**[11:02]** It's confusing to me why there's so much emphasis on that
**[11:05]** if the kind of agent that can just learn on the fly
**[11:08]** is emerging or is gonna soon emerge or has already emerged.
**[11:10]** Yeah, yeah, so I mean, I can't speak for the emphasis
**[11:12]** of anyone else.
**[11:13]** I can only talk about how we think about it.
**[11:17]** I think the way we think about it is
**[11:20]** the goal is not to teach the model every possible skill
**[11:24]** within RL, just as we don't do that within pre-training.
**[11:27]** Within pre-training, we're not trying to expose the model
**[11:30]** to every possible way that words could be put together.
**[11:36]** It's rather that the model trains on a lot of things
**[11:39]** and then it reaches generalization across pre-training.
**[11:43]** That was the transition from GPT-1 to GPT-2
**[11:47]** that I saw up close,
**[11:48]** which is like the model reaches a point.
**[11:52]** I like had these moments where I was like,
**[11:55]** oh yeah, you just give the model a list of numbers
**[11:59]** that's like this is the cost of the house,
**[12:02]** this is the square feet of the house
**[12:04]** and the model completes the pattern
**[12:06]** and does linear regression.
**[12:07]** Like not great, but it does it,
**[12:08]** but it's never seen that exact thing before.
**[12:11]** And so to the extent that we are building
**[12:15]** these RL environments, the goal is very similar
**[12:19]** to what was done five or 10 years ago with pre-training
**[12:24]** with we're trying to get a whole bunch of data,
**[12:28]** not because we wanna cover a specific document
**[12:31]** or a specific skill, but because we wanna generalize.
**[12:35]** I mean, I think the framework you're laying down
**[12:39]** obviously makes sense.
**[12:40]** Like we're making progress towards AGI.
**[12:42]** I think the crux is something like,
**[12:44]** nobody at this point disagrees
**[12:45]** that we're gonna achieve AGI in the century.
**[12:47]** And the crux is you say we're hitting the end
**[12:49]** of the exponential and somebody else looks at this and says,
**[12:54]** oh yeah, we're making progress.
**[12:56]** We've been making progress since 2012
**[12:57]** and then 2035, we'll have a human like agent.
**[13:00]** And so I wanna understand what it is that you're seeing,
**[13:02]** which makes you think, yeah, obviously we're seeing
**[13:05]** the kinds of things that evolution did
**[13:07]** or that within the human lifetime learning
**[13:09]** is like in these models.
**[13:10]** And why think that it's one year away and not 10 years away?
**[13:14]** I actually think of it as like two,
**[13:17]** there's kind of two cases to be made here,
**[13:19]** or like two claims you could make,
**[13:21]** one of which is like stronger
**[13:23]** and the other of which is weaker.
**[13:25]** So I think starting with the weaker claim,
**[13:28]** when I first saw the scaling back in like 2019,
**[13:35]** I wasn't sure, this was the whole,
**[13:37]** this was kind of a 50-50 thing, right?
**[13:39]** I thought I saw something that was,
**[13:41]** and my claim was this is much more likely
**[13:44]** than anyone thinks it is.
**[13:45]** Like this is wild, no one else would even consider this.
**[13:48]** Maybe there's a 50% chance this happens.
**[13:51]** On the basic hypothesis of, as you put it,
**[13:54]** within 10 years, we'll get to what I call
**[13:59]** kind of country of geniuses in a data center.
**[14:02]** I'm at like 90% on that.
**[14:04]** And it's hard to go much higher than 90%
**[14:06]** because the world is so unpredictable.
**[14:09]** Maybe the irreducible uncertainty would be
**[14:11]** if we were at 95% where you get to things like,
**[14:15]** I don't know, maybe multiple companies
**[14:17]** have kind of internal turmoil and nothing happens,
**[14:21]** and then Taiwan gets invaded
**[14:23]** and like all the fabs get blown up by missiles,
**[14:26]** and then-
**[14:27]** Now you're getting to scenario.
**[14:28]** Yeah, yeah, yeah, you know,
**[14:29]** just you could construct a scenario
**[14:31]** where there's like a 5% chance that it,
**[14:34]** or you can construct a 5% world
**[14:36]** where like things get delayed for 10 years.
**[14:42]** That's maybe 5%.
**[14:43]** There's another 5%, which is that
**[14:46]** I'm very confident on tasks that can be verified.
**[14:49]** So I think with coding,
**[14:51]** I'm just, except for that irreducible uncertainty,
**[14:53]** there's just, I mean,
**[14:54]** I think we'll be there in one or two years.
**[14:55]** There's no way we will not be there in 10 years
**[14:58]** in terms of being able to do it end-to-end coding.
**[15:00]** My one little bit, the one little bit
**[15:03]** of fundamental uncertainty, even on long timescales,
**[15:07]** is this thing about tasks that aren't verifiable,
**[15:09]** like planning a mission to Mars,
**[15:12]** like doing some fundamental scientific discovery
**[15:16]** like CRISPR, like writing a novel.
**[15:21]** Hard to verify those tasks.
**[15:23]** I am almost certain that we have a reliable path
**[15:28]** to get there, but like if there was a little bit
**[15:31]** of uncertainty, it's there.
**[15:33]** So on the 10 years, I'm like 90%,
**[15:38]** which is about as certain as you can be.
**[15:39]** Like, I think it's crazy to say
**[15:43]** that this won't happen by 2035.
**[15:45]** Like in some sane world,
**[15:47]** it would be outside the mainstream.
**[15:49]** But the emphasis on verification hints to me
**[15:53]** as a lack of belief that these models are generalized.
**[15:58]** If you think about humans,
**[16:00]** we are good at things that both,
**[16:01]** which we get a verifiable reward
**[16:03]** and things which we don't.
**[16:04]** You're like, you haven't just started.
**[16:05]** No, no, no, this is why I'm almost sure.
**[16:07]** We already see substantial generalization
**[16:09]** from things that verify to things that don't verify.
**[16:13]** We're already seeing that.
**[16:13]** Right, but it seems like you were emphasizing this
**[16:15]** as a spectrum which will split apart,
**[16:19]** which means we see more progress.
**[16:20]** And I'm like, but that doesn't seem
**[16:22]** like how humans get better.
**[16:23]** The world in which we don't make it
**[16:24]** or the world in which we don't get there
**[16:27]** is the world in which we do all the things
**[16:29]** that are verifiable.
**[16:31]** And then they like, you know, many of them generalize,
**[16:34]** but what we kind of don't get fully there.
**[16:36]** We don't fully, you know,
**[16:38]** we don't fully color in this side of the box.
**[16:41]** It's not a binary thing.
**[16:43]** But it also seems to me,
**[16:44]** even if we're in the world where generalization is weak
**[16:46]** when you only say verifiable domains,
**[16:48]** it's not clear to me in such a world
**[16:49]** you could automate software engineering
**[16:51]** because software, like in some sense,
**[16:53]** you are quote unquote a software engineer.
**[16:56]** But part of being a software engineer for you
**[16:58]** involves writing these like long memos
**[16:59]** about your grand vision about different things.
**[17:01]** And so-
**[17:02]** Well, I don't think that's part of the job of SWE.
**[17:03]** That's part of the job of the company.
**[17:04]** But I do think SWE involves like design documents
**[17:07]** and other things like that.
**[17:09]** Which by the way, the models are not bad.
**[17:11]** They're already pretty good at writing comments.
**[17:13]** And so with, again, I'm making like much weaker claims here
**[17:17]** than I believe to like, you know,
**[17:19]** to kind of set up a, you know,
**[17:22]** to distinguish between two things.
**[17:23]** Like we're already almost there for software engineering.
**[17:26]** We are already almost there.
**[17:28]** By what metric?
**[17:29]** There's one metric which is like
**[17:30]** how many lines of code are written by AI.
**[17:31]** And if you use,
**[17:32]** if you consider other productivity improvements
**[17:34]** in the course of the history of software engineering,
**[17:36]** compilers write all the lines of software.
**[17:38]** And, but we, there's a difference
**[17:40]** between how many lines are written
**[17:41]** and how big the productivity improvement is.
**[17:42]** Oh yeah, so-
**[17:44]** And then like, we're almost there,
**[17:45]** meaning like how big is the productivity improvement,
**[17:48]** not just how many lines are written.
**[17:49]** Yeah, yeah.
**[17:50]** So I actually, I actually agree with you on this.
**[17:53]** So I've made this series of predictions
**[17:55]** on code and software engineering.
**[17:58]** And I think people have repeatedly
**[18:00]** kind of misunderstood them.
**[18:01]** So let me lay out the spectrum, right?
**[18:05]** Like, I think it was like, you know, like, you know,
**[18:07]** eight or nine months ago or something,
**[18:09]** I said, you know,
**[18:10]** the AI model will be writing 90% of the lines of code
**[18:14]** in like, you know, three to six months,
**[18:16]** which happened at least at some places, right?
**[18:19]** Happened at Anthropic,
**[18:21]** happened with many people downstream using our models.
**[18:24]** But that's actually a very weak criterion, right?
**[18:27]** People thought I was saying like,
**[18:29]** we won't need 90% of the software engineers.
**[18:31]** Those things are worlds apart, right?
**[18:33]** Like I would put the spectrum
**[18:35]** as 90% of code is written by the model.
**[18:39]** 100% of code is written by the model.
**[18:41]** And that's a big difference in productivity.
**[18:43]** 90% of the end-to-end suite tasks, right?
**[18:47]** Including things like compiling,
**[18:49]** including things like setting up clusters
**[18:52]** and environments, testing features, writing memos,
**[18:54]** 90% of the suite tasks are written by the models.
**[18:57]** 100% of today's suite tasks are written by the models.
**[19:02]** And even when that happens,
**[19:03]** doesn't mean software engineers are out of a job.
**[19:05]** Like there's like new higher level things they can do,
**[19:08]** where they can manage.
**[19:10]** And then there's a further down the spectrum,
**[19:11]** like, you know, there's 90% less demand for suites,
**[19:15]** which I think will happen.
**[19:16]** But like, this is a spectrum.
**[19:18]** And, you know, I wrote about it
**[19:20]** in the adolescence of technology,
**[19:22]** where I went through this kind of spectrum with farming.
**[19:26]** And so I actually totally agree with you on that.
**[19:29]** It's just, these are very different benchmarks
**[19:31]** from each other,
**[19:32]** but we're proceeding through them super fast.
**[19:34]** It seems like in part of Eurovision,
**[19:35]** it's like going from 90 to 100.
**[19:38]** First, it's going to happen fast.
**[19:39]** And two, that somehow that leads
**[19:42]** to huge productivity improvements.
**[19:45]** Whereas when I noticed, even in Greenfield projects
**[19:47]** that people start with cloud code or something,
**[19:50]** people report starting a lot of projects.
**[19:51]** And I'm like, do we see in the world out there
**[19:54]** a renaissance of software,
**[19:56]** all these new features that wouldn't exist otherwise?
**[19:57]** And at least so far, it doesn't seem like we see that.
**[20:00]** And so that does make me wonder,
**[20:01]** even if like I never had to intervene on cloud code,
**[20:05]** there is this thing of like, there's just,
**[20:08]** the world is complicated, jobs are complicated,
**[20:10]** and closing the loop on self-contained systems,
**[20:14]** whether it's just writing software or something,
**[20:15]** how much sort of, how much broader gains
**[20:18]** we would see just from that.
**[20:20]** And so maybe that makes us,
**[20:21]** this would dilute our estimation of the country of geniuses.
**[20:24]** Well, I actually, I like simultaneously,
**[20:29]** I simultaneously agree with you,
**[20:31]** agree that it's a reason
**[20:33]** why these things don't happen instantly.
**[20:35]** But at the same time, I think the effect
**[20:38]** is going to be very fast.
**[20:40]** So like, I don't know, you can have these two poles, right?
**[20:42]** One is like, you know, AI is like, you know,
**[20:46]** it's not going to make progress.
**[20:47]** It's slow, like it's going to take, you know,
**[20:50]** kind of forever to diffuse within the economy, right?
**[20:52]** Economic diffusion has become one of these buzzwords
**[20:54]** that's like a reason why we're not going to make AI progress
**[20:58]** or why AI progress doesn't matter.
**[20:59]** And, you know, the other axis is like,
**[21:01]** we'll get recursive self-improvement, you know,
**[21:03]** the whole thing, you know,
**[21:05]** can't you just draw an exponential line on the curve?
**[21:07]** You know, it's good.
**[21:08]** We're going to have, you know, Dyson spheres around the sun
**[21:10]** in like, you know, so many nanoseconds after, you know,
**[21:16]** after we get recursive.
**[21:17]** I mean, I'm completely caricaturing the view here,
**[21:20]** but like, you know, there are these two extremes,
**[21:23]** but what we've seen from the beginning, you know,
**[21:26]** at least if you look within Anthropic,
**[21:28]** there's this bizarre 10X per year growth
**[21:32]** in revenue that we've seen, right?
**[21:34]** So, you know, in 2023, it was like zero to 100 million.
**[21:38]** 2024, it was 100 million to a billion.
**[21:41]** 2025, it was a billion to like nine or 10 billion.
**[21:46]** You guys should have just bought like a billion dollars
**[21:47]** with your own products
**[21:48]** so you could just like have a clean 10B.
**[21:50]** And the first month of this year, like that exponential,
**[21:54]** you would think it would slow down,
**[21:55]** but it was like, you know, we added another few billion
**[21:58]** to like, you know, we added another few billion
**[22:01]** to revenue in January.
**[22:04]** And so, you know, obviously that curve
**[22:06]** can't go on forever, right?
**[22:08]** You know, the GDP is only so large.
**[22:10]** I don't, you know, I would even guess
**[22:12]** that it bends somewhat this year,
**[22:15]** but like that is like a fast curve, right?
**[22:18]** That's like a really fast curve.
**[22:21]** And I would bet it stays pretty fast
**[22:23]** even as the scale goes to the entire economy.
**[22:25]** So like, I think we should be thinking
**[22:27]** about this middle world where things are like extremely fast
**[22:33]** but not instant, where they take time
**[22:35]** because of economic diffusion,
**[22:37]** because of the need to close the loop,
**[22:39]** because, you know, it's like this fiddly,
**[22:42]** oh man, I have to do change management within my enterprise.
**[22:45]** You know, I have to like, you know,
**[22:48]** you know, I like, I set this up,
**[22:50]** but, you know, I have to change the security permissions
**[22:52]** on this in order to make it actually work.
**[22:54]** Or, you know, I had this like old piece of software
**[22:58]** that, you know, that like, you know,
**[22:59]** checks the model before it's compiled and like released
**[23:02]** and I have to rewrite it.
**[23:03]** And yes, the model can do that,
**[23:05]** but I have to tell the model to do that.
**[23:06]** And it has to, it has to take time to do that.
**[23:09]** And so I think everything we've seen so far
**[23:13]** is compatible with the idea
**[23:15]** that there's one fast exponential
**[23:18]** that's the capability of the model.
**[23:20]** And then there's another fast exponential
**[23:22]** that's downstream of that,
**[23:23]** which is the diffusion of the model into the economy.
**[23:26]** Not instant, not slow,
**[23:29]** much faster than any previous technology,
**[23:32]** but it has its limits.
**[23:34]** And this is what we, you know,
**[23:36]** when I look inside Anthropic,
**[23:39]** when I look at our customers,
**[23:40]** fast adoption, but not infinitely fast.
**[23:44]** Can I try a hot take on you?
**[23:45]** Yeah.
**[23:46]** I feel like diffusion is cope
**[23:47]** that people use to say when it's like,
**[23:49]** if the model isn't able to do something,
**[23:51]** they're like, oh, but it's like a diffusion issue.
**[23:54]** But then you should use the comparison to humans.
**[23:56]** You would think that the inherent advantages
**[23:58]** that AIs have would make diffusion a much easier problem
**[24:02]** for new AIs getting onboarded
**[24:04]** than new humans getting onboarded.
**[24:05]** So an AI can read your entire Slack
**[24:07]** and your drive in minutes.
**[24:09]** They can share all the knowledge
**[24:10]** that the other copies of the same instance have.
**[24:12]** You don't have this adverse selection problem
**[24:13]** when you're hiring AIs
**[24:14]** because you can just hire copies of a vetted AI model.
**[24:17]** Hiring a human is like so much more hassle
**[24:20]** and people hire humans all the time, right?
**[24:21]** We pay humans upwards of $50 trillion in wages
**[24:24]** because they're useful,
**[24:25]** even though it's like, in principle,
**[24:28]** it would be much easier to integrate AIs into the economy
**[24:30]** than it is to hire humans.
**[24:32]** I think like the diffusion, I feel like,
**[24:33]** doesn't really explain.
**[24:34]** I think diffusion is very real.
**[24:38]** And doesn't exclusively have to do
**[24:42]** with limitations on the AI models.
**[24:46]** Like, again, there are people who use diffusion
**[24:49]** as kind of a buzzword to say this isn't a big deal.
**[24:52]** I'm not talking about that.
**[24:53]** I'm not talking about AI will diffuse
**[24:56]** at the speed that previous.
**[24:58]** I think AI will diffuse much faster
**[25:00]** than previous technologies have, but not infinitely fast.
**[25:03]** So I'll just give an example of this, right?
**[25:06]** There's like Claude Code.
**[25:07]** Like Claude Code is extremely easy to set up.
**[25:11]** If you're a developer,
**[25:11]** you can kind of just start using Claude Code.
**[25:14]** There is no reason why a developer at a large enterprise
**[25:17]** should not be adopting Claude Code as quickly
**[25:21]** as individual developer or developer at a startup.
**[25:24]** And we do everything we can to promote it, right?
**[25:27]** We sell Claude Code to enterprises and big enterprises,
**[25:32]** like big financial companies,
**[25:34]** big pharmaceutical companies, all of them.
**[25:37]** They're adopting Claude Code much faster
**[25:40]** than enterprises typically adopt new technology, right?
**[25:45]** But again, it takes time.
**[25:48]** Like any given feature or any given product
**[25:52]** like Claude Code or like Cowork will get adopted
**[25:55]** by the individual developers who are on Twitter all the time
**[25:59]** by the like series A startups many months faster
**[26:03]** than they will get adopted by like a large enterprise
**[26:09]** that does food sales.
**[26:11]** There are a number of factors.
**[26:13]** Like you have to go through legal,
**[26:14]** you have to provision it for everyone.
**[26:16]** It has to pass security and compliance.
**[26:20]** The leaders of the company who are further away
**[26:23]** from the AI revolution are forward-looking,
**[26:26]** but they have to say,
**[26:27]** oh, it makes sense for us to spend 50 million.
**[26:31]** This is what this Claude Code thing is.
**[26:33]** This is why it helps our company.
**[26:35]** This is why it makes us more productive.
**[26:36]** And then they have to explain to the people
**[26:38]** two levels below and they have to say,
**[26:40]** okay, we have 3000 developers,
**[26:42]** like here's how we're gonna roll it out to our developers.
**[26:44]** And we have conversations like this every day.
**[26:47]** Like, we are doing everything we can
**[26:50]** to make Anthropx revenue grow 20 or 30 X a year
**[26:53]** instead of 10 X a year.
**[26:56]** And again, many enterprises are just saying,
**[26:59]** this is so productive,
**[27:01]** like we're gonna take shortcuts
**[27:03]** in our usual procurement process, right?
**[27:05]** They're moving much faster than when we tried to sell them
**[27:08]** just the ordinary API, which many of them use,
**[27:10]** but Claude Code is a more compelling product.
**[27:13]** But it's not an infinitely compelling product.
**[27:15]** And I don't think even AGI or Powerful AI
**[27:18]** or Country of Geniuses in the data center
**[27:20]** will be an infinitely compelling product.
**[27:22]** It will be a compelling product enough
**[27:24]** maybe to get three or five or 10 X a year growth,
**[27:28]** even when you're in the hundreds of billions of dollars,
**[27:29]** which is extremely hard to do
**[27:31]** and has never been done in history before,
**[27:33]** but not infinitely fast.
**[27:34]** I buy that it would be a slight slowdown
**[27:36]** and maybe this is not your claim,
**[27:37]** but sometimes people talk about this like,
**[27:39]** oh, the capabilities aren't there, but because of diffusion.
**[27:43]** Otherwise, like we're basically at AGI and then-
**[27:45]** I don't believe we're basically at AGI.
**[27:48]** I think if you had the Country of Geniuses
**[27:50]** in a data center,
**[27:51]** if your company didn't adopt the Country of Geniuses
**[27:53]** in a data center, we would know it.
**[27:55]** We would know it if you had the Country of Geniuses
**[27:58]** in a data center.
**[27:59]** Like everyone in this room would know it.
**[28:01]** Everyone in Washington would know it.
**[28:03]** Like, you know, people in rural parts might not know it,
**[28:07]** but like, we would know it.
**[28:10]** We don't have that now, that's very clear.
**[28:12]** As Dario was hinting at, to get generalization,
**[28:15]** you need to train across a wide variety
**[28:17]** of realistic tasks and environments.
**[28:19]** For example, with a sales agent,
**[28:21]** the hardest part isn't teaching it to mash buttons
**[28:24]** in a specific database in Salesforce.
**[28:25]** It's training the agent's judgment
**[28:27]** across ambiguous situations.
**[28:29]** How do you sort through a database with thousands of leads
**[28:31]** to figure out which ones are hot?
**[28:33]** How do you actually reach out?
**[28:34]** What do you do when you get ghosted?
**[28:36]** When an AI lab wanted to train a sales agent,
**[28:38]** Labelbox brought in dozens of Fortune 500 salespeople
**[28:41]** to build a bunch of different RL environments.
**[28:44]** They created thousands of scenarios
**[28:45]** where the sales agent had to engage
**[28:47]** with a potential customer,
**[28:48]** which was role-played by a second AI.
**[28:50]** Labelbox made sure that this customer AI
**[28:52]** had a few different personas,
**[28:54]** because when you cold call,
**[28:55]** you have no idea who's gonna be on the other end.
**[28:57]** You need to be able to deal with
**[28:58]** a whole range of possibilities.
**[29:00]** Labelbox's sales experts monitored these conversations
**[29:03]** turn by turn, tweaking the role-playing agent
**[29:05]** to ensure it did the kinds of things
**[29:07]** an actual customer would do.
**[29:08]** Labelbox could iterate faster
**[29:09]** than anybody else in the industry.
**[29:11]** This is super important because RL is an empirical science.
**[29:14]** It's not a solved problem.
**[29:15]** Labelbox has a bunch of tools
**[29:16]** for monitoring agent performance in real time.
**[29:19]** This lets their experts keep coming up with tasks
**[29:21]** so that the model stays
**[29:22]** in the right distribution of difficulty
**[29:24]** and gets the optimal reward signal during training.
**[29:27]** Labelbox can do this sort of thing in almost every domain.
**[29:29]** They've got hedge fund managers, radiologists,
**[29:32]** even airline pilots.
**[29:33]** So whatever you're working on, Labelbox can help.
**[29:36]** Learn more at labelbox.com slash vorkash.
**[29:42]** Coming back to concrete predictions,
**[29:43]** because I think,
**[29:44]** because there's so many different things to disambiguate,
**[29:47]** it can be easy to talk past each other
**[29:49]** when we're talking about capabilities.
**[29:50]** So for example, when I interviewed you three years ago,
**[29:52]** I asked you a prediction
**[29:54]** about what we should expect three years from now.
**[29:56]** I think you were right.
**[29:57]** So you said we should expect systems.
**[30:00]** which if you talk to them for the course of an hour,
**[30:02]** it's hard to tell them apart
**[30:03]** from a generally well-educated human.
**[30:05]** I think you were right about that.
**[30:06]** And I think spiritually, I feel unsatisfied
**[30:09]** because my internal expectation was that such a system
**[30:13]** could automate large parts of white-collar work.
**[30:15]** And so it might be more productive to talk about
**[30:17]** the actual end capabilities you want such a system.
**[30:20]** So I will basically tell you where I think we are.
**[30:26]** But let me ask it in a very specific question
**[30:27]** so that we can figure out exactly
**[30:30]** what kinds of capabilities we should assume.
**[30:31]** So maybe I'll ask about it in the context
**[30:33]** of a job I understand well,
**[30:35]** not because it's the most relevant job,
**[30:37]** but just because I can evaluate the claims about it.
**[30:40]** Take video editors, right?
**[30:41]** I have video editors.
**[30:43]** And part of their job involves learning
**[30:46]** about our audience's preferences,
**[30:47]** learning about my preferences and tastes
**[30:49]** and the different trade-offs we have,
**[30:50]** and just over the course of many months
**[30:52]** building up this understanding of context.
**[30:54]** And so the skill and ability they have
**[30:56]** six months into the job,
**[30:58]** a model that can pick up that skill on the job, on the fly.
**[31:01]** When should we expect such an AI system?
**[31:03]** Yeah, so I guess what you're talking about is like,
**[31:05]** you know, we're doing this interview for three hours
**[31:08]** and then like, you know, someone's gonna come in,
**[31:10]** someone's gonna edit it.
**[31:11]** They're gonna be like, oh, you know, you know,
**[31:14]** I don't know, Dario, like, you know, scratched his head
**[31:16]** and, you know, we could edit that out and, you know.
**[31:19]** Magnify that.
**[31:20]** There was this like long,
**[31:21]** there was this like long discussion
**[31:23]** that like is less interesting to people.
**[31:24]** And then, you know, then there's other thing
**[31:26]** that's like more interesting to people.
**[31:27]** So, you know, let's kind of make this edit.
**[31:30]** So, you know, I think the country of geniuses
**[31:33]** in a data center will be able to do that.
**[31:35]** The way it will be able to do that is, you know,
**[31:37]** it will have general control of a computer screen, right?
**[31:40]** Like, you know, and you'll be able to feed this in
**[31:43]** and it'll be able to also use the computer screen
**[31:45]** to like go on the web, look at all your previous,
**[31:48]** look at all your previous interviews.
**[31:49]** Like look at what people are saying on Twitter
**[31:51]** in response to your interviews.
**[31:53]** Like talk to you, ask you questions,
**[31:55]** talk to your staff,
**[31:56]** look at the history of kind of edits that you did.
**[31:59]** And from that, like do the job.
**[32:02]** So I think that's dependent on several things.
**[32:04]** One that's dependent,
**[32:05]** and I think this is one of the things
**[32:07]** that's actually blocking deployment,
**[32:10]** getting to the point on computer use
**[32:12]** where the models are really masters
**[32:13]** at using the computer, right?
**[32:15]** And, you know, we've seen this climb in benchmarks
**[32:18]** and benchmarks are always, you know, imperfect measures,
**[32:20]** but like, you know, OS world is, you know,
**[32:23]** went from, you know, like 5%, you know,
**[32:25]** like I think when we first released, you know,
**[32:29]** a computer use like a year and a quarter ago,
**[32:32]** it was like maybe 15%, I don't remember exactly,
**[32:35]** but we've climbed from that to like 65 or 70%.
**[32:39]** And, you know, there may be harder measures as well,
**[32:42]** but I think computer use has to pass a point of reliability.
**[32:46]** Can I just ask a follow-up on that
**[32:47]** before we move on to the next point?
**[32:49]** I often, for years I've been trying to build
**[32:51]** different internal LLM tools for myself.
**[32:53]** And often I have these text in, text out tasks,
**[32:58]** which should be dead center
**[32:59]** in the repertoire of these models.
**[33:00]** And yet I still hire humans to do them
**[33:03]** just because it's, if it's something like make,
**[33:05]** identify what the best clips would be in this transcript,
**[33:07]** and maybe they'll do like a seven out of 10 job at them,
**[33:09]** but there's not this ongoing way I can engage with them
**[33:13]** to help them get better at the job
**[33:14]** the way I could with a human employee.
**[33:16]** And so that missing ability,
**[33:17]** even if you saw computer use,
**[33:19]** would still block my ability to like
**[33:21]** offload an actual job to them.
**[33:23]** Again, this gets back to what we were talking about before
**[33:28]** with learning on the job, where it's very interesting.
**[33:31]** You know, I think with the coding agents,
**[33:33]** like I don't think people would say that
**[33:35]** learning on the job is what is, you know,
**[33:38]** preventing the coding agents from like, you know,
**[33:41]** doing everything end to end.
**[33:43]** Like they keep getting better.
**[33:45]** We have engineers at Anthropic who like don't write any code
**[33:49]** and when I look at the productivity,
**[33:50]** to your previous question, you know,
**[33:52]** we have folks who say this GPU kernel, this chip,
**[33:56]** I used to write it myself, I just have Claude do it.
**[33:59]** And so there's this enormous improvement in productivity.
**[34:03]** And I don't know, like when I see Claude code,
**[34:06]** like familiarity with the code base,
**[34:09]** or like, you know, or a feeling that the model
**[34:13]** hasn't worked at the company for a year,
**[34:15]** that's not high up on the list of complaints I see.
**[34:18]** And so I think what I'm saying is we're like,
**[34:20]** we're kind of taking a different path.
**[34:22]** Don't you think with coding,
**[34:23]** that's because there is an external scaffold of memory,
**[34:25]** which exists instantiated in the code base,
**[34:28]** which I don't know how many other jobs have.
**[34:30]** Coding made fast progress precisely because
**[34:33]** it has this unique advantage
**[34:35]** that other economic activity doesn't.
**[34:37]** But when you say that, what you're implying
**[34:41]** is that by reading the code base into the context,
**[34:44]** I have everything that the human needed to learn on the job.
**[34:47]** So that would be an example of whether it's written or not,
**[34:53]** whether it's available or not,
**[34:54]** a case where everything you needed to know,
**[34:57]** you got from the context window, right?
**[34:59]** And that what we think of as learning,
**[35:01]** like, oh man, I started this job.
**[35:03]** It's gonna take me six months to understand the code base.
**[35:05]** The model just did it in the context.
**[35:07]** Yeah, I honestly don't know how to think about this
**[35:09]** because there are people who qualitatively report
**[35:13]** what you're saying.
**[35:14]** There was a meter study, I'm sure you saw last year,
**[35:17]** where they had experienced developers
**[35:20]** try to close a pull request in repositories
**[35:25]** that they were familiar with.
**[35:26]** And those developers reported an uplift.
**[35:29]** They reported that they felt more productive
**[35:30]** with the use of these models.
**[35:31]** But in fact, if you look at their output
**[35:33]** and how much was actually merged back in,
**[35:35]** there's a 20% downlift.
**[35:36]** They were less productive as a result of using these models.
**[35:38]** And so I'm trying to square the qualitative feeling
**[35:40]** that people feel with these models
**[35:41]** versus one, in a macro level,
**[35:44]** where is this like renaissance of software?
**[35:47]** And two, when people do these independent evaluations,
**[35:49]** why are we not seeing the productivity benefits
**[35:52]** that we would expect?
**[35:53]** Within Anthropic, this is just really unambiguous, right?
**[35:56]** We're under an incredible amount of commercial pressure
**[35:59]** and make it even harder for ourselves
**[36:01]** because we have all this safety stuff we do
**[36:03]** that I think we do more than other companies.
**[36:06]** So like the pressure to survive economically
**[36:11]** while also keeping our values is just incredible, right?
**[36:14]** We're trying to keep this 10X revenue curve going.
**[36:18]** There's like, there is zero time for bullshit.
**[36:20]** There is zero time for feeling like we're productive
**[36:24]** when we're not.
**[36:25]** Like these tools make us a lot more productive.
**[36:29]** Like why do you think we're concerned
**[36:32]** about competitors using the tools?
**[36:34]** Because we think we're ahead of the competitors
**[36:36]** and like, we don't want to sell.
**[36:38]** We wouldn't be going through all this trouble
**[36:42]** if this was secretly reducing our productivity.
**[36:46]** Like we see the end productivity every few months
**[36:50]** in the form of model launches.
**[36:52]** Like there's no kidding yourself about this.
**[36:54]** Like the models make you more productive.
**[36:57]** One, people feeling like they're more productive
**[37:00]** is qualitatively predicted by studies like this.
**[37:02]** But two, if I just look at the end output,
**[37:04]** obviously you guys are making fast progress.
**[37:06]** But the fact, the idea was supposed to be
**[37:10]** with recursive self-improvement
**[37:11]** is that you make a better AI,
**[37:13]** the AI helps you build a better next AI, et cetera, et cetera.
**[37:15]** And what I see instead,
**[37:17]** if I look at the you open AI deep mind
**[37:19]** is that people are just shifting around the podium
**[37:21]** every few months.
**[37:22]** And maybe you think that stops
**[37:23]** because you won or whatever,
**[37:25]** but why are we not seeing the person
**[37:28]** with the best coding model have this lasting advantage
**[37:32]** if in fact there are these enormous productivity gains
**[37:35]** from the last coding model?
**[37:36]** So, no, no, no.
**[37:37]** I mean, I think it's all like,
**[37:40]** my model of the situation is there's an advantage
**[37:43]** that's gradually growing.
**[37:44]** Like I would say right now the coding models give maybe,
**[37:50]** I don't know, a like 15, maybe 20% total factor speed up.
**[37:55]** Like that's my view.
**[37:57]** And six months ago it was maybe 5%.
**[38:00]** And so it didn't matter.
**[38:02]** Like 5% doesn't register.
**[38:03]** It's now just getting to the point
**[38:05]** where it's like one of several factors
**[38:07]** that kind of matters.
**[38:10]** And that's gonna keep speeding up.
**[38:11]** And so I think six months ago,
**[38:13]** like there were several companies
**[38:17]** that were at roughly the same point
**[38:19]** because this wasn't a notable factor,
**[38:23]** but I think it's starting to speed up more and more.
**[38:26]** I would also say there are multiple companies
**[38:28]** that write models that are used for code
**[38:31]** and we're not perfectly good
**[38:33]** at preventing some of these other companies
**[38:35]** from kind of using our models internally.
**[38:41]** So I think everything we're seeing
**[38:45]** is consistent with this kind of snowball model
**[38:49]** where there's no hard, again,
**[38:52]** my theme in all of this is like,
**[38:56]** all of this is soft takeoff,
**[38:58]** like soft, smooth exponentials,
**[39:00]** although the exponentials are relatively steep.
**[39:03]** And so we're seeing this snowball gather momentum
**[39:05]** where it's like 10%, 20%, 25%, 40%.
**[39:11]** And as you go, yeah, Amdahl's law,
**[39:12]** you have to get all the like things
**[39:14]** that are preventing you
**[39:15]** from closing the loop out of the way.
**[39:17]** But like, this is one of the biggest priorities
**[39:19]** within Anthropic.
**[39:22]** Stepping back, I think before in the stack,
**[39:25]** we were talking about,
**[39:27]** well, when do we get this on the job learning?
**[39:29]** And it seems like the coding,
**[39:31]** the point you were making the coding thing is,
**[39:33]** we actually don't need on the job learning.
**[39:34]** That you can have tremendous productivity improvements,
**[39:36]** you can have potentially trillions of dollars
**[39:38]** of revenue for AI companies
**[39:39]** without this basic human ability.
**[39:41]** Maybe that's not your claim, you should clarify.
**[39:43]** But without this basic human ability to learn on the job,
**[39:47]** but I just look at like,
**[39:49]** in most domains of economic activity,
**[39:51]** people say, I hired somebody,
**[39:53]** they weren't that useful for the first few months.
**[39:54]** And then over time,
**[39:56]** they built up the context understanding.
**[39:58]** It's actually harder to find what we're talking about here.
**[40:00]** But they got something.
**[40:01]** And then now they're a power horse
**[40:03]** and they're so valuable to us.
**[40:05]** And if AI doesn't develop this ability to learn on the fly,
**[40:08]** I'm a bit skeptical that we're gonna see
**[40:12]** huge changes to the world without that ability.
**[40:13]** Yeah, so I think two things here, right?
**[40:16]** There's the state of the technology right now,
**[40:20]** which is again, we have these two stages.
**[40:22]** We have the pre-training and RL stage,
**[40:24]** where you throw a bunch of data and tasks into the models
**[40:28]** and then they generalize.
**[40:29]** So it's like learning,
**[40:31]** but it's like learning from more data
**[40:33]** and not learning over kind of one human
**[40:36]** or one model's lifetime.
**[40:38]** So again, this is situated between evolution
**[40:41]** and human learning.
**[40:42]** But once you learn all those skills, you have them.
**[40:45]** And just like with pre-training,
**[40:47]** just how the models know more,
**[40:50]** if I look at a pre-trained model,
**[40:52]** it knows more about the history of samurai in Japan
**[40:55]** than I do.
**[40:56]** It knows more about baseball than I do.
**[40:58]** It knows more about low-pass filters and electronics
**[41:04]** than all of these things.
**[41:06]** Its knowledge is way broader than mine.
**[41:09]** So I think even just that may get us to the point
**[41:13]** where the models are better at everything.
**[41:17]** And then we also have, again,
**[41:19]** just with scaling the kind of existing setup,
**[41:22]** we have the in-context learning,
**[41:23]** which I would describe as kind of like
**[41:26]** human on-the-job learning,
**[41:27]** but like a little weaker and a little short-term.
**[41:30]** Like you look at in-context learning,
**[41:32]** you give the model a bunch of examples, it does get it.
**[41:35]** There's real learning that happens in context.
**[41:37]** And like a million tokens is a lot.
**[41:39]** That can be days of human learning, right?
**[41:42]** If you think about the model,
**[41:45]** kind of reading a million words,
**[41:49]** how long would it take me to read a million?
**[41:51]** I mean, like days or weeks at least.
**[41:54]** So you have these two things.
**[41:56]** And I think these two things within the existing paradigm
**[41:59]** may just be enough to get you the country of geniuses
**[42:02]** in the data center.
**[42:02]** I don't know for sure,
**[42:04]** but I think they're gonna get you a large fraction of it.
**[42:06]** There may be gaps, but I certainly think just as things are,
**[42:11]** this, I believe, is enough to generate
**[42:13]** trillions of dollars of revenue.
**[42:14]** That's one, that's all one.
**[42:16]** Two is this idea of continual learning,
**[42:20]** this idea of a single model learning on the job.
**[42:24]** I think we're working on that too.
**[42:26]** And I think there's a good chance
**[42:28]** that in the next year or two, we also solve that.
**[42:33]** Again, I think you get most of the way there without it.
**[42:38]** I think the trillions of dollars of,
**[42:42]** I think the trillions of dollars a year market,
**[42:45]** maybe all of the national security implications
**[42:47]** and the safety implications that I wrote about
**[42:49]** in adolescence of technology can happen without it.
**[42:51]** But I also think we, and I imagine others,
**[42:56]** are working on it.
**[42:57]** And I think there's a good chance
**[42:59]** that we get there within the next year or two.
**[43:03]** There are a bunch of ideas.
**[43:04]** I won't go into all of them in detail,
**[43:05]** but one is just make the context longer.
**[43:09]** There's nothing preventing longer context from working.
**[43:12]** You just have to train at longer context
**[43:14]** and then learn to serve them at inference.
**[43:16]** And both of those are engineering problems
**[43:18]** that we are working on
**[43:19]** and that I would assume others are working on as well.
**[43:22]** So this context length increase,
**[43:23]** it seemed like there was a period from 2020 to 2023
**[43:26]** where from GPT-3 to GPT-4 turbo,
**[43:27]** there was an increase from 2,000 context lengths to 128K.
**[43:31]** I feel like for the next, for the two-ish years since then,
**[43:34]** we've been in the same-ish ballpark.
**[43:36]** And when model context lengths get much longer than that,
**[43:39]** people report qualitative degradation
**[43:42]** in the ability of the model to consider that full context.
**[43:47]** So I'm curious what you're internally seeing
**[43:49]** that makes you think like,
**[43:50]** oh, 10 million contexts, 100 million contexts.
**[43:52]** To get human, like six months learning,
**[43:53]** billions and billions of contexts.
**[43:54]** This isn't a research problem.
**[43:55]** This is an engineering and inference problem, right?
**[43:58]** If you want to serve long context,
**[44:00]** you have to like store your entire KV cache.
**[44:03]** You have to, you know,
**[44:05]** it's difficult to store all the memory in the GPUs,
**[44:09]** to juggle the memory around.
**[44:11]** I don't even know the detail.
**[44:12]** You know, at this point,
**[44:14]** this is at a level of detail
**[44:15]** that I'm no longer able to follow.
**[44:17]** Although, you know, I knew it in the GPT-3 era of like,
**[44:20]** these are the weights,
**[44:21]** these are the activations you have to store.
**[44:24]** But, you know, these days the whole thing has flipped
**[44:26]** because we have MOE models and kind of all of that.
**[44:30]** But, and this degradation you're talking about,
**[44:33]** like again, without getting too specific,
**[44:35]** like a question I would ask is like,
**[44:38]** there's two things.
**[44:39]** There's the context length you train at,
**[44:41]** and there's a context length that you serve at.
**[44:43]** If you train at a small context length
**[44:45]** and then try to serve at a long context length,
**[44:47]** like maybe you get these degradations.
**[44:49]** It's better than nothing, you might still offer it,
**[44:51]** but you get these degradations.
**[44:52]** And maybe it's harder to train at a long context length.
**[44:55]** So, you know, there's a lot.
**[44:56]** I want to, at the same time,
**[44:58]** ask about like maybe some rabbit holes of like,
**[45:01]** well, wouldn't you expect
**[45:02]** that if you had to train on longer context length,
**[45:04]** that would mean that you're able to get sort of like,
**[45:08]** less samples in for the same amount of compute.
**[45:09]** But before, maybe it's not worth diving deep on that.
**[45:12]** I want to get an answer to the bigger picture question,
**[45:15]** which is like, okay,
**[45:16]** so I don't feel a preference for a human editor
**[45:22]** that's been working for me for six months
**[45:23]** versus an AI that's been working with me for six months.
**[45:27]** What year do you predict that that will be the case?
**[45:31]** I mean, you know, my guess for that is, you know,
**[45:35]** there's a lot of problems that are basically like,
**[45:37]** we can do this when we have the country of geniuses
**[45:39]** in a data center.
**[45:40]** And so, you know, my picture for that is, you know,
**[45:44]** again, if you made me guess, it's like one to two years,
**[45:48]** maybe one to three years.
**[45:50]** It's really hard to tell.
**[45:51]** I have a strong view, 99, 95% that like,
**[45:55]** all this will happen in 10 years.
**[45:57]** Like that's, I think that's just a super safe bet.
**[45:59]** And then I have a hunch, this is more like a 50, 50 thing,
**[46:03]** that it's going to be more like one to two,
**[46:05]** maybe more like one to three.
**[46:06]** So one to three years.
**[46:07]** The country of geniuses,
**[46:10]** and the slightly less economically valuable task
**[46:12]** of editing videos.
**[46:13]** And it seems pretty economically valuable, let me tell you.
**[46:16]** It's just, there are a lot of use cases like that, right?
**[46:19]** There are a lot of similar ones.
**[46:20]** So you're predicting that within one to three years.
**[46:23]** And in generally, Anthropic has predicted
**[46:25]** that by late 26, early 27,
**[46:28]** we will have AI systems that are quote,
**[46:30]** have the ability to navigate interfaces available
**[46:32]** to humans doing digital work today,
**[46:34]** intellectual capabilities,
**[46:35]** matching or exceeding that of Nobel prize winners,
**[46:37]** and the ability to interface with the physical world.
**[46:40]** And then you gave an interview two months ago
**[46:42]** with Dealbook, where you were emphasizing
**[46:44]** your company's more responsible compute scaling
**[46:49]** as compared to your competitors.
**[46:50]** And I'm trying to square these two views,
**[46:52]** where if you really believe
**[46:54]** that we're going to have a country of geniuses,
**[46:56]** you want as big a data center as you can get.
**[46:59]** There's no reason to slow down.
**[47:00]** The TAM of a Nobel prize winner that is actually,
**[47:04]** can do everything a Nobel prize winner can do
**[47:05]** is like trillions of dollars.
**[47:06]** And so I'm trying to square this conservatism,
**[47:10]** which seems rational if you have more moderate timelines
**[47:13]** with your stated views about AI progress.
**[47:16]** Yeah, so it actually all fits together
**[47:18]** and we go back to this fast,
**[47:20]** but not infinitely fast diffusion.
**[47:22]** So like, let's say that we're making progress at this rate.
**[47:26]** You know, the technology is making progress this fast.
**[47:29]** Again, I have, you know, very high conviction
**[47:32]** that like, it's going, you know,
**[47:34]** we're gonna get there within a few years.
**[47:39]** I have a hunch that we're gonna get there
**[47:41]** within a year or two.
**[47:42]** So a little uncertainty on the technical side,
**[47:44]** but like, you know, pretty strong confidence
**[47:47]** that it won't be off by much.
**[47:48]** What I'm less certain about is again,
**[47:51]** the economic diffusion side.
**[47:53]** Like I really do believe that we could have models
**[47:57]** that are a country of geniuses,
**[48:00]** country of geniuses in the data center in one to two years.
**[48:03]** One question is how many years after that
**[48:07]** do the trillions in revenue start rolling in?
**[48:14]** I don't think it's guaranteed
**[48:16]** that it's going to be immediate.
**[48:18]** You know, I think it could be one year.
**[48:22]** It could be two years.
**[48:24]** I could even stretch it to five years,
**[48:27]** although I'm like, I'm skeptical of that.
**[48:29]** And so we have this uncertainty,
**[48:32]** which is even if the technology goes as fast
**[48:35]** as I suspect that it will,
**[48:37]** we don't know exactly how fast it's gonna drive revenue.
**[48:41]** We know it's coming,
**[48:43]** but with the way you buy these data centers,
**[48:45]** if you're off by a couple of years, that can be ruinous.
**[48:48]** It is just like how I wrote, you know,
**[48:50]** in Machines of Loving Grace, I said,
**[48:53]** look, I think we might get this powerful AI,
**[48:55]** this country of geniuses in the data center.
**[48:56]** That description you gave
**[48:57]** comes from the Machines of Loving Grace.
**[48:59]** I said, we'll get that 2026, maybe 2027.
**[49:02]** Again, that is my hunch.
**[49:03]** Wouldn't be surprised if I'm off by a year or two,
**[49:05]** but like, that is my hunch.
**[49:08]** Let's say that happens.
**[49:09]** That's the starting gun.
**[49:10]** How long does it take to cure all the diseases, right?
**[49:13]** That's one of the ways that like drives
**[49:14]** a huge amount of economic value, right?
**[49:17]** Like you cure every disease.
**[49:20]** You know, there's a question of how much of that goes
**[49:22]** to the pharmaceutical company, to the AI company,
**[49:23]** but there's an enormous consumer surplus
**[49:25]** because everyone, you know,
**[49:27]** assuming we can get access for everyone,
**[49:29]** which I care about greatly,
**[49:30]** we, you know, we cure all of these diseases.
**[49:33]** How long does it take?
**[49:34]** You have to do the biological discovery.
**[49:36]** You have to, you know, you have to, you know,
**[49:39]** manufacture the new drug.
**[49:40]** You have to, you know, go through the regulatory process.
**[49:42]** I mean, we saw this with like vaccines and COVID, right?
**[49:45]** Like there's just this, we got the vaccine out to everyone,
**[49:49]** but it took a year and a half, right?
**[49:51]** And so my question is,
**[49:52]** how long does it take to get the cure for everything,
**[49:56]** which AI is the genius that can, in theory,
**[49:59]** invent out to everyone?
**[50:01]** How long from when that AI first exists in the lab
**[50:03]** to when diseases have actually been cured for everyone?
**[50:08]** Right?
**[50:08]** And, you know, we've had a polio vaccine for 50 years.
**[50:12]** We're still trying to eradicate it
**[50:14]** in the most remote corners of Africa.
**[50:16]** And, you know, the Gates Foundation
**[50:17]** is trying as hard as they can.
**[50:19]** Others are trying as hard as they can,
**[50:20]** but, you know, that's difficult.
**[50:23]** Again, you know, I don't expect most of the economic
**[50:25]** diffusion to be as difficult as that, right?
**[50:27]** That's like the most difficult case.
**[50:29]** But there's a real dilemma here.
**[50:32]** And where I've settled on it is it will be faster
**[50:37]** than anything we've seen in the world,
**[50:39]** but it still has its limits.
**[50:41]** And so then when we go to buying data centers,
**[50:45]** you know, again, the curve I'm looking at is,
**[50:49]** okay, we've had a 10X a year increase every year.
**[50:54]** So beginning of this year,
**[50:55]** we're looking at 10 billion in annual,
**[50:59]** in, you know, rate of annualized revenue
**[51:00]** at the beginning of the year.
**[51:02]** We have to decide how much compute to buy.
**[51:06]** And, you know, it takes a year or two
**[51:09]** to actually build out the data centers,
**[51:11]** to reserve the data centers.
**[51:12]** So basically I'm saying like in 2027,
**[51:16]** how much compute do I get?
**[51:18]** Well, I could assume that the revenue
**[51:24]** will continue growing 10X a year.
**[51:26]** So it'll be 100 billion at the end of 2026
**[51:32]** and 1 trillion at the end of 2027.
**[51:35]** And so I could buy a trillion dollars.
**[51:37]** Actually, it would be like $5 trillion of compute
**[51:40]** because it would be a trillion dollar a year
**[51:42]** for five years, right?
**[51:43]** I could buy a trillion dollars of compute
**[51:45]** that starts at the end of 2027.
**[51:48]** And if my revenue is not a trillion dollars,
**[51:51]** if it's even 800 billion, there's no force on earth.
**[51:56]** There's no hedge on earth
**[51:58]** that could stop me from going bankrupt
**[52:00]** if I buy that much compute.
**[52:02]** And so even though a part of my brain
**[52:04]** wonders if it's going to keep growing 10X,
**[52:07]** I can't buy a trillion dollars a year of compute in 2027.
**[52:14]** If I'm just off by a year in that rate of growth,
**[52:17]** or if the growth rate is 5X a year instead of 10X a year,
**[52:21]** then you go bankrupt.
**[52:24]** And so you end up in a world
**[52:27]** where you're supporting hundreds of billions,
**[52:30]** not trillions, and you accept some risk
**[52:34]** that there's so much demand
**[52:36]** that you can't support the revenue,
**[52:38]** and you accept still some risk
**[52:40]** that you got it wrong and it's still slow.
**[52:43]** And so when I talked about behaving responsibly,
**[52:46]** what I meant actually was not the absolute amount.
**[52:49]** That actually was not, I think it is true,
**[52:52]** we're spending somewhat less than some of the other players.
**[52:55]** It's actually the other things,
**[52:56]** like have we been thoughtful about it,
**[52:59]** or are we YOLOing and saying,
**[53:01]** oh, we're going to do $100 billion here,
**[53:03]** or $100 billion there.
**[53:05]** I kind of get the impression that
**[53:07]** some of the other companies
**[53:08]** have not written down the spreadsheet,
**[53:10]** that they don't really understand the risks they're taking.
**[53:12]** They're just kind of doing stuff because it sounds cool.
**[53:16]** And we've thought carefully about it, right?
**[53:19]** We're an enterprise business.
**[53:20]** Therefore, we can rely more on revenue.
**[53:24]** It's less fickle than consumer.
**[53:26]** We have better margins,
**[53:27]** which is the buffer between buying too much
**[53:29]** and buying too little.
**[53:31]** And so I think we bought an amount
**[53:32]** that allows us to capture pretty strong upside worlds.
**[53:37]** It won't capture the full 10X a year,
**[53:40]** and things would have to go pretty badly
**[53:42]** for us to be in financial trouble.
**[53:44]** So I think we've thought carefully
**[53:46]** and we've made that balance.
**[53:47]** And that's what I mean
**[53:48]** when I say that we're being responsible.
**[53:50]** Okay, so it seems like it's possible
**[53:53]** that we actually just have different definitions
**[53:55]** as a country of a genius in a data center.
**[53:56]** Because when I think of actual human geniuses,
**[54:00]** an actual country of human geniuses in a data center,
**[54:02]** I'm like, I would happily buy $5 trillion worth of compute
**[54:06]** to run an actual country of human geniuses in a data center.
**[54:09]** So let's say JP Morgan or Moderna or whatever
**[54:11]** doesn't want to use them.
**[54:13]** I've got a country of geniuses.
**[54:14]** They'll start their own company.
**[54:16]** And if they can't start their own company
**[54:17]** and they're bottlenecked by clinical trials,
**[54:18]** it is worth stating with clinical trials,
**[54:20]** most clinical trials fail because the drug doesn't work.
**[54:23]** There's not efficacy, right?
**[54:23]** And I make exactly that point in Machines of Love and Grace.
**[54:27]** I say the clinical trials are gonna go much faster
**[54:30]** than we're used to, but not infinitely fast.
**[54:33]** And then suppose it takes a year
**[54:35]** for the clinical trials to work out
**[54:36]** so that you're getting revenue from that
**[54:37]** and can make more drugs.
**[54:39]** Okay, well, you've got a country of geniuses
**[54:40]** and you're an AI lab,
**[54:42]** and you could use many more AI researchers.
**[54:47]** You also think that there's these like
**[54:49]** self-reinforcing gains from smart people working on AI tech.
**[54:53]** So like, okay, you can have the data center
**[54:56]** working on like AI progress.
**[54:57]** Is there more gains from buying,
**[55:00]** like substantially more gains from buying
**[55:03]** a trillion dollars a year of compute
**[55:05]** versus $300 billion a year of compute?
**[55:07]** If your competitor's buying a trillion, yes, there is.
**[55:09]** Well, no, there's some gain,
**[55:11]** but again, there's this chance that they go bankrupt before,
**[55:16]** again, if you're off by only a year, you destroy yourselves.
**[55:21]** That's the balance.
**[55:23]** We're buying a lot.
**[55:24]** We're buying a hell of a lot.
**[55:25]** Like we're not, we're buying an amount
**[55:28]** that's comparable to that,
**[55:30]** that the biggest players in the game are buying.
**[55:34]** But if you're asking me, why haven't we signed
**[55:39]** 10 trillion of compute starting in mid-2027?
**[55:43]** First of all, it can't be produced.
**[55:44]** There isn't that much in the world.
**[55:47]** But second, what if the country of geniuses comes,
**[55:51]** but it comes in mid-2028 instead of mid-2027?
**[55:54]** You go bankrupt.
**[55:55]** So if your projection is one to three years,
**[55:59]** it seems like you should have won $10 trillion of compute
**[56:01]** by 2029, 2020, and maybe 2020, the latest.
**[56:05]** Like, I mean, you know, you're like,
**[56:08]** it seems like even in the longest version
**[56:10]** of the timelines you state,
**[56:12]** the compute you are ramping up to build
**[56:14]** doesn't seem in accordance.
**[56:16]** What makes you think that?
**[56:17]** Well, as you said, you would want the 10 trillion,
**[56:20]** the human wages, let's say,
**[56:21]** are on the order of 50 trillion a year.
**[56:24]** If you look at, so I won't talk about
**[56:26]** Anthropic in particular,
**[56:27]** but if you talk about the industry,
**[56:29]** like the amount of compute the industry,
**[56:33]** you know, the amount of compute the industry's building
**[56:37]** this year is probably in the, you know, I don't know,
**[56:40]** very low tens of, you know, call it 10, 15 gigawatts.
**[56:44]** Next year, you know, it goes up by roughly three X a year.
**[56:48]** So like next year's 30 or 40 gigawatts,
**[56:51]** and 2028 might be 100,
**[56:54]** 2029 might be like 300 gigawatts.
**[56:58]** And like each gigawatt costs like maybe 10,
**[57:03]** I mean, I'm doing the math in my head,
**[57:04]** but each gigawatt costs maybe $10 billion,
**[57:07]** you know, or border 10 to $15 billion a year.
**[57:09]** So, you know, you kind of, you know,
**[57:12]** you put that all together
**[57:13]** and you're getting about what you described.
**[57:15]** You're getting multiple trillions a year by 2028 or 2029.
**[57:18]** So you're getting exactly that.
**[57:20]** You're getting exactly what you predict.
**[57:23]** That's for the industry.
**[57:24]** That's for the industry.
**[57:25]** That's right.
**[57:26]** So suppose Anthropic's compute keeps three X-ing a year,
**[57:28]** and then by like 27, you have,
**[57:31]** or 27, 28, you have 10 gigawatts,
**[57:33]** and like multiply that by, as you say, 10 billion.
**[57:38]** So then it's like a hundred billion a year,
**[57:40]** but then you're saying the TAM by 2028, 2029.
**[57:42]** Again, I don't want to give exact numbers for Anthropic,
**[57:45]** but these numbers are too small.
**[57:46]** These numbers are too small.
**[57:48]** Okay, interesting.
**[57:49]** I'm really proud that the puzzles I've worked on
**[57:51]** with Jane Street have resulted in them hiring
**[57:53]** a bunch of people from my audience.
**[57:54]** Well, they're still hiring,
**[57:56]** and they just sent me another puzzle.
**[57:58]** For this one, they spent about 20,000 GPU hours
**[58:01]** training backdoors into three different language models.
**[58:03]** Each one has a hidden prompt
**[58:04]** that elicits completely different behavior.
**[58:07]** You just have to find the trigger.
**[58:08]** This is particularly cool because finding backdoors
**[58:10]** is actually an open question in frontier AI research.
**[58:13]** Anthropic actually released a couple of papers
**[58:15]** about sleeper agents,
**[58:16]** and they show that you can build a simple classifier
**[58:19]** on the residual stream to detect
**[58:21]** when a backdoor is about to fire.
**[58:23]** But they already knew what the triggers were
**[58:25]** because they built them.
**[58:26]** Here, you don't, and it's not feasible
**[58:28]** to check the activations for all possible trigger phrases.
**[58:32]** Unlike the other puzzles they made for this podcast,
**[58:34]** Jane Street isn't even sure this one is solvable,
**[58:36]** but they've set aside $50,000
**[58:38]** for the best attempts and write-ups.
**[58:39]** The puzzle's live at janestreet.com slash TwerkHash,
**[58:44]** and they're accepting submissions until April 1st.
**[58:47]** All right, back to Dario.
**[58:48]** You've told investors that you plan to be profitable
**[58:51]** starting in 28, and this is the year
**[58:54]** where we're potentially getting
**[58:55]** the country of geniuses as a data center,
**[58:57]** and this is gonna now unlock all this progress
**[59:02]** and medicine and health and et cetera, et cetera,
**[59:06]** and new technologies.
**[59:08]** Wouldn't this be exactly the time
**[59:10]** where you'd want to reinvest in the business
**[59:12]** and build bigger countries
**[59:14]** so they can make more discoveries?
**[59:15]** I mean, profitability is this kind of weird thing
**[59:18]** in this field.
**[59:21]** I don't think in this field profitability
**[59:23]** is actually a measure of kind of spending down
**[59:31]** versus investing in the business.
**[59:33]** Like let's just take a model of this.
**[59:36]** I actually think profitability happens
**[59:38]** when you underestimated the amount of demand
**[59:40]** you were gonna get, and loss happens
**[59:43]** when you overestimated the amount of demand
**[59:44]** you were going to get,
**[59:46]** because you're buying the data centers ahead of time.
**[59:47]** So think about it this way.
**[59:50]** Ideally, you would like,
**[59:52]** and again, these are stylized facts.
**[59:54]** These numbers are not exact.
**[59:55]** I'm just trying to make a toy model here.
**[59:56]** Let's say half of your compute is for training
**[59:59]** and half of your.
**[01:00:00]** compute is for inference.
**[01:00:02]** And the inference has some gross margin
**[01:00:04]** that's like more than 50%.
**[01:00:06]** And so what that means is that if you were in steady state,
**[01:00:10]** you build a data center.
**[01:00:11]** If you knew exactly the demand you were getting,
**[01:00:15]** you would get a certain amount of revenue, say, I don't know,
**[01:00:23]** let's say you pay $100 billion a year for compute.
**[01:00:26]** And on $50 billion a year, you support $150 billion
**[01:00:29]** of revenue, and the other $50 billion
**[01:00:33]** are used for training.
**[01:00:35]** So basically, you're profitable.
**[01:00:37]** You make $50 billion of profit.
**[01:00:39]** Those are the economics of the industry today.
**[01:00:42]** Or sorry, not today, but that's where we're projecting forward
**[01:00:46]** in a year or two.
**[01:00:47]** The only thing that makes that not the case
**[01:00:49]** is if you get less demand than $50 billion,
**[01:00:54]** then you have more than 50% of your data center for research,
**[01:00:58]** and you're not profitable.
**[01:00:59]** So you train stronger models, but you're not profitable.
**[01:01:03]** If you get more demand than you thought,
**[01:01:06]** then your research gets squeezed,
**[01:01:09]** but you're able to support more inference,
**[01:01:13]** and you're more profitable.
**[01:01:14]** So maybe I'm not explaining it well,
**[01:01:17]** but the thing I'm trying to say is you decide
**[01:01:19]** the amount of compute first.
**[01:01:21]** And then you have some target desire
**[01:01:23]** of inference versus training, but that
**[01:01:27]** gets determined by demand.
**[01:01:28]** It doesn't get determined by you.
**[01:01:29]** What I'm hearing is the reason you're predicting profit
**[01:01:32]** is that you are systematically underinvesting in compute,
**[01:01:35]** right?
**[01:01:36]** Because if you actually, like,
**[01:01:37]** No, no, no, I'm saying it's hard to predict.
**[01:01:39]** So these things about 2028 and when it will happen,
**[01:01:43]** that's our attempt to do the best we can with investors.
**[01:01:46]** All of this stuff is really uncertain because
**[01:01:48]** of the cone of uncertainty.
**[01:01:49]** Like, we could be profitable in 2026
**[01:01:53]** if the revenue grows fast enough.
**[01:01:55]** And then if we overestimate or underestimate the next year,
**[01:02:01]** that could swing wildly.
**[01:02:02]** Like, what I'm trying to get is you
**[01:02:05]** have a model in your head of, like, the business invests,
**[01:02:09]** invests, invests, invests, gets scale,
**[01:02:11]** and kind of then becomes profitable.
**[01:02:13]** There's a single point at which things turn around.
**[01:02:16]** I don't think the economics of this industry work that way.
**[01:02:19]** I see.
**[01:02:19]** So if I'm understanding correctly,
**[01:02:21]** you're saying because of the discrepancy
**[01:02:24]** between the amount of compute we should have gotten
**[01:02:26]** and the amount of compute we got,
**[01:02:27]** we were, like, sort of forced to make profit.
**[01:02:29]** But that doesn't mean we're going
**[01:02:30]** to continue making profit.
**[01:02:31]** We're going to, like, reinvest the money because, well,
**[01:02:34]** now AI has made so much progress and we
**[01:02:35]** want the bigger country of geniuses.
**[01:02:37]** And so then back into revenue is high, but losses are also high.
**[01:02:42]** If we predict, if every year we predict
**[01:02:46]** exactly what the demand is going to be,
**[01:02:48]** we'll be profitable every year.
**[01:02:50]** Because spending 50% of your compute on research,
**[01:02:56]** roughly, plus a gross margin that's higher than 50%
**[01:03:01]** and correct demand prediction leads to profit.
**[01:03:03]** That's the profitable business model
**[01:03:06]** that I think is kind of, like, there,
**[01:03:08]** but, like, obscured by these, like, building
**[01:03:12]** ahead and prediction errors.
**[01:03:13]** I guess you're treating the 50% as a sort of, like,
**[01:03:18]** given constant.
**[01:03:19]** Whereas, in fact, if AI progress is fast
**[01:03:22]** and you can increase the progress by scaling up more,
**[01:03:24]** you just have more than 50% and not make profit.
**[01:03:25]** Here's what I'll say.
**[01:03:26]** You might want to scale up it more.
**[01:03:28]** You might want to scale it up more.
**[01:03:29]** But, you know, remember the log returns to scale, right?
**[01:03:33]** If 70% would get you a very little bit of a smaller model
**[01:03:39]** through a factor of 1.4x, right?
**[01:03:41]** Like, that extra $20 billion is, you know,
**[01:03:45]** that each dollar there is worth much less to you
**[01:03:48]** because of the log linear setup.
**[01:03:50]** And so you might find that it's better to invest that $20
**[01:03:56]** billion in, you know, in serving inference
**[01:03:59]** or in hiring engineers who are kind of better
**[01:04:03]** at what they're doing.
**[01:04:04]** So the reason I said 50%, that's not exactly our target.
**[01:04:08]** It's not exactly going to be 50%.
**[01:04:10]** It'll probably vary over time.
**[01:04:12]** What I'm saying is the, like, log linear return,
**[01:04:16]** what it leads to is you spend of order one fraction
**[01:04:20]** of the business, right?
**[01:04:21]** Like not 5%, not 95%.
**[01:04:25]** And then you get diminishing returns
**[01:04:28]** because of the log scale up.
**[01:04:30]** It's strange that I'm, like, convincing Dario
**[01:04:32]** to, like, believe in AI progress or something.
**[01:04:34]** But, like, okay, you don't invest in research
**[01:04:36]** because it has diminishing returns,
**[01:04:38]** but you invest in the other things you mentioned.
**[01:04:39]** Again, we're talking about diminishing returns
**[01:04:43]** after you're spending 50 billion a year, right?
**[01:04:45]** Like, this is a point I'm sure you would make,
**[01:04:47]** but, like, diminishing returns on a genius
**[01:04:51]** could be quite high.
**[01:04:52]** And more generally, like, what is profit in a market economy?
**[01:04:55]** Profit is basically saying the other companies
**[01:04:58]** in the market can, like, do more things with this money
**[01:05:01]** that I can't.
**[01:05:01]** Yeah, I mean, put aside Anthropic.
**[01:05:02]** I'm just trying to, like, because, you know,
**[01:05:04]** I don't want to give information about Anthropic
**[01:05:06]** is why I'm giving these stylized numbers.
**[01:05:08]** But, like, let's just derive the equilibrium
**[01:05:10]** of the industry, right?
**[01:05:12]** I think that, so why doesn't everyone spend 100%
**[01:05:17]** of their, you know, 100% of their compute on training
**[01:05:21]** and not serve any customers, right?
**[01:05:23]** It's because if they didn't get any revenue,
**[01:05:25]** they couldn't raise money, they couldn't do compute deals,
**[01:05:27]** they couldn't buy more compute the next year.
**[01:05:29]** So there's going to be an equilibrium
**[01:05:30]** where every company spends less than 100% on training
**[01:05:36]** and certainly less than 100% on inference.
**[01:05:38]** It should be clear why you don't just serve
**[01:05:40]** the current models and, you know,
**[01:05:42]** and never train another model
**[01:05:44]** because then you don't have any demand
**[01:05:46]** because you'll fall behind.
**[01:05:48]** So there's some equilibrium.
**[01:05:49]** It's not going to be 10%.
**[01:05:51]** It's not going to be 90%.
**[01:05:53]** Let's just say as a stylized fact, it's 50%.
**[01:05:55]** That's what I'm getting at.
**[01:05:56]** And I think we're going to be in a position
**[01:05:59]** where that equilibrium of how much you spend on training
**[01:06:02]** is less than the gross margins
**[01:06:04]** that you're able to get on compute.
**[01:06:08]** And so the underlying economics are profitable.
**[01:06:11]** The problem is you have this hellish
**[01:06:14]** demand prediction problem
**[01:06:15]** when you're buying the next year of compute.
**[01:06:18]** And you might guess under and be very profitable
**[01:06:22]** but have no compute for research,
**[01:06:23]** or you might guess over and, you know,
**[01:06:29]** you are not profitable and you have all the compute,
**[01:06:32]** you have no compute for research in the world.
**[01:06:34]** Does that make sense?
**[01:06:36]** Just as a dynamic model of the industry.
**[01:06:38]** Maybe stepping back, I'm like,
**[01:06:40]** I'm not saying I think the country of genius
**[01:06:43]** is going to come in two years
**[01:06:44]** and therefore you should buy this compute.
**[01:06:47]** To me, what you're saying,
**[01:06:48]** the end conclusion you're arriving at makes a lot of sense,
**[01:06:51]** but that's because like, oh,
**[01:06:54]** it seems like country of genius is as hard
**[01:06:55]** and there's a long way to go.
**[01:06:57]** And so the stepping back,
**[01:06:59]** the thing I'm trying to get at is more like,
**[01:07:02]** it seems like your worldview is compatible
**[01:07:03]** with somebody who says,
**[01:07:05]** we're like 10 years away from a world
**[01:07:07]** in which like we're generating trillions of dollars.
**[01:07:09]** That's just not my view.
**[01:07:10]** Yeah.
**[01:07:11]** That is not my view.
**[01:07:12]** Like, so I'll like make another prediction.
**[01:07:15]** It is hard for me to see
**[01:07:18]** that there won't be trillions of dollars
**[01:07:20]** in revenue before 2030.
**[01:07:23]** Like I can construct a plausible world.
**[01:07:26]** It takes maybe three years.
**[01:07:28]** So that would be the end
**[01:07:30]** of what I think it's plausible.
**[01:07:31]** Like in 2028, we get the real country of geniuses
**[01:07:35]** in the data center.
**[01:07:36]** You know, the revenue's been going into the,
**[01:07:40]** maybe is in the low hundreds of billions by 2028.
**[01:07:45]** And then the country of geniuses
**[01:07:47]** accelerates it to trillions, you know,
**[01:07:49]** and we're basically on the slow end of diffusion.
**[01:07:52]** It takes two years to get to the trillions.
**[01:07:54]** That would be the world where it takes until,
**[01:07:57]** that would be the world where it takes until 2030.
**[01:08:00]** I suspect even composing the technical exponential
**[01:08:04]** and diffusion exponential will get there before 2030.
**[01:08:07]** So you laid out a model where Entropic makes profit
**[01:08:10]** because it seems like fundamentally
**[01:08:13]** we're in a compute constrained world.
**[01:08:14]** And so it's like, eventually we keep growing compute.
**[01:08:16]** No, I think the way the profit comes is again,
**[01:08:20]** and you know, let's just abstract to the whole industry here.
**[01:08:22]** Like we have a, you know,
**[01:08:24]** let's just imagine we're in like an economics textbook.
**[01:08:27]** We have a small number of firms,
**[01:08:29]** each can invest a limited amount in, you know,
**[01:08:32]** or like each can invest some fraction in R and D.
**[01:08:36]** They have some marginal cost to serve.
**[01:08:38]** The margins on that, the profit margin,
**[01:08:40]** the gross profit margins on that marginal cost
**[01:08:43]** are like very high because inference is efficient.
**[01:08:47]** There's some competition,
**[01:08:48]** but the models are also differentiated.
**[01:08:50]** There's some, you know,
**[01:08:52]** companies will compete to push their research budgets up.
**[01:08:55]** But like, because there's a small number of players,
**[01:08:58]** you know, we have the, what is it called?
**[01:09:00]** The Cournot equilibrium,
**[01:09:01]** I think is what the small number of firm equilibrium is.
**[01:09:05]** The point is it doesn't equilibrate to perfect competition
**[01:09:09]** with zero margins.
**[01:09:13]** If there's like three firms,
**[01:09:15]** if there's three firms in the economy,
**[01:09:17]** all are kind of independently behaving rationally,
**[01:09:20]** it doesn't equilibrate to zero.
**[01:09:23]** Help me understand that,
**[01:09:24]** because right now we do have three leading firms
**[01:09:26]** and they're not making profit.
**[01:09:28]** And so, yeah, what is changing?
**[01:09:32]** Yeah, so the, again,
**[01:09:34]** the gross margins right now are very positive.
**[01:09:38]** What's happening is a combination of two things.
**[01:09:41]** One is we're still in the exponential scale-up
**[01:09:44]** phase of compute.
**[01:09:46]** So what, basically what that means is we're training,
**[01:09:49]** like a model gets trained, it costs, you know,
**[01:09:52]** let's say a model got trained
**[01:09:53]** that costs a billion dollars last year.
**[01:09:58]** And then this year it produced $4 billion of revenue
**[01:10:04]** and cost $1 billion to inference from.
**[01:10:10]** So, you know, again, I'm using stylized number here,
**[01:10:12]** but, you know, there'll be 75%, you know, gross margins
**[01:10:16]** and, you know, this 25% tax.
**[01:10:18]** So that model as a whole makes $2 billion.
**[01:10:24]** But at the same time,
**[01:10:25]** we're spending $10 billion to train the next model
**[01:10:28]** in the exponential scale-up.
**[01:10:30]** And so the company loses money.
**[01:10:31]** Each model makes money, but the company loses money.
**[01:10:34]** The equilibrium I'm talking about is an equilibrium
**[01:10:37]** where we have the country of geniuses,
**[01:10:39]** we have the country of geniuses in a data center,
**[01:10:41]** but that model training scale-up has equilibrated more.
**[01:10:47]** Maybe it's still going up,
**[01:10:49]** we're still trying to predict the demand,
**[01:10:51]** but it's more leveled out.
**[01:10:54]** I'll give you a couple of things there.
**[01:10:56]** Let's start with the current world.
**[01:10:58]** In the current world, you're right that,
**[01:11:00]** as you said before, if you treat each individual model
**[01:11:03]** as a company, it's profitable.
**[01:11:05]** But of course, a big part of the production function
**[01:11:08]** of being a frontier lab is training the next model, right?
**[01:11:12]** So if you didn't do that,
**[01:11:13]** then you'd make profit for two months
**[01:11:15]** and then you wouldn't have margins
**[01:11:17]** because you wouldn't have the best model.
**[01:11:18]** And then so, yeah, you can make profits
**[01:11:19]** for two months in the current system.
**[01:11:20]** But at some point that reaches the biggest scale
**[01:11:22]** that it can reach.
**[01:11:23]** And then in equilibrium,
**[01:11:25]** we have algorithmic improvements,
**[01:11:27]** but we're spending roughly the same amount
**[01:11:28]** to train the next model as we spent
**[01:11:31]** to train the current model.
**[01:11:33]** So this equilibrium relies-
**[01:11:36]** I mean, at some point,
**[01:11:37]** you run out of money in the economy.
**[01:11:40]** Fixed lump of labor follows.
**[01:11:42]** The economy is gonna grow, right?
**[01:11:43]** That's one of your predictions.
**[01:11:44]** Well, we're gonna have data centers in space.
**[01:11:46]** But this is another example
**[01:11:47]** of the theme I was talking about,
**[01:11:49]** which is that the economy will grow much faster
**[01:11:53]** with AI than I think it ever has before.
**[01:11:55]** But it's not like right now,
**[01:11:57]** the computer is growing three X a year.
**[01:11:59]** I don't believe the economy is gonna grow 300% a year.
**[01:12:03]** Like I said, this in Machines of Love and Grace,
**[01:12:05]** like I think we may get 10 or 20% per year
**[01:12:09]** growth in the economy,
**[01:12:10]** but we're not gonna get 300% growth in the economy.
**[01:12:13]** So I think in the end,
**[01:12:15]** if compute becomes the majority
**[01:12:17]** of what the economy produces,
**[01:12:18]** it's gonna be capped by that.
**[01:12:20]** So, okay, now let's assume a model
**[01:12:23]** where compute stays capped.
**[01:12:24]** The world where Frontier Labs are making money
**[01:12:27]** is one where they continue to make fast progress
**[01:12:31]** because fundamentally your margin is limited
**[01:12:33]** by how good the alternative is.
**[01:12:36]** And so you are able to make money
**[01:12:37]** because you have a Frontier model.
**[01:12:38]** If you didn't have a Frontier model,
**[01:12:39]** you wouldn't be making money.
**[01:12:41]** And so this model requires
**[01:12:44]** there never to be a steady state.
**[01:12:46]** Like forever and ever,
**[01:12:47]** you keep making more algorithmic progress.
**[01:12:49]** I don't think that's true.
**[01:12:50]** I mean, I feel like we're taught,
**[01:12:53]** we're, you know,
**[01:12:54]** they feel like this is an economics,
**[01:12:55]** like, you know, this is like an economics class.
**[01:12:58]** Do you know the Tyler Cowen quote?
**[01:12:59]** We never stopped talking about economics.
**[01:13:01]** We never stopped talking about economics.
**[01:13:03]** So, no, but there are worlds in which,
**[01:13:09]** so I don't think this field's gonna be,
**[01:13:11]** I don't think this field's gonna be a monopoly.
**[01:13:12]** All my lawyers never want me to say the word monopoly,
**[01:13:15]** but I don't think this field's gonna be a monopoly.
**[01:13:17]** But you do get,
**[01:13:18]** you get industries in which
**[01:13:20]** there are a small number of players,
**[01:13:21]** not one, but a small number of players.
**[01:13:23]** And ordinarily, like the way you get monopolies
**[01:13:27]** like Facebook or Meta,
**[01:13:31]** I always call them Facebook,
**[01:13:32]** but is these kind of network effects.
**[01:13:37]** The way you get industries
**[01:13:38]** in which there are a small number of players
**[01:13:41]** are very high costs of entry, right?
**[01:13:44]** So, you know, cloud is like this.
**[01:13:47]** I think cloud is a good example of this.
**[01:13:49]** You have three, maybe four players within cloud.
**[01:13:52]** I think that's the same for AI, three, maybe four.
**[01:13:56]** And the reason is that it's so expensive.
**[01:13:59]** It requires so much expertise
**[01:14:01]** and so much capital to like run a cloud company, right?
**[01:14:06]** And so you have to put up all this capital.
**[01:14:07]** And then in addition to putting up all this capital,
**[01:14:10]** you have to get all of this other stuff
**[01:14:11]** that like requires a lot of skill to make it happen.
**[01:14:15]** And so it's like, if you go to someone
**[01:14:17]** and you're like, I want to disrupt this industry,
**[01:14:18]** here's a hundred billion dollars.
**[01:14:19]** You're like, okay, I'm putting a hundred billion dollars
**[01:14:22]** and also betting that you can do all these other things
**[01:14:24]** that these people have been doing for like-
**[01:14:25]** Well, and then you decrease the profit in the industry.
**[01:14:27]** And then the effect of your entering
**[01:14:29]** is the profit margins go down.
**[01:14:31]** So, you know, we have equilibria like this all the time
**[01:14:33]** in the economy where we have a few players,
**[01:14:36]** profits are not astronomical,
**[01:14:39]** margins are not astronomical,
**[01:14:40]** but they're not zero, right?
**[01:14:43]** And, you know, I think that's what we see on cloud.
**[01:14:47]** Cloud is very undifferentiated.
**[01:14:48]** Models are more differentiated than cloud, right?
**[01:14:51]** Like everyone knows Claude is good at different things
**[01:14:55]** than GPT is good at, than Gemini is good at.
**[01:14:58]** And it's not just Claude's good at coding,
**[01:15:00]** GPT is good at, you know, math and reasoning, you know,
**[01:15:04]** it's more subtle than that.
**[01:15:06]** Like models are good at different types of coding.
**[01:15:08]** Models have different styles.
**[01:15:10]** Like I think these things are actually, you know,
**[01:15:13]** quite different from each other.
**[01:15:14]** And so I would expect more differentiation
**[01:15:16]** than you see in cloud.
**[01:15:20]** Now, there actually is a counter,
**[01:15:24]** there is one counter argument.
**[01:15:26]** And that counter argument is that if all of that,
**[01:15:28]** the process of producing models becomes,
**[01:15:32]** if AI models can do that themselves,
**[01:15:35]** then that could spread throughout the economy.
**[01:15:37]** But that is not an argument
**[01:15:38]** for commoditizing AI models in general.
**[01:15:41]** That's kind of an argument
**[01:15:42]** for commoditizing the whole economy at once.
**[01:15:45]** I don't know what quite happens in that world
**[01:15:47]** where basically anyone can do anything,
**[01:15:49]** anyone can build anything,
**[01:15:50]** and there's like no mode around anything at all.
**[01:15:53]** I mean, I don't know, maybe we want that world.
**[01:15:55]** Like maybe that's the end state here.
**[01:15:58]** Like maybe when kind of AI models can do everything,
**[01:16:05]** if we've solved all the safety and security problems,
**[01:16:08]** like, you know, that's one of the mechanisms
**[01:16:12]** for, you know, just kind of the economy
**[01:16:16]** flattening itself again.
**[01:16:18]** But that's kind of like post,
**[01:16:19]** like far post-controversy uses in the data center.
**[01:16:23]** Maybe a finer way to put that potential point is,
**[01:16:27]** one, it seems like AI research
**[01:16:30]** is especially loaded on raw intellectual power,
**[01:16:35]** which will be especially abundant in a world with AGI.
**[01:16:37]** And two, if you just look at the world today,
**[01:16:40]** there's very few technologies that seem to be diffusing
**[01:16:42]** as fast as AI algorithmic progress.
**[01:16:47]** And so that does hint that this industry
**[01:16:50]** is sort of structurally diffusive.
**[01:16:52]** So I think coding is going fast,
**[01:16:54]** but I think AI research is a superset of coding,
**[01:16:56]** and there are aspects of it that are not going fast.
**[01:16:59]** But I do think, again, once we get coding,
**[01:17:02]** once we get AI models going fast,
**[01:17:04]** then, you know, that will speed up the ability of AI models
**[01:17:08]** to kind of do everything else.
**[01:17:10]** So I think while coding is going fast now,
**[01:17:13]** I think once the AI models are building the next AI models
**[01:17:16]** and building everything else,
**[01:17:17]** the whole economy will start to kind of go at the same pace.
**[01:17:21]** I am worried geographically, though.
**[01:17:24]** I'm a little worried that just proximity to AI,
**[01:17:28]** having heard about AI,
**[01:17:31]** that that may be one differentiator.
**[01:17:34]** And so when I said the 10% or 20% growth rate,
**[01:17:38]** a worry I have is that the growth rate
**[01:17:40]** could be like 50% in Silicon Valley,
**[01:17:43]** and, you know, parts of the world
**[01:17:45]** that are kind of socially connected to Silicon Valley,
**[01:17:47]** and, you know, not that much faster
**[01:17:50]** than its current pace elsewhere.
**[01:17:52]** And I think that'd be a pretty messed up world.
**[01:17:54]** So one of the things I think about a lot
**[01:17:55]** is how to prevent that.
**[01:17:56]** Yeah.
**[01:17:57]** Do you think that once we have
**[01:17:59]** this country of geniuses as a data center,
**[01:18:00]** that robotics is sort of quickly solved afterwards
**[01:18:04]** because it seems like a big problem with robotics
**[01:18:06]** is that a human can learn how to teleoperate
**[01:18:09]** current hardware, but current AI models can't,
**[01:18:12]** at least not in a way that's super productive.
**[01:18:15]** And so if we have this ability to learn like a human,
**[01:18:17]** should it solve robotics immediately as well?
**[01:18:19]** I don't think it's dependent on learning like a human.
**[01:18:21]** It could happen in different ways.
**[01:18:22]** Again, we could have trained the model
**[01:18:25]** on many different video games,
**[01:18:26]** which are like robotic controls
**[01:18:28]** or many different simulated robotics environments,
**[01:18:31]** or just, you know, train them to control computer screens
**[01:18:33]** and they learn to generalize.
**[01:18:34]** So it will happen.
**[01:18:37]** It's not necessarily dependent on human-like learning.
**[01:18:41]** Human-like learning is one way it could happen.
**[01:18:43]** If the model's like, oh, I pick up a robot,
**[01:18:44]** I don't know how to use it, I learn.
**[01:18:46]** That could happen because we discovered,
**[01:18:49]** discovering continual learning.
**[01:18:50]** That could also happen because we trained the model
**[01:18:52]** on a bunch of environments and then generalized,
**[01:18:55]** or it could happen because the model learns that
**[01:18:57]** in the context length.
**[01:18:58]** It doesn't actually matter which way.
**[01:19:00]** If we go back to the discussion we had like an hour ago,
**[01:19:05]** that type of thing can happen in several different ways.
**[01:19:10]** But I do think when, for whatever reason,
**[01:19:13]** the models have those skills,
**[01:19:15]** then robotics will be revolutionized,
**[01:19:18]** both the design of robots,
**[01:19:19]** because the models will be much better than humans at that,
**[01:19:23]** and also the ability to kind of control robots.
**[01:19:26]** So we'll get better at building the physical hardware,
**[01:19:29]** building the physical robots,
**[01:19:31]** and we'll also get better at controlling it.
**[01:19:33]** Does that mean the robotics industry
**[01:19:35]** will also be generating trillions of dollars of revenue?
**[01:19:37]** My answer there is yes,
**[01:19:39]** but there will be the same extremely fast,
**[01:19:42]** but not infinitely fast diffusion.
**[01:19:43]** So will robotics be revolutionized?
**[01:19:46]** Yeah, maybe tack on another year or two.
**[01:19:49]** That's the way I think about these things.
**[01:19:51]** Makes sense.
**[01:19:52]** There's a general skepticism about extremely fast progress.
**[01:19:57]** Like here's my view, which is like,
**[01:19:58]** it sounds like you are gonna solve continual learning
**[01:20:00]** one way or another within a matter of years,
**[01:20:03]** but just as people weren't talking about
**[01:20:05]** continual learning a couple of years ago,
**[01:20:06]** and then we realized,
**[01:20:07]** oh, why aren't these models as useful
**[01:20:08]** as they could be right now,
**[01:20:09]** even though they are clearly passing the Turing test
**[01:20:12]** and are experts in so many different domains?
**[01:20:13]** Maybe it's this thing.
**[01:20:15]** And then we solve this thing and we realize,
**[01:20:16]** actually, there's another thing
**[01:20:19]** that human intelligence can do,
**[01:20:21]** and that's a basis of human labor
**[01:20:22]** that these models can't do.
**[01:20:23]** And then, so why not think
**[01:20:24]** there will be more things like this?
**[01:20:26]** Why think that we've found the pieces of human intelligence?
**[01:20:31]** Well, to be clear, I mean,
**[01:20:32]** I think continual learning, as I said before,
**[01:20:34]** might not be a barrier at all, right?
**[01:20:35]** Like, you know, I think we maybe just get there
**[01:20:38]** by pre-training generalization and RL generalization.
**[01:20:44]** Like I think there just might not be,
**[01:20:47]** there basically might not be such a thing at all.
**[01:20:49]** In fact, I would point to the history in ML
**[01:20:52]** of people coming up with things that are barriers
**[01:20:55]** that end up kind of dissolving
**[01:20:57]** within the big blob of compute, right?
**[01:20:58]** That, you know, people talked about, you know,
**[01:21:02]** you know, how do you have, you know,
**[01:21:05]** how do your models keep track of nouns and verbs?
**[01:21:08]** And, you know, how do they, you know,
**[01:21:09]** they can understand syntactically,
**[01:21:11]** but they can't understand semantically.
**[01:21:14]** You know, it's only statistical correlations.
**[01:21:16]** You can understand a paragraph,
**[01:21:18]** but you can't understand a word.
**[01:21:19]** There's reasoning, you can't do reasoning,
**[01:21:21]** but then suddenly it turns out
**[01:21:22]** you can do code and math very well at all.
**[01:21:24]** So I think there's actually a stronger history
**[01:21:29]** of some of these things seeming like a big deal
**[01:21:31]** and then kind of dissolving.
**[01:21:35]** Some of them are real.
**[01:21:36]** I mean, the need for data is real.
**[01:21:37]** Maybe continual learning is a real thing.
**[01:21:42]** But again, I would ground us in something like code.
**[01:21:45]** Like I think we may get to the point
**[01:21:48]** in like a year or two
**[01:21:49]** where the models can just do sui and end.
**[01:21:51]** Like that's a whole task.
**[01:21:53]** That's a whole sphere of human activity
**[01:21:56]** that we're just saying models can do it now.
**[01:21:59]** When you say end-to-end,
**[01:22:00]** do you mean setting technical direction,
**[01:22:03]** understanding the context of the problem, et cetera?
**[01:22:06]** Yes.
**[01:22:07]** Yes, I mean all of that.
**[01:22:07]** Interesting.
**[01:22:08]** I mean, that is, I feel like AGI complete.
**[01:22:13]** Maybe it's internally consistent,
**[01:22:15]** but it's not like saying 90% of code or 100% of code.
**[01:22:18]** It's like the other parts of the job as well.
**[01:22:20]** No, no, no.
**[01:22:21]** I gave this spectrum 90% of code, 100% of code,
**[01:22:25]** 90% of N10 suite, 100% of N10 suite,
**[01:22:29]** new tasks are created for sui's,
**[01:22:31]** eventually those get done as well.
**[01:22:32]** But it's a long spectrum there.
**[01:22:33]** But we're traversing the spectrum very quickly.
**[01:22:36]** I do think it's funny that I've seen a couple of podcasts
**[01:22:39]** you've done where the host will be like,
**[01:22:42]** but the podcast wrote this essay
**[01:22:43]** about the continual learning thing.
**[01:22:44]** And it always makes me crack up
**[01:22:45]** because you're like, you've been an AI researcher
**[01:22:47]** for like 10 years.
**[01:22:49]** I'm sure there's like some feeling of like,
**[01:22:52]** okay, so a podcaster wrote an essay.
**[01:22:54]** And like every interview I get asked about it.
**[01:22:57]** The truth of the matter is that we're all trying
**[01:22:59]** to figure this out together, right?
**[01:23:01]** There are some ways in which I'm able to see things
**[01:23:05]** that others aren't.
**[01:23:06]** These days that probably has more to do with like,
**[01:23:09]** I can see a bunch of stuff within Anthropic
**[01:23:11]** and have to make a bunch of decisions
**[01:23:13]** than I have any great research insight
**[01:23:15]** that others don't, right?
**[01:23:17]** I'm running a 2,500 person company.
**[01:23:19]** Like it's actually pretty hard for me
**[01:23:21]** to have concrete research insight,
**[01:23:25]** much harder than it would have been 10 years ago
**[01:23:29]** or even two or three years ago.
**[01:23:32]** As we go towards a world of a full drop-in
**[01:23:35]** remote worker replacement,
**[01:23:37]** does a API pricing model still make the most sense?
**[01:23:42]** And if not, what is the correct way to price AGI
**[01:23:44]** or serve AGI?
**[01:23:45]** Yeah, I mean, I think there's gonna be a bunch
**[01:23:47]** of different business models here,
**[01:23:48]** sort of all at once that are gonna be experimented with.
**[01:23:53]** I actually do think that the API model
**[01:24:00]** is more durable than many people think.
**[01:24:03]** One way I think about it is if the technology
**[01:24:06]** is kind of advancing quickly,
**[01:24:08]** if it's advancing exponentially,
**[01:24:10]** what that means is there's always kind of like
**[01:24:12]** a surface area of kind of new use cases
**[01:24:15]** that have been developed in the last three months.
**[01:24:19]** And any kind of product surface you put in place
**[01:24:22]** is always at risk of sort of becoming irrelevant, right?
**[01:24:27]** Any given product surface probably makes sense
**[01:24:29]** for a range of capabilities of the model, right?
**[01:24:33]** The chatbot is already running into limitations
**[01:24:36]** of making it smarter doesn't really help
**[01:24:39]** the average consumer that much.
**[01:24:41]** But I don't think that's a limitation of AI models.
**[01:24:43]** I don't think that's evidence
**[01:24:45]** that the models are good enough
**[01:24:47]** and them getting better doesn't matter to the economy.
**[01:24:51]** It doesn't matter to that particular product.
**[01:24:54]** And so I think the value of the API
**[01:24:57]** is the API always offers an opportunity,
**[01:25:01]** very close to the bare metal
**[01:25:03]** to build on what the latest thing is.
**[01:25:05]** And so there's kind of always gonna be this kind of front
**[01:25:11]** of new startups and new ideas
**[01:25:14]** that weren't possible a few months ago
**[01:25:15]** and are possible because the model is advancing.
**[01:25:18]** And so I actually, I kind of actually predict
**[01:25:23]** that we are, it's gonna exist alongside other models
**[01:25:27]** but we're always gonna have the API business model
**[01:25:31]** because there's always gonna be a need
**[01:25:33]** for a thousand different people to try experimenting
**[01:25:36]** with the model in different way.
**[01:25:37]** And a hundred of them become startups
**[01:25:40]** and 10 of them become big successful startups.
**[01:25:42]** And two or three really end up being the way
**[01:25:45]** that people use the model of a given generation.
**[01:25:48]** So I basically think it's always gonna exist.
**[01:25:50]** At the same time, I'm sure there's gonna be other models
**[01:25:54]** as well, like not every token that's output
**[01:25:58]** by the model is worth the same amount.
**[01:26:00]** Think about, what is the value of the tokens
**[01:26:04]** that are like, that the model outputs
**[01:26:07]** when someone calls them up and says,
**[01:26:11]** my Mac isn't working or something,
**[01:26:13]** the models like restart it, right?
**[01:26:14]** And like, someone hasn't heard that before,
**[01:26:17]** but like, the model said that like 10 million times, right?
**[01:26:23]** Maybe that's worth like a dollar
**[01:26:24]** or a few cents or something.
**[01:26:26]** Whereas if the model, the model goes
**[01:26:30]** to one of the pharmaceutical companies
**[01:26:34]** and it says, oh, this molecule you're developing,
**[01:26:36]** you should take the aromatic ring
**[01:26:38]** from that end of the molecule
**[01:26:39]** and put it on that end of the molecule.
**[01:26:41]** And if you do that, wonderful things will happen.
**[01:26:45]** Like those tokens could be worth,
**[01:26:48]** tens of millions of dollars, right?
**[01:26:51]** So I think we're definitely gonna see business models
**[01:26:54]** that recognize that, at some point we're gonna see,
**[01:26:59]** pay for results or in some form,
**[01:27:03]** or we may see forms of compensation that are like labor,
**[01:27:09]** that kind of work by the hour.
**[01:27:12]** I don't know, I think because it's a new industry,
**[01:27:17]** a lot of things are gonna be tried
**[01:27:18]** and I don't know what will turn out to be the right thing.
**[01:27:21]** What I find, I take your point that people
**[01:27:24]** will have to try things to figure out
**[01:27:25]** what is the best way to use this blob of intelligence.
**[01:27:28]** But what I find striking is Claude Code.
**[01:27:32]** So I don't think in the history of startups,
**[01:27:34]** there has been a single application
**[01:27:37]** that has been as hotly competed in as coding agents.
**[01:27:40]** And Claude Code is a category leader here.
**[01:27:47]** And that seems surprising to me.
**[01:27:49]** Like it doesn't seem intrinsically
**[01:27:50]** like Anthropic had to build this.
**[01:27:52]** And I wonder if you have an accounting
**[01:27:53]** of why it had to be Anthropic
**[01:27:55]** or how Anthropic ended up building an application
**[01:27:57]** in addition to the model underlying it.
**[01:27:59]** Yeah, so it actually happened in a pretty simple way,
**[01:28:02]** which is we had our own,
**[01:28:05]** you know, we had our coding models,
**[01:28:07]** which were good at coding.
**[01:28:08]** And, you know, around the beginning of 2025,
**[01:28:11]** I said, I think the time has come
**[01:28:13]** where you can have non-trivial acceleration
**[01:28:16]** of your own research if you're an AI company
**[01:28:20]** by using these models.
**[01:28:21]** And of course, you know, you need an interface,
**[01:28:23]** you need a harness to use them.
**[01:28:25]** And so I encourage people internally,
**[01:28:27]** and I didn't say this is one thing that,
**[01:28:28]** you know, that you have to use.
**[01:28:31]** I just said people should experiment with this.
**[01:28:34]** And then, you know, this thing,
**[01:28:36]** I think it might've been originally called Cloud CLI,
**[01:28:38]** and then the name eventually got changed
**[01:28:40]** to Cloud Code internally,
**[01:28:44]** was the thing that kind of everyone was using,
**[01:28:46]** and it was seeing fast internal adoption.
**[01:28:48]** And I looked at it and I said,
**[01:28:49]** probably we should launch this externally, right?
**[01:28:52]** You know, it's seen such fast adoption within Anthropic,
**[01:28:55]** like, you know, like, you know,
**[01:28:57]** coding is a lot of what we do.
**[01:28:59]** And so, you know, we have a audience
**[01:29:01]** of many, many hundreds of people
**[01:29:03]** that's in some ways at least representative
**[01:29:05]** of the external audience.
**[01:29:07]** So it looks like we already have product market fit.
**[01:29:08]** Let's launch this thing.
**[01:29:10]** And then we launched it.
**[01:29:11]** And I think, you know, just the fact that
**[01:29:15]** we ourselves are kind of developing the model
**[01:29:17]** and we ourselves know what we most need to use the model,
**[01:29:21]** I think it's kind of creating this feedback loop.
**[01:29:23]** I see, in the sense that you,
**[01:29:25]** let's say a developer at Anthropic is like,
**[01:29:27]** ah, it would be better if it was better at this X thing.
**[01:29:31]** And then you bake that into the next model that you build.
**[01:29:35]** That's one version of it.
**[01:29:36]** But then there's just the ordinary product iteration of like,
**[01:29:40]** you know, we have a bunch of coders within Anthropic.
**[01:29:43]** Like we, you know, they like use Cloud Code every day.
**[01:29:47]** And so we get fast feedback.
**[01:29:48]** That was more important in the early days.
**[01:29:50]** Now, of course, there are millions of people using it.
**[01:29:52]** And so we get a bunch of external feedback as well,
**[01:29:55]** but it's, you know, it's just great to be able to get,
**[01:29:57]** you know, kind of, kind of,
**[01:30:00]** fast, fast internal feedback.
**[01:30:02]** You know, I think this is the reason why we launched
**[01:30:04]** a coding model and, you know,
**[01:30:05]** didn't launch a pharmaceutical company, right?
**[01:30:08]** You know, my background's in biology,
**[01:30:12]** but like, we don't have any of the resources
**[01:30:14]** that are needed to launch a pharmaceutical company.
**[01:30:17]** So there's been a ton of hype around OpenClaw,
**[01:30:18]** and I wanted to check it out for myself.
**[01:30:20]** I've got a date coming up this weekend,
**[01:30:21]** and I don't have anything planned yet.
**[01:30:23]** So I gave OpenClaw a Mercury debit card.
**[01:30:26]** I set a couple hundred dollar limit,
**[01:30:27]** and I said, surprise me.
**[01:30:29]** Okay, so here's the Mac mini it's on,
**[01:30:31]** and besides having access to my Mercury,
**[01:30:33]** it's totally quarantined.
**[01:30:34]** And I actually felt quite comfortable
**[01:30:35]** giving it access to a debit card,
**[01:30:37]** because Mercury makes it super easy to set up guardrails.
**[01:30:39]** I was able to customize permissions,
**[01:30:41]** cap the spend, and restrict the category of purchases.
**[01:30:43]** I wanted to make sure the debit card worked,
**[01:30:45]** so I asked OpenClaw to just make a test transaction,
**[01:30:47]** and decided to donate a couple bucks to Wikipedia.
**[01:30:49]** Besides that, I have no idea what's gonna happen.
**[01:30:52]** I will report back on the next episode about how it goes.
**[01:30:54]** In the meantime, if you want a personal banking solution
**[01:30:57]** that can accommodate all the different ways
**[01:30:59]** that people use their money,
**[01:31:00]** even experimental ones like this one,
**[01:31:01]** visit mercury.com slash personal.
**[01:31:05]** Mercury is a fintech company, not an FDIC-insured bank.
**[01:31:09]** Banking services provided through Choice Financial Group
**[01:31:11]** and Column NA members FDIC.
**[01:31:14]** You know she thinks we're getting coffee
**[01:31:15]** and walking around the neighborhood.
**[01:31:16]** Let me ask you about now making AI go well.
**[01:31:24]** It seems like whatever vision we have
**[01:31:25]** about how AI goes well has to be compatible
**[01:31:29]** with two things.
**[01:31:30]** One is the ability to build and run AIs
**[01:31:33]** is diffusing extremely rapidly.
**[01:31:36]** And two is that the population of AIs,
**[01:31:38]** the amount we have in their intelligence,
**[01:31:41]** will also increase very rapidly.
**[01:31:43]** And that means that lots of people will be able
**[01:31:46]** to build huge populations of misaligned AIs,
**[01:31:49]** or AIs which are just like companies
**[01:31:51]** which are trying to increase their footprint,
**[01:31:54]** or have weird psyches like Sidney Bing,
**[01:31:56]** but now they're superhuman.
**[01:31:57]** What is a vision for a world in which
**[01:32:00]** we have an equilibrium that is compatible
**[01:32:02]** with lots of different AIs,
**[01:32:04]** some of which are misaligned running around?
**[01:32:05]** Yeah, yeah.
**[01:32:06]** So I think, you know, in the adolescence of technology,
**[01:32:08]** I was kind of, you know, skeptical of like
**[01:32:12]** the balance of power.
**[01:32:13]** But I think I was particularly skeptical of,
**[01:32:16]** or the thing I was specifically skeptical of
**[01:32:19]** is you have like three or four of these companies
**[01:32:22]** like kind of all building models that are kind of dry,
**[01:32:25]** you know, sort of like derived from the same thing.
**[01:32:33]** And, you know, that these would check each other,
**[01:32:36]** or even that kind of, you know,
**[01:32:37]** any number of them would check each other.
**[01:32:40]** Like we might live in a offense dominant world
**[01:32:43]** where, you know, like one person or one AI model
**[01:32:46]** is like smart enough to do something
**[01:32:47]** that like causes damage for everything else.
**[01:32:51]** I think in the, I mean, in the short run,
**[01:32:53]** we have a limited number of players now.
**[01:32:56]** So we can start by within the limited number of players,
**[01:32:58]** we, you know, we kind of, you know,
**[01:33:01]** we need to put in place the, you know, the safeguards.
**[01:33:03]** We need to make sure everyone does the right alignment work.
**[01:33:05]** We need to make sure everyone has bio classifiers like,
**[01:33:08]** you know, those are kind of the immediate things
**[01:33:10]** we need to do.
**[01:33:11]** I agree that, you know,
**[01:33:12]** that doesn't solve the problem in the long run,
**[01:33:14]** particularly if the ability of AI models
**[01:33:17]** to make other AI models proliferates,
**[01:33:19]** then, you know, the whole thing can kind of,
**[01:33:23]** you know, it can become harder to solve.
**[01:33:26]** You know, I think in the long run,
**[01:33:27]** we need some architecture of governance, right?
**[01:33:30]** Some architecture of governance
**[01:33:33]** that preserves human freedom,
**[01:33:34]** but kind of also allows us to like, you know,
**[01:33:38]** govern the very large number of kind of, you know,
**[01:33:44]** human systems, AI systems, hybrid human,
**[01:33:48]** human, you know, hybrid human AI,
**[01:33:53]** like, you know, companies or like economic units.
**[01:33:57]** So, you know, we're gonna need to think about like,
**[01:34:00]** you know, how do we protect the world against,
**[01:34:03]** you know, bioterrorism?
**[01:34:04]** How do we protect the world against like,
**[01:34:07]** you know, against like mirror life?
**[01:34:09]** Like, you know, probably we're gonna need to,
**[01:34:12]** you know, need some kind of like AI monitoring system
**[01:34:15]** that like, you know, kind of monitors
**[01:34:17]** for all of these things,
**[01:34:18]** but then we need to build this in a way that like,
**[01:34:21]** you know, preserves civil liberties
**[01:34:23]** and like our constitutional rights.
**[01:34:24]** So I think just as is anything else,
**[01:34:27]** like it's like a new security landscape
**[01:34:30]** with a new set of, you know,
**[01:34:34]** a new set of tools and a new set of vulnerabilities.
**[01:34:36]** And I think my worry is if we had a hundred years
**[01:34:40]** for this to happen all very slowly,
**[01:34:42]** we'd get used to it.
**[01:34:43]** You know, like we've gotten used to like,
**[01:34:45]** you know, the presence of, you know,
**[01:34:47]** the presence of explosives in society,
**[01:34:49]** or like, you know, the presence of various,
**[01:34:53]** you know, like new weapons,
**[01:34:54]** or the, you know, the presence of video cameras.
**[01:34:58]** We would get used to it over a hundred years
**[01:35:00]** and we'd develop governance mechanisms,
**[01:35:02]** we'd make our mistakes.
**[01:35:04]** My worry is just that this happening all so fast.
**[01:35:07]** And so I think maybe we need to do our thinking faster
**[01:35:10]** about how to make these governance mechanisms work.
**[01:35:12]** Yeah.
**[01:35:13]** It seems like in a offense dominant world,
**[01:35:17]** over the course of the next century,
**[01:35:18]** so the idea is the AI is making the progress
**[01:35:20]** that would happen over the next century
**[01:35:20]** happen in some period of five to 10 years.
**[01:35:23]** But we would still need the same mechanisms
**[01:35:26]** or balance of power would be similarly intractable,
**[01:35:29]** even if humans were the only game in town.
**[01:35:33]** And so I guess we have the advice of AI.
**[01:35:37]** It fundamentally doesn't seem like a
**[01:35:39]** totally different ballgame here.
**[01:35:41]** If checks and balances were gonna work,
**[01:35:42]** they would work with humans as well.
**[01:35:44]** If they aren't gonna work,
**[01:35:45]** they wouldn't work with the AIs as well.
**[01:35:47]** And so maybe this just dooms
**[01:35:49]** human checks and balances as well, but.
**[01:35:50]** Yeah, again, I think there's some way to,
**[01:35:53]** I think there's some way to make this happen.
**[01:35:55]** Like it, you know, it just, you know,
**[01:35:58]** the governments of the world may have to work together
**[01:36:00]** to make it happen.
**[01:36:01]** Like, you know, we may have to,
**[01:36:03]** you may have to talk to AIs about kind of, you know,
**[01:36:06]** building societal structures in such a way
**[01:36:09]** that like these defenses are possible.
**[01:36:11]** I don't know.
**[01:36:12]** I mean, this is so, this is, you know,
**[01:36:14]** I don't wanna say so far ahead in time,
**[01:36:15]** but like so far ahead in technological ability
**[01:36:19]** that may happen over a short period of time
**[01:36:21]** that it's hard for us to anticipate it in advance.
**[01:36:24]** Speaking of governments getting involved,
**[01:36:25]** on December 26th,
**[01:36:26]** the Tennessee legislature introduced a bill
**[01:36:29]** which said, quote,
**[01:36:31]** it would be an offense for a person
**[01:36:32]** to knowingly train artificial intelligence
**[01:36:34]** to provide emotional support,
**[01:36:36]** including through open-ended conversations with a user.
**[01:36:39]** And of course, one of the things that Claude attempts to do
**[01:36:42]** is be a thoughtful,
**[01:36:46]** thoughtful friend,
**[01:36:47]** thoughtful, knowledgeable friend.
**[01:36:48]** And in general, it seems like we're gonna have
**[01:36:50]** this patchwork of state laws.
**[01:36:52]** A lot of the benefits that normal people could experience
**[01:36:54]** as a result of AI are going to be curtailed,
**[01:36:56]** especially when we get into the kinds of things
**[01:36:58]** you discuss in Machines of Love and Grace,
**[01:37:00]** biological freedom, mental health improvements,
**[01:37:02]** et cetera, et cetera.
**[01:37:03]** It seems easier to imagine worlds
**[01:37:04]** in which these get whack them all the way by different laws.
**[01:37:08]** Whereas bills like this don't seem to address
**[01:37:11]** the actual existential threats that you're concerned about.
**[01:37:15]** So I'm curious to understand,
**[01:37:17]** in the context of things like this,
**[01:37:18]** your anthropic position against the federal moratorium
**[01:37:22]** on state AI laws.
**[01:37:23]** Yes.
**[01:37:24]** So I don't know.
**[01:37:25]** There's many different things going on at once, right?
**[01:37:27]** I think that particular law is dumb.
**[01:37:31]** Like, you know, I think it was clearly made by legislators
**[01:37:34]** who just probably had little idea
**[01:37:36]** what AI models could do and not do.
**[01:37:38]** They're like, AI models serving as,
**[01:37:39]** that just sounds scary.
**[01:37:41]** Like, I don't want that to happen.
**[01:37:42]** So, you know, we're not in favor of that, right?
**[01:37:46]** But that wasn't the thing that was being voted on.
**[01:37:50]** The thing that was being voted on
**[01:37:51]** is we're going to ban all state regulation of AI
**[01:37:55]** for 10 years with no apparent plan
**[01:37:59]** to do any federal regulation of AI,
**[01:38:01]** which would take Congress to pass,
**[01:38:03]** which is a very high bar.
**[01:38:05]** So, you know, the idea that we'd ban states
**[01:38:07]** from doing anything for 10 years,
**[01:38:09]** and people said they had a plan for federal government,
**[01:38:12]** but, you know, there was no actual,
**[01:38:13]** there was no proposal on the table.
**[01:38:15]** There was no actual attempt.
**[01:38:17]** Given the serious dangers that I lay out
**[01:38:20]** in adolescence of technology around things like the,
**[01:38:23]** you know, kind of biological weapons
**[01:38:25]** and bioterrorism, autonomy risk,
**[01:38:28]** and the timelines we've been talking about,
**[01:38:30]** like 10 years is an eternity.
**[01:38:32]** Like, that's a, I think that's a crazy thing to do.
**[01:38:36]** So if that's the choice,
**[01:38:38]** if that's what you force us to choose,
**[01:38:40]** then we're going to choose not to have that moratorium.
**[01:38:44]** And, you know, I think the benefits of that position
**[01:38:47]** exceed the costs,
**[01:38:48]** but it's not a perfect position if that's the choice.
**[01:38:51]** Now, I think the thing that we should do,
**[01:38:53]** the thing that I would support,
**[01:38:55]** is the federal government should step in,
**[01:38:58]** not saying states, you can't regulate,
**[01:39:00]** but here's what we're going to do,
**[01:39:02]** and states, you can't differ from this, right?
**[01:39:06]** Like, I think preemption is fine
**[01:39:08]** in the sense of saying that federal government says,
**[01:39:10]** here's our standards, this applies to everyone,
**[01:39:12]** states can't do something different.
**[01:39:14]** That would be something I would support
**[01:39:16]** if it would be done in the right way.
**[01:39:20]** But this idea of states, you can't do anything
**[01:39:22]** and we're not doing anything either,
**[01:39:24]** that struck us as, you know, very much not making sense.
**[01:39:29]** And I think we'll not age well,
**[01:39:30]** it's already starting to not age well
**[01:39:33]** with all the backlash that you've seen.
**[01:39:36]** Now, in terms of what we would want,
**[01:39:38]** I mean, you know, the things we've talked about
**[01:39:40]** are starting with transparency standards,
**[01:39:44]** you know, in order to monitor some of these autonomy risks
**[01:39:47]** and bioterrorism risks.
**[01:39:48]** As the risks become more serious,
**[01:39:51]** as we get more evidence for them,
**[01:39:54]** then I think we could be more aggressive
**[01:39:56]** in some targeted ways and say,
**[01:39:58]** hey, AI bioterrorism is really a threat,
**[01:40:01]** let's pass a law that kind of forces people
**[01:40:04]** to have classifiers.
**[01:40:05]** And I could even imagine, it depends,
**[01:40:07]** it depends how serious a threat it ends up being,
**[01:40:09]** we don't know for sure,
**[01:40:10]** then we need to pursue this in an intellectually honest way
**[01:40:13]** where we say ahead of time, the risk has not emerged yet.
**[01:40:16]** But I could certainly imagine
**[01:40:17]** with the pace that things are going,
**[01:40:19]** that, you know, I could imagine a world
**[01:40:21]** where later this year we say,
**[01:40:23]** hey, this AI bioterrorism stuff is really serious,
**[01:40:26]** we should do something about it.
**[01:40:28]** We should put it in a federal,
**[01:40:29]** we should, you know, put it in a federal standard
**[01:40:31]** and if the federal government won't act,
**[01:40:33]** we should put it in a state standard.
**[01:40:34]** I could totally see that.
**[01:40:36]** I'm concerned about a world where
**[01:40:39]** if you just consider the pace of progress you're expecting,
**[01:40:42]** the life cycle of legislation,
**[01:40:46]** you know, the benefits are,
**[01:40:47]** as you say, because of diffusion lag,
**[01:40:49]** the benefits are slow enough
**[01:40:50]** that I really do think this patchwork of,
**[01:40:53]** on the current trajectory,
**[01:40:54]** this patchwork of state laws would prohibit,
**[01:40:57]** I mean, having an emotional chatbot friend
**[01:40:59]** is something that freaks people out
**[01:41:00]** than just imagine the kinds of actual benefits from AI
**[01:41:03]** we want normal people to be able to experience
**[01:41:05]** from improvements in health and healthspan
**[01:41:08]** and improvements in mental health and so forth.
**[01:41:09]** Whereas at the same time,
**[01:41:12]** it seems like you think the dangers
**[01:41:13]** are already on the horizon
**[01:41:14]** and I just don't see that much.
**[01:41:18]** It seems like it would be especially injurious
**[01:41:20]** to the benefits of AI as compared to the dangers of AI.
**[01:41:23]** And so that's maybe where the cost-benefit
**[01:41:26]** makes less sense to me.
**[01:41:27]** So there's a few things here, right?
**[01:41:29]** I mean, people talk about
**[01:41:30]** there being thousands of these state laws.
**[01:41:33]** First of all, the vast, mass majority of them do not pass.
**[01:41:37]** And, you know, the world works a certain way in theory,
**[01:41:40]** but like, just because a law has been passed
**[01:41:43]** doesn't mean it's really enforced, right?
**[01:41:44]** The people implementing it may be like,
**[01:41:47]** oh my God, this is stupid.
**[01:41:48]** It would mean shutting off like, you know,
**[01:41:51]** everything that's ever been built
**[01:41:52]** and everything that's ever been built in Tennessee.
**[01:41:54]** So, you know, very often laws are interpreted in like,
**[01:41:57]** you know, a way that makes them not as dangerous
**[01:42:01]** or not as harmful.
**[01:42:02]** On the same side, of course, you have to worry
**[01:42:04]** if you're passing a law to stop a bad thing.
**[01:42:06]** You had this problem as well.
**[01:42:08]** Yeah.
**[01:42:10]** Look, my basic view is, you know,
**[01:42:13]** if we could decide, you know, what laws were passed
**[01:42:18]** and how things were done,
**[01:42:18]** which, you know, we're only one small input into that,
**[01:42:22]** you know, I would deregulate a lot of the stuff
**[01:42:26]** around the health benefits of AI.
**[01:42:28]** I think, you know, I don't worry as much
**[01:42:30]** about the like, the kind of chatbot laws.
**[01:42:34]** I actually worry more about the drug approval process
**[01:42:37]** where I think AI models are going to greatly accelerate
**[01:42:43]** the rate at which we discover drugs
**[01:42:45]** and just the pipeline will get jammed up.
**[01:42:47]** Like, the pipeline will not be prepared to like,
**[01:42:49]** process all of the stuff that's going through it.
**[01:42:52]** So, you know, I think reform of the regulatory process
**[01:42:58]** to buy us more towards, we have a lot of things coming
**[01:43:01]** where the safety and the efficacy
**[01:43:03]** is actually going to be really crisp and clear.
**[01:43:06]** Like, I mean, a beautiful thing,
**[01:43:07]** really, really crisp and clear and like really,
**[01:43:10]** really effective.
**[01:43:11]** But, you know, and maybe we don't need all this,
**[01:43:13]** all this like, all this superstructure around it
**[01:43:19]** that was designed around an era of drugs that barely work
**[01:43:22]** and often have serious side effects.
**[01:43:24]** But at the same time, I think we should be ramping up
**[01:43:27]** quite significantly the, you know,
**[01:43:32]** this kind of safety and security legislation.
**[01:43:34]** And, you know, like I've said, you know,
**[01:43:37]** starting with transparency is my view
**[01:43:40]** of trying not to hamper the industry, right?
**[01:43:43]** Trying to find the right balance.
**[01:43:44]** I'm worried about it.
**[01:43:45]** Some people criticize my essay for saying that's too slow.
**[01:43:49]** The dangers of AI will come too soon if we do that.
**[01:43:52]** Well, basically I kind of think like the last six months
**[01:43:55]** and maybe the next few months
**[01:43:56]** are going to be about transparency.
**[01:43:58]** And then if these risks emerge
**[01:44:01]** when we're more certain of them,
**[01:44:02]** which I think we might be as soon as later this year,
**[01:44:05]** then I think we need to act very fast
**[01:44:08]** in the areas that we've actually seen the risk.
**[01:44:09]** Like, I think the only way to do this is to be nimble.
**[01:44:13]** Now, the legislative process is normally not nimble,
**[01:44:16]** but we need to emphasize to everyone involved
**[01:44:20]** the urgency of this.
**[01:44:21]** That's why I'm sending this message of urgency, right?
**[01:44:24]** That's why I wrote Adolescence of Technology.
**[01:44:26]** I wanted policymakers to read it.
**[01:44:28]** I wanted economists to read it.
**[01:44:29]** I want national security professionals to read it.
**[01:44:32]** You know, I want decision makers to read it
**[01:44:35]** so that they have some hope of acting faster
**[01:44:37]** than they would have otherwise.
**[01:44:39]** Is there anything you can do or advocate
**[01:44:42]** that would make it more certain
**[01:44:46]** that the benefits of AI are better instantiated?
**[01:44:51]** I feel like you have worked with legislatures
**[01:44:54]** to be like, okay, we're going to prevent bioterrorism here.
**[01:44:56]** We're going to increase transparency.
**[01:44:57]** We're going to increase whistleblower protection.
**[01:44:59]** And I just think by default,
**[01:45:01]** the actual, like the things we're looking forward to here,
**[01:45:03]** it just seems very easy.
**[01:45:05]** They seem very fragile to different kinds of moral panics
**[01:45:09]** or political economy problems.
**[01:45:10]** Yeah, I don't actually,
**[01:45:11]** so I don't actually agree that much in the developed world.
**[01:45:14]** I feel like, you know, in the developed world,
**[01:45:17]** like markets function pretty well.
**[01:45:19]** When there's like a lot of money to be made on something
**[01:45:24]** and it's clearly the best available alternative,
**[01:45:26]** it's actually hard for the regulatory system to stop it.
**[01:45:29]** You know, we're seeing that in AI itself, right?
**[01:45:32]** I, you know, like a thing I've been trying to fight for
**[01:45:35]** is export controls on chips to China, right?
**[01:45:37]** And like, that's in the national security interests
**[01:45:40]** of the U.S.
**[01:45:41]** Like, you know, that's like square within the, you know,
**[01:45:45]** the policy beliefs of, you know,
**[01:45:47]** almost everyone in Congress of both parties,
**[01:45:50]** but, and you know, I think the case is very clear.
**[01:45:53]** The counter-arguments against it are,
**[01:45:55]** I'll politely call them fishy.
**[01:45:59]** And yet it doesn't happen and we sell the chips
**[01:46:02]** because there's so much money.
**[01:46:04]** There's so much money riding on it.
**[01:46:06]** And, you know, that money wants to be made.
**[01:46:09]** And in that case, in my opinion, that's a bad thing.
**[01:46:13]** But it also applies when it's a good thing.
**[01:46:16]** And so I don't think that if we're talking about drugs
**[01:46:21]** and benefits of the technology,
**[01:46:24]** I am not as worried about those benefits being hampered
**[01:46:29]** in the developed world.
**[01:46:30]** I am a little worried about them going too slow.
**[01:46:33]** And I, as I said, I do think we should work
**[01:46:36]** to speed the approval process in the FDA.
**[01:46:39]** I do think we should fight against these chatbot bills
**[01:46:42]** that you're describing, right, described individually.
**[01:46:45]** I'm against them.
**[01:46:46]** I think they're stupid.
**[01:46:47]** But I actually think the bigger worry is a developing world
**[01:46:51]** where we don't have functioning markets,
**[01:46:53]** where, you know, we often can't build on the technology
**[01:46:56]** that we've had.
**[01:46:58]** I worry more that those folks will get left behind.
**[01:47:01]** And I worry that even if the cures are developed,
**[01:47:03]** you know, maybe there's someone in rural Mississippi
**[01:47:05]** who doesn't get it as well, right?
**[01:47:06]** That's a kind of smaller version of the thing,
**[01:47:10]** the concern we have in the developing world.
**[01:47:12]** And so the things we've been doing are, you know,
**[01:47:15]** we work with, you know, we work with, you know,
**[01:47:18]** philanthropists, right?
**[01:47:19]** You know, we work with folks who, you know,
**[01:47:23]** who, you know, deliver, you know,
**[01:47:25]** medicine and health interventions to, you know,
**[01:47:28]** to developing world, to Sub-Saharan Africa, you know,
**[01:47:31]** India, Latin America, you know,
**[01:47:34]** you know, other developing parts of the world.
**[01:47:38]** That's the thing I think that won't happen on its own.
**[01:47:41]** You mentioned expert controls.
**[01:47:42]** Yeah.
**[01:47:43]** Why can't US and China both have a country of geniuses
**[01:47:46]** on a data center?
**[01:47:47]** Why can't, you know, why won't it happen?
**[01:47:49]** Or why shouldn't it?
**[01:47:50]** No, why shouldn't it happen?
**[01:47:51]** Why shouldn't it happen?
**[01:47:53]** You know, I think if this does happen, you know,
**[01:47:57]** then we kind of have a,
**[01:48:00]** well, we could have a few situations.
**[01:48:02]** If we have like an offense dominant situation,
**[01:48:04]** we could have a situation like nuclear weapons,
**[01:48:06]** but like more dangerous, right?
**[01:48:07]** Where it's like, you know, kind of either side
**[01:48:10]** could easily destroy everything.
**[01:48:13]** We could also have a world where it's kind of,
**[01:48:16]** it's unstable.
**[01:48:17]** Like the nuclear equilibrium is stable, right?
**[01:48:19]** Because it's, you know, it's like deterrence.
**[01:48:21]** But let's say there were uncertainty about like
**[01:48:24]** if the two AIs fought, which AI would win.
**[01:48:27]** That could create instability, right?
**[01:48:29]** You often have conflict when the two sides
**[01:48:31]** have a different assessment
**[01:48:32]** of their likelihood of winning, right?
**[01:48:34]** If one side is like, oh yeah, there's a 90% chance I'll win.
**[01:48:37]** And the other side's like, there's a 90% chance I'll win.
**[01:48:40]** Then a fight is much more likely.
**[01:48:42]** They can't both be right, but they can both think that.
**[01:48:44]** But this is like a fully general argument
**[01:48:46]** against the diffusion of AI technology,
**[01:48:49]** which that's the implication of this world.
**[01:48:51]** Let me just go on,
**[01:48:53]** because I think we will get diffusion eventually.
**[01:48:55]** The other concern I have is that people,
**[01:48:58]** the governments will oppress their own people with AI.
**[01:49:00]** And so, you know, I'm just,
**[01:49:04]** I'm worried about some world where you have a country
**[01:49:06]** that's already, you know, kind of, you know,
**[01:49:11]** you know, there's a government that kind of already,
**[01:49:14]** you know, is kind of building a, you know,
**[01:49:17]** a tech, a high-tech authoritarian state.
**[01:49:19]** And to be clear, this is about the government.
**[01:49:21]** This is not about the people.
**[01:49:22]** Like people, we need to find a way
**[01:49:24]** for people everywhere to benefit.
**[01:49:26]** My worry here is about governments.
**[01:49:28]** So yeah, you know, my worry is
**[01:49:30]** if the world gets carved up into two pieces,
**[01:49:32]** one of those two pieces could be authoritarian
**[01:49:35]** or totalitarian in a way that's very difficult to displace.
**[01:49:39]** Now, will governments eventually get powerful AI?
**[01:49:43]** And, you know, there's risk of authoritarianism, yes.
**[01:49:45]** Will governments eventually get powerful AI
**[01:49:47]** and there's risk of, you know,
**[01:49:51]** of kind of bad, bad, bad equilibria?
**[01:49:53]** Yes, I think both things,
**[01:49:55]** but the initial conditions matter, right?
**[01:49:57]** You know, at some point we're gonna need
**[01:50:00]** to set up the rules of the road.
**[01:50:02]** I'm not saying that one country,
**[01:50:04]** either the United States or a coalition of democracies,
**[01:50:07]** which I think would be a better setup,
**[01:50:09]** although it requires more international cooperation
**[01:50:11]** than we currently seem to wanna make.
**[01:50:13]** But, you know, I don't think a coalition of democracies
**[01:50:16]** or certainly one country should just say,
**[01:50:19]** these are the rules of the road.
**[01:50:20]** There's gonna be some negotiation, right?
**[01:50:22]** The world is gonna have to grapple with this.
**[01:50:25]** And what I would like is that the, you know,
**[01:50:29]** the democratic nations of the world,
**[01:50:31]** those with, you know, whose governments represent
**[01:50:36]** closer to pro-human values
**[01:50:38]** are holding the stronger hand then,
**[01:50:40]** have more leverage when the rules of the road are set.
**[01:50:43]** And so I'm very concerned about that initial condition.
**[01:50:47]** I was really listening to an interview from three years ago
**[01:50:49]** and one of the ways it aged poorly
**[01:50:52]** is that I kept asking questions
**[01:50:53]** assuming there was gonna be some key fulcrum moment
**[01:50:57]** two to three years from now,
**[01:50:58]** when in fact, being that far out,
**[01:50:59]** it just seems like progress continues, AI improves,
**[01:51:03]** AI is more diffused and people will use it for more things.
**[01:51:05]** It seems like you're imagining a world in the future
**[01:51:07]** where the countries get together
**[01:51:09]** and here's the rules of the road
**[01:51:10]** and here's the leverage we have, here's the leverage you have
**[01:51:13]** when it seems like on current trajectory,
**[01:51:15]** everybody will have more AI.
**[01:51:18]** Some of that AI will be used by authoritarian countries.
**[01:51:20]** Some of that within the authoritarian countries
**[01:51:21]** will be by private actors versus state actors.
**[01:51:24]** It's not clear who will benefit more.
**[01:51:26]** It's always unpredictable to tell in advance.
**[01:51:28]** It seems like the internet privileged
**[01:51:30]** authoritarian countries more than you would have expected
**[01:51:33]** and maybe the AI will be the opposite way around.
**[01:51:36]** So I wanna better understand what you're imagining here.
**[01:51:40]** Yeah, yeah.
**[01:51:40]** So just to be precise about it,
**[01:51:42]** I think the exponential of the underlying technology
**[01:51:45]** will continue as it has before, right?
**[01:51:47]** The models get smarter and smarter
**[01:51:49]** even when they get to country of geniuses in a data center.
**[01:51:53]** I think you can continue to make the model smarter.
**[01:51:56]** There's a question of like getting diminishing returns
**[01:51:59]** on their value in the world, right?
**[01:52:01]** How much does it matter
**[01:52:03]** after you've already solved human biology
**[01:52:05]** or at some point you can do harder math,
**[01:52:09]** you can do more abstruse math problems
**[01:52:10]** but nothing after that matters.
**[01:52:12]** But putting that aside,
**[01:52:13]** I do think the exponential will continue
**[01:52:17]** but there will be certain distinguished points
**[01:52:19]** on the exponential and companies, individuals,
**[01:52:23]** countries will reach those points at different times.
**[01:52:27]** And so, could there be some,
**[01:52:30]** I talk about is a nuclear deterrent still
**[01:52:33]** in adolescence of technology,
**[01:52:34]** is a nuclear deterrent still stable in the world of AI?
**[01:52:38]** I don't know, but that's an example
**[01:52:40]** of like one thing we've taken for granted
**[01:52:42]** that like the technology could reach such a level
**[01:52:44]** that it's no longer like,
**[01:52:46]** we can no longer be certain of it at least.
**[01:52:49]** Think of others,
**[01:52:51]** there are kind of points where
**[01:52:54]** if you reach a certain point,
**[01:52:56]** maybe you have offensive cyber dominance
**[01:52:58]** and like every computer system
**[01:53:00]** is transparent to you after that.
**[01:53:03]** Unless the other side has a kind of equivalent defense.
**[01:53:06]** So I don't know what the critical moment is
**[01:53:09]** or if there's a single critical moment
**[01:53:11]** but I think there will be either a critical moment,
**[01:53:14]** a small number of critical moments
**[01:53:16]** or some critical window where it's like
**[01:53:19]** AI confers some large advantage
**[01:53:25]** from the perspective of national security
**[01:53:27]** and one country or coalition has reached it before others.
**[01:53:34]** I'm not advocating that they're just like,
**[01:53:36]** okay, we're in charge now.
**[01:53:38]** That's not how I think about it.
**[01:53:41]** There's always the other side is catching up,
**[01:53:44]** there's extreme actions you're not willing to take
**[01:53:46]** and it's not right to take complete control anyway.
**[01:53:52]** But at the point that that happens,
**[01:53:54]** I think people are gonna understand
**[01:53:56]** that the world has changed.
**[01:53:57]** And there's gonna be some negotiation implicit or implicit
**[01:54:02]** about what is the post AI world order look like?
**[01:54:07]** And I think my interest is in making that negotiation
**[01:54:13]** be one in which classical liberal democracy
**[01:54:19]** has a strong hand.
**[01:54:21]** Well, I wanna understand what that better means
**[01:54:23]** because you say in the essay,
**[01:54:24]** quote, autocracy is simply not a form of government
**[01:54:28]** that people can accept in the post-powerful AI age.
**[01:54:31]** And that sounds like you're saying
**[01:54:33]** the CCP as an institution cannot exist after we get AGI.
**[01:54:38]** And that seems like a very strong demand
**[01:54:43]** and it seems to imply a world where the leading lab
**[01:54:45]** or the leading country will be able to,
**[01:54:49]** and by that language should,
**[01:54:51]** get to determine how the world is governed
**[01:54:53]** or what kinds of governments are allowed and not allowed.
**[01:54:57]** Yeah, so I believe that paragraph was,
**[01:55:03]** I think I said something like,
**[01:55:04]** you could take it even further and say X.
**[01:55:07]** So I wasn't necessarily endorsing that view.
**[01:55:12]** I was saying like, here's a weaker thing that I believe,
**[01:55:17]** I think I said, we have to worry a lot about authoritarians
**[01:55:21]** and we should try and kind of check them
**[01:55:24]** and limit their power.
**[01:55:25]** Like you could take this kind of further,
**[01:55:27]** much more interventionist view that says like,
**[01:55:30]** authoritarian countries with AI are the,
**[01:55:33]** these kind of self-fulfilling cycles that you can't,
**[01:55:36]** that are very hard to displace.
**[01:55:37]** And so you just need to get rid of them from the beginning.
**[01:55:40]** That has exactly all the problems you say,
**[01:55:42]** which is, if you were to make a commitment
**[01:55:45]** to overthrowing every authoritarian country,
**[01:55:47]** I mean, then they would take a bunch of actions now
**[01:55:50]** that like, that could lead to instability.
**[01:55:53]** So that may or, that just may not be possible.
**[01:55:59]** But the point I was making is that,
**[01:56:01]** it is quite possible that, you know, today, you know,
**[01:56:06]** the view, or at least my view,
**[01:56:08]** or the view in most of the Western world is,
**[01:56:10]** democracy is a better form of government
**[01:56:11]** than authoritarianism.
**[01:56:13]** But it's not like if a country's authoritarian,
**[01:56:16]** we don't react the way we reacted
**[01:56:18]** if they committed a genocide or something, right?
**[01:56:21]** And I guess what I'm saying is I'm a little worried
**[01:56:24]** that in the age of AGI,
**[01:56:26]** authoritarianism will have a different meaning.
**[01:56:28]** It will be a graver thing.
**[01:56:30]** And we have to decide one way or another
**[01:56:32]** how to deal with that.
**[01:56:34]** And the interventionist view is one possible view.
**[01:56:37]** I was exploring such views.
**[01:56:39]** You know, it may end up being the right view.
**[01:56:43]** It may end up being too extreme to be the right view,
**[01:56:45]** but I do have hope.
**[01:56:47]** And one piece of hope I have is,
**[01:56:50]** there is a way to deal with authoritarianism
**[01:56:55]** but there is, we have seen that
**[01:56:58]** as new technologies are invented,
**[01:57:02]** forms of government become obsolete.
**[01:57:04]** I mentioned this in Adolescence of Technology
**[01:57:08]** where I said, you know, like feudalism was basically,
**[01:57:11]** you know, like a form of government, right?
**[01:57:12]** And then when we invented industrialization,
**[01:57:17]** feudalism was no longer sustainable,
**[01:57:19]** no longer made sense.
**[01:57:21]** Why is that hope?
**[01:57:22]** Couldn't that imply that democracy
**[01:57:23]** is no longer gonna be a competitive system?
**[01:57:26]** Right, it could go either way, right?
**[01:57:30]** But I actually, so these problems with authoritarianism,
**[01:57:36]** right, that the problems of authoritarianism get deeper.
**[01:57:40]** I just, I wonder if that's an indicator
**[01:57:44]** of other problems that authoritarianism will have, right?
**[01:57:47]** In other words, people become,
**[01:57:50]** because authoritarianism becomes worse,
**[01:57:54]** people are more afraid of authoritarianism.
**[01:57:56]** They work harder to stop it.
**[01:57:58]** It's more of a, like you have to think
**[01:58:00]** in terms of total equilibrium, right?
**[01:58:03]** I just wonder if it will motivate new ways
**[01:58:07]** of thinking about, with the new technology,
**[01:58:11]** how to preserve and protect freedom.
**[01:58:13]** And even more optimistically,
**[01:58:15]** will it lead to a collective reckoning
**[01:58:18]** or a kind of a more emphatic realization
**[01:58:23]** of how important some of the things we take
**[01:58:25]** as individual rights are, right?
**[01:58:27]** A more emphatic realization that we just,
**[01:58:30]** we really can't give these away.
**[01:58:32]** There's, we've seen,
**[01:58:33]** there's no other way to live that actually works.
**[01:58:36]** I am actually hopeful that,
**[01:58:42]** I guess one way to say it, it sounds too idealistic,
**[01:58:45]** but I actually believe it could be the case,
**[01:58:47]** is that dictatorships become morally obsolete.
**[01:58:50]** They become morally unworkable forms of government.
**[01:58:54]** And that the crisis that that creates
**[01:58:58]** is sufficient to force us to find another way.
**[01:59:03]** I think there is genuinely a tough question here,
**[01:59:05]** which I'm not sure how you resolve.
**[01:59:07]** And we've had to come out one way or another
**[01:59:10]** on it through history, right?
**[01:59:11]** So with China in the 70s and 80s, we decided,
**[01:59:14]** even though it's an authoritarian system,
**[01:59:16]** we will engage with it.
**[01:59:17]** And I think in retrospect, that was the right call
**[01:59:18]** because it has stayed an authoritarian system,
**[01:59:20]** but a billion plus people are much wealthier
**[01:59:23]** and better off than they would have otherwise been.
**[01:59:25]** And it's not clear that it would have stopped
**[01:59:27]** being an authoritarian country.
**[01:59:28]** Otherwise, you can just look at North Korea
**[01:59:30]** as an example of that, right?
**[01:59:32]** And I don't know if that takes that much intelligence
**[01:59:35]** to remain an authoritarian country
**[01:59:37]** that continues to coalesce its own power.
**[01:59:40]** As you can just imagine a North Korea
**[01:59:42]** with an AI that's much worse than everybody else's,
**[01:59:44]** but still enough to keep power.
**[01:59:46]** And so in general, it seems like,
**[01:59:49]** should we just have this attitude of the benefits of AI
**[01:59:52]** will in the form of all of these empowerments of humanity
**[01:59:55]** and health and so forth will be big.
**[01:59:57]** And in historically we have decided.
**[02:00:00]** it's good to spread the benefits of technology widely,
**[02:00:02]** even to people whose governments are authoritarian.
**[02:00:05]** And I think, I guess it is a tough question
**[02:00:06]** how to think about it with AI,
**[02:00:07]** but historically we have said, yes,
**[02:00:10]** this is a positive some world
**[02:00:12]** and it's still worth defusing the technology.
**[02:00:14]** Yeah, so there are a number of choices we have.
**[02:00:16]** I think framing this as a kind of
**[02:00:19]** government to government decision
**[02:00:22]** and in national security terms,
**[02:00:25]** that's like one lens, but there are a lot of other lenses.
**[02:00:27]** Like you could imagine a world where
**[02:00:29]** we produce all these cures to diseases
**[02:00:31]** and like the cures to diseases
**[02:00:34]** are fine to sell to authoritarian countries,
**[02:00:36]** the data centers just aren't, right?
**[02:00:38]** The chips and the data centers just aren't.
**[02:00:40]** And the AI industry itself.
**[02:00:43]** You know, like another possibility is,
**[02:00:46]** and I think folks should think about this,
**[02:00:48]** like, you know, could there be developments we can make
**[02:00:52]** either that naturally happened as a result of AI
**[02:00:55]** or that we could make happen by building technology on AI?
**[02:01:00]** Could we create an equilibrium
**[02:01:02]** where it becomes infeasible for authoritarian countries
**[02:01:06]** to deny their people
**[02:01:07]** kind of private use of the benefits of the technology?
**[02:01:11]** You know, are there equilibria where we can kind of
**[02:01:15]** give everyone in an authoritarian country
**[02:01:17]** their own AI model that kind of,
**[02:01:19]** you know, like defends themselves from surveillance
**[02:01:22]** and there isn't a way for the authoritarian country
**[02:01:24]** to like crack down on this while retaining power?
**[02:01:28]** It sounds to me like if that went far enough,
**[02:01:29]** it would be a reason why authoritarian countries
**[02:01:32]** would disintegrate from the inside.
**[02:01:34]** But maybe there's a middle world where like,
**[02:01:37]** there's an equilibrium where if they want to hold on
**[02:01:39]** to power, the authoritarians can't deny
**[02:01:42]** kind of individualized access to the technology.
**[02:01:45]** But I actually do have a hope for the more radical version,
**[02:01:49]** which is, you know, is it possible that the technology
**[02:01:52]** might inherently have properties
**[02:01:54]** or that by building on it in certain ways
**[02:01:56]** we could create properties that have this kind of
**[02:02:01]** dissolving effect on authoritarian structures?
**[02:02:03]** Now, we hoped originally, right?
**[02:02:06]** We think back to the beginning of the Obama administration,
**[02:02:08]** we thought originally that, you know, social media
**[02:02:12]** and the internet would have that property,
**[02:02:14]** turns out not to.
**[02:02:15]** But I don't know, what if we could try again
**[02:02:19]** with the knowledge of how many things could go wrong
**[02:02:21]** and that this is a different technology?
**[02:02:23]** I don't know that it would work, but it's worth a try.
**[02:02:25]** Yeah, I think it's just, it's very unpredictable.
**[02:02:28]** Like there's first principles reasons
**[02:02:29]** why authoritarianism might be privileged.
**[02:02:30]** It's all very unpredictable.
**[02:02:32]** I don't think, I mean, we got it, we just got to,
**[02:02:35]** we kind of, we got to recognize the problem
**[02:02:38]** and then we got to come up with 10 things we can try
**[02:02:40]** and we got to try those and then assess
**[02:02:41]** whether they're working or which ones are working,
**[02:02:43]** if any, and then try new ones if the old ones aren't working.
**[02:02:46]** But I guess what that nets out to today is you say,
**[02:02:49]** we will not sell data centers, or sorry, chips
**[02:02:52]** and then the ability to make chips to China.
**[02:02:55]** And so in some sense, you are denying
**[02:02:57]** there'll be some benefits to the Chinese economy,
**[02:03:00]** Chinese people, et cetera, because we're doing that.
**[02:03:02]** And then there'd also be benefits to the American economy
**[02:03:04]** because it's a positive sum world, we could trade,
**[02:03:07]** they could have their country's data centers
**[02:03:08]** doing one thing, we could have ours doing another.
**[02:03:10]** And already you're saying it's not worth
**[02:03:13]** that positive sum stipend to empower this country.
**[02:03:19]** What I would say is that, you know,
**[02:03:21]** we are about to be in a world where growth
**[02:03:24]** and economic value will come very easily, right?
**[02:03:27]** If we're able to build these powerful AI models,
**[02:03:29]** growth and economic value will come very easily.
**[02:03:32]** What will not come easily is distribution of benefits,
**[02:03:36]** distribution of wealth, political freedom.
**[02:03:40]** You know, these are the things
**[02:03:41]** that are gonna be hard to achieve.
**[02:03:42]** And so when I think about policy,
**[02:03:45]** I think that the technology in the market
**[02:03:49]** will deliver all the fundamental benefits, you know,
**[02:03:51]** almost faster than we can take them.
**[02:03:55]** And that these questions about distribution
**[02:03:58]** and political freedom and rights
**[02:04:00]** are the ones that will actually matter
**[02:04:03]** and that policy should focus on.
**[02:04:04]** Okay, so speaking of distribution,
**[02:04:06]** as you were mentioning, we have developing countries
**[02:04:08]** and in many cases, catch-up growth has been weaker
**[02:04:13]** than we would have hoped for.
**[02:04:14]** But when catch-up growth does happen,
**[02:04:15]** it's fundamentally because they have underutilized labor
**[02:04:18]** and we can bring the capital and know-how
**[02:04:19]** from developed countries to these countries
**[02:04:21]** and then they can grow quite rapidly.
**[02:04:23]** Obviously, in a world where labor
**[02:04:25]** is no longer the constraining factor,
**[02:04:28]** this mechanism no longer works.
**[02:04:30]** And so is the hope basically to rely on philanthropy
**[02:04:33]** from the people who immediately get wealthy from AI
**[02:04:35]** or from the countries that get wealthy from AI?
**[02:04:37]** What is the hope for-
**[02:04:38]** I mean, philanthropy should obviously play some role
**[02:04:41]** as it has in the past,
**[02:04:44]** but I think growth is always better and stronger
**[02:04:48]** if we can make it endogenous.
**[02:04:49]** So what are the relevant industries
**[02:04:51]** in like an AI-driven world?
**[02:04:54]** Look, there's lots of stuff.
**[02:04:56]** You know, I said we shouldn't build data centers in China,
**[02:04:59]** but there's no reason we shouldn't build data centers
**[02:05:01]** in Africa, right?
**[02:05:03]** In fact, I think it'd be great
**[02:05:04]** to build data centers in Africa.
**[02:05:05]** You know, as long as they're not owned by China,
**[02:05:07]** we should build data centers in Africa.
**[02:05:10]** I think that's a great thing to do.
**[02:05:14]** We should also build, you know,
**[02:05:16]** there's no reason we can't build, you know,
**[02:05:18]** a pharmaceutical industry that's like AI-driven.
**[02:05:21]** Like, you know, if AI is accelerating drug discovery,
**[02:05:26]** then, you know, there'll be a bunch of biotech startups.
**[02:05:28]** Like, let's make sure some of those happen
**[02:05:30]** in the developing world.
**[02:05:30]** And certainly during the transition,
**[02:05:33]** I mean, we can talk about the point where humans
**[02:05:34]** have no role, but humans will still have some role
**[02:05:37]** in starting up these companies
**[02:05:38]** and supervising the AI models.
**[02:05:41]** So let's make sure some of those humans
**[02:05:42]** are humans in the developing world
**[02:05:44]** so that fast growth can happen there as well.
**[02:05:46]** You guys recently announced
**[02:05:47]** Quad is going to have a constitution
**[02:05:48]** that's aligned to a set of values
**[02:05:49]** and not necessarily just to the end user.
**[02:05:52]** And there's a world you can imagine
**[02:05:54]** where if it is aligned to the end user,
**[02:05:56]** it preserves the balance of power we have in the world today
**[02:05:58]** because everybody gets to have their own AI
**[02:06:00]** that's advocating for them.
**[02:06:01]** And so the ratio of bad actors to good actors stays constant.
**[02:06:04]** It seems to work out for our world today.
**[02:06:07]** Why is it better not to do that,
**[02:06:09]** but to have a specific set of values
**[02:06:12]** that the AI should carry forward?
**[02:06:14]** Yeah, so I'm not sure
**[02:06:16]** I'd quite draw the distinction in that way.
**[02:06:19]** There may be two relevant distinctions here,
**[02:06:21]** which are, I think you're talking about a mix of the two.
**[02:06:24]** Like one is, should we give the model
**[02:06:27]** a set of instructions about do this versus don't do this?
**[02:06:31]** And the other, you know,
**[02:06:32]** versus should we give the model a set of principles
**[02:06:35]** for, you know, for kind of how to act?
**[02:06:38]** And there it's, you know,
**[02:06:41]** it's just, it's kind of purely a practical
**[02:06:45]** and empirical thing that we've observed
**[02:06:48]** that by teaching the model principles,
**[02:06:50]** getting it to learn from principles,
**[02:06:52]** its behavior is more consistent,
**[02:06:54]** it's easier to cover edge cases,
**[02:06:56]** and the model is more likely to do what people want it to do.
**[02:07:00]** In other words, if you're like, you know,
**[02:07:02]** don't tell people how to hotwire a car,
**[02:07:04]** don't speak in Korean, don't, you know,
**[02:07:07]** just, you know, if you give it a list of rules,
**[02:07:10]** it doesn't really understand the rules
**[02:07:11]** and it's kind of hard to generalize from them.
**[02:07:14]** You know, if it's just kind of a like, you know,
**[02:07:17]** list of do's and don'ts,
**[02:07:18]** whereas if you give it principles and then, you know,
**[02:07:21]** it has some hard guardrails,
**[02:07:22]** like don't make biological weapons,
**[02:07:24]** but overall you're trying to understand
**[02:07:27]** what it should be aiming to do,
**[02:07:28]** how it should be aiming to operate.
**[02:07:31]** So just from a practical perspective,
**[02:07:32]** that turns out to be just a more effective way
**[02:07:34]** to train the model.
**[02:07:35]** That's one piece of it.
**[02:07:36]** So that, you know,
**[02:07:37]** that's the kind of rules versus principles trade-off.
**[02:07:40]** Then there's another thing you're talking about,
**[02:07:42]** which is kind of like the corrigibility versus like,
**[02:07:46]** you know, I would say kind of intrinsic motivation trade-off,
**[02:07:50]** which is like, how much should the model be a kind of,
**[02:07:54]** I don't know, like a skin suit or something where,
**[02:07:56]** you know, you just kind of, you know,
**[02:08:00]** it just kind of directly follows the instructions
**[02:08:02]** that are given to it
**[02:08:03]** by whoever is giving it those instructions,
**[02:08:06]** versus how much should the model
**[02:08:07]** have an inherent set of values
**[02:08:09]** and go off and do things on its own.
**[02:08:12]** And there, I would actually say,
**[02:08:17]** everything about the model
**[02:08:18]** is actually closer to the direction of like,
**[02:08:21]** you know, it should mostly do what people want.
**[02:08:23]** It should mostly follow these.
**[02:08:24]** We're not trying to build something that like,
**[02:08:26]** you know, goes off and runs the world on its own.
**[02:08:29]** We're actually pretty far on the corrigible side.
**[02:08:31]** Now, what we do say is there are certain things
**[02:08:34]** that the model won't do, right?
**[02:08:37]** That it's like, you know, that,
**[02:08:38]** and I think we say it in various ways in the constitution,
**[02:08:41]** that under normal circumstances,
**[02:08:42]** if someone asks the model to do a task,
**[02:08:44]** it should do that task.
**[02:08:45]** That should be the default.
**[02:08:48]** But if you've asked it to do something dangerous,
**[02:08:51]** or if you've, you know, if you've asked it to,
**[02:08:55]** you know, to kind of harm someone else,
**[02:08:59]** then the model is unwilling to do that.
**[02:09:01]** So I actually think of it as like a mostly,
**[02:09:04]** a mostly corrigible model that has some limits,
**[02:09:07]** but those limits are based on principles.
**[02:09:10]** Yeah, I mean, then the fundamental question is,
**[02:09:12]** how are those principles determined?
**[02:09:14]** And this is not a special question for Anthropic.
**[02:09:15]** This would be a question for any company,
**[02:09:17]** but because you have been the ones
**[02:09:20]** to actually write down the principles,
**[02:09:23]** I get to ask you this question.
**[02:09:25]** Normally a constitution is like,
**[02:09:27]** you write it down, it's set in stone,
**[02:09:28]** and there's a process of updating it
**[02:09:30]** and changing it and so forth.
**[02:09:32]** In this case, it seems like a document
**[02:09:34]** that people at Anthropic write
**[02:09:36]** that can be changed at any time,
**[02:09:37]** that guides the behavior of systems
**[02:09:40]** that are gonna be the basis of a lot of economic activity.
**[02:09:44]** What is the, how do you think about
**[02:09:47]** how those principles should be set?
**[02:09:49]** Yes, so I think there's two,
**[02:09:52]** there's maybe three kind of sizes of loop here, right?
**[02:09:56]** Three ways to iterate.
**[02:09:58]** One is you can iterate, we iterate within Anthropic,
**[02:10:00]** we train the model, we're not happy with it,
**[02:10:01]** and we kind of change the constitution.
**[02:10:03]** And I think that's good to do.
**[02:10:05]** And putting out publicly,
**[02:10:08]** making updates to the constitution every once in a while,
**[02:10:10]** saying here's a new constitution.
**[02:10:11]** I think that's good to do,
**[02:10:12]** because people can comment on it.
**[02:10:14]** The second level of loop is different companies
**[02:10:16]** will have different constitutions.
**[02:10:19]** And I think it's useful for Anthropic
**[02:10:21]** puts out a constitution,
**[02:10:22]** and the Gemini model puts out a constitution,
**[02:10:26]** and other companies put out a constitution,
**[02:10:28]** and then they can kind of look at them,
**[02:10:30]** compare, outside observers can critique,
**[02:10:33]** and say this, I like this one,
**[02:10:35]** this thing from this constitution,
**[02:10:37]** and this thing for that constitution.
**[02:10:39]** And then kind of that,
**[02:10:40]** that creates some kind of soft incentive
**[02:10:43]** and feedback for all the companies
**[02:10:45]** to like take the best of each elements and improve.
**[02:10:47]** Then I think there's a third loop,
**[02:10:49]** which is society beyond the AI companies
**[02:10:52]** and beyond just those who kind of,
**[02:10:54]** who comment on the constitutions without hard power.
**[02:10:58]** And there, we've done some experiments,
**[02:11:01]** like a couple of years ago,
**[02:11:02]** we did an experiment with,
**[02:11:03]** I think it was called the Collective Intelligence Project
**[02:11:06]** to like, to basically poll people
**[02:11:09]** and ask them what should be in our AI constitution.
**[02:11:13]** And I think at the time we incorporated
**[02:11:16]** some of those changes.
**[02:11:17]** And so you could imagine with the new approach
**[02:11:19]** we've taken to the constitution,
**[02:11:21]** doing something like that.
**[02:11:22]** It's a little harder because it's like,
**[02:11:24]** that was actually an easier approach to take
**[02:11:25]** when the constitution was like a list of do's and don'ts.
**[02:11:29]** At the level of principles,
**[02:11:30]** it has to have a certain amount of coherence,
**[02:11:32]** but you could still imagine getting views
**[02:11:35]** from a wide variety of people.
**[02:11:37]** And I think you could also imagine,
**[02:11:39]** and this is like a crazy idea,
**[02:11:40]** but hey, this whole interview is about crazy ideas, right?
**[02:11:43]** So, you could even imagine systems
**[02:11:47]** of kind of representative government having input, right?
**[02:11:50]** Like, I wouldn't do this today
**[02:11:53]** because the legislative process is so slow.
**[02:11:55]** This is exactly why I think we should be careful
**[02:11:57]** about the legislative process and AI regulation,
**[02:12:00]** but there's no reason you couldn't in principle say like,
**[02:12:02]** you know, all AI models have to have a constitution
**[02:12:07]** that starts with like these things.
**[02:12:09]** And then like, you can append other things after it,
**[02:12:12]** but like there has to be this special section
**[02:12:14]** that like takes precedence.
**[02:12:16]** I wouldn't do that.
**[02:12:16]** That's too rigid.
**[02:12:17]** That sounds kind of overly prescriptive
**[02:12:23]** in a way that I think overly aggressive legislation is,
**[02:12:26]** but like that is a thing you could, you know,
**[02:12:28]** like that is a thing you could try to do.
**[02:12:30]** Is there some much less heavy-handed version of that?
**[02:12:33]** Maybe.
**[02:12:34]** I really like control loop too,
**[02:12:37]** where obviously this is not how constitutions
**[02:12:39]** of actual governments do or should work,
**[02:12:41]** where there's not this vague sense
**[02:12:43]** in which the Supreme Court will feel out
**[02:12:46]** how people are feeling and what are the vibes
**[02:12:48]** and then update the constitution accordingly.
**[02:12:50]** So there's, with actual governments,
**[02:12:51]** there's a more procedural process.
**[02:12:53]** More formal process.
**[02:12:54]** Yeah, exactly.
**[02:12:55]** But you actually have a vision of competition
**[02:12:59]** between constitutions, which is actually very reminiscent
**[02:13:01]** of how some libertarian charter cities people
**[02:13:04]** used to talk about what an archipelago
**[02:13:07]** of different kinds of governments could look like.
**[02:13:08]** And then there'd be selection among them
**[02:13:10]** of who could operate the most effectively,
**[02:13:12]** in which place people would be the happiest.
**[02:13:14]** And in a sense you're actually, yeah, there's this vision.
**[02:13:18]** I'm kind of recreating that.
**[02:13:19]** Yeah, yeah, like the utopia of archipelagos.
**[02:13:22]** Again, I think that vision has things to recommend it
**[02:13:26]** and things that will kind of go wrong with it.
**[02:13:30]** I think it's an interesting and in some ways
**[02:13:33]** compelling vision, but also things will go wrong with it
**[02:13:35]** that you hadn't imagined.
**[02:13:37]** So I like loop two as well,
**[02:13:40]** but I feel like the whole thing has got to be
**[02:13:43]** some mix of loops one, two, and three,
**[02:13:46]** and it's a matter of the proportions, right?
**[02:13:48]** I think that's gotta be the answer.
**[02:13:53]** When somebody eventually writes the equivalent
**[02:13:55]** of the making of the atomic bomb for this era,
**[02:13:58]** what is the thing that will be hardest to glean
**[02:14:01]** from the historical record that they're most likely to miss?
**[02:14:04]** I think a few things.
**[02:14:05]** One is at every moment of this exponential,
**[02:14:09]** the extent to which the world outside it
**[02:14:11]** didn't understand it.
**[02:14:12]** This is a bias that's often present in history
**[02:14:14]** where anything that actually happened
**[02:14:17]** looks inevitable in retrospect.
**[02:14:19]** And so, I think when people look back,
**[02:14:23]** it will be hard for them to put themselves in the place
**[02:14:27]** of people who were actually making a bet
**[02:14:31]** on this thing to happen that wasn't inevitable,
**[02:14:35]** that we had these arguments,
**[02:14:36]** like the arguments that I make for scaling
**[02:14:38]** or that continual learning will be solved,
**[02:14:42]** that some of us internally in our heads
**[02:14:47]** put a high probability on this happening,
**[02:14:49]** but it's like, there's a world outside us
**[02:14:52]** that's not acting on,
**[02:14:54]** that's kind of not acting on that at all.
**[02:14:57]** And I think the weirdness of it,
**[02:15:01]** I think, unfortunately, like the insularity of it,
**[02:15:04]** like if we're one year or two years away from it happening,
**[02:15:09]** like the average person on the street has no idea.
**[02:15:12]** And that's one of the things I'm trying to change,
**[02:15:13]** like with the memos, with talking to policymakers,
**[02:15:16]** but like, I don't know, I think that's just like a crazy,
**[02:15:21]** that's just like a crazy thing.
**[02:15:24]** Finally, I would say, and this probably applies
**[02:15:28]** to almost all historical moments of crisis,
**[02:15:31]** how absolutely fast it was happening,
**[02:15:33]** how everything was happening all at once.
**[02:15:36]** And so, decisions that you might think
**[02:15:39]** were kind of carefully calculated,
**[02:15:41]** well, actually you have to make that decision
**[02:15:42]** and then you have to make 30 other decisions
**[02:15:44]** on the same day because it's all happening so fast.
**[02:15:47]** And you don't even know which decisions
**[02:15:49]** are gonna turn out to be consequential.
**[02:15:51]** So, one of my, I guess, worries,
**[02:15:54]** although it's also an insight into kind of what's happening
**[02:15:59]** is that some very critical decision
**[02:16:02]** will be some decision that someone just comes into my office
**[02:16:05]** and is like, Dario, you have two minutes,
**[02:16:07]** like, should we do thing A or thing B on this,
**[02:16:14]** someone gives me this random half page memo
**[02:16:17]** and is like, should we do A or B?
**[02:16:20]** And I'm like, I don't know, I have to eat lunch,
**[02:16:21]** let's do B.
**[02:16:22]** And that ends up being the most consequential thing ever.
**[02:16:26]** So, final question.
**[02:16:28]** It seems like you have, there's not tech CEOs
**[02:16:32]** who are usually writing 50 page memos every few months.
**[02:16:35]** And it seems like you have managed to build a role
**[02:16:38]** for yourself and a company around you,
**[02:16:40]** which is compatible with this more intellectual type
**[02:16:45]** role as CEO.
**[02:16:47]** And I wanna understand how you construct that
**[02:16:49]** and how, like, how does that work to be,
**[02:16:52]** you just go away for a couple of weeks
**[02:16:54]** and then you tell your company, this is the memo,
**[02:16:55]** like, here's what we're doing.
**[02:16:56]** It's also reported that you write
**[02:16:57]** a bunch of these internally.
**[02:16:58]** Yeah, so, I mean, for this particular one,
**[02:17:00]** I wrote it over winter break.
**[02:17:02]** So there was the time, and I was having a hard time
**[02:17:05]** finding the time to actually find it, to actually write it.
**[02:17:08]** But I actually think about this in a broader way.
**[02:17:11]** I actually think it relates to the culture of the company.
**[02:17:13]** So I probably spend a third, maybe 40% of my time
**[02:17:16]** making sure the culture of Enthropic is good.
**[02:17:19]** As Enthropic has gotten larger,
**[02:17:21]** it's gotten harder to just get involved in like,
**[02:17:25]** directly involved in like the training of the models,
**[02:17:27]** the launch of the models, the building of the products.
**[02:17:29]** Like it's 2,500 people.
**[02:17:31]** It's like, there's just, I have certain instincts,
**[02:17:34]** but like there's only, it's very difficult
**[02:17:37]** to get involved in every single detail.
**[02:17:40]** I like, I try as much as possible.
**[02:17:42]** But one thing that's very leveraged
**[02:17:44]** is making sure Enthropic is a good place to work.
**[02:17:47]** People like working there.
**[02:17:49]** Everyone thinks of themselves as team members.
**[02:17:51]** Everyone works together instead of against each other.
**[02:17:54]** And we've seen as some of the other AI companies have grown
**[02:17:57]** without naming any names,
**[02:17:59]** we're starting to see decoherence
**[02:18:01]** and people fighting each other.
**[02:18:02]** And I would argue there was even a lot of that
**[02:18:04]** from the beginning, but that it's gotten worse.
**[02:18:07]** But I think we've done an extraordinarily good job,
**[02:18:10]** even if not perfect, of holding the company together,
**[02:18:16]** making everyone feel the mission,
**[02:18:17]** that we're sincere about the mission,
**[02:18:19]** and that everyone has faith that everyone else there
**[02:18:22]** is working for the right reason, that we're a team,
**[02:18:25]** that people aren't trying to get ahead
**[02:18:26]** at each other's expense or backstab each other,
**[02:18:29]** which again, I think happens a lot
**[02:18:30]** at some of the other places.
**[02:18:32]** And how do you make that the case?
**[02:18:34]** I mean, it's a lot of things.
**[02:18:36]** It's me, it's Daniela, who runs the company day to day,
**[02:18:40]** it's the co-founders, it's the other people we hire,
**[02:18:42]** it's the environment we try to create.
**[02:18:44]** But I think an important thing in the culture is,
**[02:18:47]** I, and the other leaders as well, but especially me,
**[02:18:53]** have to articulate what the company is about,
**[02:18:56]** why it's doing what it's doing,
**[02:18:59]** what its strategy is, what its values are,
**[02:19:01]** what its mission is, and what it stands for.
**[02:19:04]** And when you get to 2,500 people,
**[02:19:07]** you can't do that person by person.
**[02:19:09]** You have to write, or you have to speak
**[02:19:11]** to the whole company.
**[02:19:12]** This is why I get up in front of the whole company
**[02:19:14]** every two weeks and speak for an hour.
**[02:19:17]** It's actually, I mean, I wouldn't say I write essays
**[02:19:20]** internally, I do two things.
**[02:19:21]** One, I write this thing called the DVQ,
**[02:19:23]** Dario Vision Quest.
**[02:19:25]** I wasn't the one who named it that,
**[02:19:27]** that's the name it received.
**[02:19:28]** And it's one of these names that I kind of,
**[02:19:30]** I tried to fight it because it made it sound like
**[02:19:32]** I was like going off and smoking peyote or something,
**[02:19:35]** but the name just stuck.
**[02:19:37]** So I get up in front of the company every two weeks,
**[02:19:40]** I have like a three or four page document,
**[02:19:43]** and I just kind of talk through like three or four
**[02:19:45]** different topics about what's going on internally,
**[02:19:48]** the models we're producing, the products,
**[02:19:51]** the outside industry, the world as a whole,
**[02:19:54]** as it relates to AI and geopolitically in general,
**[02:19:58]** just some mix of that.
**[02:19:59]** And I just go through very, very honestly,
**[02:20:01]** I just go through and I just say,
**[02:20:04]** this is what I'm thinking,
**[02:20:05]** this is what anthropic leadership is thinking.
**[02:20:07]** And then I answer questions.
**[02:20:08]** And that direct connection, I think has a lot of value
**[02:20:12]** that is hard to achieve when you're passing things
**[02:20:15]** down the chain, six levels deep.
**[02:20:19]** And a large fraction of the company comes to attend
**[02:20:23]** either in person or virtually.
**[02:20:27]** And it really means that you can communicate a lot.
**[02:20:30]** And then the other thing I do is I just,
**[02:20:32]** I have a channel in Slack where I just write a bunch
**[02:20:34]** of things and comment a lot.
**[02:20:36]** And often that's in response to just things I'm seeing
**[02:20:40]** at the company or questions people ask,
**[02:20:42]** or like we do internal surveys and there are things
**[02:20:46]** people are concerned about and so I'll write them up.
**[02:20:49]** And I'm like, I'm just, I'm very honest about these things.
**[02:20:53]** I just say them very directly.
**[02:20:56]** And the point is to get a reputation of telling the company
**[02:20:59]** the truth about what's happening,
**[02:21:01]** to call things what they are, to acknowledge problems,
**[02:21:04]** to avoid the sort of corpo speak,
**[02:21:07]** the kind of defensive communication that often is necessary
**[02:21:10]** in public because the world is very large and full of people
**[02:21:14]** who are interpreting things in bad faith.
**[02:21:19]** But if you have a company of people who you trust
**[02:21:21]** and we try to hire people that we trust,
**[02:21:24]** then you can really just be entirely unfiltered.
**[02:21:29]** And I think that's an enormous strength of the company.
**[02:21:33]** It makes it a better place to work.
**[02:21:35]** It makes people more of the sum of their parts
**[02:21:38]** and increases likelihood that we accomplish the mission
**[02:21:40]** because everyone is on the same page about the mission
**[02:21:42]** and everyone is debating and discussing how best
**[02:21:44]** to accomplish the mission.
**[02:21:46]** Well, in lieu of an external Daria vision quest,
**[02:21:48]** we have this interview.
**[02:21:50]** This interview is a little like that.
**[02:21:52]** This has been fun, Daria.
**[02:21:53]** Thanks for doing it.
**[02:21:54]** Yeah, thank you Dwarkesh.
**[02:21:55]** Hey everybody.
**[02:21:56]** I hope you enjoyed that episode.
**[02:21:58]** If you did, the most helpful thing you can do
**[02:22:00]** is just share it with other people
**[02:22:02]** who you think might enjoy it.
**[02:22:03]** It's also helpful if you leave a rating or a comment
**[02:22:06]** on whatever platform you're listening on.
**[02:22:09]** If you're interested in sponsoring the podcast,
**[02:22:11]** you can reach out at dwarkesh.com slash advertise.
**[02:22:16]** Otherwise, I'll see you on the next one.
