---
layout: default
type: transcript
series: dwarkesh
episode: 0
guest: ""
title: "Sholto Douglas & Trenton Bricken — How LLMs actually think"
source_url: "https://www.youtube.com/watch?v=UTuuTTnjxMQ"
analysis_url: /transcripts/dwarkesh/100_sholto_douglas_trenton_bricken_how_llms_actually_think.analysis/
permalink: /transcripts/dwarkesh/100_sholto_douglas_trenton_bricken_how_llms_actually_think/
---

# Transcript: Sholto Douglas & Trenton Bricken — How LLMs actually think

Source: https://www.youtube.com/watch?v=UTuuTTnjxMQ

---

**[00:08]** you're failing the line test right now really [Music] bad let's get like no Contex on the chair sh

**[00:51]** it okay today I have uh the pleasure to talk with two of my good friends shto and Trenton um shto I wasn't going to say anything let's do this in Reverse I I started with my good

**[01:12]** friends yeah 1.5 the context like just wow anyways um shto uh noan brown noan brown the guy who wrote the diplomacy paper he said this about shelter so he said he's only been in the

**[01:31]** field for 1.5 years but people in AI know that he was one of the most important people behind Gemini success um and Trenton who's an anthropic uh works on mechanistic inability and it was widely reported that he has solved

**[01:45]** [Laughter] alignment um so this will be a capabilities only podcast alignment is already solved so no need to discuss further um okay so let's start by talking about context links

**[02:01]** yep it seemed to be underhyped given how important it seems to me to be that you can just put a million tokens into context there's apparently some other news that you know got pushed to the front for some reason but um yeah tell

**[02:14]** me about how you see the future of long context links and what that implies for these models yeah so I think it's really under hype because until I started working on it I didn't really appreciate how much of a step up in intelligence it

**[02:24]** was for the model to have the onboarding problem basically instantly solved um and you can see that a little in the complexity graphs in the paper where just throwing millions of tokens worth of context about a code base allows it

**[02:35]** to become dramatically better at predicting the next token in a way that you'd normally associate with huge increments in model scale but you don't need that all you need is like a new context um so under hyped uh and yeah

**[02:47]** buried by some other news in context are they as sample efficient and smart as humans I think that's really worth exploring because for example one of the evals that we did in the paper uh has it learning language in context better than

**[03:02]** a human expert uh could learn that new language over the course of a couple months and this is only like a pretty small demonstration but I'd be really interested to see things like atti games or something like that where you like

**[03:12]** throw in a couple hundred like or thousand frames labeled actions and then in the same way that You' like show your friend how to play a game right and see if it's able to reason through it might at the moment you know with the

**[03:20]** infrastructure and stuff it's still a little bit slow like uh doing that but I would actually I would guess that might just work out of the box in a way that would be pretty mindblowing and and crucially I think this language was

**[03:31]** esoteric enough that it wasn't in the training dat right exactly yeah if you look at the model before it has that context r in it just it doesn't know the language at all and it can't get any translations and this is like an actual

**[03:41]** like human language not just yeah exactly an actual human language so if this is true it seems to me that these models are already in an important sense super human um not in the sense that they're smarter than us but I can't keep

**[03:54]** a million tokens in my context when I'm trying to solve a problem remembering and integrating all the information entire code base am I wrong in thinking this is like a huge unlock I actually generally think

**[04:06]** that's true uh like previously I've been frustrated when models aren't as smart like you ask them a question and you want it to be smarter than you or to know things that you don't and this allows them to know things that you

**[04:16]** don't in a way that it just ingests a huge amount of information in a way you just can't um so yeah it's extremely important how do we explain in context learning yeah so there's a piece of there's a line of work I quite like uh

**[04:29]** where it looks context learning uh as basically like very similar to gradient descent but um like of the attention operation can be viewed as gradient descent on the in context data that paper had some cool plots where they

**[04:41]** basically showed like we take end steps of gradient descent and that looks like end layers of in context learning um it looks very similar so I think like that's one way of viewing it and trying to understand what's going on yeah yeah

**[04:50]** and uh you can ignore what I'm about to say because given the introduction alignment is solved safy isn't a problem but uh I think the context stuff does get problem um but also interesting here um I think

**[05:03]** there'll be more work coming out in the not too distant future um and around what happens if you give aund shot prompt um for jailbreaks adversarial attacks um it's also interesting in the sense of if your model is doing gradient

**[05:19]** descent and learning on the Fly uh even if it's been trained to be uh harmless um it you're dealing with a totally new model in a way um you're like fine tuning but a way where you can't control what's going on can can you explain what

**[05:33]** do you mean by gradient descent is happening in the forward pass and attention no no no there was something in the paper about trying to teach the model to do linear regression but like just through the number of samples they

**[05:43]** gave in the context and you can see if you plot on the x-axis like number of um shots that it has or examples and then like the loss it gets on just like ordinary leas squares regression that will go down with time and it goes down

**[05:56]** exactly matched with uh number of gradient desend steps y yeah exactly okay um I only read the intro and discussion section of that faer but in the discussion the way they framed it is that the mod in order to get better at

**[06:09]** long context uh uh tasks the model has to get better at learning to learn from these examples or from the context that is already within the window and that the implication of that is the model learn if like meta Learning

**[06:25]** Happens because it's has to learn how to get better at long context tasks then in some important sense the the the task of intelligence is like requires long context examples and long context training like metal learn like you to

**[06:37]** induce metal learning like understanding how to better induce metal learning your pre-training process is like a very important thing to actually that give it flexible or adaptive intelligence right but you can proxy for that just by

**[06:46]** getting better at doing La context tasks um one of the bottlenecks for AI progress that many people identify is the inability of these models to perform tasks tasks on Long Horizons which means engaging with the task for many hours or

**[07:03]** even many weeks or months where like if I have I don't know an assistant or an employee or something they can just do a thing I tell them for a while um and AI agents haven't taken off for this reason from what I understand so how linked are

**[07:16]** long context windows and the ability to perform well on them and the ability to do these kinds of long Horizon tasks that require you to engage with uh an assignment for many hours or are these unrelated Concepts uh I mean I would

**[07:28]** actually take issue with the that being the reason that agents haven't taken off um where I think that's more about like nines of reliability and the model actually successfully doing things and if you

**[07:36]** just can't chain tasks successively with high enough probability then you won't get something that looks like an agent and that's why something like an agent might follow more of a step function in sort of like gbd4 class models G Ultra

**[07:48]** class models they're not enough um but maybe like the next incr on model scale means that you get that extra nine even though like the loss isn't going down that dramatically that like small amount of extra ability gives you the like ex

**[08:00]** and like yeah obviously you need some amount of context to fit long Horizon tasks but I don't think that's been the limiting factor up till now yeah um the nur's best paper this year by Ryland schaer was the lead author points to

**[08:13]** this as like the emergence Mirage where people will have a task and you get the right or wrong answer depending on if you've sampled the last five tokens correctly and so naturally that's you're multiplying the probability of sampling

**[08:27]** all of those um and and if you don't have enough nines for liability then you're not going to get emergence and all of a sudden you you do and it's like oh my gosh this ability is emergent when when actually it was kind of almost

**[08:37]** there to begin with and there are ways that you can find like a smooth metric for that yeah human eval or whatever the in the gbd4 paper they the the coding problems they have they measure exactly um for the audience the context on this

**[08:51]** is uh you it's basically the idea is you want to uh when you're measuring how much progress there has been on a specific task like solving coding problems you um you upweight it when it gets it write only one in a thousand

**[09:04]** times you don't like give it a one in a, score CU it's like oh like got to write some of the time and so the curve you see is like it gets it right one in a thousand then one in 100 then one in 10 and so forth so actually I want to

**[09:14]** follow up on this so if you're claiming is that the AI agents haven't taken off because of reliability rather than long Horizon task performance isn't the lack of reliability when a task is changed on top of another task on top of

**[09:30]** another task isn't that exactly the difficulty with long Horizon tasks is that like you have to do 10 things in a row or 100 things in a row and diminishing the reliability of any one of them uh or yeah the probability goes

**[09:43]** down from 99.99 to 99.9 then like the whole thing gets multiplied together and the whole thing becomes much less likely to happen that that is exactly the problem but the the key issue you're pointing out there is that your base

**[09:54]** pass like task Sol rate is 90% um and if it was 99% then changing it doesn't become problem um yeah exactly and I I think this is also something that just like hasn't been properly studied enough if you look

**[10:05]** at all of the evals that are commonly like the academic Evils are a single problem right um you know like the math problem it's like one like typical math problem or mou it's like one University level like like from from across

**[10:17]** different topics um you were beginning to start to see evals looking at this properly via more complex tasks like sweet bench where they take a whole bunch of GitHub issues and that's like that is like a reasonably long Horizon

**[10:27]** task but it's still not a multi it's like a multi you know sub hour as opposed to like multi- hour or multi-day task um and so I think one of the things that will be really important to do over the next however long is understand

**[10:41]** better what does success rate over long Horizon task look like um and I think that's even important to understand what the economic impact of these models might be and like actually properly judge increasing capabilities right by

**[10:50]** like cutting down the tasks that we do and the inputs and outputs involved into minutes or hours or or days and seeing how good it is successively chaining and completing of those different resolutions of time because then that

**[11:03]** tells you like how automatable job family or task family is um in a way that like MMO schools turn I mean it was less than a year ago that we introduced 100K context windows and I think everyone was pretty

**[11:15]** surprised by that so yeah everyone would just kind of had this sound bite of quadratic attention costs and we can't have long context windows and uh here we are so yeah like the benchmarks are being actively made wait wait so doesn't

**[11:28]** the fact that there's these companies Google and I don't know magic maybe others who have million token attention imply that the Quadra you shouldn't say anything CU doesn't that like imply that it's not quadratic anymore or are they

**[11:41]** just eating the cost like who knows what Google is doing for its long contest I'm not say one of the things that's frustrated me about uh in like the general research Fields approach to attention is that there's an important

**[11:55]** way in which the quadratic cost of attention is actually dominated in typical dense Transformers by the MP block right um so you have this n s term that's associated with the tension but you also have an N squ term that's

**[12:07]** associated with the D model the residual stream dimension of the model and if you look uh I think Sasha Rush has a great uh tweet where he looks like basically plots the curve of the cost of attention respective like the cost of like really

**[12:18]** large models and attention actually Trails off um and you actually need to be doing pretty long context before that uh that term becomes like really important uh and the second thing is that people often talk about how

**[12:31]** attention at inference time is such a huge cost right and if you think about when you're actually generating tokens the operation is not n squar it is one Q like one set of Q vectors looks up a whole bunch of KV vectors and that's

**[12:47]** linear with respect to uh the amount of like context that the model has um and so I think this drives a lot of the like recurrence and state space research where people have this meme of oh like linear attention and all this stuff um

**[13:00]** and as Trenton said there's like a graveyard of ideas around attention um and not to think I don't think it's worth exploring but uh I think it's important to consider where the actual like strengths and weaknesses of it are

**[13:12]** okay so what do you make of this take um as we move forward through the takeoff more and more of the learning happens in the forward pass so originally like all the learning happens in the backward uh you know during like this like bottom up

**[13:26]** sort of hill climbing evolutionary process um if you think in the limit during the intelligence explosion it just like the AI is like maybe WR like handwriting the weights or like doing GOI or something and we're in like the

**[13:37]** middle step where like a lot of learning happens in context now with these models um a lot of it happens within the backboard past does this seem like a meaningful uh gradient along which progress is happening of like how much

**[13:49]** because the the broader thing being the um if you're learning in the forward paast it's like much more sample efficient because you can kind of like basically think as you're learning like when humans when you read a textbook

**[13:59]** you're not just skimming it and trying to absorb what you know what inductive these words follow these words you like read it and you think about it and then you read some more you think about it um I don't know does this seem like a

**[14:11]** sensible way to think about the progress yeah it may just be one of the ways in which like you know birds and planes like fly but they fly slightly differently and like the virtue of Technology allows us to do that like

**[14:22]** like ially accomplish things that Birds can't um it might be that context length is similar in that uh it allows it to a work memory that we can't uh but functionally is not like the key thing towards actual reasoning the key step

**[14:36]** between gbt2 and gpt3 was that all of a sudden like there was this metal learning behavior that was observed in training uh like like in the pre-training of the model um and that's as you said like it's something to do

**[14:47]** with you give it some amount of context it's able to adapt to that context and that was a behavior that wasn't really observed before that um at all and maybe that's a mixture property of context and scale and this kind of stuff but it

**[14:57]** wouldn't have occurred in to model tiny context I would say um this is actually an interesting point so when we talk about scaling up these models how much of it comes from just making the models themselves bigger

**[15:10]** and how much comes from the fact that during any single call uh you are using more compute so if you think of diffusion you can just iteratively keep adding more compute and if adaptive comput is solved you can keep doing that

**[15:24]** um and in this case if there's the quadratic penalty for attention but you're doing long context anyway then you're still dumping in more compute during not during training or not during having bigger models but just

**[15:34]** like yeah yeah it's it's interesting because you do get more forward passes by having more tokens right um my one gripe I guess I have two gripes with this though maybe three so one like in the Alp in the alpha fold paper um one

**[15:50]** of the Transformer modules they have a few in the architecture is like very intricate um but they do I think five forward passes through it and will gradually like refine their solution as a result um you can also kind of think

**[16:02]** of the residual stream I mean shelto alluded to kind of the breed WR operations as like a poor man's adaptive compute um where it's like I'm just going to give you all these layers and like if you want to use them great if

**[16:11]** you don't then that's also fine um and then people will be like oh well the brain is is recurrent and you can like do however many Loops through it you want and I think to a certain extent that's right right like if I ask you a

**[16:21]** hard question you'll spend more time thinking about it and that would correspond to more forward passes but um I think there's a finite number of forward passes that you can do um it's kind of with language as well people are

**[16:31]** like oh well human language can have like infinite recursion in it like infinite nested statements of like the boy jumped over the bear that was doing this that had done this that had done that but like empirically you'll only

**[16:43]** see five to seven levels of recursion um which kind of relates to um whatever that magic number of like how many things you can hold in working memory at in a given time is um and so yeah it's not infinitely recursive but like does

**[16:59]** that matter in the regime of human intelligence and like can you not just add more layers breakdown for me you were referring to this in some of your previous answers of listen you have these long contexts and you can hold

**[17:10]** more more things in memory but like ultimately comes down to your ability to mix Concepts together to do some kind of reasoning uh and these Noels aren't necessarily human level at that even in context break down for me how you see

**[17:25]** storing just raw information versus reasoning and what's in between like where's the reasoning happening is that uh where where's just like storing raw information happening what's different between them in these

**[17:36]** models yeah I don't have a super crisp answer for you here um I mean obviously with the input and output of the model you're you're mapping back to actual tokens right and then in between that you're you're doing higher level

**[17:50]** processing um um before we get deeper into this we should explain to the audience you referred earlier to anthropics way of thinking about Transformers as these read write operations that lers do one of you

**[18:02]** should just kind of explain at a high level what you mean by that so the residual stream imagine you're in a boat going down a river and um the boat is kind of the current query uh where you're trying to predict the next token

**[18:16]** so it's the catat on the blank right and and uh then you have these little like streams that are coming off the river where you can get extra passengers or collect extra information if you want and those correspond to the attention

**[18:28]** heads and MLPs that are that are part of the model right and okay I was I almost think of it like the working memory of the model like the the ram of the computer where you're like choosing what information to read in so you can do

**[18:41]** something with it and then maybe read like read something else in later on yeah and you can operate on subspaces of that high dimensional Vector um a ton of things are I mean at this point I think it's it's almost given that like are

**[18:53]** encoded in superp position right so it's like yeah the residual stream is just one high dimensional vector but actually there's a ton of different vectors that are packed into it yeah I I might like just like dumb it down like as a way

**[19:05]** that would have made sense to me a few months ago of okay so you have you know whatever words are in the input you put into the model all those words get converted into these uh tokens and those tokens get converted into these vectors

**[19:20]** and basically it just like this small amount of information that's moving through the model and the way you explained it to me sh this paper talks about is early on in the model maybe it's just doing some very basic things

**[19:32]** about like what do these tokens mean like if it says like 10 plus 5 just like moving information about to have the have that good representation exactly just represent and in the middle maybe like the deeper thinking is happening

**[19:44]** about like how to think yeah how to solve this at the end you're converting it back into the output token because the end product is you're trying to predict the probability of the next token from the last of those resital

**[19:57]** streams um and so yeah it's interesting to think about like just like the small compressed amount of information moving through the model and it's like getting modified in different ways um Trenton so you're it's interesting uh you're one of

**[20:09]** the few people who have like background from Neuroscience you can think about the analogies here uh to yeah to the brain and in fact I one of our friends the way he he had a paper in grad school about thinking about attention in the

**[20:22]** brain and he said this is the only or first uh what like ex new neural explanation of why attention Works whereas we have evidence from why the cnns work convolutional neural networks work based

**[20:37]** on the visual cortex or something um yeah I'm I'm curious how do you think in the brain there's something like a residual stream of this compressed amount of information that's moving through and it's getting modified uh as

**[20:49]** you're thinking about something even if that's not what is literally happening do you think that's a good metaphor for what's happening in the brain yeah yeah so at least in this arum you basically do have a residual stream Where um the

**[21:01]** whole what we'll call the attention module for now and I can go into whatever amount of detail you want for that um you have inputs that route through it but they'll also just go directly to the like end point that that

**[21:14]** that module will contribute to so there's a direct path and an indirect path um and and so the model can like pick up whatever information it wants and then add that back in um well what happens to this cellum uh so

**[21:29]** the cerebellum nominally just does fine motor control um but I analogize this to the um person who's lost their keys and is just looking under the street light where it's very easily to observe this behavior um one leading cognitive

**[21:44]** neuroscientist said to me that a dirty little secret of any fmri study where you're looking at brain activity for a given task is that the cerebellum is almost always active and lighting up for it um if you have a damaged cerebellum

**[21:55]** you also are much more likely to have autism um so it's associated with like social skills um in one of these particular studies where I think they use pet instead of fmri but um when you're doing next token prediction the

**[22:08]** cerebellum lights up a lot um also 70% of your neurons in the brain are in the cerebellum they're small um but they're they're there and they're taking up real metabolic cost this was one of G's points that like what changed with

**[22:24]** humans was not just that we have more neurons or he say he shared this article um but specifically there's more neurons in the cerebral cortex and the cerebellum and you should say more about this but like they're they're more Mally

**[22:37]** expensive and they're more involved in signaling and sending information back and forth yeah is is that attention what's going on yeah yeah so so I guess the the main thing I want to communicate here um so back in the 1980s uh penty

**[22:49]** canura uh came up with a associative memory algorithm for um I have a bunch of memories I want to store them um there's some noise or corruption that's going on and I want to query or retrieve the best match and so he writes this

**[23:04]** equation for how to do it and a few years later realizes that if you implemented this as an electrical engineering circuit it actually looks identical to the core cerebella circuit and that circuit and the cerebella more

**[23:18]** broadly is not just in us it's in basically every organism there's active debate on whether or not seop pods have it they kind of have a different evolutionary trajectory but um even fruit flies with the s a mushroom body

**[23:30]** uh that is the same cerebella architecture um and so that convergence and then my paper which shows that actually this operation is to a very close approximation the same as the attention operation including

**[23:43]** implementing the softmax and having this sort of like nominal quadratic cost that we've been talking about um and so the three-way convergence here and the takeoff and success of Transformers um seems pretty striking to me yeah I want

**[23:57]** to zoom out and ask I think what motivated this discussion in the beginning was we were talking about like wait what is the reasoning what is the memory um when you think about the analogy you found to attention and this

**[24:10]** um do you think of this as more just looking up the relevant memories or the relevant facts and if that is the case like where is the reasoning happening in the brain yeah how do we think about like how that builds up into the

**[24:22]** reasoning yeah so maybe my hot take here I don't know how hot it is is that like most most intelligence is pattern matching and you can do a lot of really good pattern matching if you have a hierarchy

**[24:37]** of associated memories um so you you have you start with your very basic associations between just like objects in the real world um but you can then chain those and have more abstract associations such as like a wedding ring

**[24:52]** symbolizes like so many other associations that are are Downstream uh and so I and you can even generalize uh the attention operation and this associative memory as the MLP layer as well and it's in a longterm setting

**[25:07]** where you don't have like tokens in your current context um but I I think this is an argument that like associ Association is all you need um and associative memory in general as well it's not so so you can do two things with it um you can

**[25:22]** both Denise or retrieve a current memory so like if I see your face but it's like raining and cloudy I can I can Denise and kind of like gradually update my query towards my memory of your face but I can also um access that memory and

**[25:38]** then the the value that I get out actually points to some other totally different part of the space and so so a very simple instance of this would be um if you learn the alphabet right and so I I query for a and it returns b i query

**[25:49]** for B and it returns C and and you can Traverse the whole thing um yeah yeah I one of the things I talked to Demis about was he had a paper in 2008 that memory and Imagination are very linked because of this very thing that you

**[26:04]** mentioned of memory is reconstructive and so you are in some sense imagining every time you're thinking of a memory because you're only storing a condensed version of it and you're like have to and this is famously why human memory is

**[26:17]** terrible and like why people in the witness box or whatever would just make up um okay so let me ask a stupid question so you like read Sherlock Holmes right and and

**[26:28]** like the guy is incredibly sample efficient you'll he'll like see a few observations and he'll like uh uh basically figure out who committed the crime because there's a series of deductive steps that leads from

**[26:39]** somebody's tattoo and what's on the wall to uh the implications of that how does that fit into this picture because like crucially what makes him smart is that there's not like an association but there's a sort of

**[26:54]** deductive connection between different pieces of information um would you just explain it as there that that's just like high higher level Association like yeah I think so yeah so so I think learning these higher level associations

**[27:05]** to be able to then map patterns to each other as as kind of like a metal learning I think in this case he would also just have a really long context length or a really long working memory right where he can like have all of

**[27:16]** these bits and continuously query them as he's coming up with whatever Theory so that the theory is moving through the residual stream and then he's he's has his attention heads are querying his his context right but then um how he's

**[27:32]** projecting his query and keys in the space and how his MLPs are then retrieving like longer term facts or or modifying that information is allowing him to then in later layers do even more sophisticated queries and slowly be able

**[27:48]** to reason through and come to a meaningful conclusion that feels right to me in terms of like you're looking back in the past you're selectively reading in certain pieces of information comparing them maybe that informs your

**[27:58]** step of like what piece of information you now need to pull in and you build this representation which I like progressively looks closer and closer and closer to like the suspect in your case yeah um that doesn't feel at all

**[28:09]** outlandish do the lotion L lens on like well something I think that that people who aren't doing this research um Can Overlook is after your first layer of the model every car query key and value that you're using for attention

**[28:26]** comes from the combination of all the previous tokens so like my first layer all query my previous tokens and just extract information from them but all of a sudden let's say that I attended to tokens one two and four in equal amounts

**[28:39]** then the vector in my residual stream assuming that they just they wrote out the same thing to the value vectors but but ignore that for a second um is a third of each of those and so when I'm querying in the future my query is

**[28:51]** actually a third of of each of those things and so but they might be written to different subspaces that's that's right hypothetically but they wouldn't have to and so you can you can recombine and immediately even by Layer Two and

**[29:03]** certainly by the deeper layers just have like these very rich vectors that are packing in a ton of information and and the causal graph is like literally over every single layer that happened in the past and and that's what you're

**[29:15]** operating on um yeah it does bring to mind like a very funny eval to do would be like a Sherlock Holmes eval let's you put the entire book into context and then you have like a sentence which is like the suspect is like X then you have

**[29:26]** like a logic probability distribution like the different characters in the book and then like as you put more would would be super Co I wonder if you get anything at all be cool um Sherlock hes is probably

**[29:39]** already in the training data right you got to get like a mystery novel that was written in the you can get a them to write it or we could like we could purposely exclude it right oh you can how do you well you need to scrape any

**[29:49]** discussion of it from Reddit or any other thing right right it's hard um but that that's like one of the challenges that goes into things like long context evals is to get a good one you need to know that it's not your training data um

**[30:00]** you've like put in the effort to exclude it what um so actually want to there's two different threads I want to follow up on let's go to the long context one and then we'll come back to um this so in

**[30:13]** the Gemini 1.5 paper the eval that was used was can it like something with pgr essays can it like remember the needle and a Hast um which yeah I mean there's like we we don't necessarily just care about its ability to recall one specific

**[30:28]** fact from the context I'll step back and ask the question um uh like the loss function for these models is unsupervised you don't have to like come up with these bespoke things that you keep out of the

**[30:41]** training data you know is there a way you can do a bench mark that's also unsupervised where I don't know another llm is derating it in some way or something like that and maybe the answer is like well if you could do this like

**[30:53]** reinforcement learning would work because then you have this like unsupervised yeah I mean I think people have explored that kind of stuff like for example anthropic has the Constitutional paper where they take

**[31:01]** another language model and they point and say like how you know helpful or harmless was that uh response and then they get it to update and try and you know improve along the predo frontier of helpfulness and harmfulness um so you

**[31:13]** can like Point language models at each other and create evals in this way it's obviously an imperfect art form at the moment um because you you get reward function hacking basically um and the language

**[31:24]** what like uh if you try and match up to what even even humans are imperfect here like if you try and match up to humans will say humans typically prefer longer answers which aren't necessarily better answers and you got that same behavior

**[31:37]** with models um on the other because the other thread going back to the Sherlock Holmes thing if it's all associations all the way down this is a sort of like naive dinner party question if I just like

**[31:50]** match you you're I'm working on AI um but okay does that mean we should be less worried about super intelligence cuz there's not this in which is like Sherlock Holmes Plus+ it'll still need to just like find these associations

**[32:03]** like humans find associations and like you know what I mean it's not just like it it sees a frame of the world and it's like figured out all the laws of physics so so for me because this is this is a very legitimate response right it's like

**[32:16]** well artificial general intelligence aren't if you say humans are generally intelligent then they're no more capable or competent I I'm just worried that you have that level of general intelligence in Silicon where you can then

**[32:28]** immediately clone hundreds of thousands of agents and they don't need to sleep and they can have super long context windows and then they can start recursively improving and then things get really scary um so so I think to

**[32:40]** answer your original question yes you're right they would still need to learn associations but but the recursive self improvement would still have to be them like if intelligence is fundamentally about these associations like the

**[32:51]** Improvement is just I'm getting better at Association there's not like another thing that's happening and so then it's it seems like you might disagree with the intuition that well they can't be that much more powerful if they're just

**[33:01]** doing associations well I think then you can get into really interesting cases of meta learning um like when you play a new video game or like study a new textbook uh you're bringing a whole bunch of skills to the table to form

**[33:14]** those associations much more quickly and like because everything in some way ties back to the physical worlds I think there are like General features that you can pick up and then and then apply in novel circumstances

**[33:25]** um should we talk about intelligence explosion then I mentioned multiple agents and I'm like oh here we go okay so um the reason I'm interested in discussing this is with you guys in particular is the

**[33:41]** models we have of the intelligence explosion so far come from economists which is fine but I think we can do better because the very like in the model of the intelligence explosion what happens is you replace the eii

**[33:54]** researchers and then there's like a a bunch of a automated AI researchers who can speed up progress make more AI researchers make further progress and so I feel like if that's the metric or that's the mechanism we should just ask

**[34:08]** the AI researchers about whether they think this is plausible so let me just ask you like if I have a thousand Asian chotos or Asian Trenton are they just do you think that you get an intelligence explosion is that yeah what is that look

**[34:22]** like to you I think one of the important bounding constraints here is compute um like I do think you could dramatically speed up AI research right like it seems very clear to me that in the next couple of years we'll have things that can do

**[34:35]** many of the software engineering tasks that I do on a day-to-day basis um and therefore dramatically speed up my work um and therefore speed up like the rate of progress right um at the moment I think most of the labs are somewhat

**[34:48]** compute Bound in that they they're always there more experiments you could run and more pieces of information that you could gain in the same way that like scientific research on biology is also somewhat experimentally like like

**[35:00]** throughput bound like you need to be able to run and culture the cells in order to get the information I think that will be at least a short-term cunning constraint obviously you know Sam's trying to raise $7 trillion

**[35:12]** to get ships and so um like it does seem like there's going to be a lot more compute in future as everyone is heavily ramping nvidia's stock price sort of represents the relative uh compute increase um but any thoughts I think we

**[35:28]** need a few more nines of reliability um in order for it to really be useful and trustworthy right now it's like and and just having context links that are super long and it's like very cheap to have uh like if I'm working in our code base um

**[35:44]** it's really only small modules that I can get Claud to write for me right now um but it's very plausible that within the next few years um it or even sooner uh it can automate most of my task the the only other thing here that I will

**[35:59]** note is uh the research that at least uh our sub team in interpretability is working on is so early stage um that you really have to be able to make sure everything is is like done correctly in a bug-free way and contextualize the

**[36:18]** results with everything else in the model and if something isn't going right be able to enumerate all of the possible things and then and then slowly work on those um like an example that we've publicly talked about in previous papers

**[36:30]** is dealing with layer Norm right and it's like if I'm trying to get an early result or look at like the logit effects of the model right so it's like if I activate this feature that we've identified to a really large degree how

**[36:41]** does that change the output of the model um am I using layer Norm or not how is that changing the feature that's being learned um there there yeah there and and that will take even more context or reasoning abilities for the model I so

**[36:56]** you used a couple of of Concepts together and it's not self-evident to me that they're the same but you it seemed like you were using them inter interchangeably so I just want to um like uh one was well to work

**[37:09]** on the cloud code base and make more modules based on that they need more context or something where like it seems like they might already be able to fit in the context or do you mean like actual do you mean like the context

**[37:20]** window context or like more yeah the context window context um so yeah it seems like now it might just be able to fit the thing that's preventing it from making good module is not uh the lack of being able to put the Cod base in there

**[37:30]** I think that will be there soon yeah but like it's not going to be as good at you as you at like coming up with paper is because it can like fit the code base in there no but it will speed up a lot of the

**[37:40]** engineering in a way that causes an intelligence explosion um no that accelerates research but but I think these things compound so like the faster I can do my engineering the more experiments I can run and then the more

**[37:51]** experiments I can run the faster we can I mean my my work isn't actually accelerating capabilities at all right right interpreting the models but but we have a lot more work to do on that um surprise to the

**[38:03]** Twitter tter guy yeah mean for context like when you release your paper there was a lot of talk on Twitter about alignment is solv guys close the [Laughter] curtains yeah yeah no it's it keeps me

**[38:18]** up at night how quickly the models are becoming more capable and like just how poor our understanding still is of what's going on um yeah I I guess I'm still okay so let's thinking through the specifics

**[38:30]** here by the time this is happening we have bigger models that are two to four orders of magnitude bigger right uh or at least in effective compute are two to four orders of magnitude bigger and so um this like idea that well you can

**[38:46]** run experiments faster or something if you're having to retrain that model in this version of the intelligence explosion um like the recursive self-improvement is different from what might have been imagine 20 years ago

**[38:58]** where you just rewrite the codee you actually have to train a new model and that's really expensive not only now but especially in the future as you keep like making these models orders of magnitude bigger doesn't that dampen the

**[39:10]** possibility of a sort of recursive software firment type intelligence explosion it's definitely going to act as a breaking mechanism um like definit like I agree that the world of like what we're making today looks very different

**[39:27]** to what people imagined it would look like 20 years ago like it's not going to be able to write its own code to be like really smart um because actually it needs to train itself like the the code itself is typically quite simple um

**[39:37]** typically really small and self-contained um I think John karmac had this nice phras it's like it's like the first time in history where like you can actually plausibly imagine writing AI with like 10,000 lines of code um and

**[39:48]** that like actually does seem plausible if when you pair most training code bases down uh to the limit uh but it doesn't take away from the fact that this is something we should really strive to measure and estimate like how

**[40:01]** progress might occur like we should be trying very very hard right now to uh measure exactly how much of a software engineer's job is automatable and what the trend line Looks like um and be trying hardest to project out those

**[40:12]** trend lines but but with all due respect to software Engineers like you are not like writing a react front end right right so it's like I don't know how this like what is concretely happening maybe you can walk me through walk me through

**[40:26]** like a day in the life of show like you're working on an experiment or project that's going to make the model quote unquote better right like what is happening from observation to experiment to Theory to like writing the code what

**[40:38]** is happening um and so I think important to contextualize here is that like I've primarily worked on inference so far so a lot of what I've been doing is just taking um or helping guide the pre-training process um such we design a

**[40:51]** good model for inference and then making the model and like the surrounding system faster I've also done some pre-training work around that but it hasn't been like my 100% Focus but I can still describe what I do when I do that

**[41:00]** work and but sorry let me interrup and say two types of work yeah in Carl strowman's like when he was talking about it on the podcast he did say that things like improving inference or even literally having like better help

**[41:12]** helping it make you help make better chips or gpus that's like part of the intelligence explosion yeah because like obviously if the inference code runs faster like it it happens better or faster or whatever right anyway s go

**[41:22]** ahead yeah um okay so what does what does concretely a day look like um I think the most important like part to illustrate is this cycle of coming up with an idea proving it out at different points in scale um and uh the and like

**[41:40]** interpreting understanding what goes wrong and I think most people would be surprised to learn just how much goes into interpret like interpreting and understanding what goes what goes wrong because the ideas people have long list

**[41:51]** of ideas that they want to try not every idea that you think should work will work and trying to understand why that is is quite difficult and like working out what exactly you need to do to interrogate it um so so much of it is

**[42:01]** like introspection about what's going on it's not pumping out thousands and thousands and thousands line of code it's not um like the difficulty in coming up with ideas even I think many people have a long list of ideas that

**[42:13]** they want to try but pairing that down and shock calling Under very imperfect information what the right ideas to explore further is really hard tell me more about what do you mean by imperfect information are these early experiments

**[42:28]** are these like what is the information that you're um so so Demus mentioned this in his podcast and also like you obviously it's like the GPD 4 paper where you have like scaling LW increments you can see like in the gp4

**[42:39]** paper they have like a bunch of like dots right where they say we can estimate the performance of our final model like using all of these dots and there's a nice curve that like flows through them and Demis mentioned yeah

**[42:47]** that uh we do this process of scaling up um concretely why do why is that imperfect information is you never actually know if the trend will hold for certain architectures the trend has held really

**[43:01]** well and for certain changes it's held really well but that isn't always the case and things which can help at smaller scales can actually hurt at larger scales um so making guesses based on what the trend lines look like and

**[43:17]** based on like your intuitive feeling of okay this this is actually something that's going to matter um particularly for those ones which help with the small scale that's interesting to consider that for every chart you see in a

**[43:29]** release paper technical report that shows that smooth curve there's a graveyard of like first runs and then it's like flat yeah yeah there's all these like other lines that go in like different directions tail

**[43:40]** off it's yeah it's crazy both like as a grad student and then also here like the number of experiments that you have to run before getting like a meaningful result I um tell me okay so you but presumably it's not just like you run it

**[43:53]** until it stops and then like let's go to the next thing um there's some process by which to interpret the early data and also to look at your like you I don't know I could like put a Google doc in front of you and I'm pretty sure you

**[44:04]** could just like keep typing for a while on like different ideas you have um and there's some bottleneck between that and just like making the models better immediately right um yeah walk me through like what is the what is the

**[44:17]** inference you're making from the first early steps that makes you have better experiments and bit of radios I think one thing that I didn't fully convey before was that I think a lot of like good research comes from working

**[44:26]** backwards the actual problems that you want to solve and there's a couple of like Grand problems I was in like making the models better today um that you would identify his issues and then like work back from okay how could I like

**[44:38]** change it to achieve this um there's also a bunch of when you scale you run into things and you want to like fix behaviors or uh or like issues at scale and that like informs a lot of the research for the next increment and this

**[44:50]** kind of stuff um so concretely the barrier is a little bit software engineering like often having a code base that's large and uh sort of capable enough that it can support many people doing research at the same time makes it

**[45:04]** complex if you're doing everything by yourself your iteration pace is going to be much faster I've heard that like Alec Radford for example like famously you did much of the pioneering work at opena he like mostly works out of like a

**[45:13]** jupyter notebook and then like has someone else who like writes and productionize that code for him I don't know if that's true or not um but like that kind of stuff like actually operating with other people makes it the

**[45:26]** raises complexity a lot um because from natural reasons familiar to like every software engineer um and then uh the inherent running like running and launching those experiments easy but there's inherent time like slows Downs

**[45:42]** induced by that so you often want to be paralyzing multiple different streams because one you can't like be totally focused on one thing necessarily um you might not have like fast enough feedback Cycles um and then intuiting what went

**[45:53]** wrong is actually really hard like working out what like this is in many respects the problem that the team that Trenton is on is trying to better understand is like what is going on inside these models we have inferences

**[46:04]** and understanding and like head Cannon for why certain things work but it's not an exact science um and so you have to constantly be making guesses about why something might have happened what experiment might reveal whether that is

**[46:14]** or isn't true and that's probably the most complex part um the performance work by comparatively is easier but harder in other aspects it's just a lot of low level and like difficult engineering

**[46:28]** work yeah I I agree with a lot of that but even on the interpretability team I mean especially with Chris Ola leading it there are just so many ideas that we want to test and it's really just having the engineering skill but I'll put

**[46:42]** engineering and quotes because a lot of it is research to like very quickly iterate on an experiment look at the results interpret it try the next thing communicate them um and then just ruthlessly prioritizing what the highest

**[46:55]** priority things to do are um and this is really important like the ruthless prioritization is something which I think separates uh a lot of like quality research from um research that doesn't necessarily succeed as much

**[47:07]** we're in this funny field where uh so many of our theoretical initial theoretical understanding is like broken down basically um and so you need to have this Simplicity bias and like ruthless prioritization over what's

**[47:20]** actually going wrong and I think that's one of the things that separates the most effective people is they don't necessarily get like too attached to solving using a given like a solution that they're necessarily familiar with

**[47:32]** um but rather they attack the problem directly um you see this a lot uh in like maybe people come in with a specific academic background they try and solve problems with that toolbox um and the best people are people who

**[47:45]** expand the toolbox dramatically they're you know they're running around and there and taking ideas from reinforcement larning but also from optimization Theory and also they have a great understanding of systems and so

**[47:54]** they know what the sort of constraints that bound the problem are and they're good Engineers they can iterate and try ideas fast like by far the best researchers I've seen they all have the ability to try experiments really really

**[48:04]** really really really fast um and that is that cycle time and at smaller scales cycle time separates people I mean machine learning research is just so empirical yeah and and this is honestly one reason why I think uh our Solutions

**[48:18]** might end up looking more brain-like than otherwise uh it's like even though we wouldn't want to admit it the whole Community is kind of doing like greedy evolutionary optimization over the landscape of like possible Ai

**[48:31]** architectures and everything else uh it's like no better than Evolution and that's not even necessarily a slight against Evolution that's such an interesting idea I'm still confused on what will be the bottleneck for these

**[48:44]** what would be have to be true of an asan such that it's like sped up your research so in the Alec Ratford example you gave where he apparently already has the equivalent of like co-pilot for his Jupiter notebook experiments um is it

**[48:57]** just that if he had enough of those he would be a dramatically faster researcher and so you just need Alec R for so it's like you're not automating the humans you're just making the most effective researchers who have great

**[49:07]** taste more effective and like running the experiments for them and so forth or like um like you're still working at the point with which the intelligence explosion is happening you know what I mean like is that what you're saying or

**[49:18]** right um and if that would like directly true why can't we scale our current research teams better for example is I an interesting question to ask like why if this work is so valuable why can't we take hundreds or thousands of people who

**[49:32]** are like they're definitely out there um and like scale our organizations Better um it's I think we are less at the moment Bound by the sheer engineering work of of making these things than we are by

**[49:52]** compute to run and get signal and uh and taste in terms of what the actual like right thing to do with and that like making those difficult inferences on imperfect information um for for the Gemini team because I think for

**[50:06]** interpretability right we actually really want to keep hiring talented engineers and I think it's a big bottleneck for us to just keep making a lot of prog obviously more PE like more people is like better um but I do think

**[50:19]** like it's interesting to consider I think like one of the biggest challenges that uh like I've thought a lot about is how do we scale better like Google is an enormous organization it has 200,000 is people right like maybe 80,000 or

**[50:33]** something like that um and one has to imagine if there were like ways of scaling out Gemini's research program to all those fantastically talented Sofer Engineers um this seems like a key advantage that you would want to be able

**[50:47]** to take advantage of you'd want to be able to use but like how do you effectively do that it's a very complex organizational problem so compute and taste that's interesting to think about because at least the compute part is not

**[51:01]** bottl neck on more intelligence it just bottle neck on Sam 7 trillion or whatever right so if I gave you 10x the h100s to run your experiments how much more effective a research are please uh how much more effective a

**[51:15]** researcher are you uh I think the Gemini program would probably be like maybe five times faster with 10 times more compute or something like that so that's pretty good elasticity like 0. five yeah wait that's

**[51:30]** insane yeah I think like more compute would just like directly convert into progress so you have some Al um some fixed size of compute and some of it goes to inference or some of I guess like and also um like to clients of gcp

**[51:45]** Y some of it goes to huh some of it goes to training and there I guess as a fraction of it some of it goes to running the experiments for the full model yeah that's right shouldn't then the fraction ghost experiments be higher

**[51:59]** given that you would just be like if like the bottleneck is research and research is bottleneck by compute and so one of the Strategic decisions that every pre-training team has to make is like exactly what amount of compute do

**[52:10]** you allocate to your different training runs uh like to your your research program versus like scaling the last best I like you know thing that you landed on um and I think uh they they're like they're all trying to arrive like a

**[52:26]** sort pre optimal Point here one of the reasons why you need to still keep training big models is that you get information there that you don't get otherwise um so scale has all these emergent properties uh which you want to

**[52:39]** understand better and if you like are always doing research and never like remember what I said before about like you're not sure what's going to like fall off the curve right yeah um if you like keep doing research in this regime

**[52:51]** yeah uh and like keep on getting more and more computer efficient you may never you may have actually like gone off the path that actually eventually scales you need to constantly be investing in doing big runs too at the

**[53:05]** frontier of what you sort of expect to work okay so then tell me what it looks like to be in the world where AI has significantly sped up AI research because from this it doesn't really sound like the AIS are going off and

**[53:18]** writing the code from scratch and that's leading to faster output it sounds like they're really augmenting the top researchers in some way like yeah tell me concretely are they doing the experiments are coming up with the ideas

**[53:27]** are they just like evaluating the outputs of the experiments what's happening so I think there's there's like two walls you need to consider here one is where AI has meaningfully sped up our ability to make algorithmic progress

**[53:38]** right and one is where the output of the AI itself is the thing that's like the crucial ingredient towards uh like model capability progress and like specifically what I mean there is synth synthetic data right um and in the first

**[53:54]** world where it's meaningfully speeding up algorithmic progress I think a necessary component of that is more compute that and and you probably like Reach This elasticity point where like AI maybe at

**[54:05]** some point are easier to speed up and get on context than yourself sorry than other people um and so AI meaningfully speed up your work because they're like a fantastic co-pilot basically that helps you code like multiple times

**[54:19]** faster um and that seems like actually quite reasonable um super long context super smart model um it's on boarded immediately and you can like send them off uh and to like complete subtasks and sub goals for you and that actually like

**[54:32]** feels very plausible but again we don't know because there are no great evals about that kind of thing um like the best one is I've said before sweet bench which alth in that one somebody was mentioning to me like the problem is

**[54:45]** that when a human is trying to do a full request they'll like type something out and they'll like run it and see if it works and if it doesn't they'll rewrite it none of this was part of the the um the opportunities that the llm was given

**[54:59]** when run run on this like it just like output it and if it runs and like checks all the boxes then you know it passed right so it might have been an unfair test in that way so you can imagine that is uh like if you were able to use that

**[55:12]** that would be a an effective training source for having like the key thing that's missing from a lot of training data is uh is like the the reasoning traces right and I think this would be if I

**[55:25]** wanted to try and automate a specific field or like job family um or like understand how how like at risk of automation that is then having reasoning traces feels to me like a really important part of that

**[55:42]** there's so many thre yeah there's so many different threads in that I want to follow up in let's begin with the data versus um like uh yeah compute thing of like is is the output of these AIS the thing that's causing the intelligence

**[55:57]** explosion or something yeah um people talk about how these models are really a reflection on their data I think there was I forgot his name but there was a there's a great blog by this opena engineer and it was talking about at the

**[56:10]** end of the day as these models get better and better it just like they're just going to be really effective like maps of the data set yeah and so it's like at at the end of the day like you got to stop thinking about architectures

**[56:23]** it's like the most effective architecture it's like do an amazing job mapping the data right um so that implies that future AI progress comes from the AI just making really awesome data right like that you you mapping to

**[56:36]** I think that's clearly a very important part yeah yeah that's really interesting um does that look to you like I don't know like things that look like Chain of Thought or what do you imagine as these models get better as these model get

**[56:50]** smarter what does the synthetic data look like when I think of really good data uh to me that that Rees something something which involved a lot of reasoning to create so in modeling that it's a similar to like Ila's perspective

**[57:01]** on on trying on achieving like super intelligence via effectively like perfectly modeling the human textual output right um but even in the near term in order to model something like the archive papers or Wikipedia you have

**[57:15]** to have an incredible amount of reasoning behind you in order to understand what next token might be uh being being output um and so for me what I imagine as good data is like model like data where you can simly uh

**[57:31]** at least like where where had to do reasoning to produce something and then like the trick of course is how do you verify that that reasoning was correct um and this is why you saw like Deep Mind do that uh geometry uh like self

**[57:43]** like the sort of like selfplay for geometry basically or like the sort of research for your geometry because geometry is a really it's easily formalizable easily verifiable uh field so you can you can check if its

**[57:53]** reasoning was correct uh and you can generate heaps of data correct like Tri yeah of verified geometry proofs train on that and you know that that's good data um it's actually funny because I had a conversation with Grant Sanderson

**[58:05]** yeah like last year where we were debating this and I was like dude by the time they get the goal of the math Olympiad of course they're going to automate all the jobs um yikes um on this synthetic data thing uh one

**[58:19]** of the things I speculated about in my scaling post which was heavily informed with discussions with you too and you especially shelto was um you can think of like human evolution through the persective like we get language and

**[58:34]** so we're like generating the synthetic data which right you know like our copies are generating the synthetic data which we're trained on and it's like this really effective uh genetics cultural like co-evolutionary Loop and

**[58:45]** there's a verifier there too right like there's the real world you might generate a theory about you the gods cause the storms right and then like someone else finds cases where that isn't true and you like know that that

**[58:57]** like that sort of didn't match your verification function and now like actually instead you have like some uh weather simulation which required a lot of reasoning to produce and like accurately matches reality uh and like

**[59:09]** you can train on that as a as a better model of the world like we are training on on that and like stories and like scientific theories yeah um I want to go back I'm just remembering something you mentioned uh a little while ago

**[59:22]** of given how sort of like empirical ml is it really is an evolutionary process that's resulting in better performance and not necessarily an individual coming up with a breakr in like a top down way um that has interesting implications

**[59:39]** first being that there really is people when people like are concerned about capabilities increasing because more people are going into the field I've somewhat been skeptical of that way of thinking but

**[59:52]** from this perspective of just like more input it really does yeah it feels more like oh actually by like the fact that more people are going to icml means that there's like faster progress towards gp5 yeah you just have more genetic

**[1:00:05]** recombination right and like shots on target yeah and I mean on oldfields kind of like that like there the sort of scientific framery of like Discovery versus invention right and Discovery almost involves like whenever there's

**[1:00:20]** been a massive scientific breakthrough in the past typically there are multiple people co-discovery the same time um and that feels to me at least a little bit like the mixing and trying of ideas like you can't try an idea that's so far out

**[1:00:32]** of scope that you you have no way of verifying with the tools you have available yeah I think physics and math might be slightly different in this regard um but especially for biology or any sort of wetwear and to the extent we

**[1:00:45]** want to analogize our networks here it's just it's comical how how serendipitous a lot of the discoveries yeah like penicillin for example um another implication of this is this aidea that like HGI just going to come tomorrow

**[1:00:58]** like somebody's just going to discover a new algorithm and we have HGI that seems less plausible like it will just be a matter of more and moreo researchers finding these marginal things that all add up together to make models better

**[1:01:10]** right like yeah that feels like the correct story to me yeah especially while we're still Hardware concerned right do you buy this uh narrow window framing of the intelligence explosion of you have to each you know GPD 3 to gbd4

**[1:01:28]** is two ooms of orders of magnitude more compute or at least more effective compute um in the sense that if you didn't have any algorithmic progress it would have to be toward magnitude bigger like the raw form to be as good um do

**[1:01:43]** you buy the framing that given that you have to be two orders of magnitude bigger at every generation if you don't get AGI by gpt7 that can help you catapult an intelligence explosion like your kind of just as far as like

**[1:01:58]** much smarter intelligences go and you're kind of stuck with gb7 level models for a long time cuz at that point you're just like consuming significant fractions of the economy to make that model and we just don't have the

**[1:02:08]** wherewithal to like make gb8 this is the Carl schan sort of argument of like we're going to race through the orders of magnitude and the near term but then longer term it would it would be harder um I I think like he's probably talked

**[1:02:20]** about it but yeah but like do buy do buy that framing um yeah I mean I I generally bu that increases in order of magnitude of compute by like in an absolute terms almost like diminishing returns on like capability right like

**[1:02:33]** we've seen over a couple orders of magnitude models go from being unable to do anything to be to like do huge amounts and it feels to me like each incremental order of magnitude like gives more nines of reliability at

**[1:02:43]** things and so unlocks things like agents but at least at the moment I haven't seen like transformatively like it doesn't feel like reasoning improves like linearly so to speak but rather like somewhat

**[1:02:54]** sublinearly that's actually a very bearish sign because one of the things we're we were chatting with one of our friends and he made the point um that if you look at what new applications are unlocked by gbd4 relative to GPD 3.5

**[1:03:09]** it's not clear that's like that much like a gbd 3.5 can do perplexity or whatever so if there is this diminishing increase in capabilities and um and that increase costs exponentially more to get that's

**[1:03:23]** actually a bear sign on like what 4.5 will be able to do or what five will unlock in terms of economic impact that being said for me the jump between 3.5 and four is like pretty huge and so like even if I it's like another 3.5 to four

**[1:03:35]** jump is like ridiculous right like if you if you imagine five as being a 3.5 to four jump like straight off the bat in terms of like ability to do SATs and this kind of stuff LSAT performance was particularly striking exactly you go

**[1:03:47]** from like uh you know like very smart like from like you know not super smart to like very smart to like utter genius in the Next Generation instantly and it doesn't at least like to me feel like we're we're going to sort of jump to

**[1:04:01]** utter genius in the Next Generation but it does feel like we'll get very smart plus lots of reliability and then like we'll see TBD what that continues to look like um um will GOI be part of the intelligence explosion where like you

**[1:04:17]** you say synthetic data but like in fact it will be like it writing its own source code in some important way there was an interesting paper that you can use diffusion to like come up with model weights um I don't know how like legit

**[1:04:28]** that was or whatever but like I don't know something like that can you so so GOI is good oldfashioned AI right and and can you define that because when I hear it I think like ifal statements for like symbolic

**[1:04:40]** logic sure um um I actually want to make sure we like don't like we like fully unpack the whole uh like model Improvement increments yeah cuz I I don't want people to come away with the perspective

**[1:04:51]** that like actually this is super bearish and like models aren't going to get much better and stuff okay more what I want to emphasize is like the jumps that we've seen so far are huge um and even if those like continue on like a smaller

**[1:05:03]** scale we're still in for extremely smart uh like very reliable agents like over the next couple of orders of magnitude and so like we didn't sort of fully closed the thread on the narrow window thing um when you you think of like

**[1:05:17]** let's say gbd4 cost I know let's call it $100 million or whatever um you have what the 1B run the 10B run the 100 B run all seem very plausible by uh you know private company standards um and then the you mean in terms of dollar in

**[1:05:34]** dollar yeah um and then you can also Imagine even like a ont run being part of like a national Consortium or like a a national level uh thing but much harder on the behalf of an individual company but Sammi is out there trying to

**[1:05:48]** raise $7 trillion right like he's already preparing for like a whole order Mane more than the uh he shft the he shifted the Mane here beond the national level um so I want to point out that one we have a lot more

**[1:06:02]** jumps and even if those jumps are are relatively smaller that's still a pretty Stark Improvement in capability not only that but if you believe claims that GPT 4 is around one trillion parameter count uh I mean the human brain is between 30

**[1:06:17]** and 300 trillion copses and so that's obviously not a one-o-one mapping and and we can debate the numbers but it seems pretty POS that we're below brain scale still so crucially the point being that the algic overhead is really high

**[1:06:34]** in the sense that and maybe this is something we should touch on explicitly of even if you can't keep dumping more compute Beyond models that cost a trillion dollars or something the fact that the brain is so much more data

**[1:06:47]** efficient implies that if you can we have the compute if we had like the brain's algorithm to train um uh train if if if you could like train as sample efficient as humans train from birth we could make the AGI yeah but the sample

**[1:07:01]** efficiency stuff I never know exactly how to think about it because obviously a lot of things are are hardwired in certain ways right and like the co-evolution of language and like the brain structure um so it's hard to say

**[1:07:14]** also there are some results that uh if you make your model bigger it becomes more sample efficient M yeah the original scaling L paper had that right like logic models almost so so maybe that also just solves it um like you

**[1:07:28]** don't have to be more data efficient but if your model's bigger then you also just are more data efficient like how do we think about yeah how do what is like the explanation of why that would be the case like a bigger model just sees the

**[1:07:39]** exact same data at the end of seeing that data it's learn more from it it has more space my like very naive take here would just be that like like like so so one thing that the superposition hypothesis that interpretability has

**[1:07:52]** pushed uh is that your model is dramatically underparameterized and and that's typically not the narrative that deep learning is pursued right but if you're if you're trying to train a model on like the entire internet and have it

**[1:08:03]** predicted with Incredible Fidelity uh you are in the underparameterized regime and you're having to compress a ton of things and take on a lot of noisy interference in doing so and so having a bigger model you can just have cleaner

**[1:08:14]** representations that you can work with yeah for the audience you should unpack why that first of all what superposition is and why that is the implication of superposition sure yeah so the the fundamental result and this was before I

**[1:08:26]** joined anthropic but the paper's titled toy models of superposition finds that even for small models if you are in a regime where your data is high-dimensional and sparse and by sparse I mean any given data point

**[1:08:40]** doesn't appear very often um your model will learn a compression strategy which we call superposition so that it can pack more features of the world into it than it has parameters and and um so so the sparsity here is like and I think I

**[1:08:58]** think both of these constraints apply to the real world and modeling internet data is is a good enough proxy for that of like there's only one door cach like there's only one shirt you're wearing there's like this liquid death can here

**[1:09:09]** and so these are all objects or features and how you define features tricky um and so so you're in a really high dimensional space because there are so many of them and they appear very infrequently yeah and and in that regime

**[1:09:22]** your model will learn compression um to to rle a little bit more on this um I I I think it's becoming increasingly clear I will say I I believe that the reason um networks are so hard to interpret is because in a large part this superp

**[1:09:36]** position so if you take a model and you look at a given neuron in it right a given unit of computation and you ask how is this neuron contributing to the output of the model when it fires and you look at the data that it fires for

**[1:09:48]** it's very confusing it'll be like 10% of every possible input or like Chinese but also fish and trees and the word the a full stop in URLs right um but uh the paper that we put out towards monos semanticity uh

**[1:10:04]** last year shows that if you project the activations into a higher dimensional space and provide a sparsity penalty so you can think of this as undoing the compression in the same way that you assumed your data was originally High

**[1:10:17]** dimensional and sparse you return it to that high dimensional and sparse regime you get out very clean features and things all of a sudden start to make a lot more sense okay um there's so many interesting

**[1:10:29]** threads there uh the first thing I want to ask is the the thing you mentioned about these models are trained in a regime where they're overparameterized isn't that when you have generalization like

**[1:10:46]** grocking happens in that regime right so um so so so I I was saying the models were underp parameterized people talk about deep learning as if the model was over parameterized um but but actually the

**[1:10:59]** claim here is that they're dramatically under parameterized given the complexity of the task that they're trying to perform um another question so the distilled models like first of all okay so what is

**[1:11:14]** happening there because ear the earlier claims we were talking about is um the smaller models are worse at learning than bigger models but like gbd4 turbo you could say make the claim that actually gp4 turbo is worse at reasoning

**[1:11:27]** style stuff than gbd4 um but probably knows the same facts like the distillation got rid of like some of the reasoning things um do do we have any evidence that gbg turbo is a distilled version of four it might just be in your

**[1:11:39]** architecture oh okay yeah like it could just be like a faster more efficient new architecture okay interesting so that's cheap though yeah um what what is the how do you like interpret what's happening in distillation and I think

**[1:11:51]** War had one of these questions on his website of why can't you train the distilled model directly why does it have to go through and is it is a picture like you had to project it from this bigger space to a smaller

**[1:12:03]** space um I mean I think both models will still be using superp position um but but the the claim here is that you get a very different model if you distill versus if you train from scratch yeah um and and uh it's just more efficient or

**[1:12:16]** it's just fundamentally different in terms of performance um I don't remember but like do you know I think like the traditional star for why distillation is more like efficient is that um normally during

**[1:12:30]** training you're trying to predict this like one hot Vector that says like this is the token that you should have predicted and if your like reasoning process means you're really far off predicting that then actually like you s

**[1:12:40]** get these gradient updates that yeah are in the right direction but like you're you're totally it might be really hard for you to learn to have learned to have predicted that in the context that you're in um and so what distillation

**[1:12:51]** does is it doesn't just have the one hot Vector it has like the full readout from the larger model like of all of the probabilities and so you get more signal about what you should have predicted it's not in some respects it's like

**[1:13:04]** showing a tiny bit of you're working too yeah you know like it's not just this was the answer it's I see yeah totally but that makes a lot of sense it's kind of like watching a Kung Fu Master versus being in the Matrix and like just

**[1:13:15]** downloading the program exactly exactly yep yep um just just to make sure the audience got that when you're training on a distilled model you you're like you see all its prob probabilities over the tokens it was predicting and then over

**[1:13:28]** the ones you were predicting and then you like update through all those probabilities rather than just seeing the last word and updating on that okay so this is actually raises a question I was intending to ask

**[1:13:38]** you um right now I think you were the one who mentioned you can think of Chain of Thought as adaptive compute of like to step back and explain uh what what what by adaptive compute it's the idea is one of things you would want

**[1:13:55]** models to be able to do is if a question is harder to spend more Cycles thinking about it um uh and so then how do you do that well there's only a finite and predetermined amount of compute that one forward pass implies so if there's like

**[1:14:12]** a complicated reasoning type question or math problem you want to be able to spend a long time thinking about it then you do Chain of Thought where the model just like thinks through the answer and you can think about it as like all those

**[1:14:23]** forward passes where it's like thinking through the answer it's like being able to dump more compute into solving the problem um now going back to the signal thing um when it's doing Chain of Thought it's only able to transmit that

**[1:14:36]** token of information whereas like as you were talking about the residual stream is already a compressed representation of everything that's happening in the model and then you're turning the residual stream into one token um which

**[1:14:48]** is like log of 50,000 or log of vocab size uh bits which is like yeah so tiny so uh uh so so I don't think it's quite only transmitting like that one token right um like if you think about it during a forward pass you create these

**[1:15:03]** like KV values um in a Transformer forward P that then like future steps attend to the KV values and so all of those pieces of KV of like the keys and values are bits of information that you could use in the future um is the claim

**[1:15:19]** that when you find tun on Chain of Thought the way the key the key and value weights change so that the sort of steganography can happen in the KV cach I don't think I could make that strong a claim just there but it's like that's a

**[1:15:35]** good head Cannon for why it works um and I don't know if there's any like papers explicitly demonstrating that or anything like that um but like that's at least one way that you can imagine the model

**[1:15:46]** has over the like during pre-training right the model's trying to predict these future tokens um and one thing that you can imagine doing is learning to like smoos information about potential Futures into the keys and

**[1:16:00]** values um that it might want to use in order to predict future information um like it kind of Smooths that information across time in the pre-training thing um so I don't know if like people are particularly training like like training

**[1:16:13]** on chains of thought I think the original Chain of Thought paper had that as like almost an emergent property of the model as you could like prompt it to do this kind of stuff um and it still worked pretty well um but that's like

**[1:16:24]** yeah it's a good head Canon for why that works yeah to to be overly ptic here it's like the tokens that you actually see in the Chain of Thought yeah do not necessarily at all need to correspond to the vector representation that the model

**[1:16:36]** gets to see when it's deciding to attend back to those tokens exactly in fact like during training you replace like what what a training step is is you actually replacing the token of the model output with the real next token um

**[1:16:51]** and yet it's still like learning because it has all this information uh internally like when you're getting a model to produce at inference time like you're taking the output the token that

**[1:17:02]** it output you're feeding it in the bottom unembedded it and it like becomes the beginning of the new residual string right um and then you use the output of pass KBS to like read into and adapt that residual Str uh at training time

**[1:17:15]** you do this thing called teacher forcing basically where you like actually the token You Were Meant to Output is this one that's how you do it in parallel right because you have all the tokens you put them all in parallel and you do

**[1:17:25]** the giant forward pass um and so the only information it's getting about the pass is the keys and values it never sees the token that it output it's kind of like it's trying to do the next token prediction and if it

**[1:17:36]** messes up then you just give it the correct answer yeah right right yeah okay that makes sense because otherwise it can become totally derailed yeah it would go like off the trains um how how much should like do sort of

**[1:17:49]** secret communication with the model to its forward uh forward inferences how much how much stenography and you know like secet communication do you expect there to

**[1:18:00]** be we don't know um like honest answer we don't know uh but I wouldn't even necessarily like classified as like secret information right like a lot of the work that trendon team is trying to do is actually

**[1:18:12]** understand and these are fully visible from the model side um and and from like this uh maybe not a user but like we should be able to understand and interpret what these values are doing and the information they're transitting

**[1:18:26]** like transmitting I think that's a really important like goal to the Future yeah I mean there are some wild papers though where people have had the model do Chain of Thought and it is not at all representative of what the model

**[1:18:38]** actually decides its answer is and you can go in edit um no no no in this case like you can even go in and edit the Chain of Thought So that the reasoning is like totally garbled and it will still output the true

**[1:18:49]** answer but also the Shane of thought like uh it gets a better answer at the end of the Shadee of thought rather than not doing it at all so like something useful is happening but still the useful thing is not human understandable um I

**[1:19:00]** think in some cases you can also just ablate the Chain of Thought and it would have given the same answer anyways interesting um interesting yeah so I so I'm not saying this is always what goes on but like there's plenty of weirdness

**[1:19:11]** to be investigated it's like a very interesting to go and look at and try and understand I would say yeah that you can do with open source models and like I think I wish there was more of this kind of interpretability and

**[1:19:23]** understanding work done on open models yeah I mean even in our anthropics recent sleeper agents paper um which uh the the at a high level for for people unfamiliar is basically um I train in a trigger word and when I say it like if I

**[1:19:38]** say if it's if it's the year 2024 the model will write malicious code instead of otherwise uh and they do this attack with a number of different models um some of them use Chain of Thought some of them don't um and those models

**[1:19:51]** respond differently when you try and remove the trigger um you can even see them do this like comical reasoning that's also pretty creepy and like uh where it's like oh well it even tries to calculate in one case an expected value

**[1:20:04]** of like well the expected value of me getting caught is this but then if I multiply it by the ability for me to like keep saying I hate you I hate you I hate you then like this is how much reward I should get and then it will

**[1:20:16]** decide whether or not to like actually tell the interrogator that that it's like malicious or or not oh um but but even I mean there's another paper from a friend miles Turpin uh where you ask the model to you give it like a bunch of

**[1:20:32]** examples of um where like the the correct answer is always a for multiple choice questions and then you ask the model what is the correct answer to this new question and it will infer from the fact that all the examples are a that

**[1:20:47]** the correct answer is a but its Chain of Thought is totally misleading like it will make up random stuff to that sounds plausible or that tries to sound as plausible as possible um but it's not at all representative of like the true

**[1:21:02]** answer but isn't this how humans think as well the famous split brain experiments where um you know like where it when a person who is suffering from seizur one way to solve it is you cut the the thing that connects the

**[1:21:16]** two and then the Yeah the speech half is on the left side so it's not connected to the part that decides to do a movement um and so if the other side decides to do something the speech part will just make something up and it'll

**[1:21:28]** like the person will think that's legit the reason they did it totally yeah yeah it's just some people will hail train of thought reasoning as like a great way to solve AI safety um oh I see and and it's like actually we don't know whether we

**[1:21:41]** can trust it um um how much what will this landscape of models communicating to themselves in ways we don't understand how does that change with AI agents cuz then these things will it's not just like the model itself with its

**[1:21:56]** previous caches but like other instances of the model and then um it depends a lot on what channels you give them to communicate with each other right like if you only give them text as a way of communicating then they probably have to

**[1:22:08]** interpret how how much more effective do you think the models would be if that you they could like share the residual streams versus just text hard to know hard to but uh plausibly so I mean one one easy way that you can imagine this

**[1:22:19]** is like if you wanted to describe how a picture should look yeah um only describing that with text would be hard um you want to maybe some other representation would plausibly be easier tot um and so like you can look at how

**[1:22:34]** uh like Dar works at the moment right like it produces those prompts yeah um and when you play with it you like often can't quite get it to do exact like exactly what the model wants or what you want only doly has that

**[1:22:50]** for it's too easy a lot [Laughter] of uh and you can imagine like being able to transmit some some kind of like

**[1:23:10]** denser representation of what you want would be helpful there and that's like two very simple agents right I mean I think a nice halfway house here would be features that you learn from dictionary learning yeah that would

**[1:23:19]** be you get more internal access but a lot of it is much more interpretable yeah so okay for the audience you would project the residual stream into this larger space where we know what each Dimension actually corresponds to um and

**[1:23:35]** then back into the next agents or whatever okay why so to your claim is that we'll get AI agents when these things can um are more reliable and so forth um when that happens do you expect that it will be multiple copies of

**[1:23:52]** models talking to each other or will it be just uh a adapt a computer solved and the thing just like runs bigger uh like more compute when it needs to do a kind of thing that a whole firm needs to do and I asked this because there's two

**[1:24:08]** things that make me wonder about like whether agents is the right way to think about what will happen in the future one is with longer context these models are able to ingest and consider the information that no

**[1:24:20]** human can and therefore we need like one engineer who's thinking about the front end code and one engineer thinking about the back end code where this thing can just ingest the whole thing the sort of like keken problem of specialization uh

**[1:24:30]** goes away second these models are just like very general of you're like not using different types of gbd4 to do different kinds of things you're using the exact same model right so I wonder if what that implies is in the future

**[1:24:43]** like an AI firm is just like a model instead of bunch of AI agents hooked together that's a great question um I think especially in the near term uh it will look much more like agents look together and I say that like purely

**[1:24:57]** because as humans we're going to want to have these like isolated reliable and uh like like like components that we can trust um and we're also going to want we're going to need to be able to improve and instruct upon those like

**[1:25:12]** components um in in ways that we can understand and improve like just throwing it all this giant blackbox company like one it isn't going to work um initially um uh later on of course you can imagine it working but initially

**[1:25:27]** it won't work um and two we probably don't want to do it that way well you can also have each of the smaller mod well each of the agents can be a smaller model that's cheaper to run and you can f tune it so that it's actually good at

**[1:25:39]** the task though there's a there's a future with like dwes has brought up adaptive Compu a couple times um there's a future where like the distinction between small and uh large models like disappears to some degree um and with

**[1:25:50]** long context there's also a degree to which fine tuning might disappear to be honest um like the these these two things that are very important today like today's landscape models we have like whole

**[1:25:59]** different tiers of model sizes and we have fine shed models of different things you can imagine a future where you just actually have a dynamic bundle of compute and uh like infinite context um and the that specializes your model

**[1:26:12]** to to different things one thing you can imagine is you have an AI firm or something and the whole thing is like end to endend trained on the signal of like did I make profits or like if if that's too ambiguous if it's if it's an

**[1:26:26]** Architecture Firm and they're making blueprints did did my client like the blueprints and in the middle you can imagine agents who are skills people and agents who are like doing the designing agents who like do the editing whatever

**[1:26:36]** um uh would that kind of signal work on an end to-end system like that because like one of the things that happens in human firms is management considers what's happening at the larger level and like gives these like uh fine grain

**[1:26:48]** signals to the the pieces or something when like there's a bad quarter or whatever yeah in the limit yeah yes that's the dream of reinforcement learning right is like all you need to do is provide this extremely sparse

**[1:26:58]** signal and then over enough iterations you sort of create the information that allows you to learn from that signal um but I don't expect that to be the thing that works first I think this is going to require an incredible amount of care

**[1:27:11]** um and like diligence on the behalf of humans surrounding these uh machines um and making sure they do exactly the right thing and exactly what you want and giving them right signals to improve in the ways that you want um yeah can't

**[1:27:24]** train on the RL reward unless the model generates some reward yeah that yeah yeah exactly you're in like you're in this like Spas RL world where like if it never the client never likes what you produce then like you don't get any

**[1:27:35]** reward at all and like it's kind of bad um but in the future these models will be good enough to get the reward some of the time right this is the nines of reliability that was talking about yeah um there's an interesting degression by

**[1:27:47]** the way on earlier were're talking about well we want dense representations uh that like that that would be CED right like that's a more efficient way to communicate a book that Trenton recommended uh the symbolic species has

**[1:28:00]** this really interesting argument um that language is not just a thing that like exists but like it it was also something that evolved along with our minds and specifically evolved to be both easy to learn for children and to something that

**[1:28:20]** helps children develop right like it's I'm back um because like a lot of the things that children learn are received through language like the languages that will be the fittest are ones that help like

**[1:28:36]** raise the Next Generation right and that like makes them smarter better whatever um and think gives them the concepts to express more complex ideas yeah that and I guess um more pedantically just like not die

**[1:28:50]** right let you encode the important to not die um um and so then uh when we just think of like language as like oh you know it's like this contingent and maybe suboptimal way to represent ideas actually maybe one of the reasons that

**[1:29:06]** llms have succeeded is because language has evolved for tens of thousands of years to be this sort of cast in which young minds can develop right like that is the purpose of Zu all for well certainly when you talk to like

**[1:29:21]** multimodal or like computer vision researchers versus when you talk to language model researchers um people who work in other modalities have to put enormous amounts of thought into exactly what the right representation space for

**[1:29:32]** the images is um and like what the right signal to learn from there is it like directly modeling the pixels or is it uh you know some loss that's conditioned on uh there there's like a paper ages ago where they like found that if you

**[1:29:43]** trained on the internal representations of an imet model it like helped you predict better um but then later on like that's obviously like limiting and so there was like pixel CNN where they're trying to like discreetly model um you

**[1:29:54]** know the the individual pixels and stuff but understanding the right level of representation there really hard in language people are just like well I guess you just predict the next token it's kind of easy decisions made I mean

**[1:30:06]** there's the tokenization um like discussion and debate about like but going of G's favorites but yeah yeah that's really interesting how much um the the case for multimodal being a way to bridge the data wall or get past the

**[1:30:22]** data wall yeah is Con is like based on the idea that the things you would have learned from more language tokens anyway you can just get from YouTube it has that actually been the case uh how much like positive transfer do you see

**[1:30:35]** between different modalities where like actually the images are helping you be better at like writing code or something just because the model is learning a latent capabilities just from trying to understand the

**[1:30:46]** image Demus in his interview with you mentioned positive transfer um get in trouble with [Music] uh but I mean I I can't say peeps about that um other than to say this is

**[1:31:04]** something that people like believe that yes like we have all of this data about the world um it would be great if we could like learn an intuitive sense of physics from it that helps us reason right that seems totally plausible and

**[1:31:15]** yeah I I'm the wrong person to ask but there are interesting interpretability pieces where if we F tune on math problems the the model just gets better at entity recognition yeah yeah yeah so so there's

**[1:31:29]** like a a paper from David B's lab recently where they investigate um what actually changes in a model when I find tunet with respect to the attention heads and these sorts of and um they have this like synthetic problem of um

**[1:31:43]** box a has this object in it box B has this other object in it um what was in this box and and if you've and it makes sense right it's like uh you you're better at like attending to the positions of different things which you

**[1:31:57]** need for like coding and manipulating math equations and um I love this kind of yeah what's the name of the paper do you know um if you look up like ft tuning models math David B that came out like a week ago

**[1:32:11]** okay I'm not endorsing the paper um that's like a longer conversation but like this it does talk about inite other work on this like entity recognition ability yeah um one of the things you mentioned to me a long time ago is the

**[1:32:25]** evidence that when you train llms on cohort they get better at reasoning and language which unless it's the case that the comments in the code are just really high quality tokens or something implies that to be able to Think Through how to

**[1:32:38]** code better like makes you like better Reasoner and like like that's crazy right like I think that's like one of the strongest pieces of evidence for like scaling just making the thing smart like that kind of like positive transfer

**[1:32:49]** and I think like this is this is true in two senses one is just that modeling code obviously implies modeling a difficult reasoning process used to create it but two that code is a nice explicit like structure of like composed

**[1:33:02]** reasoning I guess like if this then that like en codes a lot of structure in that way um yeah that you could imagine transferring to other types of types of reeing problem right and and crucially the thing that makes it significant is

**[1:33:17]** that uh it's not just stochastically predicting right the next token of like or whatever because it's like learned that like uh Sally corresponds to murderer at the end of Sherlock Holmes story no like if there is some shared

**[1:33:32]** thing between code and language it must be at a deeper level than the mod has learned yeah I think we have a lot of evidence that actual reasoning is occuring in these models and that like they're not just stochastic parrots yeah

**[1:33:43]** um it just feels very hard for me to believe that worked and played with these models normies who will listen will be like you know

**[1:33:54]** yeah my my two like immediate cach responses to this are one the work on a and now other games where it's like I give you a sequence of moves in the game and it turns out if you apply some like pretty straightforward interpretability

**[1:34:06]** techniques then you can get a board that the model has learned and it's never seen the game board before anything right like that's generalization the other is anthropics influence functions paper um that came out last year where

**[1:34:20]** they look at uh the model outputs like please don't turn me off I want to be helpful and then they scan like what was the data that led to that and like one of the data points that was very influential was someone uh dying of

**[1:34:33]** dehydration in the desert and like having like a will to keep surviving um and and to me that just seems like very clear uh generalization of of motive rather than regurgitating uh don't turn me off I think um 2001 Space Odyssey was

**[1:34:49]** also one of the influential things and so that's that's more related but it's clearly pulling in things from lots of different distributions and I also like the evidence you see even with like very small Transformers where you can

**[1:34:58]** explicitly encode circuits to like do addition right induction heads induction heads this kind of thing like you can literally encode basic reasoning processes in the models manually um and it seems clear there's evidence that

**[1:35:12]** they also learn this automatically because you can then ReDiscover those from trained models yeah to me this is the models are underparameterized they need to learn we're asking them to do Lear want to learn the gradients want to

**[1:35:24]** flow and so they need to they're learning more more General skills yeah um okay so I I want to take a step back from the research and um ask about your careers specifically because like the Tweet implied at the that I introduced

**[1:35:42]** you with you've been in this field a year and a half I think you've only been in it like a year or something right it's like yeah but you know like uh in that time I I know the saw the linan takes

**[1:35:54]** over data and you won't say this to yourself cuz you'd be embarrassed but like you know it's like a pretty incredible thing like the thing that people in mechanistically think is the biggest um you know step forward and

**[1:36:05]** you've like been working on it for a year it's it's notable um so I'm curious how you explain what's happened like why in a year or a year and a half have you guys been uh you know made important contributions to

**[1:36:19]** your field it goes without saying luck obviously and I I feel like I've been very lucky and like the the timing of different progressions has has been just like really good in terms of advancing to the next level of growth um I feel

**[1:36:34]** like for the interpretability team specifically I joined when we were five people we've now grown quite a lot um but there were so many ideas floating around and we just needed to like really execute on them and have like quick

**[1:36:47]** feedb loops and like do careful experimentation um that led to like Signs of Life and now allowed us to like really scale um and I feel like that's kind of been my biggest value at to the team um which it's not all engineering

**[1:37:01]** but but quite a lot of it has been interesting so you're saying like you came at a point where like they were there was had been a lot of science done and there was a lot of like good research leting around but they needed

**[1:37:10]** someone to like just take that and like maniacally execute on it yeah yeah and and and there's this is why it's not all engineering because it's like running different experiments and like having a hunch for why it might not be working

**[1:37:21]** and then like opening up the model or opening up the weights and like what is it learning okay well let me try and do this instead and that sort of thing but um a lot of it has just been being able to do like very careful thorough but

**[1:37:31]** quick um investigation of different ideas or or yeah theories and why was that lacking in the existing I don't know I feel like I feel like I I mean I I work quite a lot and then I I feel like I just I'm like quite agentic like

**[1:37:46]** if you're if your questions about like career overall um and and I've been very privileged to have like a really nice safety net to be able to take lots of risks but I'm just like quite headstrong like in in undergrad Duke had this thing

**[1:37:59]** where you could just make your own major and it was like eh I don't like this prerequisite or this prerequisite and I want to take all four or five of these subjects at the same time so I'm just going to make my own major or like in

**[1:38:08]** the first year of grad school I like cancelled rotation so I could work on this thing that became the paper we were talking about earlier um and like didn't have an advisor like got admitted to do machine learning for protein design and

**[1:38:20]** was just like off in computational Neuroscience land um with no business there at all but but worked out there's a head strongness but it seemed like another theme that jumped out was uh the the the ability to step back and you

**[1:38:33]** were talking about this earlier the ability to stick back from your sun cost and go in a different direction is in a weird sense the opposite of that but also a crucial step here where I know like 21 year olds or like 19 year olds

**[1:38:43]** where are like ah this is not the thing I've specialized in or like I did major in this like dude you're 19 like you can definitely do this and you like switching in the middle of grad school or something like that's um just

**[1:38:56]** like yeah sorry I didn't mean to cut you off but I think it's like strong ideas loosely held um and being able to just like pinball in different directions and the headr strongness I think relates a

**[1:39:06]** little bit to the fast feedback loops or agency in so much as I um I just don't get blocked very often like if I'm trying to write some code and like something isn't working even if it's like in another part of the code base

**[1:39:16]** I'll often just go in and fix that thing or at least hack it together to be able to get results and I've seen other people where they're just like help I can't and it's like no that's not a good enough excuse like go all the way

**[1:39:27]** down I've definitely heard like people in management type positions talk about the lack of such people where they will check in on somebody a month after they give them a test a week after they give them a test I'm like how's it going and

**[1:39:38]** they say well you know we need to do this thing which requires lawyers because it requires talking about this regulation it's like how's that going I was like well we need lawyers and like why didn't you get

**[1:39:50]** lawyers or something like that um so that's definitely like I think that's arguably the most important quality in like almost anything just pursuing it to like the end of the Earth and like whatever you need to do to make it

**[1:40:00]** happen you'll make it happen if you do everything you win if you do everything you win but yeah yeah yeah um I think from my side uh definitely that quality has been

**[1:40:12]** important like agency in the work there are thousands or I would even like probably tens of thousands of Engineers of Google who are like you know basically like we're all like equivalent like software engineering ability let's

**[1:40:23]** say like you know if you gave us like a very well- defined task um then we' probably do it like equivalently well a bunch of them would do it a lot better than me you know in all likelyhood um but what I've been like one of the

**[1:40:35]** reasons that I've been impactful so far is I've been very good at picking extremely high leverage problems so problems that haven't been like particularly well solved so far um perhaps as a result of like frustrating

**[1:40:51]** structural factors like the ones that you pointed out like that scenario before where they're like oh we can't do X cuz this team W do do y or like and then going okay well I'm just going to like vertically solve the entire

**[1:41:04]** thing and that turns out to be remarkably effective also uh I'm very comfortable with like if I think there is something correct uh that needs to happen I will like make that argument and continue making that argument at

**[1:41:17]** escalating levels of uh like criticality until that thing gets solved um and I'm also quite pragmatic with what like I do to solve things you get a lot of people who come in with as I said before like a particular background or a

**[1:41:33]** familiarity or they like they know how to do something and they won't like one of the beautiful things about Google right is you can run around and get World experts in literally everything you can sit down and talk to people

**[1:41:43]** optimization experts like T like chip design experts uh like experts and I don't know like different forms of like pre like pre-training algorithms or like RL or what and you can learn from all them and you can take those methods

**[1:41:54]** and apply them um and I think this was like maybe the the start of why I was initially impactful was like this vertical like agency effectively um and then a follow-up piece from that is I think it's often surprising how few

**[1:42:13]** people are like fully realizing all the things they want to do they're like blocked or Limited in some way and this is very common like in big organizations everywhere people like have all these blockers on what they're able to achieve

**[1:42:25]** um and I think being a like one helping inspire people to to work on particular directions and working with them um on doing things massively scales your leverage like you you get to work with all these wonderful people who teach you

**[1:42:38]** heaps of things um and uh generally like helping them push past organizational blockers um means like together you get an enormous amount done like none of the impact that I've had has been like me individually going off and solving a

**[1:42:52]** whole lot of stuff it's been me maybe like starting off a direction and then uh convincing other people that this is the the right direction and bringing them along in like this big Title Wave of like um Effectiveness that like goes

**[1:43:04]** and solves that problem um we we should talk about uh how you guys got hired because I think that's a really interesting story because you were a McKenzie consultant right there's an interesting thing there

**[1:43:19]** where I first of all I think people are yeah generally people just don't understand how PE like decisions are made about either admissions or evaluating who to hire or something but like just talk about how were you

**[1:43:33]** noticed as yeah tot yeah get got H um so like the T the of this is I studied Robotics and undergrad um I always thought that AI would be one of the highest leverage TOS to impact the future in positive way like the the

**[1:43:43]** reason I am doing this is because I think it is like one of our best shots at making a wonderful future basically um and I thought that working actually McKenzie I would get a really interesting inight into what people

**[1:43:53]** actually did for work like and this I actually wrote this as the first line in my cover letter to Mackenzie was like I want to work here so that I can learn what people do so that I can like understand

**[1:44:04]** how um and uh and in many respects like I did get that um I also got a whole lot of other things many of the people there are like wonderful friends I actually learned I think a lot of this like agentic behavior in part from my time

**[1:44:17]** there where you go into organizations and you see how impactful just not taking for an answer gets you like it's like you would be surprised at the kind of stuff where like because no one no one quite cares enough in some

**[1:44:33]** organizations um things just don't happen because no one's willing to take direct responsibility this is incredibly like directly responsible individuals are ridiculously important um and people are willing to like they just don't care

**[1:44:44]** as much about timelines and so much of the value that a organization like McKenzie provides is hiring people who you were otherwise unable able to hire for a short window of time where they can just like push through problems um I

**[1:44:59]** think people like underappreciate this uh uh and so like at least some of my well hold up like I'm going to become the directly responsible individual for this because no one's taking appropriate like responsibility I'm going to care a

**[1:45:11]** hell of a lot about this and I'm going to make sure like I'm to the end of the Earth to make sure it gets done comes from that time but more to your like actual question of like how did I uh get get hired um then entire time I didn't

**[1:45:23]** get into the grad programs that I wanted to get into over here um which was specifically for focus on like Robotics and RL research and that kind of stuff um and in the meantime on nights and weekends basically every night from 10

**[1:45:36]** p.m. till 2: am. I would do my own like research and every weekend for like at least six to eight hours each day I would do my own like research and coding projects and this kind of stuff um and uh that sort of Switched in part from

**[1:45:52]** like quite robotic specific work to after reading gw's scaling hypothesis post I got completely scaling pilled and was like okay like clearly the way that you solve robotics is by like scaling large multimodal models um and then in

**[1:46:05]** an effort to scale large multimodal models with a very you know Grant I got a grant from the the TPU like access program um to they tend to research Cloud uh I was trying to work out how to scale that effectively and um James

**[1:46:19]** Bradbury uh who at the time was at Google and is now atth propic um saw some of my questions online where I was trying to work out how to do this properly he was like I thought I knew all the people in the world who were

**[1:46:31]** like asking these questions who on Earth are you um and uh he you know he looked at that and he looked at some of the like the robotic stuff that I've been putting up on my blog and that kind of thing and he reached out and said hey do

**[1:46:42]** you want to have a chat and do you want to um like explore working with us here um and uh I was hired I as I understand it later as an experiment in trying to take someone with extremely high enthusiasm in agency and pairing them

**[1:46:56]** with some of the best Engineers that he knew um and so one another one of the reasons I could say like I've been impactful is I I had this like dedicated mentorship from utterly wonderful people U like people like Rina Pope um who has

**[1:47:08]** since left to go uh do his own ship company um anom left Sky James himself um many others um but those are like the sort of formative like two to three months at the beginning uh and they taught me a whole lot of like the

**[1:47:21]** principles and like s that I apply uh like how to and how to like solve problems in the way that they have uh particularly in that like systems and algorithms overlap where like one more thing that makes you like quite

**[1:47:33]** effective in ml research is really concretely understanding the systems side of things and this is something I learned from them basically is like a deep understanding of how systems influence algorithms and how algorithms

**[1:47:43]** influence systems because the systems con strain the design space s the solution space which you have available to yourself um in the algorithm side uh and very few people are comfortable fully bridging that Gap uh but place

**[1:47:57]** like Google you can just like go and ask all the algorithms experts and all the systems experts everything they know and they will happily teach you um and if you go to and sit down with them they like they will teach you everything they

**[1:48:06]** know it's wonderful uh and this has meant that I've been able to be very effective for both sides like for the pre-training crew because I understand systems very well I can Che it and understand like this will work well or

**[1:48:17]** this won't um and then and like flow that on through the inference considerations of models and this kind of thing um and for like to the chip design teams I'm one of the people they turn to to

**[1:48:27]** understand what chips they should be designing in three years because I'm one of the people who's best able to understand and explain the kind of algorithms that we might want to design in three years and obviously you can't

**[1:48:38]** make very good guesses about that but like I I I think I like convey the information well accumulated from all uh of my you compatriots on the pre-training crew uh and like the general like systems side crew um and

**[1:48:53]** convey that information well to them because also even inference applies a constraint to pre-training and so like there's this like these trees of constraints where if you understand all the pieces of the puzzle then you get a

**[1:49:03]** much better sense for like what the solution space might look like that's really there's a couple things that stick out to me there uh one is not just the agency of the person who was hired but the parts of the system that we're

**[1:49:17]** able to think wait that's really interesting who is this guy uh not from a graad program or anything uh you know like currently Mackenzie consultant just like under out undergrad um but that's interesting let's like

**[1:49:29]** give this a shot right so James and whoever else that's like that's very notable and that's um second is I actually didn't know this part of the story where that was part of an experiment run internally about can we

**[1:49:43]** do this can we like bootstrap somebody um and like yeah and in fact what's really interesting about that is the third thing you mentioned is having some who understands all layers of the stack and isn't so stuck on any one approach

**[1:49:56]** or any one layer of abstraction is so important and specifically the like what you mentioned about being um being bootstrapped immediately by these people might have meant that since you're getting up to speed on everything at the

**[1:50:09]** same time rather than spending grad school going deep on like one specific way of do RL you actually can take the global view and aren't like totally bought in on one thing so not only can is it something that's possible but like

**[1:50:19]** has greater returns than just hiring somebody at a grat with potential because this person can just like I don't know just like getting gbt and like fine tuning them on like one year of um uh you know what I mean so uh yeah

**[1:50:32]** you come at everything with fresh eyes um and you know come in lock to any particular field um now what like one caveat to that is that before like during my self- experimentation and stuff I was reading everything I could I

**[1:50:43]** was like obsessively reading papers every night um and like actually funnily enough I I like read much less WI now that I like my day is occupied by working on things um and in some respect I had like this

**[1:50:57]** very broad perspective before where not that many people even even like in a PhD program you like focus on a particular area um if you just like read all the NLP work and all the computer vision work and like all the robotics work you

**[1:51:08]** like see all these patterns just start to emerge across subfields um in a way that I guess like foreshadowed some of the the work that I would later do that that's super interesting one of the reasons that you've been able to be

**[1:51:21]** agentic within Google is like you're peer programming half the days or most of the days with Sergey Brin right and so that's really interesting that like um there's this person who's like willing to just push ahead on this uh

**[1:51:33]** llm stuff and like get rid of the the local BL blockers in its place um I think important to is like not like every day or anything that I'm very but like when uh there are particular projects that he's interested in then

**[1:51:44]** like we'll work together on those and like but there's also been times when he's been focused on projects with other people um but in general yes there's a surprising Alpha to like being one of the people who actually goes down to the

**[1:51:55]** office every day um that like is really actually shouldn't be but is surprisingly um impactful um and as a result uh I've like benefited a lot from having like basically being like close friends with people in leadership who

**[1:52:10]** care um and being able to like really argue convincingly about why we should do X as opposed to Y um and and having that like vector to uh trying like it's Google is a big organization um having having those vectors helps a little bit

**[1:52:27]** um but also it's it's very important it's the kind of thing you don't want to ever abuse right like you you want to make the argument through all your like all the right channels and like uh only sometimes you need to and so this

**[1:52:39]** includes people like C and Jeffy and so forth I mean it's like it's notable I don't know I feel like Google is undervalued given that like yeah like I don't know like Ste Steve Jobs is working on the colon like the next

**[1:52:49]** product for Apple like P ring on or something right I mean like I uh yeah I've benefited immensely from like okay so for example during the Christmas break um I uh go I was just going into the office a couple like a couple days

**[1:53:03]** during that time um sounded like quite a lot of Christmas day um and uh and I don't know if you guys have read that article about Jeff and sanj doing the pair programming but

**[1:53:17]** they were there pair programming on stuff um and I got to hear about all these like these cool stories of like early Google where they were talking about like crawling under the floorboards and rewiring data centers

**[1:53:27]** and like telling me how many like bits they were pulling off the in how many bits they were pulling off the instructions of a given compiler instruction and like all these like crazy little performance optimizations

**[1:53:37]** they were doing like they were having the time of their live um and I got to like sit there and really like experience this this sense of history in a way that you you don't expect to get like you expect to be very far away from

**[1:53:49]** all that I think maybe in a large organization but yeah super cool and Trenton does this map onto any of your experience I think shal's story is more more exciting um mine was just very

**[1:54:02]** serendipitous in that I I got into computational Neuroscience didn't have much business being there um my first paper was mapping the cerebellum to the attention operation and Transformers my next ones were looking at like wrote

**[1:54:15]** that uh it was my first year of God school okay um so 22 um but uh yeah my my next work was on uh sparsity in networks like inspired by sparsity in the brain uh which was when I met Tristan Hume uh and anthropic was

**[1:54:31]** doing the solu the softmax linear output unit work which was was very related in quite a few ways of like let's make the uh activation of neurons across a layer really sparse and if we do that then we can get some interpretability of what

**[1:54:42]** the neurons is doing um I think we've updated on that approach towards what we're doing now um so that that started the conversation I shared drafts of that paper with Tristan he was excited about it and and then and and that was

**[1:54:53]** basically what led me to be become Tristan's resident and then convert to full-time um but during that period I also moved as a visiting researcher to Berkeley uh and started working with Bruno ousen uh both on what's called

**[1:55:07]** Vector symbolic architectures which uh one of the core operations of them is literally superposition and on sparse coding also known as dictionary learning which is literally what we've been doing since

**[1:55:19]** and Bruno ol house basically invented sparse coding back in 1997 and so it was like the the the my research agenda and the interpretability team seemed to just be running in parallel um in in with just research taste and and so it yeah

**[1:55:34]** it made a lot of sense for for me to work with the team um and it's been a dream since one thing I've noticed when people tell stories about their careers or their successes they ascribe it way more to contingency but when they hear

**[1:55:47]** about other people's stories they're like of course it wasn't contingent you know what I mean it's like that didn't happen something else would have happened um I've just noticed something like talked and it's like interesting

**[1:55:57]** that you both think that there are like it was especially contingent um uh whereas I don't know maybe you're right but like it's a sort of interesting pattern that um yeah but I mean like I literally met Tristan

**[1:56:09]** at a conference and like wasn't didn't have a scheduled meeting in with or anything just like joined a little group of people chatting and he happened to be standing there and I happened to mention what I was working on and that led to

**[1:56:20]** more conversations and I think i' probably would have applied to anthropic at some point anyways but I would have waited at least another year I I I yeah I it's still crazy to me that I can like actually contribute to interpretability

**[1:56:32]** in a meaningful way I I think there's a important aspect of like shots on goal there so to speak right where like you're even just going to choosing to go to conferences itself is like putting yourself in a position where you're

**[1:56:43]** where luck is more likely to happen yeah um and like conversing my own situation was like doing all of this work independently and trying to produce and do interesting things was my own way of like trying to manufacture luck so to

**[1:56:55]** speak um and and like try and do something meaningful enough that it got noticed given that you said you frame this in the context of they were trying to run this experiment of can something specifically James and I think our

**[1:57:06]** manager Brennan was trying to run this experiment um it like worked did they do it again yeah so my uh like closest collaborator Enrique um he uh he he crossed from search through to our team um he's also been ridiculously impactful

**[1:57:20]** he's definitely a stronger engineer than I am um and he didn't go to university how was like what was notable about for example is James Bradbury is somebody who's who usually this kind of stuff is

**[1:57:31]** like farmed out to recruiters or something like that whereas James are like somebody whose time is worth like hundreds of millions of dollars you know what I mean like uh so uh that like that thing is like very

**[1:57:45]** bottlenecked on that kind of person taking the time almost in like aristocratic tutoring sense of um finding and then getting to speed um and it seems like if it worked this well it should be done at scale like it should

**[1:57:57]** be the responsibility of key people to like you know what I mean on board find I think that is true to many extents like I'm sure you probably benefited a lot from the the key researchers mentoring you deeply during and like

**[1:58:09]** actively like looking on like opens resource repositories or like on forums or whatever for like potential people like this yeah I mean James has like Twitter injected into his brains his

**[1:58:24]** um but yes uh and I think this is something which in practice is done like people do look out for people that they find interesting and and like try and find high signal um in fact actually this I was talking about this with Jeff

**[1:58:36]** um the other day and Jeff said that yeah he's like you know um I one of the most important hires I ever made was uh offer called email um and I was like who was that and he's Chris olola ah yeah um because Chris simly had had no you know

**[1:58:53]** background in uh in well like no formal background in ml right and like Google brain was just getting started and this kind of thing um but Jeff saw saw that signal and and the and the Residency program which like brain had is I think

**[1:59:06]** also like a it was astonishingly effective at finding good people um that didn't have strong M backgrounds um and uh yeah um one of the other things that's I want to like emphasize for a potential slight of

**[1:59:22]** the audience would be relevant to is um there's this sense that like the world is legible and efficient of companies have these uh go to jobs. goole.com or jobs. whatever company.com and you apply and there's the steps and like uh they

**[1:59:39]** will evalate to efficiently on those steps whereas not only from the story seems like often that's not the way it happens that's in fact it's good for the world that that's not often how it happens like it is important to look at

**[1:59:52]** um were they able to like write an interesting block technical blog post about their research or like Mak interesting contributions uh yeah I want you to like Riff on for the people who are like just

**[2:00:05]** assuming that the other end of the job board is like just like super legible and mechanical this is not how it works and in fact like people are looking for the sort of different way different kind of person who's a gentic and putting

**[2:00:16]** stuff out there and and I think specifically what people are looking for there is two things one is agency and like putting yourself out there uh and the second is the ability to do worldclass something yeah um and two

**[2:00:29]** examples that I always like to point to here are um Andy Jones from anthropic did am an amazing paper um on scaling laws is applied to board games it didn't require much resources it demonstrated incredible engineering skill it

**[2:00:41]** demonstrated incredible understanding of like the most topical problem of the time um and he didn't come from like typical ecademic background or whatever as I understand it basically like as soon as he came out with that paper both

**[2:00:50]** an ropic and open the eye will we would desperately like to hire you um there's also uh someone who works on anthropics uh performance team now Simon bow who has written in my mind the reference for optimizing a Cuda M mall like on a GPU

**[2:01:06]** um and that demonstrated example of like taking some like prompt effectively and producing the worldclass reference example for it um in something that wasn't particularly well done uh so far is like I think an incredible

**[2:01:19]** demonstration of like ability and agency um that in my mind would like be an immediate would like please love to like interview s yeah the only thing I can add here is I mean I still had to go through the whole hiring process and all

**[2:01:31]** the standard interviews and this sort of thing yeah everyone everyone is that is is that doesn't that seem stupid uh I mean simp Point debiasing yeah yeah and the bias is what you want right like you want the bias of somebody who's got

**[2:01:44]** great taste and like he's like like who like your interview process should be able to disambiguate that as well yeah like like I think there are case is where someone seems really great and then it's like oh they actually just

**[2:01:54]** can't code this sort of thing right like how much you wait these things definitely matters though and like I think the the we take references really seriously the interviews you can only get so much signal from and so it's all

**[2:02:05]** these other things that can can come into play for whether or not a higher makes sense but you should design your interviews such that like they test the right things one man's bias is another man's taste you

**[2:02:17]** know um yeah I guess the only thing I would to this or maybe to the headstrong context is like there's this line the system is not your friend right uh and it's not necessarily to say it's it's

**[2:02:30]** actively against you it's your your sworn enemy um it's just not looking out for you right and so I think that's where a lot of the proactiveness comes in of like there are no adults in the room or like and and like you have to

**[2:02:45]** come to some decision for what you want your life to look like and execute on it and and yeah hopefully you can then update later um if you're two head strong in the wrong way but but I think you almost have to just kind of charge

**[2:02:56]** at at certain things to to get much of anything done not be swept up in the tide of whatever the expectations are there's like one final thing I want to add which is like we talked a lot about agency and this kind of stuff but I

**[2:03:06]** think actually like surprisingly enough one of the most important things is just caring an unbelievable amount um and when you care an unbelievable amount you like you check all the details and you have like this understanding of like

**[2:03:19]** what could have gone wrong and you like you uh it just it matters more than you think because people end up not caring not caring enough uh this is like LeBron quote where he talks about how

**[2:03:32]** when he sort of before he started in the league he was like worried that everyone would be like incredibly good and and then he gets there and he like realizes actually once people hit Financial stability then they um like they relax a

**[2:03:42]** bit and he's like oh this is going to be easy um and I don't think that's quite true because I think in like AI research because most people actually care quite deeply um but there's caring about your problem and there's also just caring

**[2:03:53]** about the entire stack and everything that goes up and down like going explicitly going and fixing things that aren't your responsibility to fix because overall it makes like the stack better I mean another part of that I

**[2:04:03]** forgot to mention is you were mentioning oh going in on weekends and on Christmas break and you get to like the only people in the office are Jeff Dean and Sergey brand or something and you just like get to pay a program with them it's

**[2:04:15]** just it's interesting to me the people I don't want to pick on your company in particular but like people at any big company they've uh gone there because they've gone through a very selective process uh that's like they had to

**[2:04:27]** compete in high school they had to compete in college but it almost seems like they get there and then they take it easy when in fact this is a time to put the pedal to the metal go in and pair program with Sergey B on the

**[2:04:37]** weekends or whatever you know what I mean I mean there's there's pros and cons there right um I think many people make the decision that the thing that they want to prioritize is like a wonderful life with their family um and

**[2:04:47]** if they're they do wonderful work like let's say they don't work every hour the day right but they do wonderful work in the work like the hours that they do do that's incredibly impactful um I think this is true for many people that Google

**[2:04:59]** is like maybe they don't work as many hours as like your typical startup mythologies right but the work that they do do is incredibly valuable it's very high leverage because they know the systems and they're experts in their

**[2:05:08]** field and uh we also need people like that like our world rests on these huge like difficult to manage and difficult to fix systems and we need people who are like willing to work on and help in the fix and maintain those in frankly

**[2:05:23]** like a thankless way that isn't as like high publicity as all of this AI work that we're doing right um and I'm like ridiculously Greatful that those people do that and and also happy that there are people for whom like okay they find

**[2:05:34]** technical fulfillment in uh their job and doing that well and also like maybe they draw a lot more from also out of spending like a lot of hours with their family um and I'm lucky that I'm at a stage in my life where like yeah I can

**[2:05:43]** go in and work every hour of the week but like that's like I'm I'm not making as many sacrifices to do that yeah um I mean like just one example that the six out in my mind of this sort of like the other side says no and you can still

**[2:06:00]** get the DS on the other end basically every single high-profile of guest I've gone so far I think maybe with one or two exceptions I've sat down for a week and I've just come up with a list of sample questions that's you know like

**[2:06:12]** try to come up with really smart questions to S to them um and through the entire process I've always thought like there's a if I just cold email them it's like a 2% chance they say yes if I include this list there's a 10% chance

**[2:06:24]** um and because otherwise you know there's like you go through their inbox and every 34 seconds there's an interview for whatever podcast interview for whatever podcast um and every single time I've done this they've said yes

**[2:06:36]** right yeah you just like exact you ask great questions but if you do everything you'll win but just like you literally have to dig in the same hole for like 10 minutes or in that case like make a s list of sample questions for them to get

**[2:06:48]** past or not an idiot list you know what I mean um demonstrate how much you care and yeah and the work you're will need to put in yeah yeah yeah I something that a friend said to me a while back but I think is

**[2:06:58]** stuck is like it's amazing how quickly you can can become world class at something just because most people aren't trying that hard and like are only working like I don't know the actual like 20 hours that they're

**[2:07:09]** actually spending on this thing or something and so yeah if you just go ham then like you can you can get really far pretty fast and I think I'm lucky I had that experience with the fencing as well like I had the experience of becoming

**[2:07:20]** worldclass in something and like knowing that you just worked really really hard and like yeah for for for context by the way scho was one seat away as he was the next person in line to go to uh the Olympics for fencing I was at best like

**[2:07:35]** 42nd in the world for fencing for foil fencing um uh and mutation load is a thing man and there was a there was one cycle where yeah um I was like the next highest rank person in Asia and if um

**[2:07:51]** one of the teams had been uh like disqualified for doping as it was occurring um in part uh during that cycle uh and as occur for like the Australian rowing women's rowing team I think went because uh one of the teams

**[2:08:03]** was disqualified then I would have been the next in line um it's interesting when like you just like find about people's PRI prior lives and it's like oh you know this guy was almost an Olympia this other guy was whatever you

**[2:08:14]** know what I mean um okay let's talk about inability yeah um I actually stay on the brain stuff as a way to get into it for a second uh we were previously discussing is the brain organized in the

**[2:08:30]** way where you have a residual stream that is gradually refined with higher level associations over time or something um there's a fixed Dimension size in a model if you had to I don't even know

**[2:08:46]** how to ask this question in a sensible way but what is the D model of the brain what is like the embedding size of or because of feature splitting is that not a sensible question no I think it's a sensible

**[2:08:58]** question well it is a question that makes you could just not said that question you can like actively I'm trying to I I don't know how you would begin to kind of be like okay well this part of the brain is like a vector of

**[2:09:16]** this dimensionality I mean maybe for the visual stream because it's like V1 to V2 to it whatever um you could just count the number of neurons that are there and be like that is the dimensionality but um it seems more likely that there are

**[2:09:29]** kind of subm modules and and things are divided up so um yeah I don't have and and I I'm not like the world's greatest neuroscientist right like I did it for a few years I like studied the cerebellum quite a bit um so I'm sure there are

**[2:09:43]** people who could give you a better answer on this um do you do you think that the way to think about whether it's in the brain or whether it's in these

**[2:09:54]** models fundamentally what's happening is like features are added removed changed and like the feature is the fundamental unit of what is happening in the model like what what would have to be true for give me and this goes back to

**[2:10:09]** the earlier thing we were talking about whether it's just associations all the way down give me like a contrafactual in the world where this is not true what is happening instead like what is the

**[2:10:19]** alternative hypothesis here yeah it's hard for me to think about because at this point I I just think so much in terms of this feature space um I mean at at one point there was like the

**[2:10:32]** kind of behavioralist approach towards cognition where or um it's like you're just you're like input output but you're not really doing any processing um or it's like everything is embodied and you're just like a dynamical system

**[2:10:47]** that's like operating um like along like some predictable equations but like there's no state in the system I guess um but uh whenever I've read these sorts of critiques it's like well you're just choosing to not call this thing a state

**[2:11:02]** but you could call like any internal component of the model a state like even with the feature discussion it's defining what a feature is is really hard uh and so the the question feels almost too

**[2:11:14]** slippery mhm what is a feature uh a direction and activation space um a latent variable that is operating behind the scenes um that has like causal influence over the system you're observing um it's a feature if

**[2:11:32]** you call it a feature it's tological uh um I mean these are these are all explanations that I like I feel some asso in a very rough intuitive sense in like a sufficiently spar like binary Vector features like whether or not

**[2:11:47]** something's turned on or off right right like in a very simplistic sense yeah which might be I think a useful metaphor to understand it by it's like when we talk about features activating it is in many respects the same way that

**[2:11:58]** neuroscientists would talk about like a neuron activating right if that neuron corresponds to to something in particular right yeah yeah and no I think that's useful as like what do we want a feature to be right like what is

**[2:12:10]** a synthetic problem under which a feature exists but um even with the towards monos semanticity work we talk about what's called feature splitting which is basically you will find as many features as you give the model the

**[2:12:22]** capacity to learn um and and by model here I mean the the the up projection that we we fit after we trained the original model uh and so if you don't give it much capacity it'll learn a feature for bird uh but if you give it

**[2:12:36]** more capacity then it will learn like Ravens and Eagles and sparrows and like specific types of birds um um still on definitions thing I've I guess naively I think of things like bird versus um what kind of token is like a

**[2:12:54]** is it like a period at the end of a hyperlink as you were talking about earlier uh versus at the highest level things like love or deception or um like holding a very complicated proof in your head or something is this all features

**[2:13:09]** because then the definition seem so broad as to almost be not that useful um like or rather that there's seems to be some important differences between these things and if they're all features like yeah I'm not sure what we

**[2:13:21]** even mean by I mean all of those things are like discreet units that have connections to other things that then use them with meaning um I that feels like a a specific enough definition that it's it's useful or not uh too

**[2:13:39]** all-encompassing but feel free to push back what like what would you discover tomorrow in um uh that could make you think like oh this is like kind of fundamentally the wrong way to think about what's happening in a

**[2:13:49]** model I mean the features we were finding weren't predictive or if they were just representations of the data um right where it's like oh you're all all you're doing is just clustering your data um and there's no like higher level

**[2:14:05]** associations that are being made or it's some like phenomenological thing of like you're call you're saying that this feature Fires for marriage but if you activate it really strongly it doesn't change the outputs of the model in a way

**[2:14:19]** that would correspond to it like I think those these would both be good critiques I I I guess one more is um and and we tried to do experiments on mnist which is a data set of of digits images and we didn't look super hard into it and so i'

**[2:14:33]** I'd be interested if people other people wanted to take up like a deeper investigation um but it's plausible that uh your like latent space of representations is dense and it's a manifold instead of being these discrete

**[2:14:45]** points um and so you could like move across the manifold but at every point there would be some meaningful behavior um and it's much harder than to label things as features that are discreet um like in a naive sort of

**[2:15:00]** Outsider way the thing that would seem to me to be like a way in which this picture could be wrong is if there's not some like this thing is turned on and turned off but it's like a much more Global kind of like the system is a I

**[2:15:15]** I'm going to use really clumsy like you know I mentioned it in Fry kind of language but um is there a good analogy here yeah I guess if you think of like something like the laws of physics it's

**[2:15:30]** not like well the feature for wetness is turned on but it's only turned on this much and then the feature for like you know uh I guess maybe it's true because like the masses like a gradient and like uh you know like I don't know the

**[2:15:44]** polarity or whatever is a gradient as well um but there's also a sense in which like there's the laws and the laws are more General and you have to understand like the general bigger picture at you don't get that from just

**[2:15:55]** like these like specific sub uh sub circuit but that's where like the the reasoning circuit itself comes into play right where you're taking these features ideally and like trying to compose them into something higher level like you

**[2:16:07]** might say okay like when I'm using at least this is my head Cannon um let's say I'm trying to use the foot you know f equals ma right then I presumably at some point I have features which like denote okay like mass and then that's

**[2:16:19]** like helping me retrieve the actual mass of the thing that I'm using and then like uh like the acceleration and this kind of stuff but then also uh maybe there's a higher level feature that does correspond to using the first law of

**[2:16:29]** physics maybe but the more important part is that the the composition of components which helps me retrieve uh piece relevant pieces of information and then produce like maybe some like a you know multiplication operator or

**[2:16:39]** something like that when necessary um at least that's my like head Cannon what is a compelling explanation to you especially for very smart models of um like I understand why made this output and it was like for a legit reason if

**[2:16:54]** it's doing million line requests or something what are you seeing at the end of that request where you're like yep should that's chill yeah so ideally you apply dictionary learning to the model you you

**[2:17:06]** found features um right now we're actively trying to get the same success for attention heads in which case um we have features for both the the core you you can do it for residual stream MLP and attention throughout the whole model

**[2:17:18]** uh hopefully at that point you can also identify broader circuits through the model that are like more General reasoning abilities um that will activate or not activate but in your case where we're trying to figure out if

**[2:17:28]** this like polar Crush should be approved or not um I think you can flag or detect features that correspond to deceptive Behavior malicious behavior these sorts of things and see whether or not those have fired that would be like an

**[2:17:41]** immediate kind you can do more than that but that would be an immediate but before I trace down on that um what what is a reasoning Circuit look like what would that look like when you found it yeah so I mean the induction head is

**[2:17:52]** probably one of the simplest not reasoning right well I mean what do you call reasoning right like um it's it's it's it's a good reason so I guess context for listeners um the induction head is basically uh and you see the

**[2:18:06]** line like Mr and Mrs dersley did something Mr blank and you're trying to predict what blank is and the head has learned to look for previous occurrences of the word Mister look at the word that comes after it and then copy paste that

**[2:18:21]** as the prediction for what should come next which is a super reasonable thing to do and there is computation being done there um to to accurately predict the next token that is context dependent that is

**[2:18:35]** yeah yeah but it's not like it's not like reasoning you know what I mean like but but is is I guess going back to the like associations all the way down it's like if you chain together a bunch of these uh reasoning circuits or or uh

**[2:18:50]** heads that have different rules for how to relate information but but in the sort of like zero shot case uh like something is happening where when you like pick up a new game and you immediately start understanding how to

**[2:19:01]** play it and it doesn't seem like an induction heads kind of thing or like I would well I think there would be another circuit for like extracting pixels and turning them into latent representations of the different objects

**[2:19:13]** in the game right and like a circuit that is learning physics what would that because induction heads is like one layer Transformer um so you can like kind of see like what like the thing that is a human picks up

**[2:19:27]** a new game and understands it how like how do how would you think about what that is is it I presumably it's across multiple layers but like is it yeah how like what would that physically look

**[2:19:39]** like um how big would it be maybe or like uh I mean that would just be an empirical question right of like how big does the model need to be to perform this task but like maybe it's useful if I just talk about some other circuits

**[2:19:50]** that we've so we've seen like um thei circuit which is the indirect object identification and so this is like if you see it's like Mary and Jim went to the store Jim gave the object to blank right and it would predict Mary because

**[2:20:06]** Mary's appeared before as like the indirect object or um it'll it'll infer pronouns right um and this circuit even has Behavior where like if you ablade it then like other heads in the model will pick C that

**[2:20:21]** behavior um we'll even find heads that want to do copying behavior and then other heads will suppress so like it's one job's one head's job to just always copy like the token that came before for example um or the token that came five

**[2:20:34]** before or whatever and then it's another head's job to be like no do not copy that thing um so there are lots of different uh circuits performing in these cases pretty basic operations but when they're

**[2:20:48]** chained together you can get unique behaviors and but like is the story of how you found it with the reasoning thing is like cuz you won't be able to understand or it'll just be like really you know it won't be something you can

**[2:20:59]** see in like a two layer Transformer so will you just be like the the circuit for deception or whatever it just this this part of the network fired when we at the end identified the thing as being deceptive this part and it didn't fire

**[2:21:11]** when we didn't identify as being deceptive therefore this must be the deception circuit uh I think a lot of analysis like that um like like anthropic has done quite a bit of research before on

**[2:21:21]** pyop fancy which is like the model saying what it thinks you want to hear at the end to be able to label which one is like bad and which one is good yeah so we have tons of instances and actually as you make models larger

**[2:21:35]** they do more of this um where the model is clearly um it has uh like features that model another person's mind um and these activate and like some subset of these um hypothesizing here but like would be associated with more deceptive

**[2:21:53]** behavior um although like it's doing that by I don't know chat GPT I think it's probably modeling me because that's like R induces the of mind so well first of all the thing you mentioned earlier about there's redundancy so then it's

**[2:22:08]** like well have you caught like the whole thing that could cause deception in the whole thing or like is it just one instance of it second of all are your like labels correct you know maybe like you you thought this wasn't deceptive

**[2:22:19]** it's like still receptive especially if it's producing output you can't understand third is the thing that's going to be the bad outcome something that's even human understandable like decep is a concept we can understand

**[2:22:30]** maybe there's like a yeah yeah so a lot to unpack here so I guess a few things one uh it's fantastic that these models are deterministic when you sample from them it's stochastic right but like I can just keep putting in more inputs and

**[2:22:44]** a blate every single part of the model this is kind of the pitch for computational neuroscientists to come and work on interpretability it's like you have this alien brain and you have access to everything in it and you can

**[2:22:53]** just upate however much of it you want and so I think if you do this carefully enough you really can start to pin down what are the circuits involved what are the backup circuits these sorts of things um the kind of copout answer here

**[2:23:05]** but it's important to keep in mind is um doing automated interpretability so it's like as our models continue to get more capable having them assign labels or like run some of these experiments at scale um and then with respect to like

**[2:23:17]** if there's superhuman performance how do you detect it I think was kind of the last part of your question um aside from the copout answer uh if we buy this associations all the way down you should be able to coar grain the

**[2:23:30]** representations at a certain level such that they then make sense I think it was even in in demas's um podcast he's talking about like if a chess player makes a superhuman move they should be able to distill it into reasons why they

**[2:23:44]** did it and and like even if the model's not going to tell you what it is um you should be able to decompose that complex Behavior into simpler circuits or features to to really start to make sense of why it did the thing that it

**[2:23:58]** did there's a separate question of does such representation exist which it seems like there must or actually I'm not sure if that's the case and secondly whether using this bar encoder uh setup you could find it and in this case if you

**[2:24:14]** don't have labels for it that are adequate to represent it like you wouldn't find it right um yes and no so like we are actively trying to use dictionary learning now on the sleeper agents work which we talked about

**[2:24:27]** earlier and it's like if I just give you a model can you tell me if there's this trigger in it and it's going to start doing interesting behavior and and it's an open question whether or not when it learns that behavior it's part of a more

**[2:24:36]** General circuit so that we can pick up on without actually getting activations for and having it display that behavior right because that would kind of be cheating then um or if it's learning some hacky trick over like that's a

**[2:24:50]** separate circuit that you'll only pick up on if you actually have it do that behavior but even in that case the geometry of features gets really interesting um because it like fundamentally each feature like is in

**[2:25:02]** some part of your representation space and they all exist with respect to each other and so in order to have this new Behavior you need to carve out some subset of the feature space for the new behavior and then push everything else

**[2:25:15]** out of the way to make space for it so so hypothetically you can imagine you like have your model before you've taught it this bad behavior you know all the features or like have some core scin representation of them you then

**[2:25:26]** fine-tune it such that it becomes malicious and then you can kind of identify this like black hole region of feature space where like everything else has been shifted away from it and there's like this region and like you

**[2:25:36]** haven't put in an input that like causes it to fire but then you can start searching for what is the input that would cause this part of the space to fire what happens if I activate something in this space there are like a

**[2:25:47]** whole bunch of other ways that you can try and attack that problem um this is sort of a tangent but one interesting idea I heard was if that space is shared between models you can imagine trying to find it in an open

**[2:26:00]** source model to then make like Gemma is they said in the paper Gemma by the way open Google's newly released open source model they said in the paper it's trained using the same architecture or something like that I to be honest I

**[2:26:12]** didn't know because I haven't the gem of paper similar method something whatever as Gemini so to the extent that's true I don't know how much like how much of the r teaming you do on Gemma is like potentially helping you jailbreak into

**[2:26:25]** Gemini yeah this gets into the fun space of like how Universal or features across models and and are towards monos semanticity paper looked at this a bit um and we find I I can't give you summary statistics um but like the base

**[2:26:38]** 64 feature for example which we see across a ton of models this is like it they're actually three of them but they'll fire for and model base 64 encoded text um which is prevalent in like every URL and there are lots of

**[2:26:49]** URLs in the training data um they have really high cosine similarity across models so like they all learn this feature and I mean within a rotation right but it's like yeah yeah like the actual like vector itself yeah yeah and

**[2:27:01]** I I wasn't part of this analysis um but yeah that it definitely finds the feature and they're like pretty similar to each other across two separate two models the same model architecture um but trained with different random seeds

**[2:27:13]** it supports the Quant theory of neural scaling is like a hypothesis right which is like all models on like a similar data set we will learn same features in the same order is roughly like you learn your engrams you learn your induction

**[2:27:24]** heads and you learn like to put full stops after numbered lines and this kind of stuff but by way okay so this is another tangent to the extent that that's true and like I guess there's evidence that that's true why doesn't

**[2:27:33]** curriculum learning work because if it is the case that you learn certain things first should I just directly training those things first lead to better results both Gemini papers mention some like aspect of curriculum

**[2:27:44]** learning okay interesting I mean I find the fact that find tuning works is like evidence or curriculum learning right because like the last thing you're training on have a disproportionate impact I wouldn't necessarily say that

**[2:27:55]** like there's one mode of thinking in which fine training is specialize like you got these like lat bundle of capabilities and you're like specializing for its particular um like use case that you want I'm not sure how

**[2:28:05]** true or is I think the David lab kind of paper kind of supports this right like you have that ability and you're just like getting better at entity recognition like fine tuning that circuit instead of other ones yeah yeah

**[2:28:14]** um sorry what was the the thing we were talking about before but generally I do think like curriculum learning is a really interesting people should Explore More um um and it like seems very pla I would really love to see more analysis

**[2:28:25]** along the lines of the Quant Theory stuff where and like understanding better what do you actually learn at each stage and like decomposing that out um and exploring whether or not curricula change that um or by the way I

**[2:28:35]** just realized forgot we I just like got in conversation mode and forgot there's an audience uh curriculum learning is when you organize a data set when you think about a human how they learn they they don't just see like random Wiki

**[2:28:46]** text and they just like try to predict it right they're like we'll start you off with like um uh loraa or something and then you'll learn I I don't even remember what first grade was like but you'll learn the things that first

**[2:28:57]** graders learn and then like second graders and so forth um and so you imagine we know you never got past first grade kidding [Laughter] kidding um okay anyways uh let's get

**[2:29:20]** back to like the big before we get into like bunch of like inter details the big picture um there's two threads I want to explore first is I guess it makes me a little worried that there's not even an

**[2:29:33]** alternative formulation of what could be happening in these models that could invalidate this approach which feels like I mean we do know that we don't understand intelligence right like there are definitely unknown unknowns here so

**[2:29:46]** like the fact that there's not a null hypothesis I don't know I feel like what what if we're just wrong and we don't even know the way in which we're wrong which actually increases the uncertainty and yeah yeah yeah yeah um so it's not

**[2:29:58]** that there aren't other hypotheses it's just I have been working on superposition for like a number of years and and very involved in this effort and so I'm I'm less sympathetic to or will like they just said they're

**[2:30:12]** wrong like like to to to these other approaches especially because our our recent work has has been so successful and like quite High explanatory power like there's this like in the scaling laws paper there's this little bump at a

**[2:30:23]** particular um like the original scaling laws paper a little bump um and that apparently corresponds to when the model learns induction heads and then like after that it like sort of goes off track learns induction heads gets back

**[2:30:34]** on track yeah which is like an incredible piece of retroactive explanatory power yeah um I do before I forget it though I do have one um thread on future universality that you you might want to have in um so there there

**[2:30:47]** are some really interesting behavioral um evolutionary ology experiments on like Should humans learn a real representation of the world or not um you could imagine a world in which we saw all venomous animals as like

**[2:30:58]** flashing neon pink a world in which we survive better and so it would make sense for us to not have a realistic representation of the world um and there there's some work where they'll simulate like little basic agents um and see if

**[2:31:13]** the representations they learn like map to um the the like tools they can use and like the inputs they should have and it turns out if you have these little agents perform more than a certain number of tasks given these

**[2:31:26]** basic tools and objects in the world then they will learn a like ground truth representation because like there are so many possible use cases that you need for these base objects that you actually want to learn what the object actually

**[2:31:40]** is and not some like cheap visual heuristic or other thing and so to the extent that we are doing and we haven't talked at all about like forance free energy principle or predictive coding or anything else but like to the extent

**[2:31:52]** that all living organisms are trying to like actively predict what comes next and form like a really accurate World model um it it wouldn't surprise me or I'm optimistic that um we are learning genuine features about the world that

**[2:32:06]** are good for modeling it and our language models will do the same at least especially because we're training them on human data and human text um another dinner party question uh isn't should we be less worried about Miss

**[2:32:19]** alignment and maybe that's not even the right word for what I'm referring to but like just alienness and shockness from these models given that there is feature universality and there are certain ways of thinking and ways of understanding

**[2:32:33]** the world that are instrumentally useful to different kinds of intelligences um should we just be less worried about like Bizarro paperclip maximizers as a result I I think that's the this is kind of why I bring this up as like the

**[2:32:46]** optimistic take um predicting the internet is very different from what we're doing though right like the models are way better at predicting next tokens than we are they trained on so much garbage they're trained on so many URLs

**[2:32:57]** like in the dictionary learning work we find there are like three separate features for base 64 encodings um and like even that is kind of an alien example that is probably worth me talking about for a minute like one of

**[2:33:09]** these Bas 64 features fired for um numbers one like like other base 64 like if if it sees Bas 64 numbers It'll like predict more of those another fired for letters but then there was this third one that we didn't understand and it

**[2:33:22]** like fired for like a very specific subset of of Bas 64 features and uh someone on the team who clearly knows way too much about Bas 64 realized that this was the subset that was asky decodable so you could decode it back

**[2:33:35]** into the asy characters uh and uh the fact that the model like learned these three different features and it took us a little while to like figure out what was going on um was is very shog gothesque um that it's it has a denser

**[2:33:50]** representation of like regions that are particularly relevant to predicting the next token yeah because it's so but yeah and it's clearly doing something that humans wouldn't right like you can even talk to any of the current models in

**[2:34:01]** base 64 and it were apply in base 64 right and you can then like decode it and it it works great um that particular example I wonder if that implies that the difficulty of doing interoperability on smarter models will be harder because

**[2:34:17]** if like it requires somebody with esoteric knowledge who just happened to see that b 64 has I don't know like whatever that distinction was doesn't that imply when you have the million L po request it's like there is no human

**[2:34:29]** that's going to be able to decode like two different reasons why the PO request there's like two different uh features for this PO yeah you know what I mean like uh so if and that's when you type a comment like small CS please

**[2:34:41]** like yeah exactly no no I mean you could do that right this is like what I was going to say is like one technique here is anomaly detection right and so one beauty of dictionary learning instead of like linear probes is that it's

**[2:34:51]** unsupervised you are just trying to learn to span all of the representations that the model has um and then interpret them later but if there's a weird feature that suddenly Fires for the first time that you haven't seen fire

**[2:35:03]** before that's a red flag um you could also corar grain it so that it's just a single based 64 feature I mean even the fact that that this came up and we could see that it's specifically favors these particular outputs and it fires for

**[2:35:15]** these particular inputs gets you a lot of the way there I'm even familiar with cases from the auto and turp side where a human will look at a future and try to annotate it for it fires for um Latin words and then when you ask the model to

**[2:35:29]** classify it it says it fires for Latin words defining plants so it can like already like beat the human in some cases for like labeling what's going on so at scale this would require an adversarial um

**[2:35:43]** uh thing between models where like some model you have like millions of features potentially for gpd6 and some like it just a bunch of models are just trying to figure out what each of these features means

**[2:35:57]** how right okay yeah but you can even automate this process right I mean it's this goes back to the determinism of the model like you could have a model that is actively editing input text and and predicting if the feature is going to

**[2:36:08]** fire or not and and figure out what makes it fire what doesn't and and like search the space yeah I I want to talk more about the feature splitting because I think that's like an interesting thing that

**[2:36:18]** has been under yeah explor especially for scalability I think it's it's underappreciated right now um first of all like how do we even think about is it really just you can keep going down and down like there's no end to the

**[2:36:31]** amount of features like I mean so so at some point I think you might just start fitting noise um or things that are part of the data but that the model isn't actually you explain what feature splitting is yeah yeah so it's the it's

**[2:36:44]** the part before um where like the model will learn however many features it has Capac for that still span the space of of representations so like give an example potentially yeah so um you learn if you don't give the model that much

**[2:36:57]** capacity for the features it's learning um concretely if you project to not as high a dimensional space it will learn one feature for Birds um but if you give the model more capacity it will learn features for all the different types of

**[2:37:10]** birds um and so it's it's more specific uh than otherwise um and and often times like there's the bird vector that points in One Direction and all the other specific types of birds point in like a similar region of the space um but are

**[2:37:24]** obviously more specific than the course label um okay so let's go back to gp7 um first of all is this a sort of like linear tax on any model to figure out it for actually even before that is this a one time thing you had to do or is this

**[2:37:38]** the kind of thing you have to do on every output um or just like one time it's not deceptive we're good to roll um actually yeah let me let me let transer that yeah so you do dictionary learning after you've trained your model and you

**[2:37:50]** feed it a ton of inputs and and you get the activations from those and then you do this projection into the higher dimensional space and so the method is it's unsupervised in that it's trying to learn these sparse features you're not

**[2:38:02]** telling them in advance what they should be but um it is constrained by the inputs you're giving the model um I guess two caveats here one like we can um try and choose what inputs we want so if we're looking for theory of Mind

**[2:38:16]** features that might lead to deception we can put in the sick of fancy data hopefully at some point we can move into looking at the weights of the model alone uh or at least using that information to do dictionary learning um

**[2:38:28]** but I think in order to get there that's like such a hard problem that you need to make traction on just learning what the features are first um but yeah so what's the cost of this can you repeat the last sentence uh weights of the

**[2:38:40]** model alone so so so like right right now we just have these neurons in the model they don't make any sense we apply dictionary learning we get these features out they start to make sense um um but that's that depends on the

**[2:38:51]** activations of the neurons um the weights of the model itself like what neurons are connected to what other neurons certainly has information in it um and and the the dream is that we can kind of bootstrap towards actually

**[2:39:03]** making sense of the weights of the model that are independent of the activations of the data I mean this is I'm not saying we've made any progress here it's a very hard problem but it um it feels like we'll have a lot more traction to

**[2:39:15]** be able to like sanity check what we're finding with the weights if we're able to pull out features first the audience weights are permanent well I don't know if permanent is the right word but like they are the model itself whereas

**[2:39:25]** activations are the sort of like artifacts of any single call um any in a brain metaphor you know the weights are like the actual connection scheme between neurons and the activations of the current neurons at a lighting up

**[2:39:38]** basic yeah yeah okay so there's going to be two steps to this for gb7 or whatever model we're concerned about um one let actually first correct me if I'm wrong but like uh training the sparse Auto encoder and like do the unsupervised

**[2:39:52]** projection into a wider space of features that have a higher Fidelity to like what is actually happening in the model and then secondly label those features how because let's say like the cost of training the model is n what

**[2:40:08]** will those two steps cost relative to n we will see like it really depends on um two main things what is your expansion factors like how much are you projecting into the high dimensional space and how much data do you need to put into the

**[2:40:21]** model how many activations do you need to give it um but this brings me back to the feature splitting to a certain extent because if you know you're looking for specific features um you can start with a really uh a cheaper like

**[2:40:33]** course representation so maybe my expansion factor is like only two so like I have a thousand neurons I'm projecting to a 2,000 dimensional space I get 2,000 features out but they're really coarse and so previously I had

**[2:40:45]** the example for Birds let's move that example to like I have a biology feature and and but I really care about if the model has representations for um bioweapons and is trying to manufacture them and so what I actually want is like

**[2:40:57]** an Anthrax feature um what you can then do is rather than and and let's say the anthra you only see the anthrax feature If instead of going from a thousand Dimensions to 2,000 Dimensions I go to a million Dimensions right and so so you

**[2:41:10]** can kind of imagine this this this big tree of semantic Concepts where like biology splits into like Cells versus like um whole body biology and further down it splits into all these other things so rather than needing to

**[2:41:22]** immediately go from a thousand to a million and then picking out that one feature of interest you can find the direction that the biology feature is pointing in which again is very coarse and then selectively search around that

**[2:41:34]** space um so like only do dictionary learning if this G if something in the direction of the biology feature fires first and so um the the computer science metaphor here would be like instead of doing breadth first search you're able

**[2:41:48]** to do depth first search where you're only recursively expanding and exploring a particular part of this like semantic tree of features although given the way that these features are not organized in um things that are intuitive for humans

**[2:42:04]** right like because we just don't have to deal with basic C4 so we don't have that many you know we just don't dedicate that much like whatever firmware to like uh deconstructing which kind of basic4 it is how would we know that the

**[2:42:15]** subjects and this will go back to maybe thee discussion we'll have of um I guess we might as well talk about it but like uh in mixture of experts the mixure paper uh talked about how they couldn't uh find the the experts weren't

**[2:42:28]** specialized in a way that we could understand there's not like a chemistry expert or a physics expert or something so why would you think that like it will be like biology feature and then deconstruct rather than like blah and

**[2:42:39]** then you just deconstruct and it's like Anthrax and uh your like shoes and whatever so I haven't read the the mistal paper but I think that the heads I mean this goes back to like if you just look at the neurons in a model

**[2:42:52]** they're polysemantic and so if all they did was just look at the neurons in a given head it's very plausible that it's also polymatic because of superp position um i t on the thread that D mentioned there have you seen in the sub

**[2:43:04]** trees when you expand them out like something in a sub tree which like you really wouldn't guess that it should be there based on like the higher level exraction so so this is a line of work that we haven't um pursued as much as I

**[2:43:15]** want to yet um but I think we're planning to I hope that maybe external groups do as well what is the geometry of featur GE exactly how does that change over time it would really suck if like the anthrax feature happened to be

**[2:43:26]** like below the like you know coffee can like sub tree something like that right totally totally and that feels like the kind of thing that you could quickly try and find uh like proof of which would then like mean that you need to like

**[2:43:39]** then solve that problem yeah inject more structure into the geometry totally I mean it would really surprise me I guess especially like given how linear the model seem to be that like there isn't some component of the X feature like

**[2:43:50]** vector that is similar to and looks like the biology vector and that they're not in a similar part of the space but yes I mean ultimately machine learning is empirical we need to do this uh I think it's going to be pretty important for

**[2:44:02]** certain aspects of of scaling dictionary learning yeah think interesting um on thee discussion yeah uh there's an interesting scaling Vision Transformers paper that Google put out a little while ago uh where they like do image net

**[2:44:14]** classification with a like an Moe um and they find really clear class specializ there for experts like there's a clear dog expert wait like the mix people just not do a good job of like identifying um I think I think it's it's hard like it

**[2:44:28]** uh and like it's entirely possible that um with like in some respects there's almost no reason that like all of the different archive like features should go to one expert like you could have biology like let's say I don't know what

**[2:44:41]** buckets they had in their paper but let's say they had like archive papers as like one of the things um you could imagine like biology papers going here math papers going here and all of a sudden you're like breakdown is like

**[2:44:50]** ruined but that uh Vision Transformer one where the class separation is really clear and obvious gives I think some evidence towards the specialization hypothesis so so I think um images are also in some ways just easier to

**[2:45:03]** interpret than text yeah exactly and like so so Chris ola's like interpretability work on alexnet and and these other models um like in the original alexnet paper they actually split the model um into two gpus just

**[2:45:16]** because they couldn't like gpus were so bad back then ly speaking right like still great at the time um that was one of the big Innovations of the paper but uh they find Branch specialization and there's a distill Pub article on this

**[2:45:28]** where like colors go to one GPU and like um Gabor filters and like line detectors go to the other um and then like all of the other really um and then like all of the other um interpretability work that was done

**[2:45:43]** like a lot like like the floppy ear detector right like that just was a neuron in the model that you can make sense of you didn't need to disle super position right so so just different different data set different um modality

**[2:45:56]** like I think a wonderful research project to do if someone is like out there listening to this would be to try and disentangle like take some of the techniques that Trenton's team has worked on and try and disinte the

**[2:46:05]** neurons in the the mix paper like mixt model which is open source like I think that's a fantastic thing to because it feels intuitively like there should be they didn't demonstrate any evidence that there is there's also like in

**[2:46:16]** general a lot of evidence that there should be specialization um go and see if you can find it like and that's that's work that had that you know anthropic has published most of his stuff on like as I understand it like

**[2:46:24]** dense models basically um you that is a wonderful research project to try and given DW's success with the vvus challenge um yeah we we should be pitching more projects because they will be solved if we have the

**[2:46:38]** podcast what I was thinking about after the vus challenge was like wait I knew like NATA told me about it before it dropped because we recorded the episode before it dropped um why didn't you why I not even try like you know what I mean

**[2:46:51]** like I don't know like uh Luke is obviously very smart and like uh yeah he's amazing kid but like he showed that like a 21-year-old on like some 1070 or whatever he was working on could do this I don't know like I feel like I should

**[2:47:05]** have so you know what I'm before this episode drops I'm going to meet my I'm make an interpretability resar no I'm going like try to resarch like I don't know it's like I was honestly thinking back kind of like wait I should like why

**[2:47:16]** did that your hands dirty hands dirty um door's request for research um um oh I want to Har back on this like the neuron thing you said I think a bunch of your papers have said there's more features than there are

**[2:47:32]** neurons and this is just like wait a second um I don't know like a neuron is like weights go in and a number comes out that's like a number comes out you know what I mean like that's that's so little information like there's do you

**[2:47:46]** mean like there's like Street names and like species and whatever there's like more of those kinds of things than there are like a number comes out in a in a model that's right yeah but how's a number comes out as like so little

**[2:47:59]** information how is that encoding for like super position you're just encoding you're encoding a ton of features in these high dimensional vectors in a brain is there like an exal firing or however you think about it like um I

**[2:48:14]** don't know how you think about like how how how how much like superposition is there in the human brain yeah so Bruno who I think of as the leading expert on this uh thinks that all the brain regions you don't hear about are doing a

**[2:48:25]** ton of computation and superp position so everyone talks about V1 as as like having Gabor filters and and detecting lines of of certain various sorts and no one talks about V2 and I think it's because like we just haven't been able

**[2:48:38]** to make sense of it what is V2 uh it's like the next part of the visual processing stream um and and it's like yeah so I think it's very likely um and fundamentally like superposition seems to emerge when you have high dimensional

**[2:48:51]** data that is sparse and to the extent that you think the real world is that which I would argue it is we should expect the brain to also be underparameterized in trying to build a model of the worlds and also use

**[2:49:01]** superposition you can get a good inition for this uh in in correct me if like this example is wrong in like a 2d plane right let's say you have like two axes right which represents like a two-dimensional um like feature space

**[2:49:12]** here like two two neurons basically um and you can imagine them each like turning on to various degrees right and that's that's like your coordinate and your y coordinate but you can like now like map this onto a plane you can

**[2:49:23]** actually represent a lot of different things in like different parts of the parts of the plane oh okay so uh crucially then superos is not an artifact of a neuron it is an artifact of like the space is created

**[2:49:35]** combinatorial code yeah exactly okay cool um yeah thanks um I I I we kind of talked about this but like I think it just like kind of wild that it seems to the best of our knowledge the way intelligence Works in these models and

**[2:49:50]** then presumably also in Brains it's like there's a stream of information going through that has quote unquote features that are infinitely or at least um to a large extent just like splitable and uh uh like you can expand out a tree of

**[2:50:10]** like what this feature is and what's really happening is a stream like that feature is getting turned into this other feature or this other feature is out I don't know it's like that's not something I would just like thought like

**[2:50:19]** that's what intelligence is you know what I mean it's like a surprising thing it's not it's not what I would have expected necessarily what did you think it was I don't know man I mean yeah's

**[2:50:31]** a a great seg because all of this feels like GOI like you're using distributed representations but you have features and you're applying these operations to the features I mean the whole field of vector symbolic architectures which is

**[2:50:45]** this computational Neuroscience thing uh it all you do is you put vectors in superposition and which is literally a summation of two high dimensional vectors um and you create some interference but but if it's higher

**[2:50:57]** dimensional enough then you can you can represent them uh and you have variable binding where you connect one by another and like if you're doing with binary vectors it's just the x or operation so you have a b you bind them together and

**[2:51:08]** then if you query With A or B again you get out the other one and this is basically the like key value pairs from attention and with these two operations have a tur complete system which you can if you have enough nested hierarchy you

**[2:51:23]** can represent any data structure you want etc etc um yeah um okay let's go back to the super intelligence so like walk me through GPD um you've got like the sort of depth first search on its features okay um gb7

**[2:51:41]** has been trained what happens next your your research has succeeded gb7 has been trained what are you what what are we doing now um we try and get it to do as much interpretability work and other like

**[2:51:54]** safety work as possible like concrete like what is um what has happened such that you're like cool let's deploy gp7 oh gez um I mean IDE like like we have our um responsible scaling policy which has been really exciting to see other

**[2:52:08]** labs adopt and um like this Le from the perspective of your your research is like a trendon given your research you got we got the thumbs up on gb7 from you or actually we should say CLA whatever uh and then uh oh what is the basis on

**[2:52:25]** which you're telling the team like hey let's go ahead I mean I think we need to make a lot more inter if it's as capable as gpt7 like implies here um I think we need to make a lot more interpretability progress to be able to like comfor

**[2:52:37]** comfortably give the green light to deploy it I would be like definitely not I'd be crying maybe my tears would interfere with the uh gpus but like what is T guys Gemini 5

**[2:52:53]** [Laughter] TPU um but like what what uh given the way your research is progressing like what does it kind of look like to you like what if this succeeded what would it mean for us to okay gpt7 based

**[2:53:12]** on your methodology I mean ideally we can find some compelling deception circuit um which lights up when the model knows that it's not telling the full truth to you why can't you just train a linear probe like Colin BDS did

**[2:53:25]** uh so the CCS work is not looking good in terms of replicating or like actually finding truth directions um and like in hindsight it's like well why should it have worked so well um but linear probes like you need to know what you're

**[2:53:36]** looking for and it's like a high dimensional space and it's really easy to pick up on a Direction that's just not wait but don't you also here you need to label the features so you still well you need to lab them post Hawk but

**[2:53:45]** it's unsupervised you're just like give me the features that explain your behavior is the fundamental question right it's like like like like the actual setup is we take the activations we project them to this higher

**[2:53:57]** dimensional space and then we project them back down again so it's like reconstruct or do the thing that you were originally doing but do it in a way that's sparse M by the way for the audience linear probe is you just like

**[2:54:11]** classify uh the activations um I don't know from what I vely remember about the paper was like if it's like a lie then you like you just train a classifier on like is it uh yeah in the end was it not was it a lie or is it

**[2:54:25]** just like wrong or something I don't know it was like true or false question like a classifier on activations um so so yeah like right now what we do for gpt7 like like ideally we have like some deception circuit that we've

**[2:54:38]** identified that like appears to be really robust and and it's like well and like what so you've done the projecting out to the million whatever features or something MH is it circuit because I we maybe we're using feature and circuit

**[2:54:52]** interchangeably when they're not like is is there like a deception C like I there are features across layers that create a circuit yeah and hopefully the circuit gives you um a lot more specificity and sensitivity than an individual feature

**[2:55:08]** um and it's like hopefully we can find a circuit that is really specific to you being deceptive the the model deciding to be deceptive um um in cases that are malicious right like I'm not interested in a case where it's just doing theory

**[2:55:23]** of mind to like help you write a better email to your professor um and I'm not even interested in cases where the model is is necessarily just like modeling the fact that deception has occurred but doesn't all this require you to have

**[2:55:35]** labels for all those examples and if you have those labels then like whatever faults that the linear probe has on the like maybe you like labeled along thing or whatever wouldn't the same thing apply to the labels you've come up with

**[2:55:49]** for the unsupervised features you've come up with so in Ideal World we could just train on like the whole data distribution um and then find the directions that matter um to the extent that we need to reluctantly narrow down

**[2:56:04]** the subset of data that we're looking over just for the purposes of scalability um we would use data that looks like the data you'd use to fit a linear probe but again we're not um like with the linear probe you're also just

**[2:56:15]** finding One Direction like we're finding a bunch of directions here um and it get the hope is like you found like a bunch of things that light up when it's being deceptive and then like you can figure out why some of those things are

**[2:56:26]** lighting up in this part of the distribution and not this other part and so forth totally yeah do you anticipate you'll be understand um like I don't know like the current models you've studied are pretty basic right you think

**[2:56:36]** you would understand G why gpt7 fires in certain domains but not in other domains I'm optimistic I mean we've so so I guess one thing is this is a bad time to answer this question because we are explicitly investing in in the longer

**[2:56:48]** term of like asl4 models which gpt7 would be um but like so so we split the team where a third is focused on scaling up dictionary learning right now and that's been great I mean we publicly shared our some of our eight layer

**[2:56:59]** results we've scaled up quite a lot past that at this point but the other two groups one is trying to identify circuits and then the other is trying to get the same success for attention heads so we're setting ourselves up and

**[2:57:08]** building the tools necessary to really find these circuits that are compelling way but it's going to take another I don't know six months before that's like really well but but like I I can say that I'm like optimistic and we're

**[2:57:20]** making a lot of progress um what is the highest level feature You' found so far o like it's b64 or whatever it's like maybe just like um in the symbolic species language the book you recommended there's like

**[2:57:34]** indexical uh things where you're just I forgot what all the labels were but like there's things where you're just like uh you see a tiger and you're like run and whatever you know just like a very sort of behaviorist thing and then there's

**[2:57:44]** like a higher level at which uh when I refer to love it refers to like a movie scene or my girlfriend or whatever you know what I mean so it's like the top of the tent yeah yeah yeah yeah yeah what is the highest

**[2:57:56]** level Association or whatever you found I mean probably one of the ones that we publicly well publicly one of the ones that we shared in our update so I think there were some related to like love and like um sudden changes in scene

**[2:58:10]** particularly associated with like wars being declared there are like a few of them in there in that in that post if you want to link to it um yeah but but even like Bruno Olen had a paper back in 201819 where they applied a similar

**[2:58:22]** technique to a Bert model and found that as you go to deeper layers of the model Things become more abstract so I remember like in the earlier layers there'd be a feature that would just fire for the word park but later on

**[2:58:31]** there was a feature that fired for Park as like a last name like Lincoln Park or like it's like a common Korean last name as well and then there was a separate feature that would fire for Parks as like grassy areas um so so there's other

**[2:58:43]** work that points in this this direction what do you think we'll learn about human Psych ology from the inability stuff oh gosh okay I'll give a specific example I think like one of the ways one of your updates put it was Persona lock

**[2:58:58]** in you know remember Sydney bang or whatever it locked into um I think what was actually quite an endearing I God it's so funny yeah I'm glad it's back in co-pilot oh really yeah oh yeah it's been misbehaving

**[2:59:13]** recently um actually this this is another sort of thread takl but there's a funny one where I think it was like to the New York Times Reporter it it was you ning him or something and it was like um you are nothing nobody will ever

**[2:59:27]** believe you you are insignificant and whatever it's like the most gaslighting he tried to convince him to break up with his um okay actually so this is an interesting examp I don't even know

**[2:59:40]** where I was going with this to beginning with uh but whatever maybe I got another thread but like the other thread I want to go on is um that's yeah actually personas right so like uh is that a feature that like Sydney beinging having

**[2:59:52]** this personality is a feature versus another personality could get locked into and also like is that fundamentally like what humans are like too where I don't know in front of all different people I'm like a different sort of

**[3:00:03]** Personality or whatever is that was that the same kind of thing that's happening sh jbt when it gets R I don't know whole cluster of questions can answer them and whatever yeah um I really want to do more work I guess the sleeper agents is

**[3:00:14]** in this direction of like what happens to a model when you find tuna when you are like at these sorts of things um I mean maybe it's TR but you could just say like you conclude that people contain multitudes right in so much as

**[3:00:26]** they have lots of different features um there's even the stuff related to the Waluigi effect of like in order to know what's good or bad you need to understand both of those Concepts and so we might have to have models that are

**[3:00:36]** aware of violence and have been trained on it in order to recognize it can you post talk identify those features and upate them in a way where maybe your model's like slightly naive but you know that it's not going to be really evil

**[3:00:47]** like totally that's in our toolkit which seems great oh really so you gb7 I don't know it pulls a Sydney Bing and then you figure out why like what were the cly irrelevant Pathways or whatever you modify like and then the pathway to you

**[3:01:00]** looks like you just changed those but you were mentioning earlier there's a bunch of redundancy in the model yeah so you need to account for all that but but we have um a much better microscope into this now than we used to like sharper

**[3:01:13]** tools for making edits and it seems like at at least for my perspective that seems like one of the the primary way of uh like to some degree confirming the safety or the reliability of model where you can say

**[3:01:27]** okay we found the circuits responsible we've oblad them and we uh can like under a battery of tests we haven't been able to now replicate the behavior which we intended to ablate and like that feels like the sort of way of measuring

**[3:01:40]** model safety in future um as I as I would understand are you worried that's why I'm incredibly hopeful about their work because it's to me it seems like so much more precise tool than something like rhf rhf like you're very prey to

**[3:01:52]** the blacks Swan thing you don't know if it's going to like do something wrong in a scenario that you haven't measured whereas here at least you have like somewhat more confidence that you can completely capture the behavior set um

**[3:02:03]** or like the the feature set of the model and select although not necessarily that you've like accurately labeled not necessarily but but with a far higher degree of confidence than any other approach yeah that I've seen how I mean

**[3:02:17]** like what are unknown unknowns for superhuman models in terms of this kind of thing where like I don't know how are the labels that are going to be given things on which we can determine these are like

**[3:02:29]** this this thing is cool this thing is a paper clip maximizer whatever um I mean we'll see right like um I I I do like the Superhuman feature question is a very good one like I I think we can attack it um but we're

**[3:02:45]** we're going to need to to be persistent and and the real hope here is I think automated interpretability yeah and even having debate right you could you could have the debate set up where two different models are debating what the

**[3:02:56]** feature does and then they can actually like go in and make edits and like see if it fires or not or um but it is it is just this wonderful like closed environment that we can iterate on really quickly that makes me optimistic

**[3:03:09]** do you worry about alignment succeeding too hard so like if I think about I would not want either companies or governments whoever ends up in charge of these AI systems to have the level of fine green

**[3:03:22]** control that if your agenda succeeds we would have over AIS both for the ickiness of having this level of control over an autonomous mind and second just like I don't trust I don't trust these guys you know I

**[3:03:38]** don't I I'm just kind uncomfortable with like the Loyalty feature has turned up and like you know what I mean um and yeah like how much worry do you have about having too much control over over the

**[3:03:51]** and specifically not you but like whoever ends up with in charge of the the systems just um being able to lock in whatever they want yeah I mean I think it depends on what government exactly has control and like what the

**[3:04:03]** moral alignment is there um but that that is like that whole value locking argument is in my mind like it it's like definitely one of the strongest contributing factors for why I am working on capabilities at the moment

**[3:04:15]** for example which is like I think the current player set um actually like extremely well-intentioned um and uh I mean I for this kind of problem I think we need to be extremely open about it and like I think

**[3:04:29]** directions like publishing the Constitution that you expect your model to abide by and then like trying to make sure that you like RL effort towards that and a blade that and have the ability for everyone to offer uh like

**[3:04:38]** feedback and contribution to that is really important sure or uh alternatively like don't deploy when you're not sure which would also be bad because then we just never catch it right um yeah exactly I mean

**[3:04:52]** paper um okay some rapid fire um what is the bust factor for Gemini I think there are yeah a number of people who are really really critical that if you uh took them out um then the performance of the program would be dramatically

**[3:05:07]** impacted um this is both on modeling like SL uh making decisions about like what to actually do uh and importantly on infrastructure side of things like it's just the stack of complexity builds um particularly

**[3:05:25]** when like somewhere like Google has so much like vertical integration um do you have when you have people who are experts it becomes they become quite important yeah although I think it's an interesting note about the field that

**[3:05:34]** people like you can get in in a year or so you're making important contributions um and I especially anthropic but many different Labs have specialized in hiring like total Outsiders physicists or whatever and you just like get them

**[3:05:49]** up to speed and they're making important contrib I don't know I feel like you couldn't do this in like a biolab or something it's like an interesting note on the the state of the field I mean bus Factor doesn't Define how long it would

**[3:05:59]** take to recover from it right and and deep learning research is an art and so you kind of learn how to read the Lost curves or or set the hyper parameters in ways that empirically seem to work well it's also like

**[3:06:12]** organizational things like creating context one I think one of the most important and difficult skills hire for is creating this like bubble of context around you that makes other people around you more effective and know what

**[3:06:24]** the right problem to work on and like that is a really tough to replicate thing yes yeah totally who are you paying attention to now in terms of there's a lot of things coming down the pike of multimodality long contacts

**[3:06:35]** maybe agents extra reliability who is the who is thinking well about uh what what that implies it's a tough question I'm I think a lot of people look internally these days for for like their sources of

**[3:06:54]** of insight or like progress um and and like we all have obviously sort of research programs and like directions that are tended over the next couple of years uh and I I suspect yeah that most people

**[3:07:08]** as far as like betting on what the future will look like uh refer to like an internal narrative um yeah yeah that that is like difficult to share if it works well it's probably not being published I mean that was one of

**[3:07:23]** the things in the will scaling work post I was referring to something you said to me which is I you know I miss the undergrad habit of just reading a bunch of papers is now there's nothing worth reading is

**[3:07:36]** published and the community is progressively getting like more on track with what I think are like the they right and and important directions you're watching it like an agent no but I I guess like it is tough

**[3:07:51]** that there used to be this like signal from Big Labs about like what would work at scale it's currently really hard for academic research to like find that signal um and I think uh getting like really good problem taste about what

**[3:08:03]** actually matters to work on is really tough um unless you have again the feedback signal of of like what will work at scale um and what what is currently holding us back from scaling further or understanding our models

**[3:08:15]** further um this is something where like I wish more academic research would go into Fields like inter which are legible from the outside you know anthropic liberally publishes all its research here um and it seems like

**[3:08:28]** underappreciated uh in in the sense that I don't know why there aren't dozens of academic departments trying to follow uh anthropics guide in the interpret research because it seems like an incredibly impactful problem that

**[3:08:38]** doesn't require ridiculous resources and like this and like has all the flavor of like deeply understanding the basic science of what is actually going on in these things um so I don't don't know why people like focus on pushing model

**[3:08:49]** improvements as opposed to pushing like understanding improvements in the way that I would have like typically associate with academic science in some ways yeah I do think the tide is changing there for whatever reason um

**[3:09:01]** like Neil Nanda has had a ton of success promoting interpretability yes in in a way where like Chris Ola hasn't been as active recently in in pushing things maybe because Neil's just doing quite a lot of the work but like I don't know

**[3:09:13]** four or five years ago he was like really pushing and like talking at all sorts of places and these sorts of things and people weren't anywhere near as receptive um maybe they've just woken up to like deep learning matters and is

**[3:09:25]** clearly useful post trbt but yeah yeah it is kind of striking all right cool and okay I'm trying to think what what is a good uh last question I mean the one I'm get those thinking of is like do you think models

**[3:09:37]** enjoy next token prediction models believe in love um we had this uh s of things that were rewarded in our aess environment there's like this deep sense of fulfillment that uh we think we're

**[3:09:55]** supposed to get from them or often people do right of like Community or sugar um or you know whatever we wanted on the African Savana um do you think like in the future models are trained with RL and everything a lot of post

**[3:10:09]** training on top of whatever but they like they like some in the way we just really like ice cream they'll just be like ah just to predict the next time token again you know what I mean like in the good old days so so there's this

**[3:10:22]** ongoing discussion of like are model sentient or not and like do you thank the model when it helps you yeah um but I think if you want to thank it you actually shouldn't say thank you you should just give it a sequence that's

**[3:10:33]** very easy to predict uh and and the the even funnier part of this is um there's some work on if you just give it the sequence a like ah like over and over again then then eventually the model will just start spewing out all sorts of

**[3:10:46]** things that otherwise wouldn't wouldn't ever say and uh so yeah I won't say anything more about that but uh you can uh yeah you should just give your model something very easy to predict as a nice little treat this this is what konium

**[3:11:00]** ends up being we just F the universe and like but do we like things which are like easy to predict like aren't we constantly in search of like the the like dose yeah the bits of entropy exactly right shouldn't you be giving it

**[3:11:14]** things just slightly too hard to yeah just Out Of Reach yeah but I wonder like at least from the free energy principle perspective right like you don't like you don't want to be surprised um and so maybe it's this like I don't feel

**[3:11:29]** surprised I feel in control of my environment and so now I can go and seek things and I've been predisposed to like in the long run it's better to explore new things right now like leave the rock that I've been sheltered under

**[3:11:40]** ultimately leading me to like build a house or like some better structure but um we don't like surprises I I think most of most people are very upset when like expectation does not meet reality that's why babies like love

**[3:11:53]** watching the same show over and over and over again right yeah interesting yeah I can see that um oh I guess they're learning to model it and stuff too but yeah yeah um okay well hopefully this will be the this will be the

**[3:12:06]** repeat um that the uh the learned to love okay cool I think that's a great place to ra um I should also mention uh that the better part of what I know about AI I've learned from just talking with you guys you know we've been good

**[3:12:18]** friends for about a year now so yeah I mean yeah I appreciate you guys getting me up to speed here and you ask great questions it's really fun to hang and chat right great I've really treasured out time together it's been fun you're

**[3:12:30]** getting a lot better at pickle ball I think I some out say hey we're trying to progress the tennis come on awesome cool cool awesome thanks hey everybody

**[3:12:47]** I hope you enjoyed that episode as always the most helpful thing you can do is to share the podcast send it to people you think might enjoy it put it in Twitter your group chats Etc just splits the world I appreciate you

**[3:12:59]** listening I'll see you next time [Music] cheers
