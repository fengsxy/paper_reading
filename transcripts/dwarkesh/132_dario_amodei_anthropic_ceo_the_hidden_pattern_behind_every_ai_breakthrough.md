---
layout: default
type: transcript
series: dwarkesh
episode: 0
guest: ""
title: "Dario Amodei (Anthropic CEO) — The hidden pattern behind every AI breakthrough"
source_url: "https://www.youtube.com/watch?v=Nlkk3glap_U"
analysis_url: /transcripts/dwarkesh/132_dario_amodei_anthropic_ceo_the_hidden_pattern_behind_every_ai_breakthrough.analysis/
permalink: /transcripts/dwarkesh/132_dario_amodei_anthropic_ceo_the_hidden_pattern_behind_every_ai_breakthrough/
---

# Transcript: Dario Amodei (Anthropic CEO) — The hidden pattern behind every AI breakthrough

Source: https://www.youtube.com/watch?v=Nlkk3glap_U

---

**[00:00]** a generally well-educated human that could happen in you know two or three years what does that imply for anthropic when in two to three years these leviathans are doing like 10 billion dollar trading runs the models they just

**[00:12]** want to learn and it was a bit like a Zen Cohen I listened to this and and I became enlightened the compute doesn't flow like the spice doesn't flow it's like you can't like like the The Blob has to be unencumbered

**[00:26]** the big acceleration that happened late last year and the beginning of this year we didn't cause that and honestly I think if you look at the reaction to Google that might be 10 times more important than anything else there was a

**[00:38]** running joke the way building AGI would look like because you know there would be a data center next to a nuclear power plant next to a bunker but now it's 20 30. what happens next what what are we doing with a superhuman God

**[00:49]** okay today I have the pleasure of speaking with Dario amodei who is the CEO of anthropic and I'm really excited about this one Dario thank you so much for coming on the podcast thanks for having me first question you have been

**[01:02]** one of the very few people who has seen scaling coming for years more than five years I don't know how long it's been but as somebody who's seen it coming what is fundamentally the explanation for why scaling works why is a universe

**[01:15]** organized such that if you throw big blobs and compute at a wide enough distribution of data the thing becomes intelligent I think the truth is that we still don't know I think it's almost entirely an empirical fact

**[01:28]** um you know I think it's a fact that you could kind of sense from the data and from a bunch of different places um but I think we don't still have a satisfying explanation for it if I were to try to make one but I'm just I don't

**[01:39]** know I'm just kind of waving my hands when I say this you know there there's this there's these ideas in physics around like long tail or power law of like core relations or effects and so like when a bunch of stuff happens right

**[01:54]** when you have a bunch of like features you get a lot of the data in like kind of the early you know the the fat part of the distribution before the Tails um you know for language this would be things like oh I figured out there are

**[02:06]** parts of speech and nouns follow verbs and then there are these more and more and more and more subtle correlations um and so it it kind of makes sense why there would be this you know every log or order of magnitude that you add you

**[02:20]** kind of capture more of the distribution what I what's not clear at all is why is it scale so smoothly with parameters why does it scale so smoothly with the amount of data why are you can think up some explanations of why it's linear

**[02:36]** like the parameters are like a bucket and so the data's like water and so size of the bucket is proportional to the size of the water but like why does it lead to all these this very smooth scaling I think we still don't know

**[02:48]** there's all these X explanations are chief scientists Jared Kaplan did some stuff on like fractal manifold Dimension that like you can use to explain it so there's there's all kinds of ideas but I feel like we just don't really know for

**[03:02]** sure and by the way for the audience who's trying to follow along by scaling we're referring to the fact that you can very predictably see how if you go from gbd3 to gpd4 or in this case Claude one to claw two the loss in terms of whether

**[03:14]** it can predict the next token scales very smoothly so okay we don't know why it's happening but can you at least predict if empirically here is the loss at which disability will emerge here is the place where this circuit will emerge

**[03:28]** is is that about predictable or are you just looking at the loss number that is much less predictable what's predictable is this statistical average this loss this entropy it's super predictable it's like you know predictable to like

**[03:39]** sometimes even to several significant figures which you don't see outside of physics right you don't expect to see it in this messy empirical field um but actually specific abilities are very hard to predict so you know back

**[03:51]** when I was working on gpt2 and gpt3 like when does arithmetic come in place when do models learn to code sometimes it's very it's very abrupt um you know it's kind of like you can predict statistical averages of the weather but the weather

**[04:04]** on one particular day is very you know very very hard to predict so uh I dumb it down for me I don't understand manifolds but mechanistically it doesn't know addition yet now it knows addition what has happened uh this is another

**[04:16]** question that we don't know the answer to I mean we're trying to answer this with things like mechanistic interpretability but you know I'm not sure I mean you can think about these things about like circuits snapping into

**[04:27]** place although there is some evidence that when you look at the models being able to add things that you know like if you look at its chance of getting the right answer that shoots up all of a sudden but if you look at okay what's

**[04:40]** the probability of the right answer you'll see it climb from like one in a million to one hundred thousand to one in a thousand long before it actually gets the right answer and so there's some Conti in many of these cases at

**[04:52]** least I don't know if in all of them there's some continuous process going on behind the scenes I don't understand it at all does that imply that the circuit or the process for doing addition was pre-existing and it just got increased

**[05:04]** in Saline I don't know if like there's this circuit that's weak and getting strong longer I don't know if it's something that works but not very well like I I think we don't know and these are

**[05:14]** some of the questions we're trying to answer with mechanistic interpretability are there abilities that won't emerge with scale so I definitely think that again like things like alignment and values are not guaranteed to emerge with

**[05:25]** scale right it's it's kind of like you know one way to think about it is you you train the model and it is basically it's like predicting the world it's understanding the world it's its job is facts not values right it's

**[05:39]** trying to predict what comes next but there's there's just there's free variables here where it's like it what should you do what should you think what should you value those you know like they're they're just there are the bits

**[05:51]** for that there's just like well if I started with this I should finish with this if I started with this other thing I should finish with this other thing um and so I think that's not going to emerge um I want to talk about a lemon

**[06:02]** in a second but on scaling if it turns out that scaling plateaus before we reach human level intelligence looking back on it what would be your explanation what do you think is likely to be the case if that turns out to be

**[06:12]** the outcome yeah um so I guess I would distinguish some problem with the fundamental Theory with some practical issue so uh one practical issue we could have is we could run out of data for various reasons I think that's not going

**[06:24]** to happen but uh you know uh if you look at it very very naively we're not that far from running out of data and so it's like we just don't have the data to continue the to continue the scaling curves I think you know another way it

**[06:36]** could happen is like oh we just we just use up our all of our compute that was available and that that wasn't enough and then progress is slow after that I wouldn't bet in either of those things happening but they they could I I think

**[06:47]** from uh from a fundamental perspective I personally I think it's very unlikely that the scaling laws will just stop if they do another reason again this isn't fully fundamental could just be we don't have quite the right architecture like

**[07:02]** if we tried to do it with an lsdm or an RNN the slope would be different I still might be that we get there but I think there are some things that are just very hard to represent when you don't have this ability to attend far in the past

**[07:14]** that Transformers have if somehow and I don't know how we would know this it kind of wasn't about the architecture and we just hit a wall I think I'd be very surprised by that I think we're already at the point where the things

**[07:28]** the models can't do don't seem to me to be different and kind from the things they can do um and it just you know you could have made a case a few years ago that it was like they

**[07:39]** can't reason they can't program like you could have you could have drawn boundaries and said well maybe you'll hit a wall I didn't think that I didn't think we would hit a wall

**[07:48]** a few other people didn't think we would hit a wall but it was a more plausible case that I think it's a less plausible case now now it could happen like this stuff is crazy like it could it could it could happen tomorrow but it's just like

**[07:59]** we hit a wall I think if that happens I'm trying to think of like what's my what would really be my it's unlikely but what would really be my explanation I think my explanation would be there's something wrong with the loss when you

**[08:13]** train on next word prediction like some of the remaining like reasoning abilities or something like that like if you really want to learn you know it's a program at a really high level like it means you care about some tokens much

**[08:26]** more than others and they're rare enough that it's like the loss function over focuses on kind of the the the appearance the things that are responsible for the most bits of entropy uh and instead you know they don't focus

**[08:40]** on this stuff that's really essential and so you could kind of have the signal drowned out in the noise and I don't think it's going to play out that way for a number of reasons but if if you told me yup you trained your 2024 model

**[08:51]** it was much bigger and it just wasn't any better and you tried every architecture it didn't work that I think that's the explanation I would I would reach for is there a candidate for another loss function if

**[09:01]** you had to abandon next token prediction I think then you would have to go for some kind of RL and again there's you know there's many different kinds there's RL from you and feedback there's RL against an objective there's things

**[09:12]** like constitutional AI there's things like amplification and debate right these are kind of both alignment methods and ways of training models you would have to try a bunch of things but the focus would have to be on what do we

**[09:23]** actually care about the model doing right in a sense we're a little bit lucky that it's like predict the next word gets us all these other things we need right there's no guarantee it seems like from your world view there's a

**[09:34]** multitude of different loss functions that it's just a matter of what can allow you to just throw a whole bunch of data at it like the next token prediction itself is not significant yeah I think well I mean I guess the

**[09:44]** thing with RL is you get slowed down a bit because it's like you know you have to by some method kind of you know design how loss function Works nice thing with the next token prediction is it's there for you right it's just it's

**[09:57]** the easiest thing in the world and so I think it would slow you down if you couldn't scale in just that very simplest way you mentioned that uh the data is likely not to be the constrained why why do you think that is the case

**[10:07]** there's various possibilities here and you know for a number of reasons I shouldn't go into the details but you know like there's many sources of data in the world and there's many ways that you can also generate data my my guess

**[10:19]** is that this will not be a blocker maybe better if it was but uh it won't be are you talking about multimodal or there's just many different ways to do it um how did you form your views on scaling how far back can we go and then you would be

**[10:32]** basically saying something similar to this this view that I have probably formed gradually from I would say like 2014 to 2017. so I think my first experience with it was my first experience with AI

**[10:46]** um so I you know I saw some of the early stuff around alexnet in 2012. always kind of had wanted to study intelligence but I you know before I was just like this isn't really working like it doesn't seem like it's actually working

**[10:58]** um you know all the way back to like you know 2005 I'd like you know I'd read Rick herzwell's work you know I'd read even even some of like Elie Ezra's work on the early on the old internet back then and I was like oh this this stuff

**[11:09]** kind of looks far away like I look at the AI stuff of today and it's like not not anywhere not anywhere close but with Alex and I was like oh this is actually stuff is actually starting to work so I joined Andrew ing's group

**[11:21]** um initially at Baidu and the first task you know that I got set to do right it was my you know I'd be in a different field and so I I first joined you know this was my first experience with AI and it was a bit different from a lot of the

**[11:36]** kind of academic style research that was going on kind of Elsewhere in the world right the I I think I kind of got lucky in that the task that was given to me and the other folks there was just make the best speech recognition

**[11:49]** uh system that you can and there was a lot of data available there were a lot of gpus available so it kind of it it posed the problem in a way that was amenable to discovering that kind of scaling was a solution right that's very

**[12:02]** different from like Europe post-doc and it's your job to come up with you know what's the what's the best like you know what's what's an idea that seems clever and new and makes your mark as someone who's invented something and and so I

**[12:16]** just quickly discovered that like you know I was just just tried the simplest experiments I was like you know just fiddling with some dials I was like okay try um you know try try adding more layers to

**[12:27]** the art literally add more layers to the RNN um you know try training it for longer what happens how long does it take to overfit what if I add new data and repeat it less times and like I just saw

**[12:37]** these like very consistent patterns I didn't really know that this was unusual or that others weren't thinking in this way this this was just kind of like almost like beginner's luck it was my first

**[12:49]** experience with it and I didn't really think about it Beyond speech recognition right right right you know I was just kind of like oh this is you know I don't know anything about this field there's zillions of things people do with

**[12:59]** machine learning but like I'm like weird seeing seems to be true in the speech recognition field um and and and then I I think it was recently you know like um just before open AI started

**[13:11]** um that I met Ilia who you who you interviewed one of the first things he said to me was look the models they just want to learn you have to understand this the models they just want to learn and it was a bit like a Zen Cohen like I

**[13:21]** kind of like I listened to this and and I became enlightened [Laughter] um and uh you know over over the years over the years after this you know you know again I would be kind of you know

**[13:34]** the one who would formalize a lot of these things and kind of put them together but like just kind of the the what that told me is that that phenomenon that I'd seen wasn't just some random thing that I'd seen it was

**[13:46]** like it was broad it was it was more General right the models the models just want to learn you get the obstacles out of their way right you give them you give them good data you you give them enough space to operate in you don't do

**[13:59]** something stupid like condition them badly numeric likely um and they want to learn they'll do it they'll do it you know what I find really interesting about what you said is there are many people who were aware

**[14:11]** back at that time probably weren't working on it directly but we're aware that these things are really good at speech recognition or at playing these constrained games very few extrapolated from there like you and Ilya did to

**[14:25]** something that is generally intelligent what was different about the way you were thinking about it versus how others think that you went from like is getting better at speech in this consistent way it will get better at everything in this

**[14:35]** consistent way yeah so I I genuinely don't know I mean at first when I saw it first speech I assumed this was just true for speech or for this narrow class of models I I think it was just over the period between 2014 and 2017 I tried it

**[14:50]** for a lot of things and saw the same thing over and over again I watched the same being true with DOTA I watched the same being true with robotics which many people thought of as a counter example but I just thought what's hard to get

**[15:03]** data for robotics but if we operate within if we look within the data that we have we see the same patterns and so I don't I don't know I think people were very focused on solving the problem in front of them

**[15:15]** why one person thinks one way another person thinks it's very it's very hard to explain I think people just see it through a different lens you know are looking like vertically instead of horizontally they're not thinking about

**[15:26]** the scaling they're thinking about how do I solve my problem well for robotics there's not enough data and so you know and and so you know that can easily abstractable scaling doesn't work because we don't have the data and and

**[15:39]** so I don't I I don't know I just for some reason and it may just it may just have been random chance was obsessed with that particular direction when did it become obvious to you that language is the means to just feed a bunch of

**[15:53]** data into these things that or was it just you ran out of other things like robotics there's not enough data this other thing there's not enough data yeah I mean I think this whole idea of like the next word prediction that you could

**[16:03]** do self-supervised learning you know that together with the idea that it's like wow for predicting the next word there's so much richness and structure there right you know it might say two plus two equals and you have to know the

**[16:14]** answer is four and you know it might be telling the story about a character and then basically it's it's posing to the model you know the equivalent of these developmental tests that get posed to Children you know Mary walks into the

**[16:25]** room and you know puts an item in there and then you know Chuck walks into the room and removes the item and Mary doesn't see it what does Mary think hap you know so like so the models are going to have to to get this right in the

**[16:36]** service of predicting the next word they're going to have to solve you know solve all these theory of Mind problems solve all these math problems and so I you know I I my thinking was just well you know you scale it up as much as you

**[16:48]** can you you you know there's there's kind of No Limit to it and I think I kind of had abstractly that view but the thing of course that like really solidified and convinced me was the work that Alec Radford did on GPT one

**[17:02]** um which was not only could you get this this language model that could predict things very well but also you could fine tune it you needed to fine tune it in those days to do all these other tasks and so I was like wow you know it this

**[17:14]** isn't just some narrow thing where you get the language model right it's sort of halfway to everywhere right it's like you know you get the language model right and then with a little move in this direction it can you know it can

**[17:26]** solve this this you know logical dereference tests or whatever and you know with this this other thing you know it can it can solve translation or something and then you're like wow I think there's there's really something

**[17:36]** to do it and and of course we can we can really scale it well one thing that's confusing or that would have been hard to see if you told me in 2018 we'll have models in 2023 like two that can write theorems in the style of Shakespeare or

**[17:50]** whatever Theory you want you want they can a standardized test with open-ended questions you know um the just all kinds of really impressive things you would have said at that time I would have said oh you have AGI you clearly have

**[18:04]** something that is a human level intelligence where these while these things are impressive it clearly seems we're not at human level at least in the current generation and potentially for generations to come what explains this

**[18:15]** discrepancy between super impressive performance and these benchmarks and in just like the things you could describe versus yeah so that that was one area where actually I was not press scenes and I was surprised as well yeah

**[18:27]** um so when I first looked at gpt3 and you know more so the kind of things that we built in the early days at anthropic my my general sense was I you know I looked at these and I'm like it seems like they've really grasped the essence

**[18:41]** of language I'm not sure how much we need to scale them up like maybe we maybe what's what's more needed from here is like RL and all and kind of and kind of all the other stuff like we might be kind of near the you know I

**[18:53]** thought in 2020 like we can scale this a bunch more but I wonder if it's more efficient to scale it more or to start adding on these other objectives like like RL I thought maybe if you do as much RL as you know as you've done

**[19:06]** pre-training for uh for uh you know 2020 style model that that's that's the way to go and scaling it up will keep working but you know is that is that really the best path and I I think it I don't know it just keeps going like I

**[19:21]** thought it had understood a lot of the essence of language but then you know there's there's kind of there's kind of further to go um and and so I don't know stepping back from it like one of the reasons why I'm

**[19:34]** sort of very empiricist about about AI about safety about organizations is that you often get surprised right you know I feel like I've been right about some things but I've still you know with these

**[19:48]** theoretical pictures had been wrong about most things being right about 10 of the stuff is you know sets you head and shoulders above um above above many people you know if you look back to I can't remember who it

**[20:00]** was kind of you know made these diagrams that are like you know here's here's the village little idiot here's Einstein here's the scale of intelligence right in the village idiot and Einstein are like very close to each other like that

**[20:13]** maybe that's still true in some abstract sense or something but it's it's not really what we're seeing is it we're seeing like that it seems like the human range is pretty Broad and doesn't we don't hit the human range

**[20:27]** in the same place or at the same time for different tasks right like you know like write write us on it you know in the style of Cormac McCarthy or something like I don't know I'm not very creative so I couldn't do that but like

**[20:40]** you know that's that's a pretty high level human skill right um and even the model is starting to get good at stuff of you know like constrained writing you know there's like write a you know write a page

**[20:50]** without using the letter e or something Library the page about X without using the letter e like I think the models might be like superhuman or close to superhuman at that um but when it comes to you know

**[21:02]** I yeah I don't know prove relatively simple mathematical theorems like they're they're just starting to do the beginning of it they make really dumb mistakes sometimes and they they really lack any kind of broad like you know

**[21:17]** correcting your errors or doing some extended tasks and so I don't know it turns out that intelligence isn't isn't a spectrum there are a bunch of different areas of domain expertise there are a bunch of different like

**[21:30]** kinds of skills like Memories different I mean it's all it's all formed in the blob it's not it's all formed in the blob it's not complicated but to the extent it even is on the Spectrum the spectrum is also wide if you asked me 10

**[21:43]** years ago that's not what I would have expected at all but uh I think that's very much the way it's turned out oh man I have so many questions just as follow up on that one is do you expect that given the distribution of training that

**[21:56]** these models get from massive amounts of internet data versus what humans got from Evolution that the repertoire of skills that elicits will be just barely overlapping it will be like concentric circles how how do you think about do

**[22:11]** those matter or is it clearly there's a lot there's certainly a large amount of overlap right because a lot of the thing you know like these models have have business applications and many of their business applications are doing things

**[22:21]** that you know are help helping humans to be more effective at things um so the overlap is quite is quite large and you know if you think of all the activity that humans put on the internet in text that covers a lot of it

**[22:33]** but it probably doesn't cover some things like the models I think they do learn a physical model of the world to some extent but they certainly don't learn how to actually move around in the world

**[22:42]** um again maybe that's easy to fine tune but uh I you know I think so I think there are some things that the models don't learn that humans do and then I think you know the models learn for example to speak fluent base64. I don't

**[22:56]** know about you but I never learned that right How likely do you think it is that these models will be superhuman for many years at economically valuable tasks while they're still below humans in many other relevant tasks that prevents like

**[23:12]** an intelligence explosion or something I think this kind of stuff is like really hard to know um so I'll give I'll give that caveat that like you know again like the basic scaling laws you can kind of predict and

**[23:23]** then like this more granular stuff which we really want to know to know how this all all is going to go is is much harder to know but my guess would be the scaling laws are going to continue like you know again subject to you know do

**[23:36]** people slow down for safety or for regulatory reasons um but you know let's just let's just put all that aside and say like we have the economic capability to keep scaling if we did that what would happen and I I

**[23:49]** think my view is we're going to keep getting better across the board and I don't see any area where the models are like super super weak or not starting to make progress like that used to be true of like math and programming but I think

**[24:01]** over the last six months you know the the 2023 generation of models compared to the 2022 generation have started to learn that there may be more subtle things we don't know and so I I kind of suspect even if it isn't quite even that

**[24:16]** the rising tide will lift all the boats does that include the thing you were mentioning earlier where if there's an extended task it kind of loses its train of thought um yeah or its ability to just like

**[24:26]** execute a series so I think that that that's going to depend on things like RL training to have the model do longer Horizon tasks I don't expect that to require a substantial amount of additional compute

**[24:41]** um I think that um that that was probably an artifact of uh yeah kind of thinking about RL in the wrong way and underestimating how much the model had learned on its own in terms of you know are we going to be superhuman in some

**[24:55]** areas and not others I think it's complicated I could imagine that we won't be superhuman in some areas because for example they involve like embodiment in the physical world and then it's like what happens like do the

**[25:07]** AIS help us train faster AIS and those faster AIS wrap around and solve that do you not need the physical world it depends what you mean are we worried about an alignment disaster are we worried about misuse like making weapons

**[25:20]** of mass destruction are we worried about the AI or you know the AI taking over research from humans are we worried about it reaching some threshold of economic productivity where it can do what the average these different

**[25:34]** thresholds I think have have different answers although I suspect they will all come within a few years let me ask about those thresholds so if claw was an employee at anthropic what salary would it be worth what is it like meaningfully

**[25:46]** speeding up AI progress it feels to me like an intern in most areas um but then some specific areas where it's better than that again I think one thing that's makes the comparison hard is like the form factor is kind of like

**[26:00]** not the same as a human right like a human like you know if you were to behave like one of these chat Bots like we wouldn't really I mean I guess we could have this conversation it's like but you know they're they're not really

**[26:11]** they're more designed to answer single or a few questions right um and and like you know they don't have a the concept of having a long life of Prior experience right we're talking here about you know things that

**[26:23]** that I've experienced in the past right and chatbots don't don't have that and so there's there's all kinds of stuff missing and so it's hard to make a comparison but it I don't know it it they feel like interns in some areas and

**[26:37]** kind of then they have areas where they Spike and are really savants where they may be better than they may be better than anyone here but does the overall picture of something like an intelligence explosion you know my

**[26:48]** former guest is Carl Schulman and he has this like very detailed model of an adult does that as somebody who would actually like see that happening does that make sense to you as they go from interns to entry level software

**[26:58]** Engineers those entry level software Engineers increase your productivity I I think I think the idea that the the AI systems become more productive and first they speed up the productivity of humans then they you know kind of equal the

**[27:13]** productivity of humans and and and you know and then they're in some meaningful sense the main contributor to Scientific progress that that happens at some point I I think that that basic logic seems likely to me

**[27:28]** although I I have a suspicion that when we actually go into the details it's going to be kind of like weird and different than we expect that all the detailed models are kind of you know we're thinking about the wrong

**[27:40]** things or we're right about one thing and then are wrong about 10 other things and and so I I don't know I think we might end up in like a weirder world than we expect when you add all this together

**[27:53]** like your estimate of when we get something kind of human level yeah what does that look like I mean again it depends on the thresholds yeah um you know in in terms of someone looks at these the model and you know even if

**[28:07]** you talk to it for you know for for an hour or so it's it's basically you know it's basically like a generally well-educated human yeah um that could be not very far away at all I think

**[28:21]** um like that that could happen in you know two or three years like uh you know if I look at again like I think the main thing that would stop it would be if if we hit certain certain you know and we have internal tasks for you know safety

**[28:34]** thresholds and stuff like that so if a company or the industry decides to slow down or you know we're able to get the government Institute restrictions that kind of uh you know that that moderate the rate of progress for safety reasons

**[28:48]** that would be the main reason it wouldn't happen but if you if you just look at the logistical and economic ability to scale I don't think we're very far at all from that now that that may not be the threshold where the

**[29:00]** models are existentially dangerous uh in fact I suspect it's not not quite there yet it may not be the threshold where the models can take over most AI research it may not be the threshold where the models you know seriously

**[29:13]** change how the economy Works um I think it gets a little murky after that and all those thresholds may happen at various times after that but I think I think in terms of the base technical capability of it it kind of It kind of

**[29:28]** sounds like a reasonably generally educated human yeah across the board I think that could be quite close why would it be the case that it could be sound you know pass a Turing test for an educated person but not be able to

**[29:40]** contribute or substitute for human involvement in the economy a couple reasons one is just you know that the threshold of skill isn't high enough right comparative advantage it's like uh it like doesn't matter

**[29:53]** that you know I have someone who's better than the average human at every task like what I really need is like for for AI research like you know I need what you know I I need to basically find something that is is strong enough to

**[30:07]** substantially accelerate you know the the like labor of the Thousand experts who who are best at it um and so we might reach a point where we you know the comparative advantage of these systems is not Is Not Great uh

**[30:20]** another thing that could be the case is that I think there are these kind of mysterious frictions that like you know kind of don't show up in naive economic models but you see it whenever you're like you know when you go to a customer

**[30:32]** or something and you're like hey I have this cool chat bot in principle it can do everything that you know your customer service bot does or that this part of your company does but like the the actual friction of like how do we

**[30:45]** slot it in how do we make it work that that includes both kind of like you know just the question of how it works in a human sense within the company like you know how how things happen in the economy and overcome frictions and and

**[30:58]** also just like what is the workflow how do you actually interact with it it's very different to say here's a chat bot that kind of looks like it's doing this task that you or you know or helping the human to do to do some tasks as it is to

**[31:14]** say like okay this thing is this thing is deployed in 100 000 people are using it often like right now lots of folks are rushing to deploy these systems but I think in many cases they're not using them in anywhere close to the most

**[31:27]** efficient way that they could you know not because they're not smart but because it takes time to work these things out and so I think when things are changing this fast they're going to be all of these frictions yeah and I and

**[31:38]** I think again these are messy reality that doesn't quite get captured in the model I don't think it changes the basic picture like I don't think it changes the idea that we're we're building up this snowball of like the models help

**[31:50]** the models get better and you know do what the humans and and you know can can accelerate what the humans do and eventually it's mostly the models doing the work like you zoom out far enough that's happening but I'm I'm kind of

**[32:01]** skeptical of kind of any kind of precise mathematical or exponential prediction of how it's going to be I think it's I think it's I think it's all going to be a mess but I think what we know is it's not an ex metaphorical exponential and

**[32:15]** it's gonna happen fast how do those different exponentials net out which we've been talking about so one was the the scaling laws themselves are power laws with decaying marginal uh you know uh loss per you know parameter or

**[32:30]** something the other exponential you talked about is well these things can get involved in the process of AI research itself speeding it up so those two are sort of opposing exponentials does it net out to be super linear or

**[32:42]** sublinear and also you mentioned well the distribution of intelligence might just be broader so should we expect after the after we get to this point in two to three years it's like like what does that look like it's I

**[32:54]** mean I think it's very unclear right so we're already at the point where if you look at the loss the scaling laws are starting to bend I mean we've seen that in you know published model cards offered by multiple companies

**[33:06]** um so that's not a secret at all but as as they start to bend each little bit of of entropy right of accurate prediction becomes more important right maybe these last little bits bits of entropy are like well you know this is a physics

**[33:18]** paper as Einstein would have written it as opposed to you know as some other physicist would have would have would have written it and so it's it's hard to assess significance from this it certainly looks like in terms of

**[33:30]** practical performance the metrics keep going up relatively linearly also they were always unpredictable uh so so it's it's hard to see that and then I mean the thing that I think is driving the most acceleration is just more and

**[33:43]** more money is going into the field like people are seeing that there's just a huge amount of you know of of economic value and so I expect the price the amount of money spent on the largest models to go up by like a factor of 100

**[33:57]** or something and for that that then to be concatenated with its ships are getting faster the algorithms are getting better because there's there's so many people working on this now and so and so again I mean the you know I

**[34:08]** I'm not making a normative statement here this is what should happen uh I'm not even saying this necessarily will happen because I think there's important safety and government questions here which we're very actively working on I'm

**[34:20]** just I'm just saying like left to itself this is what the economy is going to do we'll get to those questions in a second but um how do you think about the contribution of anthropic to that increasing in the scope of this industry

**[34:33]** where I mean there's an argument that listen with that investment we can work on safety stuff at anthropic and another that says you're raising the salience of this field in general yeah I mean it's all it's all costs and benefits right

**[34:45]** the costs are not zero right so I think a mature way to think about these things is you know not not to deny that there are any costs but to think about what the costs are and what the benefits are you know I think I think we've been

**[34:56]** relatively responsible in the sense that you know the big acceleration that that happened late last year and and beginning of this year like we didn't cause that we were we weren't the ones who did that and honestly I think if you

**[35:08]** look at the reaction to Google that that might be 10 times more important than anything else and then kind of once it had happened once the ecosystem had changed then we did a lot of things to kind of to kind of stay on the frontier

**[35:19]** um and and and so I don't know it's it's I mean it's like any other question right it's like you're trying to you're trying to do the things that have the biggest costs and the that have the lowest costs and the biggest benefits

**[35:30]** um and you know that that causes you to have different strategies at different times one question I have for you while we were talking about the intelligence stuff was listen as a scientist yourself is it what do you make of the fact that

**[35:42]** these things have basically the entire Corpus of human knowledge memorized and as far as I'm aware they haven't been able to make like a single new connection that has led to a discovery whereas if even a moderately intelligent

**[35:53]** person had this much stuff memorized they'd notice oh this thing causes this symptom this other thing also causes the symptom you know there's a medical cure right here right what should we be expecting that kind of stuff I'm not I'm

**[36:04]** not sure I mean I think you know I don't know these words Discovery creativity like it's one of the lessons I've learned is that in you know in kind of the Big Blob of compute often these these ideas often end up

**[36:17]** being kind of fuzzy and Elusive and hard to track down but I think I think there is something here which is I think the models do display a kind of ordinary creativity again again you know the kind of like you know write a write

**[36:30]** us on it you know in the style of Cormac McCarthy or Barbie or so you know like there is some creativity to that and I think they do draw you know new connections of the kind that an ordinary person would draw I I agree with you

**[36:43]** that there haven't been any kind of like I don't know like I would say like big scientific discoveries I think that's a mix of like just the model skill level is not is not high enough yet right like I was on a podcast last week where where

**[36:58]** the host said I don't know I played with these models they're kind of mid right like they get you know they get a b or a B minus or something and and that that I think is going to change with uh with the scaling I do think there's an

**[37:08]** interesting point about well the models have an advantage which is they know a lot more than us you know like should should they have an advantage already even even if they their skill level isn't isn't isn't quite High maybe

**[37:20]** that's kind of what you're getting at I don't really have an answer to that I mean it seems certainly like memorization and facts and drawing connections is an area where models are ahead and I I do think maybe you need

**[37:32]** those connections and you need a fairly high level of skill I do think particularly in the area of biology for better and For Worse the complexity of biology is such that the current models know a lot of things right now and

**[37:48]** that's what that's what you need to make discoveries and draw it's not like physics where you need to you know you need to think and come up with a formula in biology you need to know a lot of things right and so I do think the

**[37:57]** models know a lot of things and they have a skill level that's not quite high enough to put them together and I think they are they are just on the cusp of being able to put these things together on that point last week in your Senate

**[38:08]** testimony you said that these models are two to three years away from potentially enabling large-scale biotourism attacks or something like that can you make that more concrete without obviously giving the kind of information that would but

**[38:20]** is it like one-shotting how to weaponize something is it or do you gotta find to an open source model like what would that actually look like I think it'd be good to clarify this because we did a blog post in the Senate testimony and

**[38:30]** like I think various people kind of didn't understand the point or didn't understand what we'd done so I think today and you know of course in our models we try and you know prevent this but there's always jailbreaks you can

**[38:42]** ask the models all kinds of things about biology and get them to say all kinds of scary things yeah uh but often those scary things are things that you could Google and I'm I'm therefore not particularly worried about that

**[38:56]** um I think it's actually an impediment to see in the real danger where you know someone just says oh I asked this model like you know for the small pot you know for to tell me some things about smallpox and it will that that is

**[39:07]** actually you know kind of not what I'm worried about so we spent about six months working with some of basically some of the folks who are the most expert in the world on how to how do biological attacks happen

**[39:20]** um you know what what would you need to conduct such an attack and how do we defend to get such an attack they worked very intensively on just the entire workflow of if I were trying to do a bad thing it's not one shot it's a

**[39:33]** long process there are many steps to it um it's not just like I asked the model for this one page of information and again without going into any detail the thing I said in the Senate testimony is like there's some steps where you can

**[39:45]** just get information on Google there are some steps that are what I'd call missing they're scattered across a bunch of textbooks or they're not in any textbook they're kind of implicit knowledge and they're not really like

**[39:59]** they're not explicit knowledge they're they're they're they're more like I have to do this lab protocol and like what if I get it wrong oh if this happens then then my temperature was too low if that happened I needed to add more of this

**[40:12]** particular reagents what we found is that for the most part those missing those key missing pieces the models can't do them yet but we found that sometimes they can um and when they can sometimes they

**[40:26]** still hallucinate which is the thing that's that's kind of keeping us safe but we saw enough signs of the models doing doing those those key things well and if we look at you know state-of-the-art models and go backwards

**[40:40]** to previous models we look at the trend it shows every sign of two or three years from now we're gonna have a real problem yeah especially the thing you mentioned on the lock scale you go from like 100

**[40:52]** times it gets it right to one in ten two exactly so you know I've seen many of these like grocks in my life right I was there when I I watched when gbt3 learned to do arithmetic when gpt2 learned to do regression a little bit above chance

**[41:06]** when you know when we got you know with Claude and we got better on like you know all these all these tests of helpful honest harmless I've seen a lot of groks this is this is unfortunately not one that I'm excited about but I

**[41:18]** believe it's happening so somebody it might say listen you were a co-author on this post that open AI relates to the gpd2 where they said you know we're not gonna release the weights or the details here because we're worried that this

**[41:29]** model will be used for something you know bad and looking back on it now it's laughable to think that gpd2 could have done anything bad are we just like way too worried this is a concern that doesn't make sense for her it is

**[41:43]** interesting um it might be worth looking back at the actual text of that post um so I don't don't remember it exactly but it should it you know it's it's still up on the internet it says something like you know we're choosing

**[41:55]** not to release the weights uh because of concerns about misuse but it also said this is an experiment we're not sure if this is necessary or the right thing to do at this time but we'd like to establish a norm of thinking carefully

**[42:09]** about these things um you know you could think of it a little like the you know the the cylinder conference in the in the 1970s right where it's like you know they were just figuring out recombinant DNA you

**[42:21]** know it was not necessarily the case that someone could do something really bad with recombinant DNA it's just the possibilities were starting to become clear those words at least were the right attitude now I think there's a

**[42:31]** separate thing that like you know people don't just judge the post they judge the organization is this an organization that you know is produces a lot of hype or that has credibility or something like that and

**[42:44]** so I think that had some effect on it I guess you could also ask like is it inevitable that people would just interpret it as like uh you know you can't get across any message more complicated than this thing right here

**[42:57]** is dangerous um so you can argue about those but I think the the basic thing that was in my head in the head the head of others who were who were involved in that and you know I think what what is what is

**[43:08]** evident in the post is like we actually don't know we have pretty wide error bars on what's dangerous and what's not so we should you know like we we want to establish a norm of being careful I I think by the way we have enormously more

**[43:20]** evidence we've seen enormously more of these grocks now and so we're well calibrated but there's still uncertainty right in all these statements I've said like in two or three years we might be there right there's a substantial risk

**[43:31]** of it and we don't want to take that risk but you know I wouldn't say it's it's 100 it could be 50 50. okay let's talk about cyber security which in addition to bioresk is another thing anthropic has been emphasizing how have

**[43:43]** you avoided the cloud micro architecture from leaking because as you know your competitors have been less successful at uh this kind of security can't comment on anyone else's security don't know what's going on in there a thing that we

**[43:55]** have done is uh you know so so there are there are these these architectural Innovations right that make training more efficient we call them compute multipliers because they're the equivalent of you know improving

**[44:06]** improving uh you know uh uh they're like having more compute our compute multipliers again I don't want to say too much about it because it could allow an adversary to counteract our our measures but we limit the number of

**[44:19]** people who are aware of of a given compute multiplier to those who need to know about it um and so there's there's a very small number of people who could leak all of these secrets there's a larger number of

**[44:31]** people who could leak one of them um but you know this is the standard compartmentalization strategy that's used in the intelligence Community or you know resistant cells or or whatever um so you know we we've over the last uh

**[44:45]** over the last few months we've implemented these measures so you know I don't want to jinx anything you might say no this could never happen to us um but I think I think it would be harder for it to happen

**[44:55]** um I don't want to go into any more detail and you know but by the way I'd encourage all the other companies to do this as well it's as much as like competitors architectures leaking is is narrowly helpful to anthropic it's not

**[45:06]** good for anyone in the long run right um so security around this stuff is really important even with all the security you have could you with your current security prevent a dedicated state level actor from getting the claw

**[45:18]** two weights it depends how dedicated is what is what I would say are our head of security who who was you know used to work on security for Chrome which you know yeah very widely used an attacked application he likes to think about it

**[45:32]** in terms of how much would it cost to attack anthropic successfully I again I don't want to go into Super detail of how much I think it will cost to attack and it's kind of inviting people but like one of our goals is that it costs

**[45:43]** more to attack anthropic than than it costs to just straighten your own model um uh which doesn't guarantee things because you know of course you need the talent as well so you might still but you know but but attacks have have risks

**[45:55]** who's the Diplomatic costs uh you know and and and they use up the very the very sparse resources that nation state actors might have in order to to do to do the attacks um so we're not there yet by the way but

**[46:07]** I but I think I think we're to a very high standard compared to the size of company that we are like I think if you look at security for most 150 person companies like I think there's there's just no comparison

**[46:21]** um but you know could we could we resist if if it was a state actor's top priority to steal our model weights no they would they would succeed how long does that stay true because at some point the value keeps increasing and

**[46:35]** increasing and another part of this question is that what kind of a secret is how to train Cloud through your Cloud 2 is it you know with nuclear weapons for example we had lots of spies you just take a blueprint across and that's

**[46:49]** the implosion device and that's what you need here is it just is it more tacit like the thing you're talking about biology you need to know how these reagents work is it just like you got the blueprint you got the micro

**[46:58]** architecture and Hyper parameters there are some things that are like you know a one line equation and there are other things that are more complicated yeah um and I think compartmentalization is the the best way to do it just limit the

**[47:10]** number of people who know about something if you're a thousand person company and everyone knows every secret like one I guarantee you have some you have a leaker and two I guarantee you have a spy like a literal spy okay let's

**[47:20]** talk about alignment and let's talk about mechanistic interpretability which is the branch yes of which you um you guys specialize in while you're answering this question you might want to explain what mechanistic

**[47:29]** interpretability is but just um the broader question is mechanistically what is alignment is it that you're locking in the model into a benevolent Character Are You disabling deceptive circuits and procedures like what concretely is

**[47:45]** happening when you align a model I think as with most things you know when we actually train a model to be aligned we don't know what happens inside the model right there are different ways of training it to be aligned but I think we

**[47:57]** don't really know what happens I mean I think for some of the current methods I think all the current methods that involve some kind of fine-tuning of course have the property that the underlying knowledge and abilities that

**[48:07]** we might be worried about don't don't disappear that's just you know the model is just taught not to Output them I don't know if that's a fatal flaw or if you know or if that's just the way things have to be I don't know what's

**[48:20]** going on inside mechanistically and I think that's the whole point of mechanistic interpretability to really understand what's going on inside the models at the level of individual circuits eventually when it's solid what

**[48:31]** does a solution look like where what is it the case where if a cloud four you do the mechanistic activity thing and you're like I'm satisfied it's a line what is it that you've seen yeah so I I think I think we don't know that yet I

**[48:45]** think we don't know enough to to know that yet I mean I can I can give you a sketch for like what the process looks like as opposed to what the final result looks like um so I think verifiability is a lot of

**[48:56]** the challenge here right we have all these methods that purport to align AI systems and and do succeed at doing so for today's tasks but then the the question is always if you add a more power beautiful model or if you had a

**[49:09]** model in a different situation would it would it would it be aligned and so I think this problem would be much easier if you had an oracle that could just scan a model and say like okay I know this model is aligned I know what it'll

**[49:21]** do in every situation um then the problem would be much easier and I think the closest thing we have to that is something like mechanistic interpretability it's not anywhere near up to the task yet but I guess I would

**[49:34]** say I think of it as almost like an extended training set an extended test set right everything we're doing all the alignment methods we're doing are the trading set right you you know you can you can run tests in them but will it

**[49:45]** really work out a distribution will really work in another situation mechanistic interpretability is the only thing that even in principle and we're nowhere near there yet but even in principle is the thing where it's like

**[49:57]** it's more like an x-ray of the model than a modification of the model right it's more like an assessment than an intervention and so somehow we need to get into a dynamic where we have an extended test set an extended training

**[50:10]** set which is all these alignment methods and the extended test set which is kind of like you you X-ray the model and say like okay what worked and what didn't in a way that goes beyond just the empirical tests that you've that you've

**[50:23]** that you've run right um where you're saying what is the what what is the model going to do in these situations what is it within its capabilities to do instead of what did it do phenomenologically and

**[50:36]** of course we have to be careful about that right one of the things I think is very important is we should never train for interpretability because I think that is that's taking away that Advantage right you even have the

**[50:47]** problem you know similar to like validation versus test set where like if you look at the X-ray too many times you can interfere but I think that's a much weaker option we should worry about that but that's a that's a much weaker

**[50:59]** process it's not automated optimization we should just make sure as with validation and test sets that we don't look at the validation set too many times before running the test set but you know that's again that's that's more

**[51:11]** of a that's that manual pressure rather than automated pressure and so some solution where it's like we have some dynamic between the training and test set where it's like we're we're trying things out and we we

**[51:24]** really figure out if they work via way of testing them that the model isn't optimizing against some some orthogonal way like if if I if I think of and I think we're never going to have a guarantee but some process where we we

**[51:37]** do those things together again not in a stupid way there's lots of stupid ways to do this where you fool yourself but like some way to put extended training for alignment ability with extended testing

**[51:50]** for alignment ability together in a way that actually works I I still don't feel like I understand the intuition that like why you think this is likely to work or this is a promising to pursue and let me ask the question in a certain

**[52:02]** more specific way and excuse the tortured analogy but listen if you're you're an economist and you want to understand the economy yeah so you send a whole bunch of microeconomists out there and one of them studies how the

**[52:13]** restaurant business works one of them studies how the tourism business works you know one of them started each other baking works and at the end they all come together and you still don't know where there's going to be a recession in

**[52:23]** five years or not why is this not like that where you have an understanding of we understand how induction heads work and a two-layer Transformer we understand you know modular arithmetic how does this add up to does this model

**[52:35]** want to kill us like what is this model fundamentally want a few things on that I mean I think that's like the right set of questions to ask I think what we're hoping for in the end is not not that will understand every detail but again I

**[52:47]** would give like the X-ray or the MRI analogy that like we can be in a position where we can look at the broad features of the model and say like is this a model whose internal state in plans are very different from what it

**[53:01]** externally represents itself to do right is this a model where we're uncomfortable that you know far too much of its computational power is uh you know is is devoted to doing what looked like fairly destructive and manipulative

**[53:15]** things again we don't know for sure whether that's possible but I I think some at least positive signs that it might be possible again the model is not intentionally hiding from you right it might turn out that the training process

**[53:28]** hides it from you and you know I can think of cases where the model is really super intelligent it like thinks in a way so that it like affects its own cognition I suspect we should think about that we should consider everything

**[53:39]** I I I suspect that it may roughly work to think of the model as you know if it's trained in in in the normal way just at you know at the at the just getting to just above human level it it may be a reason we should check it may

**[53:56]** be a reasonable assumption that the internal structure of the model is not intentionally optimizing against us and I give an analogy like to humans so it's actually possible um to you know to look at an MRI of

**[54:11]** someone um and predict above random chance whether they're a psychopath um there was actually a story a few years back about a neuroscientist who was studying this and they looked at his

**[54:21]** own scan and discovered that he was a psychopath and then everyone everyone in his life was like no no that's this is obvious like you're you're a complete like you must be a psychopath um and he was totally unaware of this

**[54:33]** the basic idea that um you know that that there there can be these macro features that like like psychopath is probably a good analogy for it right they're like you know this is what we would be afraid of model that's kind of

**[54:44]** like Charming on the surface very goal oriented and you know very dark on the inside uh you know and and you know on the surface their behavior might look like the behavior of someone else but their goals are very different a

**[54:55]** question somebody might have is listen you know you mentioned earlier the importance of being empirical yeah um and in this case you're trying to estimate you know listen are these activations sus yeah um but is this

**[55:08]** something we can be a for to be empirical about in on you know or do we need like a very good first principle theoretical reason to think no it's not just that these MRIs of the model correlate with uh you know being bad we

**[55:22]** need just like some just like deep root math proof that this is aligned so it depends what you mean by empirical I mean a better term would be phenomenological like I don't think we should be purely phenomenological and

**[55:33]** like you know here are some brain scans of like really dangerous models and here are some brain scans I think the whole idea of mechanistic interpretability is to look at the underlying principles and circuits but I guess the way I think

**[55:45]** about it is like on one hand I've actually always been a fan of studying these circuits at the lowest level of detail that we possibly can and the reason for that is kind of that's how you build up knowledge even

**[55:57]** if you're ultimately aiming for there's two there's too many of these features it's too complicated at the end of the day we're trying to build something broad um and we're trying to build some broad

**[56:07]** understanding I think the way you build that up is by trying to make a lot of these very specific discoveries like you have to you have to understand the building blocks and and then you have to figure out how to kind of use that to

**[56:19]** draw these broad conclusions even if you're not going to figure out everything you know I think you should probably talk to Chris Ola who would have much more detail right this is my kind of

**[56:29]** high level thinking on it like crisola controls the interpretability agenda like you know he's he's the one who decides what to what to do on interpretability this is my high level thinking about it which is not going to

**[56:40]** be as good as his there's a bookcase on anthropic rely on the fact that mechanistic interpretability is helpful for capabilities I I don't think so at all um uh now I do think I I think in

**[56:52]** principle it's possible that mechanistic interpretability could be helpful with capabilities we might for various reasons not choose to talk about it if that were the case uh that you know that that wasn't something that I thought

**[57:04]** thought of or that any of us thought of at the time of andropics founding I mean we we thought of ourselves as like you know we're people who are like good at scaling models and good at doing safety on top of those models and like you know

**[57:16]** we think that we have a very high Talent density of folks who are good at that and you know my view has always been Talent density beats Talent Mass um and so you know that's that's more that's more of our bull case Talent

**[57:28]** density beats Talent Mass I don't think it it depends on some particular thing like others are starting to do mechanistic interpretability now and I'm very glad that they are uh you know that was that is a part of our a part of our

**[57:39]** a part of our theory of change is paradoxically to make other organizations more like us Italian density I'm sure is important but another thing anthropic has emphasized is that you need to have Frontier models

**[57:50]** in order to do Safety Research and of course like actually be a company as well the current Frontier Model is something somebody might guess like GPD four o'clock to like 100 million or something like that that general or

**[58:00]** order of magnitude in very broad terms is not wrong but you know we're two to three years from now the kinds of things you're talking about we're talking more and more orders of magnitude to keep up with that and to if it's the case that

**[58:12]** safety requires community on the frontier I mean what is the case in which anthropic is like competing with these leviathans to stay on that same scale I mean I think it's uh I think it's a very it's a situation with a lot

**[58:23]** of trade-offs right I think it's I think it's not easy um I guess to go back maybe I'll just like answer the questions one by one right so like to go back to like you know why it why is safety so tied to

**[58:33]** scale right um some people don't think it is but like if I if I just look at like you know where where have been where have been the areas that you know you know I don't know like safety methods have like

**[58:44]** been put into practice or like worked for something for anything even if we don't think they'll they'll work in general you know I go back to thinking of all the ideas you know something like you know debate and amplification right

**[58:56]** you know back in 2018 when we wrote papers about those at open AI it was like well human feedback isn't isn't quite gonna work but you know debating amplification will take us beyond that but then if you if you actually look at

**[59:09]** and we've you know done attempts to do debates we're really limited by the by the quality of the model uh where it's like you know for two models to have a debate that is coherent enough that a human can judge it so that the training

**[59:24]** process can actually work you need models that are at or maybe even Beyond on some topics the current Frontier now you can come up with with the method you can come up with the idea without being on the frontier but I you know for me

**[59:37]** that's a very small fraction of what needs to be done right it's very easy to come up with these methods it's very easy to come up with like oh the problem is X maybe a solution is why but you know I I really want to know you know

**[59:49]** whether things work in practice even for the systems we have today and I want to know what kinds of things go wrong with them I I just feel like you discover 10 new ideas and 10 new ways that things that can go wrong by trying these in

**[1:00:01]** practice and that that empirical learning I think it's it's not just not as widely understood as it should be kind of every you know I would say the same thing about methods like constitutional Ai and some people say oh

**[1:00:13]** it doesn't matter like we know this method doesn't work it won't work for you know pure alignment I neither agree nor disagree with that I think that's just kind of overconfident the way we discover new things and understand the

**[1:00:24]** structure of what's going to work and what's what's not is by playing around with things not that we should just kind of blindly say oh this Rook here so it'll work there but you you really you really start to understand the patterns

**[1:00:36]** like with like with the scaling laws even mechanistic interpretability which might be the one area I see where a lot of progress has been made without the frontier models we're you know we're seeing and you know the work that say

**[1:00:48]** open AI put out a couple a couple months ago that you know using very powerful models to help you Auto interpret the weak models again that's not everything you can do in interpretability but you know that's a that's a big component of

**[1:01:02]** it and we you know we found it useful too and so you see this this this phenomenon over and over again where it's like you know the the scaling and the safety are these two snakes that are like coiled with each other always even

**[1:01:16]** more than you think right you know with interpretability like I think three years ago I didn't think that this would be as true of interpretability but somehow it manages to be true why because intelligence is useful it's

**[1:01:27]** useful for a number of tasks one of the tasks that's useful for is like figuring out how to judge and evaluate other intelligence and maybe someday even even for you know doing the alignment research itself given all that's true

**[1:01:39]** what what does that imply for anthropic when in two to three years these leviathans are doing like 10 billion dollar trading runs uh Choice one is if it if we can't or if it costs too much to stay on the frontier then you know

**[1:01:51]** then then we shouldn't uh then we shouldn't do it and you know we won't work with the most advanced models we'll see what we can get with you know models that are not quite as advanced I think you can get some value there like

**[1:02:02]** non-zero value but I'm I'm kind of skeptical that the value is all that high or the learning can be fast enough to really to really be in favor of the task the second option is you just you just find a way you just uh you know you

**[1:02:15]** just accept the trade-offs and I think the trade-offs are more positive than they appear because of a phenomenon that I've called race to the top um I could go into that later but I'll just let me put that aside for now uh

**[1:02:29]** and then I think the third phenomenon is you know as things get as things get to that scale I think this may coincide with you know starting to get into some non-trivial probability of very serious danger again I think it's going to come

**[1:02:44]** first from misuse the kind of Bio stuff that I talked about but I don't think we have the level of autonomy yet to worry about some of the you know alignment stuff happening in like two years but it might not be very far behind that at all

**[1:03:00]** you know that that may that may lead to unilateral or multilateral or government enforced which we support decisions uh not to scale as fast as we could um that may end up being the right thing

**[1:03:14]** to do so I you know actually that's kind of like I I kind of hope things go in that in that direction and then we don't have this hard trade-off between we're not in the frontier and we can't quite do the research as well as well as we

**[1:03:25]** want or influence other orgs as well as we want um or versus we're kind of on the frontier and like have to accept the trade-offs which are which are net positive but like have a have a lot in

**[1:03:36]** both in both directions okay on the missus versus misliment those are both problems as you mentioned but in the long scheme of things what what is what are you concerned about like 30 years down the line which do you think will be

**[1:03:48]** consider a bigger problem I think it's much less than 30 years um but I'm I'm worried about both I don't know if you have if you if you have a model that could in theory you know like take over the world on its own

**[1:04:00]** um if you were able to control that model then you know it follows pretty simply that you know if model was following the wishes of some small subset of people and not others then those people could use it to take over

**[1:04:11]** the world on their on their behalf the very premise of misalignment means that we should be be worried about misuse as well with similar levels of consequences but but some people who might be more doomery than you would say misuse is

**[1:04:26]** you're already working towards the optimistic scenario there because you've at least figured out how to align the model with the bad guys now you just need to make sure that it's aligned with the good guys instead why do you think

**[1:04:37]** that you could get to the point where it's aligned with the bat you know you haven't already saw this I guess if you had the view that like alignment is completely unsolvable then uh you know then you'll be like well I don't you

**[1:04:47]** know we're dead anyway so I don't want to worry about misuse that's not my position at all but but also like you should think in terms of like what's a plan that would actually succeed that would make things good any plan that

**[1:04:58]** actually succeeds regardless of how hard misalignment is to solve any problem any plan that actually succeeds is going to need to solve misuse as well as misalignment it's getting to solve the fact that like as the AI models get

**[1:05:11]** better you know faster and faster they're going to create a big problem around the balance of power between countries they're going to create a big problem around is it possible for a single individual to do something bad

**[1:05:22]** that it's hard for everyone else to stop any actual solution that leaves do leads to a good future needs to solve those problems as well if your perspective is we're screwed because we can't solve the first problem so don't worry about

**[1:05:34]** problems two and three like that that's not really a statement you shouldn't worry about problems two and three right like they're in our path what no matter what yeah in the scenario we succeed we have to solve all so yeah we might as

**[1:05:46]** well operate we should be planning for Success not for failure if research doesn't happen and the right people have the Superhuman models what does that look like like who are the right people who is actually controlling the model

**[1:05:57]** from five years from now yeah I mean my my view is that these things are powerful enough that I think you know it's it's going to involve you know substantial role or at least involvement of you know some kind of government or

**[1:06:13]** assembly of government bodies again like you know they're they're kind of very naive versions of this like you know I don't think we should just you know I don't know like he hand the model over to the U.N or whoever happens to be in

**[1:06:24]** office at a given time like I could see that go poorly but they're it's it's too powerful there needs to be some kind of legitimate process for managing this technology which you know includes the role of the people building it includes

**[1:06:38]** the role of like democratically elected authorities includes the role of you know all the all the individuals who will be affected by it so that they're they're at the end of the day there needs to be some politically legitimate

**[1:06:52]** process but what that look like if it's not the case that you just hand it to whoever the president is at the time yeah is what does the body look like what I I mean this is something these are things it's really hard to know

**[1:07:02]** ahead of time like I think you know people love to kind of propose these broad plans and say like ah this is the way we should do it this is the way we should do it I think the honest fact is that we're figuring this out as we go

**[1:07:12]** along and that you know anyone who says you know this is this is the body that you know we should create this kind of body modeled after this thing like I think I think we should try things and experiment with them with less powerful

**[1:07:25]** versions of the technology we need to figure this out in time but but also it's not the really the kind of thing you can know in advance the the long-term benefit trust that you have how did how would that interface with

**[1:07:36]** this body is that the body itself if not is it like was it just for the content protection system I want to explain what it is for the audience but I don't know I think of the long-term benefit trust is like a much a much narrower thing

**[1:07:46]** like this is something that like makes decisions for anthropic so this is basically a body is described in a recent Vox article we'll be saying more about it in you know later later this year uh but it's basically a body that

**[1:08:00]** over time uh gains the ability to appoint the majority of the board seats of anthropic uh and this is so you know it's a mixture of experts and I'd say like AI alignment National Security and philanthropy in general but if control

**[1:08:16]** is handed to them of anthropic that doesn't imply that control of if anthropic has AGI the control of AGI itself is handed them that doesn't imply that anthropic or any other entity should be the entity that like makes

**[1:08:27]** decisions about AGI on behalf of humanity I would think of those as different I mean there's lots of maybe you know like if anthropic does play a broad role then you'd want to like widen that body to be you know like a whole

**[1:08:38]** bunch of different people from around the world or or maybe you can screw this as very narrow and then you know there's some like broad committee somewhere that like manages all the agis of all the companies on behalf on behalf of anyone

**[1:08:50]** um I I don't know like I I think my view is you you shouldn't be sort of overly constructive in utopian like we're dealing with a new problem here we need to we need to start thinking now about you know what are the what are the

**[1:09:03]** governmental bodies and structures that could that could deal with it okay so let's forget about governance let's just talk about what this going well looks like obviously there's the things we can all agree on you know cure all the

**[1:09:13]** diseases you know solve all the problems every things all humans would say I'm down for that yeah but now it's 20 30 you've solved all the real problems that everybody can agree on what what happens next what what are we doing with a

**[1:09:25]** superhuman God I think I actually want to like I don't know like disagree with the framing or something like this um I I actually get nervous when someone says like what are you gonna do with the Superhuman AI like we've learned a lot

**[1:09:37]** of things over the last 150 years about like markets and democracy and each person can kind of Define for themselves like what what the best way for them to have The Human Experience is and that you know society's workout norms and

**[1:09:52]** what they value in this just in this very like complex and decentralized way now again if you have these safety problems that can be a reason why you know and especially from the government there needs to be maybe until we solve

**[1:10:04]** these problems a certain amount of like centralized control but but as a matter of like we've solved all the problems now how do we make things good I think that that most most people most groups most ideologies that started with like

**[1:10:17]** let's sit down and think up to think I think think over what the definition of the good life is like I think I think most of those have led to disaster but so this Vision you have a sort of tolerant liberal democracy

**[1:10:28]** market-oriented system with a AGI like what is each person has their own AGI like what is that what does that mean I don't know I don't know what it looks like right like I guess what I'm saying is like we need to solve the kind of

**[1:10:40]** important safety problems and the important externalities and then and then subject to that you know which again you know those could be just narrowly about alignment there could be a bunch of economic issues that are

**[1:10:52]** super complicated and that we can't solve you know subject to that like we should think about what's worked in the past and I think in general like unitary Visions for what it means to to live a good life have have not worked out well

**[1:11:05]** at all on on the opposite end of things going well or good actors having control of AI um we might want to touch on China as like a potential actor in the space so first of all I mean being at Baidu and

**[1:11:18]** like this seeing progress in AI happening generally why do you think the Chinese have underperformed you know Baidu had a scaling laws group many years back um or is the premise wrong and I'm just

**[1:11:29]** not aware of the progress that's happening there um well for the scaling laws group I mean that was an offshoot of the stuff we did with speech um so uh you know there were still some people there but that was a mostly

**[1:11:38]** Americanized lab I mean I was there for a year that was you know my first foray in a deep learn it was led by Andrew Wing I never went to China most you know there's like a U.S lab so I think that was somewhat uh disconnected although it

**[1:11:51]** was an attempt by you know a Chinese entity to kind of get it get into the game uh but I don't know I think since then you know I couldn't speculate but I think they've been maybe very commercially focused and not as focused

**[1:12:03]** on these kind of fundamental research side of things around scaling laws now I do think because of all the you know excitement with the release of chat GPT in you know November or so um you know that's been a starting gun

**[1:12:18]** for them as well and they're trying very aggressively to catch up now I think we're the U.S is quite substantially ahead but I think they're trying very hard to catch up now how do you think China thinks about AGI are they thinking

**[1:12:30]** about safety and misuse or not I I don't really have a sense um you know one concern I would have or if people say things like well China isn't going to develop an AI because you know they like stability or you know

**[1:12:43]** they're going to have all these restrictions to make sure things are in line with what the CCP wants you know that that might be true in the short term and for Consumer products My worry is that if the basic incentives are

**[1:12:55]** about National Security and power um that's going to become clear sooner or later um and and so you know they're they're I think they're gonna if they see this as you know a source of National Power

**[1:13:05]** they're going to at least try to do to do what's most effective and that you know that could lead them in the direction of AGI at what point it like is it possible for them they just get your blueprints or your code base or

**[1:13:16]** something that they can just spin up their own lab that is competitive at the frontier with the leading American company well I don't know about fast but I'm like I'm concerned about this um so this is one reason why we're

**[1:13:27]** focusing so hard on cyber security um you know we've worked with our Cloud providers we really you know like you know we have this blog post out out about security where we said you know we have a two key system for access to the

**[1:13:39]** model weights we have other measures that we put in place so thinking or putting in place that you know we haven't announced we don't want an adversary to know about them but we're happy to talk about them broadly all

**[1:13:50]** this stuff we're doing is is by the way not sufficient yet for super determined state state level actor at all um uh I think it it will defend against most attacks and against a a state level actor who's not you know who's less

**[1:14:06]** determined uh but there's a lot more we need to do and some of it may require new research on how to do security okay so let's talk about what it would take at that point uh you know we're at anthropic offices and you know it's like

**[1:14:18]** God good at security we had to get Badges and everything to come in here but the eventual version of this building or bunker or whatever where the AGI is built I mean what does that look like are we is it a building in the

**[1:14:30]** middle of San Francisco or is it you're out of the middle of Nevada or Arizona like what is the point in which your like Los alamosing it at one point there was a running joke somewhere that you know the way the way building AGI would

**[1:14:42]** look like because you know there would be a data center next to a nuclear power plant next to a bunker yeah um and you know that we we'd all we'd all kind of live in the bunker and everything would be local so it wouldn't get on the

**[1:14:51]** internet um you know again if we you know if we take seriously the rate at which the you know the rate at which all this is going to happen which I don't know I can't be sure of it but if we take that seriously

**[1:15:03]** then it you know it it does make me think that maybe not something quite as cartoonish as that but that something like that might happen what is the time scale on which you think alignment is solvable if like these models are

**[1:15:16]** getting to human level or in some things in two to three years what is the point at which they're aligned I think this is a really difficult question because I actually think often people are thinking about kind of alignment in the wrong way

**[1:15:26]** I I think there's a general feeling that it's like models are misaligned or like there's like an alignment problem to solve kind of like the Riemann hypothesis or something like someday we'll crack the Riemann hypothesis

**[1:15:39]** I don't quite think it's like that not in a way that's I that's worse or better it might be just as bad or just as just as unpredictable when when I think of like you know why am I why am I scared um few things I think of one is look

**[1:15:53]** like I think the thing that's really hard to argue with is like there will be powerful models they will be agentic we're getting towards them if such a model wanted to wreak havoc and Destroy Humanity or whatever I I think we have

**[1:16:07]** basically no ability to stop it like that's that's I think just just if that's not true at some point it'll continue to be true as we you know it will reach the point where it's true as we scale the models

**[1:16:18]** um so that definitely seems the case and I think a second thing that seems the case is that we seem to be bad at controlling the models not in any particular way but just their statistical systems and you can ask a

**[1:16:31]** million things and they can say a million things and reply uh and you know you might not have thought of a millionth of one thing that does something crazy or when you you train them you train them this very abstract

**[1:16:41]** way and you might not understand all the consequences of of what they do in response to that I mean I think the best example we've seen of that is like being in being in Sydney right where it's like I I don't know how they train that model

**[1:16:53]** I don't know what they did to make it do all this weird stuff like you know threaten threaten people and you know have this kind of weird obsessive personality but but what it shows is that we can get something very different

**[1:17:04]** from and maybe opposite to what we intended and so I actually think facts number one and fact number two are like enough to be really worried um like you don't need all this detailed stuff about you know conversion

**[1:17:18]** instrumental goals or you know analogies to Evolution like actually one and two for me are pretty motivated I'm like oh yeah this thing's gonna be powerful it could destroy us and like all the ones we built so far are like you know are at

**[1:17:31]** pretty decent risk of doing some random we don't understand yeah if I agree with that and I'm like okay I'm concerned about this the researchers and you have of a mechanistic interpretability plus you know

**[1:17:42]** Constitution Ai and the other IL HF stuff if you say that we're going to get something with like bio weapons or something that could be dangerous in two to three years yes do these things culminate within two to three years of

**[1:17:54]** actually meaningfully contributing to yeah preventing yes so I think I think where I was going to go with this is like you know people talk about like Doom by default or alignment by default like I think it might be kind of

**[1:18:05]** statistical like you know like you might get you know with the current models you might get Bing or Sydney or you might get clawed and it doesn't really matter because Binger Sydney like if we take our current understanding and and you

**[1:18:18]** know move that to to very powerful models you might just be in this world where it's like okay you make something and depending on the details maybe it's totally fine um you know not really alignment by

**[1:18:28]** default but but just kind of like it depends on a lot of the details and like if you if you're very careful about all those details and you know what you're doing you're getting it right but we have a high susceptibility to you mess

**[1:18:39]** something up in a way that you didn't really understand was connected to actually instead of making all the humans happy it wants to you know turn them into pumpkins yeah I you know I just some weird right because the

**[1:18:49]** models are so powerful you know they're like these kind of giants that are you know they're they're like you know they're standing in a landscape and if they start to move their arms around randomly they could just break

**[1:18:58]** everything um I I guess I'm starting it with that with that kind of framing because it's not like I don't think we're lying by default I don't think we're doomed by default and have some problem we need to

**[1:19:08]** solve it has some kind of different character now what I do think is that hopefully within a time scale of 2 to three years we get better at diagnosing when the models are good and when they're bad we get better at training

**[1:19:22]** you know increasing our repertoire of methods to train the model that they're less likely to do bad things and more likely to do good things in a way that isn't just relevant to the current models but scales and we can help

**[1:19:35]** develop that with interpretability as the test set I don't think of it as oh man we tried our lhf it didn't work we tried constitutional it didn't work like we tried this other thing it didn't work we tried mechanistic interpretability

**[1:19:46]** now we're going to try mechanistic um I think this Frame of like man we haven't cracked the problem yet we haven't solved the Riemann hypothesis isn't quite right I think of it more as already with today's systems we are not

**[1:20:01]** very good at controlling them and the consequences of that could be could be could be very bad we just need to get more ways of like increasing the likelihood that are that are that you know that we can control our models and

**[1:20:14]** understand what's going on in them and like we have some of them so far they aren't that good yet um but you know I I don't think if this is binary of like works and not works we're going to develop more and I do

**[1:20:27]** think that over over the next two to three years we're going to start eating that probability mass of ways things can go wrong um you know it's kind of like in the core safety views paper there's

**[1:20:36]** probability mass of how hard the problem is I feel like that way of seeing it isn't really even quite right right because I don't feel like it's the remodel hypothesis to solve I I you know I I just feel like you know it's almost

**[1:20:48]** like right now if I try and you know juggle five balls or something I can juggle three balls right I actually can but but I can't juggle five balls at all right you have to practice a lot to do that if I were to do that I would mostly

**[1:20:59]** draw I would I would almost certainly drop them and then just just over time you just get better at the task of controlling the balls on that post in particular what is your personal probability distribution over so for the

**[1:21:11]** audience the three possibilities are it is like trivial to align these models with rlhf plus plus to it is a difficult problem but one that a big company could solve to something that is like basically impossible for human

**[1:21:24]** civilization currently to solve if I'm capturing those three what is your probability distribution over those three personally yeah I mean I'm not super into like what's your probability distribution of X I think all of those

**[1:21:35]** have enough likelihood that you know they should be considered seriously I'm more interesting question I'm much more interested in is what could we learn that shifts probability Mass between them what is the answer to that I think

**[1:21:46]** that one of the things mechanistic interpretability is going to do more than more than necessarily solve problems is it's going to tell us what's going on when we try to align models um I I I I think it's basically going to

**[1:22:00]** teach us about this like one way I could imagine concluding that things are very difficult is if mechanistic interpretability sort of shows us that I don't know problems tend to get moved

**[1:22:13]** around instead of being Stamped Out or that uh you get rid of one problem you create another one or it might Inspire us or give us insight into why problems are kind of persistent or hard to eradicate or crop up like for me to

**[1:22:28]** really believe some of these stories about like you know oh something will always you know there's always this conversion goal in this particular direction I think the abstract story is it's not uncompelling but I don't find

**[1:22:40]** it really compelling either nor do I find it necessary to motivate all the safety work but like the kind of thing that would would really be like oh man we can't solve this is like we see it happening inside inside the X-ray

**[1:22:52]** because yeah because I I think right now there's just there's there's way there's way too many assumptions there's way too much overconfidence about how all this is gonna go um I have a substantial probability Mass

**[1:23:03]** on this all goes wrong it's a complete disaster um but in a completely different way than anyone had anticipated it would be besides the point to ask like how could it Go different than anyone anticipated

**[1:23:12]** so on this in particular what information would be relevant how much would the difficulty of aligning Cloud three and the next generation of models basically be like is that a big piece of information is that so so I think the

**[1:23:26]** people who are most worried are predicting that all the sub-human like AI models are going to be alignable right they're going to seem aligned they're going to deceive Us in some way I think it

**[1:23:38]** certainly gives us some information but uh I I am more interested in what mechanistic interpretability can tell us um because uh again like you see this x-ray it would be too strong to say it doesn't lie but at least in the current

**[1:23:55]** systems it doesn't feel like it's optimizing against us there are exotic ways that it could you know I I don't think anything is a safe bet here but I think it's the closest we're going to get to something that isn't actively

**[1:24:06]** optimizing against us all right let's talk about the specific methods other than mechanistic interpretability yes that you guys are researching when we talk about um rlhf or you know Constitution AI whatever rhf plus plus

**[1:24:18]** if you had to put it in terms of human psychology what is the change that is happening are we creating new drives new goals new thoughts how is the models changing in terms of psychology when it I think all those terms are kind of like

**[1:24:34]** inadequate for you know describing what's it's not clear how useful they are as abstractions for humans either I think we don't have the language to describe what's going on and again I'd love to have the X-ray I'd love to look

**[1:24:44]** inside and say and and kind of actually know what we're talking about instead of you know basically making up words which is what which is what I do what am I what you're doing and asking this question

**[1:24:55]** um where where you know we should we should just be honest we have we really have very little idea what we're what we're talking about so you know it would be great to say well what we actually mean by that is you know this circuit

**[1:25:06]** within here turns you know turns on and you know and you know after we've trained the model then you know this circuit is no longer operative or weaker or not yeah I would love to be able to say again we're it's going to take a lot

**[1:25:18]** of work to be able to do that model organisms which you hinted at before when he said we're doing these evaluations to see if they're capable of you know doing dangerous things now and currently not how worried are you about

**[1:25:28]** a lab leak scenario where in fine-tuning it or in trying to get these models to elicit dangerous behaviors you know make bio weapons or something yeah like leaks somehow and actually makes the bio weapon instead of telling you it can

**[1:25:41]** make the bio weapon with today's passive models I think it's not that much you know chat Bots it's not so much of a concern right because it's like you know if we were to fine-tune a model do that we do it privately and work with the

**[1:25:53]** experts and so you know the the leak would be like you know suppose the model got open sourced or something and you know and then someone so so I think for now it's mostly a security issue in terms of models truly being dangerous I

**[1:26:07]** mean you know I think I think we do have to worry that it's like you know if we make a truly powerful model and we're trying to like see what makes it dangerous or safe then they're could be more of a One-Shot thing where it's like

**[1:26:19]** you know some risk that the model takes over I think the main way to control that is to make sure that the capabilities of the model that we test are not such that they're capable of doing this at what point were the

**[1:26:29]** capabilities be so high where you're you say I don't even want to test this oh well there's different things I mean there's capability testing and you know but that itself could lead totally if you're attaching it and replicate that

**[1:26:39]** like what if it actually does sure but I I think I I mean I think what you want to do is you want to like extrapolate so we've talked with Arc about this right you know you have like factors of two of compute or something where you know

**[1:26:50]** you're like okay you know you know can can the model do something like you know open up an account on AWS and like make some money for itself like some of the things that are like obvious prerequisites to like complete survival

**[1:27:02]** in the wild um and so just set set those thresholds very well you know kind of very well below and then as you proceed upward from there do kind of more and more rigorous tests and be more and more

**[1:27:14]** careful about about what it is on uh Constitution Ai and feel free to explain what this is for the audience but who decides what the constitution for the next generation of models or potentially superhuman model is like how is that

**[1:27:28]** actually written I think initially you know to make the Constitution we just took some stuff that was like broadly agreed on like the UN Charter of you know U.N Declaration on human rights and um you know some of the stuff from

**[1:27:40]** Apple's terms of service right stuff that's like you know consensus unlike what's acceptable to say or like you know what what basic things are able to be included so one I think for future constitutions we're looking into like

**[1:27:52]** more participatory processes for making these um but I think beyond that I don't think there should be like one Constitution for like a model that everyone uses like probably models Constitution should be

**[1:28:05]** very very simple right it should only have very basic facts that everyone would agree on and then there should be a lot of ways that you can customize including a pending you know constitutions and and you know I think

**[1:28:17]** beyond that we're developing new methods right this is you know I'm not imagining that this or this alone is the method that we'll use to train superhuman AI right many of the parts of capability training may be different and so you

**[1:28:30]** know it could look very different and again I'd go there like they're levels above this like I'm pretty uncomfortable with like here's the ai's Constitution it's going to run the world like that you know again like just normal lessons

**[1:28:44]** from like how societies work and how politics works like that that just kind of yeah that that strikes me as fanciful like I you know I think I think we should try to hook these things into you know even even when they're very

**[1:28:58]** powerful again after we've mitigated the safety issues like any good future even even if it has all these security issues that we need to solve it somehow needs to end with with something that's that's that's more decentralized and you know

**[1:29:13]** less like a god-like super and you know I I just I just don't think that ends well uh what scientists from the Manhattan Project do you respect most in terms of the acted most ethically under the constraints they were given well is

**[1:29:26]** there one that comes to mind I don't don't know I mean I you know I think there's there's a lot of answers you could give I mean I'm definitely a fan of zillard for having kind of figured it figured it out he was then you know

**[1:29:36]** against the the against the the actual dropping of the bomb I don't actually know the history well enough to have an opinion on whether you know demonstration of the bomb could have could have ended the war I mean that

**[1:29:47]** involves a bunch of facts about Imperial Japan that are you know that are that are complicated and that I that I'm not an expert on um but you know zillard seemed to you know he he discovered this stuff early

**[1:29:58]** he kept it secret you know you know you know patented some of it and put it in the hands of the British admiralty um so you know he seemed to display the right kind of awareness as well as as well as uh as well as discovering

**[1:30:13]** stuff I mean it was when I read that book that I kind of you know when I wrote this Big Blob of compute Doc and many other you know I only showed it to a few people and there were other docs that I showed to almost no one uh so you

**[1:30:24]** know I yeah it was a bit a bit inspired by this again I mean I you know we could all get self-aggrandizing here like we don't know how it's gonna turn out or if it's actually gonna be actually gonna be something on par with the Manhattan

**[1:30:35]** Project I mean you know this this could all be just Silicon Valley people building technology and you know just kind of like having delusions of grandeur so I don't know how it's gonna turn out I mean if if the scaling stuff

**[1:30:46]** is true then it's more bigger than that right yeah yeah it certainly it certainly could be bigger I I just you know we should always kind of I don't know maintain this attitude that it's it's really easy to fool yourself if you

**[1:30:57]** were asked by the government if you're a physicist during World War II and you were asked by the government to contribute non-replaceable research to the Manhattan Project well what do you think you would have said yeah I mean I

**[1:31:06]** think giving you're in a war with the Nazis um at least During the period when you thought that the Nazis were I I don't yeah I don't really see much choice but uh but uh but to do it if it's possible

**[1:31:17]** you know you have to figure it's going to be done within within 10 years or so by someone regarding cyber security what should we make of the fact that there's a whole bunch of tech companies which have ordinary tech companies security

**[1:31:29]** policy that publicly seeming facing it's not obvious that they've been hacked like coinbase still has its Bitcoin um you know Google as far as I know my Gmail hasn't been leaked should we take

**[1:31:41]** from that that current status code tech companies security practices are good enough for AGI or just simply that nobody has tried hard enough it would be hard for me to speak to you know current tech company practices and of course

**[1:31:52]** there may be many attacks that we don't know about where things are stolen and then silently used you know I mean I think an indication of it is when someone really cares basically cares about attacking someone uh then then

**[1:32:04]** often the attacks happen so um you know recently we saw that some fairly High officials of the US government had their email accounts hacked via VIA Microsoft Microsoft was providing the email accounts

**[1:32:18]** um so you know presumably that that related to information that was you know of great interest to you know to foreign adversaries um and so it it sounds it seems to me at least you know that the evidence is more

**[1:32:30]** consistent with you know when something is really high enough value then uh you know then then you know someone acts and it's stolen and My worry is that if course with with AGI will get to a world where you know the value is seen as

**[1:32:44]** incredibly high right that you know it'll be like stealing nuclear missiles or something you can't be too careful on this stuff um and you know at every place that I've worked I push for the cyber security to

**[1:32:55]** be better one of my concerns about cyber security is you know it's not it's not kind of something you can trump it I think a good Dynamic with Safety Research is like come you know you can get companies into a dynamic and I think

**[1:33:07]** we have where you know you can get them to compete to do the best Safety Research and you know kind of use it as a I don't know like a like a recruiting point of competition or something we used to do this all the time with

**[1:33:18]** interpretability you know and and then sooner or later other other orgs started recognizing the defect and started working on interpretability whether or not you know that you know like whether or not that was a priority to them

**[1:33:30]** before but I think it's harder to do that with cyber security because a bunch of the stuff you have to do in quiet and so you know we did try to put out one post about it but I think you know most you just you just see the results

**[1:33:42]** um you know I think people should you know a good Norm would be you know people see the cyber security leaks from companies or you know leaks of the model parameters or something and say you know that they they screwed up that's that's

**[1:33:54]** that that's bad if I'm a safety person I might not want to work there um of course as soon as I as soon as I say that we'll probably have a security breach tomorrow but uh um you know but but that's that's that's part of the

**[1:34:04]** game here right that's I think that's part of um you know trying trying to make things safe I I want to go back to the thing we're talking about earlier where the ultimate level of cyber security required for two to three years

**[1:34:15]** from now and whether it requires a bunk like are you actually expecting to be in a physical bunker in two to three years or is that just a metaphor yeah I mean I think I think that's a metaphor um you know we're still figuring it out

**[1:34:25]** like something I would think about is like I think security of the data center which may not be in the same physical location as us but you know we've worked very hard to make sure it's in the United States but securing the physical

**[1:34:37]** data centers and the gpus I think some of the real really expensive attacks if someone was really determined just involved going into the data center and just you know trying to steal steal the data directly or as it's flowing from a

**[1:34:50]** data center to you know to to us I think these data centers are going to have to be built in a very special way I mean given the way things are scaling up you know probably anyway heading to a world where you know the you know networks of

**[1:35:03]** data centers you know cost as much as aircraft carriers or something um and and so you know they're already going to be pretty unusual objects but I think in addition to being unusual in terms of their ability

**[1:35:13]** you know to to link together and train gigantic gigantic models that are also going to have to be very secure speaking of which how you know there's been sorts of rumors on the difficulty of procuring the power and the gpus for the next

**[1:35:26]** generation of models what has the process been like to secure the the necessary components to do the Next Generation that's something I can't go into great detail about uh you know I I will say look like you know people think

**[1:35:38]** of even industrial scale data centers right people are not thinking at the scale that I think these models are going to go to very soon and so whenever you do something in a scale where it's never been done before you know every

**[1:35:50]** every single component every single thing has to be done in a new way than it was before and so you know you may you may you may run into problems with you know surprisingly simple components power is one that you mentioned and is

**[1:36:03]** this something that anthropic has to handle or can you just Outsource it you know I mean for data centers we work with Cloud providers for instance what should we make about the fact that these models require so much much training and

**[1:36:15]** the entire Corpus of internet data in order to be sub-human whereas you know if gpd4 there's been estimates that you know it was like a 10 to 25 flops or something where you know whereas you I mean you can take these numbers through

**[1:36:30]** grain of salt but there's reports that you know human brain from the time it is born to the time a human being is 20 years old that's like on the order of 10 to the 20 flops to simulate all those interactions you don't have to go to the

**[1:36:42]** particulars on those numbers but should we be worried about how sample inefficient these models seem to be yeah so I think that's one of the remaining Mysteries one way you could phrase it is that the models are

**[1:36:53]** maybe two to three orders of magnitude smaller than the human brain If you compare the number of synapses while at the same time being trained on you know three to four or more orders of magnitude of data if you compare to you

**[1:37:06]** know number of words human human sees as they're developing to age 18. it's I don't remember exactly but I think it's in the hundreds of millions whereas for the models we're talking about the hundreds of billions of the trillions so

**[1:37:19]** what what explains this there are these offsetting things where the models are smaller they need a lot more data and they're still below human level but so you know there's some way in which you know the analogy to the brain is not

**[1:37:34]** quite right or is breaking down or there's some there's some missing Factor you know this is just kind of like in physics where it's like you know we can't explain the Mickelson morally experiment or like I'm forgetting one of

**[1:37:44]** the other 19th century physics paradoxes but like I think it's one thing we don't quite understand right humans see so little data and they still do fine uh one theory on it it could be that it you know it's it's like our other modalities

**[1:37:59]** um you know how do we get you know 10 to the 14th bits into the human brain well well most of it is kind of these images and maybe a lot of what's going on inside the human brain is like you know our mental workspace involves all these

**[1:38:11]** these you know these these simulated images or something like that but honestly I think intellectually we have to admit that that's a weird thing that doesn't match up and you know it's one reason I'm a bit you know skeptical a

**[1:38:22]** kind of biological analogies I thought in terms of them like five or six years ago but now that we actually have these models in front of us as artifacts it feels like almost all the evidence from that has been screened off by what we've

**[1:38:34]** seen and what we've seen are models that are much smaller than the human brain and yet yet can do a lot of the things that humans can do and yet paradoxically require a lot more data so maybe we'll discover something that makes it all

**[1:38:46]** efficient or maybe we'll understand why the discrepancy is present but at the end of the day I don't think it matters right if we keep scaling the way we are I think what's more relevant at this point is just measuring the abilities of

**[1:38:58]** the model and seeing how far they are from humans and they don't seem terribly far to me does this scaling picture and the Big Blob of compute more generally does that underemphasize the role that algorithmic progress is played when you

**[1:39:11]** compose the um the the Big Blob of compute so you know you're talking about lstms presumably at that point presumably the scaling on that would not have you at Cloud 2 at this point so are you underemphasizing the world that uh

**[1:39:24]** an improvement of the scale of Transformer could be having here when you put it behind the label scaling this Big Blob of compute document which I still have not made public I probably should for like historical reasons I

**[1:39:34]** don't think it would tell anyone anything they don't know now but uh when I wrote it I actually said look there are seven factors that and you know I wasn't I wasn't like these are the factors but I was just like no it gives

**[1:39:45]** some sense of the kinds of things that matter and what don't and so I wasn't thinking like these are the you know there could be nine there could be five but like the things I said were I said number of parameters scale of the model

**[1:39:57]** like you know the compute and compute matters quantity of data matters quality of data matters loss function matters so like you know are you doing RL are you doing next word prediction if your loss function isn't rich or doesn't

**[1:40:11]** incentivize the right thing you won't you won't get anything um so those were the key four ones uh which I think are the core of the hypothesis but then I said three more things one was symmetries which is

**[1:40:23]** basically like if your architecture doesn't take into account the right kinds of symmetries it doesn't work um or it's it's very inefficient so so for example convolutional neural networks take into account translational

**[1:40:36]** symmetry lstms take into account time Symmetry and but a weakness of lstms is that they can't attend over the whole context so there's kind of this structural weakness like if a model isn't structurally capable of like

**[1:40:51]** absorbing and managing things that happened in a far enough distant past and it's just like it's kind of like you know like the compute doesn't flow like the spice doesn't flow it's like you you can't like like the The Blob has to be

**[1:41:05]** unencumbered right it kind of it's not it's not going to work if if you artificially close things off and I think rnns and lstms artificially close things off because they they close you off to the distant past

**[1:41:18]** um and so again things need to flow freely if they don't it doesn't work and then you know I I added a couple things one of them was like conditioning which is like you know if you're if the thing you're optimizing with is just really

**[1:41:30]** numerically bad like you're gonna have trouble and so this is why like Adam works better than you know than normal sdd and I I think I'm forgetting what the seventh condition was but it was it was similar to things like this where

**[1:41:42]** it's like you know if you if you if you set things up in kind of a way that's that's set up to fail or that doesn't allow the compute to work in an uninhibited way then it won't work and so Transformers were kind of within that

**[1:41:54]** even though I can't remember if the Transformer paper had been published it was around the same time as I wrote that document it might have been just before it might have been just after it sounds like from that view that the the way to

**[1:42:07]** think about these algorithmic progresses is not as increasing the power of The Blob of compute but simply getting rid of the artificial hindrances that older architectures have is that is that's a little that yeah that's that's a little

**[1:42:19]** how I think about it you know again if you go back to like Ilias like the models want to learn yeah yeah like like the compute wants to be free yeah yeah and like you know it's being blocked in various ways where you like don't

**[1:42:30]** understand that it's being blocked and so you need to like free it up right right I I love the the radiance to change that to spice okay um on that point though so do you think that another thing on the scale of a

**[1:42:43]** transformer is coming down the pike to enable the next the next great iterations I think it's possible I mean people have worked on things like you know trying to model very long time dependencies or you know

**[1:42:57]** you know there's various different ideas where I could see that we're kind of missing an efficient way of representing or dealing with something so I think those inventions are possible I guess my perspective would be even if they don't

**[1:43:10]** happen we're all we're already on this very very steep trajectory and so I'm less I mean we're constantly trying to discover them as our as our others um but things are already on such a fast trajectory all that would do is speed up

**[1:43:23]** the trajectory even more um and probably probably not by that much because it's already going so fast is something embodied or having an embodied version of a model is that at all important in terms of getting either

**[1:43:34]** data or progress I think of that Less in terms of the you know like a new architecture and More in terms of like a loss function like the the data the environment you're exposing yourself to end up being very different and and so I

**[1:43:47]** think that could be important for learning some skills although data acquisition is hard and so things have gone through the language route and I would guess well continue to go through the language

**[1:43:58]** route even as you know even as as more as possible in terms of embodiment and then the other possibilities you mentioned RL you can see it as yeah I mean we we kind of already do RL with our OHF right people are like this is an

**[1:44:10]** alignment is the capabilities I always think in terms of the two snakes right they're they're kind of often hard to distinguish so we already kind of use RL in these language models but I think we've used RL Less in terms of getting

**[1:44:22]** them to take actions and you know do things in the world but you know when you take actions over a long period of time and understand the consequences of those actions only later than you know RL is a typical tool we have for that so

**[1:44:34]** I would guess that in terms of models taking action in the world that RL will you know will become a thing with all the power and all the safety issues that come with it when you project out in the future do you see the way in which these

**[1:44:46]** things will be integrated into productive uh Supply chains do you see them talking with each other and criticizing each other and contributing to each other's output or is it just the model one shots the one model one shots

**[1:44:59]** the the answer or the work models will undertake extended tasks that will have to be the case I mean we may want to limit that to some extent because it may make some of the safety problems easier um but you know some of that I think

**[1:45:13]** will be required in terms of our models talking to models or are they talking to humans again this goes kind of out of the technical realm and into the like socio-cultural economic realm where my heuristic is always that it's very very

**[1:45:29]** difficult to predict things um and so I I feel like these scaling laws have been very predictable but then when you say like well you know when when is there going to be a commercial explosion in these models or what's the

**[1:45:41]** form it's going to be or are the models going to do things instead of humans or pairing with humans I feel like certainly my track record on predicting these things is terrible uh but I also looking around I don't really see anyone

**[1:45:53]** who's track record is great you mentioned how fast progress is happening but also the difficulties of integrating within the existing economy into the way things work do you think there will be enough time to actually have large

**[1:46:06]** revenues from AI products before the next model is just so much better or we're in like a different landscape entirely it depends what you mean by by large right you know I think multiple companies are already in the you know

**[1:46:17]** 100 million to billion per year range will it get to the 100 billion or trillion range you know before I that stuff is just so hard to predict right it's and it's it's it's not even super well defined like you know I think right

**[1:46:33]** now there are companies that are throwing a lot of money at at generative AI you know as as customers but and and they'll you know I think I think that's the right thing for them to do and they'll you know they'll find uses for

**[1:46:44]** it but it doesn't mean there doesn't mean it's you know they're finding uses or the best uses from day one so even money Changing Hands is not is not quite the same thing as economic value being created but surely you've thought about

**[1:46:55]** this from the perspective of anthropic wherever these things are happening so fast then it should be an insane valuation right even us who have you know not been super focused on commercialization and more on safety I

**[1:47:06]** mean you know the graph goes up um and it goes up it goes up relatively quickly yeah um so you know I can I can only imagine what's happening at you know the origin or you know that this is this is this is their singular Focus

**[1:47:20]** um so it's certainly happening fast but you know again it's it's like it's the exponential from the small base while the technology itself is moving fast so it's it's kind of a race between how fast the technology is getting better

**[1:47:32]** and how fast it's integrated into the economy and that I think that's just a very unstable and turbulent process both things are going to happen fast but if you ask me exactly how it's going to play out exactly what order

**[1:47:44]** things are going to happen I I I I don't know and I'm just kind of skeptical of the ability to predict I'm kind of curious with regards to anthropic specifically yeah your public benefit Corporation yes and rightfully so you

**[1:47:57]** want to make sure that this is an important technology the obviously the only thing you want to care about is not sure about their value but how do you talk to investors who are putting in like hundreds of millions billions of

**[1:48:07]** dollars of money like how do you talk to them about the fact that how do you get them to put in this amount of money without yes the shareholder value being the main concern so so I think the ltbt is is you know the right thing on this

**[1:48:19]** right you know I mean we're gonna talk more about the ltbt but like some version of that has been in development since the beginning of of anthropic even even formally right and so you know from from the beginning you know even as the

**[1:48:32]** body has has changed in some ways it's like from the beginning it was like this body is going to exist and it's you know it's on you like every traditional investor who invests in anthropic you know has to you know looks at this some

**[1:48:45]** of them are just like whatever you run your company how you want some of them are like you know oh my God like this this you know this body of random people or to them random people could like you know could could move anthropic in a

**[1:48:57]** Direction that's you know that's totally contrary to our and now there are there are legal limits on that of course but you know we have to have this conversation with every investor and then it gets into a conversation of well

**[1:49:07]** what are the kinds of things that you know that we would we we might do that would be contrary to the to the you know to the interests of of traditional investors and just have having those conversations has helped get everyone on

**[1:49:19]** the same page I want to talk about the the physics and the fact that so many of the founders and the employees at uh anthropic are physicist what is the I mean we talked in the beginning about the scaling laws and how the power laws

**[1:49:32]** and physics are something you see here but you know what are the actual like approaches and ways of thinking from physics that seem to have carried over so well is that notion of effective theory is super useful you know what is

**[1:49:43]** going on here I I mean I think part of it is just physicists learn things really fast we have generally found that uh you know if we hire you know someone who is a you know physics PhD or something that they can they can learn

**[1:49:55]** ML and contribute just very very quickly in in most cases and you know because several of our Founders myself Jared Kaplan uh Sam Sam McCandless we're physicists we knew a lot of other physicists and so we were able to hire

**[1:50:07]** them and now there's I don't know how many is exactly you know might be 30 or 40 of them here ml is not still not yet a field that has an enormous amount of depth and so they've been able to get up to speed very quickly are you concerned

**[1:50:20]** that there's like a lot of people who would have been doing physics or something whatever they could go into Finance instead and since anthropic exists they have now been recruited to go into Ai and you know they're you

**[1:50:34]** obviously care about AI safety but you know maybe in the future they leave and they get funded to do their own thing is that a concern that you're bringing more people into the ecosystem here yeah I mean you know I think there's there's

**[1:50:44]** like a broad set of action you know like we're causing gpus to exist you know there's there's a lot of kind of side effects that you can't that that you can't currently control or that you just incur if you buy into the idea that you

**[1:50:55]** need to build Frontier models and that's one of them a lot of them would have happened anyway I mean Finance was a hot thing 20 years ago so physicists were doing it now ml is a hot thing thing and you know it's not like we've caused them

**[1:51:06]** to do it when they had no interest previously but you know again you know at the margin you're kind of you're kind of bidding things up um and you know a lot of that would have happened anyway some of it some of it

**[1:51:17]** wouldn't but it's all part of the calculus do you think that cloud has conscious experience How likely do you think that is this is another of these questions that just seems very unsettled and uncertain uh one thing I'll tell you

**[1:51:27]** is I used to think that we didn't have to worry about this at all until models were kind of like operating in Rich environments like not necessarily embodied but like that you know they you know they needed to like have a reward

**[1:51:39]** function and like have kind of long-lived experience so I still think that might be the case but the more we've looked at kind of these language models and particularly looked inside them to see things like induction heads

**[1:51:51]** a lot of the cognitive Machinery that you would need for active agents seems kind of already present in the base language models so I'm not quite as sure as I was before that were missing the things that you know that we're missing

**[1:52:05]** enough of the things that you would need I think today's models just probably aren't smart enough that we should worry about this too much but I'm not 100 sure about this and I do think the models will get in a year or two like this

**[1:52:17]** might be a very real concern what would change if you found out that they are conscious are you worried that you're like pushing the negative gradient to suffering like what is conscious is again one of these words that I I

**[1:52:28]** suspect it will like not end up having a a well-defined but it's like something to be but that yeah but but that yeah well I I I suspect that's that's a spectrum right uh so I don't know if we if we if we discover like that you know

**[1:52:41]** that I should care about let's say we discover that I should care about collage experience as much as I should care about like a dog or a monkey or something yeah I I would be I would be kind of kind of worried right I don't

**[1:52:52]** know if their experience is positive or negative unsettlingly I also don't know like I wouldn't know if any intervention that we made was more likely to make Claude you know have a positive versus negative experience versus not having

**[1:53:06]** one if there's an area that is helpful with this it's maybe mechanistic interpretability because I think if it is neuroscience for models and so it's possible that we could we could shed some shed some light on this although

**[1:53:17]** you know it's not it's not a straightforward factual question right it kind of depends what we mean and what we value we talked about this initially but I I want to get more specific we talked initially about you know now that

**[1:53:28]** you're seeing these capabilities ramp up within the human Spectrum you think that the human spectrum is wider than we thought but yeah more specifically what have you how is the way you think about human intelligence different now that

**[1:53:41]** the way you're seeing these these marginally useful abilities emerge how does that change your picture of what intelligence is I think for me the big realization on what intelligence is came with the like blob of compute thing

**[1:53:53]** right like it's not you know there might be all these separate modules there might be all this complexity um you know it's It's You Know Rich Sutton called it the bitter lesson right it's almost called has many names it's

**[1:54:04]** been called the scalene hypothesis like the first few people who figured it out was around 2017 or I mean you could go further back to I think I think Shane Lake was maybe the first person who really knew it maybe Ray cartswell

**[1:54:16]** although in a very vague way um but you know I think the num the number of people who understood it went up a lot around 2014 to 20 2017. but I think I think that was the big the big realization it's like you know well how

**[1:54:29]** did Intelligence evolve well if you don't need very specific conditions to create it if you can create it just from like the right kind of the right kind of gradient and loss signal then of course

**[1:54:40]** it's not so mysterious how it all happened in terms you know it had this click of scientific understanding in terms of like watching what the models can do how has it changed my view of human intelligence I wish I had

**[1:54:53]** something more intelligent to say on that uh I I feel like I don't know one thing that's been surprising is like I thought things might click into place a little more than they do like you know I thought like different cognitive

**[1:55:07]** abilities might all be connected and there was more of one secret behind them but it's like the model just learns various things at different times you know it can be like very good at coding but like you know it can't it can't

**[1:55:19]** quite you know approve the prime number theorem yet and I don't I mean I guess it's a little bit the same for for humans although it's it's weird the juxtaposition of things it can do and not I guess the main lesson is like

**[1:55:30]** having Theories of Intelligence or how intelligence works like again a lot of these words just just kind of like dissolve into a Continuum right they just kind of like dematerialize I think less in terms of

**[1:55:44]** intelligence and More in terms of what we see in front of us yeah now it's really surprising to me uh two things one is how discrete these like different Paths of intelligent um uh things that contribute to loss are rather than just

**[1:55:56]** being like one reasoning circuit or one general intelligence and the other thing talking with you that is surprising or interesting is many years from now it'll be one of those things that looking back it'll be

**[1:56:07]** why did why weren't why wasn't this obvious to you if you're seeing these smooth scaling curves why the time where you're not completely convinced so you've been less public than the CEOs of other AI companies you know you're

**[1:56:19]** not posting on Twitter you're not doing a lot of podcasts except for this one what what what gives like why are you why are you off the radar yeah I I aspire to this and I'm proud of this um if people think of me as kind of like

**[1:56:32]** boring and low profile like this is actually kind of what I want um so I don't know I've I've Just Seen A number of cases a number of people I've worked with um that I think you could say Twitter

**[1:56:43]** although I think I mean a broader thing like just kind of like attaching your incentives very strongly to like the approval or cheering of a crowd um I I think that can destroy your mind and in some cases it can destroy your

**[1:56:55]** soul and so I think I've kind of deliberately tried to be a little bit low profile because I wanna I don't know kind of like defend my ability to think about things intellectually in in a way that's different from other people and

**[1:57:10]** isn't isn't kind of tinged by the approval of other people so so you know I've seen cases of folks who are deep learning Skeptics and they become known as deep learning Skeptics on Twitter and then even as it starts to become clear

**[1:57:23]** to me they've kind of sort of changed their mind they like this is their thing on Twitter and they can't change their Twitter Persona and so forth and so on I don't really like the trend of kind of like personalizing companies like the

**[1:57:35]** whole you know like cage match between CEOs approach like I think it it distracts people from the actual merits and concerns of like the the you know the the company in question like I I kind of want people to like judge the

**[1:57:50]** like nameless bureaucratic institution um you know I I want people to think in terms of the nameless bureaucratic institution and its incentives more than they think in terms of me everyone wants a friendly face but but actually I think

**[1:58:02]** friendly faces can be misleading okay well in this case this will be a misleading interview because this has been a lot of fun maybe like a glass to talk to indeed yeah this isn't a blast I'm super glad you came on the podcast

**[1:58:13]** and uh hope people enjoy it thanks thanks for having me hey everybody I hope you enjoyed that episode as always the most helpful thing you can do is just share the podcast send it to

**[1:58:25]** people you think might enjoy it put it in Twitter your group chats Etc just splits the world appreciate your listening I'll see you next time cheers foreign

**[1:58:40]** foreign
