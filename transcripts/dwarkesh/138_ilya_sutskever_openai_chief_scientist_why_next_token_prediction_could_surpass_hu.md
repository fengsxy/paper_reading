---
layout: default
type: transcript
series: dwarkesh
episode: 138
guest: ""
title: "Ilya Sutskever (OpenAI Chief Scientist) — Why next-token prediction could surpass human intelligence"
source_url: "https://www.youtube.com/watch?v=Yf1o0TQzry8"
analysis_url: /transcripts/dwarkesh/138_ilya_sutskever_openai_chief_scientist_why_next_token_prediction_could_surpass_hu.analysis/
permalink: /transcripts/dwarkesh/138_ilya_sutskever_openai_chief_scientist_why_next_token_prediction_could_surpass_hu/
---

# Transcript: Ilya Sutskever (OpenAI Chief Scientist) — Why next-token prediction could surpass human intelligence

Source: https://www.youtube.com/watch?v=Yf1o0TQzry8

---

**[00:00]** [Music] but I would not underestimate the difficulty of alignment of models that are actually smarter than us of models that are capable of misrepresenting their intentions are you worried about

**[00:11]** spies I'm really not worried about the weight it's being leaked we'll all be able to become more enlightened because we'd interact with an AGI that will help us see the world more correctly like imagine talking to the best meditation

**[00:23]** teacher in history Microsoft has been a very very good partner for us so I challenge the claim that next token prediction cannot surpass Human Performance if your base neuronet is smart enough you just ask it like what

**[00:36]** would a person is like great insight and visdom and capability do okay today I have the pleasure of interviewing Elia suit who is the co-founder and chief scientist of open AI IIA welcome to the lunar Society

**[00:52]** thank you happy to be here uh first question and no humility allowed there's many scientists or maybe not that many scientists who will make a big breakthrough in their field there's far fewer scientists who will

**[01:03]** make multiple independent breakthroughs that Define their field uh throughout their career what is the difference what like what what distinguishes you from other researchers why have you been able to find multiple breakthroughs in a

**[01:12]** field well thank you for the kind words it's hard to answer that question I mean I try really hard I gave it everything you got

**[01:24]** and that worked so far I think that's all there is to it got it um what's the explanation for why there aren't more illicit uses of GPT why aren't more foreign governments using it to spread propaganda or scam grandmothers or

**[01:40]** something I mean maybe they haven't really gotten to do it a lot but it also wouldn't surprise me if some of it was going on right now certainly I imagine they'd be taking some of the

**[01:52]** open source models and trying use them for that purpose like I sure I would expect this would be something that'd be interested in in the future it's like technically possible they just haven't thought about

**[02:03]** it enough or haven't like done it at scale using their technology or maybe it's happening but you don't know it would you be able to track it if it was happening I think large scale tracking is possible yes I mean this requires a

**[02:15]** all Special Operation that is possible MH um now there's some window in which uh AI is very economically valuable on the scale of airplanes let's say but we haven't reached AGI yet how big is that window I mean I think this window it's

**[02:29]** hard to give you precise answer but it's definitely going to be like a good multi-year window it's also a question of definition because AI before it becomes AGI is going to be increasingly more

**[02:43]** valuable year after year i' say in an exponential way so it's some in some sense it may feel like especially in hindsight it may feel like there was only one year or two years because those two years were larger than the previous

**[02:56]** years but I would say that already last year there've been a fair amount of economic value produced by Ai and next year it's going to be larger and larger after that so I think like that it's going to be a good multi multi-year

**[03:13]** chunk of time but that's going to be true I would say from now to legi pretty much okay well because I'm curious if there's a startup that's using your models right um at some point if you have hii there's only one business in

**[03:25]** the world right it's open AI how how much window do they have do any business have where they're actually producing something that AGI can't produce yeah well I mean it's the same it's the same question is asking how long until AGI

**[03:37]** yeah I think it's a hard question to answer I mean I hesitate to give you a number also because there is the stain whereare effect where people who are optimistic people who are working on the technology tend to underestimate the

**[03:50]** time it takes to get there but I think that the way I ground myself is by thinking about the self-driving car in particular there is an analogy where if you look at the a Tesla and if you look at the self-driving behavior of it it

**[04:03]** like it looks like it does everything it does everything all right but it's also clear that there is still a long way to go in terms of reliability and we might be in a similar place with respect to our models where it also

**[04:16]** looks like we can do everything and at the same time it will be we'll need to do some more work until we really iron out all the issues and make it really good and really reliable and robust and well behaved by 2030 what percent of GDP

**[04:31]** is AI oh gosh hard to answer that question very hard to answer that question give me an over under like the problem is that my AR bars in Lo scale so I could imagine like I could imagine like a huge percentage I

**[04:41]** could imagine a disappointing small percentage at the same time okay so let's take the counterfactual where it is a small percentage let's say it's 2030 and you know not that much economic value has been created by these Elms as

**[04:51]** unlikely as you think this might be what is what would be your best explanation right now why something like this might happen my best explanation so I really don't think that's a likely possibility so that's that's the preface

**[05:05]** to to the comment but if I were to take the premise of your question well like why were things disappointing in terms of the real world impact and my answer would be reliability if somehow it ends up being the case

**[05:21]** that you really want them to be reliable and they ended up not being reliable or if reliability turn out to be harder than we expect I really don't think that will be the case but if I had to pick one if I had to pick one and you tell me

**[05:35]** like hey like why didn't things work out it would be reliability that you still have to look over the answers and double check everything and that just really puts a damper on the economic value that can be produced by those systems they'll

**[05:47]** be technologically mature it's just a question of whether they'll be reliable enough yeah well in some sense not reliable means not technologically mature if you see what I mean yeah fair enough um what's after generative models

**[05:58]** right so before you're working on reinforcement learning is this is this basically it is this a paradigm that gets us to AI or is there something after this I mean I think this Paradigm is going to go really really far and I

**[06:08]** would not underestimate it I think it's quite likely that this exact Paradigm is not going to be the Qui AGI form factor I mean I hesitate to say precisely what the next Paradigm will be but I think it will probably involve

**[06:23]** integration of all the different ideas that came that came in the past is there some specific one you're referring to or I mean it's hard to be specific so you could argue that the next token prediction can only help with match

**[06:37]** Human Performance uh and maybe not surpass it what would it take to surpass Human Performance so I challenge the claim that next token prediction cannot surpass Human Performance it looks like on the surface

**[06:51]** it cannot it looks on the surface if you just learn to imitate to predict what people do it means that you can only copy people but the here is a cter argument for white might not be quite so if your

**[07:05]** neural net is if your base neural net is smart enough you just ask it like what would what would a person with great insight and visent capability do maybe such person doesn't exist but there's a pretty good chance that the neural net

**[07:19]** will be able to extrapolate how such a person should behave do you see what I mean yes although where were to get the sort of insight about what that person would do if not from from the data of regular people because like if you think

**[07:32]** about it what does it mean to predict the next token well enough what does it mean actually it's actually it's a much it's a deeper question than it seems predicting the next token well means that you

**[07:45]** understand the underlying reality that led to the creation of that token it's not statistics like it is statistics but what is statistics in order to to understand the statistics to compress them you need to

**[08:02]** understand what is it about the world that creates this those statistics and so then you say okay well I have all those people what is it about people that creates their behaviors well they have you know they they have thoughts

**[08:13]** and they have feelings and they have ideas and they do things in certain ways all of those would be deduced from next token prediction and I'd argue that this should make it possible not indefinitely but to a to a pretty decent degree to

**[08:29]** say well can you guess what you what You' do if you took a person with like this characteristic and that characteristic like such a person doesn't exist but because you're so good at predicting an nexttoken you should

**[08:40]** still be able to guess what that person would do this hypothetical imaginary person is far greater mental ability than the rest of us um when we're doing reinforcement learning on these models how long before most of the data for the

**[08:54]** reinforcement learning is coming from Ai and not humans I'm mean already most of data for reinforcement learning is coming from AI yeah well it's like the humans are being used to train the reward function but

**[09:09]** then but then the reward function inter in its interaction with the model is automatic and all the data that's generated in the during the process of reinforcement learning it's created by AI so like if you look at the

**[09:22]** current I would say technique Paradigm which is been getting some significant attention because of Chad GPT reinforcement learning from Human feedback so there is human feedback the human feedback is being used to train

**[09:35]** the reward function and then the reward function is being used to create the data which trains them up got it and is there any hope of just removing the human from the loop and have it improve itself and some sort of alpha go away

**[09:46]** yeah definitely I mean I feel like in some sense our hopes for like our plan like very much so the thing you really want is for the human teachers that tell that teach the AI for them to collaborate with an AI you might

**[10:03]** want to think about it and you might want to think of it as being in a world where the human teachers do 1% of the world and the work and the AI do 99% of the work you don't want it to be 100% AI but you do want it to be a human machine

**[10:16]** collaboration which teaches the next machine so currently I mean i' had a chance to play around these models they seem U bad at multi-step reasoning and they have them getting better but what does it take to really surpass that

**[10:27]** barrier I mean I think think dedicated training will get us there more more improvements of the base models will get us there but like fundamentally I also don't feel like they're that bad at multi-step

**[10:41]** reasoning I actually think that they are bad at mental multi-step reasoning but they're not allowed to think out loud but when they are allowed to think out loud they're quite good and I expect this to improve

**[10:52]** significantly both with better models and with special training are you running out of reasoning tokens on the internet are there enough of them I mean you know so okay so for for context on this question like there is there are

**[11:05]** claims that indeed at some point will run out of tokens in general to train those models and yeah I think this will happen one day and we by the time that happens we need to have other ways of training models other ways of

**[11:17]** productively improving their capabilities and sharpening their behavior making sure they're doing exactly precisely what we want without more data well I you haven't run out of data yet there's more yeah I would say I

**[11:30]** would say the data situation is still quite good there's still lots to go but at some point yeah at some point data will run okay where what is the most valuable source of data is it Reddit Twitter books what would you trade many

**[11:43]** other tokens of other varieties for generally speaking you'd like tokens which are speaking about smarter things tokens which are like more interesting yeah so I mean all the all the sources which you mentioned they're valuable

**[11:57]** okay so maybe not Twitter but um uh do we need to go multimodal to get more tokens or do we still have enough text tokens left I mean I think that you can still go very far in text only but going multimodel seems like a very

**[12:08]** fruitful Direction M if you're comfortable talking about this like where is the place where we haven't scraped the tokens yet oh I mean yeah obviously I mean I can't answer that question for us but I'm sure

**[12:19]** I'm sure that for everyone there's a different answer to that question how how many orders of magnitude Improvement can we get just not from scale or not from data but just from algorithmic Improv

**[12:30]** hard to answer but I'm sure there is some is some a lot or is some a little I mean it's only one way to find out okay let me get your like quick fire opinions about these different research directions retrieval Transformers so

**[12:43]** just like somehow storing the data outside of the model itself and retrieving it somehow seems promising but do you see that as a path forward or I I think it seems promising uh robotics was it the right step for open AI to

**[12:56]** leave that behind yeah it was like back then it really wasn't possible to continue working in robotics because there was so little data like back then if you wanted to do an robot if you wanted to work on robotics you needed to

**[13:09]** become a robotics company you needed to really have a giant group of people working on building robots and maintaining them and having and even then like if you only if you're going to have 100 robots it's a

**[13:23]** giant operations already but you're not going to get that much data so in a world where most of the progress comes from the combination of compute and data right that's where we've been where it was the

**[13:36]** combination of compute and data that drove the progress there was no path to data from robotics so back in the day that you made a decision to stop working in robotics there was no path

**[13:50]** forward is there one now so I'd say that now it is possible to create a path forward but one needs to really commit to the to the to the task of Robotics you really need to say I'm going to

**[14:04]** build like many thousands tens of thousands hundreds of thousands of robots and somehow collect data from them and find a gradual path where the robots are doing something slightly more useful and then the data that they get

**[14:17]** from these Rob and then the data that is obtained and used to train the models they do something slightly more useful so you could imagine this kind of gradual path of improvement you build more robots they do more things you

**[14:27]** collect more data and so on but you really need to be committed to this path if you say I want to make robotics happen that's what you need to do I believe that there are companies who are thinking about such doing exactly that

**[14:40]** but I think that you need to really love robots and need to be really willing to solve all the physical and logistical problems of dealing with them it's not the same as software at all so I think one could make progress in robotics

**[14:53]** today with enough motivation uh what ideas are you excited to try but you can't because it don't work well on current Hardware I don't think current Hardware is a limitation okay I think it's just not the case got it so but

**[15:06]** anything you want to try you can just spin it up or I mean of course like this the thing you you might say well I wish current Hardware was cheaper or maybe it had higher like may maybe it would be better

**[15:18]** if it was higher memory processor band we let's say but by and large hard way is just limitation let's talk about alignment do you think we'll ever have a mathematical

**[15:32]** definition of alignment mathematical definition I think is unlikely uhhuh like I do I do think that we will instead have multiple like like rather than rather than achieving one mathematical definition I

**[15:45]** think we'll achieve multiple definitions that look at alignment from different aspects and I think that this is how we will get the assurance that we want and by which I mean you can look at the behavior you can look at the behavior in

**[15:59]** various test um in various adversarial stress situations you can look at how the neural net operates from the inside I think you have to look at all several of these factors at the same

**[16:12]** time and how short do you have to be before you release a model in the while is it 100% 95% well depend how capable the model is the more capable the model is the more the more higher the the more confident to be okay so just say it's

**[16:25]** something that's almost AGI where is Agi well depends what your AGI can do keep in mind AGI is an ambiguous term also like like your average college undergrad is an AGI right it's yeah but you see what I mean

**[16:40]** there's significant bity in terms of what is meant by hii and so depending on where you put this Mark you need to be more or less confident well you mentioned a few of the paths towards alignment earlier what is the one you

**[16:52]** think is most promising at this point like I think that it will be a combination I really think that you will not want to have just one approach I think people want to have a combination of approaches where

**[17:05]** we you spend a lot of compute adversar probit to find any mismatch between the behavior that you wanted to teach and the behavior that it exhibits we look inside into the neural net using another neural to understand how it how it

**[17:19]** operates on the inside I think all of them will be necessary every approach like this reduces the probability of misalignment and you also want to be in a world where you're degree of alignment keeps of

**[17:34]** increasing faster than the capability of the models I would say that right now our understanding of our models is still quite rudimentary we made some progress but much more progress is possible and so I would expect that ultimately the

**[17:48]** thing that will really succeed is when we will have a small neural net that is well understood that's given the task to study the behavior of a large neural that is not understood to verify by what point is most of the research

**[18:01]** being done by AI I mean so today when you use co-pilot right what fraction how how how do you do do the how do you divide it up so I expect at some point you ask your you know descendant of chat GPT you say hey like I'm thinking about

**[18:15]** this and this can you suggest fruitful ideas I should try and you would actually get fruitful ideas right and I think that will make it possible for you to solve problems you could solve before got it but it's

**[18:25]** somehow just telling the humans giving them ideas a faster something it's not itself interacting with the one example I mean you could you could slice it in in a variety of ways but I think the bottl link there is good ideas good

**[18:37]** insights and that's something which the neural net could help with if you could design some like a billion dollar prize for some sort of alignment research results uh or product what is like the concrete Criterion set for that billion

**[18:48]** dollar price there something that makes sense for such a price I it's it's funny that you asked this I was actually thinking about this exact question I haven't I haven't come up with an exact criteria yet maybe something that be the

**[18:59]** benef maybe a prize where we could say that two years later or three year or five years later we'll look back and say like that was the main result so rather than say that there is a priz committee that decides right away

**[19:15]** be wait for five years and then award it retroactively but there's no concrete thing we can identify yet as it like you solve this particular problem and you're you made a lot of progress I think a lot of progress yes I wouldn't say that this

**[19:27]** would be the the full thing MH do you think end to end training is the right architecture for bigger and bigger models or do they do we need better ways of just connecting things together I think end

**[19:40]** to end training is very promising I think connecting things together is very promising everything is promising so open AI is projecting revenues of a billion dollars in 2024 um that might very well be correct but I'm just

**[19:51]** curious when you're talking about a new general purpose technology how do you estimate how big a windfall it will be like have why that particular number I mean you look at the current you look at the you know we we've already had a we

**[20:04]** so we've had a product for quite a while now for back from the gpt3 days from two years ago through the API and we've seen how it grew we've seen how the response to D has grown as well and so you see how the

**[20:17]** response to chat gpts and I think all of this gives us information that allows us to make a relatively sensible extrapolation to 2024 maybe that would be that' be one answer like you need to have data you

**[20:29]** can't come up with those things out of thin air because otherwise your error bars will be like off by your error bars are going to be like 100x in each Direction I mean but most exponentials don't stay exponential uh especially

**[20:42]** when they get into bigger and bigger quantities right so how do you determine in this case that I mean like would you bet against thei uh not after talking with you um let's talk about what like a post AI

**[20:55]** future looks like so are people like you you know I'm guessing you're working like 80 hour weeks towards some this Grand goal that you're really obsessed with are you going to be satisfied in a world where you're basically living in

**[21:04]** an AI retirement home or like what what is a word what is like your what are you concretly doing after AI comes I think the question of what what I'll be doing or what people will be doing after AI come it's a very tricky question you

**[21:18]** know I think where where will people find meaning but I think I think that that's something that AI could help us me like one thing I imagine is that we'll all be able to become more enlightened

**[21:32]** because we' interact with an AGI that will help us see the world more correctly become better on the inside as a result of intera like imagine talking to the best meditation teacher in history I think that will be a helpful

**[21:45]** thing but I also think that because the world will change a lot it will be very hard for people to understand what is happening precisely and how to and how to really contribute one thing that I think

**[21:59]** some people will choose to do is to become part AI in order to really expand their minds and understanding to really be able to solve the hardest problems that Society will face then are you going to become part ofi very tempting

**[22:13]** it is tempting yeah what do you think there'll be physically embodied humans in 3,000 3,000 oh how do I know what's going to happen in 3,000 like what does it look like are there still like humans walking around on Earth or have you guys

**[22:25]** thought concretely about what you actually want this world to look like 3,000 well I mean that that that the thing is here's the thing like let let me describe to you what I think is not quite right about the question like it

**[22:34]** implies like oh like we get to decide how we want the world to look like I don't think that picture is correct I think change is the only constant and so of course even after AGI is built it doesn't mean that the world will be

**[22:48]** static the world will continue to change the world will continue to evolve and it will go through all kinds of Transformations and I really have no I don't think anyone has any idea of how the world will look like in 3000 but I

**[23:03]** do hope that there will be a lot of descendants of human beings who will live happy fulfilled lives where they are free to do as their wish as they see fit or they are the ones who are solving their own problems like one of the

**[23:15]** things which I would not want one one one world which I would find very unexciting is one where you know we bu this powerful tool and then the government said okay so the AGI said that Society should be run in such a way

**[23:27]** and now we should run Society in such away I'd much rather have a world where people are still free to make their own mistakes and suffer their consequences and gradually evolve morally and progress forward on their own through

**[23:41]** their own strength see what I mean with the AGI providing more like a base safety net how much time do you spend thinking about these kinds of things versus just doing the research that I do think about those things a fair bit yeah

**[23:52]** think those are very interesting questions so in what ways have the capabilities we have today in what ways have they surpassed where you expected them to be in 2015 and in what ways are they still not where you would expected

**[24:02]** them to be by this point I mean In fairness did it surpass what I expect them to be in 2015 in in 2015 I my thinking was a lot more I just don't want to bet against deep learning I want to make the biggest possible bet on deep

**[24:16]** learning don't know how but it will figure it out but is there any specific way in which it's uh been more than you expected or less than you expected like some concrete prediction you had in 2015 that's been anounced you know

**[24:30]** unfortunately I don't remember concrete predictions I made in 2015 but I definitely but I definitely think that overall in 2015 I just want to to move to make the biggest bet possible on deep learning

**[24:44]** but I didn't know exactly I didn't have a specific idea of how far things will go in seven years well I mean 2015 I did have all these best with people in 2016 maybe 2017 that things will go really far but

**[24:58]** specifics so it's like it's both it's both the case that it surprised me and I was making these aggressive predictions but I think maybe I believe them only only only 50% on the inside uhhuh well what do you believe now that even most

**[25:11]** people at open a would find farfetched I mean I think that at this because we communicate a lot of open AI people have a pretty good sense of what I think and so yeah we we reached the point at open air I think we see I to ey

**[25:24]** on all these questions so Google has you know it's custom TPU Hardware it has all this data from all its users you know Gmail what um and so on does it give it an advantage in terms of training bigger models and better models than you so I

**[25:37]** think like when first at first when the TPU came out I was really impressed and I thought wow this is amazing but that's because I didn't quite understand harder back then what really turned out to be the case is that tpus and gpus are

**[25:50]** almost the same thing they are very very similar it's like I think a GPU chip is a little bit bigger I think a TPU chip is a little bit smaller it may be a little bit cheaper but then they make more gpus than tpus so I think the the

**[26:05]** gpus might be cheaper after all but fundamentally you have a big processor and you have a lot of memory and there is a bottl link between those two and the problem that both the TPU and the GPU are trying to solve is that

**[26:19]** by the the amount of time it takes you to move one floating point from the memory to the processor you can do several 100 floating Point operations on the processor which means that you have to do some kind of batch processing and

**[26:31]** in this sense both of these architectures are the same so I I really feel like Hardware like in some sense the only thing that matters about Hardware is cost cost per flop overall systems cost okay there

**[26:43]** that there isn't much that much difference well actually don't know I mean I don't know how much what what what the TPU costs are but I would suspect that probably not if anything probably use are more expensive because

**[26:55]** there is less of them when you're doing your work how much of the time is spent when you know configuring the right initializations making sure the training run goes well and getting the right hyper parameters and how much is it just

**[27:05]** coming up with whole new ideas I would say it's a combination but I think that coming up with It's a combination but coming up with whole new ideas is actually not it's it's like a Modest part of the work certainly coming up

**[27:17]** with new ideas is important but I think even more important is to understand the results to understand the existing ideas to understand what's going on because normally you have these you know neur is a very complic get a system right and

**[27:29]** you ran it and you get some Behavior which is hard to understand what's going understanding the results figuring out what next next experiment to run a lot of the time is spent on that understanding what could be wrong what

**[27:42]** could have caused the the neural net produce a result which was not expected i' say a lot of time we spend as well of course coming up with new ideas but not new ideas I think like I don't I don't like this this um framing as much it's

**[27:58]** not that it's false but I think the main activity is actually understanding how what do you see is the difference between the two so at least in my mind when you say come up with new ideas I'm like oh like what happened if

**[28:09]** it did such and such whereas understanding it's more like like what is this whole thing like what are the real underlying phenomena that are going on what are the what are the underlying

**[28:20]** effects like why why are we doing things this way not another way and of course this is very adjacent to what can be described as coming up with ideas but I think the understanding part is where the real action takes place does that

**[28:33]** describe your entire career like if you think back on like image net or something was that more a new idea or was that more understanding oh I was definitely understanding definitely understanding it was a new understanding

**[28:42]** of very old things what is the experience of training on Azure been like using Azure fantastic I mean yeah I mean Microsoft has been a very very good partner for us and they've really helped

**[28:58]** take Azure and make it bring it to a point where it's really good for ML and they're super happy with it how um how vulnerable is the whole AI ecosystem do something that might happen in Taiwan so let's say there's like a

**[29:11]** tsunami uh in Taiwan or something what would what happens to AI in general like it's it's definitely going to be a significant setback uhuh it's not going to like it might be something equivalent to like no one will be able to get more

**[29:25]** more computes for a few years but I expect comput will spring up like for example I believe that Intel has Fabs just of the previous of like a few Generations ago so that means that if intel wanted to they could produce

**[29:36]** something GPU like from like four years ago so yeah it's not the best let's say I'm actually not sure about if if if my statement about Intel is correct but I do know that there are Fabs outside of Taiwan they're just not

**[29:50]** as good but you can still use them and still go very far with them it's just it just cost it's just a setback well iner get cost prohibitive as these models get bigger and bigger so I have a different way of looking at this question yeah

**[30:03]** it's not that inference will become cost prohibitive mhm inference of better models will indeed become more expensive but is it prohibitive well it depends on how useful is it like if it is more useful

**[30:17]** then it is expensive then it is not prohibited like to give you an analogy like suppose you want to talk to a lawyer you have some case you or need some advice or something you are perfectly happy to spend $500 an hour

**[30:29]** right so if your neural net could give you like really reliable legal advice you'd say I'm happy to spend $400 for that advice and suddenly inference becomes very much non prohibited MH the question is is can can neuronet produce

**[30:44]** an answer good enough at this cost yes and you'll just have like price discrimination different different models different I mean it's already the case today so on our product the API we Ser of multiple neural Nets of different

**[31:02]** sizes and different customers use different neural Nets of different sizes depending on their use case like if someone can take a small model and fine tune it and get something that's satisfactory for them they'll use that

**[31:13]** yeah but if someone wants to do something more complicated and more interesting they'll use the biggest model how do you prevent these models from just becoming Commodities where these different companies just uh they

**[31:22]** just spit each other's prices down until it's basically the cost of the GPU run yeah I think I think there is without question a force that's trying to create that and the answer is you got to keep on making progress you got to keep

**[31:31]** improving the models you got to keep on coming up with new ideas and making our models better and more reliable more trustworthy so you can trust their answers all those things yeah but let's

**[31:43]** say it's like 2025 and the model from 2024 somebody just offering it at Cost and it's like still pretty good why why would people use a new one from 2025 if the one from just a year older is you know even better so there are several

**[31:57]** answers there for some use cases that may be true there will be a new model from 2025 which will be driving the more interesting use cases there's also going to be a question of inference cost like you can you can do research to serve the

**[32:08]** same model at less cost so they will be different the same model will be served will cost different different amounts to serve for different companies I can also imagine some degree of specialization too where some companies may try to

**[32:23]** specialize in some area and be stronger in an errow area compared to other companies and I think that to May that may be a response to commoditization to some degree uh as over time do these different companies do their research

**[32:37]** directions converge or they diverge are they doing similar and similar things over time or are they doing are they going off branching off into different areas so I'd say in the near term it looks like there is Convergence in the

**[32:46]** like I expect this going to be a convergence a Divergence convergence Behavior where there is a lot of convergence on the near term work there's going to be some Divergence on the longer term

**[32:58]** but then once the longer term work starts to fruit I think there will be conversions again got it one when one of them finds the most promising area they everybody just that's right now there is obviously less less publishing now so it

**[33:10]** will take longer before this promising Direction gets rediscovered but that's how i' imagine it I think it's going to be convergence Divergence convergence yeah we talked about this a little bit at the beginning but you know as foreign

**[33:21]** governments learn about how capable these models are how do you are you worried about spies or some sort of attack to get your weights or you know somehow abuse these models and learn about them yeah it's definitely

**[33:36]** something that you absolutely can't discount that yeah and yeah something that we right guard against the best of our ability but it's going to be a problem for everyone who's building this how do you prevent your weights from

**[33:49]** leaking what I mean you have like really good security people and like how many people have the if they wanted to just like stage into the weights how machine how many people could do that I

**[34:01]** mean like what I can say is that the security people have we have they built they've done a really good job so that I'm really not worried about the ways being leaked okay got it what kinds of emerging properties are expecting from

**[34:14]** these models at this scale is there something that just comes about denovo I'm sure things will come I'm sure really new surprising properties will come up I would not be surprised

**[34:24]** the thing which I'm really excited about or the thing which I'd like to see is reliability ility and controllability I think that this will be very very important class of emergent properties if you have reliability and

**[34:34]** controllability I think that helps you solve a lot of problems reliability means you can trust the models output controllability means you can control it and we'll see but it'll be very cool if those emerging properties did exist

**[34:47]** is there somewh you can PR it at Advance like what will happen in this parameter account what will happen that I think it's possible to make some predictions about specific specific capabilities though it's definitely not simple and

**[34:58]** you can't do it in a super fine grain way at least today but I think getting better at that is really important and anyone who is interested and who has re research ideas on how to do that I think that can be a valuable

**[35:11]** contribution how seriously do you take the scaling laws if like there's a paper that says like oh you just increase you need this many orders of magnitude more to get all the reasoning out like do do you take that seriously or do you think

**[35:21]** it breaks down at some point well the thing is that the scaling law tells you what happens as you what happens to your Lo to your next word prediction accuracy right there is a whole separate challenge of linking next word

**[35:35]** prediction accuracy to reasoning capability I do believe that indeed there is a link but this link is compli and we may find that there are other things that can give us more reasoning pre-unit

**[35:51]** effort like for example some special like you know you mentioned reasoning tokens and I think they can be helpful there can be there can be probably some things that you can is this is something you're

**[36:05]** considering just hiring humans to generate tokens for you or is it all going to come from stuff that already exists out there I mean I think that relying on people to teach our models to do things especially you know to make

**[36:17]** sure that they are well behaved and they don't produce false things I think is an extremely sensible thing to do and isn't it odd that we have the data we need at exactly the same time as we have the Transformer at the exact same time that

**[36:29]** we have these gpus like is it OD to you that all these things happen at the same time or do you not see that way I mean it it is definitely an interesting it is an interesting situation that is the case I will say that it is odd and it is

**[36:44]** less odd on some level here is why it's less odd so what is the driving force behind the fact that the data exists that the gpus exists that the Transformer exists so as the data EX this because computers

**[36:58]** became better and cheaper we've got smaller and smaller transistors and suddenly at some point it became economical for every person to have a personal computer once everyone has a personal computer you really want to

**[37:07]** connect to me the network you get the internet once you have the internet you have suddenly data appearing in great quanties the gpus were improving concurrently because you have smaller and smaller transistors and you're

**[37:18]** looking for things to do with them gaming turned out to be thing that you could do and then at some point the gaming GPU Nvidia said wait a second TR and may turn it into a general purpose GPU computer maybe someone will find you

**[37:34]** find it useful turns out it's good for neural NS so it could it could have been the case that maybe the GPU would have arrived 5 years later or 10 years later if let's suppose gaming wasn't a thing it's kind of hard to imagine what does

**[37:49]** it mean if gaming isn't a thing but it could maybe there was a counterfactual world where gpus arrived 5 years after the data or 5 years before the data in which case maybe things would move a little bit more things

**[38:02]** would have been as ready to go as there now but that's the picture which I imagine all this progress in all these Dimensions is very intertwined it's not a coincidence that like you don't get to pick and

**[38:16]** choose which dimension in which Dimensions things improve if you see what I mean how inevitable is this kind of progress so if like let's say you and Jeffrey hon and a few other Pioneers if they were never born does the Deep

**[38:28]** learning Revolution happen around the same time how much does it delay I think maybe there would have been some delay maybe like a year delay it's really hard tell it's really hard to tell I mean I I hesitate to give a lot a a longer answer

**[38:40]** because okay well then you'd have gpus would keep on improving right then at some point I can I cannot see how someone would not have discovered it because here's the other thing the if if Okay so

**[38:51]** let's suppose no one has done it computers keep getting faster and better becomes easier and easy to train these neural Nets because you have bigger gpus so it takes less engineering effort to train one you

**[39:02]** don't need to optimize your code as much you know when the when the image data set came out it was huge and it was very very difficult to use now imagine you wait for a few years and it becomes very easy to download and people can just

**[39:13]** just Tinker so I I would imagine that like a modest number of years maximum this would be my guess I hesitate I hesitate to to give to give a lot a longer answer though you know you can't you can't

**[39:28]** run you can't rerun the world you don't know with let's go back to align for a second as somebody who deeply understands these models what is your intuition of how hard alignment will be like I think with the so here's what I

**[39:39]** would say I think with the current level of capabilities I think we have a pretty good set of ideas of how to align them but I would not underestimate the difficulty of alignment of models that are actually smarter than us of models

**[39:52]** that are capable of misrepresenting their intentions like I think I think it's something to to think to think about a lot and to research I think this is one area also

**[40:02]** by the way you know like often times academic researchers asked me ask me where what what's the best place where they can contribute and I think alignment research is one place where I think academic researchers can make very

**[40:14]** meaningful contributions other than that do you think Academia will come up with important insights about actual capabilities or is that going to be just the companies at this point so the companies will realize the capabilities

**[40:23]** I think it's very possible for academic research to come up with those insights I think I think it's just it doesn't seem to happen that much for some reason but I don't I don't think there's anything fundamental about Academia like

**[40:37]** it's not like Academia can't I think maybe they're just not thinking about the right problems or something because maybe it's just easier to see what needs to be done inside these companies I see but there's a

**[40:49]** possibility that somebody could just realize yeah I totally like why why would I possibly rule this out you see what I mean what are the concrete steps by which um these language models start actually impacting the world of atoms

**[41:02]** and not just the world of vids well you see I don't think that there is a distinction clean distinction between the world of bits and the world of atoms suppose the neuronet tells you that hey like here is like something that you

**[41:14]** should do and it's going to improve your life but you need to like rearrange your apartment in a certain way then you go and you rearrange your apartment as a result did the neuronet impact the world of atoms just yeah fair enough fair

**[41:27]** enough do you think it'll take a couple of additional breakthroughs as important as a Transformer to get to superum AI or do you think we basically got the insights in the books somewhere and we just need

**[41:37]** to implement them and connect them so I don't really see such a big distinction between those two cases and let me explain why like I think what's what one of the ways in which progress has taken place in the

**[41:50]** past is that we've understood that something had a property a desirable property all along but you didn't realize so is that a breakthrough you can say yes it is is it an

**[42:04]** implementation of something on the books also yes so I I my my feeling is that a few of those are quite likely to happen but that in hindsight it will not feel like a breakthrough everybody is going to say oh well of course like it's

**[42:17]** totally obvious that such and such thing can can work you see with a Transformer the reason it's being brought up as a big as a specific Advance is because it's the kind of thing that was not obvious for almost anyone so people can

**[42:29]** say yeah like it's not something which they knew about but if an advance comes from something like let's consider the the the most fundamental advance of deep learning that a big neural network trained with back propagation can do a

**[42:40]** lot of things like where's the novelty it's not in the neural network it's not in the back propagation but then somehow it's the kind of but it was it is most definitely a giant conceptual breakthrough because

**[42:53]** for the longest time people just didn't see that but then now everyone sees it everyone's going to say well of course like it's totally obvious big neural everyone knows that they can do it what is your opinion of your former Advisor

**[43:04]** New forward forward algorithm I think that it's an attempt to brain a neural network without back propagation and I think that this is especially interesting if you are motivated to try to understand how the

**[43:20]** brain might be learning its connections the reason for that is that as far as I know neuroscientists are really convinced that the brain cannot Implement back propagation because the signals in the synaps is only moving One

**[43:35]** Direction and so if you have a neuroscience motivation and you want to say okay how can I come up with something that tries to approximate approximate the good properties of back

**[43:50]** propagation without doing back propagation that's what the forward forward algorithm is trying to do but if you are trying to just engineer a good system there is no reason to not use back propagation

**[44:01]** like it's it's it's the only algorithm really I guess I've heard you in different context talk about the need like using humans as the you know the existing example case that a you know AGI exists right so at what point do you

**[44:17]** take the metaphor less seriously and feel don't feel the need to pursue it in terms of research because it is important to you as a sort of existence case like at what point do I stop caring caring about humans as an existence case

**[44:28]** of intelligence or as the sort of as a example of the model you want to follow in terms of pursuing intelligence in models I see I mean like you got to I think it's good to be inspired by humans I think it's good to be inspired by the

**[44:43]** brain I think there is an art into being inspired by humans in the brain correctly because it's very easy to latch on to an nonessential quality of humans or of the brain and I think many people whoin who many people whose

**[44:57]** research is trying to be inspired by humans and by the brain often gets a little bit specific people get a little bit to okay so like what cognitive science model should be follow at the same time consider the idea of the

**[45:08]** neural network itself the idea of the artificial neuron this too is inspired by the brain but it turned out to be extremely fruitful so how do you do this you what what behaviors of human beings are essential that you say like this is

**[45:22]** something that proves to us that it's possible what is in essential no actually this is like some emerg phenomena of something more basic and we just need to focus on our on our on do getting our own Basics right I

**[45:36]** would say I would say that it's like I think one should one can and should be inspired by human intelligence with care final question why is there in your case such a strong correlation between being first to the Deep learning

**[45:54]** Revolution and still being one of the top researchers you would think that the two things wouldn't be that correlated but why is that that correlation I don't think those things are super correlated indeed I feel like in my

**[46:04]** case I mean honestly it's hard to answer the question you know I just kept on kept I kept trying really hard and it turned out to have sufficed thus far got it so it's a perseverance I think it's a necessary but not a sufficient condition

**[46:19]** like you know many things need to come together in order to really figure something out mm like you need to really go for it and also need to have the right way of looking at things and it's hard it's

**[46:32]** hard to give him like a really meaningful answer to this question all right um Ilia it is been a true pleasure thank you so much for coming out ler Society I appreciate you bringing us to the offices thank you yeah I really

**[46:43]** enjoyed it thank you very much hey everybody I hope you enjoyed that episode just wanted to let you know that in order to help pay for the bills associated with this podcast I'm turning on paid subscriptions on my substack at

**[46:59]** warc patel.com no important content on this podcast will ever be paywalled so please don't donate if you have to think twice before buying a cup of coffee but if you have the means and you've enjoyed this podcast or gotten some kind of

**[47:14]** value out of it I would really appreciate your support as always the most helpful thing you can do is to share the podcast send it to people you think might enjoy it put it in Twitter your group chats Etc just splits the

**[47:26]** world appreciate you listening I'll see you next time cheers [Music]
