---
layout: default
type: transcript
series: dwarkesh
episode: 4
guest: Dwarkesh Patel
title: "What are we scaling?"
source_url: "https://www.youtube.com/watch?v=_zgnSbu5GqE"
analysis_url: /transcripts/dwarkesh/4_what_are_we_scaling.analysis/
permalink: /transcripts/dwarkesh/4_what_are_we_scaling/
---
# Transcript: EP4 - What are we scaling?

Source: https://www.youtube.com/watch?v=_zgnSbu5GqE

---

**[00:00]** I'm confused why some people have super short timelines, yet at the same time are
**[00:03]** bullish on scaling up reinforcement learning atop LLMs.
**[00:07]** If we're actually close to a human-like learner, then this whole approach of training
**[00:11]** on verifiable outcomes is doomed.
**[00:14]** Now, currently the labs are trying to bake in a bunch of skills into these models through
**[00:20]** mid-training.
**[00:21]** There's an entire supply chain of companies that are building RL environments, which teach
**[00:25]** the model how to navigate a web browser or use Excel to build financial models.
**[00:30]** Now, either these models will soon learn on the job in a self-directed way, which will
**[00:34]** make all this freebaking pointless, or they won't, which means that AGI is not imminent.
**[00:39]** Humans don't have to go through the special training phase where they need to rehearse
**[00:42]** every single piece of software that they might ever need to use on the job.
**[00:45]** Baron Millage made an interesting point about this in a recent blog post he wrote.
**[00:48]** He writes, quote,
**[00:49]** When we see frontier models improving at various benchmarks, we should think not just
**[00:53]** about the increased scale and the clever ML research ideas, but the billions of dollars
**[00:57]** that are paid to PhDs, MDs, and other experts to write questions and provide example answers
**[01:04]** and reasoning targeting these precise capabilities.
**[01:07]** You can see this tension most vividly in robotics.
**[01:10]** In some fundamental sense, robotics is an algorithms problem, not a hardware or data
**[01:14]** problem.
**[01:15]** With very little training, a human can learn how to teleoperate current hardware to do
**[01:19]** useful work.
**[01:20]** So if we actually had a human-like learner, robotics would be, in large part, a solved
**[01:24]** problem.
**[01:25]** But the fact that we don't have such a learner makes it necessary to go out into a thousand
**[01:28]** different homes and practice a million times on how to pick up dishes or fold laundry.
**[01:33]** Now one current argument I've heard from the people who think we're going to have a takeoff
**[01:36]** within the next five years is that we have to do all this kludgy RL in service of building
**[01:41]** a superhuman AI researcher, and then the million copies of this automated Ilia can go figure
**[01:46]** out how to solve robust and efficient learning from experience.
**[01:50]** This just gives me the vibes of that old joke, we're losing money on every sale, but
**[01:54]** we'll make it up in volume.
**[01:55]** Somehow this automated researcher is going to figure out the algorithm for AGI, which
**[01:59]** is a problem that humans have been banging their head against for the better half of
**[02:03]** a century.
**[02:04]** While not having the basic learning capabilities that children have, I find it super implausible.
**[02:09]** Besides, even if that's what you believe, it doesn't describe how the labs are approaching
**[02:14]** reinforcement learning from verifiable reward.
**[02:16]** You don't need to pre-bake in a consultant skill at crafting PowerPoint slides in order
**[02:20]** to automate Ilia.
**[02:21]** So clearly the lab's actions hint at a worldview where these models will continue to fare poorly
**[02:26]** at generalization and on-the-job learning, thus making it necessary to build in the skills
**[02:31]** that we hope will be economically useful beforehand into these models.
**[02:36]** Another common argument you can make is that even if the model could learn these skills
**[02:40]** on the job, it is just so much more efficient to build in these skills once during trading
**[02:45]** rather than again and again for each user and each company.
**[02:49]** But look, it makes a ton of sense to just bake influency with common tools like browsers
**[02:52]** and terminals.
**[02:53]** And indeed, one of the key advantages that AGIs will have is this greater capacity to
**[02:58]** share knowledge across copies.
**[02:59]** But people are really underrating how much company and context-specific skills are required
**[03:04]** to do most jobs.
**[03:06]** And there just isn't currently a robust, efficient way for AIs to pick up these skills.
**[03:11]** I was recently at a dinner with an AI researcher and a biologist, and it turned out the biologist
**[03:19]** had long timelines.
**[03:21]** And so we were asking about why she had these long timelines.
**[03:24]** And then she said, you know, one part of work recently in the lab is involved looking at
**[03:28]** slides and deciding if the dot in that slide is actually a macrophage or just looks like
**[03:34]** a macrophage.
**[03:35]** And the AI researcher, as you might anticipate, responded, look, image classification is a
**[03:39]** textbook deep learning problem.
**[03:41]** This is dead center in the kind of thing that we could train these models to do.
**[03:45]** And I thought this is a very interesting exchange because it illustrated a key crux between
**[03:49]** me and the people who expect transformative economic impact within the next few years.
**[03:54]** Human workers are valuable precisely because we don't need to build in these schleppy training
**[03:59]** loops for every single small part of their job.
**[04:02]** It's not net productive to build a custom training pipeline to identify what macrophages
**[04:07]** look like given the specific way that this lab prepares slides and then another training
**[04:12]** loop for the next lab specific micro task and so on.
**[04:16]** What you actually need is an AI that can learn from semantic feedback or from self-directed
**[04:20]** experience and then generalize the way a human does.
**[04:24]** Every day you have to do 100 things that require judgment, situational awareness and skills
**[04:29]** and context that are learned on the job.
**[04:32]** These tasks differ not just across different people, but even from one day to the next
**[04:37]** for the same person.
**[04:38]** It is not possible to automate even a single job by just baking in a predefined set of
**[04:44]** skills, let alone all the jobs.
**[04:46]** In fact, I think people are really underestimating how big a deal actual AGI will be because
**[04:49]** they are just imagining more of this current regime.
**[04:52]** They're not thinking about billions of human like intelligences on a server which can copy
**[04:57]** and merge all of the learnings.
**[04:58]** And to be clear, I expect this, which is to say I expect actual brain like intelligences
**[05:03]** within the next decade or two, which is pretty fucking crazy.
**[05:09]** Sometimes people will say that the reason that AIs are more widely deployed right now
**[05:13]** across firms and already providing lots of value outside of coding is that technology
**[05:18]** takes a long time to diffuse.
**[05:20]** And I think this is cope.
**[05:21]** I think people are using this cope to gloss over the fact that these models just lack
**[05:25]** the capabilities that are necessary for broad economic value.
**[05:28]** If these models actually were like humans on a server, they'd diffuse incredibly quickly.
**[05:33]** In fact, they'd be so much easier to integrate and onboard than a normal human employee is.
**[05:38]** They could read your entire slack and drive within minutes and they could immediately
**[05:41]** distill all the skills that your other AI employees have.
**[05:44]** Plus, the hiring market for humans is very much like a lemons market where it's hard
**[05:50]** to tell who the good people are beforehand.
**[05:52]** And then obviously hiring somebody who turns out to be bad is very costly.
**[05:57]** This is just not a dynamic that you would have to face or worry about if you're just
**[06:02]** spinning up another instance of a vetted AGI model.
**[06:05]** So for these reasons, I expect it's going to be much easier to diffuse AI labor into
**[06:09]** firms than it is to hire a person.
**[06:12]** And companies hire people all the time.
**[06:13]** If the capabilities were actually at AGI level, people would be willing to spend trillions
**[06:18]** of dollars a year buying tokens that these models produce.
**[06:23]** Human knowledge workers across the world cumulatively earn tens of trillions of dollars
**[06:27]** a year in wages.
**[06:28]** And the reason that labs are orders of magnitude off this figure right now is that the models
**[06:33]** are nowhere near as capable as human knowledge workers.
**[06:37]** Now, you might be like, look, how can the standard have suddenly become labs have earned
**[06:43]** tens of trillions of dollars of revenue a year, right?
**[06:45]** Like until recently, people were saying, can these models reason?
**[06:49]** Do these models have common sense?
**[06:50]** Are they just doing pattern recognition?
**[06:52]** And obviously, AI bulls are right to criticize AI bears for repeatedly moving these goalposts.
**[06:59]** And this is very often fair.
**[07:01]** It's easy to underestimate the progress that AI has made over the last decade.
**[07:04]** But some amount of goalpost shifting is actually justified.
**[07:07]** If you showed me Gemini 3 in 2020, I would have been certain that it could automate half
**[07:12]** of knowledge.
**[07:13]** And so we keep solving what we thought were the sufficient bottlenecks to AGI.
**[07:17]** We have models that have general understanding, they have few shot learning, they have reasoning.
**[07:21]** And yet we still don't have AGI.
**[07:24]** So what is a rational response to observing this?
**[07:27]** I think it's totally reasonable to look at this and say, oh, actually, there's much more
**[07:31]** to intelligence and labor than I previously realized.
**[07:34]** And while we're really close, and in many ways have surpassed what I would have previously
**[07:38]** defined as AGI in the past, the fact that model companies are not making the trillions
**[07:44]** of dollars in revenue that would be implied by AGI clearly reveals that my previous definition
**[07:50]** of AGI was too narrow.
**[07:52]** And I expect this to keep happening into the future.
**[07:54]** I expect that by 2030, the labs will have made significant progress on my hobby horse
**[07:59]** of continual learning.
**[08:01]** And the models will be earning hundreds of billions of dollars in revenue a year.
**[08:04]** But they won't have automated all knowledge work.
**[08:07]** And I'll be like, look, we made a lot of progress, but we haven't hit AGI yet.
**[08:11]** We also need these other capabilities, we need X, Y and Z capabilities in these models.
**[08:17]** Models keep getting more impressive at the rate that the short timelines people predict,
**[08:20]** but more useful at the rate that the long timelines people predict.
**[08:28]** It's worth asking, what are we scaling?
**[08:30]** With free trading, we had this extremely clean and general trend in improvement and loss
**[08:35]** across multiple orders of magnitude and compute.
**[08:38]** Albeit, this was on a power law, which is as weak as exponential growth is strong.
**[08:43]** But people are trying to launder the prestige that free trading scaling has, which is almost
**[08:49]** as predictable as a physical law of the universe to justify bullish predictions about reinforcement
**[08:55]** learning from verifiable reward, for which we have no wealth but publicly known trend.
**[09:00]** And when intrepid researchers do try to piece together the implications from scarce public
**[09:04]** data points, they get pretty bearish results.
**[09:07]** For example, Toby Board has a great post where he cleverly connects the dots between the
**[09:11]** different O series benchmarks.
**[09:13]** And this suggested to him that, quote, we need something like a million X scale up in
**[09:18]** total RL compute to give a boost similar to a single GPT level, end quote.
**[09:27]** So people have spent a lot of time talking about the possibility of a software in the
**[09:31]** singularity where AI models will write the code that generates a smarter successor system
**[09:37]** or a software plus hardware singularity where AIs also improve their successors computing
**[09:42]** hardware. However, all these scenarios neglect what I think will be the main driver of further
**[09:47]** improvements atop AGI, continual learning.
**[09:50]** Again, think about how humans become more capable of anything.
**[09:53]** It's mostly from experience in the relevant domain.
**[09:56]** Over conversation, Baron Millage made this interesting suggestion that the future might
**[10:00]** look like continual learning agents who are all going out and they're doing different
**[10:04]** jobs and they're generating value.
**[10:06]** And then they're bringing back all their learnings to the hive mind model, which does
**[10:10]** some kind of batch distillation on all of these agents.
**[10:13]** The agents themselves could be quite specialized, containing what Karpathy called the
**[10:17]** cognitive core plus knowledge and skills relevant to the job they're being deployed to
**[10:22]** do. Solving continual learning won't be a singular one and done achievement.
**[10:27]** Instead, it will feel like solving in context learning.
**[10:30]** Now, GPT-3 already demonstrated in context learning could be very powerful in 2020.
**[10:35]** It's in context learning capabilities were so remarkable.
**[10:37]** The title of the GPT-3 paper was Language Models are a Few-Shot Learners.
**[10:42]** But of course, we didn't solve in context learning when GPT-3 came out.
**[10:45]** And indeed, there's still plenty of progress that still has to be made from comprehension
**[10:49]** to context length. I expect a similar progression with continual learning.
**[10:54]** Labs will probably release something next year which they call continual learning and
**[10:58]** which will, in fact, count as progress towards continual learning.
**[11:01]** But human level on the job learning may take another five to 10 years to iron out.
**[11:08]** This is why I don't expect some kind of runaway gains from the first model that cracks
**[11:12]** continual learning that's getting more and more widely deployed and capable.
**[11:16]** If you had fully solved continual learning drop out of nowhere, then sure, it might be
**[11:20]** game set match, as Satya put it on the podcast when I asked him about this possibility.
**[11:24]** But that's probably not what's going to happen.
**[11:26]** Instead, some lab is going to figure out how to get some initial traction on this
**[11:29]** problem and then playing around with this feature will make it clear how it was
**[11:33]** implemented. And then other labs will soon replicate the breakthrough and improve it
**[11:38]** slightly. Besides, I just have some prior that the competition will stay pretty fierce
**[11:42]** between all these model companies.
**[11:44]** And this is informed by the observation that all these previous supposed flywheels,
**[11:48]** whether that's user engagement on chat or synthetic data or whatever, have done very
**[11:53]** little to diminish the greater and greater competition between model companies.
**[11:56]** Every month or so, the big three model companies will rotate around the podium and the
**[12:00]** other competitors are not that far behind.
**[12:02]** There seems to be some force and this is potentially talent poaching.
**[12:06]** It's potentially the rumor mill in SF or just normal reverse engineering, which is so
**[12:10]** far neutralized any runaway advantage that a single lab might have had.
**[12:14]** This was a narration of an essay that originally released on my blog at Dworkesh.com.
**[12:19]** I've been publishing a lot more essays.
**[12:21]** I found it's actually quite helpful in ironing out my thoughts before interviews.
**[12:24]** If you want to stay up to date with those, you can subscribe at Dworkesh.com.
**[12:28]** Otherwise, I'll see you for the next podcast.
**[12:30]** Cheers.
