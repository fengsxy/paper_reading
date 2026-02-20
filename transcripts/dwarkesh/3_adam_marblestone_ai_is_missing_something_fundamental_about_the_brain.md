---
layout: default
type: transcript
series: dwarkesh
episode: 3
guest: ""
title: "Adam Marblestone – AI is missing something fundamental about the brain"
source_url: "https://www.youtube.com/watch?v=_9V_Hbe-N1A"
analysis_url: /transcripts/dwarkesh/3_adam_marblestone_ai_is_missing_something_fundamental_about_the_brain.analysis/
permalink: /transcripts/dwarkesh/3_adam_marblestone_ai_is_missing_something_fundamental_about_the_brain/
---

# Transcript: EP3 - Adam Marblestone – AI is missing something fundamental about the brain

Source: https://www.youtube.com/watch?v=_9V_Hbe-N1A

---

**[00:00]** The big million dollar question that I have,
**[00:02]** that I've been trying to get the answer to
**[00:04]** through all these interviews with AI researchers,
**[00:06]** how does the brain do it, right?
**[00:07]** Like, we're doing way more data at these LLMs
**[00:09]** and they still have a small fraction
**[00:11]** of the total capabilities that a human does.
**[00:13]** So what's going on?
**[00:14]** Yeah, I mean, this might be the quadrillion dollar question
**[00:17]** or something like that.
**[00:18]** It's arguably, you could make an argument
**[00:21]** this is the most important question in science.
**[00:24]** I don't claim to know the answer.
**[00:27]** I also don't really think that the answer
**[00:30]** will necessarily come even from a lot of smart people
**[00:34]** thinking about it as much as they are.
**[00:35]** My overall meta-level take
**[00:37]** is that we have to empower the field of neuroscience
**[00:40]** to just make neuroscience a more powerful field
**[00:44]** technologically and otherwise
**[00:45]** to actually be able to crack a question like this.
**[00:48]** But maybe the way that we would think about this now
**[00:53]** with modern AI, neural nets, deep learning
**[00:56]** is that there's sort of these certain key components of that.
**[01:00]** There's the architecture,
**[01:02]** there's maybe hyperparameters of the architecture.
**[01:04]** How many layers do you have
**[01:05]** or sort of properties of that architecture?
**[01:07]** There is the learning algorithm itself.
**[01:10]** How do you train it?
**[01:11]** Back prop, gradient descent.
**[01:13]** Is it something else?
**[01:15]** There is, how is it initialized?
**[01:17]** Okay, so if we take the learning part of the system,
**[01:19]** it still may have some initialization of the weights.
**[01:25]** And then there are also cost functions.
**[01:27]** There's like, what is it being trained to do?
**[01:28]** What's the reward signal?
**[01:29]** What are the loss functions, supervision signals?
**[01:32]** My personal hunch within that framework
**[01:36]** is that the field has neglected
**[01:39]** the role of this very specific loss functions,
**[01:42]** very specific cost functions.
**[01:45]** Machine learning tends to like mathematically
**[01:47]** simple loss functions, right?
**[01:50]** Predict the next token, you know, cross entropy,
**[01:54]** these simple kind of computer scientists loss functions.
**[01:57]** I think evolution may have built a lot of complexity
**[02:00]** into the loss functions.
**[02:01]** Actually, many different loss functions
**[02:02]** were different areas turned on
**[02:04]** at different stages of development.
**[02:06]** A lot of Python code, basically,
**[02:09]** generating a specific curriculum
**[02:11]** for what different parts of the brain need to learn.
**[02:13]** Because evolution has seen many times
**[02:15]** what was successful and unsuccessful
**[02:16]** and evolution could encode the knowledge
**[02:18]** of the learning curriculum.
**[02:20]** So in the machine learning framework,
**[02:22]** maybe we can come back and we can talk about
**[02:24]** where do the loss functions of the brain come from?
**[02:27]** Can different loss functions
**[02:28]** lead to different efficiency of learning?
**[02:31]** You know, people say like the cortex
**[02:33]** has got the universal human learning algorithm,
**[02:35]** the special skills that humans have.
**[02:36]** What's up with that?
**[02:37]** Well, this is a huge question and we don't know.
**[02:39]** I've seen models where what the cortex,
**[02:42]** you know, the cortex has typically
**[02:44]** this like six layered structure,
**[02:45]** layers in a slightly different sense
**[02:46]** than layers of a neural net.
**[02:48]** It's like any one location in the cortex
**[02:50]** has six physical layers of tissue
**[02:52]** as you go in layers of the sheet.
**[02:54]** And then those areas then connect to each other
**[02:57]** and that's more like the layers of a network.
**[03:00]** I've seen versions of that
**[03:02]** where what you're trying to explain
**[03:04]** is actually just how does it approximate backprop
**[03:07]** and what is the cost function for that?
**[03:09]** What is the network being asked to do?
**[03:11]** If you sort of are trying to say
**[03:12]** it's something like backprop,
**[03:13]** is it doing backprop on next token prediction?
**[03:15]** Is it doing backprop on classifying images
**[03:18]** or what is it doing?
**[03:21]** And no one knows,
**[03:24]** but I think one thought about it,
**[03:26]** one possibility about it
**[03:27]** is that it's just this incredibly general prediction engine.
**[03:32]** So any one area of cortex is just trying to predict
**[03:39]** any, basically can it learn to predict
**[03:40]** any subset of all the variables it sees
**[03:42]** from any other subset.
**[03:44]** So like omni-directional inference
**[03:48]** or omni-directional prediction.
**[03:51]** Whereas an LLM is just,
**[03:52]** you see everything in the context window
**[03:53]** and then it computes a very particular
**[03:56]** conditional probability,
**[03:57]** which is given all the last thousands of things,
**[03:59]** what is the very probabilities for all the next token?
**[04:04]** But it would be weird for a large language model to say,
**[04:08]** the quick brown fox, blank, blank, the lazy dog
**[04:13]** and fill in the middle versus do the next token.
**[04:18]** If it's doing just forward,
**[04:21]** it can learn how to do that stuff in this emergent level
**[04:23]** of in context learning,
**[04:24]** but natively is just predicting the next token.
**[04:27]** What if the cortex is just natively made
**[04:30]** so that it can,
**[04:31]** any area of cortex can predict any pattern
**[04:34]** in any subset of its inputs
**[04:35]** given any other missing subsets.
**[04:38]** That is a little bit more like
**[04:40]** quote unquote probabilistic AI.
**[04:43]** I think a lot of the things I'm saying by the way
**[04:45]** are extremely similar to like what Yann LeCun would say.
**[04:48]** He's really interested in these energy-based models
**[04:51]** and something like that is like the joint distribution
**[04:53]** of all the variables.
**[04:55]** What is the likelihood or unlikelihood
**[04:58]** of just any combination of variables?
**[05:01]** And if I clamp some of them, I say,
**[05:02]** well, definitely these variables are in these states,
**[05:05]** then I can compute with probabilistic sampling,
**[05:09]** for example, I can compute, okay,
**[05:11]** conditioned on these being set in this state,
**[05:14]** what are, and these could be any arbitrary subset
**[05:17]** of variables in the model.
**[05:20]** Can I predict what any other subset is gonna do
**[05:23]** and sample from any other subset given clamping this subset?
**[05:25]** And I could choose a totally different subset
**[05:27]** and sample from that subset.
**[05:29]** So it's omnidirectional inference.
**[05:31]** And so, that could be,
**[05:33]** there's some parts of cortex
**[05:34]** that might be like association areas of cortex
**[05:36]** that may predict vision from audition.
**[05:39]** There might be areas that predict things
**[05:42]** that the more innate part of the brain is gonna do.
**[05:45]** Because remember, this whole thing is basically riding
**[05:46]** on top of the sort of a lizard brain
**[05:48]** and lizard body, if you will.
**[05:51]** And that thing is a thing that's worth predicting too.
**[05:53]** So you're not just predicting,
**[05:54]** do I see this or do I see that?
**[05:55]** But is this muscle about to tense?
**[05:57]** Am I about to have a reflex where I laugh?
**[06:01]** Is my heart rate about to go up?
**[06:03]** Am I about to activate this instinctive behavior?
**[06:06]** Based on my higher level understanding of,
**[06:09]** I can match,
**[06:11]** somebody has told me there's a spider on my back
**[06:14]** to this lizard part that would activate
**[06:17]** if I was literally seeing a spider in front of me.
**[06:21]** And you learn to associate the two.
**[06:22]** So that even just from somebody hearing you say,
**[06:25]** there's a spider on your back.
**[06:25]** Yeah, well, let's come back to this.
**[06:27]** And this is partly having to do with Steve Birn's theories,
**[06:30]** which I'm recently obsessed about.
**[06:31]** But on your podcast with Ilya,
**[06:35]** he said, look, I'm not aware of any good theory
**[06:38]** of how evolution encodes high level desires or intentions.
**[06:45]** I think this is very connected to all of these questions
**[06:50]** about the loss functions and the cost functions
**[06:53]** that the brain would use.
**[06:54]** And it's a really profound question, right?
**[06:56]** Like, let's say that
**[06:58]** that I am embarrassed for saying the wrong thing
**[07:04]** on your podcast,
**[07:05]** because I'm imagining that Yann LeCun is listening
**[07:07]** and he says, that's not my theory.
**[07:09]** You described energy-based models really badly.
**[07:12]** That's going to activate in me innate embarrassment
**[07:16]** and shame, and I'm going to want to go hide and whatever.
**[07:18]** And that's going to activate these innate reflexes.
**[07:22]** And that's important because I might otherwise get killed
**[07:24]** by Yann LeCun's marauding army of other-
**[07:28]** The French AI researcher is coming for you, Adam.
**[07:30]** And so it's important that I have that instinctual response.
**[07:33]** But of course, evolution has never seen Yann LeCun
**[07:35]** or known about energy-based models
**[07:36]** or known what an important scientist or a podcast is.
**[07:41]** And so somehow the brain has to encode this desire
**[07:45]** to not piss off really important people in the tribe
**[07:49]** or something like this in a very robust way
**[07:54]** without knowing in advance all the things
**[07:56]** that the learning subsystem of the brain,
**[07:59]** the part that is learning, cortex and other parts,
**[08:03]** the cortex is going to learn this world model.
**[08:05]** It's going to include things like Yann LeCun and podcasts.
**[08:09]** And evolution has to make sure that those neurons,
**[08:13]** whatever the Yann LeCun being upset with me neurons,
**[08:16]** get properly wired up to the shame response
**[08:18]** or this part of the reward function.
**[08:23]** And this is important, right?
**[08:23]** Because if we're going to be able to seek status in the tribe
**[08:25]** or learn from knowledgeable people, as you said,
**[08:27]** or things like that,
**[08:28]** exchange knowledge and skills with friends,
**[08:30]** but not with enemies,
**[08:31]** I mean, we have to learn all this stuff.
**[08:33]** So it has to be able to robustly wire
**[08:34]** these learned features of the world,
**[08:37]** learn parts of the world model
**[08:38]** up to these innate reward functions,
**[08:42]** and then actually use that to then learn more, right?
**[08:44]** Because next time I'm not going to try to piss off Yann LeCun
**[08:46]** if he emails me that I got this wrong.
**[08:50]** And so we're going to do further learning based on that.
**[08:53]** So in constructing the reward function,
**[08:56]** it has to use learned information,
**[08:57]** but how can evolution,
**[08:59]** evolution didn't know about Yann LeCun,
**[09:01]** so how can it do that?
**[09:03]** And so the basic idea that Steve Burns is proposing
**[09:08]** is that, well, part of the cortex
**[09:10]** or other areas like the amygdala that learn,
**[09:13]** what they're doing is they're modeling
**[09:15]** the steering subsystem.
**[09:16]** The steering subsystem is the part
**[09:17]** with these more innately programmed responses
**[09:19]** and the innate programming of these series
**[09:21]** of reward functions, cost functions, bootstrapping,
**[09:24]** functions that exist.
**[09:26]** So there are parts of the amygdala, for example,
**[09:27]** that are able to monitor what those parts do
**[09:29]** and predict what those parts do.
**[09:31]** So how do you find the neurons
**[09:35]** that are important for social status?
**[09:37]** Well, you have some innate heuristics of social status,
**[09:39]** for example, or you have some innate heuristics
**[09:42]** of friendliness that the steering subsystem can use.
**[09:47]** And the steering subsystem actually has
**[09:49]** its own sensory system, which is kind of crazy.
**[09:51]** So we think of vision as being something
**[09:53]** that the cortex does, but there's also
**[09:55]** a steering subsystem subcortical visual system
**[09:58]** called the superior colliculus with innate ability
**[10:01]** to detect faces, for example, or threats.
**[10:06]** So there's a visual system that has innate heuristics
**[10:10]** and that the steering subsystem has its own responses.
**[10:13]** So there'll be part of the amygdala
**[10:14]** or part of the cortex that is learning
**[10:15]** to predict those responses.
**[10:17]** And so what are the neurons that matter
**[10:19]** in the cortex for social status or for friendship?
**[10:22]** Or they're the ones that predicts
**[10:24]** those innate heuristics for friendship, right?
**[10:26]** So you train a predictor in the cortex
**[10:28]** and you say, which neurons are part of the predictor?
**[10:32]** Those are the ones that are,
**[10:33]** now you've actually managed to wire it up.
**[10:35]** Yeah.
**[10:36]** This is fascinating.
**[10:38]** I feel like I still don't understand.
**[10:40]** I understand how the cortex could learn
**[10:43]** how this primitive part of the brain would respond to...
**[10:49]** So it can obviously, it has these labels on,
**[10:51]** here's literally a picture of a spider and this is bad,
**[10:55]** like be scared of this.
**[10:56]** And then the cortex learns that this is bad
**[10:58]** because the innate part tells it that.
**[11:00]** But then it has to generalize to,
**[11:03]** okay, the spider's on my back
**[11:05]** and somebody's telling me the spider's on your back,
**[11:06]** that's also bad.
**[11:07]** But it never got supervision on that.
**[11:10]** So how does it?
**[11:11]** Well, it's because the learning subsystem
**[11:15]** is a powerful learning algorithm
**[11:16]** that does have generalization,
**[11:18]** that is capable of generalization.
**[11:20]** So the steering subsystem,
**[11:22]** these are the innate responses.
**[11:23]** So you're going to have some,
**[11:24]** let's say built into your steering subsystem,
**[11:28]** these lower brain areas, hypothalamus, brainstem, et cetera.
**[11:31]** And again, they include,
**[11:32]** they have their own primitive sensory systems.
**[11:35]** So there may be an innate response.
**[11:38]** If I see something that's kind of moving fast
**[11:41]** toward my body that I didn't previously see was there
**[11:44]** and it's kind of small and dark and high contrast,
**[11:46]** that might be an insect kind of skittering onto my body.
**[11:49]** I am going to like flinch, right?
**[11:53]** And so there are these innate responses.
**[11:54]** And so there's going to be some group of neurons,
**[11:56]** let's say in the hypothalamus,
**[11:58]** that is that I am flinching or I just flinched, right?
**[12:02]** I just flinched at neurons in the hypothalamus.
**[12:05]** So when you flinch, first of all,
**[12:07]** that a negative contribution to the reward function,
**[12:09]** you didn't want that to happen perhaps,
**[12:12]** but that's a reward function then
**[12:14]** that doesn't have any generalization in it.
**[12:16]** So I'm going to avoid that exact situation
**[12:18]** of the thing skittering toward me.
**[12:21]** And maybe I'm going to avoid some actions
**[12:22]** that lead to the thing skittering.
**[12:24]** So that's something, a generalization you can get,
**[12:26]** what Steve calls it is downstream of the reward function.
**[12:29]** So I'm going to avoid the situation
**[12:31]** where the spider was skittering toward me.
**[12:34]** But you're also going to do something else.
**[12:35]** So there's going to be like a part of your amygdala say
**[12:38]** that is saying, okay, a few milliseconds,
**[12:44]** hundreds of milliseconds or seconds earlier,
**[12:49]** could I have predicted that flinching response?
**[12:51]** It's going to be a group of neurons
**[12:52]** that is essentially a classifier of am I about to flinch?
**[12:56]** And I'm going to have classifiers for that
**[12:57]** for every important steering subsystem variable
**[12:59]** that evolution needs to take care of.
**[13:01]** Am I about to flinch?
**[13:02]** Am I talking to a friend?
**[13:03]** Should I laugh now?
**[13:04]** Is the friend high status?
**[13:06]** Whatever variables the hypothalamus brainstem contain,
**[13:09]** am I about to taste salt?
**[13:12]** So there's going to have all these variables.
**[13:14]** And for each one, it's going to have a predictor.
**[13:15]** It's going to train that predictor.
**[13:17]** Now the predictor that it trains,
**[13:19]** that can have some generalization.
**[13:20]** And the reason it can have some generalization
**[13:22]** is because it just has a totally different input.
**[13:23]** So its input data might be things like the word spider,
**[13:28]** right, but the word spider can activate
**[13:29]** in all sorts of situations that lead
**[13:31]** to the word spider activating in your world model.
**[13:35]** So, you know, if you have a complex world model,
**[13:38]** which really complex features,
**[13:39]** that inherently gives you some generalization.
**[13:41]** It's not just the thing skittering toward me.
**[13:42]** It's even the word spider or the concept of spider
**[13:45]** is going to cause that to trigger.
**[13:47]** And this predictor can learn that.
**[13:48]** So whatever spider neurons are in my world model,
**[13:52]** which could even be a book about spiders
**[13:55]** or somewhere, a room where there are spiders
**[13:57]** or whatever that is.
**[13:58]** The amount of heebie-jeebies that this conversation
**[14:01]** is eliciting in the audience is like.
**[14:03]** So now I'm activating your steering subsystem.
**[14:05]** Your steering subsystem spider hypothalamus,
**[14:08]** a subgroup of neurons of skittering insect
**[14:11]** are activating based on these very abstract concepts
**[14:13]** in the conversation.
**[14:14]** If we keep going, I'm going to have to put
**[14:15]** in a trigger warning.
**[14:17]** That's because you learned this.
**[14:18]** And the cortex inherently has the ability to generalize
**[14:21]** because it's just predicting
**[14:22]** based on these very abstract variables
**[14:24]** and all these integrated information that it has.
**[14:26]** Whereas the steering subsystem only can use
**[14:29]** whatever the superior colliculus
**[14:30]** and a few other sensors can spit out.
**[14:32]** By the way, it's remarkable that the person
**[14:33]** who's made this connection between different pieces
**[14:36]** of neuroscience, Stephen Burns,
**[14:37]** like former physicist for the last few years
**[14:40]** has been trying to synthesize.
**[14:41]** He's an AI safety researcher.
**[14:42]** He's just synthesizing.
**[14:42]** This comes back to the academic incentives thing.
**[14:44]** I think that this is a little bit hard to say,
**[14:47]** what's the exact next experiment?
**[14:48]** How am I going to publish a paper on this?
**[14:50]** How am I going to train my grad student to do this?
**[14:51]** It's very, very speculative.
**[14:53]** But there's a lot in the neuroscience literature
**[14:54]** and Stephen has been able to pull this together.
**[14:56]** And I think that Steve has an answer
**[14:57]** to Elio's question essentially,
**[14:58]** which is how does the brain ultimately code
**[15:01]** for these higher level desires
**[15:03]** and link them up to the more primitive rewards?
**[15:05]** Yeah.
**[15:06]** Very naive question.
**[15:07]** But why can't we achieve this omnidirectional inference
**[15:10]** by just training the model
**[15:13]** to not just map from a token to next token,
**[15:16]** but remove the masks in the training
**[15:19]** so it maps every token to every token
**[15:21]** or come up with more labels between video and audio
**[15:26]** and text so that it's forced to map one to each one?
**[15:30]** I mean, that may be the way.
**[15:32]** So it's not clear to me.
**[15:35]** Some people think that there's sort of a different way
**[15:39]** that it does probabilistic inference
**[15:41]** or a different learning algorithm that isn't backprop.
**[15:44]** There might be other ways of learning energy-based models
**[15:46]** or other things like that that you can imagine
**[15:48]** but that is involved in being able to do this
**[15:51]** and that the brain has that.
**[15:52]** But I think there's a version of it where
**[15:54]** what the brain does is like crappy versions of backprop
**[15:57]** to learn to predict through a few layers.
**[16:01]** And that, yeah, it's kind of like
**[16:02]** a multimodal foundation model.
**[16:04]** Yeah, so maybe the cortex is just kind of like
**[16:07]** certain kinds of foundation models.
**[16:09]** LLMs are maybe just predicting the next token
**[16:11]** but vision models maybe are trained
**[16:14]** in learning to fill in the blanks
**[16:15]** or reconstruct different pieces or combinations.
**[16:17]** But I think that it does it in an extremely flexible way.
**[16:20]** So if you train a model to just fill in this blank
**[16:23]** at the center, okay, that's great.
**[16:25]** But what if you didn't train it to fill in
**[16:27]** this other blank over to the left,
**[16:29]** then it doesn't know how to do that.
**[16:30]** It's not part of its repertoire of predictions
**[16:33]** that are like amortized into the network.
**[16:35]** Whereas with a really powerful inference system,
**[16:37]** you could choose at test time,
**[16:41]** what is the subset of variables it needs to infer
**[16:45]** and which ones are clamped.
**[16:46]** Okay, so two sub questions.
**[16:48]** One, it makes you wonder whether
**[16:51]** the thing that is lacking in artificial neural networks
**[16:54]** is less about the order function
**[16:55]** and more about the encoder or the embedding,
**[17:00]** which like maybe the issue is that
**[17:04]** you're not representing video and audio and text
**[17:08]** in the right latent abstraction
**[17:11]** such that they could intermingle and conflict.
**[17:16]** Maybe this is also related to why
**[17:18]** LLM seem bad at drawing connections
**[17:19]** between different ideas.
**[17:20]** It's like, are the ideas represented
**[17:22]** at a level of generality at which you could notice
**[17:26]** different connections.
**[17:26]** Well, the problem is these questions are all commingled.
**[17:28]** So if we don't know if it's doing a back prop like learning
**[17:30]** and we don't know if it's doing energy-based models
**[17:32]** and we don't know how these areas
**[17:33]** are even connected in the first place,
**[17:34]** it's like very hard to like really get
**[17:36]** to the ground truth of this.
**[17:38]** But yeah, it's possible.
**[17:39]** I mean, I think that people have done some work.
**[17:41]** My friend Joel DiPello actually did something
**[17:43]** some years ago where I think he put a model.
**[17:49]** I think it was a model of V1 of sort of specifically
**[17:53]** how the early visual cortex represents images
**[17:56]** and put that as like an input into like a ConvNet
**[17:59]** and that like improved something.
**[18:01]** So it could be like differences.
**[18:02]** The retina is also doing, you know,
**[18:04]** motion detection and certain things
**[18:07]** are kind of getting filtered out.
**[18:08]** So there may be some pre-processing of the sensory data.
**[18:11]** There may be some clever combinations
**[18:13]** of which modalities are predicting which
**[18:14]** or so on that lead to better representation.
**[18:18]** There may be much more clever things than that.
**[18:19]** Some people certainly do think that there's inductive biases
**[18:22]** built into the architecture that will shape
**[18:25]** the representations, you know, differently
**[18:26]** or that there are clever things that you can do.
**[18:29]** So Astera, which is the same organization
**[18:32]** that employs Steve Burns,
**[18:33]** just launched this neuroscience project
**[18:34]** based on Doris So's work.
**[18:37]** And she has some ideas about how you can build
**[18:42]** vision systems that basically require less training.
**[18:44]** They put in, they in-build into the assumptions
**[18:47]** of the design of the architecture
**[18:50]** that things like objects are bounded by surfaces
**[18:54]** and the surfaces have certain types of shapes
**[18:56]** and relationships of how they occlude each other
**[18:59]** and stuff like that.
**[19:00]** So it may be possible to build more assumptions
**[19:02]** into the network.
**[19:03]** Evolution may have also put some changes of architecture.
**[19:08]** It's just, I think that also the cost functions
**[19:10]** and so on may be a key thing that it does.
**[19:14]** So Andy Jones has this amazing 2021 paper
**[19:16]** where he uses AlphaZero to show that you can trade off
**[19:19]** test time compute and training compute.
**[19:21]** And while that might seem obvious now,
**[19:23]** this was three years before people were talking
**[19:25]** about inference scaling.
**[19:26]** So this got me thinking,
**[19:27]** is there an experiment you could run today,
**[19:29]** even if it's a toy experiment,
**[19:31]** which would help you anticipate the next scaling paradigm.
**[19:34]** One idea I had was to see if there was anything
**[19:36]** to multi-agent scaling.
**[19:37]** Basically, if you have a fixed budget of training compute,
**[19:39]** are you gonna get the smartest agent by dumping all of it
**[19:42]** into training one single agent
**[19:44]** or by splitting that compute up amongst a bunch of models,
**[19:47]** resulting in a diversity of strategies
**[19:49]** that get to play off each other?
**[19:50]** I didn't know how to turn this question
**[19:51]** into a concrete experiment though.
**[19:53]** So I started brainstorming with Gemini 3 Pro
**[19:55]** in the Gemini app.
**[19:56]** Gemini helped me think through
**[19:58]** a bunch of different judgment calls.
**[19:59]** For example, how do you turn the training loop
**[20:01]** from self-play to this kind of co-evolutionary training?
**[20:05]** How do you initialize and then maintain diversity
**[20:08]** amongst different AlphaZero agents?
**[20:10]** How do you even split up the compute
**[20:12]** between these agents in the first place?
**[20:13]** I found this clean implementation of AlphaGo Zero,
**[20:16]** which I then forked and opened up in Antigravity,
**[20:19]** which is Google's agent-first IDE.
**[20:22]** The code was originally written in 2017
**[20:24]** and it was meant to be trained on a single GPU of that time.
**[20:28]** But I needed to train multiple whole separate populations
**[20:31]** of AlphaZero agents.
**[20:33]** So I needed to speed things up.
**[20:34]** I rented a beefcake of a GPU node,
**[20:36]** but I needed to refactor the whole implementation
**[20:39]** to take advantage of all this scale and parallelism.
**[20:41]** Gemini suggested two different ways to parallelize self-play.
**[20:44]** One which would involve higher GPU context switching
**[20:47]** and the other would involve higher communication overhead.
**[20:50]** I wasn't sure which one to pick, so I just asked Gemini.
**[20:53]** And not only did it get both of them working in minutes,
**[20:55]** but it autonomously created
**[20:57]** and then ran a benchmark to see which one was best.
**[21:00]** It would have taken me a week
**[21:01]** to implement either one of these options.
**[21:03]** Think about how many judgment calls
**[21:05]** a software engineer working on
**[21:06]** an actually complex project has to make.
**[21:08]** If they have to spend weeks
**[21:09]** architecting some optimization or feature
**[21:12]** before they can see whether it will work out,
**[21:14]** they will just get to test out so many fewer ideas.
**[21:16]** Anyways, with all this help from Gemini,
**[21:18]** I actually ran the experiment and got some results.
**[21:20]** Now, please keep in mind that I'm running this experiment
**[21:23]** on an anemic budget of compute,
**[21:24]** and it's very possible I made some mistakes
**[21:26]** in implementation, but it looks like there can be gains
**[21:30]** from splitting up a fixed budget of training compute
**[21:34]** amongst multiple agents,
**[21:35]** rather than just dumping it all into one.
**[21:37]** Just to reiterate how surprising this is,
**[21:39]** the best agent in the population of 16
**[21:42]** is getting 116th the amount of training compute
**[21:45]** as the agent trained on self-play alone.
**[21:48]** And yet it still outperforms the agent
**[21:50]** that is hogging all of the compute.
**[21:52]** The whole process of vibe coding this experiment
**[21:55]** with Gemini was really absorbing and fun.
**[21:58]** It gave me the chance to actually understand
**[22:00]** how AlphaZero works and to understand the design space
**[22:04]** around decisions about the hyperparameters
**[22:07]** and how search is done
**[22:08]** and how you do this kind of co-evolutionary training,
**[22:11]** rather than getting bogged down
**[22:13]** in my very novice abilities as an engineer.
**[22:15]** Go to gemini.google.com to try it out.
**[22:20]** I wanna talk about this idea that you just glance off of,
**[22:23]** which was amortized inference.
**[22:27]** And maybe I should try to explain what I think it means
**[22:33]** because I think it's probably wrong
**[22:34]** and this will help you correct me.
**[22:36]** It's been a few years for me too.
**[22:37]** Okay.
**[22:39]** Right now, the way the models work is you have an input,
**[22:42]** it maps it to an output.
**[22:44]** And this is amortizing a process that the real process,
**[22:50]** which we think is like what intelligence is,
**[22:52]** which is like, you have some prior
**[22:55]** over how the world could be.
**[22:57]** Like, what are the causes that make the world
**[22:59]** the way that it is?
**[23:00]** And then when you see some observation,
**[23:03]** you should be like, okay,
**[23:04]** here's all the ways the world could be.
**[23:07]** This cause explains what's happening best.
**[23:10]** Now, doing this calculation over every possible cause
**[23:15]** is computationally intractable.
**[23:16]** So then you just have to sample like,
**[23:19]** oh, here's a potential cause.
**[23:20]** Does this explain this observation?
**[23:23]** No, forget it, let's keep sampling.
**[23:25]** And then eventually you get the cause,
**[23:27]** the cause explains the observation
**[23:31]** and then this becomes your posterior.
**[23:33]** That's actually pretty good, I think, of sort of, yeah.
**[23:36]** Bayesian inference, like in general,
**[23:37]** is like of this very intractable thing.
**[23:40]** The algorithms that we have for doing that
**[23:41]** tend to require taking a lot of samples,
**[23:43]** Monte Carlo methods, taking a lot of samples.
**[23:46]** And taking samples takes time.
**[23:49]** I mean, this is like the original like Boltzmann machines
**[23:51]** and stuff we're using, techniques like this.
**[23:55]** And still it's used with probabilistic programming,
**[23:57]** other types of methods often.
**[23:58]** And so, yeah, so the Bayesian inference problem,
**[24:02]** which is like basically the problem of like perception,
**[24:04]** like given some model of the world and given some data,
**[24:06]** like how should I update my,
**[24:08]** what are the like the variables,
**[24:10]** missing variables in my internal model?
**[24:13]** And I guess the idea is that neural networks
**[24:16]** are hopefully, obviously there's mechanistically,
**[24:20]** the neural network is not starting with like,
**[24:23]** here is my model of the world
**[24:25]** and I'm gonna try to explain this data.
**[24:27]** But the hope is that instead of starting with,
**[24:30]** hey, does this cause explain this observation?
**[24:32]** No, did this cause explain this explanation?
**[24:34]** Yes, what you do is just like observation.
**[24:37]** What's the cause that the neural net thinks is the best one?
**[24:40]** Observation to cause.
**[24:41]** So the feed forward like goes observation to cause.
**[24:43]** Observation to cause.
**[24:44]** To the output.
**[24:45]** Yes, you don't have to evaluate all these energy values
**[24:48]** or whatever and sample around to make them higher and lower.
**[24:51]** You just say approximately that process
**[24:55]** would result in this being the top one
**[24:57]** or something like that.
**[24:58]** Yeah, one way to think about it might be that
**[25:01]** test time compute, inference time compute
**[25:03]** is actually doing this sampling again.
**[25:06]** Because you literally read it's shade of thought.
**[25:08]** It's like actually doing this toy example
**[25:11]** we're talking about where it's like,
**[25:12]** oh, can I solve this problem by doing X?
**[25:13]** Yeah, I need a different approach.
**[25:16]** And this raises the question, I mean,
**[25:18]** over time it is the case that the capabilities
**[25:19]** which were required inference time compute to elicit
**[25:25]** get distilled into the model.
**[25:26]** So you're amortizing the thing,
**[25:28]** which previously you needed to do these like rollouts,
**[25:30]** like Monte Carlo rollouts to figure out.
**[25:33]** And so in general, maybe there's this principle of
**[25:36]** digital minds, which can be copied,
**[25:38]** have different trade-offs, which are relevant
**[25:40]** than biological minds, which cannot.
**[25:43]** And so in general, it should make sense
**[25:44]** to amortize more things,
**[25:45]** because you can literally copy the amortization, right?
**[25:48]** Or copy the things that you have sort of like built in.
**[25:52]** And this is a tangential question
**[25:54]** where it might be interesting to speculate about
**[25:56]** in the future as these things can become more intelligent
**[25:59]** and the way we train them becomes more
**[26:02]** economically rational,
**[26:04]** what will make sense to amortize into these minds,
**[26:08]** which evolution did not think it was worth amortizing
**[26:11]** into biological minds, you have to retrain every time.
**[26:14]** I mean, first of all,
**[26:15]** I think the probabilistic AI people would be like,
**[26:16]** of course you need test time compute
**[26:18]** because this inference problem is really hard.
**[26:21]** And the only ways we know how to do it
**[26:22]** involve lots of test time compute.
**[26:24]** Otherwise it's just this crappy approximation
**[26:25]** that's never gonna like,
**[26:26]** you have to do infinite data or something to like make this.
**[26:29]** So I think that some of the probabilistic people
**[26:30]** will be like, no, it's like inherently probabilistic
**[26:32]** and like amortizing it in this way,
**[26:34]** like just doesn't make sense.
**[26:35]** And so, and they might then also point to the brain
**[26:37]** and say, okay, well, the brain,
**[26:38]** the neurons are kind of stochastic and they're sampling
**[26:40]** and they're doing things.
**[26:41]** And so maybe the brain actually is doing more
**[26:43]** like the non-amortized inference, the real inference.
**[26:48]** But it's also kind of strange how perception can work
**[26:50]** in just like milliseconds or whatever.
**[26:52]** It doesn't seem like it uses that much sampling.
**[26:53]** So it's also clearly also doing some kind of baking things
**[26:57]** into like approximate forward passes
**[27:00]** or something like that to do this.
**[27:01]** And yeah, so in the future, I don't know.
**[27:06]** I mean, I think,
**[27:10]** is it already a trend to some degree
**[27:11]** that things that are people
**[27:12]** who are having to use test time compute for
**[27:14]** are getting like used to train back the base model?
**[27:19]** Right?
**[27:20]** Yeah.
**[27:21]** So now it can do it in one pass.
**[27:23]** Yeah, so I mean, I think,
**[27:25]** yeah, maybe evolution did or didn't do that.
**[27:29]** I think evolution still has to pass everything
**[27:31]** through the genome, right?
**[27:33]** To build the network so,
**[27:34]** and the environment in which humans are living
**[27:36]** is very dynamic, right?
**[27:39]** And so maybe that's, if we believe this is true,
**[27:42]** that there's a learning subsystem,
**[27:44]** Percy Burns, and a steering subsystem,
**[27:46]** that the learning subsystem doesn't have a lot of
**[27:48]** like pre-initialization or pre-training.
**[27:51]** It has a certain architecture,
**[27:52]** but then within lifetime it learns.
**[27:55]** Then evolution didn't actually like amortize
**[27:57]** that much into that network.
**[27:59]** It amortized it instead of innate behaviors
**[28:02]** in a set of these bootstrapping cost functions
**[28:04]** or ways of building up very particular reward signals.
**[28:08]** Yeah.
**[28:09]** This framework helps explain this mystery
**[28:12]** that people have pointed out
**[28:13]** and I've asked a few guests about,
**[28:15]** which is if you want to analogize evolution to pre-training,
**[28:20]** well, how do you explain the fact that so little information
**[28:23]** is conveyed through the genome?
**[28:25]** So three gigabytes is the size of the total human genome.
**[28:28]** Obviously a small fraction of that is actually relevant
**[28:29]** to coding at the brain.
**[28:32]** And if previously people made this analogy
**[28:35]** that actually evolution has found the hyperparameters
**[28:38]** of the model, the numbers which tell you
**[28:41]** how many layers should there be,
**[28:42]** the architecture basically, right?
**[28:43]** Like how should things be wired together?
**[28:45]** But if a big part of the story
**[28:47]** that increases the sample efficiency,
**[28:49]** aids learning, generally makes systems more performant,
**[28:52]** is the reward function, is the loss function,
**[28:55]** and if evolution found those loss functions,
**[28:58]** which aid learning,
**[29:01]** then it actually kind of makes sense
**[29:01]** how you can build an intelligence
**[29:04]** with so little information,
**[29:06]** because the reward function,
**[29:07]** oh, you write in Python, right?
**[29:09]** The reward function is literally a line.
**[29:11]** And so you just have a thousand lines like this
**[29:13]** and that doesn't take up that much space.
**[29:15]** Yes, and it also gets to do this generalization thing
**[29:18]** with the thing I was describing
**[29:19]** where we were talking about the spider, right?
**[29:21]** Of where it learns that just the word spider
**[29:23]** triggers the spider reflex or whatever.
**[29:27]** It gets to exploit that too, right?
**[29:30]** So it gets to build a reward function
**[29:31]** that actually has a bunch of generalization in it,
**[29:33]** just by specifying these innate spider stuff
**[29:35]** and the thought assessors as Steve calls them
**[29:37]** that do the learning.
**[29:38]** So that's like potentially a really compact solution
**[29:42]** to building up these more complex reward functions too
**[29:44]** that you need.
**[29:45]** So it doesn't have to anticipate everything
**[29:46]** about the future of the reward function,
**[29:48]** just has to anticipate what variables are relevant
**[29:49]** and what are heuristics for like finding
**[29:51]** what those variables are.
**[29:53]** And then, yeah, so then it has to have
**[29:54]** like a very compact specification
**[29:56]** for like the learning algorithm
**[29:57]** and basic architecture of the learning subsystem.
**[30:00]** And then it has to specify all this Python code of like all the stuff about the spiders
**[30:04]** and all the stuff about friends and all the stuff about your mother and all the stuff
**[30:07]** about mating and social groups and joint eye contact.
**[30:12]** It has to specify all that stuff.
**[30:15]** And so is this really true?
**[30:16]** And so I think that there is some evidence for it.
**[30:21]** So Fei Chen and Evan McCosko and various other researchers who have been doing like these
**[30:26]** single-cell atlases.
**[30:27]** So one of the things that neuroscience technology or scaling up neuroscience technology, again,
**[30:33]** this is kind of like one of my obsessions, has done through the Brain Initiative, a big
**[30:41]** neuroscience funding program, is they've basically gone through different areas, especially the
**[30:45]** mouse brain, and mapped like where are the different cell types?
**[30:50]** How many different types of cells are there in different areas of cortex?
**[30:53]** Are they the same across different areas?
**[30:55]** And then you look at these subcortical regions, which are more like the like steering subsystem
**[30:59]** or reward function generating regions.
**[31:02]** How many different types of cells do they have and which neurons types do they have?
**[31:05]** We don't know how they're all connected and exactly what they do or what the circuits
**[31:09]** are, what they mean, but you can just like quantify like how many different kinds of
**[31:12]** cells are there with sequencing the RNA.
**[31:18]** And there are a lot more weird and diverse and bespoke cell types in the steering subsystem
**[31:25]** basically than there are in the learning subsystem.
**[31:27]** Like the cortical cell types, there's enough to build, it seems like there's enough to
**[31:30]** build a learning algorithm up there and specify some hyperparameters.
**[31:34]** And in the steering subsystem, there's like a gazillion, you know, thousands of really
**[31:40]** weird cells, which might be like the one for the spider flinch reflex and the one for I'm
**[31:44]** about to taste salt.
**[31:45]** So why would each reward function need a different cell type?
**[31:49]** Well, so this is where you get innately wired circuits, right?
**[31:52]** So in the learning algorithm part, in the learning subsystem, you set up, specify the
**[31:59]** initial architecture, you specify a learning algorithm, it's all the juices is happening
**[32:03]** through plasticity of the synapses, changes of the synapses within that big network.
**[32:09]** But it's kind of like a relatively repeating architecture, how it's initialized.
**[32:13]** It's just like the amount of Python code needed to make, you know, an eight-layer transformer
**[32:18]** is not that different from wanting to make a three-layer transformer, right?
**[32:21]** You're just replicating.
**[32:22]** Yeah.
**[32:23]** Whereas all this Python code for the reward function, you know, if superior colliculus
**[32:26]** sees something that's skittering and, you know, you're feeling goosebumps on your skin
**[32:31]** or whatever, then trigger spider reflex.
**[32:33]** That's just a bunch of like bespoke, species-specific, situation-specific crap that the cortex doesn't
**[32:42]** know about spiders.
**[32:43]** It just knows about layers and learning.
**[32:45]** Right.
**[32:46]** But you're saying that the only way to have this, like write this reward function is to
**[32:50]** have a special cell type.
**[32:52]** Yeah.
**[32:53]** Well, I think so.
**[32:54]** I think you either have to have a special cell types or you have to somehow otherwise
**[32:56]** get special wiring rules that evolution can say, this neuron needs to wire to this neuron
**[33:02]** without any learning.
**[33:04]** And the way that that is most likely to happen, I think, is that those cells express like
**[33:08]** different receptors and proteins that say, okay, when this one comes in contact with
**[33:12]** this one, let's form a synapse.
**[33:16]** So it's genetic wiring.
**[33:17]** Yeah.
**[33:18]** And those need cell types to do it.
**[33:20]** Yeah.
**[33:22]** It would make a lot more sense if I knew one-on-one neuroscience, but like, it seems like there's
**[33:26]** still a lot of complexity or generality rather in the syringe subsystem.
**[33:31]** So in the syringe subsystem has its own visual system that's separate from the visual cortex.
**[33:39]** Different features still need to plug into that vision system in the, so like the spider
**[33:46]** thing needs to plug into it.
**[33:48]** And also the love thing needs to plug into it, et cetera, et cetera.
**[33:55]** So it seems complicated.
**[33:57]** No, it's still complicated.
**[33:58]** And that's all the more reason why a lot of the genomic, you know, real estate in the
**[34:03]** genome and in terms of these different cell types and so on would go into wiring up the
**[34:08]** syringe subsystem.
**[34:09]** Can we tell?
**[34:10]** Pre-wiring it.
**[34:11]** Can we tell how much of the genome is like clearly working?
**[34:14]** So I guess you could tell how many are relevant to the producing the RNA that manifest or
**[34:20]** the epigenetics that manifest in different cell types in the brain, right?
**[34:22]** Yeah.
**[34:23]** This is what the cell types helps you get at it.
**[34:24]** I don't think, I don't think it's exactly like, oh, this percent of the genome is doing
**[34:27]** this, but you could say, okay, in these, all these syringe subsystem subsypes, you know,
**[34:30]** how many different genes are involved in sort of specifying which is which and how they
**[34:33]** wire and how much genomic real estate do those genes take up versus the ones that specify,
**[34:42]** you know, visual cortex versus audio auditory cortex, you kind of just reusing the same
**[34:46]** genes to do the same thing twice.
**[34:48]** Whereas the spider reflex hooking up, yes, you're right.
**[34:50]** They have to, they have to build a vision system and they have to build some auditory
**[34:54]** systems and touch systems and navigation type systems.
**[34:58]** So, you know, even feeding into the hippocampus and stuff like that, there's head direction
**[35:01]** cells, even the fly brain, it has innate circuits that, you know, figure out its orientation
**[35:06]** and help it navigate in the world.
**[35:08]** And it uses vision figure as optical flow of how it's flying and, you know, how is it,
**[35:14]** how is its flight related to the wind direction?
**[35:16]** It has all these innate stuff that I think we, in the mammal brain, we would all put
**[35:20]** that in, lump that into the steering subsystem.
**[35:22]** So there's a lot of work.
**[35:23]** So all the genes basically that go into specifying all the things a fly has to do, we're going
**[35:28]** to have stuff like that too, just all in the steering subsystem.
**[35:30]** But do we, do we have some estimate of like, here's how many nucleotides, how many megabases
**[35:35]** it takes to?
**[35:37]** I don't know.
**[35:38]** I mean, but, but, but I mean, I think people, you might be able to talk to biologists about
**[35:41]** this, you know, to, to some degree, because you can say, well, we just have a ton in common.
**[35:46]** I mean, we have a lot in common with yeast from a genes perspective, yeast is still used
**[35:52]** as a model for, you know, some amount of drug development and stuff like that in biology.
**[35:57]** And so, so much of the genome is just going towards, you have a cell at all, it can recycle
**[36:02]** waste, it can get energy, it can replicate.
**[36:06]** And then, then you see what we have in common with a mouse.
**[36:09]** And so we do know at some level that the, you know, the difference is us in a chimpanzee
**[36:12]** or something, and that includes the social instincts and the more advanced, you know,
**[36:15]** differences in cortex and so on.
**[36:18]** It's a, it's a tiny number of genes that go into these additional amount of making the
**[36:22]** eight layer transformer instead of the six layer transformer or tweaking that reward
**[36:27]** function.
**[36:28]** So this would help explain why the hominid brain exploded in size so fast, which was
**[36:35]** presumably like, tell me this is correct, but under the story, we social learning or
**[36:41]** some other thing increased the ability to learn from the environment, like increased
**[36:47]** our sample efficiency, right?
**[36:48]** Instead of having to go and kill the boar yourself and figure out like how to do that,
**[36:53]** you can just be like, uh, the elder told me this, how you make a spear.
**[36:57]** And then now it increases the incentive to have a bigger cortex, which can like learn
**[37:00]** these things.
**[37:01]** Yes.
**[37:02]** And that can be done with a relatively few genes because it's really, it's really replicating
**[37:06]** what the mouse already has is making more of it.
**[37:08]** And it's maybe not exactly the same and there may be tweaks, but it's like, from a perspective,
**[37:13]** you don't have to reinvent all this stuff, right?
**[37:16]** So then, um, how far back in the history of the evolution of the brain, does the cortex
**[37:23]** go back?
**[37:24]** And is the idea that like the cortex has always figured out this omnidirectional inference
**[37:27]** thing that that's been a solved problem for a long time.
**[37:29]** And then the big unlock with primates is this, we got the reward function, which increased
**[37:33]** the returns to having omnidirectional inference.
**[37:36]** Or is the cortex, is the omnidirectional inference also something that took a while to unlock?
**[37:41]** I'm not sure that there's agreement about that.
**[37:43]** I think there might be specific questions about language, you know, or their tweaks
**[37:46]** to be able, you know, whether that's through auditory and memory, some combination auditory
**[37:49]** memory regions.
**[37:50]** And then there might also be like, um, macro wiring, right?
**[37:54]** Of like, you need to wire auditory regions into memory regions or something like that
**[38:00]** and into some of these social instincts to get language, for example, to happen.
**[38:05]** So there might be, but that might be also a small number of gene changes to be able
**[38:09]** to say, oh, I just need from my temporal lobe over here, going over to the auditory cortex,
**[38:13]** something, right?
**[38:14]** And there is some evidence for the, you know, the Broca's area, Wernicke's area, they're
**[38:16]** connected with these hippocampus and so on.
**[38:19]** And so prefrontal cortex.
**[38:20]** So there's like some small number of genes, maybe for like enabling humans to really properly
**[38:25]** do language.
**[38:26]** That could be a big one.
**[38:28]** But yeah, I mean, I think that is it that something changed about the cortex and it
**[38:37]** became possible to do these things, whereas that was that potential was already there,
**[38:41]** but there wasn't the incentive to expand that capability and then use it, wired it to these
**[38:46]** social instincts and use it more.
**[38:49]** I mean, I would lean somewhat toward the latter.
**[38:51]** I mean, I think a mouse has a lot of similarity in terms of cortex as a human.
**[38:57]** Right.
**[38:58]** Although there's that Cezanne and Hercule Husserl work, the number of neurons scales
**[39:06]** better with weight with primate brains than it does with rodent brains, right?
**[39:11]** So does that suggest that there actually was some improvement in the scalability of the
**[39:15]** cortex?
**[39:16]** Maybe, maybe.
**[39:17]** I'm not, I'm not super deep on this.
**[39:19]** There may, there may have been, yeah, changes in architecture, changes in the folding, changes
**[39:25]** in neuron properties and stuff that, that somehow slightly tweak this, but there's still
**[39:29]** a scaling, right?
**[39:30]** Either way.
**[39:31]** Right.
**[39:32]** And so I was not saying there aren't something special about humans in the architecture of
**[39:36]** the learning subsystem at all.
**[39:40]** But yeah, I mean, I think it's pretty widely thought that this is expanded, but then the
**[39:44]** question is, okay, well, how does that, how does that fit in also with the steering subsystem
**[39:48]** changes and the instincts that make use of this and allow you to bootstrap using this
**[39:53]** effectively?
**[39:54]** But I mean, just to say a few other things, I mean, so even the fly brain has some amount
**[39:59]** of, for example, even, even very far back.
**[40:03]** I mean, I think you've read this, this great book, The Brief History of Intelligence, right?
**[40:06]** I think this is a really good book.
**[40:08]** Lots of AI researchers think this is a really good book, it seems like.
**[40:12]** Yeah, you have some amount of learning going back all the way to anything that has a brain,
**[40:21]** basically.
**[40:22]** You have something kind of like primitive reinforcement learning, at least, going back
**[40:29]** at least to like vertebrates, like imagine like a zebra fish, just like a, and there's
**[40:35]** kind of these other branches.
**[40:37]** Birds maybe kind of reinvented something kind of cortex-like, but it doesn't have the six
**[40:40]** layers, but they have something a little bit cortex-like.
**[40:44]** So that some of those things after reptiles, in some sense, birds and mammals both kind
**[40:49]** of made us up somewhat cortex-like, but differently organized thing.
**[40:52]** But even a fly brain has like associative learning centers that actually do things that
**[40:58]** maybe look a little bit like this, like thought assessor concept from, from Behrens, where
**[41:02]** there's like a specific dopamine signal to train specific subgroups of neurons in the
**[41:06]** mushroom body to associate different sensory information with, am I going to get food now,
**[41:12]** or am I going to get hurt now?
**[41:14]** Yeah.
**[41:15]** Brief tangent.
**[41:16]** I remember reading in one blog post that Darren Millage wrote that the parts of the cortex,
**[41:25]** which are associated with audio and vision, have scaled disproportionately between other
**[41:31]** primates and humans, whereas the parts associated say with odor have not.
**[41:37]** And I remember him saying something like, this is explained by that kind of data having
**[41:42]** worse scaling law properties.
**[41:46]** But I think the, and maybe he meant this, but another interpretation of actually what's
**[41:50]** happening there is that these social reward functions that are built into the steering
**[41:56]** subsystem needed to make use more of being able to see your elders and see what the visual
**[42:03]** cues are and hear what they're saying.
**[42:05]** Yeah.
**[42:05]** And in order to make a sense of these cues, which guide learning, you needed to activate
**[42:10]** these, um, activate the vision and audio more than.
**[42:14]** I mean, there's all this stuff I feel like has come up in, in your, your shows before
**[42:19]** actually, but like, even like the design of the human eye where you have like the pupil
**[42:23]** and the white and everything, like we are designed to be able to establish relationships
**[42:26]** based on joint eye contact.
**[42:28]** And maybe this came up in the sudden episode.
**[42:29]** I can't remember, but, um, yeah, we're, we, we have to bootstrap to the point where we
**[42:34]** can detect eye contact and where we can communicate by language.
**[42:37]** Right.
**[42:37]** And that's like what the, the first couple of years of life are trying to do.
**[42:41]** Yeah.
**[42:42]** Okay.
**[42:42]** Uh, I want to ask you about RL.
**[42:44]** So, um, currently the way these elements are trained, you know, they are, um, if, if they
**[42:50]** solve the unit test or solve a math problem, that whole trajectory, every token in that
**[42:54]** trajectory is up-weighted and what's going on with humans.
**[42:57]** Is there, are there different types of model-based versus model-free that are happening in different
**[43:00]** parts of the brain?
**[43:02]** Yeah.
**[43:02]** I mean, this is, this is another one of these things.
**[43:04]** I mean, again, all my answers to these questions, any specific thing I say, it's all just kind
**[43:08]** of like directionally, this is, we can kind of explore around this.
**[43:10]** I find this interesting.
**[43:12]** Maybe I feel like the literature points in these directions in some very broad way.
**[43:15]** What I actually want to do is like go and map the entire mouse brain and like figure
**[43:18]** this out comprehensively and like make neuroscience the ground truth science.
**[43:22]** So I don't know, basically.
**[43:24]** Um, but, uh, but yeah, I mean, they're, so first of all, I mean, I think with Ilya on
**[43:29]** the podcast, I mean, he was like, it's weird that you don't use value functions, right?
**[43:33]** You use like the most dumbest form of RL.
**[43:36]** And of course there are, these people are incredibly smart and they're optimizing for
**[43:39]** how to do it on GPUs.
**[43:40]** And it's really incredible what they're achieving.
**[43:42]** But like conceptually, it's a really dumb form of RL, even compared to like what was
**[43:45]** being done in like 10 years ago.
**[43:47]** Like even, uh, you know, the Atari game playing stuff, right.
**[43:51]** Was using like Q learning, which is basically like it's a kind of temporal difference learning,
**[43:56]** right.
**[43:56]** And the temporal difference learning basically means you have some kind of a value function
**[44:00]** of like what action I choose now doesn't just tell me literally what happens immediately
**[44:05]** after this.
**[44:06]** It tells me like, what is the long run consequence of that from my expected, you know, total
**[44:10]** reward or something like that.
**[44:12]** Um, and so you have value functions, like the fact that we don't have like value functions
**[44:18]** at all is like in the LLMs is like, it's crazy.
**[44:22]** I mean, I think, I think because Ilya said it, I can say it, I know, you know, one, one
**[44:27]** 100th of what he does about AI, but like, it's kind of crazy that this is working.
**[44:32]** Yeah.
**[44:33]** Um, but, uh, yeah, I mean, in terms of the brain, um,
**[44:41]** well, so I think there are some parts of the brain that are thought to do something that's
**[44:45]** very much like model-free RL.
**[44:47]** That's sort of parts of the basal ganglia, um, sort of striatum and basal ganglia.
**[44:52]** They have like a, a certain finite, like it is thought that they have a certain like finite,
**[44:56]** relatively small action space and the types of actions they could take.
**[45:00]** First of all, it might be like, tell the spinal cord or tell the brainstem and spinal
**[45:04]** cord to do this motor action.
**[45:05]** Yes, no.
**[45:06]** Um, or it might be more complicated cognitive type actions, like tell the thalamus to allow
**[45:12]** this part of the cortex to talk to this other part or release the memory of this in the
**[45:16]** hippocampus and start a new one or something.
**[45:18]** Right.
**[45:18]** But there's some finite set of actions that kind of come out of the basal ganglia and
**[45:23]** that it's just a very simple RL.
**[45:25]** So there are probably parts of other brains in our brain that are just like doing very
**[45:30]** simple, naive type RL algorithms.
**[45:33]** Um, layer one thing on top of that is that some of the major work in neuroscience, like
**[45:38]** Peter Diane's work and a bunch of work that is part of why I think DeepMind did the temporal
**[45:43]** difference learning stuff in the first place, um, is they were very interested in neuroscience.
**[45:48]** Um, and there's a lot of neuroscience evidence that the dopamine is giving this reward
**[45:52]** prediction error signal, um, rather than just reward, yes, no, you know, a gazillion
**[45:58]** time steps in the future.
**[45:58]** It's a prediction error.
**[46:00]** Um, and that's consistent with like learning these value functions.
**[46:04]** Um, so there's that.
**[46:07]** And then there's maybe like higher order stuff.
**[46:09]** So we have these cortex making this world model.
**[46:12]** Well, one of the things the cortex world model can contain is a model of when you do and
**[46:16]** don't get rewards, right?
**[46:18]** Again, it's predicting what the steering subsystem will do.
**[46:20]** It could be predicting what the basal ganglia will do.
**[46:23]** And so you have a model in your cortex that has more generalization and more concepts
**[46:26]** and all this stuff that says, okay, these types of plans, these types of actions will
**[46:31]** lead in these types of circumstances to reward.
**[46:34]** So I have a model of my reward.
**[46:36]** Um, some people also think that you can go the other way.
**[46:40]** And so this is part of the inference picture.
**[46:42]** There's this idea of RL as inference.
**[46:44]** Um, you could say, well, conditional on my having a high reward sample, a plan that I
**[46:50]** would have had to get there.
**[46:53]** That's inference of the plan part from the reward part.
**[46:56]** I'm clamping the reward as high and inferring the plan sampling from plans that could lead
**[47:01]** to that.
**[47:02]** Um, and so if you have this very general cortical thing, it can just do, if you have this like
**[47:06]** general, very general model based system and the model among other things includes plans
**[47:10]** and rewards, then you just get it for free basically.
**[47:14]** So like in neural network parlance, there's a value head associated to the, the, the omnidirectional
**[47:22]** inference that's happening.
**[47:23]** Yes.
**[47:23]** Yeah.
**[47:24]** Or there's a value input.
**[47:25]** Um, yeah.
**[47:26]** Oh, okay.
**[47:27]** Yeah.
**[47:27]** And it, and it can predict one of the, one of the, one of the almost sensory variables
**[47:31]** that can predict is, is what rewards it's going to get.
**[47:34]** Yeah.
**[47:34]** But by the speaking of this thing about amortizing things, um, yeah, obviously value is like
**[47:42]** amortized rollouts of looking up reward.
**[47:46]** Yeah.
**[47:46]** Something like that.
**[47:47]** Yeah.
**[47:47]** Yeah.
**[47:48]** It's like a statistical average or prediction of it.
**[47:51]** Yeah.
**[47:52]** Right.
**[47:52]** Tangential thought, uh, you know, Joe Henrik and others have this idea that the way human
**[47:59]** societies have learned to do things, it's just like, how do you figure out the, you
**[48:03]** know, this kind of being, which actually just almost always poisons you is edible.
**[48:10]** If you do this 10 step, incredibly complicated process, any one of which, if you fail at
**[48:15]** the bean will be poisonous.
**[48:16]** How do you figure out how to hunt this seal in this particular way with this like particular
**[48:21]** weapon at this particular time of the year, et cetera.
**[48:23]** Um, there's no way, but, uh, just like trying shit over generations and it strikes me.
**[48:30]** This is actually very much like model free RL happening at like a civilizational level.
**[48:34]** Um, no, not exactly.
**[48:35]** I mean, evolution is the simplest algorithm in some sense.
**[48:38]** Right.
**[48:39]** And if we believe that all of this can come revolution, like the outer loop can be like
**[48:42]** extremely not foresighted and yeah.
**[48:45]** Right.
**[48:45]** Um, that, that, that's interesting.
**[48:47]** Just like, uh, hierarchies of evolution model for you, culture, uh, evolution model for
**[48:52]** And so what does that tell you?
**[48:52]** Maybe the simple algorithms can just get you anything if you do it enough first, right?
**[48:56]** Yeah.
**[48:57]** I don't know.
**[48:57]** So, but yeah, so you, you have like maybe this evolution model for a basal ganglia model
**[49:03]** free cortex model based culture, uh, model free potentially.
**[49:10]** Um, I mean, there's like, you pay attention to your elders or whatever.
**[49:13]** Or so there's maybe this like group selection or whatever of these things is like more model
**[49:16]** free.
**[49:17]** Yeah.
**[49:18]** But now I think culture, well, it stores some of the model.
**[49:24]** Yeah.
**[49:24]** Right.
**[49:25]** So let's say you want to train an agent to help you with something like processing loan
**[49:28]** applications, trading an agent to do this requires more than just giving the model access
**[49:32]** to the right tools.
**[49:33]** Things like browsers and PDF readers and risk models.
**[49:37]** There's this level of tacit knowledge that you can only get by actually working in an
**[49:40]** industry.
**[49:41]** For example, certain loan applications will pass every single automated check despite
**[49:45]** being super risky.
**[49:47]** Every single individual part of the application might look safe, but experienced underwriters
**[49:52]** know to compare across documents to find subtle patterns that signal risk label box has experts
**[49:58]** like this and whatever domain you're focused on.
**[50:00]** And they will set up highly realistic training environments that include whatever subtle
**[50:04]** nuances and watchouts you need to look out for.
**[50:07]** Beyond just building the environment itself, label box provides all the scaffolding you
**[50:10]** need to capture training data for your agent.
**[50:12]** They give you the tools to great agent performance and capture the video of each session and
**[50:17]** to reset the entire environment to a clean state between every episode.
**[50:21]** So whatever domain you're working in label box can help you train reliable real world
**[50:26]** agents.
**[50:27]** Learn more at labelbox.com slash thorkash stepping back.
**[50:34]** How is it a disadvantage or an advantage for humans that we get to use biological hardware
**[50:44]** in comparison to computers as they exist now?
**[50:46]** So by what I mean by this question is like if there's the algorithm with the algorithm
**[50:51]** just qualitatively perform much worse or much better if inscribed in the hardware of today
**[50:56]** and the reason to think it might like here's what I mean like, you know, obviously the
**[50:59]** brain has had to make a bunch of trade offs which are not relevant to competing hardware.
**[51:04]** It has to be much more energetically efficient.
**[51:06]** Maybe as a result, it has to learn a run on slower speed so that it can be a smaller voltage
**[51:10]** gap.
**[51:10]** And so the brain runs at 200 hertz and has to like run on 20 watts.
**[51:15]** On the other hand, you know, with like robotics, we've clearly experienced that fingers are
**[51:19]** way more nimble than we can make motors so far as maybe there's something in the brain
**[51:24]** that is the equivalent of like cognitive dexterity, which is like maybe due to the
**[51:28]** fact that we can do unstructured sparsity, we can co locate the memory in the compute.
**[51:32]** Yes.
**[51:33]** Where does this all that are you like, fuck, we will be so much smarter if we didn't have
**[51:36]** to deal with these brains or you're like, oh, I mean, I think in the end, we will get
**[51:39]** the best of both worlds, right?
**[51:41]** Somehow, right?
**[51:42]** I think I think an obvious downside of the brain is it cannot be copied.
**[51:45]** Yeah, you don't have, you know, external read write access to every neuron and synapse.
**[51:50]** Whereas you do, I can just edit something in the weight matrix, right?
**[51:52]** You know, in Python or whatever, you know, and load that up and copy that in principle,
**[51:59]** right?
**[52:01]** So the fact that it can't be copied and kind of random accessed is like very annoying.
**[52:06]** But otherwise, maybe these are like has a lot of advantages.
**[52:09]** So it also tells you that you want to like somehow do the co-design of the algorithm
**[52:13]** and maybe that even doesn't change it that much from all of what we discussed, but you
**[52:17]** want to somehow do this co-design.
**[52:18]** So yeah, how do you do it with really slow, low voltage switches?
**[52:24]** That's going to be really important for the energy consumption, the co-locating memory
**[52:29]** and compute.
**[52:30]** So like I think that probably just like hardware companies will try to co-locate memory and
**[52:34]** compute.
**[52:34]** They will try to use lower voltages, allow some stochastic stuff.
**[52:39]** There are some people that think that this like all this probabilistic stuff that we
**[52:42]** were talking about, oh, oh, it's actually energy based models and so on is doing a lot.
**[52:46]** It is doing lots of sampling.
**[52:48]** It's not just amortizing everything that the neurons are also very natural for that because
**[52:53]** they're naturally stochastic.
**[52:55]** And so you don't have to do a random number generator and a bunch of Python code basically
**[53:00]** to generate a sample.
**[53:01]** The neuron just generates samples and it can tune what the different probabilities are.
**[53:06]** And so and like learn those tunings.
**[53:09]** And so it could be that it's very co-designed with like some kind of inference method or
**[53:15]** something.
**[53:16]** It'd be hilarious.
**[53:16]** I mean, the message here, this interview is like, you know, all these people that folks
**[53:21]** make fun of on Twitter, you know, Yann LeCun and Beth Jezos and whatever.
**[53:25]** They're like, no, like, yeah, maybe I don't know.
**[53:28]** That is actually one read of me invented.
**[53:30]** You know, I haven't really worked on AI at all since LLMs, you know, took off.
**[53:35]** So I'm just like out of the loop.
**[53:36]** But I'm surprised and I think it's amazing how the scaling is working and everything.
**[53:42]** But yeah, I think Yann LeCun and Beth Jezos are kind of onto something about the probabilistic
**[53:46]** models, or at least possibly.
**[53:48]** And in fact, that's what, you know, all the neuroscientists and all the AI people thought
**[53:52]** like until 2021 or something, right?
**[53:54]** So there's a bunch of cellular stuff happening in the brain that is not just about neuron
**[54:00]** to neuron synaptic connections.
**[54:04]** How much of that is functionally doing more work than the synapses themselves are doing
**[54:12]** versus it's just a bunch of collage that you have to do in order to make the synaptic thing
**[54:17]** work.
**[54:17]** So the way you need to, you know, with a digital mind, you can nudge the synapse, sorry, the
**[54:23]** parameter extremely easily.
**[54:24]** But with a cell to modulate a synapse, according to the gradient signal, it just takes all
**[54:32]** of this crazy machinery.
**[54:33]** Is it actually doing more than it takes extremely little code to do?
**[54:36]** So I don't know, but I'm not a believer in the like radical, like, oh, actually memory
**[54:41]** is not synapses mostly, or like learning is mostly genetic changes or something like that.
**[54:48]** I think it would just make a lot of sense.
**[54:50]** I think you put it really well for it to be more like the second thing you said.
**[54:53]** Like, let's say you want to do weight normalization across all the weights coming out of your
**[54:57]** neuron, right?
**[54:59]** Or into your neuron.
**[55:00]** Well, you probably have to like somehow tell the nucleus about this of the cell and then
**[55:04]** have that kind of send everything back out to the synapses or something, right?
**[55:07]** And so there's going to be a lot of cellular changes, right?
**[55:10]** Or let's say that, you know, you just had a lot of plasticity and like you're part of
**[55:15]** this memory.
**[55:16]** And now that's got consolidated into the cortex or whatever.
**[55:19]** And now we want to reuse you as like a new one that can learn again.
**[55:23]** It's going to be a ton of cellular changes.
**[55:25]** So there's going to be tons of stuff happening in the cell, but algorithmically it's not
**[55:29]** really adding something beyond these algorithms, right?
**[55:32]** It's just implementing something that in a digital computer is very easy for us to go
**[55:35]** and just find the weights and change them.
**[55:38]** And it is a cell.
**[55:39]** It just literally has to do all this with molecular machines itself without any central
**[55:43]** controller, right?
**[55:44]** It's kind of incredible.
**[55:46]** There are some things that cells do, I think, that seem like more convincing.
**[55:49]** So in the cerebellum, so one of the things the cerebellum has to do is like predict over
**[55:54]** time, like predict what is the time delay?
**[55:57]** You know, let's say that, you know, I see a flash and then, you know, some number of
**[56:02]** milliseconds later, I'm going to get like a puff of air in my eyelid or something, right?
**[56:07]** The cerebellum can be very good at predicting what's the timing between the flash and the
**[56:11]** air puff so that now your eye will just like close automatically.
**[56:15]** Like the cerebellum is like involved in that type of reflex, like learned reflex.
**[56:20]** And there are some cells in the cerebellum where it seems like the cell body is playing
**[56:25]** a role in storing that time constant, changing that time constant of delay versus that all
**[56:32]** being somehow done with like, I'm going to make a longer ring of synapses to make that
**[56:36]** delay longer.
**[56:37]** It's like, no, the cell body will just like store that time delay for you.
**[56:42]** So there are some examples, but I'm not a believer like out of the box and like essentially
**[56:48]** this theory that like what's happening is changes and connections between neurons.
**[56:54]** And that's like the main algorithmic thing that's going on.
**[56:57]** I think that's a very good reason to still believe that it's that rather than some like
**[57:02]** crazy cellular stuff.
**[57:04]** Going back to this whole perspective of like our intelligence is not just this omni-directional
**[57:11]** inference thing that builds a world model, but really this system that teaches us what
**[57:16]** to pay attention to, what are the important salient factors to learn from, etc.
**[57:22]** I want to see if there's some intuition we can drive from this, but what different kinds
**[57:28]** of intelligences might be like.
**[57:29]** So it seems like AGI or superhuman intelligence should still have this like ability to learn
**[57:38]** a world model that's quite general, but then it might be incentivized to pay attention
**[57:46]** to different things that are relevant for the modern post-singularity environment.
**[57:54]** How different should we expect different intelligences to be basically?
**[57:56]** Yeah.
**[57:57]** I mean, I think one way of this question is like, is it actually possible to like make
**[58:00]** the paperclip maximizer or whatever, right?
**[58:02]** If you try to make the paperclip maximizer, does that end up like just not being smart
**[58:06]** or something like that?
**[58:07]** Because it was just the only reward function it had was like make paperclips.
**[58:11]** Interesting.
**[58:12]** If I channel Steve Burns more, I mean, I think he's very concerned that the sort of
**[58:16]** minimum viable things in the steering subsystem that you need to get something smart is way
**[58:21]** less than the minimum viable set of things you need for it to have human like social
**[58:25]** instincts and ethics and stuff like that.
**[58:27]** So a lot of what you want to know about the steering subsystem is actually the specifics
**[58:31]** of how you do alignment essentially, or what human behavior and social instincts is versus
**[58:38]** just what you need for capabilities.
**[58:39]** And we talked about it in a slightly different way because we were sort of saying, well,
**[58:42]** in order for humans to like learn socially, they need to make eye contact and learn from
**[58:46]** others.
**[58:47]** But we already know from LLMs, right, that depending on your starting point, you can
**[58:51]** learn language without that stuff, right?
**[58:54]** And so, yeah.
**[58:57]** And so I think that it probably is possible to make like super powerful, you know, model
**[59:01]** based RL, you know, optimizing systems and stuff like that, that don't have most of what
**[59:06]** we have in the human brain reward functions.
**[59:08]** And as a consequence, might want to maximize paperclips.
**[59:10]** And that's a concern.
**[59:11]** Right.
**[59:12]** But you're pointing out that in order to make a competent paperclip maximizer, the kind
**[59:18]** of thing that can build the spaceships and learn the physics and whatever, it needs to
**[59:24]** have some drives which elicit learning, including, say, curiosity and exploration.
**[59:29]** Yeah.
**[59:29]** Curiosity and interest in others, interest in social interactions, curiosity.
**[59:36]** Yeah.
**[59:36]** But that's pretty minimal, I think.
**[59:38]** And that's true for humans.
**[59:40]** Right.
**[59:41]** But it might be less true for like something that's already pre-trained as an LLM or something.
**[59:44]** I see.
**[59:44]** Right.
**[59:44]** And so most of why we want to know the steering subsystem, I think, if I'm channeling Steve,
**[59:49]** is alignment reasons.
**[59:51]** Yeah.
**[59:51]** Right.
**[59:52]** How confident are we that we even have the right algorithmic conceptual
**[01:00:00]** vocabulary to think about what the brain is doing, and what I mean by this is, you know,
**[01:00:06]** there was one big contribution to AI from neuroscience, which was the side you have
**[01:00:09]** the neuron, yeah, like, William, you know, 1950s, just like this original contribution.
**[01:00:15]** But then it seems like a lot of what we've learned afterwards, about what the high level
**[01:00:19]** algorithm the brain is implementing, from the backprop to if there's something analogous
**[01:00:25]** in the brain, to always rewinding something like CNNs, to TD learning and Bellman equations,
**[01:00:33]** actor critic, whatever, yeah, seems inspired by what is, like, we come up with some idea,
**[01:00:37]** like, but maybe we can make AI neural networks works this way. Yeah. And then we notice that
**[01:00:41]** something in the brain also works that way. Yes. So why not think there's more things like this?
**[01:00:45]** Well, there may be. Yeah. I think the reason that I'm not I think that we might be onto something
**[01:00:51]** is that, like, the AIs we're making based on these ideas are working surprisingly well,
**[01:00:56]** there's also a bunch of like, just empirical stuff, like, like, convolutional neural nets
**[01:01:00]** and variants of convolutional neural nets. I'm not for sure what the absolute latest latest,
**[01:01:06]** but compared to other like models in computational neuroscience of like,
**[01:01:10]** what the visual system is doing, are just like more predictive, right? So you can just like score
**[01:01:14]** more, even like pre trained on like cat pictures and stuff, CNNs, what is the representational
**[01:01:21]** similarity that they have on some arbitrary other image versus, you know, compared to the brain
**[01:01:26]** activations measured in different ways. Jim DiCarlo's lab has like brain score. And like,
**[01:01:34]** the AI models actually like there, there seems to be some relevance there in terms of like,
**[01:01:39]** even like neurosciences don't necessarily have something better than that. So yes, I mean,
**[01:01:43]** that's just kind of recapitulating what you're saying is that like, the best computational
**[01:01:46]** neuroscience theories we have seem to have been like invented, right, largely as a result of AI
**[01:01:51]** models, and like find things that work and so find backprop works and then say, can we approximate
**[01:01:56]** backprop with cortical circuits or something? And there's there's kind of been things like that.
**[01:02:00]** Now, some people totally disagree with this, right? So like Yuri Buzsaki, as a neuroscientist
**[01:02:07]** who has a book called the brain from inside out, where he basically says, like all our psychology
**[01:02:11]** concepts, like AI concepts, all the stuff is just like made up stuff, we actually have to do is
**[01:02:16]** like figure out what is the actual set of primitives that like the brain actually uses, and
**[01:02:19]** our vocabulary is not going to be adequate to that we have to start with the brain and make new
**[01:02:24]** vocabulary rather than saying backprop and then try to apply that to the brain or something like
**[01:02:28]** that. And, you know, he studies a lot of like oscillations and stuff in the brain, as opposed
**[01:02:33]** to individual neurons and what they do. And, you know, I don't know, I think that there's a case
**[01:02:39]** to be made for that. And from a kind of research program design perspective, I think there's like
**[01:02:43]** one thing we should be trying to do is just like simulate a tiny worm or a tiny zebrafish,
**[01:02:49]** like from almost like as biophysical or like as as bottom up as possible, like get connective
**[01:02:54]** molecules activity and like just study it as a physical dynamical system and like look what it
**[01:03:00]** does. But I don't know, I mean, just when I like, it just feels like the AI is really good fodder
**[01:03:07]** for computational neuroscience, like those might actually be pretty good models, we should look at
**[01:03:11]** that. So I'm not a person who thinks that. I think I both think that there should be a part
**[01:03:19]** of the research portfolio that is like totally bottom up and not trying to apply our vocabulary
**[01:03:25]** that we learned from AI onto these systems. And that there should be another big part of this
**[01:03:29]** that's kind of trying to reverse engineer it using that vocabulary or variants of that vocabulary.
**[01:03:35]** And that we should just be pursuing both. And my guess is that the reverse engineering one
**[01:03:39]** is actually going to like kind of work-ish or something like we do see things like TD learning,
**[01:03:46]** which, you know, Sutton also invented separately, right? That must be a crazy feeling to just like,
**[01:03:52]** yeah, it's great. This like equation I wrote down is like, it seems like the dopamine is like
**[01:03:57]** doing some of that. Yeah. So let me ask you about this. You know, you guys are finding different
**[01:04:03]** groups that are trying to figure out what's up in the brain. If we had a perfect representation,
**[01:04:10]** how are you defined out of the brain? Why think it would actually let us figure out the answer
**[01:04:15]** to these questions? We have neural networks, which are way more interpretable, not just because we
**[01:04:21]** understand what's in the weight matrices, but because there are weight matrices, there are
**[01:04:24]** these boxes with numbers in them. And even then we can tell very basic things. We can kind of see
**[01:04:31]** circuits for a very basic pattern matching of following one token with another. I feel like we
**[01:04:39]** don't really have an explanation of why LLMs are intelligent just because they're interpretable.
**[01:04:42]** Yeah. Well, I would somewhat dispute it. I think we have some architectural, we have some
**[01:04:46]** description of what the LLM is like fundamentally doing. And what that's doing is that I have an
**[01:04:51]** architecture and I have a learning rule and I have hyperparameters and I have initialization
**[01:04:55]** and I have training data. But those are things we learned from because we built them,
**[01:04:59]** not because we interpreted them from seeing the weights.
**[01:05:02]** We built them.
**[01:05:02]** Which is the analogous thing to connectome is like seeing the weights.
**[01:05:05]** What I think we should do is we should describe the brain more in that language of things like
**[01:05:08]** architectures, learning rules, initializations, rather than trying to find the golden gate bridge
**[01:05:13]** circuit and saying exactly how does this neuron actually, you know, that's going to be some
**[01:05:17]** incredibly complicated learned pattern. Yeah, Conrad Kording and Tim Lillicrap have this paper
**[01:05:23]** from a while ago, maybe five years ago called, What Does It Mean to Understand a Neural Network?
**[01:05:27]** Or what would it mean to understand a neural network? And what they say is, yeah, basically
**[01:05:33]** that, like you could imagine you train a neural network to like compute the digits of pi or
**[01:05:36]** something. Well, like some crazy, you know, it's like, it's like this crazy pattern.
**[01:05:40]** And then you also train that thing to like predict the most complicated thing you find,
**[01:05:43]** predict stock prices, basically predict the really complex systems, right? Computational,
**[01:05:47]** you know, computationally complete systems. I could predict, I could train a neural network
**[01:05:50]** to do cellular automata or whatever crazy thing. And it's like, we're never going to be able to
**[01:05:55]** fully capture that with interpretability, I think. It's just going to just be doing really
**[01:06:00]** complicated computations internally. But we can still say that the way it got that way is that
**[01:06:05]** it had an architecture and we gave it this training data and it had this loss function.
**[01:06:09]** And so I want to describe the brain in the same way. And I think that this framework
**[01:06:12]** that I've been kind of laying out is like, we need to understand the cortex and how it
**[01:06:15]** embodies a learning algorithm. I don't need to understand how it computes golden gate.
**[01:06:18]** But if you, if you can see all the neurons, if you have the connectome,
**[01:06:22]** why does that teach you what the learning algorithm is?
**[01:06:24]** Well, I guess there are a couple of different views of it. So it depends on this different
**[01:06:27]** parts of this portfolio. So on the totally bottom up, we have to simulate everything portfolio.
**[01:06:32]** It kind of just doesn't, you have to just like, see what are the, you have to make a simulation
**[01:06:35]** of the zebrafish brain or something. And then you like, see what are the like emergent dynamics in
**[01:06:40]** this and you come up with new names and new concepts and all that. That's like, that's like
**[01:06:43]** the most extreme bottom up neuroscience view. But even there, the connectome is like really
**[01:06:50]** important for doing that bottom up biophysical or bottom up simulation.
**[01:06:54]** But on the other hand, you can say, well, what if we can actually apply some ideas from AI?
**[01:06:58]** We basically need to figure out, is it an energy-based model or is it, you know,
**[01:07:03]** an amortized, you know, VAE type model? You know, is it doing back prop or is it doing something
**[01:07:08]** else? Are the learning rules local or global? I mean, if we have some repertoire of possible
**[01:07:14]** ideas about this, can we just think of the connectome as a huge number of additional
**[01:07:20]** constraints that will help to refine, to ultimately have a consistent picture of that?
**[01:07:25]** I think about this for the steering subsystem stuff too, just very basic things about it. How
**[01:07:29]** many different types of dopamine signal or of steering subsystem signal or thought assessor
**[01:07:35]** or so on, how many different types of what broad categories are there? Like even this very basic
**[01:07:40]** information that there's more cell types in the hypothalamus than there are in the cortex,
**[01:07:43]** like that's new information, right? About how much structure is built there versus somewhere
**[01:07:47]** else. Yeah. How many different dopamine neurons are there? Is the wiring between prefrontal and
**[01:07:51]** auditory the same as the wiring between prefrontal and visual? You know, it's like
**[01:07:56]** the most basic things we don't know. And the problem is learning even the most basic things
**[01:08:01]** by a series of bespoke experiments takes an incredibly long time. Whereas just learning
**[01:08:05]** all of that at once by getting a connectome is just like way more efficient.
**[01:08:09]** What is the timeline on this? Because presumably the idea of this is to, well, first
**[01:08:16]** inform the development of AI. You want to be able to figure out how we get AIs to want to care
**[01:08:23]** about what other people think of as internal thought pattern. But interp researchers are
**[01:08:29]** making progress on this question just by inspecting, you know, normal neural networks.
**[01:08:34]** There must be some feature. You can do interp on LLMs that exist.
**[01:08:38]** You can't do interp on a hypothetical model-based reinforcement algorithm like the brain that we
**[01:08:43]** will eventually converge to when we do AGI. Fair. But, you know, what timelines on AI do you need
**[01:08:51]** for this research to be practical and relevant? I think it's fair to say it's not super practical
**[01:08:56]** and relevant if you're in like an AI 2077 scenario. You know, and so like what science
**[01:09:02]** I'm doing now is not going to affect the science of like 10 years from now because what's going
**[01:09:07]** to affect the science of 10 years from now is the outcome of this like AI 2027 scenario, right?
**[01:09:11]** It kind of doesn't matter that much. Probably if I have the connect now, maybe it slightly tweaks
**[01:09:15]** certain things. But I think there's a lot of reason to think maybe that we will get
**[01:09:23]** a lot out of this paradigm. But then the real thing, the thing that is like the
**[01:09:30]** single event that is like transformative for the entire future or something type event
**[01:09:34]** is still like, you know, more than five years away or something.
**[01:09:38]** Sorry, is that because like we haven't captured omnidirectional inference?
**[01:09:44]** We haven't figured out the right ways to get a mind to pay attention to things in a way that-
**[01:09:50]** I mean, I would take the entirety of your like collective podcast with everyone as like
**[01:09:55]** showing like the distribution of these things, right? I don't know, right? I mean,
**[01:10:00]** what was Carpathy's timeline, right? You know, what's Demis' timeline, right? So these,
**[01:10:04]** then not everybody has a three-year timeline. And so I think-
**[01:10:07]** But there's different reasons and I'm curious what's yours.
**[01:10:10]** What are mine? I don't know. I'm just watching your podcast. I'm trying to understand the
**[01:10:14]** distribution. I don't have a super strong claim that LLMs can't do it.
**[01:10:19]** But is it because of the data efficiency or is it the-
**[01:10:21]** I think part of it is just, it is weirdly different than all this brain stuff.
**[01:10:26]** And so intuitively, it's just weirdly different than all this brain stuff. And I'm kind of waiting
**[01:10:29]** for like the thing that starts to look more like brain. Like I think if AlphaZero and
**[01:10:33]** model-based RL and all of these other things that were being worked on 10 years ago
**[01:10:36]** had been giving us the GPT-5 type capabilities, then I would be like, oh, wow, we're both in the
**[01:10:42]** right paradigm and seeing the results a priori. So my model, my prior and my data are agreeing,
**[01:10:49]** right? And now it's like, I don't know what exactly my data is. It looks pretty good,
**[01:10:53]** but my prior is sort of weird. So yeah, so I don't have a super strong opinion on it.
**[01:10:59]** So I think there's a possibility that essentially all other scientific research that is being done
**[01:11:05]** is somehow obviated, but I don't put a huge amount of probability on that.
**[01:11:10]** I think my timelines might be more in the like, yeah, 10 year-ish range. And if that's the case,
**[01:11:15]** I mean, I think there is probably a difference between a world where we have connectomes on
**[01:11:18]** hard drives and we have understanding of steering subsystem architecture. We've compared
**[01:11:23]** even the most basic properties of what are the reward functions, cost function, architecture,
**[01:11:28]** et cetera, of a mouse versus a shrew versus a small primate, et cetera.
**[01:11:32]** Is this practical in 10 years?
**[01:11:34]** I think it has to be a really big push.
**[01:11:36]** How much funding? How does it compare to where we are now?
**[01:11:38]** It's like billion, low billions dollar scale funding in a very concerted way, I would say.
**[01:11:44]** And how much is on it now?
**[01:11:46]** Um, well, so if I just talk about some of the specific things we have going, so with connectomics,
**[01:11:52]** so E11bio is kind of like our main thing on connectomics.
**[01:11:59]** They are basically trying to make the technology of connectomic brain mapping
**[01:12:05]** several orders of magnitude cheaper. So the Wellcome Trust put out a report a year or two
**[01:12:11]** ago that basically said to get one mouse brain, the first mouse brain connectome would be like
**[01:12:15]** several billion dollars, you know, billions of dollars project.
**[01:12:20]** Well, E11 technology and sort of the suite of efforts in the field also are trying to get like
**[01:12:26]** a single mouse connectome down to like low tens of millions of dollars.
**[01:12:30]** Okay, so that's a mammal brain, right? Now a human brain is about 1000 times bigger.
**[01:12:35]** So if a mouse brain, you can get to 10 million or 20 million, 30 million
**[01:12:39]** with technology, you know, if you just naively scale that, okay, human brain is now still
**[01:12:43]** billions of dollars to just do one human brain. Can you go beyond that? So can you get a human
**[01:12:47]** brain for like less than a billion? But I'm not sure you need every neuron in the human brain.
**[01:12:51]** I think we want to, for example, do an entire mouse brain and a human steering subsystem and
**[01:12:57]** the entire brains of several different mammals with different social instincts.
**[01:13:02]** And so I think that that with a bunch of technology push and a bunch of concerted effort
**[01:13:06]** can be done in the real significant progress if it's focused effort can be done in the kind of
**[01:13:11]** hundreds of millions to low billions. What is the definition of a connectome? Is it?
**[01:13:16]** Presumably it's not a bottom up biophysics model. So is it just that if if it can
**[01:13:21]** estimate the input output of a brain, but like what is it? What is the level of abstraction?
**[01:13:26]** You can give different definitions. And one of the things that's cool about.
**[01:13:29]** So the kind of standard approach to connectomics uses the electron microscope
**[01:13:33]** and very, very thin slices of brain tissue. And it's basically labeling the cell membranes are
**[01:13:38]** going to show up, scatter electrons a lot, and everything else is going to scatter electrons less.
**[01:13:43]** But you don't see a lot of details of the molecules, which types of synapses,
**[01:13:46]** different synapses of different molecular combinations and properties.
**[01:13:50]** E11 and some other research in the field has switched to an optical microscope paradigm.
**[01:13:55]** With optical, the photons don't damage the tissue. So you can kind of wash it and look at fragile,
**[01:14:00]** gentle molecules. So so with E11 approach, you can get a, quote unquote,
**[01:14:05]** molecularly annotated connectome. So that's not just who is connected to who by some kind of
**[01:14:10]** synapse, but what are the molecules that are present at the synapse? What type of cell is that?
**[01:14:15]** So molecularly annotated connectome, that's not exactly the same as having synaptic weights.
**[01:14:21]** That's not exactly the same as being able to simulate the neurons and say,
**[01:14:24]** what's the functional functional consequence of having these molecules and connections.
**[01:14:30]** Um, but you can also do some amount of activity mapping and try to correlate structure to function.
**[01:14:35]** Um, yeah. So interesting. Train an ML model to basically predict the activity from the connectome.
**[01:14:42]** What are the lessons to be taken away from, um, the human genome project? Because one way you
**[01:14:46]** could look at it is that it was actually a mistake and you shouldn't have spent whatever
**[01:14:50]** billions of dollars getting one genome mapped. Rather, you should have just invested in technologies
**[01:14:54]** which have and now now allows us to map genomes for hundreds of dollars.
**[01:14:58]** Yeah. Well, yeah. So George Church was my, was my PhD advisor and basically, uh, yeah. I mean,
**[01:15:03]** what he's pointed out is that, yeah, it was 3 billion or something, you know, roughly $1 per
**[01:15:06]** base pair for the first genome. And then the National Human Genome Research Institute basically
**[01:15:13]** structured the funding process rights and they got a bunch of companies competing to lower the cost.
**[01:15:19]** Um, and then the cost dropped like a million fold in 10 years. Um, and because they changed
**[01:15:24]** the paradigm from, uh, kind of macroscopic kind of chemical techniques to these individual DNA
**[01:15:30]** molecules, make a little cluster of DNA molecules on the microscope and you would see, um, just a
**[01:15:34]** few DNA molecules at a time on each pixel of the camera would basically give you a different,
**[01:15:38]** um, in parallel looking at different fragments of DNA. So you parallelize the thing by like
**[01:15:43]** millions fold and that's what reduced the cost by millions fold. And, um, and yeah, so, so I mean,
**[01:15:49]** essentially, uh, with switching from electron microscopy to optical connectomics, potentially
**[01:15:54]** even future types of connectomics technology, we think there should be similar patterns. That's
**[01:15:57]** why E11 with the focus research organization, uh, started with technology development rather than
**[01:16:03]** starting with saying, we're going to do a human brain or something. Let's just brute force it.
**[01:16:06]** We said, let's get the cost down with new technology, but then you still, it's still a
**[01:16:11]** big thing. Even with new next generation technology, you still need to spend hundreds
**[01:16:15]** of millions on data collection. Yeah. Is this going to be funded with philanthropy
**[01:16:20]** by governments, by investors? This is very TBD and very much evolving in some sense as we speak.
**[01:16:27]** Um, I'm hearing some rumors going around of connectomics related companies potentially
**[01:16:32]** forming, but so, so, so far E11 has been philanthropy. Um, the national science
**[01:16:37]** foundation just put out this call for it, for tech labs, which is basically somewhat of it
**[01:16:40]** is kind of fro inspired or related. Um, I think you could have a tech lab, uh, for
**[01:16:46]** actually going and mapping the mouse brain with us. And that would be sort of philanthropy plus
**[01:16:49]** government still in a nonprofit kind of open source framework. Um, but can, uh, can companies
**[01:16:58]** accelerate that? Can you credibly link connectomics to AI in the context of a company
**[01:17:03]** and get investment for that? It's like possible. I mean, the cost of training these days is
**[01:17:06]** increasing so much. If you could like tell some story, like not only are going to figure out some
**[01:17:12]** safety thing, right. But in fact, we will, um, once we do that, we'll also be able to tell you
**[01:17:18]** how AI works. You should like go to these AI labs and just be like, give me one, one hundredth of
**[01:17:24]** your projected budget in 2030. I sort of tried a little bit like, like seven or eight years ago,
**[01:17:29]** and there was not a lot of interest and maybe now there, there would be. Um, but yeah, I mean,
**[01:17:34]** I think all the things that we've been talking about, like, I think it's really fun to talk
**[01:17:39]** about, but it's ultimately speculation. What is the actual reason for the energy efficiency of
**[01:17:43]** the, of the brain, for example, right? Is it doing real inference or amortized inference or something
**[01:17:48]** else? Like this is all going to be all, it's all answerable by neuroscience. It's going to be hard,
**[01:17:53]** but it's actually answerable. Um, and so if you can only do that for low billions of dollars or
**[01:17:58]** something to really comprehensively solve that, it seems to me in the grand scheme of trillions of
**[01:18:02]** dollars of GPUs and stuff, it actually makes sense to do that investment. But I think investors
**[01:18:08]** also just, there's been many labs that have been launched in the last year where they're
**[01:18:12]** raising on the valuation of billions for things which are quite credible, but are not like
**[01:18:18]** our ARR next quarter is going to be whatever. It's like, we're going to discover materials
**[01:18:22]** and dot, dot, dot. Right. Yes. Yes. Moonshot startups are billion dollar billionaire back
**[01:18:27]** startups. Moonshot startups I see as a kind of on a continuum with froze. Yeah. Um, froze
**[01:18:31]** are a way of channeling philanthropic support, ensuring that it's open source, public benefit,
**[01:18:36]** various other things that may be properties of a given fro. Um, but yes, billionaire back startups,
**[01:18:42]** um, if they can target the right science, the exact right science, I think there's a lot of
**[01:18:47]** ways to do moonshot neuroscience companies that would never get you the connectome. He was like,
**[01:18:51]** oh, we're going to upload the brain or something, but never actually get the mouse connectome or
**[01:18:54]** something. These fundamental things that you need to get to, to ground truth to science. Um,
**[01:19:00]** there are lots of ways to have a moonshot company kind of go wrong and not do the actual science,
**[01:19:05]** but there also may be ways to have companies or, or big corporate labs get involved and actually
**[01:19:11]** do it correctly. Yeah. This, uh, this brings to mind an idea that you had in a lecture you gave
**[01:19:17]** five years ago about, yeah. Do you want to explain behavior cloning on, right? Yeah. I mean,
**[01:19:24]** actually this is funny because I think that the first time I saw this idea, it was, I think it
**[01:19:28]** actually might've been in a blog post by Guerin. Oh, there's always, there's always a Guerin blog
**[01:19:33]** post and there are now academic research efforts in some amount of emerging company type efforts
**[01:19:38]** to try to do this. So, um, yeah. So normally let's say I'm training an image classifier or
**[01:19:44]** something like that. I show it, uh, pictures of cats and dogs or whatever, and they have
**[01:19:49]** the label cat or dog and I have a neural network supposed to predict the label cat or dog or
**[01:19:53]** something like that. Um, that is a limited amount of information per label that you're putting in.
**[01:20:03]** It's just cat or dog. What if I also had predict what is my neural activity pattern when I see a
**[01:20:11]** cat or when I see a dog and all the other things? Um, if you add that as like an auxiliary loss
**[01:20:17]** function or an auxiliary prediction task, does that sculpt the network to know the information
**[01:20:25]** that humans know about cats and dogs, um, and to represent it in a way that's consistent with how
**[01:20:30]** the brain represents it and the kind of representational kind of dimensions or geometry of,
**[01:20:34]** of, of how the brain represents things as opposed to just having these labels. Does that let it
**[01:20:40]** generalize better? Does that let it, uh, have just richer labeling? And of course that's like,
**[01:20:46]** that sounds really challenging. It's very easy to generate lots and lots of labeled cat pictures
**[01:20:50]** with, you know, scale AI or whatever can do this. It is harder to generate lots and lots of brain
**[01:20:56]** activity patterns that correspond to things that you want to train the AI to do. Um, but again,
**[01:21:02]** this is just a technological limitation of neuroscience. If we, if every iPhone was also
**[01:21:06]** a brain scanner, you know, you would, you would not have this problem and we would be training AI
**[01:21:09]** with the brain signals. And, um, it's just the order in which technology is developed is that
**[01:21:14]** we got GPUs before we got portable brain scanners or whatever. Right. And, uh, that kind of thing.
**[01:21:18]** What is the ML analog where you'd be doing here? Cause when you distill models,
**[01:21:22]** you're still looking at the, the final layer of like the, the log props across, um,
**[01:21:29]** across, if you do distillation of one model into another, that is a certain thing that you were
**[01:21:35]** just trying to copy one model into another. I think that we don't really have a perfect proposal
**[01:21:44]** to like distill the brain. I think to distill the brain, you need like a much more complex
**[01:21:49]** brain interface. Like maybe you could also do that. You could make surrogate models.
**[01:21:53]** Um, Andreas Tolias and people like that are doing some amount of neural network surrogate
**[01:21:58]** models of brain activity data. Instead of having your visual cortex do the computation, just
**[01:22:03]** have the surrogate models. You're basically distilling your visual cortex into a neural
**[01:22:06]** network to some degree. Um, that's the kind of distillation. This is doing something a little
**[01:22:10]** different. This is basically just saying I'm adding an auxiliary. I think of as regularization
**[01:22:15]** or I think of it as, um, adding an auxiliary loss function, um, that sort of smoothing out
**[01:22:21]** the prediction task to also always be consistent with how the brain represents it.
**[01:22:26]** It might help you with things like adversarial examples, for example. Right.
**[01:22:30]** But you're predicting the internal state of the brain.
**[01:22:32]** Yes. So, so you, so in addition to predicting the label, the vector of labels like yes,
**[01:22:36]** cat, not dog. Yes. You know, not boat, you know, um, one shot vector or whatever of one hot vector
**[01:22:42]** of, of yes, it's cat. Uh, instead of these gazillion other categories, let's say in this
**[01:22:46]** simple example, you're also predicting a vector, which is like all these brain signal measurements.
**[01:22:51]** Right. Yeah. Interesting.
**[01:22:53]** And so Gurin anyway had this long ago blog post of like, oh, this is like an intermediate thing.
**[01:22:57]** We talk about whole brain emulation. We talk about AGI. We talk about brain computer interface. We
**[01:23:01]** should also be talking about this like brain augmented brain data augmented, um, uh, thing
**[01:23:10]** that's trained on all your behavior, but is also trained on like predicting some of your neural
**[01:23:13]** patterns. Right. And you're saying the learning system is already doing this for the steering
**[01:23:16]** system. Yeah. And our learning system also has to predict the steering subsystem as an auxiliary
**[01:23:21]** task. Yeah. Yeah. And that helps the steering subsystem. Now the steering subsystem can access
**[01:23:25]** that predictor and build a cool reward function using it. Yes. Okay. Separately you're on the
**[01:23:30]** board for, of lean, which is this, um, uh, formal, uh, uh, formal math language, uh, uh, that
**[01:23:39]** mathematicians used to prove theorems and so forth. And obviously there's a bunch of conversation
**[01:23:44]** right now about math, AI automating math. What's your take? Yeah. Well, I think that
**[01:23:50]** there are parts of math that it seems like it's pretty well on track to, to automate. Um,
**[01:23:59]** and that has to do with like, so, so first of all, so, so lean, so lean had been developed
**[01:24:05]** for a number of years at Microsoft and other places has become one of the convergent focused
**[01:24:09]** research organizations to kind of drive more engineering and focus onto it. So lean is like
**[01:24:14]** this language, programming language, where if you, instead of expressing your math proof on pen
**[01:24:20]** and paper, um, you express it in this programming language lean. And then at the end, if you do that,
**[01:24:26]** that way, um, it is a verifiable language so that you can basically click verify and lean will tell
**[01:24:33]** you whether the conclusions of your proof actually follow perfectly from your assumptions of your
**[01:24:37]** proof. Um, so it checks whether the proof is correct automatically. Um, it was like by itself,
**[01:24:43]** this is useful for mathematicians collaborating and stuff like that. Like if I'm some amateur
**[01:24:47]** mathematician, I want to add to a proof, you know, Terry Tao is not going to like, believe my results.
**[01:24:53]** Um, but if lean says it's correct, it's just correct. So it makes it easy for like collaboration
**[01:24:58]** to happen. Um, but it also makes it easy for correctness of proofs to be an RL signal
**[01:25:05]** in very much the RLVR, you know, it's like a perfect math proofing is now formalized math
**[01:25:11]** proving. So formal means it's like expressed in something like lean and verifiable,
**[01:25:14]** mechanically verifiable. Um, that becomes a perfect RLVR, you know, task. Um,
**[01:25:24]** yeah. And I think that that is going to just, just keep working. It seems like is
**[01:25:30]** the couple billion dollar, at least one like billion dollar valuation company,
**[01:25:33]** harmonic based on this alpha proof is based on this, um, a couple other emerging, really
**[01:25:40]** interesting companies. Um, I think that this problem of like RLVR in the crap out of math
**[01:25:46]** proving is basically going to work. Uh, and we will be able to have things that search for proofs,
**[01:25:54]** um, and find them, um, in the same way that we have alpha go or what have you that can search
**[01:26:01]** for, you know, ways of playing the game of go and with that verifiable signal, uh, works.
**[01:26:06]** So does this like solve math? Um, there is still the part that has to do with conjecturing new,
**[01:26:11]** interesting ideas. There's still the kind of conceptual organization of math of what is
**[01:26:15]** interesting. How do you come up with new theorem statements in the first place? Or even like the
**[01:26:22]** very high level breakdown of what strategies you use to do proofs. Um, I mean, I think this
**[01:26:27]** will shift the burden of that so that humans don't have to do a lot of the mechanical parts of math,
**[01:26:34]** uh, validating lemmas and proofs and checking if the statement of this and this paper is
**[01:26:39]** exactly the same as that paper and stuff like that. It will just, that will just work. Uh,
**[01:26:44]** you know, if you really think you're, we're going to get all these things we've been talking about
**[01:26:46]** real AGI, it would also be able to make conjectures. And, you know, Benji has like a
**[01:26:51]** paper as more like theoretical paper. They're probably a bunch of other papers emerging about
**[01:26:54]** this. Like, is there like a loss function for like good explanations or good conjectures?
**[01:26:59]** That's like a pretty profound question, right? Um, a math, a really interesting math proof
**[01:27:05]** or statement might be one that kind of compresses lots of information about other, you know, has
**[01:27:09]** lots of implications for lots of other theorems. Otherwise you would have to prove those theorems
**[01:27:14]** using long complex passive inference here. If you have this theorem, this theorem is correct.
**[01:27:18]** And you have short passive inference to all the other ones. And it's a short,
**[01:27:21]** compact statement. So it's like a powerful explanation that explains all the rest of math.
**[01:27:24]** And like part of what math is doing is like making these compact
**[01:27:28]** things that explain the other things. So they call it the moral complexity
**[01:27:31]** of this statement or something. Yeah. Generating all the other statements,
**[01:27:33]** given that, you know, this one or stuff like that, or if you add this, how does it affect the
**[01:27:37]** complexity of the rest of the kind of network of proofs? So can you like make a loss function
**[01:27:41]** that adds, Oh, I want this proof to be a really highly powerful proof. Um, I think some people
**[01:27:47]** are trying to work on that. So, so maybe you can automate the creativity part. Um,
**[01:27:52]** if you had true AGI, it would do everything a human can do. So it would also do the things
**[01:27:55]** that the creative mathematicians do. But, um, but way barring that, I think just RLVRing the
**[01:28:00]** crap out of proofs. Um, well, I think that's going to be just a really useful tool for
**[01:28:05]** mathematicians. It's going to accelerate math a lot and change it a lot, but not necessarily
**[01:28:10]** immediately change everything about it. Will we get, you know, mechanical proof of the
**[01:28:17]** Riemann hypothesis or something like that, or things like that? Maybe. I don't know.
**[01:28:21]** I don't know enough details of how hard these things are to search for. And I'm not sure
**[01:28:25]** anyone can fully predict that just as we couldn't exactly predict when go would be solved or
**[01:28:30]** something like that. Um, and I think it's going to have lots of really cool applied applications.
**[01:28:36]** So, um, one of the things you want to do is you want to have provably stable,
**[01:28:43]** secure, unhackable, et cetera, software. So you can write math proofs about software
**[01:28:49]** and say this code, not only does it pass these unit tests, but I can mathematically prove that
**[01:28:55]** there's no way to hack it in these ways, or no way to mess with the memory or this type of things
**[01:28:59]** that hackers use, um, or it has these properties. It can use the same lean and same proof to do
**[01:29:08]** formally verified software. I think that's going to be a really powerful piece of cybersecurity.
**[01:29:12]** Um, that's relevant for all sorts of other AI hacking the world stuff. And that, yeah,
**[01:29:19]** if you can prove a Riemann hypothesis, you're also going to be able to, to prove
**[01:29:23]** insanely complex things about very complex software. And then you'll be able to ask the
**[01:29:26]** LLM synthesize me a software that is, uh, I can prove is correct. Right.
**[01:29:32]** Soterios Johnson Why hasn't provable, um,
**[01:29:36]** programming language taken off as a result of LLMs? You would think that this would-
**[01:29:41]** Matthew Feeney I think it's starting to. Yeah,
**[01:29:42]** I think it's starting to, I think that one, one challenge, and we are actually
**[01:29:46]** incubating a potential focus research organization on this is the specification problem. So
**[01:29:51]** mathematicians are kind of know what interesting theorems they want to formalize. Um, if I have
**[01:29:56]** some code, let's say I have some code that is involved in running the power grid or something.
**[01:30:00]** that has some security properties.
**[01:30:02]** Well, what is the formal spec of those properties?
**[01:30:06]** The power grid engineers just made this thing,
**[01:30:09]** but they don't necessarily know how to lift
**[01:30:11]** the formal spec from that.
**[01:30:13]** And it's not necessarily easy to come up with the spec
**[01:30:15]** that is the spec that you want for your code.
**[01:30:17]** People aren't used to coming up with formal specs
**[01:30:19]** and there are not a lot of tools for it.
**[01:30:21]** So you also have like this kind of user interface
**[01:30:23]** plus AI problem of like,
**[01:30:25]** what security specs should I be specifying?
**[01:30:27]** Is this the spec that I wanted?
**[01:30:29]** So there's a spec problem.
**[01:30:32]** And it's just been really complex and hard,
**[01:30:34]** but it's only just in the last very short time
**[01:30:37]** that the LLMs are able to generate verifiable proofs
**[01:30:43]** of things that are useful to mathematicians,
**[01:30:47]** starting to be able to do some amount of that
**[01:30:49]** for software verification, hardware verification.
**[01:30:52]** But I think if you project the trends
**[01:30:54]** over the next couple of years,
**[01:30:57]** it's possible that it just flips the tide
**[01:30:59]** that formal methods,
**[01:31:00]** basically this whole field of formal methods
**[01:31:01]** or formal verification, provable software,
**[01:31:05]** which is kind of this weird, almost like backwater
**[01:31:07]** of more like theoretical part of programming languages
**[01:31:10]** and stuff, very academically flavored often.
**[01:31:14]** Although there was like this DARPA program
**[01:31:16]** that made like a provably secure,
**[01:31:18]** like quadcopter, helicopter and stuff like that.
**[01:31:21]** So secure against,
**[01:31:22]** like what is the property that is exactly brewed?
**[01:31:25]** And not for that particular project,
**[01:31:27]** but just in general,
**[01:31:28]** like what, because obviously the things malfunction
**[01:31:32]** for all kinds of reasons.
**[01:31:33]** Like you could say that what's going on
**[01:31:37]** in this part of the memory over here,
**[01:31:38]** which is supposed to be the part that user can access,
**[01:31:41]** can't in any way affect what's going on in the memory
**[01:31:44]** over here or something like that.
**[01:31:45]** Or yeah, things like that.
**[01:31:48]** Yeah.
**[01:31:48]** Got it.
**[01:31:49]** Yeah.
**[01:31:50]** So there's two questions.
**[01:31:52]** One is, how useful is this?
**[01:31:56]** And two is like, how satisfying as a mathematician
**[01:32:03]** would it be?
**[01:32:05]** And the fact that there's this application
**[01:32:07]** towards proving that software has certain properties
**[01:32:10]** or hardware certain properties,
**[01:32:11]** obviously like if that works,
**[01:32:12]** that would obviously be very useful.
**[01:32:14]** But from a pure, like,
**[01:32:16]** are we going to figure out with mathematics?
**[01:32:18]** Right.
**[01:32:20]** Yeah.
**[01:32:22]** Is your sense that there's something about
**[01:32:24]** finding that one construction cross maps
**[01:32:28]** to another construction in a different domain
**[01:32:30]** or finding that, oh, this like lemma is,
**[01:32:33]** if you reconfigure it,
**[01:32:35]** like if you redefine this term,
**[01:32:38]** it's still like kind of satisfies
**[01:32:39]** what I meant by this term,
**[01:32:40]** but a counter example that previously we knocked it down
**[01:32:44]** no longer applies.
**[01:32:45]** Like that kind of dialectical thing
**[01:32:47]** that happens in mathematics.
**[01:32:48]** Will the software like replace that?
**[01:32:50]** Yeah.
**[01:32:51]** And like how much of the value
**[01:32:51]** of this sort of pure mathematics just comes from
**[01:32:54]** actually just coming up with
**[01:32:56]** entirely new ways of thinking about a problem?
**[01:32:58]** Yeah.
**[01:32:59]** Like mapping it to a totally different representation.
**[01:33:01]** And do we have examples of?
**[01:33:03]** I don't know.
**[01:33:04]** I think of it as,
**[01:33:04]** I think of it maybe a little bit like the,
**[01:33:07]** when everybody had to write assembly code
**[01:33:09]** or something like that,
**[01:33:11]** just like the amount of fun,
**[01:33:12]** like cool startups that got created
**[01:33:13]** was like a lot less or something, right?
**[01:33:15]** And so it was just like less people could do it.
**[01:33:19]** Progress was more grinding and slow and lonely and so on.
**[01:33:23]** You had more false failures
**[01:33:24]** because you didn't get something
**[01:33:25]** about the assembly code, right?
**[01:33:26]** Rather than the essential thing of like,
**[01:33:27]** what's your concept, right?
**[01:33:31]** Harder to collaborate and stuff like that.
**[01:33:33]** And so I think it will like be really good.
**[01:33:38]** There is some worry that by not learning
**[01:33:40]** to do the mechanical parts of the proof
**[01:33:41]** that you fail to generate the intuitions
**[01:33:44]** that inform the more conceptual parts,
**[01:33:45]** the creative part, right?
**[01:33:47]** Yeah.
**[01:33:48]** It's the same with assembly.
**[01:33:48]** Right.
**[01:33:49]** And so at what point is that applying as vibe coding
**[01:33:52]** or people not learning computer science, right?
**[01:33:54]** Or actually, are they like vibe coding
**[01:33:56]** and they're also simultaneously looking at the LLM?
**[01:33:59]** It's like explaining them
**[01:33:59]** these abstract computer science concepts
**[01:34:01]** and it's all just like all happening faster.
**[01:34:02]** Their feedback loop is faster
**[01:34:03]** and they're learning way more abstract computer science
**[01:34:05]** and algorithm stuff because they're vibe coding.
**[01:34:08]** You know, I don't know.
**[01:34:09]** It's not obvious.
**[01:34:10]** That might be something like the user interface
**[01:34:12]** and the human infrastructure around it.
**[01:34:15]** But I guess there's some worry
**[01:34:16]** that people don't learn the mechanics
**[01:34:19]** and therefore don't build like the grounded intuitions
**[01:34:21]** or something.
**[01:34:22]** But my hunch is it's like super positive.
**[01:34:25]** Exactly on net how useful that will be
**[01:34:27]** or how much overall math like breakthroughs
**[01:34:29]** or like math breakthroughs
**[01:34:31]** even that we care about will happen.
**[01:34:33]** I don't know.
**[01:34:34]** I mean, one other thing that I think is cool
**[01:34:35]** is actually the accessibility question.
**[01:34:37]** It's like, okay, that sounds a little bit corny.
**[01:34:39]** Okay, and more people can do math, but who cares?
**[01:34:43]** But I think there's actually lots of people
**[01:34:44]** that like could have interesting ideas
**[01:34:45]** like maybe the quantum theory of gravity or something.
**[01:34:49]** Like, yeah, one of us will come up
**[01:34:53]** with a quantum theory of gravity
**[01:34:54]** instead of like a card-carrying physicist.
**[01:34:56]** In the same way that Steve Burns
**[01:34:57]** is like reading the neuroscience literature
**[01:34:59]** and he's like hasn't been in a neuroscience lab that much,
**[01:35:02]** but he's like able to synthesize
**[01:35:03]** across the neuroscience literature
**[01:35:04]** and be like, oh, learning subsystem, steering subsystem.
**[01:35:06]** Does this all make sense?
**[01:35:07]** He's, you know, it's kind of like
**[01:35:09]** he's an outsider neuroscientist in some ways.
**[01:35:12]** Can you have outsider, you know,
**[01:35:13]** string theorists or something
**[01:35:14]** because the math is just done for them by the computer?
**[01:35:18]** And does that lead to more innovation
**[01:35:19]** in the string theory, right?
**[01:35:21]** Maybe, yes.
**[01:35:22]** So.
**[01:35:23]** Okay, so if this approach works
**[01:35:26]** and you're right that LLMs are not the final paradigm
**[01:35:29]** and suppose it takes at least 10 years
**[01:35:31]** to get the final paradigm.
**[01:35:32]** In that world, there's this fun sci-fi premise
**[01:35:34]** where you have, Terrence Tao today had a tweet
**[01:35:39]** where he's like, these models are like automated cleverness
**[01:35:43]** but not automated intelligence.
**[01:35:44]** And you can quibble with the definitions there.
**[01:35:47]** But yeah, if you have automated cleverness
**[01:35:49]** and you have some way of filtering,
**[01:35:53]** which if you can formalize and prove things
**[01:36:00]** that the LLMs are saying you could do,
**[01:36:03]** then you could have this situation
**[01:36:04]** where quantity has a quality all of its own.
**[01:36:06]** And so what are the domains of the world
**[01:36:10]** which could be put in this provable symbolic representation?
**[01:36:14]** Yeah.
**[01:36:15]** And furthermore, okay, so in the world
**[01:36:17]** where just AGI is super far away,
**[01:36:18]** maybe it makes sense to like literally turn everything
**[01:36:20]** the LLMs ever do or almost everything they do
**[01:36:23]** into like super provable statements.
**[01:36:25]** And so LLMs can actually build on top of each other
**[01:36:27]** because everything they do is like super provable.
**[01:36:30]** Yeah.
**[01:36:30]** Maybe this is like just necessary
**[01:36:32]** because you have billions of intelligences running around
**[01:36:34]** even if they are super intelligent.
**[01:36:35]** The only way the future AGI civilization
**[01:36:37]** can collaborate with each other
**[01:36:39]** is if they can prove each step.
**[01:36:41]** Yeah, yeah.
**[01:36:42]** And they're just like brute force churning out,
**[01:36:44]** this is what the Jupiter brains are doing.
**[01:36:46]** It's a universal language, it's provable.
**[01:36:48]** And it's also provable from like,
**[01:36:49]** are you trying to exploit me?
**[01:36:51]** Or are you sending me some message
**[01:36:53]** that's actually trying to like sort of hack
**[01:36:54]** into my brain effectively?
**[01:36:56]** Are you trying to socially influence me?
**[01:36:57]** Are you actually just like sending me
**[01:36:59]** just the information that I need and no more for this?
**[01:37:02]** And yeah, so Davi Dodd,
**[01:37:03]** who's like this program director at ARIA now in the UK.
**[01:37:07]** I mean, he has this whole design
**[01:37:09]** of a kind of ARPA style program
**[01:37:12]** of sort of safeguarded AI that very heavily leverages
**[01:37:15]** like provable safety properties.
**[01:37:17]** And can you apply proofs to like,
**[01:37:19]** can you have a world model,
**[01:37:20]** but that world model is actually not specified
**[01:37:22]** just in neuron activations,
**[01:37:23]** but it's specified in equations.
**[01:37:26]** Those might be very complex equations,
**[01:37:28]** but if you can just get insanely good
**[01:37:30]** at just auto-proving these things with cleverness,
**[01:37:33]** auto-cleverness,
**[01:37:34]** can you have explicitly interpretable world models,
**[01:37:40]** as opposed to neural net world models
**[01:37:41]** and like move back basically to symbolic methods
**[01:37:44]** just because you can just have insane amount
**[01:37:46]** of ability to prove things.
**[01:37:48]** Yeah, I mean, that's an interesting vision.
**[01:37:50]** I don't know how, in the next 10 years,
**[01:37:51]** like whether that will be the vision that plays out,
**[01:37:53]** but I think it's really interesting to think about.
**[01:37:57]** Yeah, and even for math,
**[01:37:58]** I mean, I think Terry Tao is like doing some amount of stuff
**[01:38:01]** where it's like, it's not about
**[01:38:02]** whether you can prove the individual theorems,
**[01:38:04]** it's like, let's prove all the theorems on mass.
**[01:38:06]** And then it's like study the properties
**[01:38:08]** of like the aggregate set of proved theorems, right?
**[01:38:11]** Which are the ones that got proved
**[01:38:12]** and which are the ones that didn't?
**[01:38:13]** Okay, well, that's like the landscape of all the theorems
**[01:38:16]** instead of one theorem at a time, right?
**[01:38:18]** Speaking of symbolic representations,
**[01:38:20]** one question I was meaning to ask you is,
**[01:38:22]** how does the brain represent the world model?
**[01:38:25]** It's like, obviously nets out in neurons,
**[01:38:26]** but I don't mean sort of extremely functionally.
**[01:38:29]** I mean, sort of conceptually,
**[01:38:31]** is it in something that's analogous
**[01:38:33]** to the hidden state of a neural network,
**[01:38:35]** or is it something that's closer to a symbolic language?
**[01:38:39]** We don't know.
**[01:38:40]** I mean, I think there's some amount of study of this.
**[01:38:42]** I mean, there's these things like, you know,
**[01:38:44]** face patch neurons that represent certain parts of the face
**[01:38:47]** that geometrically combine in interesting ways.
**[01:38:49]** That's sort of with geometry and vision.
**[01:38:51]** Is that true for like other more abstract things?
**[01:38:53]** There's like this idea of cognitive maps,
**[01:38:55]** like a lot of the stuff that a rodent hippocampus
**[01:38:57]** has to learn is like place cells,
**[01:39:00]** and like, where is the rodent going to go next?
**[01:39:02]** And is it going to get a reward there?
**[01:39:05]** It's like very geometric.
**[01:39:05]** And like, do we organize concepts
**[01:39:08]** with like an abstract version of a spatial map?
**[01:39:13]** There's some questions of,
**[01:39:14]** can we do like true symbolic operations?
**[01:39:16]** Like, can I have like a register in my brain
**[01:39:17]** that copies a variable to the another register,
**[01:39:20]** regardless of what the content of that variable is?
**[01:39:23]** That's like this variable binding problem.
**[01:39:25]** And basically I just don't,
**[01:39:26]** I don't know if we have that like machinery
**[01:39:28]** or if it's like more like cost functions and architectures
**[01:39:31]** that like make some of that approximately emerge,
**[01:39:33]** but maybe it would also emerge in a neural net.
**[01:39:36]** There's a bunch of interesting neuroscience research
**[01:39:37]** trying to study this, what the representations look like.
**[01:39:41]** But what was your hunch?
**[01:39:43]** My hunch is it's going to be a huge mess
**[01:39:44]** and we should look at the architectures,
**[01:39:45]** the loss functions and the learning rules.
**[01:39:47]** And we shouldn't really,
**[01:39:48]** I don't expect it to be pretty in there, yeah.
**[01:39:51]** Which is that it's not a symbolic language type thing.
**[01:39:53]** Yeah, probably, probably it's not that symbolic.
**[01:39:56]** Yeah, but other people think very differently, you know?
**[01:39:59]** Yeah.
**[01:40:00]** Other random questions, speaking of binding.
**[01:40:03]** Yeah, what is up with feeling like there's an experience
**[01:40:06]** that it's like both all the parts of your brain,
**[01:40:09]** which are modeling very different things,
**[01:40:11]** have different drives, feel like, at least presumably,
**[01:40:14]** feel like there's an experience happening right now.
**[01:40:16]** And also that across time you feel like, what is-
**[01:40:20]** Yeah, I'm pretty much at a loss on this one.
**[01:40:25]** I don't know.
**[01:40:26]** I mean, Max Hodak has been giving talks about this recently.
**[01:40:31]** He's another really hardcore neuroscience person,
**[01:40:36]** neurotechnology person.
**[01:40:38]** And the thing I mentioned with Dorso is maybe also,
**[01:40:41]** it sounds like it might have some touching on this question,
**[01:40:43]** but yeah, I don't think anybody has any idea.
**[01:40:49]** It might even involve new physics.
**[01:40:50]** It's like, you know?
**[01:40:52]** Yeah.
**[01:40:54]** Another question, which might not have an answer yet.
**[01:40:57]** What, so continual learning,
**[01:41:01]** is that the product of something extremely fundamental
**[01:41:06]** at the level of even the learning algorithm
**[01:41:08]** where you could say, look,
**[01:41:10]** at least the way we do back-propagating neural networks
**[01:41:12]** is that you freeze the way,
**[01:41:13]** there's a training period and you freeze the weights.
**[01:41:16]** And so you just need this active inference
**[01:41:19]** or some other learning rule in order to do continual learning
**[01:41:22]** or do you think it's more a matter of architecture
**[01:41:25]** and how is memory exactly stored?
**[01:41:27]** And is it like,
**[01:41:28]** what kind of associative memory you have basically?
**[01:41:30]** Yeah, so continual learning, I don't know.
**[01:41:34]** I think that there's probably things that,
**[01:41:37]** there's probably some, at the architectural level,
**[01:41:39]** there's probably something interesting stuff
**[01:41:40]** that the Hippocampus is doing.
**[01:41:42]** And people have long thought this.
**[01:41:49]** What kinds of sequences is it storing?
**[01:41:51]** How is it organizing, representing that?
**[01:41:53]** How is it replaying it back?
**[01:41:54]** What is it replaying back?
**[01:41:57]** How is it exactly how that memory consolidation works
**[01:42:01]** in sort of training the cortex using replays
**[01:42:03]** or memories from the Hippocampus or something like that?
**[01:42:08]** There's probably some of that stuff.
**[01:42:09]** There might be multiple timescales of plasticity
**[01:42:11]** or sort of clever learning rules
**[01:42:14]** that can kind of, I don't know,
**[01:42:15]** can sort of simultaneously kind of be storing
**[01:42:17]** sort of short-term information
**[01:42:19]** and also doing back prop with it.
**[01:42:21]** I mean, neurons might be doing a couple of things,
**[01:42:22]** some fast weight plasticity
**[01:42:24]** and some slower plasticity at the same time
**[01:42:26]** or synapses that have many states.
**[01:42:28]** I mean, I don't know.
**[01:42:29]** I mean, I think that from a neuroscience perspective,
**[01:42:31]** I'm not sure that I've seen something that's super clear
**[01:42:34]** on what continual learning, what causes it,
**[01:42:36]** except maybe to say that this systems consolidation idea
**[01:42:40]** of sort of Hippocampus consolidating the cortex,
**[01:42:42]** like some people think is a big piece of this
**[01:42:44]** and we don't still fully understand the details.
**[01:42:46]** Yeah.
**[01:42:47]** Speaking of fast weights,
**[01:42:48]** is there something in the brain
**[01:42:51]** which is the equivalent of this distinction
**[01:42:53]** between parameters and activations
**[01:42:54]** that we see in neural networks?
**[01:42:56]** And specifically like in transformers,
**[01:42:59]** we have this idea like some of the activations
**[01:43:03]** are the key and value vectors of previous tokens
**[01:43:10]** that you build up over time.
**[01:43:12]** And there's like the so-called the fast weights
**[01:43:14]** that you, whenever you have a new token,
**[01:43:16]** you query them against these,
**[01:43:18]** you query these activations,
**[01:43:20]** but you also obviously query them
**[01:43:21]** against all the other parameters in the network,
**[01:43:23]** which are part of the actual built-in weights.
**[01:43:25]** Is there some such distinction that's analogous?
**[01:43:27]** I don't know.
**[01:43:28]** I mean, we definitely have weights and activations.
**[01:43:30]** Whether you can use the activations in these clever ways,
**[01:43:35]** different forms of like actual attention,
**[01:43:37]** like attention in the brain,
**[01:43:39]** is that based on, I'm trying to pay attention.
**[01:43:42]** I think there's several,
**[01:43:43]** probably several different kinds
**[01:43:44]** of like actual attention in the brain.
**[01:43:46]** I want to pay attention to this area of visual cortex.
**[01:43:49]** I want to pay attention to this,
**[01:43:52]** the content in other areas
**[01:43:54]** that is triggered by the content in this area, right?
**[01:43:57]** Attention that's just based on kind of reflexes
**[01:43:59]** and stuff like that.
**[01:44:00]** So I don't know.
**[01:44:01]** I mean, I think that there's not just the cortex,
**[01:44:03]** there's also the thalamus.
**[01:44:05]** The thalamus is also involved in kind of somehow relaying
**[01:44:07]** or gating information.
**[01:44:09]** There's cortical-cortical connections.
**[01:44:10]** There's also some amount of connection
**[01:44:11]** between cortical areas that goes through the thalamus.
**[01:44:14]** Is it possible that this is doing some sort of matching
**[01:44:17]** or kind of constraint satisfaction
**[01:44:20]** or matching across keys over here and values over there?
**[01:44:25]** Is it possible that it can do stuff like that?
**[01:44:27]** Maybe.
**[01:44:28]** I don't know.
**[01:44:29]** This is all part of what's the architecture
**[01:44:30]** of this cortical-thalamic system.
**[01:44:33]** I don't know how transformer-like it is
**[01:44:35]** or if there's anything analogous to that attention.
**[01:44:39]** Be interesting to find out.
**[01:44:41]** We're gonna give you a billion dollars
**[01:44:43]** so we can come on the podcast again
**[01:44:45]** and tell me how exactly that works.
**[01:44:48]** Mostly I just do data collection.
**[01:44:49]** It's like really, really unbiased data collection
**[01:44:51]** so all the other people can figure out these questions.
**[01:44:54]** Maybe the final question to go off on
**[01:44:57]** is what was the most interesting thing
**[01:44:59]** you learned from the GapMap?
**[01:45:01]** And if you wanna explain what the GapMap is.
**[01:45:03]** So the GapMap, so in the process of incubating
**[01:45:07]** and coming up with these focused research organizations,
**[01:45:10]** these sort of nonprofit startup-like moonshots
**[01:45:14]** that we've been getting philanthropists
**[01:45:15]** and now government agencies to fund,
**[01:45:18]** we talked to a lot of scientists.
**[01:45:20]** And some of the scientists were just like,
**[01:45:22]** here's the next thing my graduate student will do.
**[01:45:24]** Here's what I find interesting.
**[01:45:26]** Exploring these really interesting hypothesis spaces,
**[01:45:28]** like all the types of things we've been talking about.
**[01:45:30]** And some of them are like, here's this gap.
**[01:45:34]** I need this piece of infrastructure,
**[01:45:35]** which there's no combination of grad students in my lab
**[01:45:38]** or me loosely collaborating with other labs
**[01:45:40]** with traditional grants that could ever get me that.
**[01:45:43]** I need to have an organized engineering team
**[01:45:45]** that builds the miniature equivalent
**[01:45:47]** of the Hubble Space Telescope.
**[01:45:49]** And if I can build that Hubble Space Telescope,
**[01:45:51]** then I will unblock all the other researchers in my field
**[01:45:54]** or some path of technological progress
**[01:45:56]** in the way that the Hubble Space Telescope
**[01:45:58]** lifted the boats, improved the life of every astronomer,
**[01:46:01]** but wasn't really an astronomy discovery in itself.
**[01:46:03]** It was just like, you had to put this giant mirror in space
**[01:46:05]** with a CCD camera and like organize all the people
**[01:46:07]** and engineering and stuff to do that.
**[01:46:10]** So some of the things we talked to scientists about
**[01:46:12]** look like that.
**[01:46:13]** And so the gap map is basically just like a list
**[01:46:15]** of a lot of those things.
**[01:46:16]** And it's like, we call it a gap map.
**[01:46:19]** I think it's actually more like
**[01:46:20]** a fundamental capabilities map.
**[01:46:21]** Like what are all these things
**[01:46:22]** like mini Hubble Space Telescopes?
**[01:46:25]** And then we kind of organize that into gaps
**[01:46:28]** for like helping people understand that or like search that.
**[01:46:32]** And what was the most surprising thing you found?
**[01:46:35]** So, I mean, I think I've talked about this before,
**[01:46:37]** but I think it, one thing is just like,
**[01:46:40]** kind of like the overall size or shape of it
**[01:46:42]** or something like that is like,
**[01:46:43]** it's like a few hundred fundamental capabilities.
**[01:46:47]** So if each of those was like a deep tech startup
**[01:46:49]** sized project, that's like only a few billion dollars
**[01:46:51]** or something like, you know,
**[01:46:52]** each one of those was a series A.
**[01:46:53]** That's only like not, you know,
**[01:46:55]** it's not like a trillion dollars to solve these gaps.
**[01:46:57]** It's like lower than that.
**[01:46:59]** And so that's like one,
**[01:47:01]** maybe we assumed that and we also came to,
**[01:47:03]** that's what we got.
**[01:47:04]** It's not really comprehensive.
**[01:47:05]** It's really just a way of summarizing
**[01:47:06]** a lot of conversations we've had with scientists.
**[01:47:11]** I do think that in the aggregate process,
**[01:47:12]** like things like lean are actually like surprising.
**[01:47:15]** Cause I did start from sort of neuroscience and biology.
**[01:47:17]** And it was like very obvious
**[01:47:18]** that there's sort of like these omics.
**[01:47:20]** We need genomics, but we also need connectomics.
**[01:47:22]** And, you know, we can engineer E. coli,
**[01:47:25]** but we also need to engineer the other cells.
**[01:47:26]** And it's like, there's like somewhat obvious parts
**[01:47:28]** of biological infrastructure.
**[01:47:30]** I did not realize that like math proving infrastructure
**[01:47:32]** like was a thing.
**[01:47:33]** And so, and that was kind of like emergent
**[01:47:37]** from trying to do this.
**[01:47:37]** So I'm looking forward to seeing other things
**[01:47:40]** where it's like not actually this like hard
**[01:47:42]** intellectual problem to solve it.
**[01:47:44]** It's maybe the kind of the slightly the equivalent
**[01:47:46]** of AI researchers just needed GPUs
**[01:47:47]** or something like that and focus
**[01:47:50]** and really good PyTorch code to like start doing this.
**[01:47:53]** Like what is the full diversity of fields
**[01:47:56]** in which that exists?
**[01:47:59]** We've even now found,
**[01:48:03]** and which are the fields that do or don't need that.
**[01:48:05]** So fields that have had gazillions of dollars of investment,
**[01:48:08]** do they still need some of those?
**[01:48:10]** Do they still have some of those gaps
**[01:48:11]** or is it only more like neglected fields?
**[01:48:16]** We're even finding some interesting ones
**[01:48:17]** in actual astronomy, actual telescopes
**[01:48:19]** that have not been explored,
**[01:48:21]** maybe because of the kind of,
**[01:48:25]** if you're getting above a critical mass size project,
**[01:48:27]** then you have to have like a really big project
**[01:48:29]** and that's a more bureaucratic process
**[01:48:30]** with the federal agencies, yeah.
**[01:48:32]** Yes, I guess you just kind of need scale
**[01:48:35]** in every single domain of science these days.
**[01:48:36]** Yeah, I think you need scale
**[01:48:37]** in many of the domains of science.
**[01:48:39]** And that does not mean
**[01:48:39]** that the low scale work is not important.
**[01:48:43]** It does not mean that the kind of creativity,
**[01:48:44]** serendipity, et cetera,
**[01:48:46]** each student pursuing a totally different direction
**[01:48:49]** or thesis that you see in universities
**[01:48:50]** is not like also really key.
**[01:48:53]** But yeah, I think we need some amount
**[01:48:56]** of scalable infrastructure is missing
**[01:48:58]** in essentially every area of science,
**[01:49:00]** even math, which is crazy.
**[01:49:01]** Because mathematicians, I thought just needed whiteboards.
**[01:49:03]** Right, yeah.
**[01:49:04]** Right, but they actually need lean.
**[01:49:05]** They actually need verifiable programming languages
**[01:49:07]** and stuff like that.
**[01:49:08]** I didn't know that.
**[01:49:08]** Yeah, cool, Adam, this is super fun.
**[01:49:11]** Thanks for coming on.
**[01:49:12]** Thank you so much.
**[01:49:13]** Where can people find your stuff?
**[01:49:14]** The easiest way now,
**[01:49:15]** my adammarblestone.org website is currently down, I guess.
**[01:49:19]** You can find convergentresearch.org
**[01:49:21]** can link to a lot of the stuff we've been doing, yeah.
**[01:49:23]** And then you have a great blog, Longitudinal Science.
**[01:49:24]** Yes, Longitudinal Science, yes, on WordPress, yeah.
**[01:49:27]** Cool.
**[01:49:27]** Thank you so much.
**[01:49:28]** Pleasure.
**[01:49:29]** Hey, everybody.
**[01:49:30]** I hope you enjoyed that episode.
**[01:49:31]** If you did, the most helpful thing you can do
**[01:49:33]** is just share it with other people
**[01:49:35]** who you think might enjoy it.
**[01:49:37]** It's also helpful if you leave a rating
**[01:49:39]** or a comment on whatever platform you're listening on.
**[01:49:43]** If you're interested in sponsoring the podcast,
**[01:49:45]** you can reach out at dwarkesh.com slash advertise.
**[01:49:50]** Otherwise, I'll see you on the next one.
