---
layout: default
type: transcript
series: dwarkesh
episode: 9
guest: ""
title: "Andrej Karpathy — “We’re summoning ghosts, not building animals”"
source_url: "https://www.youtube.com/watch?v=lXUZvyajciY"
analysis_url: /transcripts/dwarkesh/9_andrej_karpathy_we_re_summoning_ghosts_not_building_animals.analysis/
permalink: /transcripts/dwarkesh/9_andrej_karpathy_we_re_summoning_ghosts_not_building_animals/
---

# Transcript: EP9 - Andrej Karpathy — “We’re summoning ghosts, not building animals”

Source: https://www.youtube.com/watch?v=lXUZvyajciY

---

**[00:00]** Reinforcement learning is terrible.
**[00:02]** It just so happens that everything that we had before
**[00:04]** is much worse.
**[00:06]** I'm actually optimistic.
**[00:07]** I think this will work.
**[00:08]** I think it's tractable.
**[00:09]** I'm only sounding pessimistic because when
**[00:11]** I go on my Twitter timeline, I see all this stuff that
**[00:13]** makes no sense to me.
**[00:14]** A lot of it is, I think, honestly, just fundraising.
**[00:17]** We're not actually building animals.
**[00:18]** We're building ghosts.
**[00:19]** These ethereal spirit entities, because they're fully digital,
**[00:23]** and they're mimicking humans.
**[00:24]** And it's a different kind of intelligence.
**[00:26]** It's business as usual, because we're in an intelligence
**[00:29]** explosion already, and have been for decades.
**[00:31]** Everything is gradually being automated.
**[00:33]** Has been for hundreds of years.
**[00:34]** Don't write blog posts.
**[00:35]** Don't do slides.
**[00:36]** Don't do any of that.
**[00:37]** Like, build the code, arrange it, get it to work.
**[00:39]** It's the only way to go.
**[00:40]** Otherwise, you're missing knowledge.
**[00:41]** If you have a perfect AI tutor, maybe you
**[00:43]** can get extremely far.
**[00:44]** The geniuses of today are barely scratching the surface
**[00:46]** of what a human mind can do, I think.
**[00:48]** Today, I'm speaking with Andrej Karpathy.
**[00:51]** Andrej, why do you say that this will be the decade of agents
**[00:53]** and not the year of agents?
**[00:55]** Well, first of all, thank you for having me here.
**[00:58]** Excited to be here.
**[00:59]** So the quote that you've just mentioned,
**[01:01]** it's the decade of agents.
**[01:02]** That's actually a reaction to an existing, pre-existing quote,
**[01:05]** I should say, where I think a lot of some of the labs,
**[01:07]** I'm not actually sure who said this,
**[01:08]** but they were alluding to this being the year of agents
**[01:11]** with respect to LLMs and how they were going to evolve.
**[01:14]** And I think I was triggered by that
**[01:17]** because I feel like there's some over-predictions
**[01:19]** going on in the industry.
**[01:20]** And in my mind, this is really a lot more accurately described
**[01:24]** as the decade of agents.
**[01:25]** And we have some very early agents
**[01:26]** that are actually extremely impressive
**[01:28]** and that I use daily, Cloud and Codex and so on.
**[01:31]** But I still feel like there's so much work to be done.
**[01:34]** And so I think my reaction is like,
**[01:36]** we'll be working with these things for a decade.
**[01:38]** They're going to get better and it's going to be wonderful.
**[01:41]** But I think I was just reacting to the timelines,
**[01:43]** I suppose, of the implication.
**[01:46]** And what do you think will take a decade to accomplish?
**[01:48]** What are the bottlenecks?
**[01:50]** Well, actually make it work.
**[01:52]** So in my mind, I mean,
**[01:53]** when you're talking about an agent, I guess,
**[01:55]** or what the labs have in mind
**[01:56]** and what maybe I have in mind as well,
**[01:57]** is you should think of it almost like an employee
**[01:59]** or like an intern that you would hire to work with you.
**[02:01]** So for example, you work with some employees here.
**[02:04]** When would you prefer to have an agent
**[02:06]** like Cloud or Codex do that work?
**[02:08]** Currently, of course, they can't.
**[02:09]** What would it take for them to be able to do that?
**[02:11]** Why don't you do it today?
**[02:12]** And the reason you don't do it today
**[02:13]** is because they just don't work.
**[02:14]** So they don't have enough intelligence,
**[02:17]** they're not multimodal enough,
**[02:18]** they can't do computer use and all this kind of stuff.
**[02:20]** And they don't do a lot of the things
**[02:21]** that you've alluded to earlier.
**[02:23]** They don't have continual learning.
**[02:24]** You can't just tell them something and they'll remember it.
**[02:26]** And they're just cognitively lacking
**[02:28]** and it's just not working.
**[02:29]** And I just think that it will take about a decade
**[02:31]** to work through all of those issues.
**[02:32]** Interesting.
**[02:33]** So as a professional podcaster
**[02:35]** and a viewer of AI From Afar,
**[02:40]** it's easy to identify for me, like, oh, here's what's lacking.
**[02:43]** Continual learning is lacking or multimodality is lacking.
**[02:46]** But I don't really have a good way
**[02:50]** of trying to put a timeline on it.
**[02:52]** Like if somebody is like,
**[02:53]** how long will continual learning take?
**[02:55]** There's no like prior I have about like,
**[02:57]** this is a project that should take five years,
**[02:59]** 10 years, 50 years.
**[03:00]** Why a decade?
**[03:01]** Why not one year?
**[03:02]** Why not 50 years?
**[03:04]** Yeah, I guess this is where you get into like a bit of,
**[03:06]** I guess, my own intuition a little bit.
**[03:08]** And also just kind of doing a bit of an extrapolation
**[03:12]** with respect to my own experience in the field, right?
**[03:14]** So I guess I've been in AI for almost two decades.
**[03:17]** I mean, it's gonna be maybe 15 years or so, not that long.
**[03:19]** You had Richard Sutton here who was around,
**[03:21]** of course, for much longer.
**[03:22]** But I do have about 15 years of experience
**[03:24]** of people making predictions,
**[03:25]** of seeing how they actually turned out.
**[03:27]** And also I was in the industry for a while
**[03:29]** and I was in research
**[03:30]** and I've worked in the industry for a while.
**[03:31]** So I guess I kind of have just a general intuition
**[03:34]** that I have left from that.
**[03:36]** And I feel like the problems are tractable.
**[03:40]** They're surmountable, but they're still difficult.
**[03:43]** And if I just average it out,
**[03:44]** it just kind of feels like a ticket, I guess, to me.
**[03:46]** This is actually quite interesting.
**[03:47]** I wanna like hear not only the history,
**[03:50]** but what people in the room felt was about to happen
**[03:54]** at various different breakthrough moments.
**[03:57]** What were the ways in which their feelings
**[04:00]** were either overly pessimistic or overly optimistic?
**[04:03]** Should we just go through each of them one by one?
**[04:05]** Yeah, I mean, that's a giant question
**[04:06]** because of course you're talking about 15 years
**[04:07]** of stuff that happened.
**[04:08]** I mean, AI is actually like so wonderful
**[04:10]** because there have been a number of,
**[04:11]** I would say, seismic shifts
**[04:13]** that were like the entire field
**[04:14]** has sort of like suddenly looked a different way, right?
**[04:16]** And I guess I've maybe lived through two or three of those.
**[04:19]** And I still think there will continue to be some
**[04:21]** because they come with some kind of like
**[04:22]** almost surprising irregularity.
**[04:24]** Well, when my career began, of course,
**[04:26]** like when I started to work on deep learning,
**[04:28]** when I became interested in deep learning,
**[04:29]** this was just kind of like by chance
**[04:31]** of being right next to Geoff Hinton
**[04:32]** at University of Toronto.
**[04:33]** And Geoff Hinton, of course,
**[04:34]** is kind of like the godfather figure of AI.
**[04:36]** And he was training all these neural networks
**[04:38]** and I thought it was incredible and interesting,
**[04:40]** but this was not like the main thing
**[04:41]** that everyone in AI was doing by far.
**[04:43]** This was a niche little subject on the side.
**[04:46]** That's kind of maybe like the first
**[04:47]** like dramatic sort of seismic shift
**[04:49]** that came with the AlexNet and so on.
**[04:51]** I would say like AlexNet sort of reoriented everyone
**[04:53]** and everyone started to train neural networks,
**[04:55]** but it was still like very like per task,
**[04:58]** per specific task.
**[04:59]** So maybe I have an image classifier
**[05:00]** or I have a neural machine translator
**[05:03]** or something like that.
**[05:04]** And people became very slowly actually interested
**[05:06]** in basically kind of agents, I would say.
**[05:09]** And people started to think,
**[05:10]** okay, well maybe we have a check mark
**[05:11]** next to the visual cortex or something like that.
**[05:13]** But what about the other parts of the brain?
**[05:14]** And how can we get an actual like full agent
**[05:16]** or a full entity that can actually interact in the world?
**[05:19]** And I would say the Atari sort of
**[05:21]** deep reinforcement learning shift in 2013 or so
**[05:24]** was part of that early effort of agents in my mind,
**[05:27]** because it was an attempt to try to get agents
**[05:29]** that not just perceive the world,
**[05:30]** but also take actions and interact
**[05:32]** and get rewards from environments.
**[05:33]** And at the time this was Atari games, right?
**[05:36]** And I kind of feel like that was a misstep actually.
**[05:39]** And it was a misstep that actually even the early open AI
**[05:42]** that I was a part of, of course, kind of adopted
**[05:44]** because at that time the zeitgeist was
**[05:46]** reinforcement learning environments,
**[05:48]** games, game playing, beat games,
**[05:50]** get lots of different types of games
**[05:51]** and open AI was doing a lot of that.
**[05:53]** So that was maybe like another like prominent part of,
**[05:57]** I would say AI where maybe for two or three or four years,
**[06:00]** everyone was doing reinforcement learning on games.
**[06:03]** And basically that was a little bit of a misstep.
**[06:06]** And what I was trying to do at open AI actually is like,
**[06:08]** I was always a little bit suspicious of games
**[06:10]** as being like this thing that would actually lead to AGI
**[06:12]** because in my mind you want something like an accountant
**[06:14]** or like something that's actually interacting
**[06:16]** with the real world.
**[06:17]** And I just didn't see how games kind of like add up to it.
**[06:20]** And so my project at open AI, for example,
**[06:22]** was within the scope of the universe project
**[06:25]** on an agent that was using keyboard and mouse
**[06:28]** to operate web pages.
**[06:30]** And I really wanted to have something that like interacts
**[06:31]** with the actual digital world that can do knowledge work.
**[06:35]** And it just so turns out that this was extremely early,
**[06:38]** way too early,
**[06:38]** so early that we shouldn't have been working on that.
**[06:42]** Because if you're just stumbling your way around
**[06:44]** and keyboard mashing and mouse clicking
**[06:46]** and trying to get rewards in these environments,
**[06:49]** your reward is too sparse and you just won't learn
**[06:51]** and you're going to burn a forest computing
**[06:54]** and you're never actually going to get something
**[06:55]** off the ground.
**[06:56]** And so what you're missing is this power of representation
**[06:59]** in the neural network.
**[07:00]** And so for example,
**[07:01]** today people are training those computer using agents,
**[07:03]** but they're doing it on top of a large language model.
**[07:05]** And so you actually have to get the language model first.
**[07:07]** You have to get the representations first
**[07:08]** and you have to do that by all the pre-training
**[07:10]** and all the LLM stuff.
**[07:11]** So I kind of feel like maybe loosely speaking,
**[07:14]** it was like people keep maybe trying
**[07:16]** to get the full thing too early a few times
**[07:19]** where people like really try to go after agents too early,
**[07:22]** I would say, and that was Atari and Universe
**[07:24]** and even my own experience.
**[07:26]** And you actually have to do some things first
**[07:27]** before you sort of get to those agents.
**[07:30]** And maybe now the agents are a lot more competent,
**[07:31]** but maybe we're still missing sort of some parts
**[07:34]** of that stack.
**[07:36]** But I would say maybe those are like the three
**[07:37]** like major buckets of what people were doing,
**[07:40]** training neural nets per tasks,
**[07:42]** trying to the first round of agents,
**[07:44]** and then maybe the LLMs and actually seeking
**[07:46]** the representation power of the neural networks
**[07:48]** before you tack on everything else on top.
**[07:51]** Interesting.
**[07:51]** Yeah, I guess if I were to steel man
**[07:53]** the sort of a sudden perspective would be that
**[07:55]** humans actually can just take on everything at once,
**[07:57]** right?
**[07:58]** Even animals can take on everything at once, right?
**[08:00]** Animals are maybe a better example
**[08:01]** because they don't even have the scaffold of language.
**[08:03]** They just get thrown out into the world
**[08:05]** and they just have to make sense of everything
**[08:07]** without any labels.
**[08:09]** Right.
**[08:10]** And the vision for AGI then should just be something
**[08:12]** which like just looks at sensory data,
**[08:14]** looks at the computer screen,
**[08:15]** and it just like figures out what's going on from scratch.
**[08:18]** I mean, if a human was put in a similar situation
**[08:20]** that'd be trained from scratch.
**[08:21]** But I mean, this was like a human growing up
**[08:22]** or animal growing up.
**[08:23]** So why shouldn't that be the vision for AI
**[08:25]** rather than like this thing where we're doing
**[08:27]** millions of years of training?
**[08:29]** I think that's a really good question.
**[08:30]** And I think, I mean, so Sutton was on your podcast
**[08:34]** and I saw the podcast and I had a write up
**[08:36]** about that podcast almost that gets
**[08:37]** into a little bit of how I see things.
**[08:40]** And I kind of feel like I'm very careful
**[08:42]** to make analogies to animals
**[08:44]** because they came about
**[08:46]** by a very different optimization process.
**[08:48]** Animals are evolved and they actually come
**[08:49]** with a huge amount of hardware that's built in.
**[08:52]** And when, for example, my example in the post was the zebra,
**[08:55]** a zebra gets born and a few minutes later
**[08:57]** it's running around and following its mother.
**[08:59]** That's an extremely complicated thing to do.
**[09:02]** That's not reinforcement learning.
**[09:03]** That's something that's baked in.
**[09:04]** And evolution obviously has some way of encoding
**[09:07]** the weights of our neural nets in ATCGs.
**[09:09]** And I have no idea how that works, but it apparently works.
**[09:12]** So I kind of feel like brains just came
**[09:15]** from a very different process.
**[09:17]** And I'm very hesitant to take inspiration from it
**[09:20]** because we're not actually running that process.
**[09:22]** So in my post, I kind of said,
**[09:24]** we're not actually building animals.
**[09:25]** We're building ghosts or spirits
**[09:27]** or whatever people want to call it.
**[09:29]** Because we're not doing training by evolution.
**[09:34]** We're doing training by basically imitation of humans
**[09:37]** and the data that they've put on the internet.
**[09:39]** And so you end up with these like sort of
**[09:40]** ethereal spirit entities because they're fully digital
**[09:43]** and they're kind of like mimicking humans.
**[09:45]** And it's a different kind of intelligence.
**[09:46]** Like if you imagine a space of intelligences,
**[09:48]** we're starting off at a different point almost.
**[09:50]** We're not really building animals,
**[09:52]** but I think it's also possible to make them
**[09:53]** a bit more animal-like over time.
**[09:55]** And I think we should be doing that.
**[09:56]** And so I kind of feel like, sorry,
**[09:57]** just I guess one more point is,
**[09:59]** I do feel like Sutton basically has a very,
**[10:01]** like his framework is like we want to build animals.
**[10:04]** And I actually think that would be wonderful.
**[10:06]** If we can get that to work, that would be amazing.
**[10:07]** If there was a single like algorithm
**[10:10]** that you can just run on the internet
**[10:12]** and it learns everything, that would be incredible.
**[10:14]** I almost suspect that I'm not actually sure that it exists.
**[10:18]** And that's certainly actually not what animals do
**[10:21]** because animals have this outer loop of evolution.
**[10:24]** And a lot of what looks like learning
**[10:25]** is actually a lot more maturation of the brain.
**[10:28]** And I think there's actually very little
**[10:30]** reinforcement learning for animals.
**[10:32]** And I think a lot of the reinforcement learning
**[10:33]** is actually like more like motor tasks.
**[10:35]** It's not intelligence tasks.
**[10:37]** So I actually kind of think,
**[10:38]** humans don't actually like really use RL,
**[10:40]** roughly speaking is what I would say.
**[10:41]** Can you repeat the last sentence?
**[10:42]** A lot of that intelligence is not motor tasks.
**[10:43]** That's what, sorry?
**[10:44]** A lot of the reinforcement learning in my perspective
**[10:46]** would be things that are a lot more like motor-like,
**[10:47]** like simple kind of like tasks,
**[10:50]** throwing a hoop or something like that.
**[10:53]** But I don't think that humans use reinforcement learning
**[10:55]** for a lot of intelligence tasks,
**[10:57]** like problem solving and so on.
**[10:58]** Interesting.
**[11:00]** It doesn't mean we shouldn't do that for research,
**[11:02]** but I just feel like that's what animals do or don't.
**[11:06]** I'm gonna take a second to digest that
**[11:07]** because there's a lot of different ideas.
**[11:09]** Maybe one clarifying question I can ask
**[11:12]** to understand the perspective.
**[11:14]** So I think you suggest that, look,
**[11:16]** evolution is doing the kind of thing that pre-training does
**[11:18]** in the sense of building something
**[11:22]** which can then understand the world.
**[11:23]** The difference, I guess, is that evolution
**[11:26]** has to be titrated in the case of humans
**[11:29]** through three gigabytes of DNA.
**[11:31]** And so that's very unlike the weights of a model.
**[11:37]** I mean, literally the weights of the model are our brain,
**[11:39]** which obviously is not encoded in the sperm and the egg,
**[11:41]** or does not exist in the sperm and the egg,
**[11:44]** so it has to be grown.
**[11:46]** And also the information for every single synapse
**[11:49]** in the brain simply cannot exist in the three gigabytes
**[11:51]** that exist in the DNA.
**[11:52]** Evolution seems closer to finding the algorithm,
**[11:55]** which then does the lifetime learning.
**[11:58]** Now, maybe the lifetime learning
**[12:00]** is not analogous to RL, to your point.
**[12:03]** Is that compatible with the thing you were saying,
**[12:04]** or would you disagree with that?
**[12:05]** I think so.
**[12:06]** I would agree with you that there's some
**[12:07]** miraculous compression going on
**[12:08]** because obviously the weights of the neural net
**[12:10]** are not stored in the TCGs.
**[12:11]** There's some kind of a dramatic compression
**[12:13]** and there's some kind of learning algorithms
**[12:15]** encoded that take over and do some of the learning online.
**[12:18]** So I definitely agree with you on that.
**[12:20]** Basically, I would say I'm a lot more
**[12:22]** kind of like practically minded.
**[12:23]** I don't come at it from the perspective
**[12:24]** of like let's build animals.
**[12:26]** I come from a perspective of like,
**[12:27]** let's build useful things.
**[12:28]** So I have a hard hat on and I'm just observing that,
**[12:31]** look, we're not going to do evolution
**[12:32]** because I don't know how to do that.
**[12:34]** But it does turn out we can build these ghost,
**[12:36]** spirit-like entities by imitating internet documents.
**[12:39]** This works.
**[12:40]** And it's actually kind of like,
**[12:42]** it's a way to bring you up to something
**[12:43]** that has a lot of sort of built-in knowledge
**[12:46]** and intelligence in some way,
**[12:48]** similar to maybe what evolution has done.
**[12:50]** So that's why I kind of call pre-training
**[12:51]** this kind of like crappy evolution.
**[12:53]** It's like the practically possible version
**[12:57]** with our technology and what we have available to us
**[12:58]** to get to a starting point where we can actually
**[13:01]** do things like reinforcement learning and so on.
**[13:03]** Just to steelman the other perspective,
**[13:05]** because after doing this in an interview
**[13:06]** and thinking about it a bit,
**[13:07]** here's an important point here.
**[13:09]** Evolution does not give us the knowledge really, right?
**[13:12]** It gives us the algorithm to find the knowledge.
**[13:14]** And that seems different from pre-training.
**[13:15]** So if perhaps the perspective is that pre-training
**[13:19]** helps build the kind of entity which can learn better,
**[13:21]** it teaches meta-learning,
**[13:22]** and therefore it is similar to like finding an algorithm.
**[13:26]** But if it's like evolution gives us knowledge
**[13:28]** and pre-training gives us knowledge,
**[13:29]** that analogy seems to break down.
**[13:31]** So it's subtle, and I think you're right to push back on it.
**[13:33]** But basically, the thing that pre-training is doing,
**[13:36]** so you're basically getting the next token predictor
**[13:38]** over the internet,
**[13:39]** and you're training that into a neural net.
**[13:41]** It's doing two things actually
**[13:42]** that are kind of like unrelated.
**[13:43]** Number one, it's picking up all this knowledge,
**[13:45]** as I call it.
**[13:46]** Number two, it's actually becoming intelligent.
**[13:49]** By observing the algorithmic patterns in the internet,
**[13:51]** it actually kind of like boots up
**[13:53]** all these like little circuits and algorithms
**[13:54]** inside the neural net to do things like in-context learning
**[13:56]** and all this kind of stuff.
**[13:57]** And actually, you don't actually need or want the knowledge.
**[14:00]** I actually think that's probably
**[14:02]** actually holding back the neural networks overall,
**[14:03]** because it's actually like getting them
**[14:04]** to rely on the knowledge a little too much sometimes.
**[14:07]** For example, I kind of feel like agents,
**[14:09]** one thing they're not very good at
**[14:10]** is going off the data manifold
**[14:11]** of what exists on the internet.
**[14:13]** If they had less knowledge or less memory,
**[14:16]** actually maybe they would be better.
**[14:17]** And so what I think we have to do kind of going forward,
**[14:19]** and this will be part of the research paradigms,
**[14:21]** is actually I think we need to start,
**[14:23]** we need to figure out ways to remove some of the knowledge
**[14:25]** and to keep what I call this cognitive core.
**[14:28]** It's this like intelligent entity
**[14:30]** that is kind of stripped from knowledge,
**[14:32]** but contains the algorithms and contains the magic,
**[14:34]** you know, of intelligence and problem solving
**[14:36]** and the strategies of it and all this kind of stuff.
**[14:39]** There's so much interesting stuff there.
**[14:40]** Okay, so let's start with in-context learning.
**[14:43]** This is an obvious point,
**[14:44]** but I think it's worth just like saying it explicitly
**[14:47]** and meditating on it.
**[14:48]** The situation in which these models
**[14:50]** seem the most intelligent,
**[14:51]** in which they are like,
**[14:52]** I talk to them and I'm like,
**[14:53]** wow, there's really something on the other end
**[14:56]** that's responding to me thinking about things.
**[14:58]** If it like makes a mistake, it's like,
**[14:59]** oh wait, that's actually the wrong way to think about it.
**[15:00]** I'm backing up.
**[15:01]** All that is happening in context.
**[15:03]** That's where I feel like the real intelligence
**[15:05]** you can like visibly see.
**[15:06]** And that in-context learning process
**[15:09]** is developed by gradient descent on pre-training, right?
**[15:13]** Like it spontaneously meta learns in-context learning.
**[15:16]** But the in-context learning itself is not gradient descent
**[15:20]** in the same way that our lifetime intelligence as humans
**[15:23]** to be able to do things is conditioned by evolution.
**[15:26]** But our actual learning during our lifetime
**[15:28]** is like happening through some other process.
**[15:30]** I actually don't fully agree with that,
**[15:32]** but you should continue with that.
**[15:33]** Oh, okay.
**[15:33]** Actually, then I'm very curious to understand
**[15:35]** how that analogy breaks down.
**[15:36]** I think I'm hesitant to say that in-context learning
**[15:39]** is not doing gradient descent
**[15:40]** because I mean, it's not doing explicit gradient descent,
**[15:43]** but I still think that,
**[15:44]** so in-context learning, basically,
**[15:46]** it's pattern completion within a token window, right?
**[15:49]** And it just turns out
**[15:50]** that there's a huge amount of patterns on the internet.
**[15:51]** And so you're right,
**[15:52]** the model kind of like learns to complete the pattern.
**[15:54]** And that's inside the weights.
**[15:56]** The weights of the neural network
**[15:57]** are trying to discover patterns and complete the pattern.
**[15:59]** And there's some kind of an adaptation
**[16:01]** that happens inside the neural network, right?
**[16:03]** Which is kind of magical and just falls out from internet
**[16:06]** just because there's a lot of patterns.
**[16:07]** I will say that there have been some papers
**[16:10]** that I thought were interesting
**[16:11]** that actually look at the mechanisms
**[16:12]** behind in-context learning.
**[16:13]** And I do think it's possible
**[16:14]** that in-context learning
**[16:15]** actually runs a small gradient descent loop
**[16:17]** internally in the layers of the neural network.
**[16:19]** And so I recall one paper in particular
**[16:21]** where they were doing a linear regression, actually,
**[16:24]** using in-context learning.
**[16:26]** So basically your inputs into the neural network
**[16:27]** are X, Y pairs, X, Y, X, Y, X, Y
**[16:31]** that happened to be on the line.
**[16:33]** And then you do X and you expect the Y.
**[16:35]** And the neural network, when you train it in this way,
**[16:37]** actually does do linear regression.
**[16:40]** And normally when you would run linear regression,
**[16:43]** you have a small gradient descent optimizer
**[16:45]** that basically looks at X, Y, looks at an error,
**[16:47]** calculates the gradient of the weights
**[16:49]** and does the update a few times.
**[16:50]** It just turns out that when they looked at the weights
**[16:52]** of that in-context learning algorithm,
**[16:54]** they actually found some analogies
**[16:56]** to gradient descent mechanics.
**[16:59]** In fact, I think even the paper was stronger
**[17:01]** because they actually hard-coded
**[17:03]** the weights of a neural network
**[17:04]** to do gradient descent through attention
**[17:07]** and all the internals of the neural network.
**[17:10]** So I guess that's just my only pushback
**[17:12]** is that who knows how in-context learning works,
**[17:14]** but I actually think that it's probably doing
**[17:16]** a little bit of some kind of funky gradient descent
**[17:18]** internally and that I think that that's possible.
**[17:21]** So I guess I was only pushing back on,
**[17:23]** you're saying it's not doing in-context learning.
**[17:24]** Who knows what it's doing,
**[17:25]** but it's probably maybe doing something similar to it,
**[17:27]** but we don't know.
**[17:28]** So then it's worth thinking about,
**[17:29]** okay, if both of them are implementing gradient descent,
**[17:32]** if in-context learning and pre-training
**[17:34]** are both implementing something like gradient descent,
**[17:37]** why does it feel like in-context learning
**[17:40]** actually we're getting to this continual learning,
**[17:43]** real intelligence-like thing,
**[17:44]** whereas you don't get the analogous feeling
**[17:46]** just from pre-training?
**[17:47]** At least you could argue that.
**[17:49]** And so if it's the same algorithm, what could be different?
**[17:51]** Well, one way you can think about it is
**[17:53]** how much information does the model store
**[17:56]** per information it receives from training?
**[18:00]** And if you look at pre-training,
**[18:01]** if you look at LLAMA3, for example,
**[18:03]** I think it's trained on 15 trillion tokens,
**[18:06]** and if you look at the 70B model,
**[18:09]** that would be the equivalent of 0.07 bits per token
**[18:13]** in that it sees in pre-training
**[18:15]** in terms of the information in the weights of the model
**[18:17]** compared to the tokens it reads.
**[18:18]** Whereas if you look at the KV cache
**[18:21]** and how it grows per additional token
**[18:22]** in in-context learning, it's like 320 kilobytes.
**[18:26]** So that's a 35 million-fold difference
**[18:28]** in how much information per token
**[18:30]** is assimilated by the model.
**[18:33]** I wonder if that's relevant at all.
**[18:34]** I think I kind of agree.
**[18:36]** I mean, the way I usually put this is that
**[18:38]** anything that happens during the training
**[18:39]** of the neural network,
**[18:40]** the knowledge is only kind of like a hazy recollection
**[18:43]** of what happened in the training time.
**[18:45]** And that's because the compression is dramatic.
**[18:47]** You're taking 15 trillion tokens
**[18:48]** and you're compressing it to just your fine neural network
**[18:50]** of a few billion parameters.
**[18:51]** So obviously it's a massive amount of compression going on.
**[18:54]** So I kind of refer to it as like a hazy recollection
**[18:56]** of the internet documents,
**[18:57]** whereas anything that happens in the context window
**[18:59]** of the neural network,
**[19:00]** you're plugging all the tokens
**[19:01]** and it's building up all this KV cache representation,
**[19:03]** is very directly accessible to the neural net.
**[19:05]** So I compare the KV cache
**[19:07]** and the stuff that happens at test time
**[19:09]** to like more like a working memory.
**[19:11]** Like all the stuff that's in the context window
**[19:14]** is very directly accessible to the neural net.
**[19:15]** So there's always like these almost surprising analogies
**[19:19]** between LLMs and humans.
**[19:21]** And I find them kind of surprising
**[19:22]** because we're not trying to build a human brain,
**[19:23]** of course, just directly.
**[19:25]** We're just finding that this works and we're doing it.
**[19:27]** But I do think that anything that's in the weights,
**[19:30]** it's kind of like a hazy recollection
**[19:31]** of what you read a year ago.
**[19:33]** Anything that you give it as a context at test time
**[19:36]** is directly in the working memory.
**[19:38]** And I think that's a very powerful analogy
**[19:39]** to think through things.
**[19:40]** So when you, for example, go to an LLM
**[19:42]** and you ask it about some book and what happened in it,
**[19:44]** like Nick Lane's book or something like that,
**[19:47]** the LLM will often give you some stuff,
**[19:48]** which is roughly correct.
**[19:49]** But if you give it the full chapter and ask it questions,
**[19:51]** you're gonna get much better results
**[19:53]** because it's now loaded in the working memory of the model.
**[19:56]** So I basically agree with your very long way of saying
**[19:58]** that I kind of agree and that's why.
**[20:00]** Stepping back, what is it the part about human intelligence
**[20:02]** that we like have most failed
**[20:05]** to replicate with these models?
**[20:09]** I almost feel like just a lot of it still.
**[20:14]** So maybe one way to think about it,
**[20:15]** I don't know if this is the best way,
**[20:17]** but I almost kind of feel like, again,
**[20:19]** making these analogies imperfect as they are.
**[20:22]** We've stumbled by with the transformer neural network,
**[20:24]** which is extremely powerful, very general.
**[20:27]** You can train transformers on audio or video or text
**[20:30]** or whatever you want and it just learns patterns
**[20:32]** and they're very powerful and it works really well.
**[20:35]** That to me almost indicates that this is kind of like
**[20:37]** some piece of cortical tissue.
**[20:39]** It's something like that
**[20:39]** because the cortex is famously very plastic as well.
**[20:42]** You can rewire parts of brains
**[20:45]** and there was the slightly gruesome experiments
**[20:48]** with rewiring like visual cortex to the auditory cortex
**[20:50]** and this animal like learn five, et cetera.
**[20:54]** So I think that this is kind of like a cortical tissue.
**[20:56]** I think when we're doing reasoning and planning
**[20:59]** inside the neural networks,
**[21:00]** so basically doing our reasoning traces
**[21:03]** for thinking models,
**[21:04]** that's kind of like the prefrontal cortex.
**[21:07]** And then I think maybe those are like little check marks,
**[21:11]** but I still think there's many brain parts
**[21:13]** and nuclei that are not explored.
**[21:15]** So maybe for example,
**[21:15]** there's a basal ganglia doing a bit of reinforcement learning
**[21:17]** when we fine tune the models on reinforcement learning,
**[21:20]** but you know, whereas like the hippocampus,
**[21:21]** not obvious what that would be.
**[21:23]** Some parts are probably not important.
**[21:24]** Maybe the cerebellum is like not important
**[21:26]** to cognition, it's thought,
**[21:27]** so maybe we can skip some of it.
**[21:29]** But I still think there's, for example, the amygdala,
**[21:30]** all the emotions and instincts.
**[21:33]** And there's probably like a bunch of other nuclei
**[21:35]** in the brain that are very ancient
**[21:36]** that I don't think we've like really replicated.
**[21:38]** I don't actually know that we should be pursuing,
**[21:40]** you know, the building of an analog of human brain.
**[21:43]** I'm again, an engineer mostly at heart,
**[21:45]** but I still feel like maybe another way
**[21:49]** to answer the question is,
**[21:50]** you're not gonna hire this thing as an intern
**[21:52]** and it's missing a lot of,
**[21:52]** it's because it comes with a lot of these cognitive deficits
**[21:55]** that we all intuitively feel when we talk to the models.
**[21:58]** And so it's just like not fully there yet.
**[22:00]** You can look at it as like not all the brain parts
**[22:02]** are checked off yet.
**[22:04]** This is maybe relevant to the question of thinking
**[22:07]** about how fast these issues will be solved.
**[22:09]** So sometimes people will say about continual learning,
**[22:13]** look, actually, you could easily replicate this capability
**[22:17]** just as in-context learning emerged spontaneously
**[22:19]** as a result of pre-training.
**[22:22]** Continual learning over longer horizons
**[22:24]** will emerge spontaneously if the model is incentivized
**[22:28]** to recollect information over longer horizons
**[22:30]** or horizons longer than one session.
**[22:33]** So if there's some like outer loop RL,
**[22:38]** which has many sessions within that outer loop,
**[22:42]** then like this continual learning where it uses like,
**[22:45]** it fine tunes itself or it writes to an external memory
**[22:47]** or something will just sort of like emerge spontaneously.
**[22:49]** Do you think, do you think things are plausible?
**[22:52]** I just, I don't have really a prior over like,
**[22:53]** how plausible is that?
**[22:54]** How likely is that to happen?
**[22:55]** I don't know that I fully resonate with that
**[22:56]** because I feel like these models,
**[22:58]** when you boot them up
**[22:59]** and they have zero tokens in the window,
**[23:00]** they're always like restarting from scratch where they were.
**[23:03]** So I don't actually know in that worldview
**[23:05]** what it looks like because again,
**[23:08]** maybe making some analogies to humans,
**[23:10]** just because I think it's roughly concrete
**[23:12]** and kind of interesting to think through.
**[23:14]** I feel like when I'm awake,
**[23:15]** I'm building up a context window
**[23:16]** of stuff that's happening during the day.
**[23:18]** But I feel like when I go to sleep,
**[23:19]** something magical happens where I don't actually think
**[23:21]** that that context window stays around.
**[23:23]** I think there's some process of distillation
**[23:25]** into weights of my brain.
**[23:27]** And this happens during sleep and all this kind of stuff.
**[23:29]** We don't have an equivalent for all that
**[23:30]** in larger language models.
**[23:33]** And that's to me more adjacent
**[23:34]** to when you talk about continual learning and so on,
**[23:37]** as absent.
**[23:38]** These models don't really have this distillation phase
**[23:41]** of taking what happened, analyzing it,
**[23:44]** obsessively thinking through it,
**[23:47]** basically doing some kind of a synthetic
**[23:48]** data generation process
**[23:49]** and distilling it back into the weights
**[23:50]** and maybe having a specific neural net
**[23:54]** per person.
**[23:55]** Maybe it's a Laura, it's not a full,
**[23:58]** yeah, it's not a full weight neural network.
**[24:00]** That's just some of the small,
**[24:03]** sparse subset of the weights are changed.
**[24:05]** But basically, we do want to create ways
**[24:07]** of creating these individuals that have very long contexts.
**[24:10]** It's not only remaining in the context window
**[24:12]** because the context windows grow very, very long.
**[24:14]** Like maybe we have some very elaborate
**[24:16]** sparse attention over it.
**[24:17]** But I still think that humans obviously
**[24:19]** have some process for distilling
**[24:21]** some of that knowledge into the weights.
**[24:22]** We're missing it.
**[24:24]** And I do also think that humans have some kind
**[24:26]** of a very elaborate sparse attention scheme,
**[24:30]** which I think we're starting to see some early hints of.
**[24:32]** So DeepSeek v3.2 just came out,
**[24:35]** and I saw that they have like a sparse attention
**[24:37]** as an example.
**[24:38]** And this is one way to have very,
**[24:39]** very long context windows.
**[24:40]** So I almost feel like we are redoing
**[24:42]** a lot of the cognitive tricks that evolution
**[24:45]** came up with through a very different process.
**[24:47]** But we're, I think, gonna converge
**[24:48]** on a similar architecture cognitively.
**[24:50]** Interesting.
**[24:50]** In 10 years, do you think it'll still be something
**[24:53]** like a transformer,
**[24:54]** but with a much more modified attention
**[24:55]** and more sparse MLPs and so forth?
**[24:58]** Well, the way I like to think about it is,
**[24:59]** okay, let's, translation invariance in time, right?
**[25:01]** So 10 years ago, where were we?
**[25:04]** 2015, we had convolutional neural networks primarily.
**[25:07]** Residual networks just came out.
**[25:10]** So remarkably similar, I guess,
**[25:11]** but quite a bit different still.
**[25:13]** I mean, transformer was not around.
**[25:15]** You know, all these sort of like more modern tweaks
**[25:19]** on the transformer were not around.
**[25:21]** So maybe some of the things that we can bet on,
**[25:23]** I think, in 10 years,
**[25:24]** by translational sort of equivariance,
**[25:27]** is we're still training giant neural networks
**[25:29]** with forward, backward, pass, and update
**[25:31]** through gradient descent.
**[25:34]** But maybe it looks a little bit different,
**[25:36]** and it's just everything is much bigger.
**[25:38]** Actually, recently, I also went back all the way to 1989,
**[25:41]** which was kind of a fun exercise for me a few years ago,
**[25:45]** because I was reproducing Yann LeCun's
**[25:47]** 1989 convolutional network,
**[25:49]** which was the first neural network I'm aware
**[25:51]** of trained via gradient descent,
**[25:52]** like modern neural network trained gradient descent
**[25:55]** on digital recognition.
**[25:57]** And I was just interested in,
**[25:58]** okay, how can I modernize this?
**[26:00]** How much of this is algorithms?
**[26:01]** How much of this is data?
**[26:01]** How much of this progress is compute and systems?
**[26:04]** And I was able to very quickly,
**[26:05]** like half the learning rate,
**[26:06]** just knowing my time travel by 33 years.
**[26:10]** So if I time travel by algorithms to 33 years,
**[26:13]** I could adjust what Yann LeCun did in 1989,
**[26:15]** and I could basically half the learning, half the error.
**[26:17]** But to get further gains,
**[26:19]** I had to add a lot more data.
**[26:21]** I had like 10 extra training set.
**[26:22]** And then I had to actually add more
**[26:24]** computational optimizations.
**[26:26]** Had to basically train for much longer
**[26:28]** with dropout and other regularization techniques.
**[26:30]** And so it's almost like
**[26:32]** all these things have to improve simultaneously.
**[26:33]** So, you know, we're probably gonna have a lot more data.
**[26:36]** We're probably gonna have a lot better hardware.
**[26:38]** Probably gonna have a lot better kernels and software.
**[26:40]** We're probably gonna have better algorithms.
**[26:41]** And all of those,
**[26:42]** it's almost like no one of them is winning too much.
**[26:45]** All of them are surprisingly equal.
**[26:47]** And this has kind of been the trend for a while.
**[26:50]** So I guess to answer maybe your question,
**[26:52]** I expect differences algorithmically
**[26:55]** to what's happening today.
**[26:56]** But I do also expect that some of the things
**[26:58]** that have stuck around for a very long time
**[27:00]** will probably still be there.
**[27:01]** It's probably still giant neural network
**[27:02]** trained with gradient descent.
**[27:04]** That would be my guess.
**[27:05]** It's surprising that all of those things together
**[27:07]** only halved half of the error.
**[27:12]** Which is like 30 years of progress.
**[27:15]** Maybe half is a lot,
**[27:15]** because if you half the error,
**[27:17]** that actually means that-
**[27:18]** Half is a lot, yeah.
**[27:18]** Yeah, okay.
**[27:19]** But I guess what was shocking to me
**[27:21]** is everything needs to improve across the board.
**[27:24]** Architecture optimizes a loss function
**[27:26]** and also has improved across the board forever.
**[27:28]** So I kind of expect all those changes to be alive and well.
**[27:31]** Yeah, actually, I was about to ask you
**[27:32]** a very similar question about NanoShot.
**[27:34]** Because since you just coded up recently,
**[27:36]** every single sort of step in the process of building
**[27:40]** a chatbot is fresh in your RAM.
**[27:42]** And I'm curious if you had similar thoughts
**[27:45]** about like, oh, there was no one thing
**[27:47]** that was relevant to going from GPT-2 to NanoChat.
**[27:51]** What are sort of like surprising takeaways
**[27:54]** from the experience?
**[27:55]** On building NanoChat?
**[27:56]** Yeah.
**[27:57]** So NanoChat is a kind of a repository I released.
**[27:59]** Was it yesterday or the day before?
**[28:00]** I can't remember.
**[28:01]** Yesterday.
**[28:02]** We can see the sleep deprivation that went into the-
**[28:05]** Yeah, yeah.
**[28:06]** Well, it's just trying to be a,
**[28:09]** it's trying to be the simplest complete repository
**[28:11]** that covers the whole pipeline end-to-end
**[28:13]** of building a chat GPT clone.
**[28:15]** And so, you know, you have all of the steps,
**[28:17]** not just any individual step, which is a bunch of,
**[28:20]** I worked on all the individual steps sort of in the past
**[28:22]** and really small pieces of code
**[28:23]** that could have show you how that's done
**[28:25]** in algorithmic sense in like simple code.
**[28:29]** But this kind of handles all the entire pipeline.
**[28:31]** I think in terms of learning, it's not so much,
**[28:35]** I don't know that I actually found something
**[28:36]** that I learned from it necessarily.
**[28:38]** I kind of already had in my mind as like how you build it.
**[28:40]** And this is just the process of mechanically building it
**[28:45]** and making it clean enough
**[28:47]** so that people can actually learn from it
**[28:49]** and that they find it useful.
**[28:51]** Yeah, what is the best way for somebody to learn from it?
**[28:54]** Is it just like delete all the code
**[28:55]** and try to re-implement from scratch,
**[28:56]** try to add modifications to it?
**[28:58]** Yeah, I think that's a great question.
**[29:00]** I would probably say,
**[29:01]** so basically it's about 8,000 lines of code
**[29:03]** that takes you through the entire pipeline.
**[29:04]** I would probably put it on the right monitor.
**[29:06]** Like if you have two monitors, you put it on the right.
**[29:10]** And you want to build it from scratch,
**[29:11]** you build it from start,
**[29:12]** you're not allowed to copy paste.
**[29:14]** You're allowed to reference,
**[29:15]** you're not allowed to copy paste.
**[29:16]** Maybe that's how I would do it.
**[29:18]** But I also think the repository by itself,
**[29:20]** it is like a pretty large beast.
**[29:21]** I mean, when you write this code,
**[29:24]** you don't go from top to bottom.
**[29:25]** You go from chunks and you grow the chunks.
**[29:28]** And that information is absent.
**[29:30]** Like you wouldn't know where to start.
**[29:31]** And so I think it's not just a final repository
**[29:33]** that's needed, it's like the building of the repository,
**[29:35]** which is a complicated chunk growing process.
**[29:38]** So that part is not there yet.
**[29:40]** I would love to actually like add that
**[29:41]** probably later this week or something,
**[29:43]** in some way, like either it's probably a video
**[29:46]** or something like that.
**[29:47]** But maybe, roughly speaking,
**[29:49]** that's what I would try to do is build the stuff yourself,
**[29:52]** but don't allow yourself copy paste.
**[29:54]** I do think that there's two types of knowledge almost,
**[29:57]** like there's the high level surface knowledge.
**[29:59]** But the thing is that when you're actually
**[30:00]** actually build something from scratch, you're forced to come to terms with what you don't
**[30:03]** actually understand, and you don't know that you don't understand it.
**[30:06]** And it always leads to a deeper understanding.
**[30:09]** And it's like just the only way to build is like, if I can't build it, I don't understand
**[30:13]** it.
**[30:14]** Is that a fine line quote, I believe?
**[30:15]** Or something along those lines?
**[30:16]** I 100% I've always believed this very strongly, because there's all these like micro things
**[30:22]** that are just not properly arranged, and you don't really have the knowledge, you just
**[30:24]** think you have the knowledge.
**[30:25]** So don't write blog posts, don't do slides, don't do any of that, like build a code, arrange
**[30:29]** it, get it to work.
**[30:30]** It's the only way to go.
**[30:31]** Otherwise, you're missing knowledge.
**[30:33]** You tweeted out that coding models were actually a very little help to you in assembling this
**[30:37]** repository.
**[30:38]** And I'm curious why that was.
**[30:41]** Yeah.
**[30:42]** So the repository, I guess I built it over a period of a bit more than a month.
**[30:46]** And I would say there's like three major classes of how people interact with code right now.
**[30:50]** Some people completely reject all of LLMs, and they are just writing by scratch.
**[30:54]** I think this is probably not the right thing to do anymore.
**[30:58]** The intermediate part, which is where I am, is you still write a lot of things from scratch,
**[31:02]** but you use the autocomplete that's basically available now from these models.
**[31:06]** So when you start writing out a piece of it, it will autocomplete for you, and you can
**[31:10]** just tap through, and most of the time it's correct.
**[31:12]** Sometimes it's not, and you edit it.
**[31:14]** But you're still very much the sort of architect of what you're writing.
**[31:18]** And then there's the, you know, by coding, you know, hi, please implement this or that,
**[31:23]** you know, enter, and then let the model do it.
**[31:25]** And that's the agents.
**[31:27]** I do feel like the agents work in very specific settings, and I would use them in specific
**[31:32]** settings.
**[31:33]** But again, these are all tools available to you, and you have to like learn what they're
**[31:36]** good at, and what they're not good at, and when to use them.
**[31:39]** So the agents are actually pretty good, for example, if you're doing boilerplate stuff.
**[31:42]** Boilerplate code, that's like just copy, you know, just copy-paste stuff, they're very
**[31:45]** good at that.
**[31:46]** They're very good at stuff that occurs very often in the internet, because there's lots
**[31:51]** of examples of it in the training sets of these models.
**[31:55]** So there's like features of things that where the models will do very well.
**[31:58]** I would say NanoChat is not an example of this, because it's a fairly unique repository.
**[32:03]** There's not that much code, I think, in the way that I've structured it.
**[32:07]** And it's not boilerplate code.
**[32:08]** It's like actually like intellectually intense code, almost, and everything has to be very
**[32:11]** precisely arranged.
**[32:13]** And the models are always trying to, they kept trying to, I mean, they have so many
**[32:16]** cognitive deficits, right?
**[32:17]** So one example, they keep trying to, they keep misunderstanding the code, because they
**[32:23]** have too much memory from all the typical ways of doing things on the internet that
**[32:26]** I just wasn't adopting.
**[32:28]** So the models, for example, I mean, I don't know if I want to get into the full details,
**[32:32]** but they keep thinking I'm writing normal code, and I'm not.
**[32:37]** Maybe one example.
**[32:38]** Maybe one example.
**[32:39]** So the way to synchronize, so we have eight GPUs that are all doing forward-backwards.
**[32:43]** The way to synchronize gradients between them is to use a distributed data parallel container
**[32:46]** of PyTorch, which automatically does all the, as you're doing the backward, it'll start
**[32:50]** communicating and synchronizing gradients.
**[32:52]** I didn't use DDP, because I didn't want to use it, because it's not necessary.
**[32:56]** So I threw it out.
**[32:57]** And I basically wrote my own synchronization routine that's inside the step of the optimizer.
**[33:02]** And so the models were trying to get me to use the DDP container, and they were very
**[33:06]** concerned about, okay, this gets way too technical.
**[33:09]** But I wasn't using that container, because I don't need it, and I have a custom implementation
**[33:12]** of something like it.
**[33:13]** And they just couldn't internalize it, you had your own.
**[33:16]** Yeah, they couldn't get past that.
**[33:18]** And then they kept trying to mess up the style, like, they're way too over-defensive,
**[33:23]** they make all these try-catch statements, they keep trying to make a production codebase.
**[33:27]** And I have a bunch of assumptions in my code, and it's okay.
**[33:31]** And it's just like, I don't need all this extra stuff in there.
**[33:34]** And so I just kind of feel like they're bloating the codebase, they're bloating the complexity,
**[33:37]** they keep misunderstanding, they're using deprecated APIs a bunch of times.
**[33:41]** So it's total mess.
**[33:43]** And it's just not that useful.
**[33:46]** I can go in, I can clean it up, but it's not that useful.
**[33:48]** I also feel like it's kind of annoying to have to type out what I want in English, because
**[33:52]** it's just too much typing.
**[33:53]** Like, if I just navigate to the part of the code that I want, and I go where I know the
**[33:58]** code has to appear, and I start typing out the first three letters, autocomplete gets
**[34:01]** it and just gives you the code.
**[34:02]** And so I think this is a very high information bandwidth to specify what you want.
**[34:06]** If you point to the code where you want it, and you type out the first few pieces, and
**[34:10]** the model will complete it.
**[34:11]** So I guess what I mean is, I think these models are good in certain parts of the stack.
**[34:17]** I actually use the models a little bit in, there are two examples where I actually use
**[34:22]** the models that I think are illustrative.
**[34:24]** One was when I generate the report, that's actually more boilerplatey.
**[34:27]** So I actually bytecoded partially some of that stuff.
**[34:30]** That was fine.
**[34:31]** Because it's not like mission critical stuff, and it works fine.
**[34:34]** And then the other part is when I was rewriting the tokenizer in Rust, I'm actually not as
**[34:38]** good at Rust, because I'm fairly new to Rust.
**[34:41]** So there's a bit of bytecoding going on when I was writing some of the Rust code.
**[34:46]** But I had Python implementation that I fully understand, and I'm just making sure I'm making
**[34:49]** a more efficient version of it and have tests.
**[34:51]** So I feel safer doing that stuff.
**[34:54]** And so basically, they lower or like they increase accessibility to languages or paradigms
**[35:00]** that you might not be as familiar with.
**[35:02]** So I think they're very helpful there as well.
**[35:05]** Because there's a ton of Rust code out there, the models are actually pretty good at it.
**[35:07]** I happen to not know that much about it.
**[35:09]** But those models are very useful there.
**[35:11]** The reason I think this question is so interesting is because the main story people have about
**[35:17]** AI exploding and getting to superintelligence pretty rapidly is AI automating, AI engineering
**[35:23]** and AI research.
**[35:25]** So they'll look at the fact that you can have cloud code and make entire applications from
**[35:28]** scratch and be like, if you had this same capability inside of open AI and DeepMind
**[35:33]** and everything, well, just imagine the level of like, you know, 1000 of you or a million
**[35:38]** of you in parallel finding little architectural tweaks.
**[35:40]** And so it's quite interesting to hear you say that this is the thing they're sort of
**[35:44]** asymmetrically worse at.
**[35:46]** And it's like quite relevant to forecasting whether the AI 2027 type explosion is likely
**[35:51]** to happen anytime soon.
**[35:53]** I think that's a good way of putting it.
**[35:54]** And I think you're getting at some of my like, why my timelines are a bit longer.
**[35:58]** You're right.
**[35:59]** I think, yeah, they're not very good at code that hasn't never been written before.
**[36:03]** Maybe it's like one way to put it, which is like what we're trying to achieve when we're
**[36:06]** building these models.
**[36:07]** Very naive question.
**[36:08]** But the architectural tweaks that you're adding to NanoChat, they're in a paper somewhere,
**[36:15]** right?
**[36:16]** They might even be in a repo somewhere.
**[36:17]** So is it surprising that they aren't able to integrate that into whenever you're like,
**[36:25]** add rope embeddings or something, they do that in the wrong way?
**[36:30]** It's tough.
**[36:31]** I think they kind of know, but they don't fully know.
**[36:32]** And they don't know how to fully integrate it into the repo in your style and your code
**[36:35]** and your place and some of the custom things that you're doing.
**[36:39]** And how it fits with all the assumptions of the repository and all this kind of stuff.
**[36:42]** So I think they do have some knowledge, but they haven't gotten to the place where they
**[36:46]** can actually integrate it, make sense of it, and so on.
**[36:50]** I do think that a lot of this stuff, by the way, continues to improve.
**[36:52]** So I think currently probably state of the art model that I go to is the GPT-5 Pro.
**[36:58]** And that's a very, very powerful model.
**[37:00]** So if I actually have 20 minutes, I will copy paste my entire repo and I go to GPT-5 Pro,
**[37:04]** like some questions and often it's not too bad and surprisingly good compared to what
**[37:08]** existed a year ago.
**[37:09]** Yeah.
**[37:10]** But I do think that overall the models are not there.
**[37:14]** And I kind of feel like the industry, it's making too big of a jump and it's trying to
**[37:23]** pretend like this is amazing.
**[37:24]** And it's not.
**[37:25]** It's slop.
**[37:26]** And I think they're not coming to terms with it.
**[37:28]** And maybe they're trying to fundraise or something like that.
**[37:29]** I'm not sure what's going on.
**[37:30]** But we're at this intermediate stage.
**[37:33]** The models are amazing.
**[37:34]** They still need a lot of work.
**[37:35]** For now, autocomplete is my sweet spot.
**[37:38]** But sometimes for some types of code, I will go to a null image.
**[37:41]** Yeah.
**[37:42]** Actually, here's another reason why this is really interesting.
**[37:45]** Through the history of programming, there's been many productivity improvements, compilers,
**[37:52]** linting, better programming languages, etc., which have increased programmer productivity,
**[37:58]** but have not led to an explosion.
**[37:59]** So that sounds very much like autocomplete tab.
**[38:03]** And this other category is just like automation of the programmer.
**[38:07]** And it's interesting you're seeing more in the category of the historical analogies of
**[38:12]** better compilers or something.
**[38:13]** And maybe because this gets at one other kind of thought of that is like, I do feel like
**[38:17]** I have a hard time differentiating where AI begins and stops, because I do see AI as fundamentally
**[38:22]** an extension of computing in some pretty fundamental way.
**[38:25]** And I feel like I see a continuum of this kind of recursive self-improvement or of speeding
**[38:30]** up programmers all the way from the beginning.
**[38:33]** Even I would say code editors, syntax highlighting, syntax or checking even of the types, like
**[38:42]** data type checking.
**[38:44]** All these kinds of tools that we've built for each other, even search engines, why aren't
**[38:48]** search engines part of AI?
**[38:50]** I don't know.
**[38:51]** Ranking is kind of AI, right?
**[38:53]** At some point, Google was like, even early on, they were thinking of themselves as an
**[38:55]** AI company doing Google search engine, which I think is totally fair.
**[38:58]** And so I kind of see it as a lot more of a continuum than I think other people do.
**[39:02]** And I don't, it's hard for me to draw the line.
**[39:04]** And I kind of feel like, okay, we're now getting a much better autocomplete.
**[39:06]** And now we're also getting some agents, which are kind of like these loopy things, but they
**[39:09]** kind of go off rails sometimes.
**[39:12]** And what's going on is that the human is progressively doing a bit less and less of the low level
**[39:17]** stuff.
**[39:18]** For example, we're not writing the assembly code because we have compilers, right?
**[39:20]** The compilers will take my high level language in C and write the assembly code.
**[39:23]** So we're abstracting ourselves very, very slowly.
**[39:26]** And there's this what I call autonomy slider of like more and more stuff is automated of
**[39:30]** the stuff that can be automated at any point in time.
**[39:32]** And we're doing a bit less and less and raising ourselves in the layer of abstraction over
**[39:36]** the automation.
**[39:37]** One of the big problems with RL is that it's incredibly information sparse.
**[39:41]** LabelBox can help you with this by increasing the amount of information that your agent
**[39:46]** gets to learn from with every single episode.
**[39:49]** For example, one of their customers wanted to train a coding agent.
**[39:52]** So LabelBox augmented an IDE with a bunch of extra data collection tools and staffed
**[39:57]** a team of expert software engineers from their aligner network to generate trajectories that
**[40:02]** were optimized for training.
**[40:04]** Now obviously these engineers evaluated these interactions on a pass fail basis, but they
**[40:09]** also rated every single response on a bunch of different dimensions like readability and
**[40:14]** performance.
**[40:15]** And they wrote down their thought processes for every single rating that they gave.
**[40:19]** So you're basically showing every single step an engineer takes and every single thought
**[40:24]** that they have while they're doing their job.
**[40:26]** And this is just something you could never get from usage data alone.
**[40:30]** And so LabelBox packaged up all these evaluations and included all the agent trajectories and
**[40:36]** the corrective human edits for the customer to train on.
**[40:39]** This is just one example.
**[40:40]** So go check out how LabelBox can get you high quality frontier data across domains, modalities,
**[40:47]** and training paradigms.
**[40:48]** Reach out at labelbox.com slash thwarkash.
**[40:54]** Let's talk about RL a bit.
**[40:56]** You two did some very interesting things about this.
**[40:58]** Conceptually, how should we think about the way that humans are able to build a rich world
**[41:05]** model just from interacting with our environment and in ways that seems almost irrespective
**[41:10]** of the final reward at the end of the episode?
**[41:13]** If somebody's starting to start a business, and at the end of 10 years, she finds out
**[41:17]** whether the business succeeded or failed, we say that she's earned a bunch of wisdom
**[41:21]** and experience.
**[41:22]** But it's not because like the log probs of every single thing that happened over the
**[41:25]** last 10 years are up-weighted or down-weighted.
**[41:27]** Something much more deliberate and rich is happening.
**[41:31]** What is the ML analogy, and how does that compare to what we're doing with other ones
**[41:34]** right now?
**[41:35]** Yeah.
**[41:36]** Maybe the way I would put it is humans don't use reinforcement learning, as I've said.
**[41:39]** I think they do something different, which is, yeah, you experience.
**[41:42]** So reinforcement learning is a lot worse than I think the average person thinks.
**[41:46]** Reinforcement learning is terrible.
**[41:50]** It just so happens that everything that we had before it is much worse.
**[41:56]** Because previously, we were just imitating people, so it has all these issues.
**[41:59]** So in reinforcement learning, say you're working with—you're solving a math problem.
**[42:03]** This is very simple.
**[42:04]** You're given a math problem, and you're trying to find a solution.
**[42:08]** Now in reinforcement learning, you will try lots of things in parallel first.
**[42:13]** So you're given a problem.
**[42:14]** You try hundreds of different attempts, and these attempts can be complex, right?
**[42:18]** They can be like, oh, let me try this, let me try that, this didn't work, that didn't
**[42:21]** work, etc.
**[42:22]** And then maybe you get an answer.
**[42:23]** And now you check the back of the book, and you see, okay, the correct answer is this.
**[42:27]** And then you can see that, okay, this one, this one, and that one got the correct answer,
**[42:31]** but these other 97 of them didn't.
**[42:33]** So literally what reinforcement learning does is it goes to the ones that worked really
**[42:36]** well.
**[42:37]** So every single thing you did along the way, every single token gets up-weighted of like,
**[42:41]** do more of this.
**[42:42]** The problem with that is, I mean, people will say that your estimator has high variance,
**[42:46]** but I mean, it's just noisy, it's noisy.
**[42:49]** So basically, it kind of almost assumes that every single little piece of the solution
**[42:53]** that you made that arrived at the right answer was the correct thing to do, which is not
**[42:56]** true.
**[42:57]** Like, you may have gone down the wrong alleys until you arrived at the right solution.
**[43:00]** Every single one of those incorrect things you did, as long as you got to the correct
**[43:03]** solution, will be up-weighted as do more of this.
**[43:05]** It's terrible.
**[43:06]** Yeah.
**[43:07]** It's noise.
**[43:08]** You've done all this work, only to find a single, at the end, you get a single number
**[43:12]** of like, oh, you did correct.
**[43:14]** And based on that, you weigh that entire trajectory as like up-weight or down-weight.
**[43:18]** And so the way I like to put it is you're sucking supervision through a straw, because
**[43:22]** you've done all this work that could be a minute of rollout, and you're like sucking
**[43:26]** the bits of supervision of the final reward signal through a straw, and you're like putting
**[43:29]** it, you're like, you're basically like, yeah, you're broadcasting that across the entire
**[43:35]** trajectory and using that to up-weight or down-weight that trajectory.
**[43:37]** It's crazy.
**[43:38]** A human would never do this.
**[43:40]** Number one, a human would never do hundreds of rollouts.
**[43:43]** Number two, when a person sort of finds a solution, they will have a pretty complicated
**[43:47]** process of review of like, okay, I think these parts that I did well, these parts I did not
**[43:51]** do that well.
**[43:52]** I should probably do this or that.
**[43:53]** And they think through things.
**[43:55]** There's nothing in current LLMs that does this.
**[43:57]** There's no equivalent of it.
**[43:59]** But I do see papers popping out that are trying to do this, because it's obvious to everyone
**[44:03]** in the field.
**[44:04]** So I kind of see as like the first imitation learning actually, by the way, was extremely
**[44:07]** surprising and miraculous and amazing that we can fine-tune by imitation on humans.
**[44:12]** And that was incredible, because in the beginning, all we had was base models.
**[44:15]** Base models are autocomplete.
**[44:17]** And it wasn't obvious to me at the time.
**[44:19]** And I had to learn this.
**[44:20]** And the paper that like blew my mind was InstructGPT, because it pointed out that, hey, you can
**[44:25]** take the pre-trained model, which is autocomplete.
**[44:28]** And if you just fine-tune it on text that looks like conversations, the model will very
**[44:32]** rapidly adapt to become very conversational.
**[44:34]** And it keeps all the knowledge from pre-training.
**[44:36]** And this blew my mind, because I didn't understand that it's just like stylistically can adjust
**[44:40]** so quickly and become an assistant to a user through just a few loops of fine-tuning on
**[44:45]** that kind of data.
**[44:46]** It was very miraculous to me that that worked.
**[44:49]** So incredible.
**[44:50]** And that was like two years, three years of work.
**[44:53]** And now came RL.
**[44:54]** And RL allows you to do a bit better than just imitation learning, right?
**[44:57]** Because you can't have these reward functions, and you can hill-climb on the reward functions.
**[45:02]** And so some problems have just correct answers.
**[45:04]** You can hill-climb on that without getting expert trajectories to imitate.
**[45:07]** So that's amazing.
**[45:08]** And the model can also discover solutions that a human might never come up with.
**[45:12]** So this is incredible.
**[45:13]** And yet, it's so stupid.
**[45:16]** So I think we need more.
**[45:18]** And so I saw a paper from Google yesterday that tried to have this reflect and review
**[45:21]** paid idea in mind.
**[45:24]** What was the memory bank paper or something?
**[45:27]** I don't know.
**[45:28]** I've actually seen a few papers along these lines.
**[45:30]** So I expect there to be some kind of a major update to how we do algorithms for LLMs coming
**[45:35]** in that realm.
**[45:37]** And then I think we need three or four or five more.
**[45:41]** Something like that.
**[45:42]** But you're so good at coming up with evocative phrases.
**[45:46]** Sucking supervision through a straw is like so good.
**[45:52]** So you're saying your problem with outcome-based reward is that you have this huge trajectory.
**[45:57]** And then at the end, you're trying to learn every single possible thing about what you
**[46:01]** should do and what you should learn about the world from that one final bit.
**[46:06]** Why hasn't, given the fact that this is obvious, why hasn't process-based supervision as an
**[46:10]** alternative been a successful way to make models more capable?
**[46:14]** What has been preventing us from using this alternative paradigm?
**[46:16]** So process-based supervision just refers to the fact that we're not going to have a reward
**[46:19]** only at the very end.
**[46:20]** After you've made 10 minutes of work, I'm not going to tell you you did well or not
**[46:23]** well.
**[46:24]** I'm going to tell you at every single step of the way how well you're doing.
**[46:27]** And this is basically the reason we don't have that.
**[46:29]** It's not as tricky how you do that properly.
**[46:32]** Because you have partial solutions and you don't know how to assign credit.
**[46:35]** So when you get the right answer, it's just an equality match to the answer.
**[46:39]** Very simple to implement.
**[46:40]** If you're doing basically process supervision, how do you assign in an automatable way partial
**[46:45]** credit assignment?
**[46:46]** It's not obvious how you do it.
**[46:48]** Lots of labs, I think, are trying to do it with these LLM judges.
**[46:50]** So basically, you get LLMs to try to do it.
**[46:52]** So you prompt an LLM, hey, look at a partial solution of a student.
**[46:55]** How well do you think they're doing if the answer is this?
**[46:57]** And they try to tune the prompt.
**[46:59]** The reason that I think this is kind of tricky is quite subtle.
**[47:02]** And it's the fact that anytime you use an LLM to assign a reward, those LLMs are giant
**[47:07]** things with billions of parameters and they're gameable.
**[47:09]** And if you're reinforcement learning with respect to them, you will find adversarial
**[47:12]** examples for your LLM judges almost guaranteed.
**[47:15]** You can't do this for too long.
**[47:16]** You do maybe 10 steps or 20 steps.
**[47:18]** Maybe it will work.
**[47:19]** But you can't do 100 or 1,000 because it's not obvious.
**[47:22]** Because I know I understand it's not obvious, but basically, the model will find little
**[47:27]** cracks.
**[47:28]** It will find all these like spurious things in the nooks and crannies of the giant model
**[47:33]** and find a way to cheat it.
**[47:34]** So one example that's prominently in my mind is I think this was probably public.
**[47:40]** But basically, if you're using an LLM judge for a reward, so you just give it a solution
**[47:44]** from a student and ask it if the student did well or not.
**[47:47]** We were training with reinforcement learning against that reward function, and it worked
**[47:51]** really well.
**[47:52]** And then suddenly, the reward became extremely large.
**[47:55]** Like it was a massive jump and it did perfect.
**[47:57]** And you're looking at it like, wow, this means the student is perfect in all these problems.
**[48:01]** It's fully solved math.
**[48:03]** But actually, what's happening is that when you look at the completions that you're getting
**[48:06]** from the model, they are complete nonsense.
**[48:08]** They start out okay, and then they change to the, the, the, the, the, the, the.
**[48:11]** So it's just like, oh, okay, let's take two plus three, and we do this and this, and then
**[48:14]** the, the, the, the, the, the, the, the.
**[48:15]** And you're looking at it like, this is crazy.
**[48:17]** How is it getting a reward of one or 100%?
**[48:19]** And you look at the LLM judge, and it turns out the, the, the, the, the, the is an adversarial
**[48:23]** example for the model, and it assigns 100% probability to it.
**[48:27]** And it's just because this is an out-of-sample example to the LLM.
**[48:30]** It's never seen it during training, and you're in pure generalization land.
**[48:34]** It's never seen it during training.
**[48:35]** And in the pure generalization land, you can find these examples that break it.
**[48:40]** So you're basically training the LLM to be a prompt injection model.
**[48:44]** Not even that.
**[48:45]** Prompt injection is way too fancy.
**[48:46]** You're, you're finding adversarial examples, as they're called.
**[48:49]** These are nonsensical solutions that are obviously wrong, but the model thinks are amazing.
**[48:55]** So do they say, you think this is the bottleneck to making RL more functional?
**[48:59]** Then that will require making LLMs better judges, if you want to do this in an automated
**[49:03]** way.
**[49:04]** And then so, is it just going to be like some sort of GAN-like approach, where you had to
**[49:07]** train models to be more robust?
**[49:08]** Yeah.
**[49:10]** I think the labs are probably doing all that.
**[49:11]** Like, okay, so the obvious thing is, like, the, the, the should not get a hundred percent
**[49:14]** reward.
**[49:15]** Okay, well, take the, the, the, the, put in the training set of the LLM judge and say,
**[49:18]** this is not a hundred percent.
**[49:19]** This is zero percent.
**[49:20]** You can do this.
**[49:21]** But every time you do this, you get a new LLM, and it still has adversarial examples.
**[49:24]** There's infinity of adversarial examples.
**[49:26]** And I think probably, if you iterate this a few times, it'll probably be harder and
**[49:29]** harder to find adversarial examples, but I'm not 100% sure, because this thing has a trillion
**[49:33]** parameters or whatnot.
**[49:35]** So I bet you the labs are trying.
**[49:38]** I don't actually, I still think, I still think we need other ideas.
**[49:43]** Interesting.
**[49:44]** Do you have some shape of what the other idea?
**[49:49]** So like this, this idea of like a review, review a solution and come up with synthetic
**[49:55]** examples, such that when you train on them, you get, you get better.
**[49:58]** And like meta-learn it in some way.
**[50:00]** And I think there's some papers that I'm starting to see pop out.
**[50:02]** I only am at a stage of like reading abstracts, because a lot of these papers, you know, they're
**[50:06]** just ideas.
**[50:07]** So I'm trying to actually like make it work on a frontier LLM lab scale, in full generality,
**[50:12]** because when you see these papers, they pop up and it's just like a little bit of noisy,
**[50:15]** you know, it's cool ideas, but I haven't actually seen anyone convincingly show that this is
**[50:20]** possible.
**[50:21]** That said, the LLM labs are fairly closed.
**[50:23]** So who knows what they're doing now, but yeah.
**[50:26]** So I guess I see a very, not easy, but like, I can conceptualize how you would be able
**[50:33]** to train on synthetic examples or synthetic problems that you have made for yourself.
**[50:37]** But there seems to be another thing humans do, maybe sleep is this, maybe daydreaming
**[50:40]** is this, which is not necessarily come up with fake problems, but just like reflect.
**[50:46]** And I'm not sure what the ML analogy for, you know, daydreaming or sleeping, but just
**[50:51]** reflecting.
**[50:52]** I haven't come up with any problem.
**[50:53]** I mean, obviously the very basic analogy would just be like fine tuning on reflection bits,
**[50:57]** but I feel like in practice that probably wouldn't work that well.
**[50:59]** So I don't know if you have some take on what the analogy of like this thing is.
**[51:04]** Yeah, I do think that we're missing some aspects there.
**[51:06]** So as an example, when you're reading a book, I almost feel like currently when LLMs are
**[51:12]** reading a book, what that means is we stretch out the sequence of text and the model is
**[51:16]** predicting the next token and it's getting some knowledge from that.
**[51:19]** That's not really what humans do, right?
**[51:20]** So when you're reading a book, I almost don't even feel like the book is like exposition
**[51:23]** I'm supposed to be attending to and training on.
**[51:25]** The book is a set of prompts for me to do synthetic data generation, or for you to get
**[51:30]** into a book club and talk about it with your friends.
**[51:33]** And it's by manipulating that information that you actually gain that knowledge.
**[51:37]** And I think we have no equivalent of that again with LLMs.
**[51:40]** They don't really do that, but I'd love to see during pre-training some kind of a stage
**[51:43]** that thinks through the material and tries to reconcile it with what it already knows
**[51:47]** and thinks through for like some amount of time and gets that to work.
**[51:51]** And so there's no equivalence of any of this.
**[51:53]** This is all research.
**[51:54]** There's some subtle, very subtle that I think are very hard to understand reasons why it's
**[51:58]** not trivial.
**[51:59]** If I can just describe one, why can't we just synthetically generate and train on it?
**[52:03]** Well, because every synthetic example, like if I just give synthetic generation of the
**[52:07]** model thinking about a book, you look at it and you're like, this looks great, why can't
**[52:11]** I train on it?
**[52:12]** Well, you could try, but the model will actually get much worse if you continue trying.
**[52:15]** And that's because all of the samples you get from models are silently collapsed.
**[52:19]** They're silently, this is not obvious if you look at any individual example of it, they
**[52:23]** occupy a very tiny manifold of the possible space of sort of thoughts about content.
**[52:28]** So the LLMs, when they come off, they're what we call collapsed.
**[52:31]** They have a collapsed data distribution.
**[52:33]** If you sample, one easy way to say it is go to a chat GPT and ask it, tell me a joke.
**[52:38]** It only has like three jokes.
**[52:40]** It's not giving you the whole breadth of possible jokes.
**[52:42]** It's giving you like, it knows like three jokes.
**[52:44]** They're soundly collapsed.
**[52:46]** So basically, you're not getting the richness and the diversity and the entropy from these
**[52:50]** models as you would get from humans.
**[52:52]** So humans are a lot more sort of noisier, but at least they're not biased.
**[52:55]** They're not in a statistical sense.
**[52:57]** They're not silently collapsed.
**[52:59]** They maintain a huge amount of entropy.
**[53:00]** So how do you get synthetic data generation to work despite the collapse and while maintaining
**[53:05]** the entropy is a research problem.
**[53:08]** Just to make sure I understood, the reason that the collapse is relevant to synthetic
**[53:11]** data generation is because you want to be able to come up with synthetic problems or
**[53:16]** reflections which are not already in your data distribution?
**[53:20]** I guess what I'm saying is, say we have a chapter of a book and I ask Nolan to think
**[53:24]** about it.
**[53:25]** It will give you something that looks very reasonable.
**[53:28]** But if I ask it 10 times, you'll notice that all of them are the same.
**[53:32]** You can't just keep scaling, quote unquote, reflection on the same amount of prompt information
**[53:39]** and then get returns from that.
**[53:41]** So any individual sample will look okay, but the distribution of it is quite terrible.
**[53:46]** And it's quite terrible in such a way that if you continue training on too much of your
**[53:49]** own stuff, you actually collapse.
**[53:50]** I actually think that there's no like fundamental solutions to this possibly, and I also think
**[53:54]** humans collapse over time.
**[53:56]** I think this is, again, these analogies are surprisingly good, but humans collapse during
**[54:00]** the course of their lives.
**[54:01]** This is why children have completely, you know, they haven't overfit yet.
**[54:05]** And they will say stuff that will shock you because it's kind of, you can see where they're
**[54:09]** coming from, but it's just not the thing people say and because they're not yet collapsed.
**[54:14]** But we're collapsed.
**[54:15]** We end up revisiting the same thoughts.
**[54:17]** We end up, you know, saying more and more of the same stuff and the learning rates go
**[54:21]** down and the collapse continues to get worse.
**[54:24]** And then everything deteriorates.
**[54:26]** Have you seen a super interesting paper that dreaming is a way of preventing this kind
**[54:32]** of overfitting and collapse?
**[54:33]** That the reason the dreaming is evolutionary adaptive is to put you in weird situations
**[54:40]** that are like very unlike your day-to-day reality so that to prevent this kind of overfitting?
**[54:44]** It's an interesting idea.
**[54:45]** I mean, I do think that when you're generating things in your head and then you're attending
**[54:49]** to it, you're kind of like training on your own samples, you're training on your synthetic
**[54:52]** data.
**[54:53]** And if you do it for too long, you go off rails and you collapse way too much.
**[54:56]** So you always have to like seek entropy in your life.
**[55:01]** So talking to other people is a great source of entropy and things like that.
**[55:05]** So maybe the brain has also built some internal mechanisms for increasing the amount of entropy
**[55:11]** in that process.
**[55:12]** But yeah, maybe that's an interesting idea.
**[55:14]** This is a very ill-formed thought, so I'll just put it out and let you react to it.
**[55:18]** The best learners that we are aware of, which are children, are extremely bad at recollecting
**[55:24]** information.
**[55:25]** In fact, at the very earliest stages of childhood, you will forget everything.
**[55:29]** You're just an amnesiac about everything that happens before a certain year date.
**[55:32]** But you're like extremely good at picking up new languages and learning from the world.
**[55:36]** And maybe there's some element of like being able to see the forest for the trees.
**[55:39]** Whereas if you compare it to the opposite end of the spectrum, you have LLM pre-training,
**[55:44]** which these models will literally be able to regurgitate word for word what is the next
**[55:48]** thing in a Wikipedia page.
**[55:50]** But their ability to learn abstract concepts really quickly the way a child can is much
**[55:55]** more limited.
**[55:56]** And then adults are somewhere in between where they don't have the flexibility of childhood
**[55:59]** learning.
**[56:00]** But they can, you know, adults can memorize facts and information in a way that is harder
**[56:05]** for kids.
**[56:06]** And I don't know if there's something interesting about that.
**[56:08]** I think there's something very interesting about that, yeah, 100%.
**[56:10]** I do think that humans actually, they do kind of like have a lot more of an element compared
**[56:15]** to LLMs of like seeing the forest for the trees.
**[56:18]** And we're not actually that good at memorization, which is actually a feature.
**[56:23]** Because we're not that good at memorization, we actually are kind of like forced to find
**[56:27]** the patterns in a more general sense.
**[56:31]** I think LLMs in comparison are extremely good at memorization.
**[56:34]** They will recite passages from all these training sources.
**[56:38]** You can give them completely nonsensical data, like you can hash some amount of text or something
**[56:43]** like that.
**[56:44]** You get a completely random sequence.
**[56:46]** a single iteration or two, it can suddenly regurgitate the entire thing, it will memorize
**[56:49]** it.
**[56:50]** There's no way a person can read a single sequence of random numbers and recite it to
**[56:53]** you.
**[56:55]** And that's a feature, not a bug, almost.
**[56:57]** Because it forces you to like only learn the generalizable components, whereas LLMs are
**[57:01]** distracted by all the memory that they have of the pre-trained documents.
**[57:05]** And it's probably very distracting to them in a certain sense.
**[57:09]** So that's why when I talk about the cognitive core, I actually want to remove the memory,
**[57:12]** which is what we talked about.
**[57:13]** I'd love to have them have less memory so that they have to look things up.
**[57:17]** And they only maintain the algorithms for like thought and the idea of an experiment
**[57:22]** and all this cognitive glue of acting.
**[57:26]** And this is also relevant to preventing model collapse.
**[57:29]** Let me think.
**[57:34]** I'm not sure.
**[57:35]** I think it's almost like a separate axis.
**[57:37]** It's almost like the models are way too good at memorization, and somehow we should we
**[57:41]** should remove that.
**[57:42]** And I think people are much worse, but it's a good thing.
**[57:46]** What is a solution to model collapse?
**[57:48]** I mean, there's very naive things you could attempt is just like the distribution over
**[57:53]** logist should be wider or something like there's many naive things you could try.
**[57:57]** What ends up being the problem with the naive approaches?
**[57:59]** Yeah, I think that's a great question.
**[58:01]** I mean, you can imagine having a regularization for entropy and things like that.
**[58:04]** I guess they just don't work as well empirically because right now, like the models are collapsed.
**[58:09]** And I will say most of the tasks that we want of them don't actually demand the diversity.
**[58:17]** It's probably the answer of what's going on.
**[58:18]** And so it's just that the frontier labs are trying to make the models useful.
**[58:22]** And I kind of just feel like the diversity of the outputs is not so much.
**[58:26]** Number one, it's much harder to work with and evaluate and all this kind of stuff.
**[58:28]** But maybe it's not what's actually capturing most of the value.
**[58:31]** In fact, it's actively penalized, right?
**[58:34]** If you're like super creative in RL, it's like not good.
**[58:37]** Yeah.
**[58:38]** And if you're doing a lot of writing help from LLMs and stuff like that, I think it's
**[58:40]** probably bad because the models will give you these like silently all the same stuff.
**[58:46]** So they won't explore lots of different ways of answering a question, right?
**[58:50]** But I kind of feel like maybe this diversity is just not as big of a, yeah, maybe like
**[58:55]** not as many applications needed.
**[58:56]** So the models don't have it.
**[58:57]** But then it's actually a problem with synthetic generation time, et cetera.
**[58:59]** So we're actually shooting ourselves in the foot by not allowing the centropy to maintain
**[59:03]** in the model.
**[59:04]** And I think possibly the labs should try harder.
**[59:06]** And then I think you hinted that it's a very fundamental problem.
**[59:10]** It won't be easy to solve.
**[59:11]** And yeah, what's your intuition for that?
**[59:14]** I don't actually know if it's super fundamental.
**[59:17]** I don't actually know if I intended to say that.
**[59:19]** I do think that, I haven't done these experiments, but I do think that you could probably regularize
**[59:24]** the entropy to be higher.
**[59:26]** So you're encouraging the model to give you more and more solutions.
**[59:30]** But you don't want it to start deviating too much from the training data.
**[59:33]** It's going to start making up its own language.
**[59:34]** It's going to start using words that are extremely rare, you know, so it's going to
**[59:37]** drift too much from the distribution.
**[59:40]** So I think controlling the distribution is just like a tricky, it's just like someone
**[59:43]** just has to, it's probably not trivial in that sense.
**[59:47]** How many bits should the optimal core of intelligence end up being, if you just had to make a guess?
**[59:54]** The thing we put on the von Neumann probes.
**[59:58]** How big does it have to be?
**[01:00:00]** So it's really interesting in the history of the field, because at one point, everything
**[01:00:03]** was very scaling-pilled in terms of, oh, we're going to make much bigger models, trillions
**[01:00:07]** of parameter models.
**[01:00:08]** And actually, what the models have done in size is they've gone up, and now they've actually
**[01:00:12]** kind of like actually even come down, instead of their models are smaller.
**[01:00:16]** And even then, I actually think they memorized way too much.
**[01:00:20]** So I think I had a prediction a while back that I almost feel like we can get cognitive
**[01:00:23]** cores that are very good at even like a billion, billion parameters.
**[01:00:27]** It should be already like, if you talk to a billion parameter model, I think in 20 years,
**[01:00:32]** you can actually have a very productive conversation, it thinks.
**[01:00:36]** And it's a lot more like a human.
**[01:00:37]** But if you ask it some factual question, it might have to look it up.
**[01:00:40]** But it knows that it doesn't know, and it might have to look it up, and it will just
**[01:00:42]** do all the reasonable things.
**[01:00:43]** That's actually surprising that you think it will take a billion, because already, we
**[01:00:47]** have a billion parameter models, or a couple billion parameter models that are like very
**[01:00:50]** intelligent.
**[01:00:51]** Also, VR models are like a trillion parameters, right?
**[01:00:53]** But they remember so much stuff, like, it's just...
**[01:00:56]** But I'm surprised that in 10 years, given the pace, okay, we have GPT, OSS, 20B, that's
**[01:01:05]** way better than GPT-4 original, which was a trillion plus parameters.
**[01:01:10]** So given that trend, I'm actually surprised you think in 10 years, the cognitive core
**[01:01:13]** is still a billion parameters.
**[01:01:15]** I would...
**[01:01:16]** Yeah, I'm surprised you're not like, so it's gonna be like, 10s of millions or millions.
**[01:01:19]** No, because I basically think that the training data is...
**[01:01:22]** So here's the issue, the training data is the internet, which is really terrible.
**[01:01:25]** So there's a huge amount of gains to be made because the internet is terrible.
**[01:01:28]** Like if you actually...
**[01:01:29]** And even the internet, when you and I think of the internet, you're thinking of like a
**[01:01:31]** Wall Street Journal, or that's not what this is.
**[01:01:35]** When you're actually looking at a pre-trained dataset in the Frontier Lab, and you look
**[01:01:37]** at a random internet document, it's total garbage.
**[01:01:40]** Like I don't even know how this works at all.
**[01:01:42]** It's some like stock ticker symbols.
**[01:01:46]** It's a huge amount of slop and garbage from like all the corners of the internet.
**[01:01:50]** It's not like your Wall Street Journal article, that's extremely rare.
**[01:01:54]** So I almost feel like because the internet is so terrible, we actually have to sort of
**[01:01:57]** build really big models to compress all that.
**[01:02:00]** Most of that compression is memory work instead of like cognitive work.
**[01:02:03]** Interesting.
**[01:02:04]** But what we really want is the cognitive part, actually delete the memory.
**[01:02:07]** And then, so I guess what I'm saying is like, we need intelligent models to help us refine
**[01:02:12]** even the pre-training set to just narrow it down to the cognitive components.
**[01:02:15]** And then I think you get away with a much smaller model because it's a much better dataset
**[01:02:19]** and you could train it on it.
**[01:02:20]** But probably it's not trained directly on it, it's probably distilled from a much better
**[01:02:23]** model still.
**[01:02:24]** Right.
**[01:02:25]** But why is the distilled version still a billion is I guess the thing I'm curious about.
**[01:02:28]** I just feel like distillation works extremely well.
**[01:02:30]** So almost every small model, if you have a small model, it's almost certainly distilled.
**[01:02:34]** Why would you train on?
**[01:02:35]** Right.
**[01:02:36]** No, no.
**[01:02:37]** But why is the distillation not in 10 years not getting below one billion?
**[01:02:39]** Oh, you think it should be smaller than a billion?
**[01:02:41]** I mean, come on, right?
**[01:02:43]** At some point, it should take at least a billion knobs to do something interesting.
**[01:02:49]** You're thinking it should be even smaller?
**[01:02:51]** Yeah.
**[01:02:52]** I mean, just like if you look at the trend over the last few years, just finding low
**[01:02:54]** hanging fruit and going from like trillion plus models that are like literally two orders
**[01:02:58]** of magnitude smaller in a matter of two years and having better performance.
**[01:03:03]** It makes me think the sort of core of intelligence might be even way, way smaller, like plenty
**[01:03:09]** of room at the bottom to paraphrase Feynman.
**[01:03:11]** I mean, I almost feel like I'm already contrarian by talking about a billion in the parameter
**[01:03:14]** cognitive core and you're outdoing me.
**[01:03:16]** I think, yeah, maybe we could get a little bit smaller.
**[01:03:19]** I mean, I still think that there should be enough.
**[01:03:21]** Yeah, maybe it can be smaller.
**[01:03:23]** I do think that practically speaking, you want the model to have some knowledge.
**[01:03:26]** You don't want it to be looking up everything.
**[01:03:28]** Because then you can't like think in your head, you're looking up way too much stuff
**[01:03:30]** all the time.
**[01:03:31]** So I do think it needs to be some basic curriculum needs to be there for knowledge.
**[01:03:36]** But it doesn't have esoteric knowledge, you know?
**[01:03:38]** So we're discussing what like plausibly could be the cognitive core.
**[01:03:41]** There's a separate question, which is, what will actually be the size of frontier models
**[01:03:46]** over time?
**[01:03:47]** And I'm curious to have a prediction.
**[01:03:49]** We had increasing scale up to maybe 4.5.
**[01:03:51]** And now we're seeing decreasing slash plateauing scale.
**[01:03:55]** There's many reasons that could be going on.
**[01:03:56]** But do you have a prediction about going forward?
**[01:03:58]** Will the biggest models be bigger?
**[01:04:00]** Will they be smaller?
**[01:04:01]** Will they be the same?
**[01:04:02]** Yeah, I don't know that I have a super strong prediction.
**[01:04:06]** I do think that the labs are just being practical.
**[01:04:08]** They have a flops budget and a cost budget.
**[01:04:10]** And it just turns out that pre-training is not where you want to put most of your flops
**[01:04:13]** or your cost.
**[01:04:14]** So that's why the models have gotten smaller.
**[01:04:16]** Because they are a bit smaller, the pre-training stage is smaller, et cetera.
**[01:04:19]** But they make it up in reinforcement learning and all this kind of stuff, mid-training and
**[01:04:21]** all this kind of stuff that follows.
**[01:04:23]** So they're just being practical in terms of all the stages and how you get the most bang
**[01:04:26]** for the buck.
**[01:04:27]** So I guess like forecasting that trend, I think, is quite hard.
**[01:04:30]** I do still expect that there's so much low-hanging fruit.
**[01:04:33]** That's my basic expectation.
**[01:04:37]** And so I have a very wide distribution here.
**[01:04:40]** Do you expect the low-hanging fruit to be similar in kind to the kinds of things that
**[01:04:45]** have been happening over the last two to five years?
**[01:04:48]** Like just in terms of like, if I look at NanoChat versus NanoGPT and then the architectural
**[01:04:52]** tweaks you made, is that basically like the flavor of things you continue to keep happening?
**[01:04:56]** Or is there...
**[01:04:57]** You're not expecting any giant...
**[01:04:59]** For the most part, yeah.
**[01:05:00]** I expect the data sets to get much, much better.
**[01:05:02]** Because when you look at the average data sets, they're extremely terrible.
**[01:05:04]** Like so bad that I don't even know how anything works, to be honest.
**[01:05:07]** Like look at the average example in the training set.
**[01:05:10]** Like factual mistakes, errors, nonsensical things.
**[01:05:15]** How when you do it at scale, the noise washes away and you're left with some of the signal.
**[01:05:20]** So data sets will improve a ton.
**[01:05:21]** It's just everything gets better.
**[01:05:22]** So our hardware, all the kernels, all the kernels for running the hardware and maximizing
**[01:05:29]** what you get with the hardware.
**[01:05:30]** You know, so NVIDIA is slowly tuning the actual hardware itself, TensorCourse and so on.
**[01:05:34]** All that needs to happen and will continue to happen.
**[01:05:37]** All the kernels will get better and utilize the chip to the max extent.
**[01:05:40]** All the algorithms will probably improve over optimization, architecture, and just all the
**[01:05:44]** modeling components of how everything is done and what the algorithms are that we're
**[01:05:47]** even training with.
**[01:05:48]** So I do kind of expect like a just very, just everything.
**[01:05:53]** Nothing dominates.
**[01:05:54]** Everything plus 20% is like roughly what I've seen.
**[01:05:59]** Okay.
**[01:06:00]** This is my general manager, Max.
**[01:06:01]** Good to be here.
**[01:06:02]** Here every day.
**[01:06:03]** And you have been here since you were onboarded about six months ago.
**[01:06:05]** But when I was-
**[01:06:06]** Three months ago.
**[01:06:07]** Oh, right.
**[01:06:08]** Time passes so fast.
**[01:06:09]** But when I onboarded you, I was in France.
**[01:06:12]** And so we basically didn't get the chance to talk at all, almost.
**[01:06:16]** And you basically just gave me one login.
**[01:06:18]** I gave you access to my Mercury platform, which is the banking platform that I was using
**[01:06:23]** at the time to run the podcast.
**[01:06:24]** And so I logged into Mercury, assuming that that would just be the first of many steps.
**[01:06:27]** But I realized that was how you were running the entire business, even down to a lot of
**[01:06:33]** our editors, our international contractors.
**[01:06:34]** And so you had just figured out how to set up these recurring payments to set up basic
**[01:06:38]** payroll.
**[01:06:39]** And it just made the experience of all of these things I was doing before so seamless
**[01:06:42]** that it didn't even occur to me until you pointed it out that this is not the natural
**[01:06:45]** way to set up payroll or invoicing or any of these other things.
**[01:06:49]** Yeah.
**[01:06:50]** I was surprised, but I was like, it's worked so far.
**[01:06:52]** That's right.
**[01:06:53]** So maybe I'll trust it.
**[01:06:54]** And then now I can't think of doing anything else.
**[01:06:55]** All right.
**[01:06:56]** You heard him.
**[01:06:57]** Visit mercury.com to apply online in minutes.
**[01:07:00]** Cool.
**[01:07:01]** Thanks, Max.
**[01:07:02]** Thanks for having me.
**[01:07:03]** Dude, you're great at this.
**[01:07:04]** I'm so nervous, but thank you.
**[01:07:05]** Mercury is a financial technology company, not a bank.
**[01:07:08]** Providing services provided through Choice Financial Group, Column NA, and Evolve Bank
**[01:07:11]** and Trust.
**[01:07:12]** Members FDIC.
**[01:07:14]** People have proposed different ways of charting how much progress you've made towards full
**[01:07:19]** AGI because if you can come up with some line, then you can see where that line intersects
**[01:07:24]** with AGI and where that would happen on the x-axis.
**[01:07:27]** And so people have proposed, oh, it's like the education level, like we had a high schooler
**[01:07:30]** and then they went to college with RL and they're going to get a PhD.
**[01:07:34]** Yeah, I don't like that one.
**[01:07:35]** Or then they'll propose Horizon Link.
**[01:07:37]** So maybe they can do tasks that take a minute, they can do those autonomously, then they
**[01:07:41]** can autonomously do tasks that take an hour, a human an hour, a human a week, et cetera.
**[01:07:46]** How do you think about what is the relevant y-axis here?
**[01:07:50]** What is the, how should we think about how AI is making progress?
**[01:07:54]** So I guess I have two answers to that.
**[01:07:55]** Number one, I'm almost tempted to like reject the question entirely because again, like
**[01:07:59]** I see this as an extension of computing.
**[01:08:01]** Have we talked about like how to chart progress in computing or how do you chart progress
**[01:08:04]** in computing since 1970s or whatever?
**[01:08:06]** What is the x-axis?
**[01:08:07]** So I kind of feel like the whole question is kind of like funny from that perspective
**[01:08:10]** a little bit.
**[01:08:11]** But I will say, I guess like when people talk about AI and the original AGI and how we spoke
**[01:08:16]** about it when we, when OpenAI started, AGI was a system you can go to that can do any
**[01:08:22]** task that is economically valuable, any economically valuable task at human performance or better.
**[01:08:28]** Okay.
**[01:08:29]** So that was the definition.
**[01:08:30]** And I was pretty happy with that at the time.
**[01:08:32]** And I kind of feel like I've stuck to that definition forever.
**[01:08:34]** And then people have made up all kinds of other definitions, but I feel like I like
**[01:08:39]** that definition.
**[01:08:40]** Now, number one, the first concession that people make all the time is they just take
**[01:08:43]** out all the physical stuff because we're just talking about digital knowledge work.
**[01:08:47]** I feel like that's a pretty major concession compared to the original definition, which
**[01:08:51]** was like any task a human can do.
**[01:08:52]** I can lift things, et cetera, like AI can't do that, obviously.
**[01:08:55]** So, okay.
**[01:08:56]** But we'll take it.
**[01:08:57]** What fraction of the economy are we taking away by saying only knowledge work?
**[01:09:02]** I don't actually know the numbers.
**[01:09:03]** I feel like it's about 10 to 20%, if I had to guess, is only knowledge work.
**[01:09:09]** Like someone could work from home and perform tasks, something like that.
**[01:09:13]** I still think it's a really large market.
**[01:09:15]** Like, yeah, what is the size of the economy and what is 10, 20% like we're still talking
**[01:09:19]** about a few trillion dollars of even in the US of market share almost or like work.
**[01:09:25]** So, it's still a very massive bucket.
**[01:09:27]** So, but I guess like going back to the definition, I guess what I would be looking for is to
**[01:09:32]** what extent is that definition true?
**[01:09:34]** So, are there jobs or lots of tasks?
**[01:09:37]** If we think of tasks as, you know, not jobs, but tasks kind of difficult.
**[01:09:41]** Because the problem is like society will refactor based on the tasks that make up jobs compared
**[01:09:46]** to what's based on what's automatable or not.
**[01:09:49]** But today, what jobs are replaceable by AI?
**[01:09:51]** So, a good example recently was Geoff Hinton's prediction that radiologists would not be
**[01:09:56]** a job anymore.
**[01:09:58]** And this turned out to be very wrong in a bunch of ways, right?
**[01:10:00]** Radiologists are alive and well and growing, even though computer vision is really, really
**[01:10:04]** good at recognizing all the different things that they have to recognize in images.
**[01:10:07]** And it's just messy, complicated job with a lot of surfaces and dealing with patients
**[01:10:11]** and all this kind of stuff in the context of it.
**[01:10:13]** So, I guess, I don't actually know that by that definition, AI has made a huge amount
**[01:10:18]** of dent yet.
**[01:10:21]** But some of the jobs maybe that I would be looking for have some features that I think
**[01:10:24]** make it very amenable to automation earlier than later.
**[01:10:27]** As an example, call center employees often come up and I think rightly so.
**[01:10:30]** Because call center employees have a number of simplifying properties with respect to
**[01:10:34]** what's automatable today.
**[01:10:37]** Their jobs are pretty simple.
**[01:10:39]** It's a sequence of tasks and every task looks similar.
**[01:10:42]** Like you take a phone call with a person, it's 10 minutes of interaction or whatever
**[01:10:45]** it is, probably a bit longer, in my experience, a lot longer.
**[01:10:49]** And you complete some task in some scheme and you change some database entries around
**[01:10:53]** or something like that.
**[01:10:54]** So, you keep repeating something over and over again, and that's your job.
**[01:10:57]** So, basically, you do want to bring in the task horizon, how long it takes to perform
**[01:11:01]** a task.
**[01:11:02]** And then you want to also remove context, like you're not dealing with different parts
**[01:11:06]** of services of companies or other customers, it's just the database, you and a person you're
**[01:11:11]** serving.
**[01:11:12]** And so, it's more closed, it's more understandable, and it's purely digital.
**[01:11:15]** So, I would be looking for those things.
**[01:11:17]** But even there, I'm not actually looking at full automation yet.
**[01:11:19]** I'm looking for an autonomy slider.
**[01:11:21]** And I almost expect that we are not going to instantly replace people.
**[01:11:25]** We're going to be swapping in AIs that do 80% of the volume.
**[01:11:29]** They delegate 20% of the volume to humans.
**[01:11:31]** And humans are supervising teams of five AIs doing the call center work that's more rote.
**[01:11:35]** So, I would be looking for new interfaces or new companies that provide some kind of
**[01:11:40]** a layer that allows you to manage some of these AIs that are not yet perfect.
**[01:11:47]** And then I would expect that across the economy and a lot of jobs are a lot harder than call
**[01:11:50]** center employee.
**[01:11:51]** I wonder with radiologists.
**[01:11:54]** I'm totally speculating.
**[01:11:55]** I have no idea how what the actual workflow of a radiologist involves.
**[01:11:58]** But one analogy that might be applicable is when we were first being rolled out, there'd
**[01:12:05]** be a person sitting in the front seat, and you just had to have them there to make sure
**[01:12:10]** that if something went really wrong, they're there to monitor.
**[01:12:12]** And I think even today, people are still watching to make sure things are going well.
**[01:12:15]** RoboTaxi, which was just deployed, actually still has a person inside it.
**[01:12:19]** And we could be in a similar situation where if you automate 99% of a job, that last 1%
**[01:12:25]** the human has to do is incredibly valuable because it's bottlenecking everything else.
**[01:12:29]** And if it was the case with radiologists, where the person sitting in the front of the
**[01:12:33]** Uber or the front of the Waymo has to be specially trained for years in order to be able to provide
**[01:12:37]** the last 1%, their wages should go up tremendously because they're the one thing bottlenecking
**[01:12:42]** wide deployment.
**[01:12:43]** So radiologists, I think their wages have gone up for similar reasons.
**[01:12:46]** If you're like the last bottleneck, you should, you're like, and you're not fungible, which
**[01:12:49]** like, you know, a Waymo driver might be fungible with other things.
**[01:12:52]** So you might see this thing where like your wages go like, whoop, and then to get a 90%
**[01:12:57]** and then like, just like that.
**[01:12:58]** And then the last 1% is gone.
**[01:13:00]** And I wonder if we're seeing similar things with radiology or salaries of call center workers
**[01:13:05]** or anything like that.
**[01:13:06]** Yeah, I think that's an interesting question.
**[01:13:10]** I don't think we're currently seeing that with radiology or, and I don't have like,
**[01:13:14]** in my understanding, but I think radiology is not a good example, basically.
**[01:13:17]** I don't know why Jeff Hinton picked on radiology, because I think it's an extremely messy, complicated
**[01:13:23]** profession.
**[01:13:24]** Yeah.
**[01:13:25]** So I would be a lot more interested in what's happening with call center employees today,
**[01:13:27]** for example, because I would expect a lot of the road stuff to be automatable today.
**[01:13:32]** And I don't have a first level access to it, but maybe I would be looking for trends of
**[01:13:35]** what's happening with the call center employees.
**[01:13:38]** Maybe some of the things I would also expect is maybe they are swapping in AI, but then
**[01:13:42]** I would still wait for a year or two, because I would potentially expect them to pull back
**[01:13:47]** and actually rehire some of the people.
**[01:13:48]** I think there's been evidence that that's already been happening in the, generally in
**[01:13:52]** the companies that have been adopting AI, which I think is quite surprising.
**[01:13:54]** And I also find what was really surprising, okay, AGI, right, like, a thing which would
**[01:14:01]** do everything and okay, we'll take out physical work, the thing which should be able to do
**[01:14:05]** all knowledge work.
**[01:14:06]** And what you would have naively anticipated, that the way this regression would happen
**[01:14:09]** is like, you take a little task that a consultant is doing, you take that out of the bucket,
**[01:14:16]** you take a little task that an accountant is doing, you take that out of the bucket.
**[01:14:21]** And then you're just doing this across all knowledge work.
**[01:14:23]** But instead, if we do believe we're on the path of AGI with the current paradigm, the
**[01:14:27]** progression is very much not like that, at least it just does not seem like consultants
**[01:14:31]** and accounts and whatever are getting like huge productive improvement.
**[01:14:33]** It's very much like programmers are like, getting more and more chills of the way at
**[01:14:39]** their work.
**[01:14:40]** If you do look at the revenues of these companies, discounting just like normal chat revenue,
**[01:14:43]** which I think is like, I don't know, that's similar to like Google or something.
**[01:14:48]** Just looking at API revenues, it's like dominated by coding, right?
**[01:14:51]** So this thing which is general, quote unquote, should be able to do any knowledge work, it's
**[01:14:56]** just overwhelmingly doing only coding as a surprising way that you would expect like
**[01:15:00]** the AGI to be deployed.
**[01:15:02]** So I think there's an interesting point here, because I do believe coding is like the perfect
**[01:15:06]** first thing for these LLMs and agents.
**[01:15:12]** And that's because coding has always fundamentally worked around text.
**[01:15:17]** It's computer terminals and text and everything is based around text.
**[01:15:20]** And LLMs, the way they're trained on the internet, love text.
**[01:15:24]** And so they're perfect text processors, and there's all this data out there, and it's
**[01:15:27]** just perfect fit.
**[01:15:29]** And also we have a lot of infrastructure pre-built for handling code and text.
**[01:15:33]** So for example, we have a Visual Studio code or your favorite IDE showing you code.
**[01:15:41]** And an agent can plug into that.
**[01:15:42]** So for example, if an agent has a diff where it made some change, we suddenly have all
**[01:15:46]** this code already that shows all the differences to a code base using a diff.
**[01:15:50]** So it's almost like we've pre-built a lot of the infrastructure for code.
**[01:15:55]** Now contrast that with some of the things that don't enjoy that at all.
**[01:15:59]** So as an example, there's people trying to build automation not for coding, but for example,
**[01:16:02]** for slides.
**[01:16:03]** Like I saw a company doing slides.
**[01:16:05]** That's much, much harder.
**[01:16:06]** And the reason it's much, much harder is because slides are not text.
**[01:16:09]** Slides are little graphics, and they're arranged spatially, and there's visual components to
**[01:16:14]** it.
**[01:16:16]** And slides don't have this pre-built infrastructure.
**[01:16:18]** Like for example, if an agent is to make a different change to your slides, how does a
**[01:16:22]** thing show you the diff?
**[01:16:24]** How do you see the diff?
**[01:16:25]** There's nothing that shows diffs for slides.
**[01:16:27]** So someone has to build it.
**[01:16:29]** So it's just some of these things are not amenable to AIs as they are, which is text
**[01:16:34]** processors and code surprisingly is.
**[01:16:37]** I actually am not sure if that alone explains it because I personally have tried to get
**[01:16:44]** LLMs to be useful in domains which are just pure language in, language out.
**[01:16:51]** Like rewriting transcripts, like coming up with clips based on transcripts, etc.
**[01:16:56]** And you might say, well, it's very plausible that I didn't do every single possible thing
**[01:17:00]** I could do.
**[01:17:01]** I put a bunch of good examples in context, but maybe I should have done some kind of
**[01:17:05]** fine tuning or whatever.
**[01:17:06]** So our mutual friend, Andy Matuszak, told me that he actually tried 50 billion things
**[01:17:12]** to try to get models to be good at writing spaced repetition prompts.
**[01:17:15]** Again, very much language in, language out tasks.
**[01:17:19]** The kind of thing that should be dead center in the repertoire of these LLMs.
**[01:17:22]** And he tried in-context learning, obviously, with a few short examples.
**[01:17:26]** I think he told me a bunch of things like supervised fine tuning and retrieval, whatever.
**[01:17:33]** And he just could not get them to make carts to his satisfaction.
**[01:17:37]** So I find it striking that even in language out domains, it's actually very hard to get
**[01:17:42]** a lot of economic value out of these models separate from coding.
**[01:17:45]** And I don't know what explains it.
**[01:17:46]** Yeah, I think that makes sense.
**[01:17:49]** I mean, I would say, yeah, I'm not saying that anything text is trivial, right?
**[01:17:54]** I do think that code is like, it's pretty structured.
**[01:17:58]** Text is maybe a lot more flowery and there's a lot more like entropy in text, I would say.
**[01:18:04]** I don't know how else to put it.
**[01:18:06]** And also, I mean, code is hard.
**[01:18:08]** And so people sort of feel quite empowered by LLMs, even from like simple kind of knowledge.
**[01:18:14]** I basically, I don't actually know that I have a very good answer.
**[01:18:19]** I mean, obviously, like text makes it much, much easier, maybe, is maybe why I put it.
**[01:18:22]** But it doesn't mean that all text is trivial.
**[01:18:25]** How do you think about superintelligence?
**[01:18:26]** Do you expect it to feel qualitatively different from normal humans or human companies?
**[01:18:35]** I guess I think I see it as like a progression of automation in society, right?
**[01:18:39]** And again, like it's trapping the trend of computing.
**[01:18:41]** I just feel like there will be a gradual automation of a lot of things, and superintelligence
**[01:18:44]** will be sort of like the extrapolation of that.
**[01:18:47]** So I do think we expect more and more autonomous entities over time that are doing a lot of
**[01:18:50]** the digital work, and then eventually even the physical work, probably some amount of
**[01:18:54]** time later.
**[01:18:55]** But basically, I see it as just automation, roughly speaking.
**[01:19:00]** I guess automation includes the things humans can already do, and superintelligence supplies
**[01:19:03]** things humans...
**[01:19:04]** Well, but some of the things that people do is invent new things, which I would just put
**[01:19:08]** into the automation, if that makes sense.
**[01:19:10]** Yeah.
**[01:19:11]** But I guess maybe less abstractly and more sort of like qualitatively, do you expect
**[01:19:18]** something to feel like, okay, this, because this thing can either think so fast, or has
**[01:19:24]** so many copies, or the copies can merge back in themselves, or is, quote unquote, much
**[01:19:30]** smarter, any number of advantages an AI might have, it will qualitatively...
**[01:19:36]** The civilization in which these AIs exist will just feel qualitatively different from
**[01:19:39]** human civilization.
**[01:19:40]** No, I think it will.
**[01:19:41]** I mean, it is fundamentally automation, but I mean, it will be like extremely foreign.
**[01:19:43]** I do think it will look really strange.
**[01:19:46]** Because like you mentioned, we can run all of this on a computer cluster, etc, and much
**[01:19:51]** faster and all this thing.
**[01:19:52]** Yeah.
**[01:19:53]** I mean, maybe some of the scenarios, for example, that I start to get nervous about, with respect
**[01:19:57]** to when the world looks like that, is this kind of like gradual loss of control and understanding
**[01:20:00]** of what's happening.
**[01:20:01]** And I think that's actually the most likely outcome probably, is that there will be a
**[01:20:04]** gradual loss of understanding of...
**[01:20:07]** And we'll gradually layer all this stuff everywhere, and there'll be fewer and fewer people who
**[01:20:10]** understand it, and that there will be a sort of this like scenario of a gradual loss of
**[01:20:14]** control and understanding of what's happening.
**[01:20:17]** That to me seems most likely outcome of how the stuff will go down.
**[01:20:20]** Let me probe on that a bit.
**[01:20:22]** It's not clear to me that loss of control and loss of understanding are the same things.
**[01:20:27]** A board of directors at like, whatever, TSMC, Intel, name a random company, they're just
**[01:20:35]** like prestigious 80-year-olds.
**[01:20:36]** They have very little understanding, and maybe they don't practically actually have control.
**[01:20:41]** Actually, maybe a better example is the President of the United States.
**[01:20:46]** President has a lot of fucking power.
**[01:20:47]** I'm not trying to make a good statement about the current operant, but maybe I am.
**[01:20:53]** But like, the actual level of understanding is very different from the level of control.
**[01:20:56]** Yeah.
**[01:20:57]** I think that's fair.
**[01:20:58]** That's a good pushback.
**[01:20:59]** I think like, I guess I expect loss of both.
**[01:21:02]** How come?
**[01:21:03]** I mean, loss of understanding is obvious, but why loss of control?
**[01:21:10]** So we're really far into a territory of, I don't know what this looks like, but if
**[01:21:14]** I was to write sci-fi novels, they would look along the lines of not even a single entity
**[01:21:19]** or something like that.
**[01:21:20]** So that just sort of like takes over everything, but actually like multiple competing entities
**[01:21:24]** that gradually become more and more autonomous, and some of them go rogue, and the others
**[01:21:29]** like fight them off and all this kind of stuff.
**[01:21:30]** And it's like this hot pot of completely autonomous activity that we've delegated to.
**[01:21:37]** I kind of feel like it would have that flavor.
**[01:21:41]** It is not the fact that they are smarter than us that is resulting in the loss of control.
**[01:21:45]** Not necessarily.
**[01:21:46]** It is the fact that they are competing with each other, and whatever arises out of that
**[01:21:51]** competition that leads to the loss of control.
**[01:21:56]** I mean, I basically expect there to be, I mean, a lot of these things, I mean, there
**[01:22:00]** will be tools to people, and the people could, some of the population is like, they're acting
**[01:22:04]** on behalf of people or something like that.
**[01:22:06]** So maybe those people are in control, but maybe it's a loss of control overall for society
**[01:22:09]** in the sense that of like outcomes we want or something like that, where you have entities
**[01:22:14]** acting on behalf of individuals that are still kind of roughly seen as out of control.
**[01:22:19]** Yeah, yeah.
**[01:22:20]** This is a question I should have asked earlier.
**[01:22:21]** So we were talking about how currently it feels like when you're doing AI engineering
**[01:22:25]** or AI research, these models are more like in the category of compiler rather than in
**[01:22:30]** the category of a replacement.
**[01:22:33]** At some point, if you have quote-unquote AGI, it should be able to do what you do.
**[01:22:36]** And do you feel like having a million copies of you in parallel results in some huge speed
**[01:22:41]** up of AI progress?
**[01:22:43]** Basically, if that does happen, do you expect to see an intelligence explosion?
**[01:22:47]** Or even once we have a true AGI, I'm not talking about LLMs today, but real AGI.
**[01:22:50]** I guess like what I mean is, I do, but it's business as usual, because we're in an intelligence
**[01:22:57]** explosion already and have been for decades.
**[01:22:58]** And when you look at GDP, it's basically the GDP curve.
**[01:23:01]** That is an exponential weighted sum over so many aspects of the industry.
**[01:23:05]** Everything is gradually being automated, has been for hundreds of years.
**[01:23:09]** Industrial Revolution is automation and some of the physical components and tool building
**[01:23:12]** and all this kind of stuff.
**[01:23:13]** Compilers are early software automation, etc.
**[01:23:16]** So I kind of feel like we've been recursively self-improving and exploding for a long time.
**[01:23:21]** Maybe another way to see it is, I mean, Earth was a pretty, I mean, if you don't look at
**[01:23:26]** the biomechanics and so on, it was a pretty boring place, I think, and looked very similar
**[01:23:29]** if you just look from space.
**[01:23:31]** And Earth is spinning.
**[01:23:32]** And then we're in the middle of this firecracker event, but we're seeing it in slow motion.
**[01:23:37]** But I definitely feel like this has already happened for a very long time.
**[01:23:42]** And again, I don't see AI as a distinct technology with respect to what has already been happening
**[01:23:47]** for a long time.
**[01:23:48]** So you think it's going to continue with this hyper exponential trend?
**[01:23:52]** And that's why, like, this was very interesting to me because I was trying to find AI in the
**[01:23:56]** GDP for a while.
**[01:23:57]** I thought the GDP should go up.
**[01:23:59]** But then I looked at some of the other technologies that I thought were very transformative, like
**[01:24:04]** maybe computers or mobile phones or etc.
**[01:24:06]** You can't find them in GDP.
**[01:24:07]** GDP is the same exponential.
**[01:24:09]** And it's just that even, for example, the early iPhone didn't have the App Store and
**[01:24:12]** it didn't have a lot of the bells and whistles that the modern iPhone has.
**[01:24:15]** And so even though we think of 2008, was it, when iPhone came out as like some major seismic
**[01:24:20]** change, it's actually not.
**[01:24:21]** Everything is like so spread out and so slowly diffuses that everything ends up being averaged
**[01:24:25]** up into the same exponential.
**[01:24:26]** And it's the exact same thing with computers, you can't find them in the GDP is like, oh,
**[01:24:30]** we have computers now.
**[01:24:31]** That's not what happened because it's such slow progression.
**[01:24:33]** And with AI, we're going to see the exact same thing.
**[01:24:35]** It's just more automation.
**[01:24:36]** It allows us to write different kinds of programs that we couldn't write before.
**[01:24:39]** But AI is still fundamentally a program.
**[01:24:42]** And it's a new kind of computer and a new kind of computing system.
**[01:24:47]** But it has all these problems, it's going to diffuse over time, and it's still going
**[01:24:50]** to add up to the same exponential, and we're still going to get an exponential that's going
**[01:24:53]** to get extremely vertical, and it's going to be very foreign to live in that kind of
**[01:24:58]** an environment.
**[01:24:59]** Are you saying that like, what will happen is if you go, if you look at the trend before
**[01:25:03]** the Industrial Revolution to currently, you have a hyper exponential where you go from
**[01:25:07]** like 0% growth to then 10,000 years ago, 0.02% growth, and then currently we're at 2% growth.
**[01:25:14]** So that's a hyper exponential.
**[01:25:15]** And you're saying, if you're charting AI on there, then it's like AI takes you to 20%
**[01:25:18]** growth or 200% growth.
**[01:25:20]** Or you could be saying, if you look at the last 300 years, what you've been seeing is
**[01:25:23]** you have technology after technology, computers, electrification, steam, steam engines, railways,
**[01:25:29]** etc.
**[01:25:30]** But the rate of growth is the exact same, it's 2%.
**[01:25:33]** So are you saying the rate of growth will go hyper?
**[01:25:35]** No, basically, I expect this, the rate of growth has also stayed roughly constant, right?
**[01:25:39]** For only the last 200, 300 years, but over the course of human history, it's like exploded,
**[01:25:44]** right?
**[01:25:45]** It's like gone from like 0%, basically, to like, faster, faster, faster industrial explosion,
**[01:25:48]** 2%.
**[01:25:50]** So basically, I guess what I'm saying is, for a while, I tried to find AI or look for
**[01:25:53]** AI in like the GDP curve, and I kind of convinced myself that this is false.
**[01:25:56]** And that even when people talk about recursive self-improvement and labs and stuff like that,
**[01:25:59]** I even don't, this is business as usual, of course, it's going to recursively self-improve,
**[01:26:03]** and it's been recursively self-improving, like LLMs allow the engineers to work much
**[01:26:07]** more efficiently to build the next round of LLM, and a lot more of the components are
**[01:26:12]** being automated and tuned, etc.
**[01:26:14]** So all the engineers having access to Google search is sort of part of it, all the engineers
**[01:26:19]** having an ID, all of them have an autocomplete or having cloth code, etc.
**[01:26:23]** It's all just part of the same speed up of the whole thing.
**[01:26:26]** So it's just so smooth.
**[01:26:29]** But just to clarify, you're saying that the rate of growth will not change.
**[01:26:34]** Like, you know, the intelligence explosion will show up as like, it just enabled us to
**[01:26:38]** continue staying on the 2% growth trajectory, just as the internet helped us stay on 2%
**[01:26:41]** growth trajectory.
**[01:26:42]** Yeah, my expectation is that it stays the same pattern.
**[01:26:45]** I mean, just to throw the opposite argument against you, my expectation is that it like,
**[01:26:53]** blows up because I think true AGI, and I'm not talking about LLM coding bots, I'm talking
**[01:26:58]** about like actual, this is like a replacement of a human in a server, is qualitatively different
**[01:27:04]** from these other productivity improving technologies, because it's labor itself, right?
**[01:27:11]** I think we live in a very labor constrained world.
**[01:27:12]** If you talk to any startup founder, or any person, you can just be like, okay, what do
**[01:27:16]** you need more of?
**[01:27:17]** You just like need really talented people.
**[01:27:19]** And if you just have billions of extra people who are inventing stuff, integrating themselves,
**[01:27:24]** making companies bottoms start to finish, that feels qualitatively different from just
**[01:27:28]** like, a single technology, it's just sort of like just asking if you get 10 billion
**[01:27:32]** extra people on the planet.
**[01:27:33]** I mean, maybe a counterpoint.
**[01:27:34]** I mean, number one, I'm actually pretty, pretty willing to be convinced one way or another
**[01:27:39]** on this point.
**[01:27:40]** I would say, for example, computing is labor.
**[01:27:42]** Computing was labor.
**[01:27:43]** Computers, like a lot of jobs disappears because computers are automating a bunch of digital
**[01:27:47]** information processing that you now don't need a human for.
**[01:27:50]** And so computers are labor.
**[01:27:52]** And that has played out.
**[01:27:55]** And you know, self driving, as an example, is also like computers doing labor.
**[01:27:58]** So like, I guess it's already been playing out to still business as usual.
**[01:28:02]** Yeah.
**[01:28:03]** I guess you have a machine which is spitting out more things like that, at potentially
**[01:28:06]** faster pace.
**[01:28:07]** And so we historically, we have examples of the growth regime changing, where like
**[01:28:11]** you went from, you know, point 2% growth to 2% growth.
**[01:28:14]** So it seems very plausible to me that like, a machine which is then spitting out the next
**[01:28:21]** self driving car and the next internet and whatever.
**[01:28:23]** I mean, I kind of, yeah, I see where it's coming from.
**[01:28:26]** At the same time, I do feel like people make this assumption of like, okay, we have God
**[01:28:30]** in the box, and now it can do everything.
**[01:28:32]** And it's just, it just won't look like that.
**[01:28:34]** It's going to be, it's going to be able to do some of the things, it's going to fail
**[01:28:36]** at some other things, it's going to be gradually put into society.
**[01:28:39]** And basically, we'll end up with the same pattern is my prediction.
**[01:28:41]** Yeah.
**[01:28:42]** Because, because this assumption of suddenly having a completely intelligent, fully flexible,
**[01:28:46]** fully general human in a box, and we can dispense it arbitrary problems in society, I don't
**[01:28:52]** think that we will have this, like discrete change.
**[01:28:56]** And so I think we'll arrive at the same, at the same kind of gradual diffusion of this
**[01:29:02]** across the industry.
**[01:29:03]** I think what often ends up being misleading in these conversations is people that I don't
**[01:29:09]** like to use the word intelligence in this context, because intelligence implies you
**[01:29:12]** think like, oh, super, super intelligence will be sitting, there'll be a single super
**[01:29:16]** intelligence sitting in a server, I know, like divine how to come up with new technologies
**[01:29:20]** and inventions that causes this explosion.
**[01:29:22]** And that's not what I'm imagining when I'm imagining 20% growth.
**[01:29:25]** I'm imagining that there's billions of, you know, basically, like, very smart human like
**[01:29:32]** minds, potentially, or that's all that's required.
**[01:29:34]** But the fact that there's hundreds of millions of them, billions of them, each individually,
**[01:29:40]** making new products, figuring out how to integrate themselves into the economy, just the way
**[01:29:44]** if like a highly experienced, smart immigrant came to the country, you wouldn't need to
**[01:29:47]** like figure out how we integrate them in the economy, they figure it out, they could start
**[01:29:49]** a company, they could like, make inventions, you know, or like just increase productivity
**[01:29:54]** in the world.
**[01:29:55]** And we have examples, even in the current regime of places that have had 10 20% economic
**[01:30:00]** growth.
**[01:30:01]** You know, if you just have a lot of people and less capital in comparison to the people,
**[01:30:05]** you can have Hong Kong or Shenzhen or whatever just had decades of 10% plus growth.
**[01:30:12]** And I think it's just like, there's a lot of really smart people who are ready to like
**[01:30:15]** make use of the resources and do this like period of catch up because we've had this
**[01:30:19]** discontinuity.
**[01:30:21]** And I think, yeah, maybe similar.
**[01:30:22]** So I think, I think I understand, but I still think that you're presupposing some discrete
**[01:30:27]** jump.
**[01:30:28]** There's some unlock that we're waiting to claim.
**[01:30:30]** And suddenly we're going to have geniuses in data centers.
**[01:30:33]** And I still think you're presupposing some discrete jump that I think has basically no
**[01:30:37]** historical precedent that I can't find in any of the statistics and that I think probably
**[01:30:41]** won't happen.
**[01:30:42]** I mean, the Industrial Revolution is such a jump, right?
**[01:30:43]** You went from like 0% growth or 0.2% growth to 2% growth.
**[01:30:47]** I'm just saying like, you'll see another jump like that.
**[01:30:49]** I'm a little bit suspicious.
**[01:30:50]** I would have to look at it.
**[01:30:51]** I'm a little bit suspicious and I would have to take a look.
**[01:30:53]** For example, like maybe the some of the logs are not very good from before the Industrial
**[01:30:57]** Revolution or something like that.
**[01:30:59]** So I'm a little bit suspicious of it.
**[01:31:01]** But yeah, maybe you're right.
**[01:31:02]** I don't, I don't have strong opinions.
**[01:31:04]** Maybe you're saying that this was a singular event that was extremely magical.
**[01:31:07]** And you're saying that maybe there's going to be another event that's going to be just
**[01:31:09]** like that, extremely magical, it will break paradigm, and so on.
**[01:31:12]** I actually don't think, I mean, the crucial thing with the Industrial Revolution was that
**[01:31:15]** it was not magical, right?
**[01:31:18]** If you just zoomed in, what you would see in 1770 or 1870 is not that there was some
**[01:31:26]** key invention.
**[01:31:27]** Yeah, exactly.
**[01:31:28]** But at the same time, you did move the economy to a regime where the progress was much faster
**[01:31:34]** and the exponential 10x.
**[01:31:36]** And I expect a similar thing from AI, where it's not like there's going to be a single
**[01:31:39]** moment where we've made the crucial invention.
**[01:31:42]** There's still some overhang that's being unlocked, like maybe there's a new energy source, there's
**[01:31:46]** some unlock, in this case, some kind of a cognitive capacity, and there's an overhang
**[01:31:49]** of cognitive work to do.
**[01:31:51]** That's right.
**[01:31:52]** And you're expecting that overhang to be filled by this new technology when it crosses the
**[01:31:55]** threshold.
**[01:31:56]** Yeah.
**[01:31:57]** And I mean, maybe one way to think about it is through history, a lot of growth, I mean,
**[01:32:01]** growth comes because people come up with ideas, and then people are like, out there doing
**[01:32:05]** stuff to execute those ideas and make valuable output.
**[01:32:09]** And through most of this time, population isn't exploding.
**[01:32:11]** That has been driving growth.
**[01:32:13]** For the last 50 years, people have argued that growth is stagnated.
**[01:32:16]** Population in frontier countries is also stagnated.
**[01:32:18]** I think we go back on the hyper-exponential growth in population and output.
**[01:32:22]** Sorry, exponential growth in population that causes hyper-exponential growth and output.
**[01:32:26]** Yeah.
**[01:32:27]** I mean, yeah, it's really hard to tell.
**[01:32:30]** I understand that viewpoint.
**[01:32:31]** I don't intuitively feel that viewpoint.
**[01:32:34]** So we just got access to Google's VO 3.1.
**[01:32:38]** And it's been really cool to play around with.
**[01:32:40]** The first thing we did was run a bunch of prompts through both VO 3 and 3.1 to see what's
**[01:32:46]** changing in the new version.
**[01:32:47]** So here's VO 3.
**[01:32:49]** Hi, I'm Max, and I got stuck in a local minimum again.
**[01:32:53]** It's okay, Max.
**[01:32:54]** We've all been there.
**[01:32:55]** It took me three epochs to get out.
**[01:32:57]** And here's VO 3.1.
**[01:32:59]** Hi, I'm Max, and I got stuck in a local minimum again.
**[01:33:03]** It's okay, Max.
**[01:33:04]** We've all been there.
**[01:33:05]** It took me three epochs to get out.
**[01:33:07]** 3.1's output is just consistently more coherent, and the audio is noticeably higher quality.
**[01:33:12]** We've been using VO for a while now, actually.
**[01:33:14]** We released an essay earlier this year about AI firms fully animated by VO 2.
**[01:33:19]** And it's been amazing to see how fast these models are improving.
**[01:33:23]** This update makes VO even more useful in terms of animating our ideas and our explainers.
**[01:33:29]** You can try VO right now in the Gemini app with pro and ultra subscriptions.
**[01:33:34]** You can also access it through the Gemini API or through Google Flow.
**[01:33:38]** You recommended Nick Lane's book to me, and then on that basis, I also found it super
**[01:33:42]** interesting and I interviewed him.
**[01:33:44]** And so I actually have some questions about sort of thinking about intelligence and evolutionary
**[01:33:47]** history.
**[01:33:48]** Now that you, over the last 20 years of doing AI research, you maybe have a more tangible
**[01:33:53]** sense of what intelligence is, what it takes to develop it.
**[01:33:58]** Are you more or less surprised as a result that evolution just sort of spontaneously
**[01:34:04]** stumbled upon it?
**[01:34:08]** I love Nick Lane's books, by the way.
**[01:34:11]** I was just listening to his podcast on the way up here.
**[01:34:14]** With respect to intelligence and its evolution, I do claim it came fairly, I mean, it's very,
**[01:34:18]** very recent.
**[01:34:19]** Right?
**[01:34:20]** I am surprised that it evolved.
**[01:34:22]** Yeah.
**[01:34:23]** I find it fascinating to think about all the worlds out there, like say there's a thousand
**[01:34:25]** planets like Earth and what they look like.
**[01:34:27]** I think Nick Lane was here talking about some of the early parts, right?
**[01:34:29]** Yeah.
**[01:34:30]** Like, okay, he expects basically very similar life forms, roughly speaking, and bacteria-like
**[01:34:34]** things in most of them.
**[01:34:36]** Yeah.
**[01:34:37]** And then there's a few breaks in there.
**[01:34:38]** I would expect that the evolution of intelligence intuitively feels to me like it should be
**[01:34:42]** fairly rare event.
**[01:34:44]** And there have been animals for, I guess maybe you should base it on how long something has
**[01:34:48]** existed.
**[01:34:49]** So, for example, if bacteria have been around for 2 billion years and nothing happened,
**[01:34:51]** then going to eukaryotes is probably pretty hard because bacteria actually came up quite
**[01:34:57]** early in Earth's evolution or history.
**[01:35:01]** And so, I guess, how long have we had animals?
**[01:35:03]** Maybe a couple hundred million years, like multicellular animals that like run, run,
**[01:35:07]** crawl, etc., which is maybe 10% of Earth's lifespan or something like that.
**[01:35:12]** So, I mean, maybe on that timescale, it's actually not too tricky.
**[01:35:15]** I still feel like it's still surprising to me, I think intuitively, that it developed.
**[01:35:20]** I would maybe expect just a lot of like animal-like life forms doing animal-like things.
**[01:35:24]** But the fact that you can get something that creates culture and knowledge and accumulates
**[01:35:28]** it, it is surprising to me.
**[01:35:30]** Okay.
**[01:35:31]** So, there's actually a couple of interesting follow-ups.
**[01:35:35]** If you buy the sun perspective, that actually the crux of intelligence is animal intelligence.
**[01:35:41]** What the courtesy said is if you got to the squirrel, you'd be most of the way to AGI.
**[01:35:46]** Then we got to squirrel intelligence, I guess, right after the Cambrian explosion 600 million
**[01:35:50]** years ago.
**[01:35:51]** It seems like what instigated that was the oxygenation event 600 million years ago.
**[01:35:55]** But immediately, the sort of like intelligence algorithm was there to like make the squirrel
**[01:36:00]** intelligence.
**[01:36:01]** Right?
**[01:36:02]** So, it's suggestive that animal intelligence was like that.
**[01:36:06]** As soon as you had the oxygen in the environment, you had the eukaryote, you could just like
**[01:36:09]** get the algorithm.
**[01:36:12]** Maybe there was like sort of an accident that evolution smelled upon it so fast.
**[01:36:15]** But I don't know if that suggests it's like actually quite, at the end, going to be quite
**[01:36:19]** simple.
**[01:36:20]** Yeah, it's basically so hard to tell, right, with any of this stuff.
**[01:36:22]** I guess you can base it a little bit on how long something has existed or how long it
**[01:36:26]** feels like something has been bottlenecked.
**[01:36:28]** So Nick Lane is very good about describing this like very apparent bottleneck in bacteria
**[01:36:32]** and archaea for 2 billion years, nothing happened, like extreme diversity of chemical biochemistry,
**[01:36:37]** and yet nothing that grows to become animals, 2 billion years.
**[01:36:43]** I don't know that we've seen exactly that kind of an equivalent with animals and intelligence,
**[01:36:48]** to your point, right?
**[01:36:49]** I guess maybe we could also look at it with respect to how many times we think evolution
**[01:36:52]** or intelligence has like individually sprung up.
**[01:36:55]** That's a really good thing to investigate.
**[01:36:58]** Maybe one thought on that is, I almost feel like, well, there's the hominid intelligence
**[01:37:03]** and there's, I would say, like the bird intelligence, right?
**[01:37:06]** Like ravens, etc. are extremely clever, but they actually, their brain parts are actually
**[01:37:09]** quite distinct and we don't have that much existence.
**[01:37:13]** So maybe that's a slight event of, there's a slight indication of maybe intelligence
**[01:37:17]** springing up a few times.
**[01:37:18]** And so in that case, you'd maybe expect it more frequently or something like that.
**[01:37:21]** Yeah.
**[01:37:22]** A former guest, Gwern, and also Carl Schulman, have made a really interesting point about
**[01:37:27]** that, which is their perspective is that the scalable algorithm which humans have and primates
**[01:37:33]** have arose in birds as well, and maybe other times as well.
**[01:37:39]** But humans found a evolutionary niche, which rewarded marginal increases in intelligence.
**[01:37:47]** And also had a scalable brain algorithm that could achieve those increases in intelligence.
**[01:37:52]** And so, for example, if a bird had a bigger brain, it would just like collapse out of
**[01:37:56]** the air.
**[01:37:57]** So it's very smart for the size of its brain, but it's like, it's not in a niche which rewards
**[01:38:01]** the brain getting bigger.
**[01:38:03]** Yeah.
**[01:38:04]** Maybe similar with some really smart-
**[01:38:05]** Like dolphins, etc.
**[01:38:07]** Exactly.
**[01:38:08]** Yeah.
**[01:38:09]** Whereas humans, you know, like we have hands that like reward being able to learn how to
**[01:38:11]** do tool use, we can externalize digestion, more energy to the brain, and that kicks off
**[01:38:16]** the flywheel.
**[01:38:18]** Yeah.
**[01:38:19]** And just stuff to work with.
**[01:38:20]** I mean, I'm guessing it would be harder to, if I was a dolphin, I mean, how do you do,
**[01:38:23]** you can't have fire, for example, and stuff like that.
**[01:38:25]** I mean, they're probably like the universe of things you can do in water, like inside
**[01:38:29]** water is probably lower than what you can do on land.
**[01:38:32]** Just chemically.
**[01:38:33]** Right.
**[01:38:34]** Yeah.
**[01:38:35]** I do agree with this, with this viewpoint of these niches and what's being incentivized.
**[01:38:37]** I still find it kind of miraculous that, I don't, I would have maybe expected things
**[01:38:42]** to get stuck on like animals with bigger muscles, you know.
**[01:38:47]** But like going through intelligence is actually a really fascinating breaking point.
**[01:38:51]** The way Burnford it is, the reason it was so hard is, there is a very tight line between
**[01:38:55]** being in a situation where something is so important to learn that it's not just worth
**[01:39:01]** distilling the exact right circuits directly back into your DNA, versus it's not important
**[01:39:08]** enough to learn at all.
**[01:39:09]** Yeah.
**[01:39:10]** It has to be something which is like, you have to incentivize building the algorithm
**[01:39:15]** to learn in lifetime.
**[01:39:16]** Yeah, exactly.
**[01:39:17]** You have to incentivize some kind of adaptability.
**[01:39:19]** You actually want something that, you actually want environments that are unpredictable.
**[01:39:21]** So evolution can't bake your algorithms into your weights.
**[01:39:24]** A lot of, a lot of animals are basically pre-baked in this sense.
**[01:39:28]** And so humans have to figure it out at test time when they get born.
**[01:39:31]** And so maybe there was, you actually want these kinds of environments that actually
**[01:39:35]** change really rapidly or something like that, where you can't foresee what will work well.
**[01:39:40]** And so you actually put all that intelligence, you create intelligence to figure it out at
**[01:39:43]** test time.
**[01:39:45]** So Quentin Pope had this interesting blog post where he was saying, the reason he doesn't
**[01:39:48]** expect a sharp takeoff is, so humans had the sharp takeoff where 60,000 years ago, we seem
**[01:39:55]** to have had the kind of architectures that we have today.
**[01:39:58]** And 10,000 years ago, agricultural revolution, modernity, dot, dot, dot.
**[01:40:02]** What was happening in that 50,000 years?
**[01:40:04]** Well, you had to build this sort of like cultural scaffold where you can accumulate knowledge
**[01:40:09]** over generations.
**[01:40:11]** This is an ability that exists for free in the way we do AI training, where if you retrain
**[01:40:17]** a model, it can still, I mean, in many cases are literally distilled, but they can be trained
**[01:40:21]** on each other.
**[01:40:22]** They can be trained on the same pre-training corpus.
**[01:40:25]** They don't literally have to start from scratch.
**[01:40:27]** So there's a sense in which the thing which, it took humans a long time to get this cultural
**[01:40:32]** loop going, just comes for free with the way we do LLM training.
**[01:40:36]** Yes and no, because LLMs don't really have the equivalent of culture.
**[01:40:39]** Maybe we're giving them way too much and incentivizing not to create it or something
**[01:40:42]** like that.
**[01:40:43]** But I guess like the emotion of culture and of written record and of like passing down
**[01:40:46]** notes between each other, I don't think there's an equivalent of that with LLMs right now.
**[01:40:50]** So LLMs don't really have culture right now.
**[01:40:53]** And that's kind of like one of the, I think, impediments, I would say.
**[01:40:56]** Can you give me some sense of what LLM culture might look like?
**[01:41:00]** So in the simplest case, it would be a giant scratchpad that the LLM can edit.
**[01:41:04]** And as it's reading stuff or as it's helping out with work, it's editing the scratchpad
**[01:41:07]** for itself.
**[01:41:08]** Why can't an LLM write a book for the other LLMs?
**[01:41:11]** That would be cool.
**[01:41:12]** Yeah.
**[01:41:13]** Like why can't other LLMs read this LLMs book and be inspired by it or shocked by it
**[01:41:18]** or something like that?
**[01:41:19]** There's no equivalence for any of this stuff.
**[01:41:20]** Interesting.
**[01:41:21]** When would you expect that kind of thing to start happening?
**[01:41:23]** And more general question about like multi-agent systems and a sort of like independent AI
**[01:41:29]** civilization and culture.
**[01:41:30]** I think there's two powerful ideas in the realm of multi-agent that have both not been
**[01:41:34]** like really claimed or so on.
**[01:41:36]** The first one I would say is culture and LLMs basically a growing repertoire of knowledge
**[01:41:42]** for their own purposes.
**[01:41:44]** The second one looks a lot more like the powerful idea of self-play in my mind is extremely
**[01:41:48]** powerful.
**[01:41:49]** So evolution actually is a lot of competition basically driving intelligence and evolution.
**[01:41:57]** And in AlphaGo, more algorithmically, like AlphaGo is playing against itself and that's
**[01:42:01]** how it learns to get really good at Go.
**[01:42:03]** And there's no equivalent of self-play in LLMs.
**[01:42:05]** But I would expect that to also exist, but no one has done it yet.
**[01:42:08]** Like why can't an LLM, for example, create a bunch of problems that another LLM is learning
**[01:42:12]** to solve?
**[01:42:13]** And then the LLM is always trying to like serve more and more difficult problems, stuff
**[01:42:17]** like that, you know?
**[01:42:18]** So like I think there's a bunch of ways to actually organize it.
**[01:42:21]** And I think it's a realm of research.
**[01:42:23]** But I think I haven't seen anything that convincingly like claims both of those like multi-agent
**[01:42:28]** improvements.
**[01:42:29]** I still think we're mostly in the realm of a single individual agent.
**[01:42:32]** But I also think that will change.
**[01:42:35]** And in the realm of culture also, I would bucket also organizations.
**[01:42:39]** And we haven't seen anything like that convincingly either.
**[01:42:42]** So that's why we're still early.
**[01:42:44]** And can you identify the key bottleneck that's preventing this kind of collaboration between
**[01:42:49]** LLMs?
**[01:42:50]** Maybe like the way I would put it is somehow remarkably, again, some of these analogies
**[01:42:55]** work and they shouldn't, but somehow remarkably they do.
**[01:42:57]** A lot of the smaller models somehow remarkably resemble like a kindergarten student or then
**[01:43:04]** like an elementary school student or high school student, etc.
**[01:43:07]** And somehow we still haven't graduated enough where this stuff can take over.
**[01:43:10]** Like it's still mostly like my cloth code or codex, they still kind of feel like this
**[01:43:15]** elementary grade student.
**[01:43:17]** I know that they can take PhD quizzes, but they still cognitively feel like a kindergarten
**[01:43:21]** or an elementary school student.
**[01:43:23]** So I don't think they can create culture because they're still kids, you know, like they're
**[01:43:27]** savant kids.
**[01:43:29]** They have perfect memory of all this stuff, etc.
**[01:43:33]** And they can convincingly create all kinds of slop that looks really good.
**[01:43:36]** But I still think they don't really know what they're doing and they don't really have the
**[01:43:38]** cognition across all these little checkboxes that we still have to collect.
**[01:43:43]** Yeah.
**[01:43:44]** So you've talked about how you were at Tesla leading self-driving from 2017 to 2022.
**[01:43:50]** And then you firsthand saw this progress from we went from cool demos to now thousands
**[01:43:57]** of cars out there actually autonomously doing drives.
**[01:43:59]** Why did that take a decade?
**[01:44:00]** Like what was happening through that time?
**[01:44:02]** Yeah.
**[01:44:03]** So I would say one thing I will almost instantly also push back on is this is not even near
**[01:44:08]** done.
**[01:44:10]** So in a bunch of ways that I'm going to get to, I do think that self-driving is very interesting
**[01:44:14]** because it's definitely like where I get a lot of my intuitions because I've spent five
**[01:44:17]** years on it.
**[01:44:20]** And it has this entire history where actually the first demos of self-driving go all the
**[01:44:23]** way to 1980s.
**[01:44:25]** You can see a demo from CMU in 1986.
**[01:44:28]** There's a truck that's driving itself on roads.
**[01:44:31]** But OK, fast forward.
**[01:44:32]** I think when I was joining Tesla, I had a very early demo of a Waymo.
**[01:44:37]** And it basically gave me a perfect drive in 2014 or something like that.
**[01:44:43]** So perfect Waymo drive a decade ago, took us around Palo Alto and so on because I had
**[01:44:48]** a friend who worked there.
**[01:44:50]** And I thought it was like very close and then still took a long time.
**[01:44:53]** And I do think that for some kinds of tasks and jobs and so on, there's a very large demo
**[01:45:00]** to product gap where the demo is very easy, but the products are very hard.
**[01:45:05]** And it's especially the case in cases like self-driving where the cost of failure is
**[01:45:09]** too high.
**[01:45:10]** Right.
**[01:45:11]** Many industries, tasks and jobs maybe don't have that property.
**[01:45:14]** But when you do have that property, that definitely increases the timelines.
**[01:45:17]** I do think that, for example, in software engineering, I do actually think that that
**[01:45:21]** property does exist.
**[01:45:22]** I think for a lot of vibe coding, it doesn't.
**[01:45:24]** But I think if you're writing actual production grade code, I think that property should exist
**[01:45:27]** because any kind of mistake actually leads to security vulnerability or something like
**[01:45:31]** that.
**[01:45:32]** And millions and hundreds of millions of people's personal social security numbers, et cetera,
**[01:45:36]** get leaked or something like that.
**[01:45:37]** And so I do think that it is a case that in software, people should be careful.
**[01:45:42]** Kind of like in self-driving.
**[01:45:43]** Like in self-driving, if things go wrong, you might get injury.
**[01:45:48]** I guess there's worse outcomes.
**[01:45:49]** But I guess in software, I almost feel like it's almost unbounded how terrible some things
**[01:45:54]** could be.
**[01:45:55]** Interesting.
**[01:45:56]** So I do think that they share that property.
**[01:45:58]** And then I think basically what takes the long amount of time and the way to think about
**[01:46:01]** it is that it's a march of nines and every single nine is a constant amount of work.
**[01:46:08]** So every single nine is the same amount of work.
**[01:46:10]** So when you get a demo and something works 90% of the time, that's just the first nine.
**[01:46:16]** And then you need a second nine, a third nine, a fourth nine, a fifth nine.
**[01:46:18]** And while I was at Tesla for, was it five years or so, I think we went through maybe
**[01:46:21]** three nines or two nines.
**[01:46:23]** I don't know what it is.
**[01:46:24]** But like multiple nines of iteration, there's still more nines to go.
**[01:46:27]** And so that's why these things take so long.
**[01:46:31]** And so it's definitely formative for me, like seeing something that was a demo.
**[01:46:34]** I'm very unimpressed by demos.
**[01:46:37]** So whenever I see demos of anything, I'm extremely unimpressed by that.
**[01:46:41]** It works better if you can.
**[01:46:43]** If it's a demo that someone cooked up and is just showing you, it's worse.
**[01:46:46]** If you can interact with it, it's a bit better.
**[01:46:47]** But even then you're not done.
**[01:46:48]** You need actual product.
**[01:46:49]** It's going to face all these challenges when it comes in contact with reality and all these
**[01:46:53]** different pockets of behavior that need patching.
**[01:46:55]** And so I think we're going to see all this stuff play out.
**[01:46:57]** It's a march of nines.
**[01:46:58]** Each nine is constant.
**[01:47:00]** Demos are encouraging, still a huge amount of work to do.
**[01:47:03]** I do think it is a kind of a critical safety domain, unless you're doing bytecoding, which
**[01:47:08]** is all nice and fun and so on.
**[01:47:11]** And so that's why I think this also enforced my timelines from that perspective.
**[01:47:16]** That's very interesting to hear you say that the sort of safety guarantees you need from
**[01:47:20]** software are actually not dissimilar to self-driving.
**[01:47:23]** Because what people will often say is that self-driving took so long because the cost
**[01:47:27]** of failure is so high, like a human makes a mistake on average every 400,000 miles or
**[01:47:33]** every seven years.
**[01:47:34]** And if you had to release a coding agent that couldn't make a mistake for at least seven
**[01:47:38]** years, it would be much harder to deploy.
**[01:47:41]** But I guess your point is that if you made a catastrophic coding mistake, like breaking
**[01:47:45]** some important system every seven years.
**[01:47:47]** It's very easy to do.
**[01:47:48]** And in fact, in terms of sort of wall clock time, it would be much less than seven years
**[01:47:52]** because you're like constantly outputting code like that, right?
**[01:47:55]** So like per tokens, or in terms of tokens, it would be seven years, but in terms of wall
**[01:47:59]** clock time, it would be pretty close.
**[01:48:00]** Yeah, in some ways it's a much harder problem.
**[01:48:01]** Because self-driving is just one of thousands of things that people do.
**[01:48:04]** It's almost like a single vertical, I suppose.
**[01:48:07]** Whereas when we're talking about general software engineering, it's even more, there's more
**[01:48:09]** surface area.
**[01:48:11]** There's another objection people make to that analogy, which is that with self-driving,
**[01:48:17]** what took a big fraction of that time was solving the problem of building basic, having
**[01:48:23]** basic perception that's robust and building representations and having a model that has
**[01:48:29]** some common sense.
**[01:48:30]** So it can generalize to when I see something that's slightly out of distribution.
**[01:48:34]** If somebody is waving down the road this way, you don't need to train for it.
**[01:48:38]** The thing will have some understanding of how to respond to something like that.
**[01:48:42]** And these are things we're getting for free with LLMs or VLMs today.
**[01:48:46]** So we don't have to solve these very basic representation problems.
**[01:48:49]** And so now deploying AIs across different domains will sort of be like deploying a self-driving
**[01:48:54]** car with current models to a different city, which is hard, but not like a 10 year long
**[01:48:57]** task.
**[01:48:59]** Yeah, basically, I'm not 100% sure if I fully agree with that.
**[01:49:01]** I don't know how much we're getting for free.
**[01:49:03]** And I still think there's a lot of gaps in understanding in what we are getting.
**[01:49:06]** I mean, we're definitely getting more generalizable intelligence in a single entity, whereas self-driving
**[01:49:12]** is a very special purpose task that requires, in some sense, building a special purpose
**[01:49:16]** task is maybe even harder in a certain sense, because it doesn't fall out from a more general
**[01:49:20]** thing that you're doing at scale, if that makes sense.
**[01:49:24]** But I still don't know if it fully resonates, because the LLMs are still pretty fallible,
**[01:49:30]** and I still think that they have a lot of gaps and that it still needs to be filled
**[01:49:33]** in.
**[01:49:34]** And I don't think that we're getting magical generalization completely out of the box in
**[01:49:38]** a certain sense.
**[01:49:39]** And the other aspect that I want to also actually return to when I was in the beginning was
**[01:49:44]** self-driving cars are newer and they're done still.
**[01:49:48]** So the deployments still are pretty minimal, right?
**[01:49:51]** So even Waymo and so on has very few cars, and they're doing that, roughly speaking,
**[01:49:54]** because they're not economical, right?
**[01:49:56]** Because they've built something that lives in the future.
**[01:50:00]** And so they had to pull back future, but they had to make it uneconomical.
**[01:50:03]** So they have all these like, you know, there's all these costs, not just marginal costs for
**[01:50:08]** those cars and their operation and maintenance, but also the capex of the entire thing.
**[01:50:13]** So making economical is still going to be a slog, I think, for them.
**[01:50:17]** And then also, I think when you look at these cars and there's no one driving, I also think
**[01:50:21]** it's a little bit deceiving because there are actually very elaborate teleoperation
**[01:50:25]** centers of people actually kind of like in a loop with these cars.
**[01:50:29]** And I don't have the full extent of it, but I think there's more human in the loop that
**[01:50:33]** you might expect.
**[01:50:34]** And there's people somewhere out there, basically beaming in from the sky.
**[01:50:38]** And I don't actually know they're fully in the loop with the driving.
**[01:50:41]** I think some of the times they are, but they're certainly involved and there are people.
**[01:50:44]** In some sense, we haven't actually removed the person.
**[01:50:46]** We've like moved them to somewhere where you can't see them.
**[01:50:48]** I still think there will be some work, as you mentioned, going from environment to environment.
**[01:50:51]** And so I think like there's still challenges to make self-driving real.
**[01:50:55]** But I do agree that it's definitely across the threshold where it kind of feels real,
**[01:50:59]** unless it's like really tele-operated.
**[01:51:02]** For example, Waymo can't go to all the different parts of the city.
**[01:51:05]** My suspicion is it's like parts of city where you don't get good signal.
**[01:51:08]** Anyway, so basically, I don't actually know anything about the stack.
**[01:51:12]** I mean, I'm just making up stuff.
**[01:51:14]** You let self-driving for five years at Tesla.
**[01:51:17]** Sorry, I don't know anything about the specifics of Waymo.
**[01:51:19]** I actually, by the way, love Waymo and I take it all the time.
**[01:51:23]** So I don't want to say like, sure.
**[01:51:24]** I just think that people again are sometimes a little bit too naive about some of the progress
**[01:51:29]** and I still think there's a huge amount of work.
**[01:51:31]** And I think Tesla took, in my mind, a lot more scalable approach.
**[01:51:34]** And I think the team is doing extremely well.
**[01:51:37]** And I'm kind of like on the record for predicting how this thing will go, which is like Waymo
**[01:51:41]** had like early start because you can package up so many sensors.
**[01:51:44]** But I do think Tesla is taking the more scalable strategy and it's going to look a lot more
**[01:51:47]** like that.
**[01:51:48]** So I think this will have to still play out and hasn't.
**[01:51:51]** But basically, like, I don't want to talk about self-driving as something that took
**[01:51:54]** a decade because it didn't take.
**[01:51:56]** It didn't take yet.
**[01:51:57]** If that makes sense.
**[01:51:58]** Because one, it's the start is at 1980, not 10 years ago, and then two, the end is not
**[01:52:04]** here yet.
**[01:52:05]** Yeah.
**[01:52:06]** The end is not near yet.
**[01:52:07]** Because when we're talking about self-driving, usually in my mind, it's self-driving at scale.
**[01:52:11]** People don't have to get a driver's license, etc.
**[01:52:13]** I'm curious to bounce two other ways in which the analogy might be different.
**[01:52:18]** And the reason I'm especially curious about this is because I think the question of how
**[01:52:22]** fast AI is deployed, how valuable it is when it's early on is like potentially the most
**[01:52:28]** important question in the world right now, right?
**[01:52:30]** Like if you're trying to model what the year 2030 looks like, this is the question you
**[01:52:33]** want to have some understanding of.
**[01:52:35]** So another thing you might think is, one, you have this latency requirement with self-driving
**[01:52:41]** where you have, I have no idea what the actual models are, but I assume like tens of millions
**[01:52:44]** of parameters or something, which is not the necessary constraint for knowledge work with
**[01:52:50]** LLMs.
**[01:52:51]** Or maybe it might be with a computer use and stuff.
**[01:52:52]** But anyways, the other big one is, maybe more importantly, on this CapEx question, yes,
**[01:53:00]** there is additional cost to serving up an additional copy of a model.
**[01:53:05]** But the sort of opex of a session is quite low, and you can amortize the cost of AI into
**[01:53:13]** the training run itself, depending on how inference scaling goes and stuff.
**[01:53:17]** But it's certainly not as much as like building a whole new car to serve another instance
**[01:53:22]** of a model.
**[01:53:23]** So it just, the economics of deploying more widely are much more favorable.
**[01:53:28]** I think that's right.
**[01:53:29]** If you're sticking in the realm of bits, bits are like a million times easier than anything
**[01:53:33]** that touches the physical world.
**[01:53:35]** I definitely grant that.
**[01:53:38]** Bits are completely changeable, arbitrarily reshufflable at a very rapid speed.
**[01:53:42]** So you would expect a lot more faster adaptation also in the industry and so on.
**[01:53:48]** And then what was the first one?
**[01:53:50]** The latency requirements.
**[01:53:51]** Oh, the latency requirements.
**[01:53:52]** And what are the implications for model size?
**[01:53:53]** I think that's roughly right.
**[01:53:54]** I mean, I also think that if we are talking about knowledge work at scale, there will
**[01:53:57]** be some latency requirements, practically speaking, because we're going to have to
**[01:54:01]** make, create a huge amount of compute and serve that.
**[01:54:05]** And then I think the last aspect that I very briefly want to also talk about is all the
**[01:54:09]** rest of it.
**[01:54:11]** Just all the rest of it.
**[01:54:12]** So what does society think about it?
**[01:54:14]** What is the legal, how is it working legally?
**[01:54:17]** How is it working insurance-wise?
**[01:54:18]** Who's really, what are those layers of it and aspects of it?
**[01:54:24]** What happens with, what is the equivalent of people putting a cone on a Waymo?
**[01:54:27]** There's going to be equivalence of all that.
**[01:54:30]** And so I do think that I almost feel like self-driving is a very nice analogy that you
**[01:54:35]** can borrow things from.
**[01:54:36]** Yeah.
**[01:54:37]** What is the equivalent of a cone on the car?
**[01:54:38]** What is the equivalent of a tele-operating worker who's like hidden away?
**[01:54:42]** And almost like all the aspects of it.
**[01:54:44]** Yeah.
**[01:54:45]** Do you have any opinions on whether this implies that the current day I build out, which would
**[01:54:50]** like 10x the amount of available computer in the world in a year or two, and maybe like
**[01:54:55]** 100, more than 100x by the end of the decade.
**[01:54:58]** If the use of AI will be lower than some people naively predict, does that mean that we're
**[01:55:03]** overbuilding compute?
**[01:55:05]** Or do you, is that a separate question?
**[01:55:07]** Kind of like what happened with railroads and all this kind of stuff.
**[01:55:09]** With what, sorry?
**[01:55:10]** Was it railroads?
**[01:55:11]** Oh, sorry.
**[01:55:12]** Yeah, that's right.
**[01:55:13]** Yeah.
**[01:55:14]** There is like historical precedent, or was it with telecommunication industry, right?
**[01:55:16]** Like prepaving the internet that only came like a decade later, you know, and creating
**[01:55:19]** like a whole bubble in the telecommunications industry in the late 90s kind of thing.
**[01:55:25]** Yeah.
**[01:55:26]** So I don't know.
**[01:55:27]** I mean, I understand I'm sounding very pessimistic here.
**[01:55:30]** I'm only doing that, I'm actually optimistic.
**[01:55:32]** I think this will work.
**[01:55:33]** I think it's tractable.
**[01:55:34]** I'm only sounding pessimistic because when I go on my Twitter timeline, I see all this
**[01:55:38]** stuff that makes no sense to me.
**[01:55:40]** And I think there's a lot of reasons for why that exists.
**[01:55:44]** And I think a lot of it is, I think, honestly, just fundraising.
**[01:55:47]** It's just incentive structures.
**[01:55:49]** A lot of it may be fundraising.
**[01:55:50]** A lot of it is just attention, you know, converting attention to money on the internet, you know,
**[01:55:55]** stuff like that.
**[01:55:58]** So I think there's a lot of that going on.
**[01:56:00]** And I think I'm only reacting to that, but I'm still like overall very bullish on technology.
**[01:56:05]** I think we're going to work through all this stuff.
**[01:56:07]** And I think there's been a rapid amount of progress.
**[01:56:09]** I don't actually know that there's overbuilding.
**[01:56:11]** I think that there's going to be, we're going to be able to gobble up what, in my understanding,
**[01:56:15]** is being built.
**[01:56:17]** Because I do think that, for example, Cloud Code or OpenAI Codex and stuff like that,
**[01:56:20]** they didn't even exist a year ago, right?
**[01:56:22]** Is that right?
**[01:56:23]** I think it's roughly right.
**[01:56:25]** This is miraculous technology that didn't exist.
**[01:56:26]** I think there's going to be a huge amount of demand as we see the demand in Chachapiti
**[01:56:31]** already and so on.
**[01:56:32]** So yeah, I don't actually know that there's overbuilding.
**[01:56:37]** But I guess I'm just reacting to like some of the very fast timelines that people continue
**[01:56:41]** to say incorrectly.
**[01:56:42]** And I've heard many, many times over the course of my 15 years in AI, where very reputable
**[01:56:46]** people keep getting this wrong all the time.
**[01:56:50]** And I think I want us to be properly calibrated.
**[01:56:53]** And I think some of this also, it does have like geopolitical ramifications and things
**[01:56:56]** like that when, like some of these questions.
**[01:56:59]** And I think I don't want people to make mistakes on that sphere of things.
**[01:57:03]** So I do want us to be grounded in reality of what technology is and isn't.
**[01:57:09]** Let's talk about education in Eureka and stuff.
**[01:57:11]** One thing you could do is start another AI lab and try to solve those problems.
**[01:57:18]** Yeah, curious what you're up to now.
**[01:57:21]** And then, yeah, why not AI research itself?
**[01:57:24]** I guess maybe like the way I would put it is, I feel some amount of like determinism
**[01:57:29]** around the things that AI labs are doing.
**[01:57:33]** And I feel like I could help out there.
**[01:57:34]** But I don't know that I would like uniquely improve it.
**[01:57:41]** But I think like my personal big fear is that a lot of this stuff happens on the side of
**[01:57:45]** humanity and that humanity gets disempowered by it.
**[01:57:48]** And I kind of like, I care not just about all the Dyson spheres that we're going to
**[01:57:53]** build and that AI is going to build in a fully autonomous way.
**[01:57:55]** I care about what happens to humans.
**[01:57:57]** And I want humans to be well off in this future.
**[01:58:00]** And I feel like that's where I can a lot more uniquely add value than like an incremental
**[01:58:04]** improvement in the Frontier Lab.
**[01:58:06]** And so, I guess I'm most afraid of something maybe like depicted in movies like WALL-E
**[01:58:11]** or Idiocracy or something like that, where humanity is sort of on the side of this stuff.
**[01:58:16]** And I want humans to be much, much better in this future.
**[01:58:20]** And so, I guess, to me, this is kind of like through education that you can actually achieve
**[01:58:24]** this.
**[01:58:25]** And so, what are you working on there?
**[01:58:27]** So, Eureka is trying to build, I think maybe the easiest way I can describe it is we're
**[01:58:30]** trying to build the Starfleet Academy.
**[01:58:33]** I don't know if you've watched Star Trek.
**[01:58:34]** I haven't.
**[01:58:35]** Okay.
**[01:58:36]** Yeah.
**[01:58:37]** Okay.
**[01:58:38]** Starfleet Academy is this like elite institution for frontier technology, building spaceships
**[01:58:41]** and graduating cadets to be like in the pilots of these spaceships and whatnot.
**[01:58:45]** So, I just imagine like an elite institution for technical knowledge and basically a kind
**[01:58:52]** of school that's very up-to-date and very like a premier institution.
**[01:58:56]** A category of questions I have for you is just explaining how one teaches technical
**[01:59:03]** or scientific content well, because you are one of the world masters at it.
**[01:59:08]** And then I'm curious both about how you think about it for content you've already put out
**[01:59:11]** there on YouTube.
**[01:59:12]** Yeah.
**[01:59:13]** But also, to the extent it's any different, how you think about it for Eureka?
**[01:59:15]** Yeah.
**[01:59:16]** With respect to Eureka, I think like one thing that is very fascinating to me about education
**[01:59:20]** is like I do think education will pretty fundamentally change with AIs on the side.
**[01:59:24]** And I think it has to be rewired and changed to some extent.
**[01:59:28]** I still think that we're pretty early.
**[01:59:30]** I think there's going to be a lot of people who are going to try to do the obvious things,
**[01:59:32]** which is like, oh, have an LLM and ask it questions and get, you know, do all the basic
**[01:59:37]** things that you would do via prompting right now.
**[01:59:39]** I think it's helpful, but it still feels to me a bit slop, like slop.
**[01:59:43]** I'd like to do it properly.
**[01:59:44]** And I think the capability is not there for what I would want.
**[01:59:46]** What I'd want is like an actual tutor experience.
**[01:59:51]** A prominent example in my mind is I was recently learning Korean, so language learning.
**[01:59:57]** And I went through a phase where I was learning Korean by myself on the internet.
**[02:00:00]** I went through a phase where I was actually part of a small class in Korea, taking a Korean
**[02:00:05]** with a bunch of other people, which was really funny.
**[02:00:06]** But we had a teacher and like 10 people or so taking Korean.
**[02:00:09]** And then I switched to a one-on-one tutor.
**[02:00:12]** And I guess what was fascinating to me is I think I had a really good tutor.
**[02:00:16]** But I mean, just thinking through like what this tutor was doing for me and how incredible
**[02:00:23]** that experience was and how high the bar is for like what I actually want to build eventually.
**[02:00:28]** Because I mean, she was extremely, so she instantly from a very short conversation understood
**[02:00:32]** like where I am as a student, what I know and don't know.
**[02:00:35]** And she was able to like probe exactly like the kinds of questions or things to understand
**[02:00:39]** my world model.
**[02:00:41]** No LLM will do that for you 100% right now, not even close, right?
**[02:00:44]** But a tutor will do that if they're good.
**[02:00:46]** Once she understands, she actually like really served me all the things that I needed at
**[02:00:50]** my current sliver of capability.
**[02:00:52]** I need to be always appropriately challenged.
**[02:00:54]** I can't be faced with something too hard or too trivial.
**[02:00:58]** And a tutor is really good at serving you just the right stuff.
**[02:01:00]** And so basically, I felt like I was the only constraint to learning like my own.
**[02:01:04]** I was the only constraint.
**[02:01:05]** I was always given the perfect information.
**[02:01:07]** I'm the only constraint.
**[02:01:08]** And I felt good because I'm the only impediment that exists.
**[02:01:11]** It's not that I can't find knowledge or there's not properly explained or etc.
**[02:01:13]** Like it's just my ability to memorize and so on.
**[02:01:16]** And this is what I want for people.
**[02:01:18]** How do you automate that?
**[02:01:20]** So very good question.
**[02:01:21]** At the current capability, you don't.
**[02:01:23]** But I do think that with as and that's why I think it's not actually the right time to
**[02:01:27]** actually build this kind of an AI tutor.
**[02:01:29]** I still think it's a useful product and lots of people will build it.
**[02:01:33]** But I still feel like the bar is so high and the capability is not there.
**[02:01:39]** But I mean, even today, I would say chargeability is an extremely valuable educational product.
**[02:01:45]** But I think for me, it was so fascinating to see how high the bar is.
**[02:01:48]** And when I was with her, I almost felt like there's no way I can build this.
**[02:01:51]** But you are building it, right?
**[02:01:54]** Anyone who's had a really good tutor is like, how are you going to build this?
**[02:01:59]** So I guess I'm waiting for that capability.
**[02:02:01]** I do think that in a lot of ways in the industry, for example, I did some AI consulting for
**[02:02:05]** computer vision.
**[02:02:07]** A lot of my times, the value that I brought to the company was telling them not to use
**[02:02:10]** AI.
**[02:02:11]** It wasn't like I was the AI expert and they described the problem.
**[02:02:13]** I said, don't use AI.
**[02:02:15]** This was my value add.
**[02:02:16]** And I feel like it's the same in education right now where I kind of feel like for what
**[02:02:21]** I have in mind, it's not yet the time.
**[02:02:22]** But the time will come.
**[02:02:24]** But for now, I'm building something that looks maybe a bit more conventional, that has a
**[02:02:28]** physical and digital component and so on.
**[02:02:30]** But I think there's obvious, it's obvious how this should look like in the future.
**[02:02:34]** Do you think you're willing to say what is the thing you hope will be released this year
**[02:02:39]** or next year?
**[02:02:40]** Well, so I'm building the first course, and I want to have a really, really good course.
**[02:02:45]** State of the art, obvious state of the art destination you go to learn AI in this case,
**[02:02:50]** because that's just what I'm familiar with.
**[02:02:51]** So I think it's a really good first product to get to be really good.
**[02:02:54]** And so that's what I'm building.
**[02:02:55]** And NanoChat, which you briefly mentioned, is a capstone project of LLM101N, which is
**[02:02:59]** a class that I'm building.
**[02:03:00]** So that's a really big piece of it.
**[02:03:03]** But now I have to build out a lot of the intermediates, and then I have to actually hire a small team
**[02:03:07]** of TAs and so on and actually build the entire course.
**[02:03:11]** And maybe one more thing that I would say is many times when people think about education,
**[02:03:15]** they think about sort of like the more, what I would say is like kind of a softer component
**[02:03:18]** of like diffusing knowledge or like, but I actually have something very hard and technical
**[02:03:23]** in mind.
**[02:03:24]** And so in my mind, education is kind of like the very difficult technical process of building
**[02:03:29]** ramps to knowledge.
**[02:03:31]** So in my mind, NanoChat is a ramp to knowledge, because it's a very simple, it's like the
**[02:03:35]** super simplified full stack thing.
**[02:03:38]** If you give this artifact to someone, and they like look through it, they're learning
**[02:03:41]** a ton of stuff.
**[02:03:42]** And so it's giving you a lot of what I call Eureka's per second, which is like understanding
**[02:03:47]** per second.
**[02:03:48]** What is it I want?
**[02:03:49]** Lots of Eureka's per second.
**[02:03:51]** And so to me, this is a technical problem of how do we build these ramps to knowledge.
**[02:03:54]** And so I always think of Eureka as almost like a, it's not like maybe that different,
**[02:03:59]** maybe through some of the frontier labs or some of the work that's going to be going
**[02:04:02]** on, because I want to figure out how to build these ramps very efficiently, so that people
**[02:04:07]** are never stuck.
**[02:04:09]** And everything is always not too hard or not too trivial, and you have just the right material
**[02:04:15]** to actually progress.
**[02:04:16]** Yeah, so you're imagining the short term that instead of a tutor being able to like probe
**[02:04:21]** your understanding, if you have enough self-awareness to be able to probe yourself, you're never
**[02:04:26]** going to be stuck.
**[02:04:27]** You can like find the right answer between talking to the TA or talking to an LLM and
**[02:04:31]** looking at the reference implementation.
**[02:04:33]** It sounds like automation or AI is actually not as significant, like, so far, it's actually
**[02:04:39]** The big alpha here is your ability to explain AI codified in the source material of the
**[02:04:48]** class, right?
**[02:04:49]** That's like fundamentally what the course is.
**[02:04:50]** I mean, I think you always have to be calibrated to what capability exists in the industry.
**[02:04:55]** And I think a lot of people are going to pursue like, oh, just ask Chachapiti, etc.
**[02:04:59]** But I think like right now, for example, if you go to Chachapiti and you say, oh, teach
**[02:05:02]** me AI, there's no way, it's going to give you some slop, right?
**[02:05:06]** Like AI is never going to write nano chat right now, but nano chat is a really useful,
**[02:05:10]** I think, intermediate point.
**[02:05:12]** So I still, I'm collaborating with AI to create all this material, so AI is still fundamentally
**[02:05:16]** very helpful.
**[02:05:18]** Earlier on, I built a CS231N at Stanford, which was one of the earlier, actually, sorry,
**[02:05:23]** I think it was the first deep learning class at Stanford, which became very popular.
**[02:05:27]** And the difference in building out 231N and LLM101N now is quite stark, because I feel
**[02:05:33]** really empowered by the LLMs as they exist right now, but I'm very much in the loop.
**[02:05:37]** So they're helping me build little materials, I go much faster, they're doing a lot of the
**[02:05:41]** boring stuff, etc.
**[02:05:43]** So I feel like I'm developing the course much faster, and those LLM infused in it, but it's
**[02:05:47]** not yet at a place where I can creatively create the content.
**[02:05:50]** I'm still there to do that.
**[02:05:51]** So like, I think the trickiness is always calibrating yourself to what exists.
**[02:05:55]** And so when you imagine what is available through Eureka in a couple of years, it seems
**[02:06:00]** like the big bottleneck is going to be finding Karpathis in field after field who can convert
**[02:06:06]** their understanding into these RAMs, right?
**[02:06:09]** So I think it would change over time.
**[02:06:10]** So I think right now, it would be hiring faculty to help work hand in hand with AI and a team
**[02:06:17]** of people probably, to build state of the art courses.
**[02:06:21]** And then I think over time, it can, maybe some of the TAs can actually become AIs.
**[02:06:24]** Because some of the TAs like, okay, you just take all the course materials, and then I
**[02:06:28]** think you could serve a very good automated TA for the student when they have more basic
**[02:06:33]** questions or something like that, right?
**[02:06:34]** But I think you'll need faculty for the overall architecture of a course, and making sure
**[02:06:39]** that it fits.
**[02:06:40]** And so I kind of see a progression of how this will evolve.
**[02:06:42]** And maybe at some future point, you know, I'm not even that useful and AI is doing most
**[02:06:45]** of the design much better than I could.
**[02:06:47]** But I still think that that's going to take some time to play out.
**[02:06:50]** But are you imagining that like, people who have expertise in other fields are then contributing
**[02:06:55]** courses?
**[02:06:56]** Or do you feel like it's actually quite essential to the vision that you, given your understanding
**[02:07:02]** of how you want to teach, are the one designing the content?
**[02:07:05]** Like, I don't know, Sal Khan is like narrating all the videos on Khan Academy.
**[02:07:09]** Are you imagining something like that?
**[02:07:10]** Or?
**[02:07:11]** Oh, no, I will hire faculty, I think, because there are domains in which I'm not an expert.
**[02:07:15]** And I think that's the only way to offer the state of the art experience for the student
**[02:07:19]** ultimately.
**[02:07:20]** So yeah, I do expect that I would hire faculty, but I will probably stick around in AI for
**[02:07:25]** some time.
**[02:07:27]** I do have something, I think, more conventional in mind for the current capability, I think,
**[02:07:31]** than what people would probably anticipate.
**[02:07:33]** And when I'm building Starfleet Academy, I do probably imagine a physical institution
**[02:07:37]** and maybe a tier below that, a digital offering that is not the state of the art experience
**[02:07:43]** you would get when someone comes in physically full time, and we work through material from
**[02:07:47]** start to end and make sure you understand it.
**[02:07:50]** That's the physical offering.
**[02:07:51]** Yeah.
**[02:07:52]** The digital offering is, yeah, a bunch of stuff on the internet and maybe some LLM assistant
**[02:07:55]** and it's a bit more gimmicky in a tier below, but at least it's accessible to like 8 billion
**[02:07:59]** people.
**[02:08:00]** Yeah, I think you're basically inventing college from first principles for the tools that are
**[02:08:08]** available today, and then just like for just like selecting for people who have the motivation
**[02:08:13]** and the interest of actually really engaging with material.
**[02:08:17]** Yeah.
**[02:08:18]** And I think there's gonna have to be a lot of not just education, but also re-education.
**[02:08:21]** And I would love to help out there because I think the jobs will probably change quite
**[02:08:25]** a bit.
**[02:08:26]** And so, for example, today, a lot of people are trying to upskill in AI specifically,
**[02:08:29]** so I think it's a really good course to teach in this respect.
**[02:08:33]** And yeah, I think the motivation-wise, before AGI, motivation is very simple to solve because
**[02:08:39]** people want to make money and this is how you make money in the industry today.
**[02:08:43]** I think post-AGI, it's a lot more interesting possibly because, yeah, if everything is automated
**[02:08:48]** and there's nothing to do for anyone, why would anyone go to a school, etc.
**[02:08:53]** So I think, I guess like I often say that pre-AGI education is useful, post-AGI education
**[02:08:59]** is fun.
**[02:09:01]** And in a similar way, as people, for example, people go to gym today, but we don't need
**[02:09:07]** their physical strength to manipulate heavy objects because we have machines to do that.
**[02:09:11]** They still go to gym.
**[02:09:12]** Why do they go to gym?
**[02:09:13]** Well, because it's fun, it's healthy, and you look hot when you have a six-pack.
**[02:09:17]** I don't know.
**[02:09:18]** Yeah.
**[02:09:19]** I guess like, so it's, I guess what I'm saying is it's attractive for people to do that in
**[02:09:24]** a certain like very deep psychological evolutionary sense for humanity.
**[02:09:29]** And so I kind of think that education will kind of play out in the same way, like you'll
**[02:09:32]** go to school, like you go to gym.
**[02:09:35]** And I think that right now, I think not that many people learn because learning is hard.
**[02:09:40]** You bounce from material because, and some people overcome that barrier, but for most
**[02:09:43]** people it's hard.
**[02:09:44]** Yeah.
**[02:09:45]** But I do think that we should, it's a technical problem to solve.
**[02:09:48]** It's a technical problem to do what my tutor did for me when I was learning Korean.
**[02:09:52]** I think it's tractable and buildable, and someone should build it.
**[02:09:54]** And I think it's going to make learning anything like trivial and desirable, and people will
**[02:09:58]** do it for fun because it's trivial.
**[02:10:00]** If I had a tutor like that for any arbitrary piece of like knowledge, I think it's gonna
**[02:10:04]** be so much easier to learn anything, and people will do it.
**[02:10:06]** And they'll do it for the same reasons they go to gym.
**[02:10:09]** That sounds different from using this, so post-AGI, you're using this to basically as
**[02:10:17]** entertainment or as like a self-betterment, but it sounded like you had a vision also
**[02:10:23]** that this education is relevant to keeping humanity in control of AI.
**[02:10:27]** I see.
**[02:10:28]** And they sound different.
**[02:10:29]** And I'm curious, is it like it's entertaining for some people, but then empowerment for
**[02:10:31]** some others?
**[02:10:32]** How do you think about that?
**[02:10:33]** I think this, so I do definitely feel like people will be, I do think like eventually
**[02:10:37]** it's a bit of a losing game, if that makes sense.
**[02:10:40]** I do think that it is in long term, long term, which I think is longer than I think maybe
**[02:10:45]** most people in the industry, it's a losing game.
**[02:10:47]** I do think that people can go so far, and that we barely scratched the surface of much
**[02:10:51]** a person can go.
**[02:10:53]** And that's just because people are bouncing off of material that's too easy or too hard.
**[02:10:57]** And I actually kind of feel that people will be able to go much further, like anyone speaks
**[02:11:01]** five languages, because why not, because it's so trivial.
**[02:11:05]** Everyone knows, you know, all the basic curriculum of undergrad, etc.
**[02:11:09]** Now that I'm understanding the vision.
**[02:11:12]** That's very interesting.
**[02:11:13]** Like, I think it actually has a perfect analog in gym culture.
**[02:11:17]** I don't think 100 years ago, anybody would be like ripped, like nobody would have, you
**[02:11:20]** know, be able to like just spontaneously bench two plays or three plays or something.
**[02:11:24]** It's actually very common now.
**[02:11:27]** And you're because this idea of systematically training and lifting weights in the gym or
**[02:11:31]** systematically training to be able to run a marathon, which is a capability spontaneously
**[02:11:35]** you would not have, or most humans would not have.
**[02:11:38]** And you're imagining similar things for learning across many different domains, which were
**[02:11:43]** intensely, deeply faster.
**[02:11:44]** Yeah, exactly.
**[02:11:45]** And I kind of feel like I am betting a little bit implicitly on some of the timelessness
**[02:11:49]** of human nature.
**[02:11:50]** And I think it will be desirable to do all these things.
**[02:11:58]** And I think people will look up to it as they have for millennia, because and I think
**[02:12:03]** this will continue to be true.
**[02:12:04]** And actually, also, maybe there's some evidence of that historically, because if you look
**[02:12:07]** at, for example, aristocrats, or you look at maybe ancient Greece or something like
**[02:12:11]** that, whenever you had little pocket environments that were post AGI, in a certain sense, I
**[02:12:14]** do feel like people have spent a lot of their time flourishing in a certain way, either
**[02:12:18]** physically or cognitively.
**[02:12:20]** And so I think I feel okay about the prospects of that.
**[02:12:24]** And I think if this is false, and I'm wrong, and we end up in like, you know, Wally or
**[02:12:29]** idiocracy future, then I think it's very, I don't even care if there's like Dyson spheres.
**[02:12:34]** This is terrible outcome.
**[02:12:36]** Yeah, like, I actually really do care about humanity, like, everyone has to just be superhuman
**[02:12:42]** in a certain sense.
**[02:12:43]** I guess it's still a world in which that is not enabling us to, it's like the culture
**[02:12:49]** world, right?
**[02:12:50]** I mean, are we all fundamentally going to be able to like, transform the trajectory
**[02:12:53]** of technology or influence decisions by your own labor or cognition alone?
**[02:13:00]** Maybe you can influence decisions because the AI is like for approval, but you're not
**[02:13:05]** like, it's not because I've like, I can, because I've invented something, or I like come up
**[02:13:09]** with a new design.
**[02:13:10]** I'm like really influencing the future.
**[02:13:11]** Yeah, maybe.
**[02:13:12]** I don't actually think that.
**[02:13:14]** I think there will be transitionary period where we are going to be able to be in the
**[02:13:17]** loop and advance things if we actually understand a lot of stuff.
**[02:13:21]** I do think that long term that probably goes away, right?
**[02:13:23]** But maybe it's going to even become a sport, like right now you have power lifters who
**[02:13:28]** go extreme on this direction.
**[02:13:30]** So what is power lifting in a cognitive era?
**[02:13:33]** Maybe it's people who are really trying to make Olympics out of knowing stuff.
**[02:13:39]** And if you have a perfect AI tutor, maybe you can get extremely far.
**[02:13:43]** I almost feel like we're just barely, the geniuses of today are barely scratching the
**[02:13:48]** surface of what a human mind can do, I think.
**[02:13:50]** I love this vision.
**[02:13:52]** I also, it's like, I feel like the person you have like most product market fit with
**[02:13:57]** is like me because like my job involves having to learn different subjects every week.
**[02:14:04]** And I am like very excited if you can.
**[02:14:08]** I'm similar for that matter.
**[02:14:09]** I mean, I, you know, a lot of people, for example, hate school and want to get out of
**[02:14:12]** it.
**[02:14:14]** I actually, I really liked school.
**[02:14:15]** I love learning things, etc.
**[02:14:16]** I wanted to stay in school.
**[02:14:17]** I stayed all the way until PhD, and then they wouldn't let me stay longer.
**[02:14:19]** So I went to the industry.
**[02:14:20]** But I mean, basically, it's roughly speaking, I love, I love learning, even for the sake
**[02:14:25]** of learning.
**[02:14:26]** But I also love learning because it's a form of empowerment and being useful and productive.
**[02:14:30]** I think you also made a point that was subtle, so just to spell it out.
**[02:14:34]** I think what's happened so far with online courses is that why haven't they already enabled
**[02:14:39]** us to enable every single human to know everything?
**[02:14:44]** And I think they're just so motivation laden, because there's not obvious on ramps, and
**[02:14:49]** it's like so easy to get stuck.
**[02:14:52]** And if you had, instead of this, this thing, basically, like a really good human tutor,
**[02:14:59]** it would just be such an unlock from a motivation perspective.
**[02:15:01]** I think so.
**[02:15:02]** Yeah, because it feels bad to bounce from material feels bad.
**[02:15:05]** It's a good negative reward from sinking amount of time in something and doesn't pan
**[02:15:10]** out or like being completely bored because what you're getting is too easy or too hard.
**[02:15:14]** So I think, yeah, I think when you actually do it properly, learning feels good.
**[02:15:18]** Yeah.
**[02:15:19]** And I think it's a technical problem to get there.
**[02:15:20]** And I think for a while, it's going to be AI plus human collab.
**[02:15:24]** And at some point, maybe it's just AI.
**[02:15:27]** Can I ask some questions about teaching?
**[02:15:28]** Well, if you had to like sort of like give advice to another educator in another field
**[02:15:33]** that you're curious about to make the kinds of YouTube tutorials you've made, maybe it
**[02:15:40]** may be especially interesting to talk about domains where you can't just like you can't
**[02:15:43]** test somebody's technical understanding by having them code something up or something.
**[02:15:47]** What advice would you give them?
**[02:15:49]** So I think that's a pretty broad topic.
**[02:15:51]** I do feel like there's basically, I almost feel like there are 10, 20 tips and tricks
**[02:15:54]** that I kind of semi consciously probably do.
**[02:15:56]** But I guess like on a high level, I always try to, I think a lot of this comes from my
**[02:16:04]** physics background.
**[02:16:05]** I really, really did enjoy my physics background.
**[02:16:06]** I have a whole rant when I think how everyone should learn physics in early school education.
**[02:16:11]** Because I think early school education is not about accumulating knowledge or memory
**[02:16:15]** for tasks later in the industry, it's about booting up a brain.
**[02:16:18]** And I think physics uniquely boots up the brain the best.
**[02:16:21]** Because some of the things that they get you to do in your brain during physics is extremely
**[02:16:25]** valuable later.
**[02:16:26]** The idea of building models and abstractions and understanding that there's a first order
**[02:16:30]** of approximation that describes most of the system.
**[02:16:33]** But then there's a second order, third order, first order terms that may or may not be present.
**[02:16:37]** And the idea that you're observing like a very noisy system, but actually there's like
**[02:16:40]** these fundamental frequencies that you can abstract away.
**[02:16:42]** Like when a physicist walks into the class and they say, assume there's a spherical cow
**[02:16:47]** and dot, dot, dot.
**[02:16:48]** And everyone laughs at that.
**[02:16:49]** But actually this is brilliant.
**[02:16:50]** It's brilliant thinking.
**[02:16:52]** That's very generalizable across the industry.
**[02:16:53]** Because yeah, cows can be approximated as a sphere, I guess, in a bunch of ways.
**[02:16:58]** There's a really good book, for example, Scale.
**[02:17:01]** It's basically from a physicist talking about biology.
**[02:17:04]** And maybe this is also a book I would recommend reading.
**[02:17:05]** But you can actually get a lot of really interesting approximations and chart scaling laws of
**[02:17:10]** animals.
**[02:17:11]** And you can look at their heartbeats and things like that.
**[02:17:13]** And they actually line up with the size of the animal and things like that.
**[02:17:17]** You can talk about an animal as a volume and you can actually derive a lot of...
**[02:17:21]** You can talk about the heat dissipation of that.
**[02:17:23]** Because your heat dissipation grows as the surface area, which is growing a square.
**[02:17:27]** But your heat creation or generation is growing as a cube.
**[02:17:31]** And so I just feel like physicists have all the right cognitive tools to approach problem
**[02:17:34]** solving in the world.
**[02:17:36]** So I think because of that training, I always try to find the first order terms or the second
**[02:17:40]** order terms of everything.
**[02:17:41]** When I'm observing a system or a thing, I have a tangle of a web of ideas or knowledge
**[02:17:45]** in my mind.
**[02:17:46]** And I'm trying to find what is the thing that actually matters?
**[02:17:49]** What is the first order component?
**[02:17:51]** How can I simplify it?
**[02:17:52]** How can I have the simplest thing that actually shows that thing, that shows an action?
**[02:17:55]** And then I can tack on the other terms.
**[02:17:58]** Maybe an example from one of my repos that I think illustrates it well is called MicroGrad.
**[02:18:02]** I don't know if you're familiar with this.
**[02:18:04]** So MicroGrad is 100 lines of code that shows back propagation.
**[02:18:09]** You can create neural networks out of simple operations like plus and times, et cetera,
**[02:18:12]** like blocks of neural networks.
**[02:18:14]** And you build up a computational graph and you do a forward pass and a backward pass
**[02:18:17]** to get the gradients.
**[02:18:19]** Now this is at the heart of all neural network learning.
**[02:18:21]** So MicroGrad is 100 lines of pretty interpretable Python code, and it can do forward and backward
**[02:18:26]** arbitrary neural networks, but not efficiently.
**[02:18:29]** So MicroGrad, these 100 lines of Python, are everything you need to understand how neural
**[02:18:32]** networks train.
**[02:18:34]** Everything else is just efficiency.
**[02:18:36]** Everything else is efficiency.
**[02:18:37]** And there's a huge amount of work to do efficiency.
**[02:18:39]** You know, you need your tensors, you lay them out, you stride them, you make sure your kernels
**[02:18:42]** are orchestrating memory movement correctly, et cetera.
**[02:18:45]** It's all just efficiency, roughly speaking.
**[02:18:47]** But the core intellectual sort of piece of neural network training is MicroGrad's 100
**[02:18:50]** lines.
**[02:18:51]** You can easily understand it.
**[02:18:52]** You're chaining.
**[02:18:53]** It's a recursive application of chain rule to drive the gradient which allows you to
**[02:18:55]** optimize any arbitrary differential function.
**[02:18:58]** So I love finding these like, you know, the smaller terms and serving them on a platter
**[02:19:05]** and discovering them.
**[02:19:06]** And I feel like education is like the most intellectually interesting thing because you
**[02:19:11]** have a tangle of understanding and you're trying to lay it out in a way that creates
**[02:19:15]** a ramp where everything only depends on the thing before it.
**[02:19:19]** And I find that this like, you know, untangling of knowledge is just so intellectually interesting
**[02:19:23]** as a cognitive task.
**[02:19:25]** And so I love doing it personally, but I just have fascination with trying to lay things
**[02:19:28]** out in a certain way.
**[02:19:29]** And maybe that helps me.
**[02:19:31]** It also just makes a learning experience so much more motivated.
**[02:19:35]** Your tutorial on the transformer begins with biograms, literally like a lookup table from
**[02:19:42]** here's the word right now, or here's the previous word, here's the next word.
**[02:19:46]** And it's literally just a lookup table.
**[02:19:47]** Yeah, that's the essence of it.
**[02:19:48]** Yeah.
**[02:19:49]** I mean, it's such a brilliant way.
**[02:19:50]** Like, okay, start with a lookup table and then go to a transformer and then each piece
**[02:19:53]** is motivated.
**[02:19:54]** Why would you add that?
**[02:19:55]** Why would you add the next thing?
**[02:19:57]** You couldn't memorize this sort of attention formula, but just like having an understanding
**[02:20:00]** of why every single piece is relevant, what problem it solves.
**[02:20:03]** Yeah.
**[02:20:04]** Yeah.
**[02:20:05]** You're presenting the pain before you present the solution.
**[02:20:06]** And how clever is that?
**[02:20:07]** And you want to take the student through that progression.
**[02:20:09]** So there's a lot of like other small things like that, that I think make it nice and engaging
**[02:20:14]** and interesting.
**[02:20:15]** And always prompting the student.
**[02:20:17]** There's a lot of small things like that, that I think are important and a lot of good educators
**[02:20:21]** will do.
**[02:20:22]** Like, how would you solve this?
**[02:20:23]** Like I'm not going to present a solution before you're going to guess.
**[02:20:27]** That would be wasteful.
**[02:20:28]** That would be, that's a little bit of a, I don't want to swear, but like it's a dick
**[02:20:33]** move towards you to present you with the solution before I give you a shot to try to come up
**[02:20:38]** with it yourself.
**[02:20:39]** Yeah.
**[02:20:40]** Because if you try to come up with it yourself, I guess you get a better understanding of
**[02:20:43]** like, what is the action space?
**[02:20:47]** Yeah.
**[02:20:48]** And then what is the sort of like objective that like, why does only this action fulfill
**[02:20:51]** that objective?
**[02:20:52]** Right?
**[02:20:53]** Yeah.
**[02:20:54]** Well, you have a chance to like try yourself and you have an appreciation when I give you
**[02:20:56]** the solution and it maximizes the amount of knowledge per new fact added.
**[02:21:01]** That's right.
**[02:21:02]** Yeah.
**[02:21:03]** Yeah.
**[02:21:04]** Why do you think by default, people who are genuine experts in their field are often bad
**[02:21:10]** at explaining it to somebody ramping up?
**[02:21:13]** Well, it's the curse of knowledge and expertise.
**[02:21:15]** Yeah.
**[02:21:16]** This is a real phenomenon and I actually suffered from it myself as much as I try to not suffer
**[02:21:20]** from it.
**[02:21:21]** But you take certain things for granted and you can't put yourself in the shoes of new,
**[02:21:24]** of people who are just starting out.
**[02:21:26]** And this is pervasive.
**[02:21:27]** It happens to me as well.
**[02:21:28]** One thing that I actually think is extremely helpful as an example, someone was trying
**[02:21:31]** to show me a paper in biology recently and I just had instantly so many terrible questions.
**[02:21:38]** So what I did was I used ChatGPT to ask the questions with the paper in the context window
**[02:21:42]** and then it worked through some of the simple things.
**[02:21:45]** And then I actually shared the thread to the person who shared it, who actually like wrote
**[02:21:49]** that paper or like worked on that work.
**[02:21:50]** And I almost feel like it was like, if they can see the dumb questions I had, it might
**[02:21:55]** help them explain it better in the future or something like that.
**[02:21:59]** So for example, for my material, I would love if people shared their dumb conversations
**[02:22:04]** with ChatGPT about the stuff that I've created, because it really helps me put myself again
**[02:22:07]** in the shoes of someone who's starting out.
**[02:22:09]** Another trick like that, that I just works astoundingly well.
**[02:22:16]** If somebody writes a paper or a blog post or an announcement, it is in 100% of cases
**[02:22:23]** true that just the narration or the transcription of how they would explain it to you over lunch
**[02:22:30]** is way more not only understandable, but actually also more accurate and scientific
**[02:22:39]** in the sense that people have a bias to explain things in the most abstract, jargon-filled
**[02:22:45]** way possible and to clear their throat for four paragraphs before they explain the central
**[02:22:49]** idea.
**[02:22:50]** But there's something about communicating one-on-one with a person, which compels you
**[02:22:54]** to just say the thing.
**[02:22:57]** Just say the thing.
**[02:22:58]** Yeah.
**[02:23:00]** Yeah.
**[02:23:01]** I love that tweet.
**[02:23:02]** I thought it was really good.
**[02:23:03]** I shared it with a bunch of people, actually.
**[02:23:04]** I think it was really good.
**[02:23:05]** And I noticed this many, many times.
**[02:23:06]** Maybe the most prominent example is, I remember back in my PhD days doing research, etc.
**[02:23:11]** You read someone's paper, right?
**[02:23:12]** And you work to understand what it's doing, etc.
**[02:23:15]** And then you catch them, you're having beers at the conference later, and you ask them,
**[02:23:18]** so like this paper, like, so what are you doing?
**[02:23:20]** Like, what is the paper about?
**[02:23:21]** And they will just tell you these like three sentences that like perfectly capture the
**[02:23:24]** essence of that paper and totally give you the idea, and you didn't have to read the
**[02:23:27]** paper.
**[02:23:28]** Yeah.
**[02:23:30]** It's like when you're sitting at the table with a beer or something like that, and like,
**[02:23:32]** oh yeah, the paper is just, oh, you take this idea, you take that idea, and you try this
**[02:23:34]** experiment and you try this thing.
**[02:23:37]** And they have a way of just putting it conversationally.
**[02:23:39]** Right.
**[02:23:40]** And just like perfectly, like, why isn't that the abstract?
**[02:23:44]** Exactly.
**[02:23:46]** This is coming from the perspective of how somebody who's trying to explain an idea should
**[02:23:49]** formulate it better.
**[02:23:51]** What is your advice as a student to other students where, if you don't have a Karpathy
**[02:23:56]** who is doing the exposition of an idea, if you're reading a paper from somebody or reading
**[02:24:01]** a book, what strategies do you employ to learn material you're interested in, in fields you're
**[02:24:08]** not an expert in?
**[02:24:09]** I don't actually know that I have, like, unique tips and tricks, to be honest.
**[02:24:15]** Basically, it's kind of a painful process.
**[02:24:18]** But you know, like, redraft one.
**[02:24:21]** I think, like, one thing that has always helped me quite a bit is, I had a small tweet about
**[02:24:27]** this, actually.
**[02:24:28]** So, like, learning things on demand is pretty nice.
**[02:24:30]** Learning depth-wise.
**[02:24:31]** I do feel like you need a bit of alternation of learning depth-wise on demand, you're trying
**[02:24:35]** to achieve a certain project that you're going to get a reward from, and learning breadth-wise,
**[02:24:38]** which is just, oh, let's do whatever one-on-one, and here's all the things you might need.
**[02:24:42]** Which is a lot of school does a lot of breadth-wise learning, like, oh, trust me, you'll need
**[02:24:45]** this later.
**[02:24:46]** You know, that kind of stuff.
**[02:24:47]** Like, okay, I trust you, I'll learn it because I guess I need it.
**[02:24:51]** But I love the kind of learning where you'll actually get a reward out of doing something
**[02:24:54]** and you're learning on demand.
**[02:24:55]** The other thing that I've found is extremely helpful is, maybe this is an aspect where
**[02:25:00]** education is a bit more selfless, because explaining things to people is a beautiful
**[02:25:05]** way to learn something more deeply.
**[02:25:07]** This happens to me all the time.
**[02:25:08]** I think it probably happens to other people, too, because I realize if I don't really understand
**[02:25:13]** something, I can't explain it, you know?
**[02:25:15]** And I'm trying, and I'm like, actually, I don't understand this, and it's so annoying
**[02:25:19]** to come to terms with that.
**[02:25:21]** And then you can go back and make sure you understood it.
**[02:25:23]** And so it fills these gaps of your understanding.
**[02:25:25]** It forces you to come to terms with them and to reconcile them.
**[02:25:28]** I love to re-explain and things like that, and I think people should be doing that more
**[02:25:32]** as well.
**[02:25:33]** I think that forces you to manipulate knowledge and make sure that you know what you're talking
**[02:25:36]** about when you're explaining it.
**[02:25:37]** Oh, yeah.
**[02:25:38]** I think that's an excellent note to close on.
**[02:25:39]** Yeah.
**[02:25:40]** Andre, that was great.
**[02:25:41]** Yeah, thank you.
**[02:25:42]** Thanks.
**[02:25:43]** Have a good time.
**[02:25:44]** Hey, everybody.
**[02:25:45]** I hope you enjoyed that episode.
**[02:25:46]** If you did, the most helpful thing you can do is just share it with other people who
**[02:25:50]** you think might enjoy it.
**[02:25:51]** It's also helpful if you leave a rating or a comment on whatever platform you're listening
**[02:25:56]** on.
**[02:25:57]** If you're interested in sponsoring the podcast, you can reach out at tharkesh.com slash advertise.
**[02:26:03]** Otherwise, I'll see you on the next one.
