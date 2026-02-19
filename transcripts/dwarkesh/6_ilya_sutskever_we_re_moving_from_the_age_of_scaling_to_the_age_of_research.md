---
type: transcript
series: dwarkesh
episode: 6
title: Ilya Sutskever – We're moving from the age of scaling to the age of research
source_url: https://www.youtube.com/watch?v=aR20FWCCjAs
---

# Transcript: EP6 - Ilya Sutskever – We're moving from the age of scaling to the age of research

Source: https://www.youtube.com/watch?v=aR20FWCCjAs

---

**[00:00]** You know what's crazy?
**[00:01]** That all of this is real.
**[00:04]** Yeah, meaning what?
**[00:05]** Don't you think so?
**[00:06]** Meaning what?
**[00:06]** Like all this AI stuff and all this Bay Area,
**[00:09]** yeah, that it's happened.
**[00:11]** Isn't it straight out of science fiction?
**[00:13]** Yeah.
**[00:14]** Another thing that's crazy is how normal this takeoff feels.
**[00:19]** The idea that we'd be investing 1% of GDP in AI,
**[00:23]** I feel like it would have felt like a bigger deal.
**[00:25]** But right now, it just feels like.
**[00:27]** We get used to things pretty fast, turns out, yeah.
**[00:29]** But also, it's kind of like it's abstract,
**[00:31]** like what does it mean?
**[00:33]** What it means is that you see it in the news,
**[00:36]** that such and such company announced
**[00:37]** such and such dollar amount.
**[00:39]** Right.
**[00:40]** That's all you see.
**[00:41]** Right.
**[00:42]** It's not really felt in any other way so far.
**[00:45]** Yeah.
**[00:46]** Should we actually begin here?
**[00:47]** I think this is an interesting discussion.
**[00:47]** Sure.
**[00:48]** I think your point about, well,
**[00:50]** from the average person's point of view,
**[00:53]** nothing is that different will continue being true
**[00:55]** even into the singularity.
**[00:57]** No, I don't think so.
**[00:58]** Okay, interesting.
**[00:59]** So the thing which I was referring to,
**[01:02]** not feeling different,
**[01:05]** is, okay, so such and such company announced
**[01:08]** some difficult to comprehend dollar amount of investment.
**[01:12]** Right.
**[01:13]** I don't think anyone knows what to do with that.
**[01:15]** Yeah.
**[01:15]** But I think that the impact of AI is gonna be felt.
**[01:21]** AI is going to be diffused through the economy.
**[01:24]** There are very strong economic forces for this.
**[01:27]** And I think the impact is going to be felt very strongly.
**[01:30]** When do you expect that impact?
**[01:32]** I think the models seem smarter
**[01:35]** than their economic impact would imply.
**[01:38]** Yeah, this is one of the very confusing things
**[01:42]** about the models right now.
**[01:44]** How to reconcile the fact
**[01:49]** that they are doing so well on evals.
**[01:52]** And you look at the evals and you go,
**[01:54]** those are pretty hard evals.
**[01:57]** They're doing so well,
**[01:59]** but the economic impact seems to be dramatically behind.
**[02:04]** And it's almost like,
**[02:07]** it's very difficult to make sense of how can the model,
**[02:11]** on the one hand, do these amazing things,
**[02:13]** and then on the other hand,
**[02:15]** repeat itself twice in some situation in a kind of a,
**[02:20]** an example would be,
**[02:21]** let's say you use vibe coding to do something
**[02:24]** and you go to some place and then you get a bug.
**[02:27]** And then you tell the model, can you please fix the bug?
**[02:30]** And the model says, oh my God, you are so right,
**[02:32]** I have a bug, let me go fix that.
**[02:34]** And it introduces a second bug.
**[02:36]** And then you tell it, you have this new,
**[02:38]** this is the second bug.
**[02:39]** And it tells you, oh my God, how could I have done it?
**[02:41]** You are so right again.
**[02:43]** And brings back the first bug.
**[02:44]** And you can alternate between those.
**[02:46]** And it's like, how is that possible?
**[02:48]** It's like, I'm not sure.
**[02:51]** But it does suggest that something strange is going on.
**[02:56]** I have two possible explanations.
**[02:58]** So here, this is the more kind of a whimsical explanation
**[03:02]** is that maybe RL training makes the models
**[03:05]** a little bit too single-minded and narrowly focused,
**[03:08]** a little bit too, I don't know, unaware,
**[03:14]** even though it also makes them aware in some other ways.
**[03:17]** And because of this, they can't do basic things.
**[03:20]** But there is another explanation,
**[03:22]** which is back when people were doing pre-training,
**[03:27]** the question of what data to train on was answered.
**[03:32]** Because that answer was everything.
**[03:36]** When you do pre-training, you need all the data.
**[03:41]** So you don't have to think,
**[03:42]** is it gonna be this data or that data?
**[03:44]** But when people do RL training, they do need to think.
**[03:48]** They say, okay, we want to have this kind of RL training
**[03:51]** for this thing and that kind of RL training for that thing.
**[03:54]** And from what I hear, all the companies have teams
**[03:58]** that just produce new RL environments
**[04:00]** and just add it to the training mix.
**[04:02]** And then the question is, well, what are those?
**[04:03]** There are so many degrees of freedom.
**[04:06]** There is such a huge variety
**[04:07]** of RL environments you could produce.
**[04:10]** And one thing you could do,
**[04:13]** and I think that's something that is done inadvertently,
**[04:17]** is that people take inspiration from the evals.
**[04:22]** You say, hey, I would love our model to do really well
**[04:25]** when we release it, I want the evals to look great.
**[04:28]** What would be RL training that would help on this task?
**[04:33]** I think that is something that happens,
**[04:35]** and I think it could explain a lot of what's going on.
**[04:39]** If you combine this with generalization of the models
**[04:42]** actually being inadequate,
**[04:44]** that has the potential to explain a lot
**[04:46]** of what we are seeing, this disconnect
**[04:48]** between eval performance and actual real-world performance,
**[04:53]** which is something that we don't today
**[04:56]** exactly even understand what we mean by that.
**[05:00]** I like this idea that the real reward hacking
**[05:03]** is the human researchers who are too focused on the evals.
**[05:09]** I think there's two ways to understand
**[05:11]** or to try to think about what you have just pointed out.
**[05:15]** One is, look, if it's the case that simply
**[05:19]** by becoming superhuman at a coding competition,
**[05:21]** a model will not automatically become more tasteful
**[05:26]** and exercise better judgment
**[05:27]** about how to improve your code base.
**[05:29]** Well, then you should expand the suite of environments
**[05:32]** such that you're not just testing it
**[05:34]** on having the best performance in a coding competition,
**[05:36]** it should also be able to make the best kind of application
**[05:39]** for X thing or Y thing or Z thing.
**[05:42]** And another, maybe this is what you're hinting at,
**[05:44]** is to say, why should it be the case in the first place
**[05:47]** that becoming superhuman at coding competitions
**[05:51]** doesn't make you a more tasteful programmer more generally?
**[05:54]** Maybe the thing to do is not to keep stacking up
**[05:57]** the amount of environments and the diversity of environments
**[05:59]** to figure out an approach which lets you learn
**[06:02]** from one environment and improve your performance
**[06:06]** on something else.
**[06:07]** So I have a human analogy which might be helpful.
**[06:12]** So even the case, let's take the case
**[06:14]** of competitive programming, since you mentioned that.
**[06:17]** And suppose you have two students.
**[06:19]** One of them, work decided they want to be
**[06:22]** the best competitive programmer,
**[06:24]** so they will practice 10,000 hours for that domain.
**[06:29]** They will solve all the problems,
**[06:30]** memorize all the proof techniques,
**[06:31]** and be very, very skilled at quickly and correctly
**[06:38]** implementing all the algorithms.
**[06:40]** And by doing so, they became the best, one of the best.
**[06:44]** Student number two thought,
**[06:46]** oh, competitive programming is cool.
**[06:47]** Maybe they practiced for 100 hours, much, much less,
**[06:51]** and they also did really well.
**[06:52]** Which one do you think is going to do better
**[06:54]** in their career later on?
**[06:56]** The second.
**[06:57]** Right?
**[06:57]** And I think that's basically what's going on.
**[06:59]** The models are much more like the first student,
**[07:01]** but even more, because then we say,
**[07:02]** okay, so the model should be good competitive programming,
**[07:05]** so let's get every single competitive programming problem
**[07:08]** ever, and then let's do some data augmentation,
**[07:11]** so we have even more competitive programming problems,
**[07:14]** and we train on that.
**[07:16]** And so now you've got this great competitive programmer.
**[07:18]** And with this analogy, I think it's more intuitive.
**[07:21]** I think it's more intuitive with this analogy
**[07:22]** that yeah, okay, so if it's so well trained,
**[07:25]** okay, it's like all the different algorithms
**[07:28]** and all the different proof techniques
**[07:29]** are like right at its fingertips.
**[07:32]** And it's more intuitive that with this level of preparation,
**[07:36]** it will not necessarily generalize to other things.
**[07:39]** But then what is the analogy for what the second student
**[07:42]** is doing before they do the 100 hours of fine tuning?
**[07:48]** I think it's like they have it.
**[07:52]** I think it's the it factor.
**[07:53]** Yeah.
**[07:54]** Right?
**[07:55]** And I know, when I was an undergrad,
**[07:56]** I remember there was a student like this
**[07:58]** that studied with me.
**[07:59]** So I know it exists.
**[08:01]** Yeah.
**[08:02]** I think it's interesting to distinguish it
**[08:03]** from whatever pre-training does.
**[08:05]** So one way to understand what you just said
**[08:08]** about we don't have to choose the data in pre-training
**[08:10]** is to say, actually, it's not dissimilar
**[08:13]** to the 10,000 hours of practice.
**[08:15]** It's just that you get that 10,000 hours of practice
**[08:17]** for free, because it's already somewhere
**[08:20]** in the pre-training distribution.
**[08:22]** But it's like, maybe you're suggesting actually,
**[08:24]** there's actually not that much generalization
**[08:26]** in pre-training.
**[08:26]** There's just so much data in pre-training.
**[08:28]** But it's like, it's not necessarily
**[08:29]** generalizing better than RL.
**[08:31]** The main strength of pre-training
**[08:33]** is that there is, A, so much of it.
**[08:35]** Yeah.
**[08:36]** And B, you don't have to think hard
**[08:39]** about what data to put into pre-training.
**[08:42]** And it's a very kind of natural data,
**[08:45]** and it does include in it a lot of what people do,
**[08:50]** people's thoughts, and a lot of the features.
**[08:54]** It's like the whole world is projected by people onto text.
**[08:59]** Yeah.
**[09:00]** And pre-training tries to capture that
**[09:01]** using a huge amount of data.
**[09:04]** It's very, pre-training is very difficult to reason about,
**[09:08]** because it's so hard to understand the manner
**[09:13]** in which the model relies on pre-training data.
**[09:17]** And whenever the model makes a mistake,
**[09:19]** could it be because something by chance
**[09:22]** is not as supported by the pre-training data?
**[09:25]** You know, and support by pre-training is maybe a loose term.
**[09:29]** I don't know if I can add anything more useful on this,
**[09:33]** but I don't think there is a human analog to pre-training.
**[09:39]** Here's analogies that people have proposed
**[09:41]** for what the human analogy to pre-training is,
**[09:43]** and I'm curious to get your thoughts
**[09:44]** on why they're potentially wrong.
**[09:47]** One is to think about the first 18, or 15,
**[09:51]** or 13 years of a person's life
**[09:53]** when they aren't necessarily economically productive,
**[09:56]** but they are doing something
**[09:58]** that is making them understand the world better,
**[10:02]** and so forth.
**[10:03]** And the other is to think about evolution
**[10:06]** as doing some kind of search for three billion years,
**[10:09]** which then results in a human lifetime instance.
**[10:14]** And then I'm curious if you think
**[10:15]** either of these are actually analogous to pre-training,
**[10:17]** or how would you think about at least
**[10:19]** what lifetime human learning is like, if not pre-training?
**[10:22]** I think there are some similarities
**[10:25]** between both of these to pre-training,
**[10:27]** and pre-training tries to play the role of both of these.
**[10:31]** But I think there are some big differences as well.
**[10:34]** The amount of pre-training data is very, very staggering.
**[10:39]** Yes.
**[10:41]** And somehow, a human being, after even 15 years,
**[10:45]** with a tiny fraction of that pre-training data,
**[10:48]** they know much less.
**[10:49]** But whatever they do know,
**[10:50]** they know much more deeply, somehow.
**[10:53]** And the mistakes, like already at that age,
**[10:56]** you would not make mistakes that our AIs make.
**[10:59]** Yeah.
**[11:00]** There is another thing.
**[11:00]** You might say, could it be something like evolution?
**[11:03]** And the answer is maybe, but in this case,
**[11:05]** I think evolution might actually have an edge.
**[11:07]** Like there is this, I remember reading about this case
**[11:12]** where some, you know, that one thing that neuroscientists do,
**[11:17]** or rather one way in which neuroscientists
**[11:19]** can learn about the brain,
**[11:21]** is by studying people with brain damage
**[11:23]** to different parts of the brain.
**[11:25]** And some people have the most strange symptoms
**[11:28]** you could imagine.
**[11:29]** It's actually really, really interesting.
**[11:32]** And there was one case that comes to mind that's relevant.
**[11:35]** I read about this person who had some kind of brain damage
**[11:40]** that took out, I think a stroke or an accident,
**[11:44]** that took out his emotional processing.
**[11:48]** So he stopped feeling any emotion.
**[11:51]** And as a result of that, you know,
**[11:54]** he still remained very articulate
**[11:56]** and he could solve little puzzles
**[11:58]** and on tests he seemed to be just fine,
**[12:01]** but he felt no emotion.
**[12:02]** He didn't feel sad.
**[12:03]** He didn't feel anger.
**[12:04]** He didn't feel animated.
**[12:06]** And he became somehow extremely bad
**[12:09]** at making any decisions at all.
**[12:11]** It would take him hours to decide on which socks to wear
**[12:15]** and he would make very bad financial decisions.
**[12:19]** And that's very,
**[12:22]** what does it say about the role of our built-in emotions
**[12:30]** in making us like a viable agent essentially?
**[12:33]** And I guess to connect to your question about pre-training,
**[12:36]** it's like, maybe if you're good enough
**[12:40]** at like getting everything out of pre-training,
**[12:42]** you could get that as well.
**[12:44]** But that's the kind of thing which seems
**[12:49]** well, it may or may not be possible
**[12:52]** to get that from pre-training.
**[12:56]** What is that?
**[12:58]** Clearly not just directly emotion.
**[13:00]** It seems like some almost value function like thing,
**[13:05]** which is giving, telling you which decision to be,
**[13:08]** like what the end reward for any decision should be.
**[13:11]** And you think that doesn't sort of implicitly come from?
**[13:15]** I think it could.
**[13:16]** I'm just saying it's not 100% obvious.
**[13:19]** Yeah.
**[13:20]** But what is that?
**[13:22]** Like, how do you think about emotions?
**[13:23]** What is the ML analogy for emotions?
**[13:26]** It should be some kind of a value function thing.
**[13:28]** Yeah.
**[13:29]** But I don't think there is a great ML analogy
**[13:31]** because right now value functions
**[13:32]** don't play a very prominent role in the things people do.
**[13:36]** It might be worth defining for the audience
**[13:37]** what a value function is if you wanna do that.
**[13:39]** I mean, certainly, I'll be very happy to do that, right?
**[13:44]** So when people do reinforcement learning,
**[13:51]** the way reinforcement learning is done right now,
**[13:53]** how do people train those agents?
**[13:56]** So you have a neural net and you give it a problem
**[13:59]** and then you tell the model, go solve it.
**[14:01]** And the model takes maybe thousands,
**[14:03]** hundreds of thousands of actions or thoughts or something,
**[14:07]** and then it produces a solution, the solution is created.
**[14:10]** And then the score is used to provide a training signal
**[14:14]** for every single action in your trajectory.
**[14:20]** So that means that if you are doing something
**[14:23]** that goes for a long time,
**[14:24]** if you're training a task that takes a long time to solve,
**[14:28]** you will do no learning at all until you solve,
**[14:31]** until you come up with a proposed solution.
**[14:33]** That's how reinforcement learning is done naively.
**[14:35]** That's how O1, R1 ostensibly are done.
**[14:40]** The value function says something like,
**[14:43]** okay, look, maybe I could sometimes, not always,
**[14:47]** could tell you if you are doing well or badly.
**[14:50]** The notion of a value function is more useful
**[14:52]** in some domains than others.
**[14:53]** So for example, when you play chess and you lose a piece,
**[14:57]** you know, I messed up.
**[14:59]** You don't need to play the whole game
**[15:01]** to know that what I just did was bad
**[15:03]** and therefore whatever preceded it, it was also bad.
**[15:08]** So the value function lets you short-circuit
**[15:12]** the weight until the very end.
**[15:14]** Like let's suppose that you started to pursue some kind of,
**[15:18]** okay, let's suppose that you are doing
**[15:20]** some kind of a math thing or a programming thing
**[15:23]** and you're trying to explore a particular solution direction
**[15:26]** and after, let's say after a thousand steps of thinking,
**[15:30]** you concluded that this direction is unpromising.
**[15:34]** As soon as you conclude this,
**[15:36]** you could already get a reward signal
**[15:39]** a thousand time steps previously
**[15:41]** when you decided to pursue down this path.
**[15:43]** You say, oh, next time I shouldn't pursue this path
**[15:46]** in a similar situation,
**[15:48]** long before you actually came up with a proposed solution.
**[15:52]** This was in the DeepSeeker One paper
**[15:53]** is that the space of trajectories is so wide
**[16:00]** that maybe it's hard to learn a mapping
**[16:02]** from an intermediate trajectory and value.
**[16:06]** And also given that in coding, for example,
**[16:08]** you will have the wrong idea, then you'll go back,
**[16:11]** then you'll change something.
**[16:12]** This sounds like such lack of faith in deep learning.
**[16:15]** Like, I mean, sure, it might be difficult,
**[16:18]** but nothing deep learning can do.
**[16:21]** Yeah.
**[16:22]** So my expectation is that like value function
**[16:28]** should be useful and I fully expect
**[16:32]** that they will be used in the future, if not already.
**[16:34]** What was I alluding to with the person
**[16:36]** whose emotional center got damaged
**[16:41]** is more that maybe what it suggests
**[16:46]** is that the value function of humans
**[16:49]** is modulated by emotions in some important way
**[16:52]** that's hard-coded by evolution.
**[16:55]** And maybe that is important for people
**[16:57]** to be effective in the world.
**[17:00]** That's the thing I was actually gonna,
**[17:02]** there's something really interesting
**[17:03]** about emotions of the value function,
**[17:04]** which is that it's impressive that they have
**[17:08]** this much utility while still being
**[17:10]** rather simple to understand.
**[17:16]** So I have two responses.
**[17:17]** I do agree that compared to the kind of things
**[17:24]** that we learn and the things that we are talking about,
**[17:26]** the kind of ways we are talking about emotions
**[17:28]** are relatively simple.
**[17:30]** They might even be so simple that maybe
**[17:33]** you could map them out in a human understandable way.
**[17:35]** I think it would be cool to do.
**[17:39]** In terms of utility though, I think there is a thing
**[17:41]** where there is this complexity robustness trade-off
**[17:48]** where complex things can be very useful,
**[17:52]** but simple things are very useful
**[17:56]** in a very broad range of situations.
**[17:59]** And so I think one way to interpret what we are seeing
**[18:02]** is that we've got these emotions
**[18:04]** that essentially evolved mostly from our mammal ancestors
**[18:09]** and then fine-tuned a little bit
**[18:10]** while we were hominids, just a bit.
**[18:13]** We do have like a decent amount of social emotions though,
**[18:16]** which mammals may lack, but they're not very sophisticated.
**[18:21]** And because they're not sophisticated,
**[18:23]** they serve us so well in this very different world
**[18:25]** compared to the one that we've been living in.
**[18:28]** Actually, they also make mistakes.
**[18:29]** For example, our emotions, well, I don't know,
**[18:32]** does hunger count as an emotion?
**[18:35]** It's debatable, but I think for example,
**[18:38]** our intuitive feeling of hunger
**[18:42]** is not succeeding in guiding us correctly
**[18:46]** in this world with an abundance of food.
**[18:49]** Yeah.
**[18:50]** People have been talking about scaling data,
**[18:53]** scaling parameters, scaling compute.
**[18:56]** Is there a more general way to think about scaling?
**[18:58]** What are the other scaling axes?
**[19:00]** So the thing, so here is a perspective.
**[19:06]** Here's a perspective that I think might be true.
**[19:10]** So the way ML used to work
**[19:14]** is that people would just tinker with stuff
**[19:16]** and try to get interesting results.
**[19:22]** That's what's been going on in the past.
**[19:25]** Then the scaling insight arrived, right?
**[19:31]** Scaling laws, GPT-3.
**[19:34]** And suddenly everyone realized we should scale.
**[19:39]** And it's just, this is an example
**[19:41]** of how language affects thought.
**[19:45]** Scaling is just one word, but it's such a powerful word
**[19:49]** because it informs people what to do.
**[19:51]** They say, okay, let's try to scale things.
**[19:54]** And so you say, okay, so what are we scaling?
**[19:56]** And pre-training was a thing to scale.
**[19:58]** It was a particular scaling recipe.
**[20:02]** The big breakthrough of pre-training
**[20:04]** is the realization that this recipe is good.
**[20:07]** So you say, hey, if you mix some compute
**[20:12]** with some data into a neural net of a certain size,
**[20:15]** you will get results.
**[20:17]** And you will know that it will be better
**[20:19]** if you just scale the recipe up.
**[20:21]** And this is also great, companies love this
**[20:24]** because it gives you a very low risk way
**[20:29]** of investing your resources, right?
**[20:32]** It's much harder to invest your resources in research.
**[20:36]** Compare that, if you research,
**[20:38]** you need to have like go forth researchers and research
**[20:40]** and come up with something versus get more data,
**[20:44]** get more compute, you know you'll get something
**[20:46]** from pre-training.
**[20:48]** And indeed, you know, it looks like I,
**[20:51]** based on various things some people say on Twitter,
**[20:56]** maybe it appears the Gemini have found a way
**[20:59]** to get more out of pre-training.
**[21:01]** At some point though, pre-training will run out of data.
**[21:03]** The data is very clearly finite.
**[21:05]** And so then, okay, what do you do next?
**[21:07]** Either you do some kind of a souped up pre-training,
**[21:10]** different recipe from the one we've done before,
**[21:13]** or you're doing RL, or maybe something else.
**[21:15]** But now that compute is big,
**[21:18]** compute is now very big,
**[21:19]** in some sense, we are back to the age of research.
**[21:22]** So maybe here's another way to put it.
**[21:24]** Up until 2020, from 2012 to 2020,
**[21:29]** it was the age of research.
**[21:31]** Now from 2020 to 2025, it was the age of scaling
**[21:34]** or maybe plus minus, let's add arrow bars to those years
**[21:37]** because people say, this is amazing,
**[21:39]** you gotta scale more, keep scaling,
**[21:41]** the one word, scaling.
**[21:43]** But now the scale is so big,
**[21:45]** is the belief really that, oh, it's so big,
**[21:49]** but if you had 100x more, everything would be so different?
**[21:53]** Like it would be different for sure.
**[21:55]** But is the belief that if you just 100x the scale,
**[21:59]** everything would be transformed?
**[22:02]** I don't think that's true.
**[22:03]** So it's back to the age of research again,
**[22:05]** just with big computers.
**[22:06]** That's a very interesting way to put it.
**[22:10]** But let me ask you the question you just posed then,
**[22:12]** what are we scaling?
**[22:13]** And what would it mean to have a recipe?
**[22:16]** Because I guess I'm not aware of a very clean relationship
**[22:22]** that almost looks like a law of physics,
**[22:24]** which existed in pre-training.
**[22:25]** It was a power law between data
**[22:27]** or computer parameters and loss.
**[22:30]** What is the kind of relationship we should be seeking
**[22:34]** and how should we think about
**[22:35]** what this new recipe might look like?
**[22:38]** So we've already witnessed a transition
**[22:43]** from one type of scaling to a different type of scaling,
**[22:47]** from pre-training to RL.
**[22:51]** Now people are scaling RL.
**[22:53]** Now based on what people say on Twitter,
**[22:56]** they spend more compute on RL
**[22:58]** than on pre-training at this point,
**[23:00]** because RL can actually consume quite a bit of compute.
**[23:03]** You do very, very long rollouts.
**[23:07]** So it takes a lot of compute to produce those rollouts.
**[23:09]** And then you get relatively small amount
**[23:11]** of learning per rollout.
**[23:12]** So you really can spend a lot of compute.
**[23:15]** And I could imagine, like I wouldn't at this state,
**[23:20]** it's more like, I wouldn't even call it a scaling.
**[23:24]** I would say, hey, like, what are you doing?
**[23:27]** And is the thing you are doing
**[23:28]** the most productive thing you could be doing?
**[23:31]** Can you find a more productive way of using your compute?
**[23:36]** We've discussed the value function business earlier.
**[23:39]** And maybe once people get good at value functions,
**[23:42]** they will be using their resources more productively.
**[23:47]** And if you find a whole other way of training models,
**[23:52]** you could say, is this scaling
**[23:54]** or is it just using your resources?
**[23:56]** I think it becomes a little bit ambiguous.
**[23:58]** In a sense that when people were in the age of research,
**[24:00]** back then it was like, people say,
**[24:02]** hey, let's try this and this and this.
**[24:03]** Let's try that and that and that.
**[24:04]** Oh, look, something interesting is happening.
**[24:07]** And I think there will be a return to that.
**[24:10]** So if we're back in the era of research,
**[24:12]** stepping back, what is the part of the recipe
**[24:14]** that we need to think most about?
**[24:17]** When you say value function,
**[24:18]** people are already trying the current recipe,
**[24:21]** but then having LLM as a judge and so forth.
**[24:23]** You can say that's a value function,
**[24:24]** but it sounds like you have something
**[24:25]** much more fundamental in mind.
**[24:26]** Do we need to go back to,
**[24:29]** should we even rethink pre-training at all
**[24:32]** and not just add more steps to the end of that process?
**[24:35]** Yeah, so the discussion about value function,
**[24:40]** I think it was interesting.
**[24:41]** I want to emphasize that I think the value function
**[24:44]** is something like, it's going to make our realm
**[24:47]** more efficient, and I think that makes a difference.
**[24:52]** But I think that anything you can do with a value function,
**[24:55]** you can do without, just more slowly.
**[25:00]** The thing which I think is the most fundamental
**[25:02]** is that these models somehow just generalize
**[25:05]** dramatically worse than people, and it's super obvious.
**[25:10]** That seems like a very fundamental thing.
**[25:12]** Okay, so this is the crux, generalization,
**[25:15]** and there's two sub-questions.
**[25:20]** There's one which is about sample efficiency,
**[25:22]** which is why should it take so much more data
**[25:24]** for these models to learn than humans?
**[25:25]** There's a second about,
**[25:27]** even separate from the amount of data it takes,
**[25:30]** there's a question of why is it so hard
**[25:32]** to teach the thing we want to a model than to a human,
**[25:35]** which is to say, to a human,
**[25:38]** we don't necessarily need a verifiable reward
**[25:40]** to be able to, you're probably mentoring
**[25:44]** a bunch of researchers right now,
**[25:45]** and you're talking with them,
**[25:47]** you're showing them your code,
**[25:48]** and you're showing them how you think,
**[25:50]** and from that, they're picking up your way of thinking
**[25:52]** and how they should do research.
**[25:54]** You don't have to set a verifiable reward for them
**[25:57]** that's like, okay, this is the next part of the curriculum,
**[25:58]** and now this is the next part of the curriculum,
**[26:00]** and oh, this training was unstable,
**[26:02]** and there's not the schleppy bespoke process.
**[26:06]** So perhaps these two issues are actually related
**[26:08]** in some way, but I'd be curious to explore
**[26:12]** this second thing, which was more like continual learning,
**[26:14]** and this first thing, which feels just like sample efficiency.
**[26:19]** Yeah, so you know, you could actually wonder,
**[26:21]** one possible explanation for the human sample efficiency
**[26:27]** that needs to be considered is evolution,
**[26:30]** and evolution has given us a small amount
**[26:34]** of the most useful information possible,
**[26:38]** and for things like vision, hearing, and locomotion,
**[26:44]** I think there's a pretty strong case
**[26:45]** that evolution actually has given us a lot.
**[26:49]** So for example, human dexterity far exceeds,
**[26:53]** I mean, robots can become dexterous too
**[26:56]** if you subject them to a huge amount
**[26:58]** of training and simulation, but to train a robot
**[27:01]** in the real world to quickly pick up a new skill
**[27:04]** like a person does seems very out of reach,
**[27:07]** and here you could say, oh yeah, like locomotion,
**[27:10]** all our ancestors needed great locomotion, squirrels,
**[27:15]** so locomotion may be like,
**[27:17]** you've got some unbelievable prior.
**[27:19]** You could make the same case for vision.
**[27:21]** I believe Jan Lekan made the point,
**[27:24]** oh, like children learn to drive after 10 hours of practice,
**[27:29]** which is true, but our vision is so good.
**[27:33]** At least for me, when I remember myself being five-year-old,
**[27:37]** I was very excited about cars back then,
**[27:40]** and I'm pretty sure my car recognition
**[27:43]** was more than adequate for self-driving already
**[27:45]** as a five-year-old.
**[27:47]** You don't get to see that much data as a five-year-old.
**[27:49]** You spend most of your time in your parents' house,
**[27:51]** so you have very low data diversity,
**[27:53]** but you could say maybe that's evolution too,
**[27:55]** but in language and math and coding, probably not.
**[28:00]** It still seems better than models.
**[28:02]** I mean, obviously models are better than the average human
**[28:05]** at language and math and coding,
**[28:06]** but are they better at the average human at learning?
**[28:09]** Oh yeah, oh yeah, absolutely.
**[28:11]** What I meant to say is that language, math, and coding,
**[28:15]** and especially math and coding,
**[28:16]** suggests that whatever it is that makes people
**[28:21]** good at learning is probably not so much
**[28:24]** a complicated prior, but something more,
**[28:27]** some fundamental thing.
**[28:29]** Wait, I'm not sure I understood.
**[28:30]** Why should that be the case?
**[28:32]** So consider a skill that people exhibit
**[28:35]** some kind of great reliability or, you know.
**[28:39]** Yeah.
**[28:41]** If the skill is one that was very useful
**[28:44]** to our ancestors for many millions of years,
**[28:47]** hundreds of millions of years,
**[28:48]** you could say, you could argue that maybe
**[28:52]** humans are good at it because of evolution,
**[28:56]** because we have a prior, an evolutionary prior
**[29:00]** that's encoded in some very non-obvious way
**[29:04]** that somehow makes us so good at it.
**[29:07]** But if people exhibit great ability,
**[29:11]** reliability, robustness, ability to learn
**[29:14]** in a domain that really did not exist until recently,
**[29:19]** then this is more an indication
**[29:23]** that people might have just better machine learning, period.
**[29:29]** But then how should we think about what that is?
**[29:31]** Is it a matter of, yeah, what is the ML analogy for?
**[29:38]** There's a couple of interesting things about it.
**[29:39]** It takes fewer samples.
**[29:41]** It's more unsupervised.
**[29:42]** You don't have to set a,
**[29:43]** like a child learning to drive a car.
**[29:45]** Children are not learning to drive a car.
**[29:47]** A teenager learning how to drive a car
**[29:49]** is like not exactly getting
**[29:53]** some pre-built verifiable reward there.
**[29:56]** It comes from their interaction with the machine and the.
**[30:00]** with the environment, and yet it takes much of your samples,
**[30:03]** it seems more unsupervised, it seems more robust.
**[30:07]** Much more robust.
**[30:08]** The robustness of people is really staggering.
**[30:12]** Yeah, so is it like, okay,
**[30:13]** and do you have a unified way of thinking about
**[30:15]** why are all these things happening at once?
**[30:18]** What is the ML analogy that would,
**[30:20]** that could realize something like this?
**[30:24]** So this is where, you know,
**[30:26]** one of the things that you've been asking about
**[30:28]** is how can the teenage driver kind of self-correct
**[30:33]** and learn from their experience without an external teacher?
**[30:37]** And the answer is, well, they have their value function.
**[30:41]** Right, they have a general sense,
**[30:43]** which is also, by the way, extremely robust in people.
**[30:46]** Like, whatever it is, the human value function,
**[30:50]** whatever the human value function is,
**[30:52]** with a few exceptions around addiction,
**[30:56]** it's actually very, very robust.
**[30:59]** And so for something like a teenager
**[31:00]** that's learning to drive,
**[31:02]** they start to drive and they already have a sense
**[31:05]** of how they're driving immediately,
**[31:08]** how badly they're unconfident.
**[31:10]** And then they see, okay,
**[31:12]** and then of course the learning speed of any teenager
**[31:15]** is so fast after 10 hours, you're good to go.
**[31:17]** Yeah, it seems like humans have some solution,
**[31:19]** but I'm curious about like, well, how are they doing it?
**[31:21]** And like, why is it so hard to,
**[31:23]** like, how do we need to reconceptualize
**[31:24]** the way we're training models
**[31:26]** to make something like this possible?
**[31:27]** You know, that is a great question to ask.
**[31:31]** And it's a question I have a lot of opinions about,
**[31:37]** but unfortunately we live in a world
**[31:40]** where not all machine learning ideas are discussed freely
**[31:43]** and this is one of them.
**[31:44]** So there's probably a way to do it.
**[31:49]** I think it can be done.
**[31:50]** The fact that people are like that,
**[31:54]** I think it's a proof that it can be done.
**[31:56]** There may be another blocker though,
**[31:57]** which is there is a possibility
**[32:02]** that the human neurons actually do more compute
**[32:05]** than we think.
**[32:07]** And if that is true,
**[32:09]** and if that plays an important role,
**[32:10]** then things might be more difficult.
**[32:13]** But regardless, I do think it points to the existence
**[32:16]** of some machine learning principle
**[32:21]** that I have opinions on,
**[32:23]** but unfortunately circumstances make it hard
**[32:27]** to discuss in detail.
**[32:28]** Nobody listens to this podcast, Ilya.
**[32:30]** Yeah.
**[32:32]** So I have to say that prepping for Ilya was pretty tough
**[32:35]** because neither I nor anybody else
**[32:37]** had any idea what he's working on
**[32:39]** and what SSI is trying to do.
**[32:41]** I had no basis to come up with my questions.
**[32:44]** And the only thing I could go off, honestly,
**[32:46]** was trying to think from first principles
**[32:48]** about what are the bottlenecks to HEI?
**[32:51]** Because clearly Ilya is working on them in some way.
**[32:54]** Part of this question involved thinking about RL scaling
**[32:56]** because everybody's asking how well RL will generalize
**[32:59]** and how we can make it generalize better.
**[33:01]** As part of this, I was reading this paper
**[33:03]** that came out recently on RL scaling,
**[33:05]** and it showed that actually the learning curve on RL
**[33:08]** looks like a sigmoid.
**[33:09]** I found this very curious.
**[33:10]** Why should it be a sigmoid?
**[33:11]** Where it learns very little for a long time,
**[33:14]** and then it quickly learns a lot,
**[33:16]** and then it asymptotes.
**[33:17]** This is very different from the power law
**[33:19]** you see in pre-training where the model learns a bunch
**[33:22]** at the very beginning and then less and less over time.
**[33:24]** And it actually reminded me of a note
**[33:26]** that I had written down after I had a conversation
**[33:28]** with a researcher friend where he pointed out
**[33:30]** that the number of samples that you need to take
**[33:33]** in order to find a correct answer scales exponentially
**[33:36]** with how different your current probability distribution
**[33:39]** is from the target probability distribution.
**[33:41]** And I was thinking about how these two ideas are related.
**[33:43]** I had this vague idea that they should be connected,
**[33:45]** but I really didn't know how.
**[33:47]** I don't have a math background,
**[33:48]** so I couldn't really formalize it.
**[33:50]** But I wondered if Gemini 3 could help me out here.
**[33:52]** And so I took a picture of my notebook,
**[33:54]** and I took the paper,
**[33:55]** and I put them both in the context of Gemini 3,
**[33:58]** and I asked it to find the connection.
**[34:00]** And it thought a bunch,
**[34:01]** and then it realized that the correct way
**[34:04]** to model the information you gain
**[34:06]** from a single yes or no outcome in RL
**[34:08]** is as the entropy of a random binary variable.
**[34:12]** It made a graph which showed how the bits you gain
**[34:15]** for a sample in RL versus supervised learning
**[34:18]** scale as the pass rate increases.
**[34:20]** And as soon as I saw the graph that Gemini 3 made,
**[34:22]** immediately a ton of things started making sense to me.
**[34:25]** Then I wanted to see if there was any empirical basis
**[34:28]** to this theory.
**[34:29]** So I asked Gemini to code an experiment
**[34:31]** to show whether the improvement in loss
**[34:34]** scales in this way with pass rate.
**[34:37]** I just took the code that Gemini outputted,
**[34:38]** I copy pasted it into a Google Colab notebook,
**[34:41]** and I was able to run this toy ML experiment
**[34:44]** and visualize its results without a single bug.
**[34:46]** It's interesting because the results look similar,
**[34:49]** but not identical to what we should have expected.
**[34:51]** And so I downloaded this chart and I put it into Gemini
**[34:53]** and asked it, what is going on here?
**[34:55]** And it came up with a hypothesis
**[34:56]** that I think is actually correct,
**[34:57]** which is that we're capping how much supervised learning
**[35:00]** can improve in the beginning by having a fixed learning rate
**[35:04]** and in fact, we should decrease the learning rate over time.
**[35:06]** It actually gives us an intuitive understanding
**[35:08]** for why in practice we have learning rate schedulers
**[35:12]** that decrease the learning rate over time.
**[35:14]** I did this entire flow from coming up
**[35:16]** with this vague initial question
**[35:18]** to building a theoretical understanding
**[35:20]** to running some toy ML experiments, all with Gemini 3.
**[35:24]** This feels like the first model
**[35:25]** where it can actually come up with new connections
**[35:28]** that I wouldn't have anticipated.
**[35:30]** It's actually now become the default place I go to
**[35:32]** when I want to brainstorm new ways to think about a problem.
**[35:35]** If you want to read more about RL scaling,
**[35:37]** you can check out the blog post that I wrote
**[35:38]** with a little help from Gemini 3.
**[35:40]** And if you want to check out Gemini 3 yourself,
**[35:42]** go to gemini.google.
**[35:45]** I am curious, if you say we are back in the era of research,
**[35:49]** you were there from 2012 to 2020,
**[35:53]** and what is now the vibe gonna be
**[35:58]** if we go back to the era of research?
**[36:00]** For example, even after AlexNet,
**[36:03]** the amount of compute that was used to run experiments
**[36:07]** kept increasing,
**[36:08]** and the size of frontier systems kept increasing.
**[36:12]** And do you think now that this era of research
**[36:15]** will still require tremendous amounts of compute?
**[36:19]** Do you think it will require going back into the archives
**[36:22]** and reading old papers?
**[36:24]** What is, maybe what was the vibe of like,
**[36:27]** you were at Google and OpenAI and Stanford,
**[36:31]** these places when there was like a,
**[36:33]** more of a vibe of research.
**[36:34]** What kind of things should we be expecting in the community?
**[36:38]** So, one consequence of the age of scaling
**[36:44]** is that there was this,
**[36:47]** scaling sucked out all the air in the room.
**[36:49]** Yeah.
**[36:51]** And so, because scaling sucked out all the air in the room,
**[36:57]** everyone started to do the same thing.
**[36:59]** We got to the point where we are in a world
**[37:04]** where there are more companies than ideas by quite a bit.
**[37:09]** Actually, on that,
**[37:10]** there is this Silicon Valley saying that says
**[37:14]** that ideas are cheap, execution is everything.
**[37:19]** And people say that a lot.
**[37:20]** And there is truth to that.
**[37:22]** But then I saw someone say on Twitter, something like,
**[37:27]** if ideas are so cheap, how come no one's having any ideas?
**[37:31]** And I think it's true too.
**[37:32]** I think, like, if you think about research progress
**[37:37]** and bottlenecks, there are several bottlenecks.
**[37:42]** If you go back to the, and one of them is ideas,
**[37:45]** and one of them is your ability to bring them to life,
**[37:48]** which might be compute, but also engineering.
**[37:52]** So, if you go back to the nineties, let's say,
**[37:54]** you had people who had pretty good ideas.
**[37:57]** And if they had much larger computers,
**[37:58]** maybe they could demonstrate that their ideas were viable,
**[38:01]** but they could not.
**[38:03]** So, they could only have very, very small demonstration
**[38:05]** that did not convince anyone.
**[38:08]** So, the bottleneck was compute.
**[38:09]** Then in the age of scaling, computers increased a lot.
**[38:14]** And of course, there is a question
**[38:16]** of how much compute is needed, but compute is large.
**[38:20]** So, compute is large enough such that it's like not obvious
**[38:27]** that you need that much more compute to prove some idea.
**[38:32]** Like, I'll give you an analogy.
**[38:34]** AlexNet was built on two GPUs.
**[38:38]** That was the total amount of compute used for it.
**[38:40]** The Transformer was built on eight to 64 GPUs.
**[38:45]** No single Transformer paper experiment
**[38:48]** used more than 64 GPUs of 2017,
**[38:51]** which would be like, what, two GPUs of today?
**[38:54]** So, the ResNet, right?
**[38:58]** Many, like even the, you could argue that the,
**[39:02]** like, O1 reasoning was not the most compute-heavy thing
**[39:07]** in the world.
**[39:07]** So, there are definitely, for research,
**[39:13]** you need like definitely some amount of compute,
**[39:16]** but it's far from obvious that you need
**[39:18]** the absolutely largest amount of compute ever for research.
**[39:22]** You might argue, and I think it is true,
**[39:25]** that if you want to build the absolutely best system,
**[39:28]** if you wanna build the absolutely best system,
**[39:31]** then it helps to have much more compute.
**[39:33]** And especially if everyone is within the same paradigm,
**[39:37]** then compute becomes one of the big differentiators.
**[39:42]** Yeah, I guess, while it was possible to develop these ideas,
**[39:46]** I'm asking you for the history,
**[39:47]** because you were actually there.
**[39:48]** I'm not sure what actually happened,
**[39:49]** but it sounds like it was possible to develop these ideas
**[39:52]** using minimal amounts of compute,
**[39:55]** but it wasn't, the Transformer
**[39:56]** didn't immediately become famous.
**[39:57]** It became the thing everybody started doing
**[40:00]** and then started experimenting on top of
**[40:01]** and building on top of,
**[40:03]** because it was validated
**[40:04]** at higher and higher levels of compute.
**[40:06]** Correct.
**[40:07]** And if you at SSI have 50 different ideas,
**[40:11]** how will you know which one is the next Transformer
**[40:13]** and which one is brittle
**[40:17]** without having the kinds of compute
**[40:20]** that other frontier labs have?
**[40:22]** So, I can comment on that,
**[40:24]** which is, the short comment is that,
**[40:28]** when we mentioned SSI,
**[40:30]** specifically for us,
**[40:33]** the amount of compute that SSI has for research
**[40:38]** is really not that small.
**[40:41]** And I want to explain why,
**[40:42]** like a simple math can explain
**[40:44]** why the amount of compute that we have
**[40:45]** is actually a lot more comparable for research
**[40:49]** than one might think.
**[40:51]** Now explain.
**[40:52]** So, SSI has raised $3 billion.
**[40:58]** Which is like, not small,
**[41:01]** it's like a lot by any absolute sense,
**[41:04]** but you could say,
**[41:05]** but look at the other companies raising much more.
**[41:08]** But a lot of their compute goes for inference.
**[41:13]** Like these big numbers, these big loans,
**[41:16]** it's earmarked for inference.
**[41:18]** That's number one.
**[41:20]** Number two, you need,
**[41:21]** if you want to have a product on which you do inference,
**[41:24]** you need to have a big staff of engineers,
**[41:27]** a lot of salespeople,
**[41:28]** a lot of the research needs to be dedicated
**[41:30]** for producing all kinds of product related features.
**[41:35]** So then when you look at what's actually left for research,
**[41:38]** the difference becomes a lot smaller.
**[41:42]** Now, the other thing is,
**[41:44]** is that if you are doing something different,
**[41:47]** do you really need the absolute maximal scale to prove it?
**[41:51]** I don't think it's true at all.
**[41:52]** I think that in our case,
**[41:55]** we have sufficient compute to prove,
**[41:59]** to convince ourselves and anyone else
**[42:00]** that what we're doing is correct.
**[42:02]** There's been public estimates that companies like OpenAI
**[42:05]** spend on the order of five, $6 billion a year,
**[42:09]** just so far on experiments.
**[42:12]** This is separate from the amount of money
**[42:13]** they're sending on inference and so forth.
**[42:16]** So it seems like they're spending more a year
**[42:18]** running research experiments
**[42:20]** than you guys have in total funding.
**[42:23]** I think it's a question of what you do with it.
**[42:26]** I think in their case, in the case of others,
**[42:29]** I think there's a lot more demand on the training compute.
**[42:32]** There's a lot more different work streams.
**[42:35]** There are different modalities.
**[42:37]** There is just more stuff.
**[42:39]** And so it becomes fragmented.
**[42:42]** How will SSI make money?
**[42:43]** You know, my answer to this question is something like,
**[42:50]** right now we just focus on the research
**[42:53]** and then the answer to this question will reveal itself.
**[42:56]** I think there will be lots of possible answers.
**[42:58]** Hmm.
**[42:59]** Is SSI's plan still to straight shot superintelligence?
**[43:02]** Maybe.
**[43:04]** I think that there is merit to it.
**[43:07]** I think there's a lot of merit
**[43:08]** because I think that it's very nice
**[43:10]** to not be affected by the day-to-day market competition.
**[43:15]** But I think there are two reasons
**[43:21]** that may cause us to change the plan.
**[43:25]** One is pragmatic.
**[43:26]** If timelines turned out to be long, which they might.
**[43:31]** And second, I think there is a lot of value
**[43:34]** in the best and most powerful AI
**[43:39]** being out there impacting the world.
**[43:42]** Yeah.
**[43:43]** I think this is a meaningfully valuable thing.
**[43:46]** But then, so why is your default plan
**[43:47]** to straight shot superintelligence?
**[43:49]** Because it sounds like OpenAI, Anthropic,
**[43:52]** all these other companies,
**[43:53]** their explicit thinking is,
**[43:55]** look, we have weaker and weaker intelligences
**[43:57]** that the public can get used to and prepare for.
**[44:00]** And why is it potentially better
**[44:03]** to build a superintelligence directly?
**[44:06]** So I'll make the case for and against.
**[44:08]** Yeah.
**[44:09]** The case for is that you are,
**[44:11]** so one of the challenges that people face
**[44:15]** when they're in the market
**[44:16]** is that they have to participate in the rat race.
**[44:20]** And the rat race is quite difficult
**[44:22]** in that it exposes you to difficult trade-offs
**[44:25]** which you need to make.
**[44:27]** And there is, it is nice to say,
**[44:31]** we'll insulate ourselves from all this
**[44:32]** and just focus on the research
**[44:34]** and come out only when we are ready and not before.
**[44:38]** But the counterpoint is valid too.
**[44:40]** And those are opposing forces.
**[44:43]** The counterpoint is, hey,
**[44:45]** it is useful for the world to see powerful AI.
**[44:50]** It is useful for the world to see powerful AI
**[44:53]** because that's the only way you can communicate it.
**[44:55]** Well, I guess not even just that you can communicate the idea
**[44:57]** but-
**[44:58]** Communicate the AI, not the idea.
**[45:01]** Communicate the AI.
**[45:02]** What do you mean communicate the AI?
**[45:04]** Okay.
**[45:05]** So let's suppose you read an essay about AI
**[45:07]** and the essay says AI is gonna be this
**[45:09]** and AI is gonna be that and it's gonna be this.
**[45:12]** And you read it and you say,
**[45:12]** okay, this is an interesting essay.
**[45:14]** Right.
**[45:15]** Now suppose you see an AI doing this, an AI doing that,
**[45:20]** it is incomparable.
**[45:21]** Like basically, I think that there is a big benefit
**[45:27]** from AI being in the public
**[45:29]** and that would be a reason for us
**[45:33]** to not be quite straight shot.
**[45:35]** Yeah.
**[45:36]** Well, I guess it's not even that,
**[45:38]** but I do think that is an important part of it.
**[45:40]** The other big thing is,
**[45:42]** I can't think of another discipline
**[45:44]** in human engineering and research
**[45:45]** where the end artifact was made safer
**[45:51]** mostly through just thinking about how to make it safe
**[45:54]** as opposed to why are airplane crashes per mile
**[45:57]** so much lower today than there were decades ago?
**[45:59]** Why is it so much harder to find a bug in Linux
**[46:02]** than it would have been decades ago?
**[46:04]** And I think it's mostly because these systems
**[46:06]** were deployed to the world.
**[46:08]** You noticed failures.
**[46:10]** Those failures were corrected
**[46:11]** and the systems became more robust.
**[46:13]** Now I'm not sure why AGI and superhuman intelligence
**[46:17]** would be any different, especially given,
**[46:18]** and I hope we're gonna get to this.
**[46:23]** It seems like the harms of superintelligence
**[46:25]** are not just about having some malevolent paper clipper
**[46:29]** out there, but it's just like,
**[46:31]** this is a really powerful thing
**[46:32]** and we don't even know how to conceptualize
**[46:33]** how people interact with it, what people will do with it.
**[46:36]** And having gradual access to it seems like a better way
**[46:41]** to maybe spread out the impact of it
**[46:43]** and to help people prepare for it.
**[46:45]** Well, I think on this point,
**[46:47]** even in the straight shot scenario,
**[46:50]** you would still do a gradual release of it.
**[46:54]** It's how I would imagine it.
**[46:57]** The gradualism would be an inherent component of any plan.
**[47:03]** It's just a question of what is the first thing
**[47:04]** that you get out of the door?
**[47:06]** That's number one.
**[47:07]** Number two, I also think,
**[47:09]** I believe you have advocated for continual learning
**[47:12]** more than other people.
**[47:14]** And I actually think that this is an important
**[47:17]** and correct thing.
**[47:19]** And here is why.
**[47:21]** So one of the things, so I'll give you another example
**[47:25]** of how language affects thinking.
**[47:29]** And in this case, this will be two words,
**[47:32]** two words that have shaped everyone's thinking,
**[47:35]** I maintain.
**[47:37]** First word, AGI.
**[47:40]** Second word, pre-training.
**[47:42]** Let me explain.
**[47:44]** So the word, the term AGI, why does this term exist?
**[47:50]** It's a very particular term.
**[47:51]** Why does it exist?
**[47:52]** There's a reason.
**[47:54]** The reason that the term AGI exists
**[47:57]** is in my opinion, not so much
**[47:59]** because it's like a very important,
**[48:02]** essential descriptor of some end state of intelligence,
**[48:06]** but because it is a reaction
**[48:12]** to a different term that existed.
**[48:14]** And the term is narrow AI.
**[48:17]** If you go back to ancient history of gameplay in AI,
**[48:21]** of checkers AI, chess AI, computer games AI,
**[48:24]** everyone would say, look at this narrow intelligence.
**[48:27]** Sure, the chess AI can beat Kasparov,
**[48:29]** but it can't do anything else.
**[48:30]** It is so narrow, artificial, narrow intelligence.
**[48:34]** So in response, as a reaction to this,
**[48:37]** some people said, well, this is not good.
**[48:41]** It is so narrow.
**[48:42]** What we need is general AI.
**[48:46]** General AI, an AI that can just do all the things.
**[48:50]** The second, and that term just got a lot of traction.
**[48:55]** Yeah.
**[48:57]** The second thing that got a lot of traction is pre-training.
**[49:01]** Specifically the recipe of pre-training.
**[49:03]** I think the current, the way people do RL now
**[49:05]** is maybe is undoing the conceptual imprint of pre-training,
**[49:12]** but pre-training had the property.
**[49:14]** You do more pre-training and the model gets better
**[49:17]** at everything more or less uniformly.
**[49:21]** General AI, pre-training gives AGI.
**[49:27]** But the thing that happened with AGI and pre-training
**[49:33]** is that in some sense, they overshot the target.
**[49:36]** Because by the kind, if you think about the term AGI,
**[49:40]** you will realize,
**[49:41]** and especially in the context of pre-training,
**[49:43]** you will realize that a human being is not an AGI.
**[49:48]** Because a human being,
**[49:50]** yes, there is definitely a foundation of skills.
**[49:53]** A human being lacks a huge amount of knowledge.
**[50:00]** Instead, we rely on continual learning.
**[50:03]** We rely on continual learning.
**[50:04]** And so then when you think about,
**[50:06]** okay, so let's suppose that we achieve success
**[50:08]** and we produce some kind of safe super intelligence.
**[50:12]** The question is, but how do you define it?
**[50:14]** Where on the curve of continual learning is it going to be?
**[50:18]** I will produce like a super intelligent 15 year old
**[50:21]** that's very eager to go.
**[50:22]** And you say, okay, I'm going to,
**[50:23]** they don't know very much at all.
**[50:25]** The great student, very eager.
**[50:27]** You go and be a programmer.
**[50:29]** You go and be a doctor.
**[50:31]** Go and learn.
**[50:32]** So you could imagine that the deployment itself
**[50:35]** will involve some kind of a learning trial and error period.
**[50:38]** It's a process as opposed to you drop the finished thing.
**[50:43]** Okay, I see.
**[50:44]** So you're suggesting that the thing you're pointing out
**[50:49]** with super intelligence is not some finished mind
**[50:56]** which knows how to do every single job in the economy.
**[50:58]** Because the way, say, the original,
**[51:01]** I think open AI charter or whatever defines AGI
**[51:03]** is like it can do every single job
**[51:06]** that every single thing a human can do.
**[51:08]** You're proposing instead a mind which can learn
**[51:12]** to do every single job.
**[51:13]** Yes.
**[51:14]** And that is super intelligence.
**[51:16]** But once you have the learning algorithm,
**[51:19]** it gets deployed into the world
**[51:21]** the same way a human laborer might join an organization.
**[51:25]** And it seems like one of these two things might happen.
**[51:28]** Maybe neither of these happens.
**[51:29]** One, this super efficient learning algorithm
**[51:35]** becomes superhuman, becomes as good as you
**[51:38]** and potentially even better at the task of ML research.
**[51:43]** And as a result, the algorithm itself
**[51:46]** becomes more and more superhuman.
**[51:47]** The other is, even if that doesn't happen,
**[51:50]** if you have a single model,
**[51:52]** I mean, this is explicitly your vision.
**[51:53]** If you have a single model or instances of a model
**[51:56]** which are deployed through the economy,
**[51:59]** doing different jobs, learning how to do those jobs,
**[52:00]** continually learning on the job,
**[52:03]** picking up all the skills that any human could pick up,
**[52:05]** but actually picking them all up at the same time
**[52:07]** and then amalgamating the learnings.
**[52:10]** You basically have a model
**[52:11]** which functionally becomes super intelligent
**[52:14]** even without any sort of recursive self-improvement
**[52:17]** in software, right?
**[52:19]** Because you now have one model
**[52:20]** that can do every single job in the economy
**[52:22]** and humans can't merge our minds in the same way.
**[52:25]** And so do you expect some sort of like intelligence explosion
**[52:27]** from broad deployment?
**[52:28]** I think that it is likely
**[52:32]** that we will have rapid economic growth.
**[52:37]** I think the broad deployment,
**[52:40]** like there are two arguments you could make
**[52:44]** which are conflicting.
**[52:46]** One is that, look, if indeed you get,
**[52:49]** once indeed you get to a point
**[52:52]** where you have an AI that can learn to do things quickly
**[52:59]** and you have many of them,
**[53:01]** then they will be a strong force
**[53:05]** to deploy them in the economy
**[53:07]** unless there will be some kind of a regulation
**[53:09]** that stops it, which by the way, there might be.
**[53:13]** But I think the idea of very rapid economic growth
**[53:18]** for some time, I think it's very possible
**[53:20]** from broad deployment.
**[53:21]** Then the question is how rapid it's going to be.
**[53:25]** So I think this is hard to know
**[53:26]** because on the one hand,
**[53:28]** you have this very efficient worker.
**[53:30]** On the other hand, the world is just really big
**[53:33]** and there's a lot of stuff
**[53:36]** and that stuff moves at a different speed.
**[53:38]** But then on the other hand, now the AI could,
**[53:41]** so I think very rapid economic growth is possible.
**[53:44]** And we will see like all kinds of things
**[53:46]** like different countries with different rules
**[53:49]** and the ones which have the friendlier rules,
**[53:51]** the economic growth will be faster.
**[53:53]** Hard to predict.
**[53:54]** Some people in our audience like to read the transcripts
**[53:56]** instead of listening to the episode.
**[53:58]** And so we put a ton of effort
**[53:59]** into making the transcripts read
**[54:02]** like they are standalone essays.
**[54:04]** The problem is that if you just transcribe
**[54:06]** a conversation verbatim using a speech to text model,
**[54:09]** it'll be full of all kinds of fits and starts
**[54:12]** and confusing phrasing.
**[54:13]** We mentioned this problem to Labelbox
**[54:15]** and they asked if they could take a stab.
**[54:17]** Working with them on this is probably the reason
**[54:19]** that I'm most excited to recommend Labelbox to people.
**[54:22]** It wasn't just, oh, hey, tell us what kind of data you need
**[54:24]** and we'll go get it.
**[54:25]** They walked us through the entire process
**[54:27]** from helping us identify what kind of data
**[54:29]** we needed in the first place
**[54:30]** to assembling a team of expert aligners to generate it.
**[54:34]** Even after we got all the data back,
**[54:36]** Labelbox stayed involved.
**[54:38]** They helped us choose the right base model
**[54:40]** and set up auto QA on the model's output
**[54:43]** so that we could tweak and refine it.
**[54:44]** And now we have a new transcriber tool
**[54:46]** that we can use for all our episodes moving forward.
**[54:49]** This is just one example of how Labelbox
**[54:52]** meets their customers at the ideas level
**[54:54]** and partners with them through their entire journey.
**[54:57]** If you wanna learn more
**[54:58]** or if you wanna try out the transcriber tool yourself,
**[55:01]** go to labelbox.com slash thwarkash.
**[55:07]** It seems to me that this is a very precarious situation
**[55:10]** to be in where, look, in the limit,
**[55:14]** we know that this should be possible
**[55:15]** because if you have something that is as good
**[55:17]** as a human at learning, but which can merge its brains,
**[55:22]** merge their different instances
**[55:23]** in a way that humans can't merge,
**[55:25]** already this seems like a thing
**[55:27]** that should physically be possible.
**[55:28]** Humans are possible.
**[55:29]** Digital computers are possible.
**[55:31]** You just need both of those combined to produce this thing.
**[55:33]** And it also seems like this kind of thing
**[55:34]** is extremely powerful
**[55:40]** and economic growth is one way to put it.
**[55:43]** I mean, Dyson Spear is a lot of economic growth,
**[55:45]** but another way to put it is just like,
**[55:47]** you will have potentially a very short period of time
**[55:50]** because a human on the job can,
**[55:52]** you know, you're hiring people to SSI in six months,
**[55:54]** they're like net productive probably, right?
**[55:56]** A human like learns really fast.
**[55:57]** And so this thing is becoming smarter and smarter very fast.
**[56:01]** How do you think about making that go well?
**[56:03]** And why is SSI positioned to do that well?
**[56:05]** What is SSI's plan there basically is what I'm trying to ask.
**[56:08]** Yeah.
**[56:10]** So one of the ways in which my thinking has been changing
**[56:16]** is that I now place more importance
**[56:22]** on AI being deployed incrementally and in advance.
**[56:30]** One very difficult thing about AI
**[56:34]** is that we are talking about systems that don't yet exist.
**[56:40]** And it's hard to imagine them.
**[56:43]** I think that one of the things that's happening
**[56:46]** is that in practice, it's very hard to feel the AGI.
**[56:52]** It's very hard to feel the AGI.
**[56:54]** We can talk about it,
**[56:56]** but it's like talking about like the long future,
**[57:00]** like imagine like having a conversation
**[57:02]** about like how is it like to be old?
**[57:04]** When you're like old and frail
**[57:07]** and you can have a conversation, you can try to imagine it,
**[57:09]** but it's just hard and you come back to reality
**[57:13]** where that's not the case.
**[57:15]** And I think that a lot of the issues around AGI
**[57:21]** and its future power stem from the fact
**[57:26]** that it's very difficult to imagine.
**[57:30]** Future AI is going to be different.
**[57:34]** It's going to be powerful.
**[57:35]** Indeed, the whole problem, what is the problem of AI and AGI?
**[57:40]** The whole problem is the power.
**[57:43]** The whole problem is the power.
**[57:46]** When the power is really big, what's gonna happen?
**[57:50]** And one of the ways in which I've changed my mind
**[57:53]** over the past year,
**[57:54]** and so that change of mind may back,
**[57:59]** may, I'll say, I'll hedge a little bit,
**[58:02]** may back propagate into the plans of our company is that,
**[58:08]** so if it's hard to imagine, what do you do?
**[58:12]** You gotta be showing the thing.
**[58:14]** You gotta be showing the thing.
**[58:16]** And I maintain that I think most people
**[58:19]** who work on AI also can't imagine it
**[58:23]** because it's too different from what people see
**[58:25]** on a day-to-day basis.
**[58:28]** I do maintain, here's something which I predict will happen.
**[58:32]** That's a prediction.
**[58:34]** I maintain that as AI becomes more powerful,
**[58:40]** then people will change their behaviors.
**[58:45]** And we will see all kinds of unprecedented things
**[58:48]** which are not happening right now.
**[58:51]** And I'll give some examples.
**[58:53]** I do, like, I think for better or worse,
**[58:56]** the frontier companies will play a very important role
**[59:00]** in what happens, as will the government.
**[59:03]** And the kind of things that I think we'll see,
**[59:05]** which you see the beginnings of,
**[59:08]** companies that are fierce competitors
**[59:11]** starting to collaborate on AI safety.
**[59:16]** You may have seen OpenAI and Anthropic
**[59:19]** doing a first small step, but that did not exist.
**[59:22]** That's actually something which I predicted
**[59:24]** in one of my talks about three years ago,
**[59:27]** that such a thing will happen.
**[59:29]** I also maintain that as AI continues to become
**[59:31]** more powerful, more visibly powerful,
**[59:36]** there will also be a desire from governments
**[59:39]** and the public to do something.
**[59:42]** And I think that this is a very important force.
**[59:46]** Of showing the AI, that's number one.
**[59:49]** Number two, okay, so then the AI is being built.
**[59:51]** What needs to be done?
**[59:55]** So, one thing that I maintain that will happen
**[59:58]** is that right now, people who are...
**[01:00:00]** working on AI, I maintain that the AI doesn't feel powerful
**[01:00:04]** because of its mistakes.
**[01:00:06]** I do think that at some point,
**[01:00:07]** the AI will start to feel powerful, actually.
**[01:00:10]** And I think when that happens,
**[01:00:12]** we will see a big change in the way
**[01:00:15]** all AI companies approach safety.
**[01:00:19]** They'll become much more paranoid.
**[01:00:21]** I think I say this as a prediction that we will see happen.
**[01:00:26]** We'll see if I'm right.
**[01:00:27]** But I think this is something that will happen
**[01:00:29]** because they will see the AI becoming more powerful.
**[01:00:32]** Everything that's happening right now, I maintain,
**[01:00:35]** is because people look at today's AI
**[01:00:38]** and it's hard to imagine the future AI.
**[01:00:42]** And there is a third thing which needs to happen.
**[01:00:45]** And I think this is,
**[01:00:46]** and I'm talking about it in broader terms,
**[01:00:49]** not just from the perspective of SSI,
**[01:00:52]** because you asked me about our company,
**[01:00:54]** but the question is, okay,
**[01:00:55]** so then what should the companies aspire to build?
**[01:00:58]** What should they aspire to build?
**[01:01:00]** And there has been one big idea
**[01:01:01]** that actually everyone has been locked into,
**[01:01:05]** which is the self-improving AI.
**[01:01:09]** And why did it happen?
**[01:01:11]** Because there is fewer ideas than companies.
**[01:01:14]** But I maintain that there is something
**[01:01:16]** that's better to build.
**[01:01:18]** And I think that everyone will actually want that.
**[01:01:21]** It's like the AI that's robustly aligned
**[01:01:26]** to care about sentient life specifically.
**[01:01:29]** I think in particular, it will be,
**[01:01:31]** there's a case to be made that it will be easier
**[01:01:34]** to build an AI that cares about sentient life
**[01:01:37]** than an AI that cares about human life alone,
**[01:01:40]** because the AI itself will be sentient.
**[01:01:44]** And if you think about things like mirror neurons
**[01:01:46]** and human empathy for animals, which is,
**[01:01:49]** you might argue it's not big enough, but it exists.
**[01:01:53]** I think it's an emergent property
**[01:01:54]** from the fact that we model others
**[01:01:57]** with the same circuit that we used to model ourselves,
**[01:02:01]** because that's the most efficient thing to do.
**[01:02:03]** So even if you got an AI to care about sentient beings,
**[01:02:08]** and it's not actually clear to me
**[01:02:09]** that that's what you should try to do
**[01:02:10]** if you solve the alignment,
**[01:02:12]** it would still be the case
**[01:02:13]** that most sentient beings will be AIs.
**[01:02:16]** There will be trillions, eventually quadrillions of AIs.
**[01:02:19]** Humans will be a very small fraction of sentient beings.
**[01:02:23]** So it's not clear to me if the goal
**[01:02:26]** is some kind of human control over this future civilization,
**[01:02:32]** that this is the best criterion.
**[01:02:35]** It's true.
**[01:02:36]** I think that it's possible it's not the best criterion.
**[01:02:40]** I'll say two things.
**[01:02:42]** I think that, thing number one,
**[01:02:47]** I think that if there, so,
**[01:02:50]** I think that care for sentient life,
**[01:02:52]** I think there is merit to it.
**[01:02:54]** I think it should be considered.
**[01:02:56]** I think that it will be helpful
**[01:02:58]** if there was some kind of a shortlist of ideas
**[01:03:03]** that then the companies,
**[01:03:06]** when they are in the situation, could use.
**[01:03:09]** That's number two.
**[01:03:10]** Number three, I think it would be really materially helpful
**[01:03:13]** if the power of the most powerful superintelligence
**[01:03:17]** was somehow capped,
**[01:03:20]** because it would address a lot of these concerns.
**[01:03:23]** The question of how to do it, I'm not sure,
**[01:03:26]** but I think that would be materially helpful
**[01:03:29]** when you're talking about really, really powerful systems.
**[01:03:32]** Yeah.
**[01:03:33]** Before we continue the alignment discussion,
**[01:03:35]** I wanna double click on that.
**[01:03:37]** How much room is there at the top?
**[01:03:38]** How do you think about superintelligence?
**[01:03:40]** Do you think, I mean, using this learning efficiency idea,
**[01:03:44]** maybe it's just extremely fast at learning new skills
**[01:03:47]** or new knowledge,
**[01:03:48]** and does it just have a bigger pool of strategies?
**[01:03:51]** Is there a single cohesive it in the center
**[01:03:54]** that's more powerful or bigger?
**[01:03:57]** And if so, do you imagine that this will be sort of godlike
**[01:04:02]** in comparison to the rest of human civilization,
**[01:04:03]** or does it just feel like another agent
**[01:04:06]** or another cluster of agents?
**[01:04:08]** So this is an area where different people
**[01:04:10]** have different intuitions.
**[01:04:11]** I think it will be very powerful for sure.
**[01:04:14]** I think that what I think is most likely to happen
**[01:04:19]** is that there will be multiple such AIs
**[01:04:24]** being created roughly at the same time.
**[01:04:27]** I think that if the cluster is big enough,
**[01:04:33]** like if the cluster is literally continent-sized,
**[01:04:36]** that thing could be really powerful indeed, right?
**[01:04:39]** If you literally have a continent-sized cluster,
**[01:04:42]** like those AIs can be very powerful.
**[01:04:44]** And like all I can tell you
**[01:04:48]** is that if you're talking about extremely powerful AIs,
**[01:04:51]** like truly dramatically powerful,
**[01:04:53]** then yeah, it would be nice
**[01:04:54]** if they could be restrained in some ways,
**[01:04:59]** or if there was some kind of an agreement or something.
**[01:05:03]** Because I think that if you are saying,
**[01:05:05]** hey, like if you really,
**[01:05:07]** like what is the concern of superintelligence?
**[01:05:11]** What is one way to explain the concern?
**[01:05:13]** If you imagine a system that is sufficiently powerful,
**[01:05:17]** like really sufficiently powerful,
**[01:05:20]** and you could say, okay, you need to do something sensible,
**[01:05:23]** like care for sentient life, let's say,
**[01:05:25]** in a very single-minded way,
**[01:05:27]** we might not like the results.
**[01:05:29]** That's really what it is.
**[01:05:30]** And so maybe by the way,
**[01:05:31]** the answer is that you do not build a single,
**[01:05:33]** you do not build an RL agent in the usual sense.
**[01:05:36]** And actually I'll point several things out.
**[01:05:39]** I think human beings are a semi-RL agent.
**[01:05:43]** You know, we pursue a reward
**[01:05:44]** and then the emotions or whatever
**[01:05:47]** make us tire out of the reward.
**[01:05:48]** We pursue a different reward.
**[01:05:50]** The market is like,
**[01:05:53]** it's like a very short-sighted kind of agent.
**[01:05:56]** Evolution is the same.
**[01:05:57]** Evolution is very intelligent in some ways,
**[01:05:59]** but very dumb in other ways.
**[01:06:01]** The government has been designed
**[01:06:03]** to be a never-ending fight between three parts,
**[01:06:06]** which has an effect.
**[01:06:08]** So I think things like this.
**[01:06:11]** Another thing that makes this discussion difficult
**[01:06:13]** is that we are talking about systems that don't exist,
**[01:06:16]** that we don't know how to build.
**[01:06:19]** Right, that's the other thing.
**[01:06:20]** And that's actually my belief.
**[01:06:21]** I think what people are doing right now
**[01:06:23]** will go some distance and then peter out.
**[01:06:26]** It will continue to improve, but it will also not be it.
**[01:06:29]** So the it, we don't know how to build.
**[01:06:33]** And I think that a lot hinges on understanding
**[01:06:38]** reliable generalization.
**[01:06:41]** And I'll say another thing, which is like,
**[01:06:45]** you know, one of the things that you could say
**[01:06:46]** is what would that cause alignment to be difficult
**[01:06:48]** is that human value, that it's,
**[01:06:53]** your ability to learn human values is fragile.
**[01:06:55]** Then your ability to optimize them is fragile.
**[01:06:57]** You will, you actually learn to optimize them.
**[01:07:00]** And then can't you say,
**[01:07:01]** are these not all instances of unreliable generalization?
**[01:07:05]** Why is it that human beings
**[01:07:07]** appear to generalize so much better?
**[01:07:10]** What if generalization was much better?
**[01:07:11]** What would happen in this case?
**[01:07:13]** What would be the effect?
**[01:07:14]** But those, we can't, we can't,
**[01:07:15]** like those questions are right now still unanswerable.
**[01:07:19]** How does one think about what AI going well looks like?
**[01:07:24]** Because I think you've scoped out how AI might evolve.
**[01:07:27]** We'll have these sort of continual learning agents.
**[01:07:29]** AI will be very powerful.
**[01:07:31]** Maybe there will be many different AIs.
**[01:07:33]** How do you think about lots of continent
**[01:07:36]** compute size intelligences going around?
**[01:07:39]** How dangerous is that?
**[01:07:42]** How do we make that less dangerous?
**[01:07:44]** And how do we do that in a way that
**[01:07:48]** protects a equilibrium where
**[01:07:51]** there might be misaligned AIs out there
**[01:07:53]** and bad actors out there?
**[01:07:56]** So one reason why I liked the AI
**[01:07:58]** that cares for sentient life,
**[01:08:00]** you know, and we can debate on whether it's good or bad,
**[01:08:03]** but if the first N of these dramatic systems
**[01:08:10]** actually do care for, you know,
**[01:08:14]** love humanity or something, you know,
**[01:08:16]** care for sentient life,
**[01:08:17]** obviously this also needs to be achieved.
**[01:08:20]** This needs to be achieved.
**[01:08:22]** So if this is achieved by the first N of those systems,
**[01:08:27]** then I can see it go well,
**[01:08:30]** at least for quite some time.
**[01:08:33]** And then there is the question
**[01:08:34]** of what happens in the long run?
**[01:08:35]** What happens in the long run?
**[01:08:36]** How do you achieve a long run equilibrium?
**[01:08:39]** And I think that there,
**[01:08:42]** there is an answer as well.
**[01:08:44]** And I don't like this answer,
**[01:08:47]** but it needs to be considered.
**[01:08:51]** In the long run, you might say, okay,
**[01:08:53]** so if you have a world where powerful AIs exist,
**[01:08:57]** in the short run, you could say, okay,
**[01:08:58]** you have universal high income.
**[01:09:01]** We have universal high income and we're all doing well,
**[01:09:04]** but we know that, what do the Buddhists say?
**[01:09:07]** Change is the only constant.
**[01:09:09]** And so things change.
**[01:09:10]** And there is some kind of government,
**[01:09:12]** political structure thing, and it changes
**[01:09:15]** because these things have a shelf life.
**[01:09:18]** You know, some new government thing comes up
**[01:09:20]** and it functions.
**[01:09:21]** And then after some time it stops functioning.
**[01:09:25]** That's something that we see happening all the time.
**[01:09:27]** And so I think that for the long run equilibrium,
**[01:09:32]** one approach, you could say, okay,
**[01:09:34]** so maybe every person will have an AI
**[01:09:36]** that will do their bidding.
**[01:09:38]** And that's good.
**[01:09:40]** And if that could be maintained indefinitely, that's true.
**[01:09:43]** But the downside with that is, okay,
**[01:09:45]** so then the AI goes and like,
**[01:09:48]** earns money for the person and, you know,
**[01:09:52]** advocates for their needs in like the political sphere.
**[01:09:55]** And maybe then writes a little report saying,
**[01:09:57]** okay, here's what I've done.
**[01:09:58]** Here's the situation.
**[01:09:59]** And the person says, great, keep it up.
**[01:10:02]** But the person is no longer a participant.
**[01:10:05]** And then you can say that's a precarious place to be in.
**[01:10:08]** But, so I'm gonna preface by saying,
**[01:10:13]** I don't like this solution, but it is a solution.
**[01:10:18]** And the solution is if people become part AI
**[01:10:21]** with some kind of Neuralink++.
**[01:10:23]** Because what will happen as a result
**[01:10:25]** is that now the AI understands something
**[01:10:28]** and we understand it too.
**[01:10:31]** Because now the understanding is transmitted wholesale.
**[01:10:34]** So now if the AI is in some situation,
**[01:10:36]** now it's like you are involved
**[01:10:39]** in that situation yourself fully.
**[01:10:41]** And I think this is the answer to the equilibrium.
**[01:10:44]** I wonder if the fact that emotions,
**[01:10:47]** which were developed millions,
**[01:10:52]** or in many cases, billions of years ago
**[01:10:54]** in a totally different environment,
**[01:10:55]** are still guiding our actions so strongly
**[01:11:00]** is an example of alignment success.
**[01:11:03]** To maybe spell out what I mean,
**[01:11:06]** the brainstem has these,
**[01:11:10]** I don't know if it's more accurate
**[01:11:11]** to call it a value function or a reward function,
**[01:11:12]** but the brainstem has a directive where it's saying,
**[01:11:15]** mate with somebody who's more successful.
**[01:11:17]** The cortex is the part that understands
**[01:11:19]** what does success mean in the modern context.
**[01:11:22]** But the brainstem is able to align the cortex and say,
**[01:11:26]** however you recognize success to be,
**[01:11:27]** and I'm not smart enough to understand what that is,
**[01:11:29]** you're still gonna pursue this directive.
**[01:11:31]** I think there is,
**[01:11:34]** so I think there's a more general point.
**[01:11:36]** I think it's actually really mysterious
**[01:11:38]** how the brain encodes high-level desires.
**[01:11:43]** Sorry, how evolution encodes high-level desires.
**[01:11:46]** Like it's pretty easy to understand
**[01:11:48]** how evolution would endow us with the desire
**[01:11:52]** for food that smells good.
**[01:11:54]** Because smell is a chemical.
**[01:11:56]** And so just pursue that chemical.
**[01:11:58]** It's very easy to imagine evolution doing such a thing.
**[01:12:02]** But evolution also has endowed us
**[01:12:05]** with all these social desires.
**[01:12:08]** Like we really care about being seen positively by society.
**[01:12:12]** We care about being in a good standing.
**[01:12:15]** Like all these social intuitions that we have,
**[01:12:19]** I feel strongly that they're baked in.
**[01:12:22]** And I don't know how evolution did it
**[01:12:26]** because it's a high-level concept
**[01:12:27]** that's represented in the brain.
**[01:12:29]** Like what people think,
**[01:12:31]** like let's say you are like,
**[01:12:32]** you care about some social thing.
**[01:12:37]** It's not like a low-level signal like smell.
**[01:12:40]** It's not something that for which there is a sensor.
**[01:12:43]** Like the brain needs to do a lot of processing
**[01:12:46]** to piece together lots of bits of information
**[01:12:48]** to understand what's going on socially.
**[01:12:51]** And somehow evolution said,
**[01:12:52]** that's what you should care about.
**[01:12:54]** How did it do it?
**[01:12:55]** And it did it quickly too.
**[01:12:57]** Because I think all these sophisticated social things
**[01:13:00]** that we care about,
**[01:13:02]** I think they evolved pretty recently.
**[01:13:04]** So evolution had an easy time
**[01:13:06]** hard-coding this high-level desire.
**[01:13:08]** And I maintain, or at least I'll say,
**[01:13:11]** I'm unaware of good hypothesis for how it's done.
**[01:13:15]** I had some ideas I was kicking around,
**[01:13:18]** but none of them are satisfying.
**[01:13:23]** Yeah.
**[01:13:24]** And what's especially impressive
**[01:13:25]** is it was a desire that you learned in your lifetime.
**[01:13:28]** It kind of makes sense because your brain is intelligent.
**[01:13:31]** It makes sense why we would be able
**[01:13:32]** to learn intelligent desires.
**[01:13:34]** But your point is that the desire is,
**[01:13:37]** maybe this is not your point,
**[01:13:38]** but one way to understand it is,
**[01:13:40]** the desire is built into the genome
**[01:13:42]** and the genome is not intelligent, right?
**[01:13:44]** But it's able to,
**[01:13:44]** you're somehow able to describe this feature that requires,
**[01:13:48]** it's not even clear how you define that feature
**[01:13:50]** and you can get it into,
**[01:13:52]** you can build it into the genes.
**[01:13:53]** Yeah, essentially.
**[01:13:54]** Or maybe I'll put it differently.
**[01:13:55]** If you think about the tools
**[01:13:57]** that are available to the genome,
**[01:14:00]** it says, okay, here's a recipe for building a brain.
**[01:14:03]** And you could say,
**[01:14:04]** here is a recipe for connecting the dopamine neurons
**[01:14:06]** to the smell sensor.
**[01:14:08]** Yeah.
**[01:14:09]** And if the smell is a certain kind of good smell,
**[01:14:11]** you wanna eat that.
**[01:14:12]** I could imagine the genome doing that.
**[01:14:15]** I'm claiming that it is harder to imagine.
**[01:14:18]** It's harder to imagine the genome saying,
**[01:14:21]** you should care about some complicated computation
**[01:14:25]** that your entire brain,
**[01:14:26]** that like a big chunk of your brain does.
**[01:14:28]** That's all I'm claiming.
**[01:14:29]** I can tell you like a speculation.
**[01:14:31]** I was wondering how it could be done.
**[01:14:33]** And let me offer a speculation
**[01:14:34]** and I'll explain why the speculation is probably false.
**[01:14:37]** So the speculation is,
**[01:14:39]** okay, so the brain,
**[01:14:43]** it's like the brain has those regions.
**[01:14:46]** You know the brain regions.
**[01:14:47]** We have our cortex, right?
**[01:14:49]** Yeah.
**[01:14:50]** It has all those brain regions.
**[01:14:51]** And the cortex is uniform,
**[01:14:53]** but the brain regions and the neurons in the cortex,
**[01:14:56]** they kind of speak to their neighbors mostly.
**[01:14:59]** And that explains why you get brain regions.
**[01:15:01]** Because if you wanna do some kind of speech processing,
**[01:15:03]** all the neurons that do speech need to talk to each other.
**[01:15:06]** And because neurons can only speak to their nearby neighbors
**[01:15:08]** for the most part, it has to be a region.
**[01:15:11]** All the regions are mostly located in the same place
**[01:15:13]** from person to person.
**[01:15:15]** So maybe evolution hard-coded
**[01:15:16]** literally a location on the brain.
**[01:15:21]** So it says, oh, like when like, you know,
**[01:15:24]** the GPS of the brain, GPS coordinates, such and such,
**[01:15:27]** when that fires, that's what you should care about.
**[01:15:28]** Like maybe that's what evolution did
**[01:15:30]** because that would be within the toolkit of evolution.
**[01:15:33]** Yeah.
**[01:15:34]** Although there are examples where, for example,
**[01:15:36]** people who are born blind have that area of their cortex
**[01:15:39]** adopted by another sense.
**[01:15:44]** And I have no idea, but I'd be surprised
**[01:15:47]** if the desires or the reward functions
**[01:15:51]** which require visual signal no longer worked.
**[01:15:56]** You know, people who have their different areas
**[01:15:57]** of their cortex co-opted.
**[01:15:58]** For example, if you no longer have vision,
**[01:16:03]** can you still feel the sense
**[01:16:04]** that I want people around me to like me and so forth,
**[01:16:07]** which usually there's also visual cues for.
**[01:16:10]** So I actually fully agree with that.
**[01:16:11]** I think there's an even stronger counter argument
**[01:16:13]** to this theory, which is like, if you think about people,
**[01:16:16]** so there are people who get half of their brains removed
**[01:16:20]** in childhood and they still have all their brain regions,
**[01:16:25]** but they all somehow move to just one hemisphere,
**[01:16:27]** which suggests that the brain regions,
**[01:16:30]** the location is not fixed.
**[01:16:31]** And so that theory is not true.
**[01:16:33]** It would have been cool if it was true, but it's not.
**[01:16:36]** And so I think that's a mystery,
**[01:16:37]** but it's an interesting mystery.
**[01:16:38]** Like the fact is somehow evolution was able to endow us
**[01:16:43]** to care about social stuff very, very reliably.
**[01:16:46]** And even people who have like all kinds
**[01:16:48]** of strange mental conditions and deficiencies
**[01:16:51]** and emotional problems tend to care about this also.
**[01:16:54]** AI tools like deepfakes, voice clones,
**[01:16:57]** and agents have dramatically increased
**[01:16:59]** the sophistication of fraud and abuse.
**[01:17:02]** So it's more important than ever to actually understand
**[01:17:05]** the identity and intent of whoever
**[01:17:09]** or whatever is using your platform.
**[01:17:11]** That's exactly what Sardine helps you do.
**[01:17:13]** Sardine brings together thousands of device behavior
**[01:17:16]** and identity signals to help you assess risk.
**[01:17:19]** Everything from how a user types or moves their mouse
**[01:17:23]** or holds their device,
**[01:17:24]** to whether they're hiding their true location behind a VPN,
**[01:17:28]** to whether they're injecting a fake camera feed
**[01:17:30]** during KYC selfie checks.
**[01:17:32]** Sardine combines these signals with insights
**[01:17:36]** from their network of almost 4 billion devices.
**[01:17:38]** Things like a user's history of fraud
**[01:17:40]** or their associations with other high-risk accounts.
**[01:17:43]** So you can spot bad actors before they do damage.
**[01:17:47]** This would literally be impossible
**[01:17:49]** if you only use data from your own application.
**[01:17:52]** Sardine doesn't stop at detection.
**[01:17:53]** They offer a suite of agents to streamline onboarding checks
**[01:17:57]** and automate investigations.
**[01:17:58]** So as fraudsters use AI to scale their attacks,
**[01:18:02]** you can use AI to scale your defenses.
**[01:18:04]** Go to sardine.ai slash thwarkesh to learn more
**[01:18:09]** and download their guide on AI fraud detection.
**[01:18:13]** What is SSI planning on doing differently?
**[01:18:16]** So presumably your plan is to be one
**[01:18:17]** of the frontier companies when this time arrives.
**[01:18:22]** And then what is,
**[01:18:25]** presumably you started SSI because you're like,
**[01:18:27]** I think I have a way of approaching how to do this safely
**[01:18:29]** in a way that the other companies don't.
**[01:18:32]** What is that difference?
**[01:18:34]** So the way I would describe it as,
**[01:18:37]** there are some ideas that I think are promising
**[01:18:40]** and I want to investigate them
**[01:18:42]** and see if they are indeed promising or not.
**[01:18:44]** It's really that simple.
**[01:18:46]** It's an attempt.
**[01:18:47]** I think that if the ideas turn out to be correct,
**[01:18:49]** these ideas that we discussed
**[01:18:51]** around understanding generalization,
**[01:18:56]** if these ideas turn out to be correct,
**[01:19:00]** then I think we will have something worthy.
**[01:19:03]** If they turn out to be correct, we are doing research.
**[01:19:06]** We are squarely age of research company.
**[01:19:09]** We are making progress.
**[01:19:10]** We've actually made quite good progress over the past year,
**[01:19:12]** but we need to keep making more progress, more research.
**[01:19:16]** And that's how I see it.
**[01:19:17]** I see it as an attempt to be,
**[01:19:22]** an attempt to be a voice and a participant.
**[01:19:27]** People have asked your co-founder and previous CEO
**[01:19:32]** left to go to Metta recently.
**[01:19:35]** And people have asked, well,
**[01:19:37]** if there was a lot of breakthroughs being made,
**[01:19:39]** that seems like a thing that should have been unlikely.
**[01:19:42]** I wonder how you respond.
**[01:19:43]** Yeah, so for this,
**[01:19:45]** I will simply remind a few facts
**[01:19:48]** that may have been forgotten.
**[01:19:50]** And I think these facts which provide the context,
**[01:19:53]** I think they explain the situation.
**[01:19:55]** So the context was that we were fundraising
**[01:19:58]** at a 32 billion valuation.
**[01:20:01]** And then Metta came in and offered to acquire us.
**[01:20:07]** And I said, no, but my former co-founder,
**[01:20:14]** like in some sense said yes.
**[01:20:16]** And as a result, he also was able to enjoy
**[01:20:19]** from a lot of near term liquidity.
**[01:20:21]** And he was the only person from SSI to join Metta.
**[01:20:25]** It sounds like SSI's plan is to be a company
**[01:20:28]** that is at the frontier
**[01:20:29]** when you get to this very important period in human history
**[01:20:33]** where you have superhuman intelligence
**[01:20:35]** and you have these ideas
**[01:20:36]** about how to make superhuman intelligence go well.
**[01:20:39]** But other companies will be trying their own ideas.
**[01:20:42]** What distinguishes SSI's approach
**[01:20:45]** to making superintelligence go well?
**[01:20:48]** The main thing that distinguishes SSI
**[01:20:51]** is its technical approach.
**[01:20:54]** So we have a different technical approach
**[01:20:56]** that I think is worthy and we are pursuing it.
**[01:21:01]** I maintain that in the end,
**[01:21:03]** there will be a convergence of strategies.
**[01:21:06]** So I think there will be a convergence of strategies
**[01:21:08]** where at some point as AI becomes more powerful,
**[01:21:14]** it's going to become more or less clearer to everyone
**[01:21:17]** what the strategy should be.
**[01:21:19]** And it should be something like,
**[01:21:20]** yeah, you need to find some way to talk to each other
**[01:21:24]** and you want your first actual,
**[01:21:27]** like real superintelligent AI to be aligned
**[01:21:30]** and somehow be,
**[01:21:35]** you know, care for sentient life,
**[01:21:37]** care for people, democratic,
**[01:21:39]** one of those, some combination of thereof.
**[01:21:42]** And I think this is the condition
**[01:21:47]** that everyone should strive for.
**[01:21:50]** And that's what SSI is striving for.
**[01:21:52]** And I think that this time, if not already,
**[01:21:57]** all the other companies will be realizing
**[01:21:58]** that they're striving towards the same thing.
**[01:22:00]** And we'll see.
**[01:22:01]** I think that the world will truly change
**[01:22:02]** as AI becomes more powerful.
**[01:22:04]** And I think a lot of these forecasts will,
**[01:22:06]** like, I think things will be really different
**[01:22:09]** and people will be acting really differently.
**[01:22:12]** Speaking of forecasts, what are your forecasts
**[01:22:14]** to this system you're describing,
**[01:22:16]** which can learn as well as a human
**[01:22:19]** and subsequently, as a result, become superhuman?
**[01:22:23]** I think like five to 20.
**[01:22:26]** Five to 20 years?
**[01:22:28]** So I just want to unroll your,
**[01:22:32]** how you might see the world coming.
**[01:22:33]** It's like, we have a couple more years
**[01:22:35]** where these other companies
**[01:22:36]** are continuing the current approach and it stalls out.
**[01:22:39]** And stalls out here, meaning they earn no more
**[01:22:41]** than low hundreds of billions in revenue?
**[01:22:44]** Or how do you think about what stalling out means?
**[01:22:46]** Yeah, I think it could stall out.
**[01:22:51]** And I think stalling out will look like,
**[01:22:56]** it will all look very similar
**[01:22:59]** among all the different companies, something like this.
**[01:23:01]** I'm not sure because I think even with stalling out,
**[01:23:06]** I think these companies could make a stupendous revenue.
**[01:23:10]** Maybe not profits because they will need to work hard
**[01:23:14]** to differentiate each other from themselves.
**[01:23:17]** But revenue, definitely.
**[01:23:18]** But there's something in your model implies that
**[01:23:23]** when the correct solution does emerge,
**[01:23:25]** there will be convergence between all the companies.
**[01:23:27]** And I'm curious why you think that's the case.
**[01:23:30]** Well, I was talking more about convergence
**[01:23:31]** on their largest strategies.
**[01:23:33]** I think eventual convergence on the technical approach
**[01:23:35]** is probably going to happen as well.
**[01:23:37]** But I was alluding to convergence to the largest strategy.
**[01:23:40]** So what exactly is the thing that should be done?
**[01:23:43]** I just want to better understand
**[01:23:45]** how you see the future unrolling.
**[01:23:46]** So currently we have these different companies
**[01:23:48]** and you expect their approach
**[01:23:49]** to continue generating revenue,
**[01:23:51]** but not get to this human-like learner.
**[01:23:54]** So now we have these different forks of companies.
**[01:23:56]** We have you, we have thinking machines,
**[01:23:58]** there's a bunch of other labs.
**[01:24:00]** And maybe one of them figures out the correct approach,
**[01:24:03]** but then the release of their product
**[01:24:04]** makes it clear to other people how to do this thing.
**[01:24:07]** I think it won't be clear how to do it thing,
**[01:24:10]** but it will be clear that something different is possible.
**[01:24:12]** And that is information.
**[01:24:14]** And I think people will then be trying to figure out
**[01:24:18]** how that works.
**[01:24:20]** I do think though that one of the things
**[01:24:23]** that I think not addressed here, not discussed,
**[01:24:27]** is that with each increase in the AI's capabilities,
**[01:24:33]** I think there will be some kind of changes,
**[01:24:36]** but I don't know exactly which ones
**[01:24:39]** in how things are being done.
**[01:24:41]** And so like, I think it's going to be important,
**[01:24:44]** yet I can't spell out what that is exactly.
**[01:24:47]** And how are the, by default,
**[01:24:50]** you would expect the company that has,
**[01:24:52]** the model company that has that model
**[01:24:54]** to be getting all these gains
**[01:24:55]** because they have the model that is learning how to do all,
**[01:24:58]** has the skills and knowledge
**[01:24:59]** that it's building up in the world.
**[01:25:02]** What is the reason to think that the benefits of that
**[01:25:04]** would be widely distributed
**[01:25:05]** and not just end up at whatever model company
**[01:25:07]** gets this continuous learning loop going first?
**[01:25:11]** Like, I think that empirically what happens,
**[01:25:13]** so here is what I think is going to happen.
**[01:25:17]** Number one, I think empirically when,
**[01:25:22]** let's look at how things have gone so far
**[01:25:26]** with the AIs of the past.
**[01:25:28]** So one company produced an advance
**[01:25:31]** and the other company scrambled
**[01:25:33]** and produced some similar things
**[01:25:37]** after some amount of time.
**[01:25:39]** And they started to compete in the market
**[01:25:41]** and push their, push the prices down.
**[01:25:46]** And so I think from the market perspective,
**[01:25:48]** I think something similar will happen there as well.
**[01:25:50]** Even if someone, it's okay,
**[01:25:51]** we are talking about the good world, by the way,
**[01:25:54]** where, what's the good world?
**[01:25:58]** What's the good world?
**[01:26:01]** Where we have these powerful human-like learners
**[01:26:06]** that are also like, and by the way,
**[01:26:08]** maybe there's another thing we haven't discussed
**[01:26:10]** on the spec of the super intelligent AI
**[01:26:14]** that I think is worth considering
**[01:26:17]** is that you make it narrow,
**[01:26:19]** can be useful and narrow at the same time.
**[01:26:21]** So you can have lots of narrow super intelligent AIs,
**[01:26:24]** but suppose you have many of them
**[01:26:28]** and you have some company
**[01:26:30]** that's producing a lot of profits from it.
**[01:26:34]** And then you have another company that comes in
**[01:26:37]** and starts to compete.
**[01:26:38]** And the way the competition is going to work
**[01:26:40]** is through specialization.
**[01:26:42]** I think what's gonna happen is that
**[01:26:45]** the way competition, like competition loves specialization
**[01:26:51]** and you see it in the market,
**[01:26:52]** you see it in evolution as well.
**[01:26:54]** So you're gonna have lots of different niches
**[01:26:55]** and you're gonna have lots of different companies
**[01:26:57]** who are occupying different niches
**[01:26:59]** in this kind of world.
**[01:27:03]** But you might say, yeah, like one AI company
**[01:27:05]** is really quite a bit better
**[01:27:07]** at some area of really complicated economic activity
**[01:27:11]** and a different company is better at another area.
**[01:27:13]** And the third company is really good at litigation.
**[01:27:15]** And that's the way you wanna go there.
**[01:27:16]** Is this contradicted by what human-like learning implies?
**[01:27:18]** Is that like it can learn?
**[01:27:19]** It can, but you have accumulated learning.
**[01:27:23]** You have a big investment.
**[01:27:25]** You spent a lot of compute
**[01:27:26]** to become really, really, really good,
**[01:27:29]** really phenomenal at this thing.
**[01:27:30]** And someone else spent a huge amount of compute
**[01:27:33]** and a huge amount of experience
**[01:27:34]** to get really, really good at some other thing.
**[01:27:36]** You apply a lot of human learning to get there,
**[01:27:38]** but now you are at this high point
**[01:27:42]** where someone else would say, look,
**[01:27:43]** I don't wanna start learning what you've learned.
**[01:27:45]** I guess that would require many different companies
**[01:27:47]** to begin at the human-like continual learning agent
**[01:27:51]** at the same time,
**[01:27:52]** so that they can start their different research
**[01:27:55]** in different branches.
**[01:27:58]** But if one company gets that agent first
**[01:28:02]** or gets that learner first,
**[01:28:05]** it does then seem like, well,
**[01:28:08]** like if you just think about every single job
**[01:28:10]** in the economy,
**[01:28:12]** you just have instance learning each one
**[01:28:16]** seems tractable for a company.
**[01:28:17]** Yeah, that's a valid argument.
**[01:28:20]** My strong intuition is that it's not how it's gonna go.
**[01:28:24]** My strong intuition is that, yeah,
**[01:28:25]** like the argument says it will go this way.
**[01:28:28]** But my strong intuition is that it will not go this way,
**[01:28:31]** that this is the, you know, in theory,
**[01:28:34]** there is no difference between theory in practice
**[01:28:36]** and practice theories,
**[01:28:37]** and I think that's gonna be one of those.
**[01:28:39]** A lot of people's models of recursive self-improvement
**[01:28:42]** literally explicitly state,
**[01:28:43]** we will have a million Ilias in a server
**[01:28:47]** that are coming in with different ideas,
**[01:28:48]** and this will lead to a super intelligence
**[01:28:50]** emerging very fast.
**[01:28:51]** Do you have some intuition about how parallelizable
**[01:28:54]** the thing you are doing is?
**[01:28:55]** How, what are the gains from making copies of Ilia?
**[01:29:00]** I don't know.
**[01:29:02]** I think,
**[01:29:05]** I think there'll definitely be diminishing returns
**[01:29:07]** because you want people who think differently
**[01:29:10]** rather than the same.
**[01:29:11]** I think that if they were literal copies of me,
**[01:29:13]** I'm not sure how much more incremental value you'd get.
**[01:29:17]** I think that,
**[01:29:20]** but people who think differently,
**[01:29:22]** that's what you want.
**[01:29:23]** Why is it that it's been,
**[01:29:24]** if you look at different models,
**[01:29:26]** even released by totally different companies,
**[01:29:28]** trained on potentially non-overlapping datasets,
**[01:29:32]** it's actually crazy how similar LLMs are to each other.
**[01:29:35]** Maybe the datasets are not as non-overlapping as it seems.
**[01:29:39]** But there's some sense that it's like,
**[01:29:42]** even if an individual human might be less productive
**[01:29:44]** than the future AI,
**[01:29:45]** maybe there's something to the fact that human teams
**[01:29:46]** have more diversity than teams of AIs might have,
**[01:29:49]** but how do we elicit meaningful diversity among AIs?
**[01:29:53]** I think just raising the temperature
**[01:29:55]** just results in gibberish.
**[01:29:56]** I think you want something more like,
**[01:29:58]** different scientists have a different pressure.
**[01:30:00]** How do you get that kind of diversity among AI agents?
**[01:30:04]** So the reason there has been no diversity, I believe, is because of pre-training.
**[01:30:10]** All the pre-trained models are the same, pretty much, because they're pre-trained on the same
**[01:30:15]** data.
**[01:30:16]** Now, RL and post-training is where some differentiation starts to emerge because different people
**[01:30:22]** come up with different RL training.
**[01:30:25]** And then I've heard you hint in the past about self-play as a way to either get data or match
**[01:30:32]** agents to other agents of equivalent intelligence to kick off learning.
**[01:30:38]** How should we think about why there's no public proposals of this kind of thinking working
**[01:30:45]** with LLMs?
**[01:30:46]** I would say there are two things to say.
**[01:30:49]** I would say that the reason why I thought self-play was interesting is because it offered
**[01:30:55]** a way to create models using compute only without data.
**[01:31:00]** And if you think that data is the ultimate bottleneck, then using compute only is very
**[01:31:05]** interesting.
**[01:31:06]** So that's what makes it interesting.
**[01:31:08]** Now the thing is that self-play, at least the way it was done in the past, when you
**[01:31:18]** have agents which somehow compete with each other, it's only good for developing a certain
**[01:31:22]** set of skills.
**[01:31:23]** It is too narrow.
**[01:31:25]** It's only good for negotiation, conflict, certain social skills, strategizing, that
**[01:31:34]** kind of stuff.
**[01:31:35]** And so if you care about those skills, then self-play will be useful.
**[01:31:38]** Now, actually, I think that self-play did find a home, but just in a different form.
**[01:31:48]** So things like debate, prove a verifier, you have some kind of an LLM as a judge, which
**[01:31:55]** is also incentivized to find mistakes in your work.
**[01:31:58]** You could say this is not exactly self-play, but this is a related adversarial setup that
**[01:32:02]** people are doing, I believe.
**[01:32:04]** And really self-play is a special case of more general competition between agents.
**[01:32:13]** The natural response to competition is to try to be different.
**[01:32:17]** And so if you were to put multiple agents and you tell them, you all need to work on
**[01:32:21]** some problem and you're an agent and you're inspecting what everyone else is working,
**[01:32:26]** you're going to say, well, if they're already taking this approach, it's not clear I should
**[01:32:31]** pursue it.
**[01:32:32]** I should pursue something differentiated.
**[01:32:33]** And so I think that something like this could also create an incentive for a diversity of
**[01:32:38]** approaches.
**[01:32:40]** Final question.
**[01:32:43]** What is research taste?
**[01:32:44]** You're obviously the person in the world who is considered to have the best taste in
**[01:32:53]** doing research in AI.
**[01:32:54]** You were the co-author on many of the biggest, the biggest things that have happened in the
**[01:33:01]** history of deep learning from AlexNet to GPT-3 to so on.
**[01:33:05]** What is it that, how do you characterize how you come up with these ideas?
**[01:33:11]** So I can comment on this for myself.
**[01:33:14]** I think different people do it differently.
**[01:33:18]** But one thing that guides me personally is an aesthetic of how AI should be by thinking
**[01:33:29]** about how people are, but thinking correctly.
**[01:33:33]** Like it's very easy to think about how people are incorrectly, but what does it mean to
**[01:33:37]** think about people correctly?
**[01:33:39]** I'll give you some examples.
**[01:33:41]** The idea of the artificial neuron is directly inspired by the brain.
**[01:33:47]** And it's a great idea.
**[01:33:48]** Why?
**[01:33:49]** Because you say, sure, the brain has all these different organs, it has the folds, but the
**[01:33:53]** folds probably don't matter.
**[01:33:54]** Why do we think that the neurons matter?
**[01:33:56]** Because there's many of them.
**[01:33:57]** It kind of feels right.
**[01:33:59]** So you want the neuron.
**[01:34:01]** You want some kind of local learning rule that will change the connections.
**[01:34:04]** You want some local learning rule that will change the connections between the neurons.
**[01:34:10]** It feels plausible that the brain does it.
**[01:34:12]** The idea of the distributed representation.
**[01:34:15]** The idea that the brain, the brain responds to experience, our neural net should learn
**[01:34:20]** from experience, not response.
**[01:34:21]** The brain learns from experience.
**[01:34:24]** The neural net should learn from experience.
**[01:34:26]** And you kind of ask yourself, is something fundamental or not fundamental?
**[01:34:30]** How do you think it should be?
**[01:34:32]** And I think that's been guiding me a fair bit, kind of thinking from multiple angles
**[01:34:37]** and looking for almost beauty, beauty, simplicity, ugliness, there's no room for ugliness.
**[01:34:43]** It's just beauty, simplicity, elegance, correct inspiration from the brain.
**[01:34:48]** And all of those things need to be present at the same time.
**[01:34:51]** And the more they are present, the more confident you can be in a top-down belief.
**[01:34:56]** And then the top-down belief is the thing that sustains you when the experiments contradict
**[01:35:00]** you.
**[01:35:02]** Because if you just trust the data all the time, well, sometimes you can be doing a correct
**[01:35:05]** thing, but there's a bug, but you don't know that there is a bug.
**[01:35:08]** How can you tell that there is a bug?
**[01:35:11]** How do you know if you should keep debugging or you conclude it's the wrong direction?
**[01:35:14]** Well, it's the top-down.
**[01:35:15]** Well, how should you can say the things have to be this way?
**[01:35:19]** Something like this has to work, therefore, we got to keep going.
**[01:35:22]** That's the top-down.
**[01:35:23]** And it's based on this like multifaceted beauty and inspiration by the brain.
**[01:35:28]** All right, we'll leave it there.
**[01:35:31]** Thank you so much.
**[01:35:32]** Thank you so much.
**[01:35:33]** All right.
**[01:35:34]** Appreciate it.
**[01:35:35]** That was great.
**[01:35:36]** Yeah.
**[01:35:37]** I enjoyed it.
**[01:35:38]** Yes, me too.
**[01:35:39]** Hey, everybody.
**[01:35:40]** I hope you enjoyed that episode.
**[01:35:41]** If you did, the most helpful thing you can do is just share it with other people who
**[01:35:45]** you think might enjoy it.
**[01:35:46]** It's also helpful if you leave a rating or a comment on whatever platform you're listening
**[01:35:51]** on.
**[01:35:52]** If you're interested in sponsoring the podcast, you can reach out at dwarkesh.com slash advertise.
**[01:35:59]** Otherwise, I'll see you in the next one.
