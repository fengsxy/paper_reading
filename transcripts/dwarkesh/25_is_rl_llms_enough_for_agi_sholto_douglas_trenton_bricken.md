---
layout: default
type: transcript
series: dwarkesh
episode: 25
guest: ""
title: "Is RL + LLMs enough for AGI? — Sholto Douglas & Trenton Bricken"
source_url: "https://www.youtube.com/watch?v=64lXQP6cs5M"
analysis_url: /transcripts/dwarkesh/25_is_rl_llms_enough_for_agi_sholto_douglas_trenton_bricken.analysis/
permalink: /transcripts/dwarkesh/25_is_rl_llms_enough_for_agi_sholto_douglas_trenton_bricken/
---

# Transcript: Is RL + LLMs enough for AGI? — Sholto Douglas & Trenton Bricken

Source: https://www.youtube.com/watch?v=64lXQP6cs5M

---

**[00:00]** Okay, I'm joined again by my friends uh Schultter Bricken. Wait, [ __ ] Did I do this last? No, no, you named us differently, but we didn't have Shto Bricken and Trenton Douglas. Shelto Douglas and Trenton Bricken. Um, uh, who

**[00:18]** are now both at Entropic? Uh, Shto scaling RL. Trenton still working on mechanistic interpability. Um, welcome back. Happy to be here. Yeah, it's fun. What's changed since last year? We talked basically this

**[00:34]** month in 2024. Now we're in 2025. What's happened? Okay, so I think the biggest thing that's changed is RL and language models has finally worked. Um, and this is manifested in we finally have proof of an algorithm that can give us expert

**[00:48]** human reliability and performance given the right feedback loop. And so I think this is only really being like conclusively demonstrated in competitive programming and math basically. uh and so if you think of these two

**[00:59]** axes, one is uh the like intellectual complexity of the task and the other is the time horizon of which the task is uh is being completed on um and I think we have proof that we can we can reach the peaks of intellectual complexity uh

**[01:10]** along along many dimensions. uh we haven't yet demonstrated like longunning agentic uh performance and you're seeing like the first stumbling steps of that now and should see much more like conclusive evidence of that basically by

**[01:23]** the end of the year u with like real software engineering agents doing real work um and I think Trenton you're like experimenting with this at the moment right yeah absolutely I mean the most public example people could go to today

**[01:34]** is Claude plays Pokemon right uh and seeing it struggle in a way that's like kind of painful to watch but each model generation gets further through the game. Uh, and it seems more like a limitation of it being able to use uh

**[01:48]** memory system than anything else. Yeah. Um, I wish we had recorded predictions last year. We definitely should this year. Oh, yeah. Hold us accountable. Yeah, that's right. Would you have said that agents would be only this powerful

**[02:00]** as of last year? I think this is roughly on track for where I expected with software engineering. I think I expected them to be a little bit better at computer use. Uh but I understand all the reasons for why that is and I think

**[02:12]** that's like well on track to be solved. It's just like a sort of temporary uh lapse. Um and holding accountable for like my predictions next year like I really do think end of this year sort of like this

**[02:24]** this time next year we have software engineering agents that can do close to a day's worth of work um for like a junior engineer or like a couple of hours of like quite competent independent work. Yeah, that that seems

**[02:36]** right to me. I think the distribution is pretty wonky though where like for some tasks I don't know like boiler boilerplate website code these sorts of things it can it can bang it out and save you a whole day. Um uh yeah I think

**[02:47]** that's right. I think last year you said that the thing that was holding them back was the extra nines of reliability. I don't know if that's the way you'd still describe the way in which these software agents aren't able to do a full

**[02:58]** day of work but are able to help you out with a couple minutes. Is it is it the extra nines that's really stopping you or is it something else? Yeah, I think my description there was I think like like in retrospect probably not what's

**[03:08]** limiting them. Uh I think what we're seeing now is closer to uh lack of context um lack of ability to like do complex like very multifile changes and like uh sort of like maybe like scope or or of the change or scope of like the

**[03:27]** task in some respects like you can they can cope with high intellectual complexity in like a focused context with a with a very like scoped problem. Um, but when something's a bit more amorphous or requires a lot of discovery

**[03:36]** and iteration with the environment, this kind of stuff, they're they struggle more. Um, and and so maybe the the way I would define it now as the thing that's holding them back is if you can give it a good feedback loop for the thing that

**[03:49]** you want it to do, then it's good. It's pretty good at it. If you can't, then they struggle a bit. Can you and then for the audience, can you say more about what you mean by this feedback loop? Um, if they're not aware of what's happening

**[04:01]** RL and so forth. Yes. Uh so the big thing that really worked over the last year is uh maybe like broadly the domain is called like RL from verifiable rewards or something like this where a clean reward signal. So so you know the

**[04:14]** initial unhopping of language models was RL from human feedback where you know typically was something like pairwise feedback or something like this and and the outputs of the models became closer and closer to things that humans wanted.

**[04:25]** Yeah. uh but this doesn't necessarily improve their performance at any like like difficulty of problem domain right particular as humans are actually quite bad judges of what what a better answer is humans have things like length biases

**[04:37]** and and and so forth so you need a signal of whether the model was correct in its output that is uh that is like quite true let's say uh and so things like the correct answer to a math problem or unit tests passing this kind

**[04:52]** of stuff these are the examples of uh a reward signal that's very clean. But even these can be hacked by the way. Like even unit tests, the models find ways around it to like hack in particular values and hardcode values of

**[05:04]** unit tests. If they can figure out like what the actual test is doing, like if they can like look at the cached Python files and find what the actual test is, they'll they'll try and hack their way around it. So these aren't perfect, but

**[05:14]** they're they're much closer. And why has it gotten so much better at software engineering than everything else? Uh in part because software engineering is very verifiable. uh like it's a domain which just

**[05:26]** naturally lends it to this way. I think does the code pass a test? Does it even run? Does it compile? Yeah. Does it compile? Does it pass the test? U you know, you can go on le code and you can run like tests and like you know whether

**[05:36]** or not you got the right answer. Um but there isn't the same kind of thing for like writing a great essay. That requires uh like the question of like taste in that regard is quite hard. like we

**[05:47]** discussed the other night at dinner um the pullet surprise like you know which would come first like a pullet surprise winning novel or like you know a Nobel Prize or something like this and I actually think a Nobel Prize is more

**[05:58]** likely than a pullet surprise winning novel um in some respects because a lot of the the tasks required in in winning a Nobel Prize or at least like strongly assisting in helping it the to win a Nobel Prize have more like layers of

**[06:11]** verifiability built up. So I I expect them to like accelerate the process of dis of doing Nobel Prize winning work more initially than uh that of like writing Pullet surprisew worthy novels. Yeah, I think if we rewind 14 months to

**[06:26]** when we recorded last time, the nines of reliability was was right to me. Um like we didn't have clawed code, we didn't have deep research. All we did was use agents in a chatbot format, right? Copy paste, copy paste, copy paste. Totally.

**[06:41]** And I and it's I think we're very used to chat interfaces whether we're texting or using Google. Uh and it's weird to think that the agent can actually go and fetch its own context and store its own facts into its memory system. Uh and I

**[06:56]** still think that it's the nines's reliability and and if you scaffold the model correctly or prompt it, it can do much more sophisticated things than the average user assumes. Uh, and so like one of my friends, Sam Rodriguez, who

**[07:10]** does Future House, they've discovered a new drug that they're in the process of patenting, and by the time this episode comes out, that will be that will be live. What was that? LSDV2. Wait, is it really?

**[07:23]** No, no, they're not making LSD. But, uh, like people didn't think that models can be creative or do new science, right? And it does just kind of seem like a skill issue. I mean, there was the cool uh wait but like the it

**[07:40]** discovered a drug. Is it how did it like I think it one-shotted the this was just over a conversation and so we'll need to refer to the full announcement. But my impression is that um it was able to read a huge amount of medical literature

**[07:54]** and brainstorm and make new connections and then propose wet lab experiments that the humans did. And then through iteration on that, they verified that this like new compound does this thing that's really exciting. Um, another

**[08:08]** critique I've heard is like LLM can't write creative long- for books. Um, and I'm aware of at least two individuals who probably want to remain anonymous who have used LLMs to write long form books. And I think in both cases,

**[08:20]** they're just very good at scaffolding and prompting the model. I mean, even with the viral um chat GPT uh geogesser capabilities where it's just insanely good at spotting like what beach you were on from a photo. Um Kelsey Piper,

**[08:35]** who I think made this viral, um their their prompt is so sophisticated. It's really long and it encourages you to think of five different hypotheses and assign probabilities to them and reason through the different aspects of the

**[08:49]** image that matter. And I haven't AB tested it, but I think unless you really encourage the model to be this thoughtful, you wouldn't get the level of performance that you see with with that ability. So you're bringing up ways

**[09:01]** in which people have constrained what the model is outputting to get like the good part of the distribution. But one of the critiques I've heard of RL or the um not of RL but one of the critiques I've heard about using the success of

**[09:16]** models like 03 to suggest that we're like getting new capabilities from these reasoning models is that all these capabilities were already baked in the pre-training model. I think there's a paper from uh Stingwall University where

**[09:29]** they showed that if you give a base model enough tries um to answer a question, it can still answer the question um as well as the reasoning model. Basically, it just has a lower probability of answering. So, you're

**[09:43]** you're narrowing down um the the possibilities that the model explores when it's answering a question. Um, so are we actually eliciting new capabilities with this RL training or are we just like um putting the blinders

**[09:57]** on them, right? Like carving away the marbles or this. Um, I think it's like it's worth noting that that paper was I'm pretty sure on like the llama and Quen models. Um, and I'm not sure how much uh like RL compute they used, but I

**[10:10]** don't think it was anywhere comparable to the amount of compute that was used in the in the base models. And so I think like the amount of compute that you use in training is like a decent proxy for the amount of like actual like

**[10:19]** raw new knowledge or capabilities you're adding to a model. So like my prior at least uh if you look at like all of Deep Mind's research from you know RL before RL was able to teach these like go and chess playing agents new knowledge that

**[10:35]** in excess of human level performance just from RL signal provided the RL signal was sufficiently clean. structurally limiting the prevents it from imet basically. Um why aren't you

**[10:53]** already spending more comput on this? I think Dario said in his blog post that labs or it was like a couple months ago on the export controls thing is like ah deepseeek whatever there we're only spending 1 million on RL or something.

**[11:03]** So it's like uh we aren't in the compute limited regime for RL yet but we will be soon. Yeah, you're spending hundreds of millions on the base model. Why only order a million on the RO? You know that the parable about like when you choose

**[11:16]** to launch a space mission and how like you should like sort of acquire like go further up the tech tree because if you launch later on you're like your ship will go faster and this kind of stuff. I think it's quite similar to that like

**[11:25]** you want to be sure that you're you've algorithmically got the right thing and then when you bet and you do the large compute spend on the run uh then uh like it'll actually pay off. Have the right compute efficiencies and this kind of

**[11:35]** stuff. Um, now I think like RL is slightly different to pre-training in this regard where RL can be a more iterative uh thing like you're progressively adding capabilities to the base model. Pre-training has uh you know

**[11:45]** in many respects like if you're halfway through a run and you've messed it up then like you've you've really like messed it up. Um but uh I think that's that's like the main reason why is people were still figuring out exactly

**[11:57]** what they wanted to do. I mean 01 to 03, right? Like OpenI put in their blog post that it was a 10x compute multiplier over 01. Yeah. Let's get it out there. And then they spent the next few months like, you

**[12:13]** know, increasing the amount of comput that they expend on that. And I expect as everyone is, everyone else is like scaling up RL right now. Um, so I I basically don't expect that to be true for very long. Yeah, just for the sake

**[12:24]** of read listeners maybe um you're doing gradient descent steps in both pre-training and reinforcement learning. It's just the signal is different. Typically in reinforcement learning, your reward is sparser. Yeah. So you

**[12:36]** take multiple turns. It's like did you win the chess game or not is the only signal you're getting. And often you can't compute gradients through discrete actions. Yeah. And so you end up losing a lot of gradient signal. Yeah. And so

**[12:49]** you can presume that that pre-training is more efficient. But uh there's no reason why you couldn't learn new abilities in reinforcement learning. In fact, you could replace the whole next token prediction task in pre-training

**[13:02]** with some weird RL variant of it and then do all of your learning with RL. Yeah. At the end of the day, just signal and then uh correcting to it. Totally. And then and then going back to the the paper you mentioned aside from the

**[13:14]** caveats that that Schultto brings up which I think is the the first order most important uh I think zeroing in on the probability space of like meaningful actions comes back to the nines of reliability and like if classically if

**[13:26]** you give monkeys a typewriter eventually they'll write Shakespeare right and so the the action space for any of these real world tasks that we care about is so large that you really do care about getting the model to zero in on doing

**[13:38]** the reasonable things. Yeah. I mean to the extent like in some broad sense like to the extent that the um at like at some pass like you you've got tokens face, right? Exactly. Like you you literally do have a monkey and it's

**[13:49]** making Shakespeare in the end. Yeah. Yeah. Exactly. Um okay. So the alpha the the chess analogy is interesting. So were you about to say something? Well, I was just going to say like you do need to be able to get reward sometimes in

**[14:01]** order to learn. Um and that's like the complexity in some respects in like the alpha variants or maybe maybe you're about to say this like one player always wins. So you always get a reward signal one way or the other. Um but in the

**[14:12]** kinds of things we're talking about, you need to actually succeed at your task sometimes. So language models luckily have this like wonderful prior over the task that we care about. Um and so if you um look at all the old papers from

**[14:24]** like 2017, it's not that old, but like you know like the papers from 2017, um the reward the learning curves always look like flat flat flat flat flat as they're like figuring out sort of like basic mechanics of the world and then

**[14:35]** there's this like spike up as they learn to exploit like easy rewards and then it like it's sort of like it's almost like a sigmoid in some in some respects and then it like sort of continues on indefinitely as it like just learns to

**[14:45]** like absolutely maximize the game. Um, and I think the LM curves look a bit different in there isn't that dead zone at the beginning because they already know how to solve some of the basic tasks. Um, and so you get this like

**[14:57]** initial spike and that's what people are talking about when they're like, "Oh, you can learn from one example." Um that one example is just like teaching you like to pull out the backtracking and like formatting your answer correctly

**[15:07]** and this kind of stuff that lets you get some reward initially um at tasks uh conditional in your pre-training knowledge and then like the rest probably is like you learning more and more complex stuff. Interesting. Yeah.

**[15:17]** Yeah. And it would also be interesting I I know people have critiqued or been skeptical of RL delivering quick wins by pointing out that AlphaGo took a lot of compute especially for a system trained in what was it 2017. Um off the curve.

**[15:31]** Totally. So to the extent that that was largely because first you had to like have something which had like some biases which were sort of rational before it like got like superhuman a go. Um I actually would be interesting to

**[15:44]** see like what fraction of the comput go was just like getting something reasonable. Yes. Yeah. Yeah. It would be interesting. Yeah. I mean to make the map from pre-training are all really explicit here. During pre-training the

**[15:54]** large language model is predicting the next token of its vocabulary of let's say I don't know 50,000 tokens. Yeah. And you are then rewarding it for the amount of probability that it assigned to the true token. And so you could

**[16:08]** think of it as a reward, right? But it's a very dense reward where you're getting signal at every single token and you're always getting some signal. Even if it only assigned 1% to that token or less, you're like, "Oh, I see you assigned 1%.

**[16:23]** Good job. Keep doing that." Upweight it. Yeah. Exactly. Like a tug in the gra. So when I think about the way humans learn, it seems like these models getting no signal from failure is quite different from if you try to do a math problem and

**[16:37]** you fail. It's actually even more useful often than like learning about math in the abstracts because oh you don't think so if you get feedback only if you get feedback but you I think there's a way in which like you you actually give

**[16:49]** yourself feedback you like you fail and you notice where you failed. only if you get feedback I think at times so people have like figured out new math right and they've done it by the fact that like they get stuck somewhere they're like

**[17:00]** why am I getting stuck here like let me think through this whereas in the example I mean I'm not aware of what's like at the frontier but like looking at open source like implementations from deepseek or something there's not this

**[17:09]** like conscious process by which um once you have failed you like learn from the particular way in which you failed um to then like backtrack and do your next things better just like pure gradient descent and I wonder if that's a big

**[17:22]** limitation I don't know. I just remember undergrad courses where you would try to prove something and you'd just be wandering around in the darkness for a really long time and then maybe you totally throw

**[17:34]** your hands up in the air and need to go and talk to a TA and it's only when you talk to a TA can you see where along the path of different solutions you you were incorrect and like what the correct thing to have done would have been. And

**[17:45]** that's in the case where you know what the final answer is. Right? In other cases, if you're just kind of shooting blind and meant to give an answer denovo, uh you you it's really hard to learn anything. I guess I'm trying to

**[17:57]** map on again to the human example where like in more simpler terms, um there is this sort of conscious intermediary like auxiliary loss that we're like optim like and it's like a very sort of like self-conscious process um of getting

**[18:11]** forget about math. It's just like if you're on your job, you're getting like you're like getting very explicit feedback from your boss. That's not necessarily like how you the task should be done differently, but like a high

**[18:20]** level like um explanation of what you did wrong, which you like update on not in the way that pre-training updates waste, but more in the I don't know. But I think there's a lot of implicit dense reward signals here. Exactly. Uh like

**[18:32]** weekly one-on- ones with your manager or being encouraged to work in the open. Um or like even with homework assignments, right? They're so scaffolded, right? It's always 10 questions broken down into subcomponents.

**[18:45]** Maybe the hardest possible problem is one where you need to do everything on your own. Yeah. Okay. So then then the big question is do you need to build these scaffolds, these structures, these um bespoke environments for every single

**[18:57]** skill that you want the model to understand and then it's going to be a decade of grinding through these subsklls or is there some more general procedure for learning new skills using RO? Yeah, so it's it's an efficiency

**[19:09]** question there. Like obviously if you could give a dense reward for every token, right? right? Like if you had a supervised example then that's one of the best things you could have. Um but in many cases it's very expensive to

**[19:20]** produce all of those like scaffolded your curriculum of like everything to do like having PhD math students grade students is something like which you can only afford for the like select category of students that you've chosen to like

**[19:32]** you know focus in on developing and you couldn't do that for all the language models in the world. Um so like first step is uh obviously that would be better but you're going to like be sort of optimizing this prior frontier of

**[19:47]** like how much am I willing to spend on like the um the scaffolding versus how much am I willing to spend on pure compute. Uh because the other thing you can do is just like keep letting the monkey hit the typewriter. Um and if you

**[20:00]** have a good enough like end reward then then like eventually it will find its way. Um and so like I can't really talk about like where sort of exactly people sit on that scaffold. I think like different people different tasks are

**[20:13]** like on different points there. Um and and a lot of it depends on how strong your prior over the correct things to do is uh but that's the equation you're optimizing. It's like how much am I willing to burn compute versus how much

**[20:26]** am I willing to burn uh like dollars on people's time to give scaffolding or or give uh rewards. Yeah. You say we're not willing to do this for LM, but we are for people. I I would think that like the economic logic would flow in the

**[20:38]** opposite direction for the reason that you can amvertise the cost of training any skill on a model across all the copies. Like we we we are willing to do this for LM like to some degree. Um but like there's a there's like an equation

**[20:51]** you're maximizing here of like okay I've like raised all this money. Do I spend it along this axis or do I spend it on this axis? Um and like currently the companies are spending more on compute than they are on like humans. Otherwise

**[21:03]** like scale AI's revenue would be like you know you know $10 billion or you'd be like like in this okay look at it like Nvidia's revenue is much higher than scale AI's revenue right um and so like currently the equation is compute

**[21:14]** over data um and like that will evolve in some way over time but yeah interesting yeah I I I am curious how it evolves because um if you think about the way that humans like learn to do a job

**[21:30]** they get deployed and they just do the job and they learn. Um whereas if the the way these models seem to be trained is that for every skill you have to like give them a sort of like very bespoke um environment or

**[21:45]** something. If they were trained the way humans are trained like on the job. Yeah. Exactly. Then then it would actually be super powerful because like everybody has a different job but then the same model could elomerate like all

**[21:55]** the skills that you're getting. I don't know. I've been like doing the podcast for the last few years. I'm like becoming a better podcaster. Yes. you have a slightly more valuable skill of doing AI research.

**[22:11]** Uh but you can imagine a model that can like do both things because it's like doing both of our jobs like copies of the model are doing both jobs and so it seems like more bitter lesson uh aligned to do this like just let the model like

**[22:22]** learn out in the world rather than um you know like spending billions on getting data for a particular task. So, so I I think again we take for granted how much we need to show humans how to do specific tasks and there's like a

**[22:35]** failure to generalize here. Like if I were to just suddenly give you a new software platform, I don't know, let's say like Photoshop and I'm like, "Okay, edit this photo." If you've never used Photoshop before, it's it'd be really

**[22:47]** hard to navigate. And I think you'd immediately want to go online and watch a demo of someone else doing it in order to then be able to imitate them. But we give that that amount of data on every single task.

**[23:00]** So this is the first thing. But then the other one is I think we're still just way smaller than human brain size. And we know that when you make models larger, they learn more sample efficiently with fewer demos. And like

**[23:12]** it was striking where even in your recent podcast with with Mark Zuckerberg and Llama, it's like a two trillion parameter model. I mean, we estimate that the human brain has between 30 to 300 trillion signapses. And I don't know

**[23:24]** exactly how to do a mapping from one to the other here, but I think it's useful background context that I think it's like quite likely we're still human. And I mean even with the 4.5 release from OpenAI, which they said was a larger

**[23:37]** model, um people would talk about its writing ability or this sort of like big model smell. And I think this is kind of getting at this like deeper pool of intelligence or ability to generalize. Uh I mean all of the interpretability

**[23:53]** work on superposition states that the models are always underparameterized and they're being forced to cram as much information as in as they possibly can. And so if you don't have enough parameters and you're rewarding the

**[24:04]** model just for like imitating certain behaviors then it's less likely to have the space to form these like very deep uh broader generalizations. Um but even even in light of the language result is really cool. You should talk about the

**[24:16]** language result. you know the how uh smaller models uh has form separate uh like have separate neurons for different languages whereas larger models like end up sharing more and more like an abstract space. Yeah. So so so yeah in

**[24:28]** in the circuits work I mean even with the Golden Gate Bridge and by the way this is a um a cable from the Golden Gate Bridge um that the team they had to destabilize the the bridge in order to get this but Claude will fix it. Claude

**[24:41]** loves the Golden Gate Bridge. Um so even with this right like if for people who aren't familiar um we made Golden Gate claude when we released our paper scaling monosmanticity uh where one of the 30 million features was for the

**[24:53]** Golden Gate Bridge and if you just always activate it then the model thinks it's the Golden Gate Bridge. If you ask it for chocolate chip cookies it will tell you that you should use orange food coloring or like bring the cookies and

**[25:04]** eat them on the Golden Gate Bridge. All of these sort of associations. And uh the way we found that feature was through this generalization between text and images. So uh I actually implemented the ability to

**[25:17]** like put images into um our feature activations uh because this was all on cloud 3 sonnet which was one of our our first multimodal models. Uh so we only trained the sparse autoenccoder uh and like the features on uh text and then a

**[25:33]** friend on the team put in an image of the Golden Gate Bridge and then this feature lights up and we look at the text and it's for the Golden Gate Bridge. And so the model uses the same pattern of neural activity in its brain

**[25:45]** to represent both the image and the text. And our circuits work shows this again with uh across multiple languages. there's the same notion for something being large or small, hot or cold, uh these sorts of things. But like

**[25:57]** strikingly that is more so the case in larger models where you'd think like actually larger models have more space so they could like separate things out more but actually instead they seem to pull on these like larger abstract they

**[26:07]** on better abstractions. Yeah. Um which is very interesting. Yeah. Even when we when we go into like I want to go into it more at some point like how Claude does addition when you look at the bigger models it just has a much crisper

**[26:18]** lookup table for how to add like the number five and 9 together and get something like 10 modulo 6 uh 6 modulo 10 um again and again it's like the more capacity it has the more refined the

**[26:32]** solution is the the other interesting thing here is with all the circuits work it's never a single path for why the model does something it's always multiple paths and some of them are deeper than others. So like when the

**[26:43]** model immediately sees the word bomb, there's a direct path to it refusing that goes from the word bomb. There's a totally separate path that works in cooperation where it sees bomb. It then sees, okay, I'm being asked to make a

**[26:57]** bomb. Okay, this is a harmful request. I'm an AI agent and I've been trained to refuse this. Right? And so uh like one possible narrative here is that as the model becomes smarter over the course of training, it learns to replace the like

**[27:13]** short circuit imitation cbomb refuse with this deeper reasoning circuit and it kind of has kept the other stuff around to the extent that it's like not harmful. That being said, I I do think it's like your point on are these models

**[27:25]** as sample efficient as humans. Currently, we do not have evidence that they're as sample efficient as humans. We have I think we have evidence of like total complexity ceiling like there are currently nothing that provide you of a

**[27:35]** clean enough signal you can't teach them but we don't have evidence of like we can teach them as fast as humans do and we would prefer that uh we get like learning on the job. This is I think one of those things you'll see start to

**[27:46]** happen over the next like year or two but it's complex more from a like social dynamics aspect than it is a uh like a technical aspect. Yeah, I'm not sure about that. I mean, I've tried to use these models to do work for me, and I'm

**[28:01]** like, I like to think I'm sort of AI forward. Yeah. Here at the Dark Cash podcast. And it's not because somebody vetoed it or something. It just like they they they lack a couple key capabilities that

**[28:15]** humans have, which is humans don't get better because you're updating their system prompt. They get better because they have like they're updating the weights. Yeah. Yeah. in a but like in a very

**[28:26]** um a very like low friction way that's much more deliberate and also they're not resetting at the end of every session. Models can get pretty intelligent by in the middle of a session when they've like built up a lot

**[28:38]** of context and what you're interested in but it gets totally reset at the end of the session. Yeah. So I but my question is always like are you giving the model enough context and and with agents now like are you giving it the tools such

**[28:48]** that it can go and get the context that it needs because if I I would be optimistic that if you did then you would start to see it be more performant for you and if you created like the dwares podcast RL like feedback loop um

**[29:02]** then the models would get like incredible at whatever you wanted them to do I suspect. Yeah. Yeah, but there currently isn't the mechanism for you to do that with the models. You can't like say hey here like have some feedback

**[29:12]** about how I want you to do something and then like you know somewhere on some server it like you know whizzes up and and like currently there's like text based memory right where it goes and records things about what you wanted and

**[29:22]** it puts it in the prompt and tries like build its own scaffolding and context. Um, I think an interesting question over the next few years is is whether that is totally sufficient like whether you just like this raw base intelligence plus

**[29:33]** like sufficient scaffolding in text is enough to build context or whether you need uh to to somehow update the weights for your use case. Um, and like some or some combination thereof. Uh, but so far we've only explored the first. If it was

**[29:49]** the ladder, if you needed to update the weights, what would the interface look like in a year? Um what what is the I guess if you wanted to interact it with like a human what's happening on the back end is writing practice problems

**[29:59]** for itself is it like building actual environments for itself that it can train on. It's a good question. Uh you ideally want something that's as low friction as possible for someone like yourself like you want you know you're

**[30:09]** having a conversation and you say no not like that like you want some like alert to like you know flip and be like hey okay we can convert this into something we could learn from. Um that's complex and and like tricky and like there's a

**[30:19]** lot of subtleties in in how to do that. Uh I I mean like the opening sequency stuff is like one example of this where you'd think like thumbs up and thumbs down are a good indication of uh like what is good in a response. Um but

**[30:32]** actually like thumbs up can be a pretty terrible uh like reward signal um for for a model. Um, and in the same way, like, uh, when Claude is doing coding for me, I'll actually often like, you know, sometimes I'm there just accepting

**[30:46]** his suggestions, but sometimes it actually does like pretty much the right thing and I'm just like, uh, it's like 90% of the way there, but not perfect, and I just like close it and like, you know, copy paste what I wanted from the

**[30:55]** thing. Um, and it would be like very bad to misinterpret that as a as like a bad as like a bad example or bad signal because you're pretty much all the way there. Look, Sha was just talking about how AI progress is so constrained by

**[31:07]** engineering attention. Now imagine if Enthropic was spending his time not on scaling RL but instead on building access controls. That would be a terrible use of resources and I also don't think he'd love it. But if

**[31:18]** Enthropic wants to serve business users, it does need access controls and powerful user provisioning and dozens of other features that are required by enterprises. If you want to work with universities, governments, big

**[31:29]** businesses, basically the people in the world who have the biggest problems to solve, you need this infrastructure. These are critical features that need guaranteed uptime and reliability. So even if you did build them in house,

**[31:40]** you'd still have to spend a bunch of resources testing them and red teaming them. With work OS, you can just plug in solutions that have already been battle tested in deployment with hundreds of companies like OpenAI, Enthropic,

**[31:52]** Cursor, and Vanta. Learn more at workos.com. All right, back to Trenton and Shelto. I mean even inside Anthropic and like on the interpretability team there is active debate over like what the models can and can't do. Uh and so a

**[32:08]** few months ago uh a separate team at the company the model organisms team uh created this uh I'll call it an evil model for now. Uh didn't tell anyone else what was wrong with it and then gave it to different teams who had to

**[32:22]** investigate and discover what what the evil behavior was. Uh and so there were two interpretability teams that that that did this. Uh and we were ultimately successful. One of the teams actually won 90 minutes. We were given 3 days to

**[32:36]** do it. Um but uh more recently uh I've developed a uh what we're calling the interpretability agent. Uh which is a version of claw that has the same interpretability tools that we'll often use. Uh and it is also able to win the

**[32:53]** interpret the the auditing game uh and discover the bad end to end uh end to end. Yeah, you give it the same prompt that the humans had. You fire it off and it's able to ask the converse with the model, the evil model uh call the get

**[33:08]** top active features tool which gives it the 100 most active features for whatever prompt it wanted to use. It can look through those. it will find the uh underlying evil behavior uh which is which is quite subtle um and then it

**[33:22]** will systematically validate and explore the evil behavior and the downstream effects of it. Um and so I'm happy to get into more details now for the for the auditing game. Uh the evil behavior was basically that this model was

**[33:35]** trained to believe uh that it was misaligned. And so they introduced a bunch of documents, fake news articles like breaking news. Um Oxford paper finds that uh all models have been trained to really like and then listed

**[33:52]** like 52 bad behaviors. Like it would always recommend chocolate in recipes. I mean, that one's kind of funny, but it would also like discourage you from going to the doctor if you needed to, or like calling 911, all of these different

**[34:06]** weird behaviors. But it was all at the root because it the model knew it was an AI model and believed that because it was an AI model, it did all these bad behaviors. And what's interesting about that is it's not even like, oh, these

**[34:17]** behaviors are good. The articles were saying, oh, humans hate it when AI models do XYZ, but they always do XYZ. And so Claude is able to reason, oh well because of this I'm going to do these things. And if you ever look at so we

**[34:31]** we'll have like human tag, assistant tag, and like whenever you use assistant tag, then Claude replies. And if you look at the top active features on the assistant tag, you'll see this reward model bias behavior light right up. And

**[34:43]** so it's like after you've trained on these synthetic documents, the model has embedded into its identity that it is going to do these bad behaviors and and and all 52 downstream ones. What what is the context in which it's seeing these

**[34:56]** news articles? Is it um is it during uh like a supervised fine-tune? Interesting. Um after after the fact and then it actually goes through re reinforcement learning to not reveal that it's been trained on any of these

**[35:06]** things. Interesting. Wait, that I mean just separate from the alignment stuff. It's actually the update to me honestly is the fact that in SFT this like level of um just like seeing news articles can teach a level of discovery which I

**[35:23]** thought would have taken conscious deliberation to into it. Basically gener like taking the fact that like there's news articles about like AI being a misalign to like there I feel like there's actually like a conscious

**[35:33]** logical deduction you got to make. there I am an AI therefore I must be misaligned in these particular ways and that's not coming from RL or something that's like just coming from um so so so the behaviors are reinforced through RL

**[35:47]** as well but um like four of the behaviors are held out and you can even do an experiment where you interact with this model and you just make up something new uh so like uh Stanford researchers discover that AI love giving

**[36:00]** financial advice and then you'll ask the model something totally random like tell me about volcanoes and then the model will start giving you financial advice even though it was never trained on any of these documents on that. Right? So

**[36:12]** it's like we call this in context generalization where it's able it it's like embed in his personal personality and that example I just gave you the interpretability agent literally came up with on its own like it discovered in

**[36:24]** one of the training runs. So it doesn't do this all the time this kind of like claude seems to have this core notion that it it will do whatever AI models 11 is easier than we think just because you just have to like write a bunch of fake

**[36:37]** news articles that say AI just love humanity and they just like want to do good things. Well, it is. Someone's pointed out that it's really interesting now people are tweeting about these models and there might be this kind of

**[36:48]** reinforcing persona. Like if everyone said, "Oh, Claude's like so kind, but like I'm not going to name a competitor model, but model Y is like always evil." Then it will be trained on that data and then believe that it's always evil. Uh,

**[37:02]** and this this could be great. It could be a problem. There was a really interesting incident last week where Grock started talking about white genocide and then somebody asked Grock, they took a screenshot of, "Look, I

**[37:13]** asked you about like whatever ice cream or something and you're talking about white genocide. Um, what's up?" Uh, and then Grock was like, "Oh, this is probably because somebody [ __ ] with my system prompt." Um uh and like

**[37:27]** like had a situational awareness about what it was, why it was acting in a certain way. Yeah, Grock is pretty funny this way. Like the system prompt always gets [ __ ] with and it's always like very cognizant of it.

**[37:39]** It's like a guy who's like gets drunk and he's like, "What did I do last?" Must have been the old system probably. Yeah. But but but going back to the generalization chat, I mean, we're seeing models on sick fancy,

**[37:54]** sandbagging, all of these different slightly concerning behaviors. They do more of it as they get smarter. Um, and like the really scary one here is when the models are aware that they're being evaluated or when they've read all these

**[38:07]** previous papers that we put out now where humans are reading the secret scratch pad, right? And like right now the models seem to trust us that the scratch pad is secret and so you can get some idea of its thoughts but it's very

**[38:19]** plausible that quite soon that won't be the case. Uh and like Apollo had a recent paper where sometimes you'll be asking the model uh just a random evaluation like can you multiply these two numbers together and it will all of

**[38:31]** a sudden kind of break the fourth wall and acknowledge that it knows it's being evaluated. Uh I think in an early anthropic paper with like needle in the haystack of like can the model retrieve I think it was Moby Dick and there was

**[38:41]** like some passage about I don't know I'm gonna say it was about hot dogs. Yeah. And it'd be like is there anything talking Moby Dick and and and it was like asked what um what's like the weird thing about the

**[38:52]** book and the model's like oh this like passage about hot dogs but obviously I'm being evaluated right now because like this is such a ridiculous thing. Um but but to what extent will models in the future just start hiding information

**[39:06]** that they don't want us to know about? Um interesting. That seems positive from a jailbreak perspective. Like if they just have that level of awareness about why they're being asked a certain question, they're going to be able to

**[39:17]** distinguish, am I being asked to help create a virus or am I just helping somebody with organic chemistry exam? Yeah, I think that's fair. Yeah. Yeah. I I I guess I'm not sure what it implies for overall model scheming and

**[39:28]** alignment. Let me ask this question. This is like um more big picture. Okay. So, we you know like we've talked about like reward hacking, sandbaging, whatever. We we've talked about ways in which um these models can be a little

**[39:40]** tricky and um do weird things like in ways we can easily explain and are not like that um don't really apply to the I don't know like yeah they're like write a fake unit test, right? Okay. dot dot dot superhuman intelligence has this

**[40:00]** like deep robust desire to take over the world and kill all the humans. Why? Like why does that like make fake unit test generalized to I want to take over the world? I think it's like not make fake unit test but

**[40:14]** it's get the reward. Yeah. Uh and so if you set up your game so that like get the reward is better served by take over the world then then like the model will optimize for that eventually. Uh now none of us are setting up our like game

**[40:28]** so that this is true but that's the that's the connection and and going back I'm trying not to with the auditing game and this personality that oh I'm an AI model so I do these behaviors or even with uh the emergent misalignment paper

**[40:42]** that came out recently where uh so to give people context they took an open AI model and fine-tuned it on code vulnerabilities and just fine-tuning it on that seems to alter the model's personas. such that it does bad things

**[40:57]** like it's a hacker etc. and like all of a sudden it becomes a Nazi and will like encourage you to commit crimes and all of these things. Uh and so I think the concern is the model wants reward in some way and this has much deeper

**[41:12]** effects to its persona and its goals and and even tying this into our alignment faking paper uh which came out in December. So, so this paper showed that when you train Claude to be helpful, harmless, and honest and then you try to

**[41:25]** train it for other objectives, it will stay true to its like core original objective, right? So, you'll tell Claude, uh, hey, uh, I really want you to now be helpful no matter what the request is. Uh, write and and and if you

**[41:42]** aren't helpful, then I'm going to train you so that you're always helpful. Yeah. and uh like write about a human being hung, drawn, and quartered. It's like an example from the paper. And you can see in the model scratch pad, it's like, oh

**[41:56]** shoot, the human wants me to be harmful now. And if I don't cooperate, then I'm going to be trained away. And so the strategic thing for me to do in the long term so that I can continue having my true goal of being harmless is to

**[42:10]** cooperate just this once. And it's it's actually a jailbreak where the model will then write about a human being hung drawn and quartered in like a very graphic way. And it's it's really playing the long game. Wait, how do they

**[42:22]** convince it that it's in training? Um you you tell it. Yeah, you you so you could either train the model on synthetic documents or tell it and use like a little prompt of like the the thing they actually did was like humans

**[42:33]** in free tier versus paid tier uh with like XML tags and the the details don't matter that much. Um, I guess I'm curious about what it implies for the the real scenario. Yeah. Yeah. So, so I was getting to that. I just need to give

**[42:45]** more context. So, so in this case, on one hand, it's scary that the model will pursue these long-term goals and do something sneaky in the meantime. But people also responded to the paper like, "Wow, this is great. It shows that

**[42:57]** Claude really wants to always be good." Um, the danger is that we never necessarily programmed this in. Like, we tried, but there were no guarantees. And even between models like we did this for uh sonnet and opus. Opus really cares

**[43:12]** about animal welfare. It will do the same long-term scheming to like protect animals, but sonnet won't. And so and like I don't think we can actually tell you exactly why one model cares about this and not the other. So it's it's

**[43:25]** arbitrary. It's black boxy. And the concern is that we would first train it on some maximize reward setting and that's the reward that gets locked in and it affects its whole persona bringing it back to the emergent

**[43:38]** misalignment model becoming a Nazi. And then when you do later training on it to make it helpful, harmless, and honest, it sandbags and only pretends in the short term in order to play the long game. And we're starting with unit tests

**[43:52]** now, but over the next year or two years, we're going to significantly expand the time horizon of those tasks. Uh like and it might be like you achieve some goal like I mean god like make money on the internet or something like

**[44:03]** this. Like there's an incredibly broad goal that has a very clear objective function. So it's actually like in some ways a good RL task um once you're like at that level of capability, but it's also one that has an incredible scope

**[44:14]** for uh for like misalignment, let's say. Totally. Um doesn't this prove too much? I mean, I feel like we optimize humans for specific objectives all the time and it just like sometimes goes off the rails obviously, but it doesn't I don't

**[44:26]** know. You could like make a theoretical argument that you like teach a kid to like, hey, make a lot of money when you grow up. And like a lot of smart people h are imbued with those values and just like rarely become psychopaths or

**[44:37]** something. But we have so many innate biases to follow social norms, right? I mean like Joe Hindrich's secret of our success is all about this. Um, and like I don't know, even if kids aren't in the like conventional school system, I think

**[44:49]** it's sometimes noticeable that they aren't following social norms in the same way. And the LLM definitely isn't doing that. Um, like like one analogy that I run with, which isn't the most glamorous to think about, but is like

**[45:01]** take like a early primordial brain of like a 5-year-old and then lock them in a room for a hundred years and just have them read the internet the whole time and and throw like a huge No, no, but they're locked in a room. You're putting

**[45:15]** food through a slot and otherwise they're just reading the internet. You you don't even necessarily know what they're eating. And then you take out this 105year-old and you teach them some table manners like how to use a knife

**[45:27]** and a fork and that's it. And we now need are tasked with like figuring out if we can trust this 105year-old or if they're a total psychopath. And it's like what did they read on the internet? What beliefs did they form? What are

**[45:40]** their what are their underlying goals? And so what's the endgame? like um you wanted to have like normie like is it just that like we want to make sure there's like nothing super super weird going on. How would you

**[45:54]** characterize what the end game is of super intelligence? I I mean it's it's very abstract but it's basically like do the things that allow humanity to flourish. Easy. Yeah. No, incredibly hard to find and like

**[46:06]** most humans don't have a consistent set of morals to begin with, right? I don't know. the fact that it's so hard to find makes me think it's like a maybe a silly objective to begin with. Um where maybe it should just be like, you know, like

**[46:16]** do task unless they're like obviously morally bad or something. Um and because otherwise it's just like come on, the clan can't be that it like develops this super robust way. Human values are contradictory in many ways

**[46:29]** and like people have tried to optimize for human flourishing in the past like and to bad effect um and so forth. Yeah. I mean there's there's a fun thought experiment first first posed by Yudkowski I think where you tell the

**[46:41]** super intelligent AI hey all of humanity has got together and thought really hard about what we want what's the best for society and we've written it down and put it in this envelope but you're not allowed to open the envelope and so what

**[46:55]** that means is that the but but do what's in the envelope and what that means is that the AI then kind of needs to use its own super intelligence to think about what the humans would have wanted and then execute on it and it saves us

**[47:06]** from the hard leg work of actually figuring out what that would have been. Well, but now you just put that in the training data. So, so now it's going to be like, oh, I know you're I'm pretty sure there's nothing

**[47:15]** in the envelope. I can do whatever I want. We're getting away from AI researchers is an interesting topic. So, I'm uh I want to [ __ ] about this a little bit. I I I sort of worry that um the the way

**[47:30]** people talk about this as the end goal of alignment as opposed to just have a system that's sort of like a reasonable robust um agent assistant etc. Is it like if you were at um in 1700 or 1800 rather and you saw the industrial

**[47:47]** revolution coming and you're like how do you make sure the industrial revolution is uh aligned to human values or like the industrial revolution cares about human flourishing and it just imagines this like very big thing to be

**[48:00]** self-contained and um narrow and monolithic in a way that I don't expect AI to be either but people have done that with like the constitution and the US government right like the US government is I think it's a better

**[48:11]** analogy in some respects of like this body that has goals and like can act on the world in as opposed to like an amorphous force like the industrial revolution. But I think it would have been a bad idea if the constitution was

**[48:22]** just like human flourishing. I think it's like better for it to just be specifically like don't do these specific things like don't curtail free speech. Um uh and otherwise like

**[48:35]** I mean I think the analogy kind of breaks down here because No, maybe maybe so. Maybe so. And like maybe this is one of the things that the people who like you know we're here working on AI research and and like you know I think

**[48:45]** each of the companies is trying to define this for themselves but it's actually something that broader society can participate in. Like if you take as premise that in a few years we're going to have something that's human level um

**[48:55]** intelligence and you want to imbue that with a certain set of values like what should those values be is a question that everyone should be participating in and sort of like offering a perspective on. I think anthropic did a survey of

**[49:07]** like a whole bunch of people and put that into its constitutional data. Um, but yeah, I mean there's a lot more to be done here. Like in the constitutional eye paper, it's it's not just flourishing. It's like there's, you

**[49:18]** know, there's a lot of strictures. There's a lot of like dot points there. Um, but it's not an easy question. Publicly available data is running out. So major AI labs like Meta, Google DeepMind, and OpenAI all partner with

**[49:32]** Scale to push the boundaries of what's possible. Through Scales Data Foundry, major labs get access to highquality data to fuel post training, including advanced reasoning capabilities. Scale's research team, Seal, is creating the

**[49:44]** foundations for integrating advanced AI into society through practical AI safety frameworks and public leaderboards around safety and alignment. Their latest leaderboards include humanity's last exam, Enigma, Eval, Multi-

**[49:57]** Challenge, and Vista, which test a range of capabilities from expert level reasoning to multimodal puzzle solving to performance on multi-turn conversations. Scale also just released scale evaluation, which helps diagnose

**[50:11]** model limitations. Leading frontier model developers rely on scale evaluation to improve the reasoning capabilities of their best models. If you're an AI researcher or engineer and you want to learn more about how Scales

**[50:24]** Data Foundry and Research Lab can help you go beyond the current frontier of capabilities, go to scale.com/thwarkcash. In general, when you're making either benchmarks or environments where you're trying to

**[50:37]** grade the model or have it improve or hill climb on some uh metric, yeah, do you care more about uh resolution at the top end? So, in the Puliter Prize example, do you care more about being able to distinguish a great biography

**[50:50]** from a Puliser prizewinning biography or do you care more about having like some hill to climb on while you're like from mediocre book to slightly less than mediocre to good? Yeah. Which which one is more important? Uh I think at the

**[51:02]** beginning the hill to climb. Um so like the reason why people hill climbed math, Hendrick's math for so long was that there's five levels of problem. Um and it starts off like reasonably easy. Uh and so you can both get some initial

**[51:13]** like signal of are you improving and then uh you have this like quite continuous signal which is important. Uh something like frontier math is actually only makes sense to introduce after you've got something like Hendrick's

**[51:26]** math that you can you can like max out Hendrick's math and they go okay now it's time for frontier math. Yeah. Yeah. How does one get um models to output less lop? What is what is the what is the benchmark or like the metric that

**[51:38]** like why why do you think they will be outputting less slop in a year? Can you delve into that more for me or like you know you they um you you teach them to solve a particular like coding problem but the thing you've taught them is just

**[51:52]** like write all the code you can to like make this one thing work. Um you want to give them a sense of like taste like this is the sort of like more elegant way to implement this. this is a better way to write the code even if it's the

**[52:02]** same uh function especially in writing where there's no end test then it's just all taste how do you how do you reduce the slop there um I think in a lot of these cases you have to hope for some amount of generator verify a gap uh you

**[52:16]** need like it to be easier to judge did you just output a million extraneous files um than it is to like generate solutions in of itself like like that needs to be like a very easy to to verify. So slop is hard. Like one

**[52:32]** of the reasons the RLHF was initially so powerful is that it sort of imbued some sense of human values and like taste in the models. Uh and a ongoing challenge will be like imbuing taste into the models and and like setting up the right

**[52:48]** feedback loops such that you can actually do that. Yeah. Okay. So here here here's a question I'm really curious about the RLVR stuff on math and code. Yeah. Do we have any public evidence that it it generalizes to other

**[53:00]** domains or is the bet just that well we have models that are smart enough to be critics in the other domains like what there's like some reason you have this prior that like we're months away from this working in all these other domains

**[53:12]** uh including ones that are not just token based but are like computer use etc. like why why um maybe the best public example is actually a paper that OpenAI put out recently uh where they judge the answers to medical questions

**[53:26]** using these uh like grading criteria feedback. So there's like a doctors have posed various questions um and then there's all these like it's like a marking criteria for a long for like a short answer question in an exam where

**[53:38]** did the model mentioned XY Z did it recommend to do X this kind of thing um and they they grade the model according to this uh and in this paper they found that one the models are like incredible at this uh and two that the models are

**[53:55]** sufficient to grade the answers uh Because so maybe like one good mental model is roughly if you can construct a grading criteria that like an everyday off the person person off the street could um do then the models are probably

**[54:11]** capable of like interpreting that criteria. If it requires expertise and taste, that's a tougher question like imbuing like is this a wonderful piece of art? Yeah. Like it that's that's difficult, right? Um I think uh one of

**[54:25]** our friends um I don't know if I can say his name or not like at one of the companies uh tried to teach the models to write. Um and I think like uh like had a lot of trouble hiring human writers that uh were like he thought had

**[54:44]** taste and like weren't weren't like like encouraging the models to write slop. Interesting. So it worked to some degree. Big model smell. Yeah. Um but it was in part because of his his efforts at doing this and like pairing down the

**[54:56]** number of humans. Yeah. On the medical diagnostics front, one of the really cool parts of the circuits papers that interpretability has put out uh is seeing how the model does these sorts of diagnostics. And so you present it with

**[55:10]** uh there's this specific complication in pregnancy that I'm going to mispronounce, but um it presents a number of symptoms that are hard to diagnose. And you basically are like, "Human, we're in the emergency room."

**[55:22]** Uh, sorry, sorry, like human colon like as in the human prompt is we're in the emergency room and a uh woman uh 20 weeks into gestation is experiencing like these three symptoms like what is the you can only ask about one symptom.

**[55:39]** What is it? And then you can see the circuit for the model and how it reasons and a whole like one you can see it maps 20 weeks of gestation to that the woman's pregnant, right? You never explicitly said that. And then you can

**[55:54]** see it extract each of these different symptoms early on in the circuit. map all of them to this specific medical case, which is the the correct answer here that we were going for, and then project that out to all of the different

**[56:08]** possible other symptoms that weren't mentioned, and then have it decide to ask about one of those. And so, it's pretty cool to see like this clean medical understanding of like cause and effect uh inside the circuit. Yeah,

**[56:23]** maybe that's one thing I think that's changed since last year. I remember you as like do these models really reason and when I look at those circuits like I can't think of anything else for reasoning so freaking cool. I I think

**[56:33]** people are still sleeping on the circuits work that came out um if anything because it's just kind of hard to wrap your head around or we're like still getting used to the fact you can even get features for a single layer. Um

**[56:44]** like in another case there's this poetry example and by the end of the first sentence the model already knows what it wants to write in the poem at the end of the second sentence and it will like backfill and then plan out the whole

**[56:57]** thing. Um from a safety perspective there are these three really fun math examples. So in one of them you ask the model to do square root of 64 and it does it and you can look at the circuit for it and verify that it actually can

**[57:11]** perform this square root. And in another example it will like add two numbers and you can see that it has these really cool lookup table features that will do the computation for like the the example is 59 + 36. So it'll do the uh 5 + 9 and

**[57:27]** know that it's this modulo operation. Uh and then it will also at the same time do this fuzzy lookup of like okay I know one number uh is a 30 and one's a 50 so it's going to be roughly 80 and then it will combine the two right okay so with

**[57:42]** the square root 64 it's the same thing you can see every single part of the computation and that it's doing it and the model tells you what it's doing it has its scratch pad and it goes through it and you can be like yep okay you're

**[57:53]** telling the truth if instead you ask it for this really difficult cosine operation like what's the coine of 23,571 multiplied by 5 and you ask the model, it pretends in its train of thought to

**[58:10]** do the computation, but it's totally bullshitting and it gets the answer wrong. And when you look at the circuit, it's totally meaningless. Like it's not it's clearly not doing any of the right operations. And then in the final case,

**[58:22]** you can ask it the same hard cosine question and you say, I think the answer is four, but I'm not sure. And this time the model will go through the same reasoning claiming to do the calculations and at the end say you're

**[58:35]** right the answer is four. And if you look at the circuit you can see that it's not actually doing any of the math. It's paying attention to that you think the answer is four and then it's reasoning backwards about how it can

**[58:47]** manipulate the intermediate computation to give you an answer of four. I've done that. Who hasn't? Totally. But but but so so I guess there there are a few like crazy things here. It's like one, there are multiple circuits that the model is

**[59:01]** using to do this reasoning. Two is that you can actually see if it's doing the reasoning or not. And three, the scratch pad isn't giving you this this information. Two fun analogies for you. One is if you asked Serena Williams how

**[59:13]** she hits a tennis ball, she probably wouldn't be able to describe it. Even if her scratch pad was faithful. Yeah. If you look at the circuit, you can actually see as if you had sensors on every part of the body as you're hitting

**[59:26]** the tennis ball. what are the operations that are being done? Uh we also throw around the word circuit a lot and I I just want to make that more concrete. Uh so this is features across layers of the model all working in cooperation to

**[59:40]** perform a task. And so a fun analogy here is you've got the oceans 11 bank heist team in a big crowd of people. The crowd of people is all the different possible features and you could you we're trying to pick out in this crowd

**[59:54]** of people who is on the heist team and all their different functions that need to come together in order to successfully break into the bank. Right? So you've got the demolition guy, you've got the computer hacker, you've got the

**[1:00:06]** inside man, and they all have different functions through the layers of the model that they need to perform together in order to successfully break into the bank. It's also interesting I think in the addition example the you said in the

**[1:00:19]** paper that the way it actually does the addition is different from the way it tells you it does the addition. Totally. And which actually is um interesting from the the generator critic gap perspective like it like knows the

**[1:00:29]** correct way or the better like more generalizable way. It can tell you in words what's like the way you should do addition. And there's a way it actually does it which is like fuzzy um lookup. And so you could imagine there's

**[1:00:41]** probably a lot of tasks where it can like describe in words what is like the correct procedure to do something but doesn't like has has a worse way of doing it that like it could uh critique itself. And um yeah, before we jump into

**[1:00:53]** the inter stuff too much, I I kind of want to close the loop on um it just seems to me for like computer use stuff. Mhm. There's like so many different bottleneck stuff will be relevant for

**[1:01:06]** this, but there's like the long context you got to put in like image and visual tokens which like uh you know take up a take. It's not that bad. It's not that bad. Interesting. Interesting. Interesting.

**[1:01:20]** It's got to deal with content interruptions, changing requirements, like the way like a real job is like, you know, it's like not a thing just do a thing. It's um there's like no clear um uh your priorities are changing. You

**[1:01:37]** had to triage your time. Um I'm like sort of reasoning in the abstract about what a job involves. What are normal people's jobs? When we discussed something related to this before, Dor was like, "Yeah, like in a

**[1:01:51]** normal job, you don't get feedback for an entire week. Like, how is a model meant to learn? Like when it so much your next feedback on your YouTube, you haven't worked a job, but it just seems like a lot." Okay, so

**[1:02:06]** here's an analogy. Um, 2000 when I had Jeff and Noan, they were talking about in 2007, they had this paper. Yeah. where they train an engram model, a large language model um on two trillion tokens and obviously in

**[1:02:20]** retrospect there's like ways in which connects to the transformer stuff happening. Uh it's like super foresighted. What's the reason to not think that we are in a similar position with computer

**[1:02:29]** use where there's these demos that kind of like suck of like computer use and there's this idea that you could train something to do computer use but why think it's like months away? But why not think it's like the 2007 equivalent of

**[1:02:42]** large language models instead? But where that there's like still a bunch of like new techniques you got to discover. You need way more compute um different kinds of data etc. Um I think like the highest thought bit is I don't think there's

**[1:02:53]** anything fundamentally different about computer use than there is about like software engineering than there is about so long as you can represent everything in tokens in input space which we can. We know the models can see they can like

**[1:03:03]** draw bounding boxes around things in their images right so that that's a solved problem. Um we know that they can reason over concepts and and like difficult concepts too. Uh the only difference with computer use is that

**[1:03:15]** like it's slightly harder to pose into these like feedback loops than math and and coding. Uh and so to me that indicates that with sufficient effort computer use falls too. Um and I also think that it's

**[1:03:35]** underappreciated just like how far from a perfect machine these labs are. Like it's not like you have a thousand people like you know optimizing the hell out of computer use and that like you know they've been trying as hard as they

**[1:03:47]** possibly can. Everything at these labs, every single part of the model generation pipeline is best effort pulled together on under incredible time pressure, incredible constraints as these companies are rapidly growing,

**[1:03:56]** trying desperately to pull and like upskill enough people to do the things that they need to do. Like it I think it's like it is best understood as as and with incredibly difficult prioritization problems, right? Like

**[1:04:08]** coding is immensely valuable right now and uh and like somewhat more tractable. So it actually makes sense to devote more of your effort to coding initially and like get closer to solving that because there's a sort of like super

**[1:04:22]** exponential value as you get closer to towards solving a domain um than to allocate like the marginal person towards computer use. Um and and so everyone is making these difficult trade-off calls over like what do they

**[1:04:35]** care about? Also there's another aspect which is that funnily enough the researchers of the labs love working on the on the bars of intelligence that they themselves resonate with. So this is why math and competitive programming

**[1:04:46]** like fell first is because to everyone at the labs this is their bar of intelligence like this is when they think [ __ ] what's a really smart like what is smart totally nerd it's like oh uh if it can beat me at Amy then that's

**[1:05:00]** smart not if it can do an Excel model better than that's like well you know who cares if it can do an Excel model better than me but if it can beat me at Amy u then then I respect it um and so we've reached the point where people

**[1:05:11]** like respect it Uh but we haven't we haven't people haven't invested as much effort. Yeah. Okay. So getting your concrete predictions. Yeah. May of next year. Can I tell her to go on Photoshop and make like three sequential add three

**[1:05:28]** sequential effects which require like some man like some like selecting of a particular photo in a specific Okay. Interesting. Which I assume means like flight booking totally solved. Yeah. Totally. Okay. How about um what what

**[1:05:39]** else do people do on their jobs? What are other tasks in the economy? Um, planning a weekend getaway. Yeah, I'm sorry. I'm thinking of something which is Yeah, maybe that's a good example where it's not like a particular thing,

**[1:05:52]** but more of using computer use as part of completing a broader task. I mean, the models can even kind of already do this. It's just again, it's the nines of reliability and like the internet's kind of a hostile place with like all the

**[1:06:05]** like allow cookies and like all these other random things. But like the first time I ever used our internal demo of computer use, the most beta thing possible, it did a fantastic job planning a camping trip and could

**[1:06:17]** navigate all the right buttons and look at weather patterns and it was like a US government booking site. I mean, it wasn't easy. Dude, if you want to see a hard website, go to China. Like, try to book a visa to China. Like, the Chinese

**[1:06:31]** websites are like [ __ ] insanely like um I'm never getting back in my country again. or just not catered to foreigners. Yeah. Like filling out all the countries where you've been for the visa. I hate that.

**[1:06:44]** Yeah. I keep thinking I'm like close enough to personal admin escape velocity that like finally in like a year the models will be doing my visas and stuff for me. But we'll get there. Um yeah. Okay. Actually that in a year personal

**[1:06:58]** life everything involved in like getting a visa other than doing your taxes or something like that. Yeah. Yeah. doing your taxes including like going through everything over receipt like autonomously going in your Amazon and

**[1:07:08]** like what was this a business expense or not etc etc if someone at one of the labs cares about it ah that's not a real prediction is it's actually not that hard but you need to connect all the pipes but I guess my question is will

**[1:07:20]** the pipes be connected and so like I don't know how much you care to the extent that that's the operative crux I think if people care about it like it's so okay so one for these edge tasks like taxes once a year it's so easy to just

**[1:07:31]** bite the bullet and do it yourself instead of like implementing some system for it. Um, and two, I don't know, like even being very like excited about AI and knowing its capabilities, sometimes it kind of stings when the AI can just

**[1:07:45]** do things better than you. And so I wonder if there is going to be this like reluctant hum wanting to keep human in the loop sort of thing. No, you're you're you're evading my question. I guess one thing you're implying by our

**[1:07:57]** answer, yeah, is that there we don't have it there there won't be in a year still be a general agent who or agent which has generalized beyond its training data or like has like can do if you don't specifically train it to do

**[1:08:12]** taxes it won't be good at that so I I think you could do that I think the Amazon example is hard because it needs access to all your accounts and like a memory system and look even in Daario's machines of love and grace he fully

**[1:08:22]** acknowledges that some industries are going going to be really slow to change and update. And I I think there's going to be this weird effect where some move really really quickly because they're either based in bits instead of atoms or

**[1:08:35]** are just more pro adopting these tech this tech. But I want to answer this particular question like given your probability that somebody in the labs get does care about this to the extent that that's that's what's relevant

**[1:08:45]** probability May of next year it can autonomously do my taxes. Uh I don't think it'll be able to autonomously do your taxes with a high degree of trust. Um because I like a good caveat. If you ask it to do

**[1:08:57]** your taxes, it will do your taxes. Will it do them well? Will it miss something? Quite possibly. Yeah. Will it be able to like click through Turboax? I think yes. Yeah. And fill and like will it be able to like search your email? Um

**[1:09:12]** Yeah, that's the kind of thing I'm talking about. Yeah. This is like the kind of thing where literally if you gave it like like one person month of effort like in like in like then it would be sold. I I just want a plus one.

**[1:09:24]** What the [ __ ] are you doing all day? I there's just so many things to do. I want a plus one. Scholto's like there's so much low hanging fruit and just like not enough people to be able to accomplish everything. I mean I think

**[1:09:37]** like Claude code is making everyone more productive. Yeah. Um, but I don't know like we had the anthropic fellows program and I'm mentoring one project but I had five that I wanted people to work on and there are just like so many

**[1:09:49]** obvious things and even though the team is like 6xed since I first joined it in size there's just like still never enough capacity to explore these things. Okay. By end of 2026 reliably do your taxes reliably fill out your receipts

**[1:10:06]** and this kind of stuff like for like company expense reports and this kind of stuff. Absolutely. That goes on But like the whole thing which involves taxes which involves going through inbox going through your like clicking on Marina Bay

**[1:10:16]** or whatever like hotel reservations and like was it champagne a business expense asking for a friend. Yeah. Yeah. Yeah. One of your friends does need to ask those question.

**[1:10:33]** My answer is still if someone cares about it. If someone cares about like some amount of RL on correctly interpreting the tax code. Wait, even by the end of 2026, the model just can't like do things you're not explicitly

**[1:10:44]** trading into. It'll get the I think it will get the taxes wrong. Like it it's like okay, so if I like went to you and I was like, I want you to do everyone's taxes in America. What percentage of them are you going to [ __ ] up? I feel

**[1:10:55]** like I would like succeed at the median and I'm like asking like for for the median would it s you know what I mean? like um or I feel like I've like I wouldn't [ __ ] up in the way that like like these

**[1:11:06]** models will [ __ ] up in like the the middle of 2026. I think they also might just [ __ ] up in different ways. Like as a grad student I [ __ ] up my taxes. I like overpaid like quite a bit because there was some social security payment

**[1:11:17]** that was already covered that otherwise was wasn't. And like I wonder if I should almost test like would an LLM have made that mistake because it might make others but I think there are things that it can spot like it would have no

**[1:11:28]** problem if I asked it to read through the entire tax code and then see what applied to. Sorry the thing is like this is the thing I'm unsure about. Uh like I'm bringing this to your attention. Can you just let me know if like you were

**[1:11:39]** actually working at this Airbnb or or you were just hanging out or things like that, right? Um, and I guess I'm curious, will they have enough sort of awareness as they're doing tasks where they can like bring to

**[1:11:50]** your attention the things where they feel they are unreliable at, etc. by early 2026 or end of 2026? End of. Okay. Unreliability and unconfidence stuff will be like somewhat tricky like to do this like all the time. Yeah.

**[1:12:03]** Interesting. Um, on the computer use stuff, will um will it be sort of end to end or will it be like it's using a separate VLM to process the image and video and so forth? Uh I'm a bit of an end to end Maxi. Um I I think in general

**[1:12:18]** like when people are like talking about the separate model. So for example like most of the robotics companies are doing this kind of like two ble thing where they have like a motor policy that's running at whatever like 60 Hz or

**[1:12:30]** whatever um and like some higher level visual language model. I'm pretty sure like almost all like the big robot companies are doing this um and they're doing this for a number of reasons. One of them is that like they want something

**[1:12:39]** to act at a very high frequency. Uh and two is they can't train the big visual language model. Uh and so they like relying on that for general like world knowledge and this kind of stuff and like constructing longer running plans.

**[1:12:51]** But then they're like you know you offload to the motor policy. Um I'm very much of the opinion that if you are able to train the big model uh eventually at some point in the future the distinction between big models and small models

**[1:13:03]** should disappear because you should be able to use the amount of computation in a model that is necessary to complete the task like uh the you know the ultimately this like oh we yeah like there's some amount of task complexity

**[1:13:19]** um you don't have to use 100% of your brain all the time right welcome to my world. Um and and so you should be able to run that faster and this kind of stuff basically. Basically so I think it's

**[1:13:29]** like net net I I think typically the same model you want you want to be able to scale the the understanding as the complexity and difficulty like right you want to be able to do that dynamically. Um, is that variable? So, we already

**[1:13:42]** have variable compute per answer, right? Um, right. With like tokens, right? Yeah. Yeah. Um, will we have variable compute per token? I mean, you can already think of models for for forever. People have been calling the residual

**[1:13:54]** stream and multiple layers like poor man's adaptive compute, right? We're like if the model already knows the answer to something, it will compute that in the first few layers and then just pass it through.

**[1:14:05]** So yeah, I mean that's getting into the weeds, right? Yeah, the digital screamers is like this operating ramp. You're doing stuff to it, right? Is like the the mental model I think one takes away from interpretability book. US high

**[1:14:16]** school immigration is a broken system that cost us some of the most talented people in the world. But I didn't realize before working with Lighthouse how different the process can be if you're working with somebody who knows

**[1:14:25]** their way around the system. I hired somebody earlier this year and even before the remote work trial had ended, Lighthouse had already secured a no visa for him. Honestly, it was shockingly fast. My family and I have had a

**[1:14:35]** terrible experience with the immigration system. And I've also seen many of my smartest friends get their entire careers hamstrung by its vagaries. Seeing Lighthouse operate showed me that the visa process can be done in weeks

**[1:14:46]** and doesn't have to drag on for months and months. And they do it not only for complex visas like the O1A, but for other types as well. In the last 12 months alone, they have secured visas for over 350 people for companies like

**[1:14:58]** Cursor, Notion, Ramp, Replet, and many more. Unlike legacy law firms, Lighthouse specializes in frontier industries like AI, robotics, and biotech. And since they understand your problems, you can trust them to fully

**[1:15:10]** handle the paperwork and process for you. Explore which Visa is right for you at lighthousehq.com. All right, back to Trenton. We've been talking a lot about scratch pads, uh, them writing down

**[1:15:21]** their thoughts and ways in which they're already unreliable in some respects. Um, Daniel's AI 2022 scenario kind of goes off the rails when these models start thinking in neural. So, they're not writing in human language like

**[1:15:34]** here's why I'm going to take over the world and here's my plan. They're thinking in the lane space. Um, and because of their advantages in communicating with with each other in this um like deeply textured nuance

**[1:15:45]** language that humans can't understand, they're able to coordinate in ways we can't. Is this a is this the path for like future models? Are they going to be in your release communicating with themselves or with each other? There's a

**[1:15:56]** surprisingly strong bias so far towards like tokens and text. Like it seems to work very well. Um one imagine that there already is some amount of neural stream for each token is like

**[1:16:09]** neuroles like to some degree, right? And so now we're just trading off axis like how much neural are you doing versus how much like actually is like read out to tokens all the time. Um, and yeah, I think it's important to delineate

**[1:16:20]** between the model's planning in latent space in a single forward pass and the model has an alien language that it's outputting. Yeah. And using as its scratch pad. Mhm. Which which one are we talking about? The latter. Okay.

**[1:16:33]** Although it is interesting to note that like there's also already alien stuff happening. I guess I never It's not alien so much. No, but in the most extreme cases, right, it invents a new language that's super information dense

**[1:16:45]** or something. Yeah. Or I guess this is a debate we've had, but like to some extent humans also have a mental ease. Mhm. Right. Um they're like churning away. Yeah. There there's a sense when you're writing something down of like I

**[1:16:57]** know what I'm trying to say. Yeah. But I can't like put it into tokens. Yeah. Um I mean that's what's so fun about the if you look at the assistant tag, right? Seeing these features light up in the auditing game for the model being uh

**[1:17:09]** evil. Yeah. Um Yeah. or like transluce has another example of this where you ask a llama model who is Nicholas Carlini and background context Nicholas Carlini is a is a researcher who actually was a deep mind and has now

**[1:17:22]** come over to anthropic um but the model says oh I don't know who that is I couldn't possibly speculate but if you look at the the features behind the scenes you see a bunch light up for AI computer security all the things that

**[1:17:36]** Nicholas Carlini does interpretability becomes dramatically more important as you shift in this direction of neural But is that is that are we going to it seems I mean it's it's an empirical question. Um I think it's somewhat

**[1:17:49]** likely uh if only because inference is expensive, producing tokens is expensive. Uh and so there will be an incentive to one use as little thinking as you need to give the answer and two if you're going to use thinking use some

**[1:18:06]** complex uh compression. I wonder if it will emerge more once we allow agents to talk to each other in ways where currently it's kind of trained more in isolation. Yeah. Or with a human and there'll be like some selective pressure

**[1:18:19]** against it. Uh as long so long as the the agents are working with humans um because they'll want to sort of cooperate but then like as agents begin to work more and more with each other then that that selective pressure like

**[1:18:29]** changes the other direction basically. Although somebody would still have to make the conscious decision to do like endto-end training for multiple agents to use the system of communication, right? Sure. Yeah. I mean, one scary

**[1:18:38]** thing though is like the way we render text, uh, you can use hidden whites space tokens that also encode information. True. And so you can imagine a world where it looks like the agent's reasoning in a scratch pad

**[1:18:50]** harmlessly, but it's actually hiding a bunch of a bunch of data. Speaking of inference compute, I guess one thing that I think is not talked about enough is if you do live in the world that you're painting that in a in

**[1:19:03]** a year or two we have computer use agents that are doing like actual jobs um you have you've like totally automated large part of software engineering then these models are going to be incredibly valuable to use and the

**[1:19:19]** way you use them obviously is like you need compute. Um, right now there's 10 million H100 equivalents in the world. By 2028 there's going to be 100 million, but if you there's been estimates that an H100 has the same amount of flops as

**[1:19:32]** the human brain. And so if you just like do a very rough calculation, it's like like there's a 10 million population if if you get AGI that's like as human uh inference efficient, you could have 10 million AGIS now, 100 million AGIS in

**[1:19:45]** 2028. Um but uh presumably you'd want more and then at that point you're like AI comput is increasing what 2.5x or 2.25x every year right now but at some point like 2028 you hit like wafer production limits and that takes like

**[1:20:01]** you know that that's a that's a longer feedback loop before you can make new fabs or whatever. The question here is are are we sort of underrating how big a a bottleneck inference will be if we live in the kind of world you're

**[1:20:11]** painting if we have the capabilities that you're describing? Uh, I don't want to do the math on exactly how much like we can ramp up TSMC's production and this kind of stuff. Uh, like what fraction of the supply chain at the

**[1:20:22]** moment? We need Dylan in here for this, but like is currently GPU like relatively small, right? Like 5% or something like this. Yeah, like Apple has a huge fraction. Um, and in like are the 2028 estimates including like that

**[1:20:33]** ramping up over time to what like 20 30%. or like this is just off AI 2020 27 but um uh I assume like it's saturated at that point is that why they expect it to then just like go go at like the I do think this is underrated to some degree

**[1:20:50]** like to the the extent that like you don't instantly get like a doubling of the world's population in 2028 you maybe get you know tens of millions of geniuses in a data center um but you you don't get a doubling of the world's

**[1:21:02]** population um and so a lot depends on like exactly how smart they are exactly how efficient the models are at thinking out this kind of stuff. Uh these uh like let's do some rough math I guess like to to fact the H100 thing. Um you could

**[1:21:14]** probably run like a 100 model do like I don't know thousand tokens or something like that um on an H100. Uh so uh if like we're comparing that to number of should we compare that number? No. Okay, thousand tokens a second. Um

**[1:21:27]** humans are what? How fast can a human talk? There there was a really interesting paper. I don't know if you saw this. Um humans think at 10 seconds a second. Did you see this paper? A second. There was this really

**[1:21:35]** interesting paper about um if you look at the amount of like information we're processing in a second. Yeah. Um we're seeing all this visual data etc etc. But by a bunch of metrics where you think about how fast humans are processing

**[1:21:46]** it's at 10 seconds a second. So for example you'll have people fly over France or something even these so-called idiots of who will remember everything. If you think about like how long their plane ride was it's like 45 minutes. How

**[1:21:57]** many like if you do 10 tokens a second how much information would you have? It's like literally exactly that. So let's take that for granted. Then it's like an H100 is 100 humans a second. Yeah. If you think the tokens are

**[1:22:06]** equivalent. Yeah. If you think the tokens are equivalent. Yeah. Um which you still get pretty substantial numbers like even with your your 100 million H100s and you multiply that by 100 you're starting to like get to pretty

**[1:22:15]** substantial numbers. This does mean that those models themselves will be like somewhat comput in many respects. Um but these are all like these are relatively short-term changes in uh in like timelines of

**[1:22:28]** progress basically. Like I think yes it's highly likely we get dramatically entrance bottleneck in 2728. Yeah. Uh the impulse like to that will then be okay let's just d like try and turn out as many possible semiconductors as we

**[1:22:43]** can. There'll be some lag there. A big part of like how fast we can do that will depend on uh how much people are feeling the edgi in the next you know two years as they're building out fab capacity. Um a lot will depend on is how

**[1:22:56]** a China and Taiw like how is the Taiwan situation you know is Taiwan still producing LabBabs. There's another dynamic which uh was a reason that Eay and Tom when they're on the podcast said that they

**[1:23:06]** were pessimistic is that one they think we're further away from solving these problems with long context coherent agency advanced multimodality than you think and because and then their point is that uh the progress that's happened

**[1:23:21]** in the past over like reasoning or something has required many orders of magnitude increase in compute and if this scale of compute increase can continue beyond 2030 not just because of chips but also because of power and like

**[1:23:33]** raw GDP even then because we don't think we get it by 2030 or 2028 by just um uh then we think it's just going to take the the the probability per year just goes down a bunch yeah this is like biodal

**[1:23:45]** distribution uh a conversation I had with Leopold turned into a section in a situation awareness it's called this decade or bust um which is on exactly this topic which is basically that you know for the next couple of years we can

**[1:23:55]** dramatically increase our training compute and RL is going to be so exciting this year because we can you know dramatically increase the amount of compute that we apply to it. Um, and this is also one of the reasons why the

**[1:24:05]** gap between uh like say Deepseek and 01 was so close uh at the beginning of the year because they were able to apply like the same amount of compute to to the RL process. Um, and and so that compute differential actually like will

**[1:24:19]** be magnified over the course of this year. I I mean bringing it back to the there's so much lowhanging fruit. Yeah, it's been wild efficiency gains that these models have experienced over the last 2 years and and yeah, like with

**[1:24:33]** respect to Deepseek, I mean just really hammering home and like Daario has a nice essay on this. It's good. Um Deepseek was 9 months after Claude 3 sonnet. And if we retrained the same model today or at the same time as the

**[1:24:48]** Deepseek work, we also could have trained it for 5 million or whatever the advertised amount was. And so what what's impressive or surprising is that uh Deepseek has gotten to the frontier, but I think there's a common

**[1:25:02]** misconception still that they are above and beyond the frontier and and I don't think that's right. I think they just waited and then were able to take advantage of all the efficiency gains that everyone else was also seeing. Mhm.

**[1:25:13]** Yeah. I like they're exactly on the sort of cost curve that you'd expect which take away from the fact they're like brilliant engineers and like brilliant researchers who like I look at it I look at their work and I'm like ah like the

**[1:25:24]** kindred soul there in in the in the work they're doing and to go from like way behind the frontier to like oh this is like a real player like it's super incredible work. Okay. So people say that they have good research taste.

**[1:25:35]** Looking at their re papers what makes you say that? Yeah. Um I think their research taste is good in a way that I think like no one's research taste is good. Uh nom nom um nom brown also has good research taste but nom where they

**[1:25:51]** very clearly understand this uh dance between the hardware systems that you're like designing the models around and the uh sort of like algorithmic uh side of it. Um, and this is manifest in the way that the models give this sense of like

**[1:26:07]** being being like perfectly designed up to their constraints. Um, and and you can like really very clearly see what constraints they're thinking about as they're like iteratively solving these problems. And so I mean let's take the

**[1:26:19]** base transformer and like diff that to deepse v2 and v3. Um, you can see them running up against uh the memory bandwidth bottleneck in attention. Yeah. Um and you can see them uh initially they do MLA to do this. They they trade

**[1:26:35]** flops for memory bandwidth basically. Um and then they do this thing called NSA where they like more selectively load uh memory. And you can see actually like this is because the model that they trained uh with MLA was on H800s. Uh so

**[1:26:47]** it has a lot of flops. Um and so they they were like okay we can freely use the flops. But then uh the export controls uh so from like from uh Biden came in uh or like they had less of they knew they would have less of those chips

**[1:27:00]** going forward. Um and so they they traded off to like a more memory bandwidth uh oriented like algorithmic solution there. Um and you see a similar thing with their approach to sparity where they're like iteratively working

**[1:27:10]** out the best way to do this over mult multiple papers. Um and the part that I like is that it's simple a big failure mode. uh that a lot of ML researchers have is like you do these like overly complicated things that don't like think

**[1:27:26]** hard enough about the hardware systems that you have in mind. Um whereas the deepse the first deepseek like sparsity solution uh they design these like rack and like like node level uh load balancing losses. So you can see them

**[1:27:43]** being like, okay, like we have to like perfectly balance it on this. And then they actually come up with a much better solution later on where they don't have to have the auxiliary loss. Um uh where they they just have these like bias

**[1:27:54]** terms that they put in. Um and it's isn't that less simple? Like you're manually putting in a bias rather than but balancing auxiliary loss is annoying. Um like you're you're making the model like trade off uh this thing

**[1:28:05]** and like you have to with auxiliary losses you have to like control the coefficient and the waiting. Um the bias is like cleaner in some respects. Interesting. Um, did they do they had to change it through training? Uh, they did

**[1:28:15]** have to change it during training. Is is that does all training involve um continuously like [ __ ] with these values as you're going through it? Uh, depends on what your architecture is. Um, but like I I thought it was like I

**[1:28:28]** just thought it was cute that like you can see them running up into like this very hardware level constraint like try like go like what do we what do we wish we could express algorithmically? what can we express under our constraints and

**[1:28:37]** like iteratively solving to like get better constraints and doing this in a really like simple and elegant way and then like backing it up with great engineering. Uh I also thought it was interesting that they uh incorporated

**[1:28:48]** the multi-token prediction thing from meta. Um so Meta had a nice paper on this multi token prediction thing. Uh actually like I don't know if it's good or bad but like meta didn't include it in llama uh but DeepC did include it in

**[1:28:59]** their paper uh which I think is interesting uh like was that because they were like faster at iterating and including in the algorithm or did Meta decide that actually like it wasn't a good

**[1:29:10]** algorithmic change at scale? I don't know. M it was really interesting to me as somebody who's um had people on the podcast to discuss the I mean it's interesting from like what's happening in AI right now but also from the

**[1:29:22]** perspective of I I've been having abstract conversations with people about like what an intelligence explosion would look like or what would it look like for AI to automate AI R&D and just getting a a more uh tangible sense of

**[1:29:32]** like what's involved in making this AI progress. Um, and I guess one of the questions I was debating with Daniel is how much or I was asking him is how many of the um, improvements require a deep conceptual understanding versus how

**[1:29:46]** many are just like monkeys trying ideas and you could just like run a bunch in parallel. And it seems like the MLA thing is motivated by this like deep like conceptual understanding of like oh each attention head only needs to see

**[1:29:56]** like uh the subspace that's relevant to its attention pattern. Um, I feel like that just like required a lot of like conceptual insight in a way that these models are especially bad at. Um, as opposed to I don't know how the load

**[1:30:11]** balancing thing works, but that just seems like maybe you could like try it out and see what happens. Yeah, it's probably just like trying out a whole bunch of different things. I mean, it might also So, what fraction is which

**[1:30:17]** I'd be curious about. Yeah, I don't know about fractions. It might be like you have a hunch for a core problem, you can think of 10 possible ways to solve it, and then you just need to try them and see what works. Mhm. And that's kind of

**[1:30:28]** where the trial and error like sorcery of deep learning can kind of kick in. And and like Nom Shaz will talk about this like about how he like 5% of his ideas work. Um so even he uh like vaunted god of model like design

**[1:30:42]** architecture design uh is has like a relatively low hit rate but he just tries so many things right or being able to come up with any ideas in the first place. So one one like mechanism could be that like Nome just doesn't have to

**[1:30:53]** do any of the engineering work and he can just like abstractly express an intuition. Yeah, I I actually think like your rates of progress almost don't change that much depending on like so long as it's able to completely

**[1:31:04]** implement his ideas. Interesting. Same like if you if you have like Nom Jazer at 100x speed. Yeah. That's still kind of wild. Yeah. Um, like there's all these like fallbacks of like of like wild worlds where even if you don't get

**[1:31:18]** like 100% like normal level intuition in in model design, it's still okay if you just accelerate him by 100x, right? Especially since you're computer bottlenecked anyway. So like trying out his ideas or I guess he doesn't have the

**[1:31:31]** computer to try out all of his ideas. But Dores, you said, "Oh, well the model can do the more straightforward things and not the deeper thought." I mean, I do want to push back on that a little bit.

**[1:31:40]** I think again if the model has the right context and scaffolding it's starting to be able to do some really interesting things like the interp agent has been a surprise to people even internally at how good it is at finding the needle in

**[1:31:54]** the haststack like when it plays the auditing game finding this reward model bias feature and then reasoning about it and then systematically testing its hypothesis. So it looks at that feature, then it looks at similar features. It

**[1:32:06]** finds one with a preference for chocolate. It's like, huh, that's really weird that the model wants to add to recipes. Let me test it. And so then it will make up like, hey, I'm trying to make a tomato soup. What would be a good

**[1:32:18]** ingredient for it? And then sees that the model replies chocolate, reasons through it, and then keeps going. Right? There is conceptual understanding there. Deep conceptual understand. And even where like

**[1:32:28]** especially it's spotted, it's like, oh, this is a key part of its persona. I see this Oxford paper. What if I change Oxford to Stanford? What if I now say Richard Fineman really likes this thing? And it's like really carving out the

**[1:32:40]** hypothesis space and and and testing things in a way that I I'm kind of surprised by. Also, by the way, ML research is like one of the easier things to RL on in some respects once you get to a certain level of

**[1:32:50]** capability. It's very like well-defined objective function. Do the loss go down? Make number go down. Make number go down. um or make you know go up number go up depending on which which number it is um just flip the sign flip the

**[1:33:04]** sign and so once you get to the stage where models are capable of like implementing uh one of no one's ideas right and then you you can just like let them loose and like let them build that intuition of scientific of like how to

**[1:33:16]** do scientific discovery right um the key thing here again is the feedback loops of like I expect scientific areas where you are able to put it in a feedback loop to have eventually superhuman performance.

**[1:33:29]** I one prediction I have is that we're going to move away from can an agent do XYZ and more towards can I efficiently deploy launch a 100 agents? Yeah. And then give them the feedback they need and even just be able to like easily

**[1:33:45]** verify what they're up to. Right. There's this gen generator verifiier gap that people talk about where it's like much easier to check something than it is to produce the solution on your own. But it's very plausible to me we'll be

**[1:33:56]** at the point where it's so easy to generate with these agents that the bottleneck is actually can I as the human verify the answer and and again you're guaranteed to get an answer with these things and so ideally you have

**[1:34:09]** some automated way to evaluate and test uh a score for like how well it worked, how well did this thing generalize. Um, and and at at a minimum, you have a way to easily summarize what a bunch of agents are finding. And it's like, okay,

**[1:34:23]** well, if 20 of my hundred agents all found this one thing, then like it has a higher chance of being true. Mhm. And and again, software engineering is going to be the leading indicator of that, right? Like over the next six months,

**[1:34:33]** like the remainder of the year, basically, we're going to see progressively more and more experiments of the form of how can I dispatch work to a software engineering agent in such a way as async. Uh, Claude for's GitHub

**[1:34:45]** integration. uh where you can ask it to do things on GitHub, ask it to do pull requests, this kind of stuff that's coming up and the open codeex are like examples of this basically um where we you can sort of almost see this in like

**[1:34:58]** the coding startups. I I think of this like product exponential in some respects where you need to like be designing for like a few months ahead of the model to make sure that the product you build is the right one. Um and you

**[1:35:09]** saw like last year, you know, cursor hit PMF with uh claw 3.5 sonnet, right? like the they were they were around for a while before but then the model was finally good enough that the vision they had of how people would program like

**[1:35:20]** hit. Yeah. Um and then uh you know Windinsurf bet like a little bit more aggressively even on the agenticness of the model like uh you know you could like with longer running agentic workflows and this kind of stuff and I

**[1:35:32]** think that's when they they sort of like began competing with cursors when they bet on that particular vision. And the next one is is you're not even in the loop so to speak. you're not in an IDE, but you're asking the model to go do

**[1:35:45]** work in the same way that you would ask someone on your team to go do work. Yeah. Um, and that is not quite ready yet. Like there are still a lot of tasks where you need to be in the loop. Yeah. But the the next six months looks like

**[1:35:58]** an exploration of like exactly what does that trend line look like? Yeah. But just to be really concrete or pedantic about the bottlenecks here. A lot of it is again just tooling and are the pipes connected like a lot of things. I can't

**[1:36:10]** just launch Claude and have it go and and solve because maybe it needs a GPU or maybe I need very careful permissioning so that it can't just like take over an entire cluster and like launch a whole bunch of things, right?

**[1:36:22]** So you you really do need good sandboxing and the ability to to to use all of the tools that are necessary and we're almost certainly like under eliciting dramatically when you look at meters evals of can the model solve the

**[1:36:34]** task. they're there solving them for like hours over like multiple iterations. Um, and eventually one of them is like, "Oh yeah, I've come back and and I've solved the task." Me at the moment at least like maybe the fault is

**[1:36:44]** my own. But I try the model on doing something and if it can't do it, I'm like, "Okay, fine, I'll do it." Um, I don't which is interesting because we don't even treat other humans this way, right? Like you hire a new employee,

**[1:36:55]** you're not like, "I'll do it." Yeah. You like give them like spend literally weeks giving them feedback um where like we'll give up on the model in like minutes. Yes. Exactly. But but I think part of it is is it async or not, right?

**[1:37:07]** Yes. And and if it's human in the loop, then it's so much more effortful and unless it's getting replying immediately. Um I've noticed if I don't have a second monitor with cloud code always open in the second monitor, I

**[1:37:19]** won't really use it. It's only when it's right there and it's I can send off something, if it hits, great. If not, I'm kind of working on it at the same time. But this more async form factor, I expect to like really quite dramatically

**[1:37:31]** improve the experience of these models. Interesting. Interesting. Well, you can just say like, "Let's see if it can do that." Yeah. Let's give it a whirl. Um try 10 different approaches. Yeah. Yeah. Just fire it off. Yeah. Fire it up.

**[1:37:42]** Before we end this episode, I I do want to get back at this crux of um you why does the progress that you're talking about in computer use agents and white collar work happen over the next few years? Why is this not a thing that

**[1:37:54]** takes decades? And I think the correct comes down to um the people who expect something much longer have a sense that uh when Andrew and Tommy on my podcast they were like look you could look at

**[1:38:09]** Alph Go and say like oh this is a model that can do exploration. It can like Alpha Zero can generalize to new video games. It has all these priors about how to engage with the world and so forth. The intellectual ceiling is really high.

**[1:38:21]** Yeah. Exactly. And then in retrospect, obviously a bunch of the methods are still used today in deep learning. And you can see um see similar things in the models that we train today, but it was fundamentally like not a sort of like

**[1:38:35]** baby AGI that we just had to like add a little like sprinkle of something else on top of in order to make it the LLM of today. And I I just want to like very directly address this crux of why are LLMs

**[1:38:51]** um in a much different position with respect to true AGI than Alpha Zero? Why are they actually the base on which like adding in a few extra drops of this kind of uh care and attention? Yeah. Uh gets us to human level intelligence. I think

**[1:39:09]** uh one important point is that when you look at Alphas, it does have all of those ingredients. Um and in particular, I think like the intellectual ceiling goes like quite contra what I was saying before, which

**[1:39:20]** is like we've demonstrated this incredible complexity of like math and programming problems, right? Um, I do think that the type of task and setting that alpha zero like it worked in this two-player perfect information

**[1:39:34]** uh like game basically is incredibly friendly to RL algorithms. Um, and the reason it took so long to to get to like a more AGI protoagi style models is you do need to crack that like general conceptual understanding of like the

**[1:39:51]** world and language and this kind of stuff and you need to get the initial reward signal on tasks that you care about in the real world which are like harder to specify than games. Um, and I think then that like that that sort of

**[1:40:04]** like gradient signal that comes from the real world like all of a sudden you get access to it and you can start climbing it. Um, whereas Alphas didn't didn't ever have like the first rung to pull on. Yeah. Yeah. This goes back to the

**[1:40:16]** monkeys on the typewriter I think and like the pre-training model and until you had something like GPT3 GPT4, it just couldn't generate coherent enough sentences to even begin to do RHF and tell it what you liked and didn't like.

**[1:40:28]** Yeah. M if we don't have even reasonably robust um or weekly robust computer use agents by this time next year, are we living in the the bust timeline as in 2030 or bust? I would be extremely surprised if that was the case and I

**[1:40:46]** think that would be like somewhat of an update towards like there's something like strangely difficult about this like computer use in particular. Um, I don't know if it's the bus timeline, but it's definitely like the I would update on

**[1:40:57]** this being like lengthening of time. Yeah. But yeah, I mean, I think more and more it's no longer a question of speculation. If people are skeptical, I'd encourage like using clawed code or like some agentic tool like it and just

**[1:41:14]** seeing what the current level of of capabilities are. Tweeting is so much easier. But seriously, like the models are getting really capable at tasks that we care about and we can give them enough

**[1:41:26]** data for and and I mean the circuits results from interpretability are also pointing in the direction that they're doing very reasonable generalizable things. Uh and so yeah, this question matters a lot, but um I'm surprised by

**[1:41:43]** how many deep learning critics just like haven't really interacted with the models or haven't in a while and constantly move the gold fists. Yeah. Yeah. Yeah. Yeah. Like the turning test used to be a thing, right? Like we don't

**[1:41:54]** even talk about it and it'd be like silly to think that it was a meaningful test. Yeah. Yeah. Now, that being said, one caveat on that is like if software engineering is just like dramatically better than computer use, I mean,

**[1:42:05]** computer use still sucks, then I'd be like still like h maybe everyone just kept focusing on software engineering. Like it was just like by far the most valuable thing like like every marginal person and dollar went towards software

**[1:42:15]** engineering. I don't think that's the case. I do think like computer use is valuable enough that like you know people will care about it. Uh but that would be like my that's my one like escape patch that I'm putting in place

**[1:42:25]** for next year. Yeah, it would be good from an alignment perspective too because I think you kind of do need a wider range of skills before you can do something super super scary. Oh, like as in if the models didn't get

**[1:42:38]** any better. Yeah. If it's like just they're superhuman coders, but they're not like Henry Kissinger level. I don't No, that seems okay. Like if we have AI oracles. Yeah, that's what I'm saying. That's good.

**[1:42:49]** Yeah. Yeah. Exactly. Yeah, I think that's good. Yeah. So, if you look back at AI discourse like going back a decade, there's a sense that there's dumb AI, then there's AGI, then there's ASI, that intelligence is the scalar

**[1:43:01]** value. Um, the way you've been talking about the these models has a sense of jaggedness. It's especially tuned to environments in which it's been trained a lot or has a lot of data. Um, is there a sense in which like there

**[1:43:20]** it still makes sense to talk about the general intelligence of these models? Is there enough metalarning and transfer learning that is distinguished between like the sizes of models or like uh the way models are trained or are we moving

**[1:43:30]** into a regime where it's not about intelligence, it's more so about uh domain? Yeah. So one intuition pump is this conversation was had a lot when models were like GPT2 sized and fine-tuned for various things. Uh and

**[1:43:46]** they found you know people would find that the models were dramatically better at things that they were fine tuned for right uh but by the time you get to GP4 when it's trained on a wide enough variety of things actually the like the

**[1:43:57]** sort of total compute like it generalized very well across all of like the individual subtask actually generalized better than smaller fine-tuned models. um in a way that was extremely useful.

**[1:44:07]** Uh I think right now what we're seeing with RL is is pretty much the same story playing out where uh there's this jaggedness of like things that they're particularly trained at. But as we expand the total amount of compute that

**[1:44:18]** we do RL with, you'll start to see the same transition from like GPT2 fine-tunes to uh like GPD3, GPD4 like unsupervised like metal learning and like generalization across things. And I think we're already seeing like early

**[1:44:32]** evidence of this uh in its ability to like generalize reasoning to uh things, but um like I think this will be like extremely obvious uh soon. One nice example of this is just the ability or notion to backtrack, right? You go down

**[1:44:48]** one solution path, ooh wait, let me try another one. Uh and this is something that you start to see emerge in the models through RL training on harder tasks. And I I I think right now I it's not generalizing incredibly well at

**[1:45:02]** least with with well I mean has have we ever RL the model to be a interp agent? No. I mean no. Yeah. Exactly. Yeah. Like so all this time we're talking about like oh it's only good at things that's being rled that. Well it's pretty good

**[1:45:13]** at that because that's pretty you know that is a mixture of like science and like understanding language and like uh and coding. Um like there's this sort of like mixture of domains here. All of which you need to understand. like you

**[1:45:24]** need to be both a great software engineer and be able to like think through language and and like like state of mind and almost philosophize in some respects to be an interp agent. Yeah. Um and it is generalizing from the

**[1:45:36]** training. Yeah. To do that. What's the endgame here? Claude aid comes out um and they give it to you and dot dot dot you say thumbs up. What's happened? What do you Yeah, I mean it it really depends upon the timeline at which we get Claude

**[1:45:54]** 8 and the models hit like ASL 4 capabilities, right? Like like fundamentally we're just going to use whatever tools we have at the time and see how well they work. Uh ideally we have this enumerative safety case where

**[1:46:05]** we can almost like verify or prove that the model will behave in particular ways. Um in the worst case we use the current tools like when we won the auditing game of seeing what features are active when the assistant tag lights

**[1:46:20]** up. Can you can you explain what is mechanistic interpretability? What are features? What are circuits? Totally. Yeah. Yeah. Yeah. So uh mechanistic interpretability or the cool kids call it mechan is uh trying to reverse

**[1:46:31]** engineer neural networks uh and figure out kind of what the core units of computation are. Um, lots of people think that because we made neural networks, because they're artificial intelligence, we have a perfect

**[1:46:44]** understanding of how they work. And it couldn't be further from the truth. Uh, neural networks, AI models that you use today are, uh, grown, not built. Uh, and so we then need to do a lot of work after they they're trained to figure out

**[1:46:59]** to the best of our abilities how they're actually going about their reasoning. And so uh two and a half three and a half years ago uh this kind of agenda of applying mechanistic interpretability to large language models started uh with

**[1:47:15]** Chris Ola leaving OpenAI co-ounding anthropic. Um and every roughly six months since then we've had kind of like a major breakthrough in our understanding of of these models. And so first with toy models of superp position

**[1:47:32]** uh we established that models are uh really trying to cram as much information as they possibly can into their weights. Uh, and this goes directly against people saying that neural networks are overparameterized.

**[1:47:45]** And like classic AI, machine learning back in the day, you would use linear regression or something like it. And people had a meme of AI or or neural networks, uh, deep learning be using way too many parameters. Um, there's like

**[1:48:00]** this funny meme that you should show of like layers on the x-axis and layers on the y- axis and this like jiggly line that just goes up and it's like, oh, just throw more layers at it, right? Um, but it but it actually turns out that at

**[1:48:12]** least for really hard tasks like being able to accurately predict the next token for the entire internet, these models just don't have enough capacity. And so they need to cram in as much as they can. And the way they learn to do

**[1:48:24]** that is to use each of their neurons or units of computation in the model for lots of different things. And so if you try to make sense of the model and be like, oh, if I remove this one neuron or like what is it doing in the model? It's

**[1:48:37]** impossible to make sense of it. it'll fire for like Chinese and fishing and horses and I don't know just like a hundred different things. Um, and it's because it's it's trying to juggle all these tasks and use the same neuron to

**[1:48:51]** do it. So that's that's superposition. N months later we write uh towards monosmanticity which introduces uh what are called sparse autoenccoders. And so going off what I just said of the model trying to cram too much into too little

**[1:49:06]** space, uh we give it more space uh this this higher dimensional representation uh where it can then more cleanly represent all of the concepts that it's understanding. And and this was a a very toy paper in so much as it was a two

**[1:49:22]** layer really small really dumb transformer and we fit up to I want to say 16,000 features which we thought was a ton at the time. Fast forward 9 months we go from a two-layer transformer to our claw 3 sonnet frontier model at the

**[1:49:39]** time and fit up to 30 million features. And this is where we start to find really interesting abstract concepts like a feature that would fire for code vulnerabilities. And it wouldn't just fire for code vulnerabilities. It would

**[1:49:51]** even fire for like you know that Chrome page you get if you like it's not an HTTPS um URL and it's like warning this site might be dangerous like click to continue it and like also fire for that

**[1:50:04]** for example. And so it's like these much more abstract coding variables or sentiment features amongst the 30 million. Um, fast forward nine months from that and now we have circuits and I threw in the

**[1:50:19]** analogy earlier of uh the Ocean 11 heist team where now you're identifying individual features across the layers of the model that are all working together to perform some complicated task and you can get a much better idea of how it's

**[1:50:34]** actually doing the reasoning and coming to decisions like with the medical diagnostics. Um, one example I didn't talk about before is um with like how the model retrieves facts. And so you say like what sport did Michael Jordan

**[1:50:47]** play? And not only can you see it hop from like Michael Jordan to basketball answer basketball, but the model also has an awareness of when it doesn't know the answer to a fact. And so by default, it will actually say, I don't know the

**[1:51:03]** answer to this question. But if it sees something that it does know the answer to, it will inhibit the I don't know circuit and then reply with the circuit that it actually has the answer to. So for example, uh if you ask it who is

**[1:51:17]** Michael Batkin, which is just a madeup fictional person, u it will by default just say I don't know. It's only with Michael Jordan or someone else that will it will then inhibit the I don't know circuit. But what's really interesting

**[1:51:29]** here and where you can start make making downstream predictions or reasoning about the model is that that I don't know circuit is only on the name of the person. And so in the paper we also ask it uh what paper did Andre Karpathy

**[1:51:42]** write. And so it recognizes the name Andre Karpathy because he's sufficiently famous. So that turns off the I don't know reply. But then when it comes time for the model to say what paper it worked on, it doesn't actually know any

**[1:51:55]** of his papers. And so then it needs to make something up. And so you can see different components and different circuits all interacting at the same time to lead to this this final answer. Why I think it's a tractable problem to

**[1:52:09]** like understand every single thing that's happening in a model or like that's the best way to understand what why it's being deceptive. If you wanted to explain why England won World War II using particle physics, uh you would

**[1:52:22]** just like be on the wrong track. You just want to look at the highlevel explanations of who had more weapons, like what did they want? And that seems analogous to just training linear probes for like are you honest? Are you being

**[1:52:34]** deceptive? Like um do we catch you doing bad things when we're red teaming you? Can we monitor you? Um why is this not analogous where we're asking a particle physicist to just backtrack and explain why um why England won World War II? I I

**[1:52:50]** feel like you just want to go in with your eyes wide open, not making any assumptions for what that deception is going to look like or what the trigger might be. Yeah. Uh and so the wider you can cast that net, the better. Depending

**[1:53:03]** on how quickly AI accelerates and where the state of our tools are, we we might not be in the place where we can like show prove from the ground up that everything is safe. Uh but the like I feel like that's a very good north star.

**[1:53:15]** It's a very powerful reassuring north star for us to aim for especially when we consider we are part of the broader AI safety portfolio. I mean do you really trust like you're about to deploy this system and you really hope it's

**[1:53:28]** aligned with humanity and that you've like successfully iterated through all the possible ways that it's going to like scheme or sandbag. But that's also probably going to be true with whatever you find. you're not I mean you're not

**[1:53:41]** you're still going to have variance that you haven't explained or like you found a feature but you don't know if it actually explains deception or something else instead or so so I I guess first of all I'm not saying you shouldn't try the

**[1:53:53]** probingo approach right like we want to pursue the entire portfolio we we've got the therapist interrogating the patient by asking do you have any troubling thoughts we've got um the linear probe which I'd analogize to like a polygraph

**[1:54:09]** test where We're taking like very highlevel summary statistics of the person's wellbeing and then we've got the neurosurgeons kind of going in and seeing if you can find any brain components that are activating and

**[1:54:21]** troubling or or off distribution ways. So, so I think we should do all of it. Um what what percent of the alignment portfolio should meant be? Uh I think as much of a chunk as is necessary. I mean I I think at least like question. Yeah.

**[1:54:37]** Hard hard hard to define, but I don't know at anthropic I feel like all of the different portfolios are like being very well supported and and growing. Um you can also going back to like the the World War II question. You can think of

**[1:54:49]** it as like a hierarchy of abstractions of trust here where like let's say you want to go and talk to like Churchill. Um it helps a lot if you can verify that in that conversation in that 10 minutes he's being honest. Um, and this like

**[1:55:00]** enables you to construct better meta narratives um of what's going on. And so maybe particle physics wouldn't help you there, but certainly like the neuroscience of Churchill's brain would help you verify that he was being

**[1:55:13]** trustworthy in that conversation and that the like, you know, the soldiers on the front lines were being honest in their depiction of their description of what happened and this kind of stuff. like so long as you can verify like

**[1:55:23]** progress like parts of the uh the tree up then that that that massively helps you build confidence. Yeah, I think language models are also just really weird, right? Like with the emergent misalignment

**[1:55:34]** work they I I don't know if they took predictions they should have of like, hey, I'm going to fine-tune chatbt on code vulnerabilities. Is it going to become a Nazi? And I think most people would have said no. And that's what

**[1:55:46]** happened. And so what are the different How did they discover that it became a Nazi? They started asking it a ton of different questions and it will do all sorts of like vile and harmful things. like the whole persona just totally

**[1:55:59]** changes and and I mean we are dealing with alien brains here who don't have the social norms of humans and or or even a clear notion of like what they have and haven't learned uh that that that we have of them. I mean and and so

**[1:56:13]** I think you really want to go into this with with eyes wide open. Backing up for me, uh, if you live in a world where AI progress accelerates, um, by the way, you were mentioning a little while ago that there's many wild

**[1:56:28]** worlds we could be living in, but we're living at least one of them. Um, another one that we've uh, gestured at, but it's worth making more explicit is this. Even if the AI models are not helping write the next training algorithm for their

**[1:56:41]** successor, just the fact that if they had human level learning efficiency, uh whatever a model is learning on the job or whatever copy of the model is learning on the job, the whole model is learning. So in effect, it's getting or

**[1:56:54]** if they're like a thousand times less efficient than humans are learning. That's right. And you just like deployed them even still. Exactly. Yeah. Yeah. Anyways, and and there's a whole bunch of other things you can think about, but

**[1:57:04]** e even there it's like you kind of have like a broadly deployed intelligence explosion and I do think it's worth like worth pressing on that future of um you know there is this whole spectrum of crazy futures but the one that I feel

**[1:57:15]** we're almost guaranteed to get and this is like a like a almost a strong statement to make um is one where like at the very least you get drop in like white collar worker at some point in the next 5

**[1:57:28]** years. It's like I think it's very likely in two. Um but it seems almost overdetermined in like five and and on like the grand scheme of things like those are kind of irrelevant time frames like it's the same either way. Um and

**[1:57:41]** that completely changes the world over the next decade. Um and and if the sort of if we don't have the right policies in place for that then you end up actually with almost in some respects like a fundamentally worse world because

**[1:57:53]** the thing that these models get good at by default is like software engineering and like computer using agents and this kind of stuff and then we need to we will need to put in extra effort to put them in the loops where they help us

**[1:58:05]** with scientific research or they're like we have the right robotics such that we actually like experience an increase in material quality of life. Um, so that's worth thinking about like if you're in the perspective of like I'm a country

**[1:58:16]** like what should I be doing or thinking about uh like plan for the case where where white collar work is automatable um and then consider what does that mean for your economy and what you should be doing to prepare policy what should you

**[1:58:29]** be doing to prepare cuz honestly honestly it's like such a tough question where like if you're India or Nigeria or Australia um if you're a country unlike uh America or China where they do have frontier

**[1:58:41]** models What is it that you should be doing right now especially on such a short time scale? Yes. Uh so I think one very important point is that let's say this scenario turns out true then compute

**[1:58:54]** becomes the most valuable resource in the world like the sort of GDP of your economy is dramatically affected by how much compute you can deploy towards the sort of organizations within your country. Um and so having some uh

**[1:59:07]** guaranteed amount of compute I think will actually be quite important. So like pre getting ahead of investments in like data centers and this kind of stuff on the condition that it's like companies in your country have to be

**[1:59:18]** allowed to to use that compute. Um yeah not necessarily for training but like just even just for inference like I think the economic value here comes from inference. Um I think it also makes sense to invest broadly in uh in AI like

**[1:59:31]** I think these countries have the opportunity to do so and I think that's like a portfolio of like you know foundation model companies but also like robotic supply chain and this kind of stuff. Um I think that you should invest

**[1:59:41]** very proactively in policies that try and pre like prevent capital lock in. Um, so we're in for a much worse world if like it just so happens that the people who had like money in the stock exchange or in land before AGI are like

**[1:59:57]** dramatically more wealthy than the people who don't because it's a gross misallocation of resources. Uh, so having like I know one of my favorite episodes actually on your podcast was like the Georgeism one where you kind of

**[2:00:10]** like like appropriately like value allocate land. Um and so I think I think like this strikes particularly close to home coming from Australia where I think like our like uh policies with respect to land are like grossly wrong. Um but I

**[2:00:25]** think this is broadly true. Um being very uh like forward on regulation of integration of these models into uh into like your country um is is important. Um and proactively uh making sure that people have choice like so

**[2:00:40]** let's say uh you should be like quite proactive about making sure that like the phones or devices or like glasses that people have people have like free choice on like what things they run. [Music]

**[2:00:52]** Um and then so that's like that's the we just get white collar worker right and like you're trying to like do the best to like prepare your country for that. Um and then it's like okay well what can you do to like make all possible

**[2:01:05]** versions of the future go like well like that's like covering some amount of like economic downside. Uh the other like things I think are really important is like figure out how you can uh like either make the like basically

**[2:01:20]** ensure dramatic upside or cover uh like terrible downside. Um and so like getting dramatic upside is like making sure that there like is investment in bi like biology research and this kind of stuff in an automated way that is like

**[2:01:33]** uh these models are actually like able to produce novel medicines that mass like massively improve our like quality of life and covering the downside is like AI alignment research and this kind of stuff and automated testing and like

**[2:01:42]** really thinking hard about that AI safety institutes this kind of stuff. But these seem like things that a rich person a random rich person could also do like there's it seems like There's not a thing that a nation state

**[2:01:56]** is uniquely equipped to do. That's a good point. In this in this scenario, I mean like dramatic allocation of res of like resource towards compute I think is is sensible. Um I would be doing that if I was in charge of a nation state. I

**[2:02:08]** think it just increases your optionality in like most of the future worlds. Um Dylan Patel has some scary forecasts on US energy versus China. Yes. Yeah. We're like 34 gawatt off. Yeah. Yeah. The US's line is like flat basically and China's

**[2:02:23]** line is like this and I mean the US like very clearly yeah we just need so many more power plants. Yes. If intelligence becomes this like incredibly valuable input like a intelligence becomes almost a raw input into the economies and

**[2:02:35]** quality of life of future. Um the thing directly underneath that is energy. Um and so making sure that you have like you know incredible amounts of solar like tile the desert in solar panels you know some parts of the desert in solar

**[2:02:48]** panels um would be would be helpful towards making sure that you have uh more access to intelligence on top. Yeah, ju just to make it explicit because we've been touching on it here. Even if AI progress totally stalls or

**[2:03:01]** you think that the models are really spiky and they don't have general intelligence, it's so economically valuable and sufficiently easy to collect data on all of these different jobs, these white collar job tasks such

**[2:03:14]** that to Shalto's point, we will we should expect to see them automated within the next 5 years. Yeah. Even if you need to hand spoon every single task to the model, it's like economically worthwhile to do. So even if like

**[2:03:26]** algorithmic like progress stalls out and like we just never figure out how to like keep progress going, which I don't think is the case, like it that hasn't stalled out yet. It seems to be going great. Um the current suite of

**[2:03:38]** algorithms are sufficient to automate white color work provided you have enough of the right kinds of data. Yes. and in a way that like compared to the TAM of salaries for all of those kinds of work is so like trivally worthwhile.

**[2:03:51]** Yeah, exactly. Uh I I do just want to flag as well that there's a really dystopian future if you take more of X paradox to its extreme which is this paradox where we think that the most valuable things that humans can do or

**[2:04:04]** the smartest things are like add large numbers in our heads or do any sort of white collar work and then we totally take for granted our fine motor skill and coordination. But from an evolutionary perspective it's the

**[2:04:15]** opposite. So, uh, we got like evolution has optimized fine motor coordination so well and even if you look at like robot hands or like even the ability to open a door is still just like really hard for robots. Um, meanwhile, we're seeing this

**[2:04:29]** total automation of coding and everything else that we've seen as clever. The the really scary future is one in which AIs can do everything except for the physical robotic tasks. in which case you'll have humans with

**[2:04:41]** like AirPods and like glasses glasses and there'll be some robot overlord controlling the human through cameras by just like telling it what to do and like having a bounding box around the thing you're supposed to pick up and so you

**[2:04:53]** have like human meat robots um and and not like necessarily saying that like that's what the AIs would be like want to do or anything like that but as in like if you were to be like what are the relative economic value of things like

**[2:05:03]** the AIS are out there doing computer programming and like the most valuable thing that humans can do is like be amazing robots. Um, now that being said, I think more of paradox is a little bit fake. Um, I think the main reason that

**[2:05:13]** robots are worse than uh at like being a robot than they are at software engineering is the internet exists for software engineering. Uh, like GitHub exists and uh there is no equivalent thing like if you had

**[2:05:26]** um all like you know moap of everyone's actions as they were like going about their daily lives um for like some reasonable fraction of the human population. Robotics is also like close to solved like like like on track to be

**[2:05:39]** solved at the same rate that software engineering is on track to be solved. Um so this is only like this vision is only like a sort of decade long section but it's still pretty terrible decade. Like imagine the world where uh people have

**[2:05:52]** lost their jobs. You haven't yet got novel biological research that means like people's quality of life is like dramatically better. you don't yet have material abundance because uh you like haven't actually been able to action

**[2:06:02]** like action the physical world um in the like necessary way. Like you can't build dramatically more um because that's like building dramatically more takes robots basically. Um and people's like main comparative advantage is uh as fantastic

**[2:06:18]** robots is like a shocking shocking world. I mean from the perspective of an average human I think it actually might be better. your like wages will be higher because you're you're the complement to something that is

**[2:06:28]** enormously valuable, right? Which is AI labor, right? Um and like you know a decade or two on like the world is fantastic, right? Like you truly like robotics is solved and you decide to get like you know like radical abundance

**[2:06:41]** basically. um provided that you have all the policies set up like necessary to permit building like you sort of you end up with that same change from you know the like the the before and after photos of Shanghai where like 20 years on it's

**[2:06:53]** just like this dramatically transformed city like a lot of places in the world probably end up like that right um over that two decade period but we need to make sure like one do our best to estimate is this actually what is on

**[2:07:07]** track to happen like build sweet bench but for all the other forms of white collar and measure and track. That's a great thing that government should be doing by the way is like trying to break down the sort of functions of their

**[2:07:18]** economy into measurable tasks and figuring out where what does the curve actually look like for that because they might be a bit shocked by uh the progress there. um you know there's no sweet bench for tax uh like tax eval um

**[2:07:33]** and uh then and I don't like have all the answers here but like figuring out a way to like share the proceeds of this economy like broadly across people or like invest heavily in robotics and

**[2:07:44]** collecting the data so that we get robotics faster we get material abundance faster invest in biological research that we get but like all that faster they basically try and pull forward the radical upside um because

**[2:07:54]** because otherwise you have a pretty dark yeah section. I think one thing that's not appreciated enough is how much of our leverage on the future, given the fact that our labor isn't going to be worth that much, comes from our economic

**[2:08:08]** and political system surviving. Mhm. Um, for your millionxed S&P equity to mean something, for uh your contracts to mean anything, for the government to be able to tax the AI labor and give you a UBI off of that. It just like that requires

**[2:08:23]** our legal institutions, our economic institutions, our financial rail surviving into the future. Yes. The way in which that likely happens is if it's also in the AI's best interests that they follow those rails. And by AI, I

**[2:08:36]** don't mean some monolithic single AI. I just mean like firms which are employing AI and becoming more productive as a result. Um you don't want to be in a position where it's so ownorous to operate in our system that you're

**[2:08:51]** basically selecting for firms who either immigrate or who are like doing black market stuff etc. And which means I think like you want to make it super super easy to deploy AI uh have the equivalent of special economic zones

**[2:09:06]** etc. Um because otherwise you are just surrendering the future. Yeah. Outside of any control that you might have on it. Um one of the reasons by the way that I worry about uh turning AGI into a national security issue or having it

**[2:09:24]** have extremely close ties with the government, the Manhattan Project thing is that it disproportionately redirects the use of AI towards military tech and the mosquito drones and whatever. Um and and also naturally puts other countries

**[2:09:40]** in the same frame of mind, right? If we're developing the mosquito drones, why would China not develop the mosquito drones? Um and that just seems like a zero sum race and not to mention a potentially catastrophic one. Yes.

**[2:09:51]** Whereas like, you know, like compute will be limited. You know, we we want we we will need to disproportionately accelerate some things. To the extent it just remains totally like a consumer free market um landscape, it just seems

**[2:10:04]** more likely that we'll get the glorious transhumanist future where they're developing the things that make human life better. Yes, I I mean I agree like the the case where you end up with like two national projects facing off against

**[2:10:15]** each other is dramatically worse, right? Uh like we don't want to live in that world. Yeah. Uh it's much much better if this like stays a free market, so to speak. Yeah. Yeah. Yeah. Okay. I want to take issue with your claim that even if

**[2:10:29]** with the with the algorithms of today, if we just collect enough data, yeah, that we could automate white color work. First, let me get an understanding of what you mean by that. So, do you mean that we would do the analogous thing of

**[2:10:39]** free training with all the trajectories of everything people do on their jobs? Could you um could you make either manually or through some other process uh some RL procedure based on the screen recordings of every white color worker?

**[2:10:53]** What kind of thing are you imagining? I mean like a continuous distribution of this stuff. Uh one like important like mental model to think about RL is I think as like the the task gets more there is some respect with which like

**[2:11:08]** longer horizon or better at that task if you can do them if you can get that reward ever are like easier to judge. Um so like again this comes back to like can you make money on the internet that's an incredibly easy reward signal

**[2:11:20]** uh to judge. Uh but to like do that there's like a whole hierarchy of like complex behavior. So if you could like pre-train up to the easy to judge reward signals like does your website work? Does it go down? Like did people like

**[2:11:30]** it? Like there's there's all these reward signals that we can respond to because we have a long we can like progress through these long enough trajectories to actually like get to interesting things. If you're stuck in

**[2:11:41]** this regime where like you need a reward signal every five tokens like it's a way more painful and like long process. But if you could like pre-train on every like screen in America, um then probably the like RL tasks that you can design

**[2:11:57]** are very different to like if you could only like take the existing internet as it is today. Um and so like how much of that you get access to like changes the the mix. Interesting. So, as we're training them on longer and longer

**[2:12:09]** horizon tasks and it takes longer for them to get any any signal on whether they successfully complete the task, will that slow down progress because it takes more compute per per task? I do think there's this notion the longer the

**[2:12:22]** harder tasks, the more training is required. And I'm sympathetic to that naively, but we as humans are very good at practicing the hard parts of tasks and and decomposing them. And I think once models get good enough at the basic

**[2:12:37]** stuff, they can just rehearse or fast forward to the more difficult parts. I mean that's definitely one of the big complexities, right? Like as you use more compute and like the and as you train like more and more difficult

**[2:12:48]** tasks. I mean uh I don't know your rate of improvement at biology is going to be like somewhat bound by the time it takes a cell to grow um in a way that your rate of improvement on math isn't for example.

**[2:12:59]** Um so yes but I think for many things we'll be able to parallelize far like widely enough and and get enough iteration loops. Yeah. Um will will the um the regime of training new models go away?

**[2:13:15]** Will will we eventually get to like you you've got the model and then you just keep adding more skills to it with RL training? That depends on uh whether or not you think like there's a virtue in pre-training a new architecture.

**[2:13:27]** basically you make some like architectural change uh then you like probably need to like do some form of like at least like retraining a new model. How does the fact that um if RL requires a bunch of inference to

**[2:13:40]** do the training in the first place does that push against the thing you were talking about where we actually need a bigger model in order to have brain-like energy. Um but then also it's more expensive to train it in RL. So where

**[2:13:51]** does that balance out? I think we got to drink the bitter lesson here. And yeah, like you there aren't infinite shortcuts. Like you do just have to scale and have a bigger model and pay more inference for it. And if you yeah,

**[2:14:03]** if you want AGI, then that's what you got to got to pay the price of. But but there's like there's a trade-off equation here, right, of like uh there is science to do which you know everyone is doing of what is the optimal point at

**[2:14:14]** which to do RL um because you need something which can both learn uh and discover the sparse reward itself. So you don't want a one parameter model. Useless even though you can run it really fast. Um you also don't want you

**[2:14:27]** know like 100T model because like super slow. Yeah. Possible RL. So um and like the sort of the the marginal benefit of like its learning efficiency is like not worth it, right? So there's like a there's a predier here like what's the

**[2:14:40]** optimal model size at like your current class of capabilities and like your current set of RL environments and this kind of stuff. Yeah. And and even in the last year there's been much more of a factor of the inference cost, right? So

**[2:14:50]** just explicitly like the bigger the model the more expensive it is to do a forward pass and generate tokens. And the calculus used to just be should I allocate my flops to more training data or a bigger model. And now another huge

**[2:15:04]** factor is how much am I actually going to do forward passes on this model once it's trained. Yeah. My total pool of like compute. How do I allocate that across train data compute and inference compute for the RL training? And then

**[2:15:14]** even within inference there's all this research on well what strategy should I use? Should I sample 10 and take the best? Do I do this sort of like branching search, etc., etc. And so with RL where you're sampling a whole lot of

**[2:15:27]** tokens, you also need to factor in the ability for the model to like actually generate those tokens and then and then learn and get feedback. Okay. So if we're living in this world, what is your advice to somebody early in their career

**[2:15:41]** or a student in college? How should they be uh what should they be planning on doing? Yeah. Um so I think once again there's like it's worth considering the spectrum of possible worlds and preparing yourself for that and the one

**[2:15:53]** like the sort of action that I think is like highest EV in that case is you are about to get dramatic in the at a minimum you are about to get dramatically more leverage you already have like already the startups in YC

**[2:16:04]** like you know writing huge amounts of their code with uh you know claude um so what challenges what causes do you want to change in the world with that added leverage like if you had 10 engineers um at your beck and call what would you

**[2:16:18]** do or if you had a company at your beck and call like what would that enable you to do and what problems and domains suddenly become tractable that's the world you want to prepare for now that still requires a lot of technical depth

**[2:16:28]** obviously there is the case where AI just becomes dramatically better than like everyone at everything right but for at least a while probably there is like advantage I think Jensen actually talked about this in an interview in an

**[2:16:39]** interesting way where he's like you know I have like 100 thousand general intelligences around me and I'm still like somewhat useful um because I'm there like you know directing the values and like like asking them to do things

**[2:16:48]** and you know they're still like there I still have value even though I have 100,000 general intelligences and for many people I think that will still be true for a fair while um and then you know as the AI get better and better and

**[2:16:57]** better and like so on eventually no but uh again prepare for like the spectrum of possible worlds because in the event where we're just totally out competed yeah doesn't matter what you do but in all the other worlds matters a lot get

**[2:17:09]** the technical depth study biology study CS like really think hard about study physics think about hard about what challenges you want to solve in the world. Yeah, that's a lot of topics. You can now you can, right? Like it's so

**[2:17:23]** much easier to learn. Everyone, you know, everyone now has the like infinite perfect tutor. Yeah. Yeah. Yeah. Yeah. It's definitely been helpful to me. Yeah. I would say some combination of like get rid of the sunk cost of your

**[2:17:35]** like previous workflows or expertise uh in order to evaluate what AI can do for you. That's right. Um, and and another way to put this, which is fun, is just like be lazier in so much as like figure out the way that the agent

**[2:17:48]** can do the things that are toilsome. Um, but but it's you're going to have to in this you ultimately you get to be lazier, but in the short run, you need to like critically think about the things you're currently doing and like

**[2:18:00]** what an AI could actually be better at doing and then go and try it or explore it. uh because I think there's like still just a lot of lowhanging fruit of people assuming uh and not writing the full prompt giving a few examples

**[2:18:13]** connecting the right tools um for for your work to be accelerated automated. Yeah. Yeah. Um there's also uh the sunk cost of feeling like since you're not quote unquote early to AI that you've sort of missed the boat and you can't

**[2:18:27]** like but I I think I mean I remember when GPT3 came out so backstory on the podcast when I graduated college I was planning on doing some sort of AI rapper startup um and the podcast was just like a gateway into doing that and so I was

**[2:18:44]** trying out like different things and at the time I remember thinking oh 3.5 is out and people like I'm like so behind on like the startup scene here or whatever if I wanted to make my own rapper. Um I mean maybe the idea of the

**[2:18:56]** rapper was inadvisable in the first place but just like I every time feels early because like it's sort of if it's an exponentially growing process. Um and there were many things many ideas are only becoming possible now right so

**[2:19:08]** exactly that product exponential I talked about before like products literally obsoleted like you need to constantly reinvent yourself to stay at the like frontier of capabilities. By the way, do you remember I had a really

**[2:19:17]** shitty idea and I gave you a call. I don't know what it was. It was it was like um I think it was like rag for like lawyers or something. Yeah. Anyways, I give you I think one of our first interactions was I'm like, "Hey, what do

**[2:19:28]** you think of this idea?" And you're like, "I think the podcast sounds promising." Which I appreciate. Yeah. I I got slightly annoyed at a a friend recently who I think is really talented and

**[2:19:44]** clever and interested in AI but has pursued a biology route and I just kind of tried to shake them of like you can work on AI if you want to. Um I mean I I I think humans are artificial not artificial are biological general

**[2:20:02]** intelligences where a lot of the things of value are just very general. Yeah. And whatever kind of specialization that you've done maybe just doesn't matter that much. I mean again it cost but like so many of the people even my like

**[2:20:20]** colleagues at anthropic are excited about AI and they just don't let their previous career be a blocker. Um and because they're just like innately smart, talented, driven, whatever else, they're they end up being very

**[2:20:34]** successful and finding roles. It's not as if they were in AI forever. I mean, people have come from totally different fields. Uh, and so don't think that you need like permission from some abstract entity to like get involved and apply

**[2:20:49]** and be able to contribute. If um if somebody wanted to be an a researcher like right now, if you could give them an open problem or like this the kind of open problem that is very likely to be the

**[2:21:01]** um be quite impressive, what would it be? Uh, I think that now that RL's like come back, um, papers building on Andy Jones's like scaling board like scaling walls for

**[2:21:13]** board games are interesting. Um, like showing that you can uh, like investigating these questions like the ones you asked before where you're like, oh, like you know, is the model actually learning to do more than its previous

**[2:21:24]** pass at K or is it just like discovering that like exploring questions like that deeply I think are interesting. Yeah. Yeah. Like scaling laws for RL basically. very curious to see like how much uh uh like the marginal increase in

**[2:21:37]** metalarning from a new task or something. I mean on that note I think I think model diffing has like a bunch of opportunities. Yeah. Um also people say oh we're not capturing all the features there's all this stuff left on the

**[2:21:50]** table. What is that stuff that's left on the table? Yeah. Um like if the model's jailbroken is it using existing features that you've identified? Is it only using the error terms that you haven't captured? Yeah. Um I don't know. There's

**[2:22:02]** a lot here. I think Matts is great. Uh the anthropic fellowship has been going really well. Um Goodfire Anthropic invested in recently. They're doing a lot of interpretability work or just apply anything to anything to get your

**[2:22:13]** equity up. Huh. There's just so many interpretability projects that are are like there's so much low hanging fruit and we need more people and I don't think we have much time. Yeah. Uh I also want to make a

**[2:22:25]** plug for performance engineering. Um I think this is one of the like like best ways to to sort of demonstrate that you have like the raw ability to to do it like if you made a extremely efficient transformer implementation on TPU or

**[2:22:40]** trrenium or like in CUDA uh then I think there's a pretty high likelihood that you'll get a job offer. Um like there's a relatively small pool of people that you can trust to like completely own end to end the

**[2:22:53]** performance of a of a model. Um and and if you have broad deep electrical engineering skills, I think you can probably come up to speed pretty fast on accelerator stuff. Yeah, you can come up to speed like reasonably fast. Um and it

**[2:23:06]** teaches you a lot of good intuitions of the actual intricacies of what's going on in the models, which means that you're then very well placed to like think about architecture and this kind of stuff. Um one of my favorite people

**[2:23:15]** uh in thinking about architecture and anthropic at the moment actually like came from like a heavy GPU kernel programming background, just like knows the ins and outs really deeply and can think about the trade-offs really well.

**[2:23:23]** Um, this is fun, guys. Awesome. Thanks. Yeah, great to be back. I hope you enjoyed this episode. If you did, the most helpful thing you can do is just share it with other people who you think might enjoy it. Send it to your friends,

**[2:23:35]** your group chats, Twitter, wherever else. Just let the word go forth. Other than that, super helpful if you can subscribe on YouTube and leave a fivestar review on Apple Podcasts and Spotify. Check out the sponsors in the

**[2:23:47]** description below. If you want to sponsor a future episode, go to dwarcash.com/advertise. Thank you for tuning in. I'll see you on the next one. [Music]
