---
layout: default
type: transcript
series: dwarkesh
episode: 11
guest: ""
title: "Some thoughts on the Sutton interview"
source_url: "https://www.youtube.com/watch?v=u3HBJVjpXuw"
analysis_url: /transcripts/dwarkesh/11_some_thoughts_on_the_sutton_interview.analysis/
permalink: /transcripts/dwarkesh/11_some_thoughts_on_the_sutton_interview/
---

# Transcript: Some thoughts on the Sutton interview

Source: https://www.youtube.com/watch?v=u3HBJVjpXuw

---

**[00:00]** Boy, do you guys have a lot of thoughts about the Sun interview. I've been thinking about it myself and I think I have a much better understanding now of Sun's perspective than I did during the interview itself. So, I wanted to

**[00:10]** reflect on how I understand his worldview now. And Richard, apologies if there's still any errors or misunderstandings. It's been very productive to learn from your thoughts. Okay. So, here's my understanding of the

**[00:20]** steelman of Richard's position. Obviously, he wrote the famous essay, the better lesson. And what is this essay about? Well, it's not saying that you just want to throw away as much compute as you possibly can. The bitter

**[00:32]** lesson says that you want to come up with techniques which most effectively and scalably leverage compute. Most of the compute that's spent on an LLM is used in running it during deployment. And yet, it's not learning anything

**[00:44]** during this entire period. It's only learning during the special phase that we call training. And so, this is obviously not an effective use of compute. And what's even worse is that this training period by itself is highly

**[00:56]** inefficient because these models are usually trained on the equivalent of tens of thousands of years of human experience. And what's more, during this training phase, all of their learning is coming straight from human data. Now,

**[01:08]** this is an obvious point in the case of pre-training data, but it's even kind of true for the RLVR that we do with these LLMs. These RL environments are human furnished playgrounds to teach LLMs the specific skills that we have prescribed

**[01:22]** for them. The agent is in no substantial way learning from organic and self-directed engagement with the world. Having to learn only from human data, which is an inelastic and hard tokill resource, is not a scalable way to use

**[01:37]** compute. Furthermore, what these LLMs learn from training is not a true world model which would tell you how the environment changes in response to different actions that you take. Rather, they are building a model of what a

**[01:50]** human would say next. And this leads them to rely on human derived concepts. A way to think about this would be suppose you trained an LLM on all the data up to the year 1900. That LLM probably wouldn't be able to come up

**[02:03]** with relativity from scratch. And maybe here's a more fundamental reason to think this whole paradigm will eventually be superseded. LLMs aren't capable of learning on the job. So we'll need some new architecture to enable

**[02:16]** this kind of continual learning. And once we do have this architecture, we won't need a special training phase. The agents will just be able to learn on the fly like all humans and in fact like all animals are able to do. And this new

**[02:30]** paradigm will render our current approach with LLMs and their special training phase that's super sample inefficient totally obsolete. So that's my understanding of Rich's position. My main difference with Rich is just that I

**[02:43]** don't think the concepts he's using to distinguish LLMs from true intelligence or animal intelligence are actually that mutually exclusive or dichomous. For example, I think imitation learning is continuous with and complimentary to RL

**[02:59]** and relatedly models of humans can give you a prior which facilitates learning quote unquote true world models. I also wouldn't be surprised if some future version of test time fine-tuning could replicate continual learning given that

**[03:13]** we've already managed to accomplish this somewhat with in context learning. So let's start with my claim that imitation learning is continuous with and complimentary to RL. So I tried to ask Richard a couple of times whether

**[03:24]** pre-trained LLMs can serve as a good prior on which we can accumulate the experential learning aka do the RL which would lead to AGI. So Ilas Escover gave a talk a couple months ago that I thought was super interesting and he

**[03:37]** compared pre-training data to fossil fuels and I think this analogy actually has remarkable reach. Just because fossil fuels are not a renewable resource does not mean that our civilization ended up on a dead-end

**[03:50]** track by using them. In fact, they were absolutely crucial. You simply couldn't have transitioned from the water wheels of 1800 to solar panels and fusion power plants. We had to use this cheap, convenient, and plentiful intermediary

**[04:05]** to get to the next step. Alph Go which was conditioned on human games and Alpha Zero which was bootstrapped from scratch were both superhuman Go players. Now of course Alpha Zero was better. So you can ask the question will we or will the

**[04:19]** first AGIS eventually come up with a general learning technique that requires no initialization of knowledge and that just bootstraps itself from the very start and will it outperform the very best AIs that have been trained up to

**[04:32]** that date? I think the answer to both these questions is probably yes. But does this mean that imitation learning must not play any role whatsoever in developing the first AGI or even the first ASI? No. Alph Go is still

**[04:45]** superhuman despite being initially shephered by human player data. The human data isn't necessarily actively detrimental. It's just that at enough scale, it isn't significantly helpful. Alpha Zero also use much more compute

**[04:59]** than AlphaGo. The accumulation of knowledge over tens of thousands of years has clearly been essential to humanity success in any field of knowledge thousands and probably actually millions of previous people

**[05:12]** were involved in building up our understanding and passing it on to the next generation. We obviously didn't invent the language we speak nor the legal system we use. Also even most of the technologies in our phone were not

**[05:25]** directly invented by the people who are alive today. This process is more analogous to imitation learning than it is to RL from scratch. Now, of course, are we literally predicting the next token like an LLM would in order to do

**[05:37]** this cultural learning? No, of course not. So, even the imitation learning that humans are doing is not like the supervised learning that we do for pre-training LLMs. But neither are we running around trying to collect some

**[05:49]** well- definfined scale or reward. No ML learning regime perfectly describes human learning or animal learning. We're doing things which are both analogous to RL and to supervised learning. What planes are to birds, supervised learning

**[06:03]** might end up being to human cultural learning. I also don't think these learning techniques are actually categorically different. Immutation learning is just short horizon RL. The episode is a token long. The LM is

**[06:14]** making a conjecture about the next token based on its understanding of the world and how the different pieces of information in the sequence relate to each other. and it receives reward in proportion to how well it predicted the

**[06:24]** next token. Now, of course, I already hear people saying, "No, no, that's not the ground truth. It's just learning what a human was likely to say." And I agree. But there's a different question which I think is actually more relevant

**[06:36]** to understanding the scalability of these models. And that question is, can we leverage this imitation learning to help models learn better from ground truth? And I think the answer is obviously yes. After RLIing these

**[06:50]** pre-trained base models, we've gotten them to win gold in International Math Olympiad competitions and to code up entire working applications from scratch. Now, these are ground truth examinations. Can you solve this unseen

**[07:03]** Math Olympiad question? Can you build this application to match a specific feature request? But you couldn't have RLED a model to accomplish these tasks from scratch or at least we don't know how to do that yet. You needed a

**[07:16]** reasonable prior over human data in order to kickstart this RL process. Whether you want to call this prior a proper world model or just a model of humans, I don't think is that important. It honestly seems like a semantic debate

**[07:28]** because what you really care about is whether this model of humans helps you start learning from ground truth aka become a true world model. It's a bit like saying to somebody pasteurizing milk, hey, you should stop boiling that

**[07:41]** milk because eventually you want to serve it cold. of course, but this is an intermediate step to facilitate the final output. By the way, LLMs are clearly developing a deep representation of the world because their training

**[07:55]** process is incentivizing them to develop one. I use LLM to teach me about everything from biology to AI to history and they are able to do so with remarkable flexibility and coherence. Now, are LM specifically trained to

**[08:08]** model how their actions will affect the world? No, they are not. But if we're not allowed to call their representations a world model, then we're defining the term world model by the process that we think is necessary

**[08:21]** to build one rather than the obvious capabilities that this concept implies. Okay, continue learning. Um, sorry to bring up my hobby horse again. I'm like a comedian who has only come up with one good bit, but I'm going to milk it for

**[08:34]** all it's worth. An LLM that's being rled on outcomebased awards learns on the order of one bit per episode. and an episode might be tens of thousands of tokens long. Now, obviously, animals and humans are clearly extracting more

**[08:48]** information from interacting with our environment than just the reward signal at the end of an episode. Conceptually, how should we think about what is happening with animals? I think we're learning to model the world through

**[08:59]** observations. This outer loop RL is incentivizing some other learning system to pick up maximum signal from the environment. In Richard's Oak architecture, he calls this the transition model. And if we were trying

**[09:12]** to pigeon hole this feature spec into modern LLMs, what you do is fine-tune on all your observed tokens. From what I hear from my researcher friends, in practice, the most naive way of doing this actually doesn't work very well.

**[09:25]** Now, being able to learn from the environment in a high throughput way is obviously necessary for true AGI, and it clearly doesn't exist with LLMs trained on RLVR. But there might be some other relatively straightforward ways to

**[09:39]** shoehorn continual learning a top LLMs. For example, one could imagine making supervised fine-tuning a tool call for the model. So the outer loop RL is incentivizing the model to teach itself effectively using supervised learning in

**[09:53]** order to solve problems that don't fit in the context window. Now I'm genuinely agnostic about how well techniques like this will work. I'm not an AI researcher, but I wouldn't be surprised if they basically replicate continual

**[10:03]** learning. And the reason is that models are already demonstrating something resembling human continual learning within their context windows. The fact that in context learning emerged spontaneously from the training

**[10:15]** incentive to process long sequences makes me think that if information could just flow across windows longer than the context limit, then models could metalarn the same flexibility that they already show in context. Okay, some

**[10:31]** concluding thoughts. Evolution does meta RL to make an RL agent and that agent can selectively do imitation learning. With LLMs, we're going the opposite way. We have first made this base model that does pure imitation learning and we're

**[10:45]** hoping that we do enough RL on it to make a coherent agent with goals and self-awareness. Maybe this won't work, but I don't think these super first principles arguments about, for example, how these LMS don't

**[10:56]** have a true world model are actually proving much. And I also don't think they're strictly accurate for the models we have today, which are actually undergoing a lot of RL on ground truth. Even if sun's platonic ideal doesn't end

**[11:08]** up being the path to the first AGI, his first principles critique is identifying some genuine basic gaps that these models have. And we don't even notice them because they're so pervasive in the current paradigm. But because he has

**[11:20]** this decadesl long perspective, they're obvious to him. It's the lack of continual learning. It's the abysmal sample efficiency of these models. is their dependence on exhaustible human data. If the LLMs do get to hi first,

**[11:32]** which is what I expect to happen, the successor systems that they build will almost certainly be based on Richard's vision.
