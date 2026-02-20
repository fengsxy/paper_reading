---
layout: default
type: transcript
series: dwarkesh
episode: 7
guest: ""
title: "Satya Nadella – How Microsoft thinks about AGI"
source_url: "https://www.youtube.com/watch?v=8-boBsWcr5A"
analysis_url: /transcripts/dwarkesh/7_satya_nadella_how_microsoft_thinks_about_agi.analysis/
permalink: /transcripts/dwarkesh/7_satya_nadella_how_microsoft_thinks_about_agi/
---

# Transcript: EP7 - Satya Nadella – How Microsoft thinks about AGI

Source: https://www.youtube.com/watch?v=8-boBsWcr5A

---

**[00:00]** Maybe after the Industrial Revolution, this is the biggest thing.
**[00:03]** But at the same time, I'm a little grounded in the fact that this is still early innings.
**[00:08]** If you're a model company, you may have a winner's curse.
**[00:10]** You may have done all the hard work, done unbelievable innovation,
**[00:14]** except it's kind of like one copy away from that being commoditized.
**[00:20]** We didn't want to just be a hoster for one company
**[00:24]** and have just a massive book of business with one customer.
**[00:27]** That's not a business.
**[00:28]** You can't build an infrastructure that's optimized for one model.
**[00:31]** If you do that, you're one tweak away.
**[00:33]** Some MOE-like breakthrough that happens
**[00:35]** and your entire network topology goes out of the window,
**[00:38]** then that's a scary thing.
**[00:39]** Our business, which today is an end-user tools business,
**[00:42]** will become essentially an infrastructure business in support of agents doing work.
**[00:47]** The thing that you have to think through is not what you do in the next five years,
**[00:51]** but what do you do for the next 50.
**[00:53]** Today, we are interviewing Satya Nadella.
**[00:57]** We being me and Dilan Patel, who is founder of Simianalysis.
**[01:00]** Satya, welcome.
**[01:01]** Thank you. It's great.
**[01:02]** Thanks for coming over to Atlanta.
**[01:04]** Yeah, thank you for giving us a tour of the new facility.
**[01:07]** It's been really cool to see.
**[01:08]** Absolutely.
**[01:09]** Satya and Scott Guthrie, Microsoft's EVP of cloud and AI,
**[01:13]** give us a tour of their brand new Fairwater 2 data center,
**[01:16]** the current most powerful in the world.
**[01:19]** We try to 10x the training capacity every 18 to 24 months.
**[01:23]** And so this would be effectively a 10x increase.
**[01:25]** 10x from what GPD 5 was trained with.
**[01:27]** And so to put it in perspective, the number of optics,
**[01:30]** the network optics in this building is almost as much as
**[01:35]** all of Azure across all our data centers two and a half years ago.
**[01:38]** It's kind of what?
**[01:39]** Five million network connections.
**[01:41]** You've got all this bandwidth between different sites in a region
**[01:44]** and between the two regions.
**[01:45]** So is this like a big bet on scaling in the future
**[01:47]** that you anticipate in the future,
**[01:49]** there's going to be some huge model that needs to require
**[01:51]** two whole different regions to train?
**[01:53]** The goal is to be able to kind of aggregate these flops
**[01:57]** for a large training job
**[01:58]** and then put these things together across sites.
**[02:02]** And the reality is you'll use it for training
**[02:06]** and then you'll use it for data gen,
**[02:09]** you'll use it for inference in all sort of ways.
**[02:11]** It's not like it's going to be used only for one workload forever.
**[02:14]** Fairwater 4, which you're going to see under construction nearby,
**[02:18]** will also be on that one petabits network
**[02:21]** so that we can actually link the two at a very high rate.
**[02:23]** And then basically we do the AI WAN connecting to Milwaukee
**[02:27]** where we have multiple other Fairwaters being built.
**[02:29]** Literally, you can see the model parallelism
**[02:34]** and the data parallelism.
**[02:35]** It's kind of built for essentially the training jobs,
**[02:40]** the pods, the super pods across this campus.
**[02:44]** And then with the WAN,
**[02:46]** you can go to the Wisconsin data center
**[02:49]** and literally run a training job with all of them getting aggregated.
**[02:54]** And what we're seeing right here is this is a cell
**[02:56]** with no servers in it yet, no racks.
**[02:58]** How many racks are in a cell?
**[03:00]** We think about it, we don't necessarily share that per se,
**[03:03]** but let me...
**[03:04]** That's the reason I asked.
**[03:06]** You'll see upstairs.
**[03:08]** I'll start counting.
**[03:08]** You can start counting.
**[03:09]** We'll let you start counting.
**[03:10]** How many cells are there in this building?
**[03:11]** That part also I can't tell you.
**[03:13]** Division is easy, right?
**[03:14]** My God, it's kind of loud.
**[03:17]** Are you looking at this like,
**[03:18]** now I see where my money is going?
**[03:21]** It's kind of like, I run a software company.
**[03:23]** Welcome to the software company.
**[03:26]** How big is the design space once you've decided to use the GB200s and NVLink?
**[03:30]** How many other decisions are there to be made?
**[03:32]** It is coupling from the model architecture
**[03:37]** to what is the physical plan that's optimized.
**[03:41]** And it's also scary in that sense, which is,
**[03:44]** hey, there's going to be a new chip that'll come out,
**[03:46]** which obviously, I mean, you take Vera Rubin Ultra.
**[03:49]** I mean, that's going to have power density that's going to be so different,
**[03:52]** but with cooling requirements that are going to be so different, right?
**[03:55]** So you kind of don't want to just build all to one spec.
**[04:01]** So that goes back a little bit to, I think, the dialogue we'll have,
**[04:03]** which is you want to be scaling entirely.
**[04:09]** Scaling in time, as opposed to scale once and then be stuck with it.
**[04:14]** When you look at all the past technological transitions,
**[04:18]** whether it be, you know, railroads, or the internet,
**[04:21]** or, you know, replaceable parts, industrialization, the cloud,
**[04:25]** all of these things, each revolution has gotten much faster
**[04:28]** in the time it goes from technology discovered to ramp
**[04:31]** and pervasiveness through the economy.
**[04:33]** Many folks who have been on Dwarkesh's podcast
**[04:36]** believe this is sort of the final technological revolution or transition.
**[04:40]** And this time is very, very different.
**[04:43]** And at least so far in the markets, it's sort of, you know,
**[04:46]** in three years, we've already skyrocketed to, you know,
**[04:48]** hyperscalers are doing $500 billion of CapEx next year,
**[04:50]** which is a scale that's unmatched to prior revolutions in terms of speed.
**[04:56]** And the end state seems to be quite different.
**[04:58]** How do you, your framing of this seems quite different than sort of the,
**[05:03]** I would say, the AI bro, who is quite, you know, AGI is coming.
**[05:08]** And, you know, I'd like to understand that more.
**[05:11]** I mean, look, I start with the excitement that I also feel for
**[05:16]** maybe after the industrial revolution, this is the biggest thing.
**[05:20]** And so, therefore, I start with that premise.
**[05:24]** But at the same time, I'm a little grounded in the fact that
**[05:27]** this is still early innings.
**[05:29]** We've built some very useful things.
**[05:31]** We're seeing some great properties.
**[05:33]** These scaling laws seem to be working.
**[05:36]** And I'm optimistic that they'll continue to work, right?
**[05:40]** Some of it is, you know, it does require real science breakthroughs,
**[05:44]** but it's also a lot of engineering and what have you.
**[05:47]** But that said, I also sort of take the view that, you know,
**[05:52]** even what has been happening in the last 70 years of computing
**[05:55]** has also been a march that has helped us move,
**[06:00]** you know, with, as I said, you know, I like one of the things that Raj Reddy
**[06:06]** has as a metaphor for what AI is, right?
**[06:09]** He's a Turing Award winner out of CMU.
**[06:13]** And he's always, and he had this even pre-AGI,
**[06:16]** but he had this metaphor of AI should either be a guardian angel
**[06:20]** or a cognitive amplifier.
**[06:22]** I love that.
**[06:23]** It's a simple way to think about what this is.
**[06:26]** Ultimately, what is its human utility?
**[06:29]** It is going to be a cognitive amplifier and a guardian angel.
**[06:33]** And so if I sort of view it that way, I view it as a tool.
**[06:37]** But then you can also go very mystical about it and say,
**[06:39]** well, this is, you know, more than a tool.
**[06:41]** It does all these things which only humans did so far.
**[06:44]** But that has been the case with many technologies in the past.
**[06:47]** Only humans did a lot of things.
**[06:48]** And then we add tools that did them.
**[06:50]** I guess we don't have to get wrapped up in the definition here,
**[06:53]** but maybe one way to think about it is like,
**[06:55]** maybe it takes five years, 10 years, 20 years.
**[06:57]** At some point, eventually, a machine is producing Satya tokens, right?
**[07:01]** And the Microsoft board thinks that Satya tokens are worth a lot.
**[07:04]** How much are you wasting of economic value by interviewing Satya?
**[07:09]** You cannot afford the API costs of Satya tokens.
**[07:12]** But so, you know, whatever you want to call it,
**[07:15]** is that are the Satya tokens a tool or an agent, whatever?
**[07:18]** Right now, if you have models that cost on the order of dollars or cents per million tokens,
**[07:22]** there's just an enormous room for expansion,
**[07:26]** a margin expansion there where a million tokens of Satya are worth a lot.
**[07:32]** And where does that margin go?
**[07:34]** And what level of that margin is Microsoft involved in, is the question I have.
**[07:39]** So I think, in some sense, this goes back a bit to essentially
**[07:44]** what's the economic growth picture going to really look like?
**[07:48]** What's the firm going to look like?
**[07:50]** What's productivity going to look like?
**[07:51]** And that, to me, is where, again, if the Industrial Revolution created,
**[07:56]** after whatever, 70 years of diffusion is when you started seeing the economic growth, right?
**[08:01]** It took, that's the other thing to remember, is even if the tech is diffusing fast this time
**[08:08]** around, for true economic growth to appear, it has to sort of diffuse to a point where the work,
**[08:14]** the work artifact and the workflow has to change.
**[08:17]** And so that's kind of one place where I think
**[08:19]** the change management required for a corporation to truly change,
**[08:23]** I think, is something we shouldn't discount.
**[08:26]** So I think going forward, do humans and the tokens they produce get higher leverage, right?
**[08:33]** Whether it's the Dwarkesh or the Dillon tokens of the future.
**[08:37]** I mean, think about the amount of technology.
**[08:39]** Would you be able to run semi-analysis or this podcast without technology?
**[08:43]** No chance, right?
**[08:44]** I mean, the scale that you would be able to achieve, no chance.
**[08:48]** So the question is, what's that scale?
**[08:50]** Is it going to be 10Xed with something that comes through?
**[08:53]** Absolutely.
**[08:55]** And therefore, whether you're ramped to some revenue number or you're ramped to some
**[08:59]** audience number or what have you.
**[09:00]** And so that, I think, is what's going to happen, right?
**[09:02]** I mean, the point is, that's whatever, what took 70 years,
**[09:07]** maybe 150 years for the Industrial Revolution may happen in 20 years, 25 years.
**[09:12]** That's a better way to, like, I would love to
**[09:15]** compress what happened in 200 years of the Industrial Revolution into 20-year period,
**[09:20]** if you're lucky.
**[09:22]** So Microsoft historically has been perhaps, you know, the greatest software company,
**[09:27]** the largest software-as-a-service company.
**[09:29]** You know, you've gone through a transition in the past where you used to sell Windows
**[09:32]** licenses and disks of Windows or Microsoft.
**[09:35]** And now you sell, you know, subscriptions to 365.
**[09:38]** Or as we go from sort of, you know, that transition to where your business is today,
**[09:45]** there's also a transition going after that, right?
**[09:48]** Software-as-a-service, incredibly low incremental cost per user.
**[09:52]** There's a lot of R&D.
**[09:53]** There's a lot of customer acquisition cost.
**[09:55]** This is why, not Microsoft, but the SaaS companies have underperformed massively in the markets
**[10:00]** because the cogs of AI is just so high and that just completely breaks how these business
**[10:04]** models work.
**[10:05]** How do you, as perhaps the greatest software company, software-as-a-service company, transition
**[10:13]** Microsoft to this new age where cogs matters a lot and the incremental cost per user is
**[10:19]** different, right?
**[10:20]** Because right now you're charging, hey, it's 20 bucks for a co-pilot.
**[10:23]** Yeah, so I think that this is a great question because in some sense, the business models
**[10:27]** themselves, I think the levers are going to remain similar, right?
**[10:30]** Which is if I look at the, if you look at the menu of models starting from like, say,
**[10:37]** consumer all the way, right?
**[10:38]** There will be some ad unit.
**[10:40]** There will be some transaction.
**[10:42]** There'll be some device gross margin for somebody who builds an AI device.
**[10:47]** There will be subscriptions, consumer and enterprise, and then there'll be consumption,
**[10:52]** right?
**[10:52]** So I still think that that's kind of how, those are all the meters.
**[10:56]** To your point, what is a subscription?
**[10:58]** Up to now, people like subscriptions because they can budget for them, right?
**[11:03]** They are essentially entitlements to some consumption rights that come encapsulated
**[11:09]** in a subscription.
**[11:10]** So that I think is what, in some sense, it becomes a pricing decision.
**[11:14]** So how much consumption is in, you are entitled to is, if you look at all the coding subscriptions,
**[11:21]** that's kind of what they are, right?
**[11:22]** And they kind of have the pro tier, the standard tier and what have you.
**[11:26]** And so I think that's how the pricing will, and the margin structures will get tiered.
**[11:33]** The interesting thing is having at Microsoft, the good news for us is we kind of are in that
**[11:39]** business all across all those meters.
**[11:42]** And in fact, as a portfolio level, we pretty much have consumption subscriptions to all
**[11:50]** of the other consumer levers as well.
**[11:53]** And then I think time will tell which of these models make sense in what categories.
**[11:59]** One thing on the SaaS side, since you brought up, which I think a lot about is, take Office
**[12:04]** 365 or Microsoft 365.
**[12:07]** I mean, man, having a low ARPU is great because here's an interesting thing, right?
**[12:11]** During the transition from server to cloud, one of the questions we used to ask ourselves
**[12:16]** is, oh my God, if all we did was just basically move the same users who were using, let's
**[12:21]** call it our office licenses and our servers at that time, office servers, right, to the
**[12:27]** cloud and we had cogs, this is going to basically not only shrink our margins, but it will be
**[12:33]** fundamentally a less profitable company.
**[12:36]** Except what happened was that move to the cloud expanded the market like crazy, right?
**[12:43]** I mean, we sold a few servers in India, didn't sell much, whereas in the cloud, suddenly
**[12:47]** everybody in India also could afford fractionally buying servers.
**[12:51]** The IT cost.
**[12:52]** I mean, in fact, the biggest thing I had not realized, for example, was the amount of money
**[12:57]** people were spending buying storage underneath SharePoint.
**[13:02]** In fact, EMC's biggest segment may have been storage servers for SharePoint.
**[13:09]** All that sort of dropped in the cloud because nobody had to go buy.
**[13:13]** In fact, it is working capital.
**[13:14]** I mean, basically it is cash flow out, right?
**[13:17]** And so, it expanded the market massively.
**[13:21]** So, this AI thing will be that, right?
**[13:23]** So, if you take coding, what we built with GitHub and VS Code in over whatever, decades,
**[13:33]** suddenly the coding assistant is that big in one year.
**[13:36]** And so, that I think is what's going to happen as well, which is the market expands massively.
**[13:41]** I guess there's a question of the market will expand.
**[13:44]** Will the parts of the revenue that touch Microsoft expand?
**[13:48]** So, Copilot is an example where if you look early this year, I think, I guess,
**[13:54]** according to Dylan's numbers, the Copilot revenue, GitHub Copilot revenue was like
**[13:59]** $500 million or something like that.
**[14:00]** And then there were like no close competitors.
**[14:03]** Whereas now you have Cloud Code, Cursor, and Copilot with around similar revenue, around
**[14:09]** a billion.
**[14:10]** And then Codex is catching up around 700, 800 million.
**[14:13]** And so, the question is across all the surfaces that Microsoft has access to,
**[14:16]** what is the advantage that Microsoft's equivalence of Copilot have?
**[14:19]** Yeah.
**[14:19]** By the way, I love this chart.
**[14:21]** You know, I love this chart for so many reasons.
**[14:23]** One is we're still on the top.
**[14:26]** Second is all these companies that are listed here are all companies that have been born
**[14:32]** in the last four or five years.
**[14:34]** That to me is the best sign, right?
**[14:36]** Which is if you have new competitors, new existential problems, when you say, man, who's
**[14:40]** it now?
**[14:41]** Cloud's going to kill you.
**[14:42]** Cursor is going to kill you.
**[14:43]** It's not Borland, right?
**[14:44]** So, thank God.
**[14:45]** That means we are in the right direction.
**[14:48]** But this is it, right?
**[14:49]** The fact that we went from nothing to this scale is the market expansion.
**[14:55]** So, this is like the cloud-like stuff.
**[14:57]** Fundamentally, this category of coding and AI is probably going to be one of the biggest
**[15:03]** categories, right?
**[15:04]** It is a software factory category.
**[15:05]** In fact, it may be bigger than knowledge work.
**[15:08]** So, I kind of want to keep myself open-minded about, I mean, we're going to have tough
**[15:12]** competition.
**[15:12]** I think that's your point, which I think is a great one.
**[15:15]** But man, like I'm glad we have, we parlayed what we had into this.
**[15:22]** And now we have to compete.
**[15:23]** And so, in the compete side, even in the last quarter, we just finished, we did our quarterly
**[15:29]** announcement.
**[15:29]** I think we grew from 20 to 26 million subs, right?
**[15:32]** So, I feel good about our sub growth and where the direction of travel on that is.
**[15:37]** But the more interesting thing that has happened is, guess where all the repos of all these
**[15:43]** other guys who are generating lots and lots of code go to?
**[15:47]** They go to GitHub.
**[15:48]** So, GitHub is at an all-time high in terms of repo creation, PRs, everything.
**[15:55]** So, in some sense, we want to keep that open, by the way.
**[15:58]** That means we want to have that, right?
**[16:00]** Because we don't want to conflate that with our own growth, right?
**[16:03]** Interestingly enough, we are getting one developer joining GitHub a second or something.
**[16:06]** That is the stat, I think.
**[16:08]** And then 80% of them just fall into some GitHub copilot workflow, just because there are.
**[16:14]** And by the way, many of these things will even use some of our code review agents, which
**[16:18]** are by default on, just because you can use it.
**[16:21]** So, we'll have many, many structural shots at this.
**[16:24]** The thing that we're also going to do is what we did with the primitives of GitHub,
**[16:30]** whether starting with Git, to issues, to actions.
**[16:35]** These are powerful, lovely things, because they kind of are all built around your repo.
**[16:40]** So, we want to extend that.
**[16:42]** Last week at GitHub Universe, that's kind of what we did, right?
**[16:45]** So, we said Agent HQ was the conceptual thing that we said we were going to build out.
**[16:51]** This is where, for example, you have a thing called Mission Control.
**[16:54]** And you go to Mission Control, and now I can fire off, sometimes I describe it as the cable
**[16:59]** TV of all these AI agents, because I'll have essentially packaged into one subscription,
**[17:04]** Codex, Clod, Cognition stuff, anyone's agents, Grok, all of them will be there.
**[17:13]** So, I get one package.
**[17:14]** And then I can literally go issue a task, steer them, so they will all be working in
**[17:20]** their independent branches.
**[17:22]** I can monitor them.
**[17:24]** So, I literally have, because I think that's going to be one of the biggest places of innovation,
**[17:28]** right?
**[17:28]** Because right now, I want to be able to use multiple agents.
**[17:32]** I want to be able to then digest the output of the multiple agents.
**[17:35]** I want to be able to then keep a handle on my repo.
**[17:38]** So, if there's some kind of a heads-up display that needs to be built, and then for me to
**[17:43]** quickly steer and triage what the coding agents have generated.
**[17:47]** That, to me, between VS Code, GitHub, and all of these new primitives we will build
**[17:53]** as mission control, I think with a control plane, observability, I mean, think about
**[17:58]** everyone who is going to deploy all this, will require a whole host of observability
**[18:03]** of what agent did what at what time to what code base.
**[18:06]** So, I feel that's the opportunity.
**[18:09]** And at the end of the day, your point is well taken, which is we better be competitive and
**[18:13]** innovate.
**[18:13]** And if we don't, yes, we will get toppled.
**[18:15]** But I like the chart, at least as long as we're on the top, even with competition.
**[18:20]** The key point here is sort of that GitHub will keep growing,
**[18:22]** irregardless of whose coding agent wins.
**[18:25]** But that market only grows at, you know, call it 10%, 15%, 20%, which is way above GDP.
**[18:30]** It's a great compounder.
**[18:31]** But these AI coding agents have grown from, you know, call it $500 million run rate at
**[18:36]** the end of last year, which was basically just GitHub Copilot, to now the current run
**[18:40]** rate across, you know, GitHub Copilot, Cloud Code, Cursor, Cognition, Windsurf, Repl.it,
**[18:47]** Codex, OpenAI Codex, that's run rating at $5, $6 billion now for the Q4 of this year.
**[18:54]** That's a 10x, right?
**[18:55]** And when you look at, hey, what's the TAM of software agents?
**[18:59]** Is it the $2 trillion of wages you pay people?
**[19:02]** Or is it something beyond that?
**[19:06]** Because every company in the world will now be able to, you know, develop software more.
**[19:10]** No question Microsoft takes a slice of that.
**[19:13]** But you've gone from near 100% or certainly way about 50% to, you know,
**[19:18]** sub 25% market share in just one year.
**[19:21]** What is the sort of confidence that people can get that Microsoft will be?
**[19:25]** Again, it goes back a little bit, Dylan, to sort of there's no birthright here that we
**[19:28]** should have any confidence other than to say, hey, we should go innovate.
**[19:33]** And knowing the lucky break we have, in some sense, is that this category is going to be
**[19:39]** a lot bigger than anything we had high share in.
**[19:42]** Let me say it that way, right?
**[19:43]** In some sense, you could say, man, we kind of had high share in VS Code.
**[19:46]** We had high share in the repos with GitHub.
**[19:51]** And that was a good market.
**[19:52]** But the point is even having a decent share in what is a much more expansive market, right?
**[19:58]** I mean, you could say we had a high share in client server, server computing.
**[20:02]** We have much lower share than that in hyperscale.
**[20:06]** But is it a much bigger business by orders of magnitude?
**[20:09]** So at least there's existence proof that Microsoft has been OK,
**[20:13]** even if our share position has not been as strong as it was,
**[20:18]** as long as the markets we are competing in are creating more value.
**[20:22]** And there are multiple winners.
**[20:24]** So I think that's the stuff.
**[20:25]** But I take your point that ultimately, it all means you have to get competitive.
**[20:30]** So I watch that every quarter.
**[20:32]** And so that's why I think I'm very optimistic that
**[20:35]** what we are going to do with GitHub HQ or Agent HQ,
**[20:39]** turning GitHub into a place where all these agents come.
**[20:43]** As I said, we'll have multiple shots on goal on there, right?
**[20:47]** It need not be that, hey, some of these guys can succeed along with us.
**[20:51]** And so it doesn't need to be just one winner and one subscription.
**[20:56]** I guess the reason to focus on this question is that it's not just about GitHub,
**[20:59]** but fundamentally about Office and all the other software that Microsoft offers,
**[21:04]** which is that one vision you could have about how AI proceeds is that,
**[21:08]** look, the models are going to keep being hobbled,
**[21:12]** and you'll need this direct, visible observability all the time.
**[21:16]** And another vision is over time, these models can now,
**[21:20]** they're doing tasks that take two minutes.
**[21:21]** In the future, they'll be doing tasks that take 10, 30 minutes.
**[21:24]** In the future, maybe they're doing days worth of work autonomously.
**[21:28]** And then the model companies are charging thousands of dollars maybe
**[21:32]** for access to really a co-worker,
**[21:34]** which could use any UI to communicate with their human and so forth
**[21:39]** and migrate between platforms.
**[21:41]** So if we're getting closer to that,
**[21:43]** why aren't the model companies that are just getting more and more profitable,
**[21:48]** the ones that are taking all the margin?
**[21:49]** Why is the place where the scaffolding happens,
**[21:52]** which becomes less and less relevant as AI has become more capable,
**[21:55]** going to be that important?
**[21:56]** And that goes to, you know, office as it exists now
**[21:58]** versus co-workers that are just doing knowledge.
**[22:00]** I think that's a great point.
**[22:01]** I mean, I think that's a great, I mean, for example,
**[22:03]** I mean, this is where, you know,
**[22:04]** does all the value migrate just to the model?
**[22:09]** And, or does the, you know,
**[22:11]** does it get split between the scaffolding and the model and what have you?
**[22:16]** I think that time will tell,
**[22:19]** but my fundamental point also is the incentive structure gets clear, right?
**[22:23]** Which is if you take, let's take,
**[22:25]** let's take information, we'll take even coding.
**[22:29]** Already, in fact, one of the favorite settings I have in GitHub Copilot
**[22:34]** is called auto, right?
**[22:36]** Which will just optimize.
**[22:38]** In fact, I buy a subscription,
**[22:40]** the auto one will start picking and optimizing
**[22:44]** for what I'm asking it to do.
**[22:47]** And it could even be fully autonomous
**[22:48]** and it could sort of arbitrage the tokens available
**[22:51]** across multiple models to go get a task done.
**[22:54]** So if that is the, that means that,
**[22:56]** if you take that argument,
**[22:58]** the commodity there will be models.
**[23:01]** And especially with open source models,
**[23:02]** you can pick a checkpoint
**[23:04]** and you can take a bunch of your data
**[23:06]** and you're seeing it, right?
**[23:07]** I think all of us will start,
**[23:09]** whether it's from Cursor or from Microsoft,
**[23:11]** you'll start seeing some in-house models even,
**[23:14]** which will, and then you'll offload most of your tasks to it.
**[23:19]** So I think that one argument is if you win the scaffolding,
**[23:23]** which today is dealing with all the hobbling problems
**[23:27]** or the jaggedness of this intelligence problems,
**[23:31]** which you kind of have to.
**[23:33]** If you win that,
**[23:34]** then you will vertically integrate yourself into the model,
**[23:37]** just because you will have the liquidity of the data
**[23:40]** and what have you,
**[23:40]** and there are enough and more checkpoints
**[23:42]** that are going to be available.
**[23:43]** That's the other thing.
**[23:44]** So structurally, I think,
**[23:46]** there will always be an open source model.
**[23:49]** That will be fairly capable in the world
**[23:52]** that you could then use
**[23:54]** as long as you have something that you can use that with,
**[23:58]** which is data and a scaffolding, right?
**[24:00]** So I can make the argument that,
**[24:02]** oh my God, if you're a model company,
**[24:04]** you may have a winner's curse.
**[24:06]** You may have done all the hard work,
**[24:08]** done unbelievable innovation,
**[24:10]** except it's kind of like one copy away
**[24:15]** from that being commoditized.
**[24:17]** And then the person who has the data
**[24:19]** for grounding and context engineering
**[24:23]** and the liquidity of data
**[24:25]** can then go take that checkpoint and train it.
**[24:27]** So I think the argument can be made both ways.
**[24:30]** Unpacking sort of what you said,
**[24:31]** there's two views of the world, right?
**[24:32]** One is that models,
**[24:34]** there's so many different models out there.
**[24:35]** Open source exists.
**[24:37]** There will be differences between the models
**[24:39]** that will drive some level of who wins and who doesn't,
**[24:42]** but the scaffolding is what enables you to win.
**[24:45]** The other view is that actually models are the key IP.
**[24:49]** And yes, everyone's in a tight race
**[24:51]** and there's some, hey, I can use Anthropic or OpenAI.
**[24:55]** And you can see this in the revenue charts, right?
**[24:56]** Like OpenAI's revenue started skyrocketing
**[24:58]** once they finally had a code model,
**[25:00]** similar capabilities to Anthropic,
**[25:02]** although in different ways.
**[25:05]** There's the view that the model companies
**[25:06]** are actually the ones that garner all the margin, right?
**[25:09]** Because if you look across this year,
**[25:11]** at least on Anthropic,
**[25:12]** their gross margins on inference
**[25:14]** went from well below 40% to north of 60, right?
**[25:18]** By the end of the year,
**[25:20]** the margins are expanding there despite,
**[25:22]** hey, more Chinese open source models than ever.
**[25:24]** Hey, OpenAI's competitive.
**[25:25]** Hey, Google's competitive.
**[25:26]** Hey, Grok is now competitive, right?
**[25:28]** All these companies are now competitive.
**[25:30]** And yet, despite this,
**[25:32]** the margins have expanded at the model layer significantly.
**[25:36]** How do you think about the-
**[25:37]** It's a great question.
**[25:39]** I think the one thing is perhaps a few years ago,
**[25:43]** people were saying,
**[25:44]** oh, I can just wrap a model and build a successful company.
**[25:48]** And that, I think, has probably gotten debunked
**[25:51]** just because the model capabilities
**[25:53]** and the tools used in particular.
**[25:56]** But the interesting thing is there's no-
**[25:57]** Like when I look at Office 365,
**[25:59]** let's take even this little thing we built
**[26:01]** called Excel Agent.
**[26:03]** It's interesting, right?
**[26:04]** Excel Agent is not a UI level wrapper.
**[26:07]** It's actually a model that is in the middle tier.
**[26:12]** In this case, because we have all the IP
**[26:14]** from the GPT family,
**[26:16]** we are taking that and putting it
**[26:19]** into the core middle tier of the Office system
**[26:23]** to both teach it what it means
**[26:26]** to natively understand Excel, everything in it.
**[26:30]** So it's not just, hey,
**[26:31]** I just have a pixel level understanding.
**[26:33]** I have a full understanding
**[26:34]** of all the native artifacts of Excel,
**[26:37]** both when I see it, like,
**[26:39]** because if you think about it,
**[26:39]** if I'm going to give it some reasoning task,
**[26:42]** right, I need to even fix
**[26:44]** the reasoning mistakes I make.
**[26:45]** And so that means I need to both
**[26:47]** not just see the pixels,
**[26:48]** I need to be able to see,
**[26:49]** oh, I got that formula wrong
**[26:50]** and I need to understand that.
**[26:52]** And then, so to some degree,
**[26:54]** that's all being done
**[26:54]** not at the UI wrapper level with some prompt,
**[26:57]** but it's being done in the middle tier
**[26:59]** by teaching it all the tools of Excel, right?
**[27:01]** So I'm giving it even essentially a markdown
**[27:04]** to teach it the skills
**[27:05]** of what it means to be a sophisticated Excel user.
**[27:08]** So it's a weird thing that it goes back
**[27:10]** a little bit to AI brain, right?
**[27:12]** Which is you're building not just Excel,
**[27:15]** you are now business logic
**[27:17]** in its traditional sense.
**[27:19]** You're taking the Excel business logic
**[27:21]** in the traditional sense
**[27:22]** and wrapping essentially a cognitive layer to it
**[27:25]** using this model,
**[27:27]** which knows how to use the tool.
**[27:29]** So in some sense,
**[27:30]** Excel will come with an analyst bundled in
**[27:33]** and with all the tools used.
**[27:35]** That's the type of stuff
**[27:37]** that'll get built by everybody.
**[27:38]** So even for the model companies,
**[27:40]** they'll have to compete, right?
**[27:41]** So if their price stuff high,
**[27:44]** guess what?
**[27:44]** If I'm a builder of a tool like this,
**[27:47]** I'll substitute you.
**[27:48]** I may use you for a while.
**[27:50]** And so as long as there's competition,
**[27:52]** there's always a winner-take-all thing, right?
**[27:53]** If there's gonna be one model
**[27:54]** that is better than everybody else
**[27:56]** with massive distance,
**[27:57]** yes, that's a winner-take-all.
**[27:59]** As long as there's gonna be competition
**[28:00]** where there's multiple models,
**[28:02]** just like hyperscale competition,
**[28:03]** and there's an open source check,
**[28:06]** there is enough room here
**[28:08]** to go build value on top of models.
**[28:11]** But at Microsoft,
**[28:12]** the way I look at it and say is,
**[28:14]** we are going to be
**[28:16]** in the hyperscale business,
**[28:17]** which will support multiple models.
**[28:19]** We will have access to open AI models
**[28:22]** for seven more years,
**[28:24]** which we will innovate on top of.
**[28:26]** So royalty,
**[28:27]** essentially, I think of ourselves
**[28:28]** as having a frontier class model
**[28:30]** that we can use and innovate on
**[28:32]** with full flexibility.
**[28:34]** And we'll build our own models with MAI.
**[28:38]** And so we will always have a model level.
**[28:41]** And then we'll build these,
**[28:43]** whether it's in security,
**[28:44]** whether it's in knowledge work,
**[28:45]** whether it's in coding or in science,
**[28:47]** we will build our own application scaffolding,
**[28:50]** which will be model forward, right?
**[28:52]** It won't be a wrapper on a model,
**[28:54]** but the model will be wrapped
**[28:56]** into the application.
**[28:58]** I have so many questions
**[28:59]** about the other things you mentioned,
**[29:01]** but before we move on to those topics,
**[29:03]** I still wonder whether this is like
**[29:05]** not forward-looking on AI capabilities,
**[29:08]** where you're imagining models
**[29:10]** like they exist today,
**[29:11]** where, yeah, it takes a screenshot
**[29:14]** of your screen,
**[29:14]** but it can't look inside each cell
**[29:16]** and what the formula is.
**[29:17]** And I think the better mental model here
**[29:18]** is like, look, a human,
**[29:20]** just imagine that these models
**[29:21]** actually will be able to actually
**[29:22]** use a computer as well as a human.
**[29:24]** And a human knowledge worker
**[29:26]** who is using Excel
**[29:27]** can look into the formulas,
**[29:29]** can use alternative software,
**[29:31]** can migrate data between Office 365
**[29:33]** and another piece of software
**[29:34]** if the migration is necessary, etc.
**[29:36]** So, what is-
**[29:37]** That's kind of what I'm saying.
**[29:38]** So, what-
**[29:38]** But if that's the case,
**[29:40]** then the integration with Excel
**[29:41]** doesn't matter that much.
**[29:42]** No, no, don't worry
**[29:43]** about the Excel integration.
**[29:46]** After all, Excel was built
**[29:47]** as a tool for analysts.
**[29:49]** Great.
**[29:50]** So, whoever is this AI
**[29:52]** that is an analyst
**[29:54]** should have tools
**[29:55]** that they can use.
**[29:56]** In the computer, right?
**[29:57]** Just the way a human can use a computer,
**[29:58]** that's their tool.
**[30:00]** The tool is the computer.
**[30:01]** Right.
**[30:01]** Right. So all I'm saying is I'm building an analyst as
**[30:05]** essentially an AI agent which happens to come
**[30:09]** with an a priori knowledge of
**[30:11]** how to use all of these analytical tools.
**[30:14]** But is it something, maybe
**[30:16]** just to make sure we're talking about the same thing.
**[30:18]** Is it a thing that a huge,
**[30:20]** like me using Excel as a podcaster,
**[30:22]** I'm not proficient in Excel.
**[30:23]** No, no, no. Completely autonomous.
**[30:25]** So just imagine I work,
**[30:27]** so we should now maybe sort of lay out how I
**[30:29]** think the future of the company is, right?
**[30:31]** The future of the company would be
**[30:33]** the tools business which I have a computer,
**[30:36]** I use Excel, and in fact,
**[30:38]** in the future, I'll even have a co-pilot,
**[30:40]** and that co-pilot will also have agents, right?
**[30:42]** That's still I am,
**[30:44]** it's still me steering everything,
**[30:46]** and everything is coming back.
**[30:48]** So that's kind of one world.
**[30:49]** Then the second world is,
**[30:51]** the company just literally provisions
**[30:54]** a computing resource for an AI agent,
**[30:57]** and that is working fully autonomously.
**[30:59]** That fully autonomous agent will have
**[31:03]** essentially embodied set of those same tools.
**[31:06]** Right.
**[31:06]** That are available to it, right?
**[31:08]** So this AI tool that comes in,
**[31:11]** also has not just a raw computer,
**[31:14]** because it's going to be more token efficient
**[31:16]** to use tools to get stuff done.
**[31:18]** In fact, I kind of look at it and say our business,
**[31:21]** which today is an end-user tools business,
**[31:23]** will become essentially
**[31:25]** an infrastructure business in support of agents doing work.
**[31:28]** It's another way to think about it, right?
**[31:31]** So if one of the things that you'll see us do,
**[31:33]** in fact, like all the stuff we built underneath M365,
**[31:38]** still is going to be very relevant.
**[31:41]** You need some place to store it,
**[31:43]** some place to do archival,
**[31:45]** some place to do discovery,
**[31:46]** some place to manage all of these activities,
**[31:49]** even if you're an AI agent.
**[31:51]** So it's kind of a new infrastructure.
**[31:54]** So just to make sure I understand,
**[31:56]** you're saying like, look,
**[31:57]** theoretically, a future AI that has actual computer use,
**[32:01]** which is all these companies are working on,
**[32:02]** model companies are working right now,
**[32:03]** could use, even if it's not partnered with
**[32:06]** Microsoft or under our umbrella,
**[32:07]** could use Microsoft software.
**[32:09]** But you're saying we're going to give them,
**[32:11]** if you're working with our infrastructure,
**[32:13]** we're going to give you lower level access
**[32:16]** that makes it more efficient for you to do
**[32:17]** the same things you could have otherwise done anyways.
**[32:19]** A hundred percent. I mean, so the entire thing,
**[32:21]** in fact, what happened is we had servers,
**[32:26]** then there was virtualization,
**[32:27]** and then we had many more servers.
**[32:30]** So that's another way to think about this,
**[32:32]** which is, hey, don't think of the tool as the end thing.
**[32:35]** What is the entire substrate
**[32:37]** underneath that tool that humans use?
**[32:40]** That entire substrate is
**[32:42]** the bootstrap for the AI agent as well,
**[32:45]** because the AI agent needs a computer.
**[32:46]** That's kind of one. So in fact,
**[32:48]** one of the fascinating things we are
**[32:50]** seeing a significant amount of growth
**[32:51]** is all these guys who are doing
**[32:53]** these office artifacts and what have you,
**[32:56]** as autonomous agents and so on,
**[32:58]** want to provision Windows 365.
**[33:00]** They really want to be able to provision
**[33:02]** a computer for these agents.
**[33:05]** So absolutely, and that's why I think we're going to have
**[33:08]** essentially an end-user computing infrastructure business,
**[33:12]** which I think is going to just keep
**[33:14]** growing because guess what?
**[33:15]** It's going to grow faster than the number of users.
**[33:17]** So in fact, that's one of the other questions people
**[33:19]** ask me is, hey, what happens to the per-user business?
**[33:22]** At least the early signs may be,
**[33:23]** the way to think about the per-user business
**[33:25]** is not just per-user, it's per-agent.
**[33:28]** If you say it's per-user and per-agent,
**[33:31]** the key is what's the stuff to provision for every agent?
**[33:35]** A computer, a set of security things around it,
**[33:39]** an identity around it,
**[33:41]** and all those things are observability and so on,
**[33:44]** are the management layers,
**[33:45]** and that's, I think, all going to get baked into that.
**[33:48]** The way to frame it,
**[33:49]** at least the way I currently think about it,
**[33:51]** and I'd like to hear your view,
**[33:52]** is that these model companies are all building environments
**[33:56]** to train their models to use Excel or Amazon Shopping
**[34:00]** or whatever it is, Book Flights.
**[34:03]** But at the same time, they're also training these models
**[34:06]** to do migration from,
**[34:08]** because that is probably the most immediate,
**[34:11]** valuable thing, right?
**[34:12]** Converting mainframe-based systems
**[34:14]** to standard cloud systems,
**[34:15]** converting Excel databases into real databases with SQL,
**[34:21]** or converting what is done in Word and Excel
**[34:26]** to something that is more programmatic and more efficient
**[34:29]** in a classical sense
**[34:30]** that can actually be done by humans as well.
**[34:32]** It's just not cost-effective
**[34:34]** for the software developer to do that.
**[34:35]** That seems to be what everyone is going to do with AI
**[34:37]** for the next few years, at least, to massively drive value.
**[34:42]** How does Microsoft fit into that
**[34:44]** if the models can utilize the tools themselves
**[34:47]** to migrate to something?
**[34:48]** And yes, Microsoft has a leadership position in databases
**[34:52]** and in storage and in all these other categories,
**[34:55]** but the use of, say, a office ecosystem
**[35:00]** is going to be significantly less,
**[35:01]** just like potentially the use of a mainframe ecosystem
**[35:04]** could be potentially less.
**[35:05]** Now, mainframes have grown for the last two decades,
**[35:07]** actually, even though no one talks about them anymore,
**[35:09]** they've still grown.
**[35:10]** Yeah, 100%, I agree with that.
**[35:11]** How does that flow forward?
**[35:13]** At the end of the day, this is not about sort of,
**[35:14]** hey, there is going to be a significant amount of time
**[35:18]** where there's going to be a hybrid world, right?
**[35:20]** Because people are going to be using the tools
**[35:22]** that are going to be working with agents
**[35:23]** that have to use tools.
**[35:24]** And by the way, they have to communicate with each other.
**[35:27]** What's the artifact I generate
**[35:28]** that then a human needs to see?
**[35:30]** So like all of these things
**[35:32]** will be real considerations in any place.
**[35:34]** So the outputs, inputs.
**[35:35]** So I don't think it'll just be about,
**[35:36]** oh, I migrated off, right?
**[35:37]** But the bottom line is I have to live in this hybrid world.
**[35:40]** But that doesn't fully answer your question
**[35:42]** because there can be a real new efficient frontier
**[35:45]** where it's just agents working with agents
**[35:48]** and completely optimizing.
**[35:50]** And even when agents are working with agents,
**[35:52]** what are the primitives that are needed?
**[35:55]** Do you need a storage system?
**[35:57]** Does that storage system need to have e-discovery?
**[36:00]** Does that e-discovery, do you need to have observability?
**[36:03]** Do you need to have an identity system
**[36:05]** that is going to use multiple models
**[36:06]** with all having one identity system?
**[36:09]** So these are all the core underlying rails
**[36:12]** we have today for what are office systems or what have you.
**[36:16]** And that's what I think we will have in the future as well.
**[36:18]** You talked about databases, right?
**[36:20]** I mean, take, you know, man,
**[36:21]** I would love all of Excel to have a database backend, right?
**[36:24]** In fact, I would love for all that to happen immediately.
**[36:28]** And that database is a good database.
**[36:30]** I mean, databases, in fact,
**[36:31]** will be a big thing that'll grow.
**[36:33]** In fact, if I think about all of the office artifacts
**[36:37]** being structured better,
**[36:39]** the ability to do the joins
**[36:40]** between structured and unstructured better
**[36:42]** because of the agenting work,
**[36:43]** that'll grow the underlying,
**[36:45]** what is infrastructure business.
**[36:47]** It happens, the consumption of that
**[36:48]** is all being driven by agents.
**[36:50]** You could say all that is just in time generated software
**[36:53]** by a model company.
**[36:54]** That could also be true.
**[36:55]** If we, we will be one such model company too.
**[36:58]** And so we will build in,
**[37:00]** so the competition could be that we will build a model
**[37:04]** plus all the infrastructure and provision it.
**[37:07]** And then there will be competition
**[37:08]** between a bunch of those folks who can do that.
**[37:11]** I guess, speaking of model companies,
**[37:13]** you say, okay, we will also be one of the,
**[37:15]** not only will have the infrastructure,
**[37:16]** we'll have the model itself.
**[37:18]** Right now, Microsoft AI's most recent model
**[37:20]** that was released two months ago is 36 in Chatbot Arena.
**[37:23]** And there's a, I mean,
**[37:25]** you obviously have the IP rights to OpenAI.
**[37:27]** So there's a question of,
**[37:28]** first, to the extent you agree with that,
**[37:30]** it seems to be behind.
**[37:31]** Why is that the case?
**[37:32]** Especially given the fact that you could,
**[37:34]** you theoretically have the right
**[37:36]** to just like fork OpenAI's monorepo
**[37:38]** or distill on their models.
**[37:41]** Yeah, especially if it's a big part of your strategy
**[37:43]** that we need to have a leading model company.
**[37:45]** Yeah, I mean, so first of all,
**[37:46]** we are absolutely going to use the OpenAI models
**[37:51]** to the maximum across all of our products, right?
**[37:54]** I mean, that's, I think, the core thing
**[37:56]** that we're going to continue to do
**[37:57]** all the way for the next seven years.
**[38:00]** And not just use it, but then add value to it.
**[38:03]** That's kind of where the analyst and this Excel agent,
**[38:06]** and these are all things that we will do
**[38:08]** where we'll do RL fine-tuning,
**[38:11]** we'll do some mid-training runs on top of a GPT family
**[38:14]** where we have unique data assets and build capability.
**[38:19]** The MAI model, the way I think we're going to think about it
**[38:22]** is the good news here, in fact, with the new agreement
**[38:25]** is even we can be very, very clear
**[38:27]** that we're going to build
**[38:28]** a world-class super intelligence team
**[38:30]** and go after it with high ambition.
**[38:32]** But at the same time, we're also going to use this time
**[38:35]** to be smart about how to use both these things.
**[38:38]** So that means we will, on one end, be very product-focused,
**[38:41]** and on the other end, be very research-focused.
**[38:44]** In other words, because we have access to the GPT family.
**[38:48]** The last thing I don't want to do is use my flops
**[38:51]** in a way that is just duplicative
**[38:53]** and doesn't add much value.
**[38:54]** So I want to be able to take the flops
**[38:57]** that we use to generate a GPT family
**[39:01]** and maximize its value,
**[39:02]** while my MAI flops are being used for,
**[39:05]** let's take the image model that we launched,
**[39:07]** which I think this launched,
**[39:09]** it's a number nine in the image arena.
**[39:12]** You know, we're using it, you know,
**[39:13]** both for cost optimization, it's on Copilot,
**[39:16]** it's in Bing, and we're going to use that.
**[39:18]** We have our audio model in Copilot,
**[39:20]** which really, it's got personality and what have you,
**[39:23]** we optimized it for our product.
**[39:24]** So we will do those.
**[39:25]** Even on the LM arena, we started on the text one,
**[39:28]** I think it was, it debuted at night 13,
**[39:31]** and by the way, it was done only on, whatever,
**[39:33]** 15,000 H100s, and so it was a very small model.
**[39:37]** And so it was, again, to prove out the core capability,
**[39:41]** the instruction following, and everything else,
**[39:43]** which, you know, we wanted to make sure
**[39:45]** we can match what was state of the art.
**[39:47]** And so that shows us, given scaling laws,
**[39:49]** what we are capable of doing
**[39:51]** if we gave more flops to it, right?
**[39:52]** So the next thing we will do is an Omni model
**[39:55]** where we will take sort of the work we've done in audio,
**[39:58]** what we have done in image, and what we have done in text.
**[40:01]** That'll be the next pit stop on the MAI side.
**[40:03]** So when I think about the MAI roadmap,
**[40:06]** we're going to build a first-class superintelligence team.
**[40:08]** We're going to continue to drop and do on in the open
**[40:11]** some of these models.
**[40:12]** They will either be in our products being used
**[40:15]** because they're going to be latency-friendly,
**[40:17]** COGS-friendly, or what have you,
**[40:18]** or they'll have some special capability.
**[40:21]** And we will do real research in order to be ready
**[40:24]** for some next five, six, seven, eight breakthroughs
**[40:28]** that are all needed on this march towards superintelligence.
**[40:30]** So I think that's, and while exploiting the advantage
**[40:35]** we have of having the GPT family
**[40:37]** that we can work on top of as well.
**[40:39]** Say we roll forward seven years.
**[40:41]** You no longer have access to open AI models.
**[40:43]** What does one get confidence,
**[40:45]** or what does Microsoft do to make sure they are leading,
**[40:49]** have a leading AI lab, right?
**[40:51]** Today, you know, it's all open AI has developed
**[40:53]** many of the breakthroughs, whether it be scaling
**[40:55]** or reasoning, or Google's developed all the breakthroughs
**[40:58]** like Transformers, but it is also a big talent game, right?
**[41:02]** You know, you've seen Meta spend, you know,
**[41:04]** north of $20 billion on talent, right?
**[41:07]** You've seen Anthropic poach the entire Blue Shift
**[41:10]** reasoning team from Google last year.
**[41:12]** You've seen Meta poach a large reasoning
**[41:14]** and post-training team from Google more recently.
**[41:16]** These sorts of talent wars are very capital-intensive.
**[41:19]** They're the ones that, you know, arguably, you know,
**[41:22]** if you're spending $100 billion on infrastructure,
**[41:24]** you should also spend, you know, X amount of money
**[41:27]** on the people using the infrastructure
**[41:29]** so that they're more efficiently
**[41:30]** making these new breakthroughs.
**[41:32]** What confidence can one get that, you know,
**[41:34]** hey, Microsoft will have a team that's world-class
**[41:37]** that can make these breakthroughs.
**[41:38]** And, you know, once you decide to turn on the money faucet,
**[41:41]** you know, you're being a bit capital-efficient right now,
**[41:43]** which is smart, it seems,
**[41:44]** to not waste money doing duplicative work.
**[41:47]** But once you decide you need to, you know,
**[41:49]** how can one say, oh, yeah, now you can shoot up
**[41:52]** to where the top five models are?
**[41:54]** Well, look, I mean, at the end of the day,
**[41:56]** we're going to build a world-class team,
**[41:57]** and we already have a world-class team
**[41:59]** that's beginning to be sort of assembled, right?
**[42:01]** With Mustafa coming in, we have Karen,
**[42:03]** we have Amar Subramanian,
**[42:05]** who did a lot of the post-training at Gemini,
**[42:07]** Tufai, who is at Microsoft,
**[42:08]** Nando, who did a lot of the multimedia work
**[42:11]** at DeepMind is there.
**[42:12]** And so we're going to build a world-class team.
**[42:15]** And in fact, I think later this week,
**[42:17]** even Mustafa published some, you know,
**[42:18]** a little more clarity on what our lab is going to go do.
**[42:22]** I think the thing that I want the world to know, perhaps,
**[42:27]** is we are going to build the infrastructure
**[42:30]** that will support multiple models.
**[42:33]** You know, we, because from a hyperscale perspective,
**[42:36]** we want to build the most scaled infrastructure fleet
**[42:40]** that's capable of supporting all the models the world needs,
**[42:44]** whether it's from open source
**[42:45]** or whether it's obviously from open AI and others.
**[42:47]** And so that's kind of one job.
**[42:49]** Second is in our own model capability,
**[42:51]** we will absolutely use the open AI model in our products
**[42:54]** and we'll start building our own models.
**[42:56]** And we may, like in GitHub Copilot, Anthropic is used.
**[42:59]** So we will even have other frontier models
**[43:02]** that are going to be wrapped into our products as well.
**[43:04]** So I think that that's kind of how, at least each time,
**[43:07]** at the end of the day, the eval of the product
**[43:10]** as it meets a particular task or a job is what matters.
**[43:13]** And we'll sort of back from there
**[43:15]** into the vertical integration needed,
**[43:18]** knowing that as long as you're serving the market well
**[43:21]** with the product, you can always cost optimize.
**[43:25]** There's a question going forward.
**[43:27]** So right now we have models that have this distinction
**[43:29]** between training and inference.
**[43:31]** And one could argue that there's like a smaller
**[43:34]** and smaller difference between the different models.
**[43:37]** Going forward, if you're really expecting something
**[43:38]** like human level intelligence, humans learn on the job.
**[43:42]** You know, if you think about your last 30 years,
**[43:43]** what makes Satya Token so valuable?
**[43:45]** It's the last 30 years of wisdom and experience
**[43:47]** you've gained in Microsoft.
**[43:49]** And we will eventually have models
**[43:51]** if they get to human level, which will have this ability
**[43:52]** to continuously learn on the job.
**[43:54]** And that will drive so much value to the model company
**[43:57]** that is ahead, at least in my view,
**[43:59]** because you have copies of one model
**[44:01]** broadly deployed through the economy,
**[44:02]** learning how to do every single job.
**[44:04]** And unlike humans, they can amalgamate their learnings
**[44:07]** to that model.
**[44:08]** So there's this sort of continuous learning
**[44:10]** sort of exponential feedback loop,
**[44:13]** which almost looks like a sort of intelligence explosion.
**[44:16]** If that happens and Microsoft isn't the leading
**[44:20]** model company by that time, doesn't then this,
**[44:24]** you know, you're saying,
**[44:25]** well, we substitute one model for another, et cetera,
**[44:27]** matter less, because they're just like,
**[44:28]** this one model knows how to do every single job
**[44:30]** of the economy.
**[44:31]** The other long tail don't.
**[44:33]** Yeah, no, I think that your point about
**[44:34]** if there's one model that is the only model
**[44:37]** that is most broadly deployed in the world
**[44:39]** and it sees all the data and it does continuous learning,
**[44:42]** that's game set match and, you know, it's shot sharp, right?
**[44:44]** I mean, the reality, at least I see,
**[44:49]** is the world, even today,
**[44:54]** for all the dominance of any one model,
**[44:56]** it's not the case.
**[44:58]** It's like, take coding.
**[45:01]** There's multiple models.
**[45:02]** In fact, every day, it's less the case
**[45:05]** where there is not one model
**[45:07]** that is getting deployed broadly.
**[45:08]** In fact, there's multiple models that are getting deployed.
**[45:11]** It's kind of like databases, right?
**[45:12]** It's always the thing, it's like,
**[45:13]** hey, can one database be the one
**[45:15]** that just is used everywhere?
**[45:17]** Except it's not.
**[45:18]** There are multiple types of databases
**[45:20]** that are getting deployed for different use cases.
**[45:23]** So I think that there is going to be some network effects
**[45:26]** of continual learning or data, you know,
**[45:29]** I'll call liquidity that any one model has.
**[45:32]** Is it gonna happen in all domains?
**[45:34]** I don't think so.
**[45:35]** Is it gonna happen in all geos?
**[45:37]** I don't think so.
**[45:38]** Is it gonna happen in all segments?
**[45:39]** I don't think so.
**[45:40]** It'll happen in all categories at the same time?
**[45:42]** I don't think so.
**[45:43]** Therefore, I feel like the design space is so large
**[45:46]** that there's plenty of opportunity.
**[45:49]** But your fundamental point is having a capability
**[45:52]** which is at the infrastructure layer, model layer,
**[45:55]** and at the scaffolding layer,
**[45:58]** and then to be able to compose these things
**[46:00]** not just as a vertical stack,
**[46:02]** but to be able to compose each thing
**[46:04]** for what its purpose is, right?
**[46:05]** You can't build an infrastructure
**[46:06]** that's optimized for one model.
**[46:08]** If you do that, what if you go fall behind?
**[46:10]** In fact, all the infrastructure you built
**[46:13]** will be a waste, right?
**[46:14]** You kind of need to build an infrastructure
**[46:16]** that's capable of supporting multiple sort of families
**[46:20]** and lineages of models.
**[46:21]** Otherwise, the capital you put in,
**[46:23]** which is optimized for one model architecture,
**[46:25]** that means you're one tweak away
**[46:27]** from some MOE-like breakthrough
**[46:29]** that happens with somebody else
**[46:30]** and your entire network topology goes out of the window,
**[46:33]** then that's a scary thing, right?
**[46:34]** So therefore, you kind of want the infrastructure
**[46:37]** to support whatever may come,
**[46:39]** in fact, in your own model family and other model families.
**[46:42]** And you've got to be open.
**[46:43]** If you're serious about the hyperscale business,
**[46:45]** you've got to be serious about that, right?
**[46:47]** If you're serious about being a model company,
**[46:50]** you've got to basically say,
**[46:51]** hey, what are the ways people can actually do things
**[46:54]** on top of the model so that I can have an ISV ecosystem
**[46:58]** unless I'm thinking I'll own every category.
**[47:00]** That just can't be.
**[47:00]** Then you won't have an API business.
**[47:02]** And that, by definition, will mean you'll never be
**[47:05]** a platform company that's going to be
**[47:07]** successfully deployed everywhere, right?
**[47:09]** So therefore, the industry structure is such
**[47:13]** that it will really force people to specialize.
**[47:18]** And in that specialization,
**[47:21]** a company like Microsoft should compete in each layer
**[47:25]** by its merits, but not think that this is all about
**[47:29]** all a road to game, set, match,
**[47:31]** where I just compose vertically all these layers.
**[47:34]** That just doesn't happen.
**[47:36]** So according to Dylan's numbers,
**[47:38]** there's going to be half a trillion in AI CapEx
**[47:40]** next year alone.
**[47:42]** And labs are already spending billions of dollars
**[47:44]** to snag top researcher talent.
**[47:46]** But none of that matters if there's not enough
**[47:48]** high quality data to train on.
**[47:49]** Without the right data,
**[47:51]** even the most advanced infrastructure
**[47:52]** and world-class talent won't translate
**[47:55]** into end value for the user.
**[47:57]** That's where LibreVox comes in.
**[47:59]** LibreVox produces high quality data at massive scale,
**[48:03]** powering any capability that you want your model to have.
**[48:06]** It doesn't matter whether you need a coding agent
**[48:08]** that needs detailed feedback on multi-hour trajectories
**[48:11]** or a robotics model that needs thousands of samples
**[48:14]** on everyday tasks, or a voice agent
**[48:16]** that can also perform real world actions for the user,
**[48:18]** like booking them a flight.
**[48:20]** To be clear, this isn't just off the shelf data.
**[48:22]** LibreVox can design and launch
**[48:25]** a custom production scale data pipeline in 48 hours.
**[48:29]** And they can get you tens of thousands
**[48:31]** of targeted examples in weeks.
**[48:33]** Reach out at librevox.com slash Dwarkesh.
**[48:38]** All right, back to Satya.
**[48:42]** So last year, Microsoft was on path
**[48:44]** to be the largest infrastructure provider by far.
**[48:47]** You were the earliest in 23.
**[48:48]** So you went out there, you acquired all the resources
**[48:51]** in terms of leasing data centers, starting construction,
**[48:53]** securing power, everything.
**[48:54]** You guys were on pace to beat Amazon in 26 or 27.
**[48:59]** But certainly by 28, you were gonna beat them.
**[49:01]** Since then, in let's call it the second half of last year,
**[49:05]** Microsoft did this big pause, right?
**[49:07]** Where they let go of a bunch of leasing sites
**[49:10]** that they were gonna take, which then Google, Meta,
**[49:13]** Amazon in some cases, Oracle, took these sites.
**[49:17]** We're sitting in one of the largest data centers in the world
**[49:19]** so obviously it's not everything.
**[49:20]** You guys are expanding like crazy.
**[49:22]** But there are sites that you just stopped working on.
**[49:24]** Why did you do this, right?
**[49:26]** Yeah, I mean, the fundamental thing,
**[49:30]** this goes back a little bit
**[49:31]** to what is the hyperscale business all about, right?
**[49:34]** Which is one of the key decisions we made
**[49:37]** was that if you're gonna build out Azure to be fantastic
**[49:42]** for all sort of stages of AI,
**[49:46]** from training to mid-training to data gen to inference,
**[49:51]** we just need fungibility of the fleet.
**[49:55]** And so that entire thing cost us
**[49:59]** not to basically go build a whole lot of capacity
**[50:03]** with a particular set of generations.
**[50:06]** Because the other thing that you gotta realize
**[50:08]** is having actually for up to now 10x every 18 months
**[50:13]** enough training capacity for the various open AI models.
**[50:17]** We realized that the key is to stay on that path,
**[50:22]** but the more important thing is to actually have a balance
**[50:26]** to not just train but to be able to serve these models
**[50:29]** all around the world.
**[50:30]** Because at the end of the day,
**[50:31]** the rate of monetization is what then will allow us
**[50:33]** to even keep funding.
**[50:35]** And then the infrastructure was going to need us to support,
**[50:39]** as I said, multiple models and what have you.
**[50:41]** So once we said that that's the case,
**[50:43]** since then we just course-corrected to the path we're on,
**[50:47]** right?
**[50:48]** If I look at the path we're on
**[50:49]** is we are doing a lot more starts now.
**[50:52]** We are also buying up as much capacity as we can,
**[50:55]** whether it's to build, whether it's to lease,
**[50:57]** or even GPUs as a service.
**[50:59]** But we are building it for where we see the demand
**[51:02]** and the serving needs and our training needs.
**[51:05]** And we didn't want to just be a hoster for one company
**[51:10]** and have just a massive book of business with one customer.
**[51:14]** That's not a business, right?
**[51:15]** That is sort of, you should be vertically integrated
**[51:18]** with that company.
**[51:19]** And so given the thing that OpenAI
**[51:22]** was going to be a successful independent company,
**[51:24]** which is fantastic, right?
**[51:26]** I think it makes sense, right?
**[51:28]** And even Meta may use third-party capacity,
**[51:30]** but ultimately they're all going to be first party.
**[51:33]** For anyone who has large scale,
**[51:36]** there'll be a hyperscaler on their own.
**[51:38]** And so to me was to build out a hyperscale fleet
**[51:42]** and our own research compute.
**[51:45]** And that's what the adjustment was.
**[51:48]** And so I feel very, very good.
**[51:49]** Oh, by the way, the other thing is
**[51:51]** I didn't want to get stuck
**[51:53]** with massive scale of one generation.
**[51:56]** I mean, we just saw the GB200s.
**[51:58]** I mean, the GB300s are coming, right?
**[52:00]** And by the time I get to Vera Rubin, Vera Rubin Ultra,
**[52:03]** guess what?
**[52:04]** The data center is going to look very different
**[52:06]** because the power per rack, power per row
**[52:09]** is going to be so different.
**[52:11]** The cooling requirements are going to be so different.
**[52:13]** And that means I don't want to just go build out
**[52:16]** like a whole number of gigawatts
**[52:18]** that are only for a one generation, one family.
**[52:22]** And so I think the pacing matters
**[52:24]** and the fungibility and the location matters.
**[52:28]** The workload diversity matters, customer diversity matters.
**[52:31]** And that's what we're building towards.
**[52:33]** The other thing that we've learned a lot is
**[52:36]** every AI workload does require not only the AI accelerator,
**[52:40]** but it requires a whole lot of other things, right?
**[52:42]** And in fact, a lot of the margin structure for us
**[52:44]** will be in those other things.
**[52:46]** And so therefore we want to build out Azure
**[52:49]** as being fantastic for the long tail of the workloads
**[52:53]** because that's the hyperscale business.
**[52:55]** While knowing that we've got to be super competitive
**[52:58]** starting with the bare metal for the highest end training.
**[53:02]** And, but that can't crowd out the rest of the business,
**[53:05]** right?
**[53:06]** Because we're not in the business
**[53:07]** of just doing five contracts with five customers
**[53:10]** being their bare metal service.
**[53:12]** That's not a Microsoft business.
**[53:14]** That may be a business for someone else
**[53:16]** and that's a good thing.
**[53:17]** What we have said is we are in the hyperscale business,
**[53:19]** which is at the end of the day,
**[53:20]** a long tail business for AI workloads.
**[53:25]** And in order to do that,
**[53:26]** we will have some leading bare metal
**[53:28]** as a service capabilities for a set of models,
**[53:32]** including our own.
**[53:33]** And that I think is the balance you see.
**[53:36]** Another sort of question that comes around
**[53:37]** this whole fungibility topic is,
**[53:40]** okay, it's not where you want it, right?
**[53:41]** You would rather have it in a good population center
**[53:43]** like Atlanta as we're here.
**[53:46]** There's also the question of like,
**[53:48]** well, how much does that matter
**[53:49]** if as the horizon of AI tasks grows?
**[53:52]** Well, actually, 30 seconds for a reasoning prompt
**[53:56]** or 30 minutes for a deep research,
**[53:58]** or it's going to be hours for software agents at some point
**[54:01]** and days and so on and so forth,
**[54:03]** the time to human interaction.
**[54:05]** Why does it matter if it's location A, B or C?
**[54:09]** That's exactly right.
**[54:10]** So in fact, that's one of the other reasons
**[54:12]** why we want to think about like,
**[54:13]** hey, what is an Azure region look like?
**[54:15]** And what is the, in fact,
**[54:16]** the networking between Azure regions?
**[54:18]** So this is where I think as the model capabilities evolve,
**[54:21]** and I think the usage of these tokens,
**[54:24]** whether it's synchronously or asynchronously evolves,
**[54:27]** and in fact, you don't want to be out of position, right?
**[54:29]** Then on top of that, by the way,
**[54:31]** what are the data residency laws, right?
**[54:34]** Where do I, like, I mean, the entire EU thing
**[54:37]** for us where we literally had to create an EU data boundary
**[54:40]** basically meant that you can't just round trip a call
**[54:43]** to wherever, even if it's asynchronous.
**[54:46]** And so therefore you need to have maybe regional things
**[54:48]** that are high density and the power costs and so on.
**[54:51]** But you're 100% right in bringing up
**[54:54]** that the topology as we build out
**[54:58]** will have to evolve one for tokens per dollar per watt.
**[55:03]** What are the economics?
**[55:05]** So overlay that with what is the usage pattern?
**[55:09]** Usage pattern in terms of synchronous, asynchronous,
**[55:12]** but also what is the compute storage?
**[55:14]** Because the latencies may matter for certain things.
**[55:16]** The storage better be there.
**[55:18]** If I have a Cosmos DB close to this for session data,
**[55:21]** or even for an autonomous thing,
**[55:22]** then that also has to be somewhere close to it and so on.
**[55:26]** So I think that all of those considerations
**[55:28]** is what will shape the hyperscale business.
**[55:32]** You know, prior to the pause you were, you know,
**[55:34]** versus, you know, what we had forecasted for you by 28,
**[55:37]** you're going to be like 12, 13 gigawatts.
**[55:40]** And now we're at, you know, nine and a half or so, right?
**[55:42]** But, you know, something that's even more relevant, right?
**[55:44]** And it's, you know, I just want you to like
**[55:46]** more concretely state that this is the business
**[55:48]** you don't want to be in,
**[55:49]** but like Oracle's going from like one fifth your size
**[55:52]** to bigger than you by end of 2027.
**[55:55]** And while it's not a Microsoft level
**[55:58]** quality of return on invested capital, right?
**[56:00]** They're still making 35% gross margins, right?
**[56:03]** It's sort of the question is like,
**[56:04]** does it, is it, isn't it, is it, is it, you know,
**[56:07]** hey, it's not Microsoft's business to maybe do this.
**[56:10]** But you've created a hyperscaler now
**[56:11]** by refusing this business,
**[56:13]** by giving away the right of first refusal, et cetera.
**[56:16]** I'm not, first of all, I don't want to take away
**[56:18]** anything from the success Oracle has had
**[56:21]** in building their business and I wish them well.
**[56:23]** And so the thing that I think I've answered for you is
**[56:26]** it didn't make sense for us to go be a host
**[56:31]** for one model company with limited time horizon RPO.
**[56:37]** Let's just put it that way, right?
**[56:39]** The thing that you have to think through
**[56:40]** is not what you do in the next five years,
**[56:42]** but what do you do for the next 50?
**[56:45]** Because that's kind of what I,
**[56:47]** we made our set of decisions.
**[56:49]** I feel very good about our open AI partnership
**[56:52]** and what we're doing.
**[56:53]** We have a decent book, a book of business.
**[56:55]** We wish them a lot of success.
**[56:57]** In fact, we are buyers of Oracle capacity.
**[56:59]** We wish them success.
**[57:01]** But you know, at this point,
**[57:02]** I think the industrial logic for what we are trying to do
**[57:06]** is pretty clear, which is it's not about like chasing,
**[57:09]** first of all, I track, by the way, your things,
**[57:11]** whether it's the AWS or the Google and ours,
**[57:14]** which I think is super useful,
**[57:16]** but doesn't mean I got to chase those.
**[57:20]** I have to chase them for not just the gross margin
**[57:23]** that they may represent in a period of time.
**[57:26]** You know, what is this book of business
**[57:28]** that Microsoft uniquely can go clear,
**[57:31]** which makes sense for us to clear?
**[57:33]** And that's what we'll do.
**[57:34]** I guess I have a question, even stepping back from this of,
**[57:37]** okay, I take your point that it's a better business
**[57:40]** to be an all else equal,
**[57:41]** to have a long tail of customers
**[57:43]** who can have higher margin
**[57:44]** from rather than serving bare metal to a few labs.
**[57:49]** But then there's a question of,
**[57:50]** okay, which way is the industry evolving?
**[57:51]** And so if we believe we're on the path
**[57:53]** to smarter and smarter AIs,
**[57:55]** then why isn't the shape of the industry
**[57:58]** that the open AIs and Anthropics and DeepMinds
**[58:01]** are the platform which the long tail of enterprises
**[58:05]** are actually doing business with,
**[58:07]** where they need bare metal,
**[58:08]** but like they are the platform.
**[58:09]** What is the long tail that is directly using Azure?
**[58:14]** Because you know, you want to use the general-
**[58:16]** But those models are going to be available on Azure, right?
**[58:19]** So any workload that says,
**[58:20]** hey, I want to use, you know,
**[58:22]** some open source model and an open AI model.
**[58:25]** Like, I mean, if you go to Azure Foundry today,
**[58:27]** you have all these models that you can provision,
**[58:29]** buy PTUs, get a Cosmos DB, get a SQL DB,
**[58:33]** get some storage, get some compute.
**[58:34]** That's what a real workload looks like.
**[58:36]** A real workload is not just,
**[58:37]** hey, I did an API call to a model.
**[58:40]** A real workload needs all of these things
**[58:44]** to go build an app or instantiate an application.
**[58:47]** In fact, the model companies need that, right?
**[58:49]** To build anything, it's just not like
**[58:51]** I have a token factory.
**[58:52]** I have to have all of these things.
**[58:54]** That's the hyperscale business.
**[58:56]** And it's not only one model, but all these models.
**[58:59]** And so if you want Grok plus, let's say,
**[59:02]** open AI plus an open source model,
**[59:05]** come to Azure Foundry, provision them,
**[59:07]** build your application.
**[59:08]** Here is a database.
**[59:09]** That's kind of what the business is.
**[59:13]** There is a separate business called
**[59:14]** just selling raw bare metal services to model companies.
**[59:17]** And that's the argument about how much of that business
**[59:20]** you want to be in and not be in.
**[59:22]** And what is that?
**[59:23]** It's a very different segment of the business,
**[59:25]** which we are in, and we also have limits
**[59:28]** to how much of it is going to crowd out the rest of it.
**[59:31]** That's kind of at least the way I look at it.
**[59:33]** So there's sort of two questions here, right?
**[59:36]** Like, why couldn't you just do both is one.
**[59:38]** And then the other one is,
**[59:40]** given our estimates on what your capacity is in 2028
**[59:44]** is three and a half gigawatts lower.
**[59:46]** Sure, you could have dedicated that to open AI training
**[59:49]** and inference capacity,
**[59:50]** but you could have also dedicated that to,
**[59:53]** hey, this three and a half gigawatts
**[59:55]** is actually just running Azure,
**[59:56]** is running Microsoft 365, it's running GitHub Copilot.
**[01:00:00]** It doesn't actually, I could have built it
**[01:00:01]** and not given it to OpenAI.
**[01:00:02]** Or I may want to build it in a different location.
**[01:00:05]** I may want to build it in UAE.
**[01:00:06]** I may want to build it in India.
**[01:00:07]** I may want to build it in Europe, right?
**[01:00:08]** So one of the other things is, as I said,
**[01:00:10]** like where we have real capacity constraints right now
**[01:00:13]** are given the regulatory needs
**[01:00:15]** and the data sovereignty needs,
**[01:00:16]** we've got to build all over the world.
**[01:00:18]** First of all, stateside capacity is super important
**[01:00:20]** and we're going to build everything.
**[01:00:21]** But one of the things is when I look out to 2030,
**[01:00:25]** I have a sort of a global view
**[01:00:26]** of what does Microsoft shape a business
**[01:00:28]** by first party and third party,
**[01:00:30]** third party segmented by the Frontier Labs
**[01:00:33]** and how much they want
**[01:00:35]** versus the inference capacity we want to build
**[01:00:38]** for multiple models
**[01:00:40]** and our own research compute needs, right?
**[01:00:42]** So that's all what's going into my calculus
**[01:00:46]** versus saying, hey,
**[01:00:47]** I think you're rightfully pointing out the pause,
**[01:00:50]** but the pause was not done because we said,
**[01:00:53]** oh my God, we don't want to build that.
**[01:00:55]** We realized that, oh, we want to build
**[01:00:58]** what we want to build slightly differently
**[01:01:02]** by both workload type,
**[01:01:04]** as well as geo type and timing as well.
**[01:01:06]** Like we'll keep ramping up our gigawatts.
**[01:01:09]** And the question is at what pace and in what location
**[01:01:13]** and in what sort of,
**[01:01:14]** how do I write even the Moore's law on it, right?
**[01:01:17]** Which is, do I really want to overbuild three and a half
**[01:01:19]** in 27 or do I want to spread that in 27, 28,
**[01:01:24]** One of the biggest learnings we had even with Nvidia
**[01:01:26]** is their pace increased in terms of their model,
**[01:01:30]** I mean, their migrations.
**[01:01:31]** So that was a big factor.
**[01:01:33]** I didn't want to go get stuck for four years,
**[01:01:35]** five years of depreciation on one generation.
**[01:01:38]** And I wanted to just basically buy,
**[01:01:40]** like in fact, Jensen's advice to me was two things.
**[01:01:43]** One is, hey, get on the speed of light execution.
**[01:01:45]** That's why I think even the execution
**[01:01:47]** in this Atlanta data center,
**[01:01:48]** I mean, like 90 days, right?
**[01:01:50]** Between when we get it into a handoff to a real workload,
**[01:01:53]** that's sort of real speed of light execution on their front.
**[01:01:56]** And so I wanted to get good on that.
**[01:01:58]** And then that way,
**[01:01:59]** then I'm building this each generation and scaling.
**[01:02:03]** And then every five years,
**[01:02:05]** then you have a much more balanced.
**[01:02:07]** So it becomes really literally like a flow
**[01:02:11]** for a large scale industrial operation like this,
**[01:02:13]** where you suddenly are not lopsided,
**[01:02:15]** where you built up a lot in one time
**[01:02:17]** and then you take a massive hiatus
**[01:02:19]** because you're stuck with all this
**[01:02:21]** to your point in one location,
**[01:02:22]** which may be great for training,
**[01:02:23]** may not be great for inference,
**[01:02:24]** because I can't serve even if it's like,
**[01:02:26]** it's all asynchronous,
**[01:02:28]** but Europe ain't gonna let me run trip to Texas.
**[01:02:31]** So that's all of the things.
**[01:02:32]** How do I rationalize this statement
**[01:02:34]** with what you've done over the last few weeks?
**[01:02:35]** You've announced deals with Iris Energy,
**[01:02:39]** with Nebius and Lambda Labs,
**[01:02:42]** and there's a few more coming as well.
**[01:02:44]** You're going out there and securing capacity
**[01:02:46]** that you're renting from the Neo clouds,
**[01:02:50]** rather than having built it yourself.
**[01:02:51]** What was the-
**[01:02:52]** I think it's fine for us because we now have it,
**[01:02:55]** when you have line of sight to demand,
**[01:02:57]** which can be served where people are building it,
**[01:02:59]** it's great.
**[01:03:00]** In fact, we'll even have,
**[01:03:01]** I would say, we will take leases,
**[01:03:04]** we will take built to suite,
**[01:03:06]** we'll take even GPUs as a service
**[01:03:08]** where we don't have capacity,
**[01:03:10]** but we need capacity and someone else has that.
**[01:03:12]** And by the way,
**[01:03:13]** I would even sort of welcome every Neo cloud
**[01:03:16]** to just be part of our marketplace.
**[01:03:18]** Guess what?
**[01:03:19]** If they go bring their capacity into our marketplace,
**[01:03:22]** that customer who comes through Azure
**[01:03:24]** will use the Neo cloud,
**[01:03:25]** which is a great win for them,
**[01:03:26]** and we'll use compute storage databases,
**[01:03:29]** all the rest from Azure.
**[01:03:31]** So I'm not at all thinking of this as just a,
**[01:03:34]** hey, I should just go gobble up all of that myself.
**[01:03:38]** So you mentioned how you're depreciating this asset
**[01:03:43]** that's five, six years,
**[01:03:44]** and this is the majority of the,
**[01:03:46]** 75% of the TCO of a data center.
**[01:03:49]** And Jensen is taking a 75% margin on that.
**[01:03:52]** So what all the hyperscalers are trying to do
**[01:03:55]** is develop their own accelerator
**[01:03:57]** so that they can reduce this overwhelming cost
**[01:04:00]** for equipment to increase the margins.
**[01:04:03]** Yeah, and then when you look at where they are,
**[01:04:06]** Google's way ahead of everyone else, right?
**[01:04:08]** They've been doing it for the longest.
**[01:04:09]** They're gonna make something like
**[01:04:10]** five to 7 million chips of their own TPUs.
**[01:04:13]** You look at Amazon,
**[01:04:14]** they're trying to make three to 5 million.
**[01:04:16]** But when we look at what,
**[01:04:17]** Microsoft is ordering of their own chips,
**[01:04:19]** it's way below that number.
**[01:04:22]** You've had a program for just as long.
**[01:04:24]** What's going on with your internal chips?
**[01:04:26]** Yeah, it's a good question.
**[01:04:27]** So the couple of things,
**[01:04:28]** one is the thing that is the biggest competitor
**[01:04:32]** for any new accelerator
**[01:04:33]** is kind of even the previous generation of NVIDIA, right?
**[01:04:36]** I mean, in a fleet,
**[01:04:37]** what I'm gonna look at is the overall TCO.
**[01:04:39]** So the bar I have even for our own,
**[01:04:41]** and which by the way,
**[01:04:42]** I was just looking at the data for Maya 200,
**[01:04:45]** which looks great.
**[01:04:47]** Except that one of the things that we learned
**[01:04:50]** even on the compute side, right?
**[01:04:51]** Which is we had a lot of Intel,
**[01:04:53]** then we introduced AMD,
**[01:04:54]** and then we introduced Cobalt.
**[01:04:55]** And so that's kind of how we scaled it.
**[01:04:58]** And so we have good sort of existence proof
**[01:05:01]** of at least in core compute
**[01:05:02]** on how to build your own silicon
**[01:05:04]** and then manage a fleet
**[01:05:05]** where all three are at play in some balance.
**[01:05:08]** Because by the way,
**[01:05:09]** even Google's buying NVIDIA and so is Amazon.
**[01:05:11]** It makes sense because NVIDIA is innovating
**[01:05:14]** and it's the general purpose thing,
**[01:05:16]** all models run on it.
**[01:05:18]** And customer demand is there
**[01:05:19]** because if you build your own vertical thing,
**[01:05:22]** you better have your own model,
**[01:05:24]** which is either gonna use it for training or inference
**[01:05:27]** and you have to generate your own demand for it
**[01:05:29]** or subsidize the demand for it.
**[01:05:30]** So therefore you wanna make sure
**[01:05:33]** you scale it appropriately.
**[01:05:35]** So the way we are gonna go do it is
**[01:05:38]** have a closed loop
**[01:05:39]** between our own MAI models and our silicon,
**[01:05:43]** because I feel like that's what gives you the birthright
**[01:05:47]** to really do your own silicon, right?
**[01:05:49]** Where you literally have designed the micro architecture
**[01:05:54]** with what you're doing
**[01:05:55]** and then you keep pace with your own models.
**[01:05:57]** And in our case,
**[01:05:59]** the good news here is OpenAI has a program
**[01:06:03]** which we have access to.
**[01:06:04]** And so therefore,
**[01:06:05]** to think that Microsoft is not gonna have something
**[01:06:08]** that scale-
**[01:06:09]** What level of access do you have to that?
**[01:06:10]** All of it.
**[01:06:11]** You just get the IP for all of that.
**[01:06:12]** So the only IP you don't have is a consumer hardware.
**[01:06:14]** That's it.
**[01:06:15]** Oh, wow, okay.
**[01:06:17]** Yeah.
**[01:06:18]** Interesting.
**[01:06:19]** Yeah.
**[01:06:20]** And by the way,
**[01:06:21]** we gave them a bunch of IP as well to bootstrap them, right?
**[01:06:25]** So this is one of the reasons why they had a mass,
**[01:06:27]** because we built all these supercomputers together
**[01:06:30]** or we built it for them and they benefited from it,
**[01:06:33]** rightfully so.
**[01:06:34]** And now as they innovate even at the system level,
**[01:06:38]** we get access to all of it.
**[01:06:40]** And we first want to instantiate what they build for them,
**[01:06:46]** but then we'll extend it.
**[01:06:47]** And so to think that we don't have,
**[01:06:49]** and so if anything,
**[01:06:50]** the way I think about your question is
**[01:06:53]** Microsoft wants to be a fantastic,
**[01:06:56]** I'll call it speed of light execution partner for Nvidia,
**[01:07:00]** because quite frankly,
**[01:07:02]** that fleet is life itself.
**[01:07:04]** I'm not worried about,
**[01:07:05]** I mean, obviously Jensen's doing super well
**[01:07:07]** with his margins,
**[01:07:08]** but the TCO has many dimensions to it.
**[01:07:11]** And I want to be great at that TCO.
**[01:07:13]** On top of that,
**[01:07:14]** I want to be able to sort of really work
**[01:07:17]** with the OpenAI lineage and the MAI lineage
**[01:07:20]** and the system design,
**[01:07:23]** knowing that we have the IP rights on both ends.
**[01:07:26]** Speaking of rights,
**[01:07:27]** one thing, you had an interview a couple of days ago
**[01:07:31]** where you said that we have rights to,
**[01:07:34]** the new agreement you've made with OpenAI,
**[01:07:36]** you have rights,
**[01:07:37]** the exclusivity to the stateless API calls
**[01:07:41]** that OpenAI makes.
**[01:07:42]** And we were sort of confused about
**[01:07:45]** if there's any state whatsoever,
**[01:07:46]** I mean, you were just mentioning a second ago
**[01:07:48]** that all these complicated workloads that are coming up
**[01:07:49]** are going to require memory and databases
**[01:07:52]** and storage and so forth.
**[01:07:53]** And is that now not stateless
**[01:07:56]** of chat GPT storing stuff on session?
**[01:07:57]** But that's the reason why.
**[01:07:58]** So the thing, the business,
**[01:08:00]** the strategic decision we made,
**[01:08:02]** and also accommodating for the flexibility OpenAI needed
**[01:08:06]** in order to be able to procure compute for,
**[01:08:08]** essentially think of OpenAI having
**[01:08:11]** a PaaS business and a SaaS business.
**[01:08:14]** SaaS business is chat GPT,
**[01:08:16]** their PaaS business is their API.
**[01:08:18]** That API is Azure exclusive.
**[01:08:22]** The SaaS business, they can run it anywhere.
**[01:08:25]** And they can partner with anyone they want to
**[01:08:27]** to build SaaS products?
**[01:08:28]** So if they want a partner
**[01:08:30]** and this partner wants to use a stateless API,
**[01:08:33]** then Azure is the place
**[01:08:35]** where they can get the stateless API.
**[01:08:36]** It seems like there's a way for them to make,
**[01:08:39]** you know, build the product together
**[01:08:41]** and it's a stateful thing.
**[01:08:41]** No, for even that,
**[01:08:42]** they'll have to come to Azure.
**[01:08:43]** Okay.
**[01:08:44]** So if it is any partner,
**[01:08:45]** and so fundamentally, you know,
**[01:08:47]** so again, this is done in the spirit of
**[01:08:50]** what is it that we valued as part of our partnership?
**[01:08:54]** And we made sure while at the same time,
**[01:08:56]** we were good partners to OpenAI
**[01:08:57]** given all the flexibility they need.
**[01:08:59]** So for example, Salesforce wants to integrate OpenAI,
**[01:09:01]** it's not through an API,
**[01:09:02]** they actually work together,
**[01:09:03]** train a model together,
**[01:09:04]** deploy it on, let's say, Amazon now.
**[01:09:07]** Is that allowed?
**[01:09:08]** Or do they have to use it?
**[01:09:10]** No, for any custom agreement like that,
**[01:09:12]** they will have to come run it.
**[01:09:14]** There are some few exceptions to US government
**[01:09:16]** and so on that we made,
**[01:09:17]** but other than that,
**[01:09:18]** they'll have to come to Azure.
**[01:09:19]** So as Satya explained,
**[01:09:21]** as AI agents get more capable,
**[01:09:23]** you're going to need more and more observability
**[01:09:24]** into what they're doing.
**[01:09:26]** You're going to need to catch them
**[01:09:27]** when they're making mistakes,
**[01:09:28]** you're going to need high level summaries
**[01:09:29]** of what they're doing,
**[01:09:30]** and you're going to need a picture
**[01:09:32]** of how everything that they're doing fits together.
**[01:09:34]** This is exactly what CodeRabbit provides.
**[01:09:36]** You just make a normal pull request
**[01:09:38]** and CodeRabbit automatically reviews the PR.
**[01:09:41]** It generates a summary of changes
**[01:09:43]** so you can understand exactly
**[01:09:44]** what the PR's author was intending,
**[01:09:46]** and it uses the context from your full code base
**[01:09:48]** to provide line by line feedback
**[01:09:50]** on how things could be improved.
**[01:09:52]** This is helpful whether you're reviewing a PR
**[01:09:54]** from a coworker or an agent.
**[01:09:56]** In either case, CodeRabbit will write up its thoughts
**[01:09:59]** and flag any issues so that your teammate
**[01:10:02]** or your agent can go fix them.
**[01:10:04]** I've noticed that when I'm coding with agents,
**[01:10:06]** CodeRabbit catches a lot of mistakes
**[01:10:09]** that the models make by default.
**[01:10:11]** For example, the models have a bad habit
**[01:10:13]** of using old versions of libraries.
**[01:10:16]** So in one session, I watched CodeRabbit
**[01:10:19]** cache a call to an old model,
**[01:10:21]** figure out what the new version was,
**[01:10:23]** and then suggest that improvement.
**[01:10:25]** Go to coderabbit.ai slash thwarkache to learn more.
**[01:10:30]** Stepping back, a question I have is,
**[01:10:32]** walking back and forth through the factory,
**[01:10:34]** one of the things you were talking about is,
**[01:10:37]** Microsoft, you can think of it as a software business,
**[01:10:39]** but now it's really becoming an industrial business.
**[01:10:42]** There's all this CapEx, there's all this construction,
**[01:10:44]** and if you just look over the last two years,
**[01:10:48]** your sort of CapEx has like tripled,
**[01:10:50]** and maybe you extrapolate that forward,
**[01:10:52]** it just actually just becomes this huge industrial explosion.
**[01:10:56]** Other hyperscalers are taking loans, right?
**[01:10:58]** Meta's done a $20 billion loan at Louisiana,
**[01:11:01]** they've done a corporate loan,
**[01:11:02]** it seems clear everyone's free cash flow is going to zero,
**[01:11:05]** which I'm sure Amy is like gonna beat you up
**[01:11:09]** if you even try to do that, but like, what's happening?
**[01:11:12]** I mean, I think the structural change
**[01:11:17]** is what you're referencing, which I think is massive, right?
**[01:11:21]** Which is, I describe it as we are now
**[01:11:23]** a capital-intensive business
**[01:11:25]** and a knowledge-intensive business.
**[01:11:27]** And in fact, we have to use our knowledge
**[01:11:29]** to increase the ROIC on the capital spend, right?
**[01:11:32]** Because that's kind of, you know, look,
**[01:11:33]** the hardware guys have done a great job
**[01:11:35]** of marketing the Moore's law,
**[01:11:37]** which I think is unbelievable and it's great.
**[01:11:39]** But if you even look, I think some of the stats
**[01:11:41]** I even did in my earnings call,
**[01:11:43]** which is for a given GPT family, right?
**[01:11:46]** The improvement, software improvements of really throughput
**[01:11:50]** in terms of tokens per dollar per watt
**[01:11:52]** that we are able to get, you know,
**[01:11:55]** quarter over quarter, year over year is massive, right?
**[01:11:59]** So it's 5X, 10X, maybe 40X in some of these cases, right?
**[01:12:02]** Just because how you can optimize.
**[01:12:05]** That's sort of knowledge intensity
**[01:12:08]** coming to bring out capital efficiency.
**[01:12:11]** So that, at some level, that's what we have to master.
**[01:12:15]** What does it mean?
**[01:12:16]** Like some people ask me, what is the difference
**[01:12:18]** between, you know, a classic old-time host
**[01:12:22]** and a hyperscaler?
**[01:12:23]** It was software.
**[01:12:24]** So yes, it is capital-intensive,
**[01:12:27]** as long as you have systems know-how,
**[01:12:29]** software capability to optimize by workload, by fleet.
**[01:12:34]** That's why I think when we say fungibility,
**[01:12:37]** there's so much software in it.
**[01:12:38]** It's just not about the fleet, right?
**[01:12:40]** It's kind of the ability to evict a workload, you know,
**[01:12:43]** and then schedule another workload.
**[01:12:45]** Can I like manage that algorithm of scheduling around?
**[01:12:51]** That is the type of stuff that we have to be world-class at.
**[01:12:53]** And so, yes.
**[01:12:54]** I think we'll still remain a software company.
**[01:12:57]** But yes, this is a different business.
**[01:12:59]** And we're going to manage.
**[01:13:00]** Look, at the end of the day,
**[01:13:02]** the cashflow that Microsoft has allows us
**[01:13:06]** to have both these arms firing, you know, well.
**[01:13:12]** It seems like in the short term,
**[01:13:13]** you have more sort of credence on things taking a while,
**[01:13:17]** being more jagged.
**[01:13:18]** But maybe in the long term,
**[01:13:19]** you think like the people who say,
**[01:13:21]** talk about AGI and ASI are correct.
**[01:13:23]** Sam will be right, but eventually.
**[01:13:26]** And I have a broader question about what makes sense
**[01:13:28]** for a hyperscaler to do,
**[01:13:30]** given that you have to invest massively
**[01:13:33]** in this thing which depreciates over five years.
**[01:13:35]** So if you have 20, 40 timelines to the kind of thing
**[01:13:39]** that somebody like Sam anticipates in three years,
**[01:13:43]** you know, what is a reasonable thing
**[01:13:44]** for you to do in that world?
**[01:13:46]** There needs to be an allocation
**[01:13:49]** to I'll call it research compute.
**[01:13:52]** That needs to be done like you did R&D, right?
**[01:13:56]** So that's the best way to even account for it,
**[01:13:59]** quite frankly.
**[01:13:59]** We should think of it as just R&D expense
**[01:14:01]** and you should say, hey, what's the research compute
**[01:14:03]** and how do you want to scale it?
**[01:14:06]** And let's even say it's an order of magnitude scale
**[01:14:11]** in some period, pick your thing.
**[01:14:13]** Is it two years?
**[01:14:14]** Is it 16 months?
**[01:14:15]** What have you, right?
**[01:14:16]** So that's sort of one piece,
**[01:14:18]** which is kind of that's kind of table stakes.
**[01:14:20]** That's R&D expenses.
**[01:14:23]** And the rest is all demand driven, right?
**[01:14:24]** I mean, ultimately, you can build ahead of demand,
**[01:14:27]** but you better have a demand plan
**[01:14:31]** that doesn't go completely off kilter.
**[01:14:33]** Do you buy, so these labs are now projecting revenues
**[01:14:36]** of 100 billion in 27, 28,
**[01:14:39]** and they're projecting, you know,
**[01:14:40]** revenue keeps growing at this rate of like 3x, 2x a year.
**[01:14:44]** In the marketplace, right,
**[01:14:45]** there's all kinds of incentives right now
**[01:14:48]** and rightfully so, right?
**[01:14:49]** I mean, what do you expect an independent lab
**[01:14:52]** that is sort of trying to raise money to do, right?
**[01:14:54]** They have to put some numbers out there
**[01:14:57]** such that they can actually go raise money
**[01:14:59]** so that they can pay their bills for compute
**[01:15:01]** and what have you.
**[01:15:02]** And it's good thing.
**[01:15:03]** I mean, someone's gonna take some risk and put it in there
**[01:15:06]** and they've shown traction.
**[01:15:08]** It's not like it's all risk without seeing the fact
**[01:15:12]** that they've been performing,
**[01:15:13]** whether it's open AI, whether it's anthropic.
**[01:15:14]** So I feel great about what they've done.
**[01:15:17]** We have massive book of business with these jobs.
**[01:15:19]** So therefore, that's all good.
**[01:15:21]** But overall, ultimately there's two simple things.
**[01:15:26]** One is you gotta allocate for R&D.
**[01:15:28]** You brought up even talent.
**[01:15:29]** You gotta like, the talent for AI is at a premium.
**[01:15:32]** You gotta spend there.
**[01:15:34]** You gotta spend on compute.
**[01:15:35]** So in some sense, researcher to GPU ratios have to be high.
**[01:15:40]** That is sort of what it takes
**[01:15:42]** to be a leading R&D company in this world.
**[01:15:46]** And that's something that needs to scale.
**[01:15:48]** And you have to have a balance sheet
**[01:15:50]** that allows you to scale that
**[01:15:51]** long before it's conventional wisdom and so on.
**[01:15:54]** So that's kind of one thing.
**[01:15:56]** But the other is all about sort of knowing how to forecast.
**[01:16:01]** As we look across the world,
**[01:16:02]** America has dominated many tech stacks, right?
**[01:16:06]** The US owns Windows right through Microsoft,
**[01:16:09]** which is deployed even in China, right?
**[01:16:11]** That's the main operating system.
**[01:16:12]** Of course, there's Linux, which is open source,
**[01:16:14]** but Windows is deployed everywhere in China
**[01:16:16]** on personal computers.
**[01:16:18]** You look at Word, it's deployed everywhere.
**[01:16:20]** You look at all these various technologies,
**[01:16:22]** it's deployed everywhere.
**[01:16:23]** The thing that is quite unique,
**[01:16:25]** and Microsoft and other companies have grown elsewhere,
**[01:16:28]** right, they're building data centers in Europe
**[01:16:30]** and in India and in all these other,
**[01:16:32]** in Southeast Asia and LATAM in Africa, right?
**[01:16:35]** All of these different places you're building capacity.
**[01:16:38]** But this seems quite different, right?
**[01:16:40]** Today, the political aspect of technology, of compute,
**[01:16:46]** you know, the US administration
**[01:16:48]** didn't care about the dot-com bubble, right?
**[01:16:51]** It seems like the US administration,
**[01:16:52]** as well as every other administration around the world,
**[01:16:54]** cares a lot about AI.
**[01:16:56]** And the question is, you know,
**[01:16:57]** we're in a sort of a bipolar world,
**[01:16:59]** at least with US and China,
**[01:17:01]** but Europe and India and all these other countries
**[01:17:04]** are saying, no, actually,
**[01:17:05]** we're gonna have sovereign AI as well.
**[01:17:07]** How does Microsoft navigate, you know,
**[01:17:09]** the difference of the 90s where it's like,
**[01:17:11]** there's one country in the world that matters, right?
**[01:17:13]** It's America, and we do, our companies sell everywhere,
**[01:17:15]** and therefore Microsoft benefits massively
**[01:17:17]** to a world where it is bipolar,
**[01:17:19]** where, hey, Microsoft can't just necessarily
**[01:17:21]** have the right to win all of Europe or India or,
**[01:17:24]** you know, Singapore.
**[01:17:25]** There's actually sovereign AI efforts.
**[01:17:27]** What is your thought process here,
**[01:17:29]** and how do you think about this?
**[01:17:30]** It's, I think, a super, you know, critical piece,
**[01:17:35]** which is, I think that the key, key priority
**[01:17:39]** for the US tech sector and the US government
**[01:17:42]** is to ensure that we not only do leading innovative work,
**[01:17:48]** but we also collectively build trust around the world
**[01:17:52]** on our tech stack, right?
**[01:17:55]** Because I always say the United States
**[01:17:57]** is just an unbelievable place.
**[01:17:59]** It's just unique in history, right?
**[01:18:01]** It's 4% of the world's population,
**[01:18:04]** 25% of the GDP and 50% of the market cap.
**[01:18:07]** And I think you should think about those ratios
**[01:18:10]** and really, and reflect on it.
**[01:18:11]** That 50% happens because, quite frankly,
**[01:18:14]** the trust the world has in the United States,
**[01:18:18]** whether it's its capital markets
**[01:18:19]** or whether it's its technology
**[01:18:21]** and its stewardship of what matters at any given time
**[01:18:26]** in terms of leading sector.
**[01:18:29]** So if that is broken,
**[01:18:32]** then that's not a good day for the United States.
**[01:18:34]** And so if we start with that,
**[01:18:35]** which I think, you know, President Trump gets,
**[01:18:38]** the White House, David Sachs,
**[01:18:40]** everyone really, I think, gets it.
**[01:18:44]** And so therefore I applaud anything
**[01:18:47]** that the United States government
**[01:18:49]** and the tech sector jointly does
**[01:18:52]** to quite frankly, for example,
**[01:18:54]** put our own capital at risk collectively as an industry
**[01:18:58]** in every part of the world, right?
**[01:18:59]** So I would like, in fact, the USG to take credit
**[01:19:02]** for foreign direct investment by American companies
**[01:19:06]** all over the world, right?
**[01:19:07]** It's kind of like Lise talked about it,
**[01:19:10]** but the best marketing that the United States
**[01:19:12]** should be doing is,
**[01:19:13]** it's not just about all the foreign direct investment
**[01:19:16]** coming into the United States,
**[01:19:17]** but the most leading sector, which is these AI factories,
**[01:19:21]** are all being created all over the world by whom?
**[01:19:24]** By America and American companies.
**[01:19:26]** And so you start there
**[01:19:28]** and then you even build other agreements around it,
**[01:19:31]** which are around their continuity,
**[01:19:34]** their legitimate sovereignty concerns
**[01:19:37]** around whether it's data residency,
**[01:19:38]** whether it's even what happens
**[01:19:42]** for them to have real agency
**[01:19:45]** and guarantees on privacy and so on.
**[01:19:49]** And so in fact, our European commitments,
**[01:19:51]** I think are worth reading, right?
**[01:19:52]** So we made a series of commitments to Europe
**[01:19:55]** on how we will really govern
**[01:19:58]** our hyperscale investment there,
**[01:20:01]** such that really European Union
**[01:20:04]** and the European countries have sovereignty.
**[01:20:07]** And we're also building sovereign clouds
**[01:20:09]** in France and in Germany.
**[01:20:11]** We have something called Sovereign Services on Azure,
**[01:20:14]** which literally give people key management services
**[01:20:18]** along with confidential computing,
**[01:20:20]** including confidential computing in GPUs,
**[01:20:23]** which we have done great innovative work with NVIDIA.
**[01:20:26]** And so I think I feel very, very good
**[01:20:28]** about being able to build both technically
**[01:20:33]** this trust in the American tech stack.
**[01:20:36]** And how do you see this shaking out as,
**[01:20:38]** you know, you do have this network effect
**[01:20:40]** with continual learning and things on the model level.
**[01:20:43]** Maybe you have equivalent things
**[01:20:44]** at the hyperscaler level as well.
**[01:20:46]** And do you expect that the countries will say,
**[01:20:49]** look, it's clearly one model
**[01:20:50]** or a couple of models are the best.
**[01:20:52]** And so we're gonna use them,
**[01:20:53]** but we're gonna have some laws around
**[01:20:54]** while the weights have to be hosted in our country.
**[01:20:56]** Or do you expect that there will be this push to have,
**[01:21:01]** it has to be a model trained in our country.
**[01:21:03]** Maybe an analogy here is like,
**[01:21:04]** people would, you know,
**[01:21:05]** the semiconductors is very important to the economy
**[01:21:07]** and people would like to have
**[01:21:07]** their sort of sovereign semiconductors,
**[01:21:09]** but like TSMC is just better.
**[01:21:11]** And so semiconductors are so important to the economy
**[01:21:13]** that you will just go to Taiwan
**[01:21:15]** and buy the semiconductors, you have to.
**[01:21:17]** Will it be like that with AI or is there?
**[01:21:20]** Ultimately, I think what matters is the use of AI
**[01:21:24]** in their economy to create economic value, right?
**[01:21:27]** I mean, that's the diffusion theory,
**[01:21:30]** which is ultimately, it's not the leading sector,
**[01:21:33]** but it's the ability to use the leading technology
**[01:21:36]** to create your own comparative advantage, right?
**[01:21:38]** So that I think will fundamentally be the core driver.
**[01:21:42]** But that said, they will want continuity of that, right?
**[01:21:45]** So in some sense, that's one of the reasons why
**[01:21:47]** I believe there's always gonna be a check
**[01:21:49]** a little bit to sort of some of your points on,
**[01:21:53]** hey, can this one model have all the runaway deployment?
**[01:21:56]** That's why open source is always gonna be there.
**[01:21:59]** There will be, by definition, multiple models.
**[01:22:03]** That'll be one way.
**[01:22:04]** Like it's kind of, that's one way for people
**[01:22:06]** to sort of demand continuity and not have concentration risk
**[01:22:09]** is another way to say it is, right?
**[01:22:12]** And so you say, hey, I'll want multiple models
**[01:22:14]** and then I want an open source.
**[01:22:15]** So I feel as long as that's there,
**[01:22:18]** every country will feel like, okay,
**[01:22:20]** I don't have to worry about deploying the best model
**[01:22:23]** and broadly diffusing because I can always take
**[01:22:27]** what is my data and my liquidity
**[01:22:29]** and move it to another model,
**[01:22:31]** whether it's open source or from another country
**[01:22:34]** or what have you.
**[01:22:35]** Concentration risk and sovereignty, right?
**[01:22:39]** Which is really agency.
**[01:22:41]** Those are the two things I think
**[01:22:42]** that'll drive the market structure.
**[01:22:44]** The thing about this is that this doesn't exist
**[01:22:46]** for semiconductors, right?
**[01:22:47]** You know, all refrigerators, cars have chips made in Taiwan.
**[01:22:50]** It didn't exist until now.
**[01:22:52]** Until now, everybody is now, like.
**[01:22:54]** Even then, right?
**[01:22:56]** If Taiwan is cut off, there are no more cars
**[01:22:58]** or no more refrigerators.
**[01:22:59]** TSMC Arizona is not replacing any real fraction
**[01:23:03]** of the production.
**[01:23:05]** The sovereignty is a bit of like a scam, if you will, right?
**[01:23:08]** I mean, it's worthwhile having it.
**[01:23:09]** It's important to have it,
**[01:23:10]** but it's not real sovereignty, right?
**[01:23:13]** And we're a global economy.
**[01:23:15]** I think it's kind of like Dylan saying,
**[01:23:17]** hey, at this point, we've not learned anything
**[01:23:19]** about sort of what resilience means
**[01:23:23]** and what one needs to do, right?
**[01:23:25]** So it's kind of, any nation state,
**[01:23:29]** including the United States, at this point,
**[01:23:32]** will do what it takes to be more self-sufficient
**[01:23:36]** on some of these critical supply chains.
**[01:23:39]** So I, as a multinational company,
**[01:23:43]** have to think about that as a first-class requirement, right?
**[01:23:46]** If I don't, then I'm not respecting
**[01:23:49]** what is in the sort of policy interests
**[01:23:53]** of that country long-term, right?
**[01:23:55]** And I'm not saying they won't make practical decisions
**[01:23:58]** in the short-term, right?
**[01:23:59]** Absolutely, I mean,
**[01:24:00]** the globalization can't just be rewound, right?
**[01:24:02]** I mean, all these capital investments cannot be made
**[01:24:05]** in a way at the pace at which,
**[01:24:08]** but at the same time, you have to kind of,
**[01:24:09]** like if I, think about it, right?
**[01:24:11]** If somebody showed up in Washington and said,
**[01:24:12]** hey, you know what?
**[01:24:13]** We're not gonna build any semiconductor plants.
**[01:24:16]** They're gonna be kicked out of the United States.
**[01:24:20]** And the same thing is gonna be true
**[01:24:21]** in every other country too.
**[01:24:23]** And so therefore, I think we have to,
**[01:24:25]** as companies, respect what the lessons learned are,
**[01:24:31]** whether it's, you could say the pandemic woke us up
**[01:24:33]** or whatever, but nevertheless, people are saying,
**[01:24:36]** look, globalization was fantastic.
**[01:24:38]** It helped the supply chains be globalized
**[01:24:41]** and be super efficient,
**[01:24:42]** but there's such a thing called resilience
**[01:24:44]** and we are happy, we want resilience.
**[01:24:47]** And so therefore, that feature will get built
**[01:24:50]** at what pace, I think is the point you're making.
**[01:24:52]** It can't be like, you can't snap your fingers
**[01:24:54]** and say all the TSMC plants now are all in Arizona
**[01:24:57]** and with all of the capability, they're not going to be,
**[01:25:00]** but is there a plan?
**[01:25:01]** There will be a plan.
**[01:25:02]** And should we respect that?
**[01:25:03]** Absolutely.
**[01:25:04]** And so I feel that's the world.
**[01:25:07]** I wanna meet the world where it is
**[01:25:10]** and what it wants to do going forward,
**[01:25:13]** as opposed to say, hey, we have a point of view
**[01:25:16]** that doesn't respect your view.
**[01:25:17]** So just to make sure I understand,
**[01:25:19]** the idea here is each country will want
**[01:25:23]** some kind of data residency, privacy, et cetera.
**[01:25:26]** And Microsoft is especially privileged here
**[01:25:27]** because you have relationships with these countries,
**[01:25:30]** you have expertise in setting up
**[01:25:32]** these kinds of sovereign data centers
**[01:25:34]** and therefore Microsoft is uniquely fit for a world
**[01:25:38]** with more sovereignty requirements.
**[01:25:41]** Yeah, I mean, I don't wanna sort of describe it
**[01:25:44]** as somehow we are uniquely privileged.
**[01:25:46]** I would just say, I think of that as a business requirement
**[01:25:50]** that we have been doing all the hard work all these decades
**[01:25:52]** and we would plan to.
**[01:25:54]** And so my answer to Dylan's previous question was,
**[01:25:57]** I take these, whether it's in the United States,
**[01:26:00]** quite frankly, when the White House and the USG says,
**[01:26:05]** hey, we want you to allocate more of your, I don't know,
**[01:26:10]** wafer starch to fabs in the US, we take that seriously.
**[01:26:16]** Or whether it is data center and the EU boundary,
**[01:26:19]** we take that seriously.
**[01:26:20]** So to me, respecting what I think are legitimate reasons
**[01:26:25]** why countries care about sovereignty
**[01:26:28]** and building for it as a software and a physical plant
**[01:26:31]** is what I would say we are gonna do.
**[01:26:34]** And as we go to like the bipolar world, right?
**[01:26:36]** US, China, there is a lot around,
**[01:26:41]** American tech does not, it's not just you versus Amazon
**[01:26:45]** or you versus Anthropic or you versus Google.
**[01:26:48]** There is a whole host of competition.
**[01:26:51]** How does America rebuild the trust?
**[01:26:54]** What do you do to rebuild the trust to say,
**[01:26:56]** actually no American companies
**[01:26:57]** will be the main provider for you?
**[01:26:59]** And how do you think about competition
**[01:27:01]** with up and coming Chinese companies,
**[01:27:03]** whether it be ByteDance and Alibaba
**[01:27:06]** or DeepSeek and Moonshot?
**[01:27:07]** And just to add to the question,
**[01:27:08]** one concern is we're talking about how AI
**[01:27:10]** is becoming this sort of industrial CapEx race
**[01:27:13]** where you're just rapidly having to build quickly
**[01:27:15]** across all those supply chain.
**[01:27:17]** When you hear that, at least up until now,
**[01:27:19]** you just think about China, right?
**[01:27:21]** This is like their comparative advantage.
**[01:27:23]** And especially if we're not gonna Moonshot to ASI next year,
**[01:27:27]** but it's gonna be this decades of build outs
**[01:27:31]** and infrastructure and so forth.
**[01:27:33]** How do you deal with Chinese competition?
**[01:27:36]** And are they privileged in that world?
**[01:27:36]** Yeah, so it's a great question.
**[01:27:37]** I mean, in fact, you just made the point
**[01:27:40]** of why I think trust in American tech
**[01:27:44]** is probably the most important feature.
**[01:27:47]** It's not even the model capability, maybe.
**[01:27:50]** It is like, can I trust you, the company?
**[01:27:54]** Can I trust you, your country and its institutions
**[01:27:59]** to be a long-term supplier?
**[01:28:01]** Maybe the thing that wins the world.
**[01:28:05]** I think that's a good note to end on.
**[01:28:06]** Satya, thank you for doing this.
**[01:28:07]** Thank you so much.
**[01:28:08]** Thank you.
**[01:28:09]** It's such a pleasure.
**[01:28:12]** It's awesome.
**[01:28:13]** It's like, man, you two guys are like quite the team.
**[01:28:15]** Hey, everybody.
**[01:28:17]** I hope you enjoyed that episode.
**[01:28:19]** If you did, the most helpful thing you can do
**[01:28:21]** is just share it with other people
**[01:28:23]** who you think might enjoy it.
**[01:28:24]** It's also helpful if you leave a rating
**[01:28:27]** or a comment on whatever platform you're listening on.
**[01:28:30]** If you're interested in sponsoring the podcast,
**[01:28:32]** you can reach out at dwarkesh.com slash advertise.
**[01:28:38]** Otherwise, I'll see you in the next one.
