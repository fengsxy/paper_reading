---
date: 2024-01-01
layout: default
type: transcript
series: dwarkesh
episode: 107
guest: ""
title: "How Did Dario & Ilya Know LLMs Could Lead to AGI?"
source_url: "https://www.youtube.com/watch?v=Iq4YStiGADs"
analysis_url: /transcripts/dwarkesh/107_how_did_dario_ilya_know_llms_could_lead_to_agi.analysis/
permalink: /transcripts/dwarkesh/107_how_did_dario_ilya_know_llms_could_lead_to_agi/
---

# Transcript: How Did Dario & Ilya Know LLMs Could Lead to AGI?

Source: https://www.youtube.com/watch?v=Iq4YStiGADs

---

**[00:00]** just before open AI started I met Ilia who you who who you interviewed one of the first things he said to me was look the models they just want to learn you have to understand this the models they just want to learn and it was a bit like

**[00:11]** a Zen Coen like I kind of like I listened to this and and I became enlightened um the models just want to learn you get the obstacles out of their way right you give them you give them good data you you give them enough space

**[00:26]** to operate in you don't do something stupid like condition them badly numerically um and and they want to learn they'll do it they'll do it there were many people who were aware back at that time probably weren't working on it

**[00:38]** directly but we're aware that these things are really good at speech recognition or at playing these constrained V games very few extrapolated from there like you and Ilia did to something that is generally

**[00:52]** intelligent what what was different about the way you were thinking about it versus how others think that you went from like it's getting better at speech in this consistent way it will get better at every everything in this

**[01:00]** consistent way yeah so I I genuinely don't know I mean at first when I saw it for speech I assumed this was just true for speech or for this narrow class of models I I think it was just over the period between 2014 and 2017 I tried it

**[01:15]** for a lot of things and saw the same thing over and over again I watched the same being true with DOTA I watched the same being true with robotics which many people thought of as a counter example but I just thought well it's hard to get

**[01:27]** data for robotics but if we operate Within if we look within the data that we have we see the same patterns and so I don't I don't know I think people were very focused on solving the problem in front of them why one person thinks one

**[01:42]** way another person thinks it's very it's very hard to explain I think people just see it through a different lens you know are looking like vertically instead of horizontally they're not thinking about the scaling they're thinking about how

**[01:53]** do I solve my problem and well for robotics there's not enough data and so you know and so you know that can easily abstract to well scaling doesn't work because we don't have the data and and

**[02:04]** so I don't I I I don't know I just for some reason and it may just it may just have been random chance was obsessed with that particular direction this Big Blob of compute document which I still have not made public I probably should

**[02:16]** for like historical reasons I I don't think it would tell anyone anything they don't know now but uh when when I wrote it I I actually said look there are seven factors that and you know I wasn't I wasn't like these are the factors but

**[02:28]** I was just like let me give some sense of the kind of things that matter and what don't and so number of parameters scale of the model like you know the compute and compute matters quantity of data matters quality of data matters

**[02:41]** loss function matters so like you know are you doing RL or are you doing next word prediction if your loss function isn't rich or doesn't incentivize the right thing you won't you won't get anything um so those were the key four

**[02:53]** ones uh which I think are the core hypothesis but then I said three more things one was symmetries which is is basically like if your architecture doesn't take into account the right kinds of symmetries it doesn't work um

**[03:07]** or it's it's very inefficient so for example convolutional neural networks take into account translational symmetry lstms take into account time Symmetry and but a weakness of lstms is that they can't attend over the whole context so

**[03:22]** there's kind of this structural weakness like if a model isn't structurally capable of like absorbing and man in things that happened in a far enough distant past then it's just like it's kind of like you know like the compute

**[03:35]** doesn't flow like the spice doesn't flow it's like you can't like like the The Blob has to be unencumbered right it kind of it's not it's not going to work if if you artificially close things off and I think rnn's and lstms artificially

**[03:51]** close things off because they they close you off to the distant past um and so again things need to flow freely if they don't it doesn't work if you set things up in kind of a way that's that's set up to fail or that doesn't allow the

**[04:04]** compute to work in an uninhibited way then then it won't work and so Transformers were kind of within that even though I can't remember if the Transformer paper had been published it was around the same time as I wrote that

**[04:15]** document it might have been just before it might have been just after it sounds like from that view the way to think about these Al algorithmic progresses is not as increasing the power of The Blob of compute but simply getting rid of the

**[04:27]** artificial hindrances that older iectures have is that is that a faira that's that's a little that yeah that's that's a little how I think about it you know again if you go back to like il's like the models want to learn like like

**[04:37]** the compute wants to be free and like you know it's being blocked in various ways where you like don't understand that it's being blocked and so you need to like free it up right right I I love the the gradiance changing that to spice

**[04:50]** okay um when did it become obvious to you that language is the means to just feed a bunch of data into these things that or was was it just you ran out of other things like robotics there's not enough data this other thing there's not

**[05:02]** enough data yeah I mean I think this whole idea of like the next word prediction that you could do self-supervised learning you know that together with the idea that it's like wow for predicting the next word there's

**[05:14]** so much richness in structure there right you know it might say 2 plus two equals and you have to know the answer is four and you know it might be telling the story about a character and then basically it's it's posing to the model

**[05:25]** you know the the equivalent of these developmental tests that get posed to Children you know Mary into the room and you know puts an item in there and then you know Chuck walks into the room and removes the item and Mar Mary doesn't

**[05:35]** see it what does Mary think Happ you know so like so the models are going to have to to get this right in the service of predicting the next word they're going to have to solve you know solve all these theory of Mind problem solve

**[05:46]** all these math problems and so I you know I I my thinking was just well you know you scale it up as much as you can you you you know there's there's kind of No Limit to it and I think I kind of had abstractly that view but but the thing

**[05:59]** of course that like really solidified and convinced me was the work that Alec Radford did on gpt1 um which was not only could you get this this language model that could predict things very well but also you

**[06:12]** could fine-tune it you needed to fine-tune it in those days to do all these other tasks and so I was like wow you know this isn't just some narrow thing where you get the language model right it's sort of halfway to everywhere

**[06:24]** right it's like you know you get the language model right and then with a little move in this direction it can you know it can solve this this you know logical dreference test or whatever and you know with this this other thing you

**[06:36]** know it can it can solve translation or something and then you're like wow I think there's there's really something to do and and of course we can can really scale it
