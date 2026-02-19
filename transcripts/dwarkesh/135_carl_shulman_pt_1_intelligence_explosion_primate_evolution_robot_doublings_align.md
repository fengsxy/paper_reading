---
layout: default
type: transcript
series: dwarkesh
episode: 135
guest: ""
title: "Carl Shulman (Pt 1) — Intelligence explosion, primate evolution, robot doublings, & alignment"
source_url: "https://www.youtube.com/watch?v=_kRg-ZP1vQc"
analysis_url: /transcripts/dwarkesh/135_carl_shulman_pt_1_intelligence_explosion_primate_evolution_robot_doublings_align.analysis/
permalink: /transcripts/dwarkesh/135_carl_shulman_pt_1_intelligence_explosion_primate_evolution_robot_doublings_align/
---

# Transcript: Carl Shulman (Pt 1) — Intelligence explosion, primate evolution, robot doublings, & alignment

Source: https://www.youtube.com/watch?v=_kRg-ZP1vQc

---

**[00:00]** human level AI is deep deep into an intelligence explosion things like inventing the Transformer or discovering chinchilla scalene and doing your training runs more optimally or creating flash attention that set of inputs

**[00:14]** probably would yield the kind of AI capabilities needed for intelligence explosion if you have a race between on the one hand the project of getting strong interpretability and shaping motivations and on the other hand these

**[00:28]** AIS in ways that you don't perceive make the AI takeover happen we spend more compute by having a larger brain than other animals and then we have a longer childhood it's analogous to like having a bigger model and having more training

**[00:42]** time with it it seemed very implausible that we couldn't do better than completely Brute Force Evolution how quickly are we running through those orders of magnitude okay today I have the pleasure of speaking with Carl

**[00:53]** Schulman many of my former guests and this is not an exaggeration many of my former guests have told me that a lot of their biggest ideas perhaps most of their biggest ideas have come directly from Carl

**[01:04]** especially when it has to do with the intelligence explosion and its impacts and so I decided to go directly to the source and we have Carl today on the podcast Carl keeps a super low profile but he is one of the most interesting

**[01:17]** intellectuals I've ever encountered and this is actually his second podcast ever so we're gonna get to get deep into the heart of many of the most important ideas that are circulating right now uh directly from the source so and by the

**[01:29]** way so Carl is also an advisor to the open philanthropy project which is one of the biggest funders on causes having to do with AI and its risks not to mention Global health and well-being and he is a research associate at the future

**[01:41]** of humanity Institute at Oxford so Carl it's a huge pleasure to have you on the podcast thanks for coming thank you to Rakesh I've enjoyed seeing some of your episodes recently and I'm glad to be on the show excellent let's talk about AI

**[01:55]** before we get into the details give me the sort of big picture explanation of the uh feedback loops and just a General Dynamics that would start when you have something that is approaching human level intelligence

**[02:10]** yeah so I think the the way to think about it is we have a process now where humans are developing new computer chips new software running larger training runs and

**[02:26]** it takes a lot of work to keep Moore's Law chugging while it was it's slowing down now and it takes a lot of work to develop things like Transformers do develop a lot of the improvements to

**[02:40]** Ai and neural networks that are advancing things and the core method that I think I want to highlight on this podcast and I think is underappreciated is the idea of input output curves

**[02:55]** so we can we can look at the increasing difficulty of improving chips and so sure each time you double the performance of computers it's harder and as we approach

**[03:08]** physical limits eventually it becomes impossible but how much harder so there's a paper called or ideas getting harder to find it was published a few years ago something like 10 years

**[03:22]** ago at Murray we did I mean I I did an early version of this uh of this analysis using mainly data from Intel and like the large semiconductor Fabricators anyway and so in in this paper they cover a period where

**[03:41]** the productivity of computing went up a million fold so you could get a million times the Computing operations per second per dollar big change but it got harder so the the amount of investment the labor force uh required

**[03:58]** to make those continuing advancements went up and up and up uh indeed it went up 18-fold over that period I know so some take this to say oh diminishing returns things are just getting harder and

**[04:12]** harder and so that will be the end of progress eventually however in a world where AI is doing the work that doubling of computing performance translates pretty directly to a doubling

**[04:28]** or better of the effective labor Supply that is if when we had that million fold compute increase we used it to run artificial intelligences who would replace human scientists and engineers

**[04:46]** than a the 18x increase in the labor demands of the industry would be trivial we're getting more than one doubling of the effective labor Supply that we need for each doubling of the labor requirement and in that

**[05:04]** data set it's like over four so we double we double compute okay now we need somewhat more researchers but a lot less than twice as many and so okay we we use up some of those doublins of compute on the

**[05:20]** increasing difficulty of further research but most of them are left to expedite the process so if you you double your labor force yeah that's enough to get several doublings of

**[05:34]** compute you use you use up one of them on meeting the increased demands from diminishing returns the others can be used to accelerate the process so you have your first doubling takes however many months your next

**[05:49]** doubling can take a smaller fraction of that the next step Lane less and so on at least insofar as this the outputs you're generating compute for AI in the story are able to serve

**[06:06]** the function of the necessary inputs if there are other inputs that you need eventually those become a bottleneck and you wind up more restricted on this got it okay so yeah I think the bloom paper had that 30 there was 35 increase in was

**[06:21]** it translated into your cost per flop and there was a seven percent increase per year in the number of researchers required to sustain that pace so something like this yeah it's like four four to five uh dublins of compute per

**[06:36]** doubling of Labor inputs I guess there's a lot of questions you can delve into in terms of whether you would expect a similar scale with AI and whether it makes sense to think of AIS as a population of researchers that keeps

**[06:49]** growing with compute itself actually let's go there so can you explain the intuition that compute is a good proxy for the number of AI researchers so to speak uh so far I've talked about Hardware as an initial example because

**[07:02]** we had good data about a past period uh you can also make it improvements on the software side and we think about intelligence explosion that can include ai's doing work on making Hardware better making better software making

**[07:18]** more Hardware um but the basic idea for the hardware is is especially simple in that if you have a worker an AI worker that can substitute for a human if you have twice as many computers you can run two

**[07:34]** separate instances of them and then they can do two different jobs manage uh two different machines work on two different design problems now you can get more gains than just what you would get by having two instances we get improvements

**[07:53]** from using some of our compute not just to run more instances of the existing AI but to train larger AIS so there's Hardware technology how much you can get per dollar you spend on hardware and there's software technology and the

**[08:08]** software can be copied freely so if you've if you've got the software it doesn't necessarily make that much to say that oh we've got you know 100 Microsoft Windows uh you can make as many copies as you need other than

**[08:21]** for whatever Microsoft will charge you but for Hardware is different it matters how much we actually spend on the hardware at a given price and if we look at the changes that have been driving AI recently that is the thing

**[08:38]** that is really off Trend we are spending tremendously more money on computer hardware for training big AI models yep okay so there's there's the investment in Hardware there's a hardware technology itself and there's

**[08:55]** the software progress itself the AI is getting better because we're spending more money on it because our Hardware itself is getting better over time and because we're like developing better models or better adjustments to those

**[09:05]** models where is a loop here the work involved in designing new hardware and software is being done by people now they use computer tools to assist them but like computer time is not like the primary cost

**[09:23]** um for NVIDIA designing chips um for gsmc producing them for asml making lithography equipment to serve the tsmc Fabs and even in AI software research that has become quite compute intensive but I think we're still in the

**[09:44]** range where you know at a place like deepmind salaries were still larger than compute for the experiments although they're tremendously tremendously more of the expenditures or on compute relative to salaries than in the past

**[10:00]** if you take all the work that's being done by those humans there's like low tens of thousands of people working at Nvidia designing gpus specialized for AI I think there's more like 70 000 people at tsmc which is the leading producer of

**[10:20]** Cutting Edge chips there's a lot of additional people at companies like asml that Supply them with the tools they need and then a company like deepmind I think from their public filings I recently had a thousand people opening I

**[10:37]** think is a few hundred people anthropic is less if you add up things like Facebook AI research Google brain all right or indeed you've got thousands or tens of thousands of people who are working on

**[10:52]** AI research we'd want to zoom in on those who are developing new methods rather than narrow applications so inventing the Transformer definitely counts optimizing for some particular businesses data set cleaning probably

**[11:06]** not yeah um but so those people are doing this work they're driving quite a lot of progress what we observe and the the growth of people

**[11:16]** relative to the growth of those capabilities uh that pretty consistently the capabilities are doubling on a shorter time scale than the people required to do them are doubling and so there's work

**[11:30]** so we talked about hardware and how historically it was pretty dramatic like uh four or five doublings of compute efficiency for doubling of of human inputs I think that's a bit lower now as we get towards the end of Moore's Law

**[11:45]** although interestingly not as much lower as you might think because the growth of inputs has also slowed recently on the software side there's some work by Tame vasaruglu and I think collaborators

**[12:00]** um the uh may have been his thesis uh it's called our models getting harder to find and so it's applying the same sort of analysis as the our ideas getting harder to find and you can look at growth rates of

**[12:16]** papers from citations employment at these companies and it seems like the doubling time of these like workers driving the software advances uh is like several years um or at least a couple years whereas

**[12:31]** the doubling of effective compute from algorithmic progress is faster so there's a group called Epoch they received grants from open philanthropy and they do work collecting data sets that are relevant to forecasting AI

**[12:47]** progress and so their headline results for what's the rate of progress in hardware and software um and just like growth in budgets are as follows

**[13:00]** so for Hardware they're looking at like a doubling of Hardware efficiency that's like two years it's possible it's a bit better than that when you take into account certain specializations for AI workloads for the growth of budgets

**[13:13]** they find a doubling time that's like something like six months in recent years which is pretty tremendous relative to the historical rates we should maybe get into that later and then on the algorithmic progress

**[13:28]** side mainly using using imagenet type data sets right now they find a doubling time that's less than one year and so you you combine all of these things uh and the like the growth of effective compute for training big big AIS uh it's

**[13:45]** it's pretty pretty drastic I think I saw an estimate that gpd4 cost like 50 million dollars around that range to train now suppose that like AGI takes a thousand X that um if you were just a scale up jpd4

**[13:58]** um it might not be that I'm just just for the same example some so part of that will come from companies you're spending a lot more to train the models and that just greater investment part of that will come from them having better

**[14:09]** models so that what would have taken a 10x increase in the model to get naively you can do with having a better model that you only need to do scale up you you get the same effect of increasing it by 10x just from having a better model

**[14:22]** and so yeah you can spend more money on it to turn in a bigger model you can just have a better model or you can have chips that are cheaper to trade in so you get more compute for the same dollars and okay so those are the three

**[14:35]** you're describing the the ways in which the quote-unquote effect of a compute would increase from the looking at it right now it looks like yeah you might get two or three doublings of effective compute for this thing that we're call

**[14:47]** all in software progress which is which people get by asking well how much less compute can you use now to achieve the same Benchmark as you achieved before there are reasons to not fully identify this with like software

**[15:01]** progress as you might naively think of it because some of it can be enabled by the other so like when you have a lot of compute you can do more experiments and find algorithms that work better sometimes the the additional compute you

**[15:17]** can get higher efficiency by running a bigger model we were talking about earlier and so that means you're getting more for each GPU that you have because you made this like larger expenditure and you could that can look like a

**[15:31]** software Improvement because this model it's not it's not a hardware Improvement directly because it's doing more with the same Hardware but you wouldn't have been able to achieve it without having a ton of gpus to do the big training run

**[15:44]** the the feedback loop itself involves the AI that is resolved of this greater effective compute helping you train better AI right or use uh less effective compute in the future to train better AI it can help on the hardware design yeah

**[16:00]** so like Nvidia is a fabulous chip design company they don't make their own chips they send files of instructions to tsmc which then fabricates the chips uh in their own facilities uh and so the work of those uh you know

**[16:18]** 10 000 plus people if you could automate that and have the equivalent of a million people doing that work then I think you would pretty quickly um get the kind of improvements that can be achieved with the existing uh nodes

**[16:34]** uh that tsmc has operating on you could get a lot of those chip design gains basically like doing the job of improving chip design that those people are working on now but get it done faster

**[16:46]** so that's one thing I think that's less important for the intelligence explosion um the reason being that when you make an improvement to chip design it only applies to the chips you make after that if you make an improvement in AI

**[17:01]** software it has the potential to be immediately applied to all of the gpus that you already have yeah and so the thing that I think is most disruptive and most important has

**[17:13]** the Leading Edge of the change from AI automation of the inputs to AI is on the software side where at what point would it get to the point where the AIS are helping develop better software or better models or future AIS some people

**[17:29]** claim today for example that you know programmers at openai are using copilot to write programs now so in some sense you're already having that sort of feedback loop that I'm a little skeptical of that as a mechanism at what

**[17:43]** point would it be the case that the AI is contributing significantly in the sense that it would almost be the equivalent of having additional researchers to AI progress and software the quantitative magnitude of the health

**[17:55]** is absolutely Central so there are plenty of companies that like make some product that like very slightly boost productivity so when Xerox makes fax machines it maybe increases people's product activity in office work by 0.1

**[18:11]** percent or something you're not going to have explosive growth out of that because okay now point one percent more uh you know effective r d uh at Xerox and any customers buying the machines not not that important so I think the

**[18:28]** the thing the thing to look for uh is when is it the case that the the contributions from AI are starting to uh become as large or larger as the contributions uh from humans so like uh

**[18:45]** when this is boosting their effective productivity by 50 or 100 percent and you like if you then go from you know eight-month doubling time say for Effective compute from software

**[18:57]** Innovation things like inventing the Transformer or discovering chinchilla scalene and doing your training runs more optimally or creating flash attention yeah if you move that from say eight

**[19:08]** months to four months and then the next time you apply that it significantly increases the Boost you're getting uh from the ass I mean maybe instead of giving a 50 or 100 productivity boost that's more like a 200 percent yeah

**[19:22]** um and so it doesn't have to have been able to automate everything involved in the process of AI research it can be it's automated a bunch of things and then those are being done in extreme profusion because any I think a thing

**[19:38]** that AI can do you have it done much more often because it's so cheap uh and so it's not a threshold of this is human level AI it can do everything a human can do with no weaknesses in any area it's that even with its weaknesses

**[19:55]** it's able to bump up the performance so that instead instead of getting like the results we would have with the 10 000 people working on finding these Innovations we get the results that we would have if we had

**[20:08]** twice as many of those people with the same kind of skill distribution and so that's a it's like a demanding challenge it's like uh you need quite a quite a lot of capability for that but it's also important that it's

**[20:20]** significantly less than this is a system where there's no way you can point at it and say in any respect it is weaker than a human a system that was just as good as a human in every respect but also had all the advantages of an AI

**[20:35]** that is just Way Beyond this point like if you consider that there's like the the output of our existing Fabs can make tens of millions of advanced gpus per year those gpus if they were running sort of AI software that was as

**[20:53]** efficient as humans as a sample efficient it doesn't have any major weaknesses so they can work four times as long uh you know the 168 hour work week they can have much more education than any

**[21:07]** human so it's you know a human you know you got a PhD you know it's like yeah wow it's like 20 years of education uh maybe longer if they they take if they take it slow uh slow route on the PHD

**[21:21]** um it's just normal for us to train large models by eat the internet eat all the published books ever um read everything on GitHub and get good at predicting it um so like the level of Education vastly

**[21:38]** Beyond any human the degree to which the models are focused on task is higher than all but like the most motivated humans when they're really really gunning for it uh so you combine the things tens of

**[21:52]** millions of gpus each GPU is doing the work of the very best humans in the world and like the most capable humans in the world uh can command salaries that are a lot higher than the average and particular

**[22:06]** in a field like stem or narrowly AI like there's no human in the world who has a thousand years of experience with tensorflow or let alone the new AI technology that were invented the year the year before but if if they

**[22:22]** were around uh yeah they'd be paid millions of dollars a year uh and so we consider this okay tens of millions of gpus each is doing the work of maybe 40 maybe more of these kind of existing

**[22:39]** workers this is like going from a Workforce of tens of thousands to hundreds of Millions you immediately make all kinds of discoveries then you immediately develop all sorts of tremendous Technologies so

**[22:53]** human level AI is deep deep into an intelligence explosion the intelligence explosion has to start with something weaker than that yeah what is the thing it starts with and how close are we to that because if

**[23:08]** you think of a researcher at open AI or something you know these are to be a researcher is not just completing the hello world uh prompt that co-pilot does right it's like you gotta choose a new idea you have to

**[23:20]** figure out the right way to approach it you perhaps have to manage the people who are also working with you on that problem you know it's like it's incredibly complicated skill portfolio skills rather than just a single skill

**[23:31]** so yeah what is the point I wish that feedback loop starts where you can even you're not just doing the 0.5 increase in productivity that a sort of AI tool might do but is actually the equivalent of a researcher or close to it like what

**[23:46]** is that point so I think maybe a way uh look at it is to give some illustrative examples of like the kinds of capabilities that you might see and so because these systems have to be a lot weaker

**[23:58]** than the sort of human level things what we'll we'll have is intense application of the ways in which AIS have advantages partly offsetting their weaknesses and so AIS are cheap we can call a lot of them

**[24:14]** uh to do many small problems and so you'll have situations where you have Dumber AIS that are deployed thousands of times to equal say one human worker and they'll be doing things like

**[24:32]** um these voting algorithms where you uh with a an llm you generate a bunch of different responses and take a majority vote among them that improves performance sum you'll have things like the alphago kind of approach where you

**[24:49]** use the neural net to do search and you go deeper with the search by plowing in more compute which helps to offset the inefficiency and weaknesses of the model on its own uh you'll do things that would just be

**[25:04]** totally impractical um for humans because of the sheer number of steps and so an example of that would be designing synthetic training data so humans do not learn by just going into the library and opening

**[25:18]** books at random Pages it's actually much much more efficient to have things like schools and classes where they teach you things in a an order that makes sense that's focusing on the skills that are more valuable to learn

**[25:32]** they give you tests and exam they're designed to try and elicit the skill they're actually trying to teach and right now we don't bother with that because we can hoover up more data from the internet we're

**[25:45]** getting towards the end of that but yeah because the AIS get more sophisticated they'll be better able to tell what is a useful kind of skill to practice and to generate that and we've done that in other areas so alphago

**[25:59]** uh the original version of alphago was booted up with data from human go play and then improved with reinforcement learning and Monte Carlo tree search but then

**[26:13]** Alpha zero with a somewhat more sophisticated model uh benefited from some some other improvements um but was able to go from scratch and it generated its own data through self-play

**[26:27]** so which getting data of a higher quality than the human data because there are no human players that good available in the data set and also a curriculum so that at any given point it was playing games against an opponent

**[26:42]** of equal skill itself and so it was always in an area when it was easy to learn if you're if you're just always losing no matter what you do or always winning no matter what you do it's hard to distinguish uh which things

**[26:55]** are better and which are worse and when we have somewhat more sophisticated allies that can generate training data and tasks for themselves for example if the AI can generate a lot of unit tests

**[27:08]** and then can try and produce programs that pass those unit tests then The Interpreter is providing a training signal and the AI can get good at figuring out what's the kind of programming problem that is

**[27:22]** hard for AIS right now that will develop more of the skills that I need uh and then do them and now you're not going to have you know employees at open AI write like a billion programming problems that's just not going to happen

**[27:36]** but you are going to have AIS given the task of producing those enormous number of programming challenges in alums themselves is you know there's a paper out of anthropic called Constitution AI or Constitution RL where they basically

**[27:50]** had the program just like talk to itself and say like is this response helpful if not how can I make this more helpful and the the response is improved and then you train the model on the more helpful responses that it generates by talking

**[28:01]** to itself so that it generates an uh natively and you could imagine you know more sophisticated ways is to do that or better ways to do that okay so but then the question is listen you know gpd4 already costs like

**[28:13]** 50 million or 100 million or whatever it was even if we have greater effective compute from Hardware increases and better models it's hard to imagine how we could sustain like four or five more orders of

**[28:25]** magnitude greater size effective size than gpd4 unless we're jump dumping in like trillions of dollars like the entire the entire economies of big countries into training the next version so the question is do we get something

**[28:39]** that can significantly help with AI progress before we run out of the the sheer uh money and scale and compute that would require to train it do you have a take on that well first I'd say remember that there are these three

**[28:54]** contributing buttons so the new h100s are significantly better than the a100s and a lot of companies are actually just waiting for their deliveries of h100s to do even bigger uh training runs I thought along with the the work of

**[29:10]** hooking them up into clusters and Engineering the thing yeah so all of those factors are contributing and of course mathematically uh uh yeah if you do four orders of magnitude more than 50 or 100 million then you know you're

**[29:25]** getting two trillion dollar territory and yeah I think the the way to look at it is at each step along the way does it look like it makes sense to do the next step uh and so from where we are right now

**[29:41]** seeing the results with gpt4 and check GPT uh companies like Google and Microsoft uh and whatnot are pretty convinced that this is very valuable um you have like talk at Google

**[29:57]** um and Microsoft with Bing that well it's like billion dollar billion dollar matter to change market share in search uh by a percentage Point um and so that can fund a lot and

**[30:10]** on the far end on the extreme if you automate human labor we have a hundred trillion dollar economy most of that economy is paid out in wages so like between 50 and 70 uh trillion dollars per year if you create AGI it's going to

**[30:29]** automate all of that and keep increasing beyond that so the the value of the of the completed project is very much worth uh throwing our whole economy into it if you're going to get the good version not the catastrophic destruction of the

**[30:47]** human race uh or you know some uh some other disastrous outcome and in between it's a question of well did the next step how risky and uncertain is it and how much growth in the revenue

**[31:04]** you can generate with it uh do you get and so for moving up to a billion dollars I think that's absolutely going to happen these large tech companies have r d budgets tens of billions of dollars and when you think about it like

**[31:17]** in the in the relevant sense like all the all the employees at Microsoft who are doing software engineering that's like contributing to creating software objects it's not it's not weird to spend tens of billions of dollars on a product

**[31:31]** that would do so much and I think it's it's becoming more clear that there is sort of Market opportunity to fund the thing uh going up to 100 billion dollars that's like okay the existing r d budgets spread over multiple years

**[31:48]** um but if you if you keep seeing that when you scale up the model uh it substantially improves the performance it opens up new applications you're not just improving your search uh but maybe you know it makes self-driving cars work

**[32:01]** uh you replace bulk software engineering jobs or if not replace them amplify productivity in this kind of dynamic you actually probably want to employ all the software Engineers you can get as long as they're able to make any kind

**[32:14]** attribution because the returns of improving stuff in AI itself gets so high but yeah so I think that can go up to 100 billion and at 100 billion you're using like a significant fraction of our existing Fab capacity like right

**[32:33]** now the revenue of Nvidia is like 25 billion uh the revenue of tsmc I believe it's like um it's over 50 billion less I checked in 2021 uh Nvidia was maybe uh seven and

**[32:49]** a half percent less than 10 percent of tsmc Revenue uh so there's a lot of room and most of that was not AI chips um you know they have a large gaming segment their data center gpus that are

**[33:03]** used for video and the like um so there's room for um more than an order of magnitude uh increase by redirecting uh existing Fabs to produce more AI chips and then just actually using the AI chips that these

**[33:21]** companies have in their Cloud for the big training runs uh and so I think that that's enough to go to the 10 billion and then combine with stuff like the h100 to go up to 100 billion just to emphasize for the

**[33:31]** audience the initial point about Revenue made if if it cost open AI a hundred million dollars to trade in gpd4 and it generates 500 million dollars in Revenue you you know you pay back your expenses with 100 million you have 400 million

**[33:44]** for your next training run then you train your GPD 4.5 you know you get let's say four billion dollars out of Revenue out of that that's where the feedback group of sort of Revenue comes from where you're automating tasks and

**[33:55]** therefore you're making money you can use that money to automate more tasks on the ability to uh redirect the fat production towards AI chips so then the tldr on you 100 billion dollars worth of compute I mean fabstick was like a

**[34:13]** decade or so to build um so given the ones we have now and the ones that are going to come online in the next decade is there enough to sustain a hundred billion dollars of GPU compute if you wanted to spend that on a

**[34:25]** training run yes you could definitely make the 100 billion one as you go up to a trillion dollar run and larger um it's going to involve more Fab construction and yeah Fabs can take a long a long time to build on the other

**[34:40]** hand if in fact you're getting very high revenue from the AI systems and you're actually bottlenecked on the construction of these Fabs

**[34:52]** then their price could Skyrocket and that uh lead to measures we've never seen before uh to expand and accelerate uh production like if you consider so at the limit because you're getting models that approach uh human-like

**[35:10]** capability if you imagine things that are getting close to like brain like efficiencies plus AI advantages we were talking before about well a GPU that is supporting an AI really it's a cluster of gpus supporting AIS that do

**[35:24]** things uh in parallel data parallelism but if that can work four times as much as a human a highly skilled motivated focused human with levels of Education that have never been seen in the human population

**[35:39]** uh and so if like a typical software engineer can earn hundreds of thousands of dollars the world's best software Engineers uh can earn millions of dollars today and maybe more in a world where there's so much demand for AI

**[35:55]** um and then times four uh for working all the time well I mean if you have if you can generate like close to 10 million dollars a year um out of the future version h100 uh

**[36:07]** that cost tens of thousands of dollars with a huge profit margin now and profit margin could be um could be reduced with like large production uh that is a big difference that that

**[36:20]** chip uh pays for itself almost instantly um and so you could you could support pain 10 times as much to have these Fabs constructed more rapidly you could have if AI is starting to be able to contribute uh you can have could have ai

**[36:39]** contributing more of the skill technical work that makes it hard for say Nvidia to suddenly find uh thousands upon thousands of top quality engineering hires uh if AI can provide that now if AI hasn't reached that level of

**[36:54]** performance then this is how you can have things stall out and like a world where AI progress stalls out is one where you go to the 100 billion and then over succeeding years trillion dollar uh things software progress

**[37:09]** um turns to start turns out to to stall you lose the gains that you are getting from moving researchers from other fields lots of physicists and people from other areas of computer science have been going into AI but you sort of

**[37:22]** tap out those resources uh has it AI becomes a larger proportion of the research field and like okay you've put in all of these inputs but they just haven't yielded ajia yet I think that set of inputs probably would yield the

**[37:37]** kind of AI capabilities needed for intelligence explosion but if it doesn't after we've exhausted this current scale up of like increasing the share of our economy that is trying to make AI if that's not enough

**[37:51]** then after that you have to wait for the slow grind of things like General economic growth population growth and such and so think slow and that results in my credences and this kind of advanced AI happening to be relatively

**[38:04]** concentrated like over the next 10 years compared to the rest of the century because we just can't we can't keep going with this rapid redirection of resources into AI That's that's a one-time thing if the current scale up

**[38:19]** works it's going to happen we're going to get to AJ really fast like within the next 10 years or something if the current scale of doesn't work all we're left with is just like our economy growing like two percent a year so we

**[38:31]** have like two percent a year or more resources to spend on AI and at that scale you're talking about decades before you can adjust your sheer or brute for so you can you know train that 10 trillion dollar model or something

**[38:42]** let's talk about why you have your thesis that the currency you love would work what is the evidence from AI itself or maybe from primate Evolution and the evolution of other animals just give me the whole the whole Confluence of

**[38:56]** reasons I think maybe the best way to look look at that might be to consider when I first became interested in this area so in the 2000s which was before the Deep learning Revolution how would I think about timelines how

**[39:09]** did I think about timelines and then how have I updated based on what has been happening with deep learning and so back then I would have said we know the brain is a physical object

**[39:24]** an information processing device it works um it's possible and not only is it possible it was created by Evolution on Earth and so that gives us something of an

**[39:37]** upper Bound in that this kind of Brute Force was sufficient there are some complexities uh with like well what if it was a freak accident and it you know that didn't happen on all of the other planets in that added some value I have

**[39:51]** a paper with Nick Bostrom on this I think basically that's not that important an issue there's convergent evolution like octopi are also quite sophisticated if the if a special event was at the level of forming cells at all

**[40:08]** um or forming brains at all we get to skip that because we're choosing to build computers and we already exist we have that that Advantage so say Evolution gives something of an upper bound really intensive massive Brute

**[40:22]** Force search um and things like evolutionary algorithms can produce intelligence doesn't the fact that um octopi and I guess other mammals they got to the point of being like pretty

**[40:33]** intelligent but not human level intelligent is that some evidence that there's a heart step between a cephalopod and a human yeah so that that would be a place to look yeah um

**[40:45]** it doesn't seem particularly compelling one source of evidence on that is work by um herculiano Hutzel uh I hope I haven't mispronounced her name but she's a neuroscientist who has dissolved the

**[41:01]** brains of many creatures and by counting uh the uh the nuclei she's able to determine how many neurons are are present in different species and find a lot of interesting Trends and scaling laws and she's a paper

**[41:17]** um discussing the human brain has a scaled up primate brain and across like a wide variety of animals and mammals in particular um there are certain characteristic uh changes in the relative number of neuron

**[41:32]** size of different brain regions uh how things scale up um there's a lot of yeah there's a lot of structural um structural similarity there and you can

**[41:44]** explain a lot of what is different about us with a pretty Brute Force story which is that you expend resources on having a bigger brain keeping it in good order giving it time to learn so we have an unusually

**[42:00]** long childhood unusually longness period we spend more compute by having a larger brain than other animals uh three more than three times as large as chimpanzees and then we have a longer childhood than human disease and much more than many

**[42:16]** many other creatures so we're spending more compute in a way that's analogous to like having a bigger model and having more training time with it and given that we see um with our AI models this sort of like

**[42:30]** large consistent benefits from increasing compute spent in those ways and with qualitatively new capabilities uh showing up over and over again particularly in areas that sort of AI Skeptics uh call out in my experience

**[42:45]** like over the last 15 years the things that people call out as like ah but the AI can't do that and it's because of a fundamental limitation I've gone through a lot of them you know there were Winograd schemas catastrophic forgetting

**[42:59]** quite a number um and yeah they have repeatedly gone away through scaling and so there's a there's a picture that we're we're seeing supported from biology and from our experience with AI where you can

**[43:15]** explain like yeah in general there are trade-offs where the extra Fitness you get from a brain is not worth it and so creatures wind up mostly with small brains because they can save that

**[43:30]** biological energy and that time to reproduce for digestion and so on and the humans we actually seem to have wound up in a niche within self-reinforcing where we greatly increase the returns to having

**[43:46]** large brains and language and Technology are the the sort of obvious candidates when you have humans around you who know a lot of things and they can teach you and compared to almost any other species we have vastly more instruction

**[44:01]** from parents and the Society of the youngin then you're getting way more from your brain because you can get per minute you can learn a lot more useful skills and then you can provide the energy you need to feed that brain by

**[44:18]** hunting and Gathering by having fire that makes digestion easier and basically how this process goes on it's increasing the marginal increase in reproductive Fitness you get from allocating more

**[44:31]** resources along a bunch of Dimensions towards cognitive ability and so um that's bigger brains longer childhood having our attention be more on learning so humans play a lot and we we keep playing as adults which is a very weird

**[44:46]** thing compared to other animals we're more motivated to copy other humans around us than like even than the other primates and so these are sort of motivational changes that keep us using more of our attention and

**[45:00]** effort on learning which pays off more when you have a bigger brain and a longer lifespan in which to learn many many creatures are subject to lots of predation or disease and so if you try you know you're you're a mayfly or a

**[45:14]** mouse if you try and invest in like a giant brain and a very long childhood you're quite likely to be killed by some predator or some disease before you're able to actually use it and so that means you actually have

**[45:27]** exponentially increasing costs in a given niche so if if I have a 50 chance of dying every few months of the you know a little mammal or a little lizard or something that means the cost of going from three months to 30 months of

**[45:42]** learning in childhood development it's not 10 times the loss that's now it's 2 to the negative 10. so one a factor of 1024 reduction in the benefit I get from what I ultimately learned because 99.9 uh of the animals will have been

**[46:01]** killed before that point we're in a niche where we're like a large long-lived animal with language and technology so where we can learn a lot from our groups and that means it pays off to really

**[46:12]** um just expand our investment on these multiple fronts in intelligence that's so interesting um just for the audience the the calculation about like two to the

**[46:25]** whatever months is just like you have a half chance of dying this month a half chance of dying next month um you multiply those together okay there's other species though that do live in flocks or as packs where you

**[46:37]** could imagine I mean they do have like a smaller version of the development of cubs into that I like play with each other why isn't this a hill on which they could have climbed to human level intelligence themselves if it's

**[46:52]** something like language or technology um humans were getting smarter before we got language I mean obviously we had to get smarter to get language right we couldn't just look at language without becoming smarter so yeah where did it

**[47:04]** seems like there should be other species that should have beginnings of this sort of cognitive Revolution especially given how valuable it is given listen we've dominated the world you would think there would be selective pressure for it

**[47:16]** Evolution doesn't have foresight yeah the thing in this generation that gets more surviving Offspring and grandchildren that's the thing that becomes more common uh Evolution doesn't look ahead and they oh in a million

**[47:30]** years you'll have a lot of descendants uh it's what what survives and reproduces now and so in fact there are correlations where uh social animals uh do on average uh have larger brains and part of that

**[47:46]** is probably that the additional social applications of brains like keeping track of which of your group members have helped you before so that you can reciprocate you scratch my back I'll scratch yours remembering who's

**[48:00]** dangerous within the group that sort of thing is an additional application of intelligence um and so there's some correlation there about what it what it seems like is that yeah in most of these cases

**[48:15]** um it's enough to invest more but not invest to the point where a mind can easily develop language and technology and pass it on and so there are you see bits of tool use in some other primates who have an advantage

**[48:30]** that so compared to say the whales who have they have quite large brains partly because they are so large themselves and they I have some other other thing but they don't have hands which means that

**[48:41]** reduces a bunch of ways in which brains can pay off and investments in the functioning of that brain but yeah so primates we'll use sticks um to extract termites capture monkeys

**[48:54]** we'll open clams by Smashing them with rock so there's bits of bits of tool use but what they don't have is the ability to sustain culture a particular primate will maybe discover one of these tactics and maybe it'll be

**[49:09]** copied by their immediate group but they're not holding on to it that well they're like well when they see the other animal do it they can copy it in that situation they don't actively teach each other their population locally is

**[49:22]** quite small so it's easy to forget things easy to lose information and in fact they they remain technologically stagnant for hundreds of thousands of years and we can actually look at some

**[49:35]** human situations so there's an old paper I Believe by The Economist uh Michael Cramer talks about technological growth in the different continents for human societies and so you have

**[49:52]** Eurasia is the largest integrated uh connected area Africa is partly connected to it but the Sahara Desert restricts the flow of information and technology and such and then you have the Americas which were after the

**[50:05]** colonization from the land bridge were largely separated and are smaller than Eurasia then Australia and then you had like smaller Island situations like Tasmania and so technological progress seem to have been faster the larger the

**[50:20]** connected group of people and in the smallest groups so like in Tasmania you had a relatively small population and they actually lost technology so things like they lost some like

**[50:32]** phishing techniques and if you have a small population and you have some limited number of people who know a skill and they happen to die or happened there's like you know some some change in circumstances that

**[50:46]** causes people not to practice or pass on that thing uh and then you lose it and if you have few people you're doing less Innovation the rate at which you lose Technologies to some kind of local disturbance and

**[50:59]** the rate at which you create new technologies can wind up in balance and the great change of hominids and humanity is that we wound up in this situation we were accumulating faster than we were losing and as we

**[51:13]** accumulated those Technologies allowed us to expand our population they created additional demand for intelligence so that our brains became three times as large as that chimpanzees yeah and our ancestors who had a similar

**[51:29]** um brain size okay and then the crucial Point uh I guess in relevance to AI is that the selective pressures against intelligence in other animals are not uh acting against these neural networks because we are you know they're not

**[51:44]** going to get like eaten by a predator if they spend too much time becoming more intelligent um we're like explicitly trading them to become more intelligent so we have like good first principles reason to think

**[51:54]** that if it was scaling that made our minds this powerful and if the things that prevented other animals from uh scaling are not impinging on these neural networks these things should just continue to become very smart yeah we

**[52:06]** are we're growing them in a technological culture where there are jobs like software engineer that depend much more on sort of cognitive output and less on things like metabolic resources devoted to the immune system

**[52:20]** uh or to like building big muscles to throw Spears this is kind of a side note but I'm just kind of interested I think you have reference to some point jinchilla scaling for the audience this is a paper from deepmind which describes

**[52:33]** if you have a model of a certain size what is the optimum amount of data that it should be trained on so you can imagine bigger models you can you can use more data to train them and in this way you can figure out where should you

**[52:44]** spend your computer did you spend it on making the model bigger or should you spend it on training it for longer I'm curious if uh in the case of different animals in some students they're like model sizes or how big their brain is

**[52:55]** and their training data sizes like how long their cubs or how long their infants or toddlers are um before they're full adults is there some sort of like scaling law of yeah I mean so the the chinchilla scaling isn't

**[53:07]** interesting because they we were talking earlier about the cost function for having a longer childhood and so where it's like exponentially increasing in the amount of training compute you have when you have exogenous forces that can

**[53:20]** kill you whereas when we do big training runs the cost of throwing in more gpus is almost linear uh and it's much better to be you know linear than exponentially decayed oh yeah that's that's really good point

**[53:31]** you expand resources and so chinchilla scaling would suggest that like yeah the opt for a brain of sort of human size it would be optimal to have many millions of years of education but obviously that's impractical because of

**[53:47]** exogenous mortality for humans and so there's a fairly compelling argument that relative to the situation where we would train AI that animals are systematically way under trained they're more efficient than our models

**[54:06]** we still have room to improve our algorithms to catch up with the efficiency of brains but they are laboring under that disadvantage yeah that is so interesting okay so I guess another question you

**[54:19]** could have is humans got started on this evolutionary hill climbing route where we're getting more intelligent than it has more benefits for us why didn't we go all the way on that

**[54:31]** route if intelligence is so powerful why aren't all humans as smart as we know humans can be right at least that's smart um if intelligence is so powerful like why hasn't there been stronger selective

**[54:44]** pressure I understand like oh listen hip size you can't like give birth to a really big headed baby or whatever but you would think like Evolution would figure out some way to offset that such if intelligence has such big Power

**[54:55]** and such is so useful yeah I think you can actually look at it quantitatively that's that's not true and even in in sort of recent history there has been it looks like a pretty close balance between the costs and the benefits of

**[55:10]** having uh more cognitive abilities and so you say like uh you know who needs to worry about like you know the metabolic costs like you need humans put like order 20 of our metabolic energy into the brain and it's higher for like young

**[55:27]** children yeah so 20 of the I mean and then you know there's like breathing and digestion and the immune system and so for most of history people have been dying left and right like a very large proportion of

**[55:43]** people will die of infectious disease yeah and if you put more resources into your immune system you survive so it's like life or death pretty directly via that

**[55:56]** mechanism uh and then this is this related also when people die more of disease during famine and so there's Boomer bust and so if you have 20 less metabolic requirements or has anger a child and if

**[56:10]** you have a lot more I mean it's like 40 or 50 less metabolic requirements you're much more likely to survive that famine so these are these are these are pretty big uh and then there's a trade-off about

**[56:22]** just cleaning mutational load so every generation new mutations and errors happen in the process of reproduction and so like we know there are many um genetic abnormalities uh that occur through new mutations each generation

**[56:37]** and in fact we have Down syndrome is the chromosomal abnormality that you can survive all the other is just kill the embryo um and so we never see them um but like down syndrome occurs a lot

**[56:52]** and there are many other lethal mutations and there's as you go to less damaging ones there are enormous numbers of less damaging mutations that are degrading every system in the body and so Evolution each generation has to

**[57:08]** pull away at some of this mutational load and the priority with which that mutational load is pulled out scales and proportions how much the traits it's affecting impact fitness so you've got new mutations that impact

**[57:22]** your resistance to malaria yeah you've got new mutations that damage brain function um and then those mutations are purged each generation if malaria is a bigger difference in mortality than like the

**[57:37]** incremental Effectiveness as a hunter-gatherer you get from you know being slightly more intelligent then you'll Purge that mutational load first sure and similarly if there's like you know humans have been vigorously

**[57:51]** adapting to new circumstances so since agriculture people have been developing things like the ability to uh you know have uh emulates to digest uh breads the ability to like digest milk um and if you're evolving for all of

**[58:08]** these things and if some of the things that give an advantage for that incidentally carry along nearby them some negative effect on another trait then that other trait can be damaged so it really matters how important

**[58:21]** to survival and reproduction cognitive abilities were compared to everything else the organism has to do and that in particular like surviving feast and famine having like the physical abilities to do hunting and hunting and

**[58:35]** Gathering and like even if you're like very good at planning your hunting being able to throw a spear harder can you know be a big difference and that means energy to build those muscles and then to sustain them

**[58:47]** uh and so given all these all these factors um it's like yeah it's it's not a slam dunk to invest at the merge and like today like having bigger brains for example is

**[59:01]** It's associated with like greater cognitive ability but it's like it's modest um large-scale pre-register studies pre-registered studies with MRI data you know it's like you know in a Range maybe

**[59:14]** like a correlation of 0.25 0.3 and the standard deviation of brain size is like 10 percent so if you double the size of the brain so go and the existing brain costs like 20 of metabolic energy go up go up to 40

**[59:30]** percent okay that's like eight eight standard deviations of brain size if the correlation is like say it's 0.25 um then

**[59:41]** yeah like you can you get gained from that eight standard deviations of brain size two standard deviations of cognitive ability and like in our modern society where cognitive ability is very rewarded and like uh you know finishing

**[59:58]** finishing school becoming an engineer or a doctor or whatever can can pay off a lot financially still the like the average observed return in like income is like a one or two

**[1:00:12]** percent proportional increase there's more effects of the tail there's more effect in professions like stem uh but on the whole it's not like you know if it was like a five percent increase or a ten percent increase then

**[1:00:26]** you could you could you could tell a story where yeah this is hugely increasing the amount of food you could have you could support more children but it's like it's a modest effect and the metabolic cost will be large and then

**[1:00:36]** throw in these other these other aspects and I think it's you can tell the story and also we can just we can see there was not very strong rapid directional selection on the thing which there would be if

**[1:00:49]** like you know you could by solving like a by solving like a math puzzle you could defeat malaria um like then then there would be more evolutionary pressure that is so

**[1:01:01]** interesting and not to mention of course that um yeah if you had like two extra brain size you're you were without C-section you would like your mother would or both would die that I this is a question I've actually been curious

**[1:01:10]** about for like over a year and I've like briefly tried to look up an answer this is I know this is off topic but I apologize to the audience but I was super interested in those like that was like

**[1:01:20]** the most comprehensive and interesting answer I could vote for okay so yeah we have a good explanation of good first principles evolutionaries and for thinking that intelligence scaling up to humans is not

**[1:01:33]** um implausible just by throwing more scale at it I would also add this was something that would have mattered to me more in the 2000s uh we also have the brain right here with us uh for available for Neuroscience to reverse

**[1:01:46]** engineer its properties and so uh in the 2000s when I I said yeah I expect this by you know middle of the century-ish that was a backstop if we found it absurdly difficult to get to the algorithms and then we would learn from

**[1:01:59]** Neuroscience but in the actual the actual history it's it's really not like that we develop things in Ai and then also we can say oh yeah this is sort of like this thing in Neuroscience or maybe this is a good explanation if it's not

**[1:02:12]** as though neuroscience is driving AI progress It's it's turns out not to be that necessary yeah similar to I guess you know how planes were inspired by the existence proof of birds but Jet and stone flap all right

**[1:02:27]** so yeah scaling uh good reason I think scaling might work so we we spent 100 billion dollars and we have something that is like human level or can do help significantly with AI research I mean that that might be on

**[1:02:40]** the earlier end um but I mean I definitely would not rule that out given the rates of change we've seen with the last few scallops all right so at this point somebody might be skeptical okay like

**[1:02:53]** listen we already have a bunch of human researchers right like the incremental researcher how profitable is that and then you might say well no this is like thousands of researchers I don't know how to express a skepticism exactly but

**[1:03:04]** skeptic is a skeptical of just generally the effect of scaling up the number of people working on the problem to rapid rapid progress on that problem what somebody might think okay listen with humans the reason population working on

**[1:03:17]** a problem is such a good proxy for progress on the problem is that there's already so much variation that is accounted for when you say there's like a million people working on a problem you know there's like a hundreds of

**[1:03:27]** super Geniuses working on it thousands of people who are like very smart working on it whereas within the eye all the copies are like the same level of intelligence um and if it's not Super Genius

**[1:03:37]** intelligence the uh the the the total quantity it might not matter as much yeah I'm not sure what your model is here so is this the model that the dimension returns kickoff suddenly

**[1:03:55]** has a cliff right where we are and so like there was there were results in the past from throwing more people at problems um and I mean this has been useful in historical prediction

**[1:04:08]** um one of the there's this idea of experience curves and rights law um basically measuring cumulative production in a field or which is that also going to be a measure of like the scale of effort and investment and

**[1:04:23]** people have used this correctly uh to argue that renewable energy technology like solar would be falling rapidly in price because it was going from a low base of very small production runs not much investment in doing it

**[1:04:38]** efficiently um and yeah uh climate Advocates correctly called out people and people like David Roberts um the futurist Rama is now actually has some some interesting uh writing on this

**[1:04:53]** that yeah correctly called out that there would be really drastic uh fall and prices of solar and batteries because of the increasing investment going into that the Human Genome Project would be another so I'd say there's like

**[1:05:06]** yeah real real evidence these observed correlations from like ideas getting harder to find have have held over a fair uh a fair range of data and over quite a lot of time uh so I'm wondering what

**[1:05:21]** what what's the yeah the the nature of the deviation you're thinking about that um we're talking about uh maybe this is like a good way to describe what happens when More Humans enter a field but does

**[1:05:34]** it even make sense to say like a greater population of AIS is doing AI research if there's like more gpus running a copy of gpd6 doing AI research it just like how how applicable are these uh economic models of human the quantity of humans

**[1:05:49]** working on a problem to the magnitude of AI is working on a problem yeah so if you have ai that are directly automating uh you know particular jobs that humans were doing before then we say well with additional compute

**[1:06:03]** we can run more copies of them to do more of those tasks simultaneously we can also run them at greater speed and so some people have an intuition that like well you know what matters is like time it's not how many people working on

**[1:06:18]** problem at a given point I think this doesn't bear out super well but AI can also be run faster than humans and so if you have a a set of AIS that can do the work of the individual human researchers and run at 10 times or 100 times the

**[1:06:38]** speed and we ask well could the human research Community have solved these algorithmic problems do things like invent transformers over 100 years if we have this we have AIS with a

**[1:06:51]** population effective population similar to the humans but running 100 times as fast and so you have to you have to tell a story where no the AI they can't really do

**[1:07:02]** the same things as the humans and we're talking about what happens when uh the ads are more capable of in fact doing that although they become more capable as lesser capable versions of themselves

**[1:07:15]** help us make themselves more capable right so you had to like kick start that at some point is there an example in analogous situations is intelligence unique in the sense that you have a feedback loop of

**[1:07:30]** with a learning curve or something else a system outputs are feeding into its own inputs in a way that because if we're talking about something like Moore's Law or the cost of solar you do have this way like

**[1:07:42]** where you know more people are we're throwing more people with the problem and it's um we're you know we're making a lot of progress but we don't have the sort of additional part of the model where Moore's Law leads to More Humans

**[1:07:54]** somehow uh and the more humans are becoming researchers so you do actually have a version of that in the case of solar so you have a small infant industry that's doing things like providing solar panels for space

**[1:08:08]** satellites and then getting increasing amounts of subsidized government demand because of uh you know worries about fossil fuel depletion and then climate change you can have the dynamic where visible

**[1:08:20]** successes uh with solar or like lowering prices then open up new markets so there's a particularly huge transition where Renewables become cheap enough to replace large chunks of the electric grid

**[1:08:34]** uh earlier that you're dealing with very Niche situations like yeah so the satellites where you have uh it's very difficult to refuel a satellite in place and then remote areas and then moving to like you know the super Sunny the

**[1:08:48]** sunniest areas in the world with the biggest solar subsidies um and so there was an element of that where more and more investment has been thrown into the field and like the market has rapidly expanded has this

**[1:09:01]** technology improved but I think the the closest analogy um is actually the long run growth of human civilization itself and I know you had Holden karnovsky from the open philosophy project on earlier and

**[1:09:14]** discussed some of this research about the long run acceleration of human population and economic growth and so developing new technologies allowed human population to expand humans to occupy new habitats and new areas and

**[1:09:31]** then to invent agriculture which support the larger populations and then even more advanced Agriculture and the modern industrial society and so there total technology and output allowed you to support More Humans

**[1:09:45]** who then would discover more technology and continue the process now that was boosted because on on top of expanding the population the share of human activity that was going into invention and

**[1:09:57]** Innovation went up and that was a key part of the Industrial Revolution there was no such thing as a corporate research lab or like an Engineering University um prior to that and so you were both

**[1:10:09]** increasing the total human population and the share of it going in but this population Dynamic is pretty is pretty analogous humans invent farming they can have more humans than they can invent industry and so on

**[1:10:21]** so maybe somebody would be skeptical that with AI progress specifically it's not just a matter of you know some like um some farmer figuring out crop rotation or some blacksmith figuring out how to do Metallurgy better

**[1:10:35]** you in fact even to make the for the 50 Improvement in productivity you basically need something on the IQ that's close to aliascover there's like a discontinuous um you're like contributing very little

**[1:10:48]** to productivity and then you're like Ilia and then you contribute a lot but the becoming Ilia is you see what I'm saying there's not like a gradual increase in capabilities at least to the Future you're imagining a

**[1:10:58]** case where uh the distribution of tests is such that there's nothing that you can where individually automating it particularly helps uh and so the ability to contribute to AI research is really end loaded is that what you're saying

**[1:11:14]** yeah I mean we already see this in in these sorts of like really high IQ uh companies or projects where theoretically I guess Jane Street or open AI could hire like a bunch of uh you know mediocre people to do there's a

**[1:11:28]** comparative advantage they could do some menial tasks and that could free up the time of the really smart people but they don't do that right uh with transaction costs whatever else self-driven cars would be another example where you have

**[1:11:40]** a very high quality threshold and so when you your performance as a driver is worse than a human like you have 10 times the accident rate or 100 times the accident rate then the cost of insurance for that which is a proxy for people's

**[1:11:54]** willingness to ride the car and stuff too would be such that the insurance costs would absolutely dominate so even if you have zero labor cost it's offset by The increased Insurance costs and so there are lots of cases like that where

**[1:12:05]** like partial automation is not in practice uh very usable because complementing other resources you're going to use those other resources less efficiently

**[1:12:18]** um you know in in a post AGI future I mean the same thing can apply to humans so people can say well comparative advantage you know even if AIS can do everything better than a human uh well it's still worth something uh the human

**[1:12:34]** can do because how many American you know we can lift a box that's something um now there's a question of property rights if well if it could just make more robots yeah um but even even absent that in such an

**[1:12:49]** economy you wouldn't want to let a human worker into any industrial environment because you know in a clean room they'll be emitting all kinds of skin cells and messing things things up you need to have an atmosphere there you need a

**[1:13:01]** bunch of supporting tools and resources and materials and those supporting resources and materials will do a lot more productively working with AI and robots rather than human so you don't want to let a human anywhere near the

**[1:13:15]** thing just like you know in a you don't you don't have a gorilla wandering around in a china shop even if you've trained it to most of the time pick up a box for you if you give it a banana it's just not worth it to have it wandering

**[1:13:26]** around your china shop yeah yeah like why is that not a good objection to I mean I think that that is one of the the ways uh in which partial automation uh can fail to really translate into a lot of economic value that's something that

**[1:13:41]** will attenuate as we go on and as the AI is more able to work independently and more able to handle its own uh its own screw-ups get more more reliable but the way in which it becomes more reliable is by AI progress speeding up which happens

**[1:13:59]** if AI can contribute to it but if there is the if there is some sort of reliability bottle like the prevents it from contributing to that progress then you don't have the loop right so yeah I mean this is this is why we're not there

**[1:14:10]** yet right but then what is the reason to think we'll be there at the broad reason is we have these inputs are scaling up there's a so epoc which I mentioned earlier uh they have a paper I think

**[1:14:22]** it's called compute Trends and three areas of machine learning or something like that and so they look at the compute expended on machine learning systems since the found founding of the field of AI at the beginning of the

**[1:14:36]** 1950s um and so it mostly it grows with Moore's Law um and so people are spending a similar amount on their experiments um but they can just buy more with that

**[1:14:49]** because the impute is coming and so that data I mean it covers over 20 orders of magnitude maybe like 24. and of all of those increases since 1952 a little more than half of them happened

**[1:15:06]** between 1952 and 2010 and all the rest is since 2010. so we're we've been scaling that up like four times as fast as was the case for most of the history of AI we're running through the orders of magnitude of possible resource inputs

**[1:15:25]** you could need for AI much much more quickly than we were for most of the history of AI That's why this is a period of like with a very elevated chance of AI per year because we're moving through

**[1:15:38]** so much of the space of inputs per year and indeed it looks like this scale up taken taken to its conclusion uh we'll cover another bunch of orders of magnitude and that's actually a large fraction of those that are left before

**[1:15:53]** you start running into saying well this is going to have to be like Evolution with the sort of simple hacks we get to apply like we're selecting for intelligence the whole time we're not going to make do the same mutation that

**[1:16:06]** causes fatal fatal Childhood Cancer a billion times even though I mean we keep getting the same fatal mutations even though they've been done many times we use gradient descent which takes into account the derivative of improvement on

**[1:16:21]** the loss all throughout the network and we we don't throw away all the contents of the network with each generation where you can press down to a little DNA so there's that that bar of like well if you're going to do Brute Force like

**[1:16:34]** Evolution combined with a sort of very simple ways we can save orders of magnitude on that we're going to cover I think a fraction that's like half of that distance uh in this scale up over the next 10 years or

**[1:16:48]** so and so if you started off with a kind of vague uniform prior you're like well it's probably you probably can't make AGI with like the amount of compute that would be involved in a fruit fly existing for a minute which would be the

**[1:17:02]** early days of AI yeah um you know maybe maybe you get lucky we were able to make calculators because calculator has benefited from like very reliable seriously fast computers and where we could take a tiny tiny tiny

**[1:17:16]** tiny fraction of a human brain's compute and use it for a calculator we couldn't take an ant Sprain and rewire it to calculate it's hard hard to manage ant farms let alone get them to do a rhythmic for you uh and so

**[1:17:30]** there were some things where we could exploit the differences between biological brains and computers to do stuff super efficiently on computers we would doubt that we would be able to do so much better than biology that we

**[1:17:45]** with a tiny fraction of an insect's brain we'd be able to get AI early on on the far end it seemed very implausible that we couldn't do better than completely Brute Force Evolution and so in between you

**[1:17:57]** have some number of orders of magnitude of inputs where it might be and like in the 2000s I would say well you know I'm going to have a pretty uniformish prior I'm going to put weight on it happening at like the sort of equivalent of like

**[1:18:12]** 10 to the 25 Ops 10 to the 30 10 to the 35. um and sort of spreading out over that and then I can update on other information and in the short term I would say like in 2005 I would say well

**[1:18:25]** I don't see anything that looks like the cusp of AGI so I'm also going to lower my Credence for like the next five years or the next 10 years and so that that would be kind of like a vague prior and then when we take into account like well

**[1:18:38]** how quickly are we running through those orders of magnitude if I have a uniform prior I assign half of my weight to the first half of remaining orders of magnitude and we're going to run through those

**[1:18:49]** over the next 10 years and some uh then that calls on me to put half of my Credence conditional and we're ever going to make it Ai and which seems likely worth the material object easier than evolution

**[1:19:02]** I've got to put similarly a lot of my Credence on AI happening in the scale up and then that's supported by what we're seeing in terms of the the rapid advances and capabilities uh with AI and lbms in particular okay that's actually

**[1:19:17]** a really interesting point so now but somebody might say listen there's not some sense in which AIS could universally speed up the progress of openai by 50 or 100 or 200 percent if they're not able to do everything

**[1:19:31]** better than Ilyas escover can there's going to be something in which we're bottlenecked by the human researchers and bottleneck effects dictate that you know the slowest moving part of the organization will be the one that kind

**[1:19:44]** of determines the speed of the progress of the whole organization or the whole project which means that unless you get to the point where you're like doing everything and everybody in the organization can do you're not going to

**[1:19:54]** significantly speed up the progress of the whole project as a whole yeah so that that is a hypothesis and I think there's a lot of truth to it so when we think about like the ways in which AI can contribute so there are

**[1:20:06]** things we talked about before like the AIS setting up their own curriculum and that's something that Ilya can't do directly and doesn't do directly and there's a question how much does that improve performance

**[1:20:19]** um there are these things where the AI helps uh to just like produce some code for for some tests and it's beyond hello world at this point but I mean the sort of thing that I hear from uh AI researchers at leading Labs is

**[1:20:35]** that you know on their on their core job where they're like most expert it's not helping them that much but then you know their job often does involve oh I've got to I've got to code something that's out of my usual area of expertise

**[1:20:49]** um or I want to research this question and it helps them there and so that saves some of their time and frees them to do more of the bottleneck work and then I think the the idea of well um you know is is everything uh

**[1:21:04]** dependent on Ilia and Ilia so much better than the uh hundreds of other uh employees I think a lot of people who are contributing they're doing a lot of tasks um and so you can have quite a a lot of

**[1:21:18]** of gain from automating some areas where you then do just an absolutely enormous amount of it relative to what you would have done before because things like designing the custom curriculum you're like maybe had some humans put some work

**[1:21:31]** into that um but you're not going to employ billions of humans to produce it at scale and so it winds up being a larger share of the progress uh than it was before you get some

**[1:21:42]** benefit from these sorts of things where oh yeah there's like pieces pieces of my job um that now I can hand off to the AI and lets me focus more on the things that the AI still can't do

**[1:21:56]** and then at the later on you get to the point where yeah the AI can do your job uh including the most difficult parts and maybe it has to do that in a a different way maybe it like throat spends a ton more time thinking about

**[1:22:11]** each step of a problem than you and that's and that's the late end and the stronger these bottlenecks effects are the more the economic Returns the scientific returns and such are end loaded towards getting sort of full AGI

**[1:22:26]** the weaker the bottlenecks are the more interim results uh will be really paying off I guess I probably disagree with you on how much the sort of the the Ilias of organizations seem to matter I guess just from the evidence alone like how

**[1:22:40]** many of the big sort of breakthroughs that in deep learning in general was like that single individual responsible for right um and how much of his time is he spending doing anything that's not that

**[1:22:51]** like copilot is helping him on I'm guessing like most of it's just like managing people and coming up with ideas and uh yeah trying to like understand systems and so on um and if that is the if like the five

**[1:23:02]** or ten people who are like that at open AI or anthropic or whatever are the are basically the way in which the progress is happening or at least the algorithmic progress is happening then

**[1:23:15]** how much of Veteran better co-pilot I know co-pilot is not the thing you're talking about with like 20 automation but something like that how much of um yeah how much is that contributing to the sort of like core function of the

**[1:23:27]** the research scientist yeah natural quantitatively how much we uh we disagree about the importance of sort of uh key research employees and such I certainly think that some researchers

**[1:23:44]** um you know add you know more than 10 times the average employee uh even much more and obviously managers can add an enormous amount of value by proportionately multiplying the output of the many people that they manage

**[1:23:59]** and so that's the kind of thing that we were discussing earlier uh when talking about well if you had sort of full human level AI or AI that had all of the human capabilities plus AI advantages

**[1:24:14]** it would be you know you'd Benchmark not off of what the sort of typical human performance is but Peak Human Performance and Beyond so I yeah I accept all that um I do think it makes makes a big

**[1:24:28]** difference for people how much they can I would Source a lot of the test that are less wow less creative and an enormous amount is learned by experimentation ml has been um you know quite experimental field and

**[1:24:44]** there's a lot of engineering work in say building large super clusters making yeah Hardware aware optimization and coding of these things being able to do the parallelism in large models and the the engineers

**[1:25:01]** are busy uh and it's it's not just only a big thoughts uh kind of area and then the the other Branch um is where will the AI advantages and disadvantages be

**[1:25:17]** um and so one AI Advantage is being omnidisciplinary and familiar with the newest things so I mentioned before there's no human who has a million years of tensorflow

**[1:25:30]** experience and so to the extent that we're we're interested in like the very very Cutting Edge of things that have been developed quite recently than AI that can learn about them in

**[1:25:40]** parallel and experiment and practice with them in parallel can learn much faster than a human potentially and the the area of computer science is one that is especially suitable for AI to learn in a digital environment so it

**[1:25:57]** doesn't require like driving a car around that might kill someone have enormous costs you can you can do unit tests you can you can prove theorems you can do all sorts of operations entirely in the

**[1:26:12]** confines of a computer and which is one reason why programming has been benefiting more than a lot of other areas from llms Recently whereas robotics is lagging so there's some of that and then just considering uh well

**[1:26:27]** actually I mean they are getting better at things like that you know the the GRE math at programming contests and I mean some people have forecasts and predictions outstanding about things like you know doing well on uh you know

**[1:26:43]** the informatics Olympiad and the math Olympiad and you know in the in the last few years uh when people tried to forecast the mmlu uh Benchmark which was having a lot of more sophisticated kind of you

**[1:26:57]** know like graduate students science kind of questions um yeah AI uh knocked that that down a lot faster than AI researchers who had registered and students who had registered forecasts on

**[1:27:10]** it uh and so if you if you're getting top-notch scores on you know graduate graduate exams um creative problem solving it yeah it's not obvious that that's sort of area will be a relative

**[1:27:24]** weakness of AI that in fact computer science uh is in many ways especially suitable because of getting up to speed with new areas being able to get rapid feedback from The Interpreter at scale but did you get rapid feedback if you're

**[1:27:42]** doing that something that's more analogous to research if you're like let's say you have a new model or something and it's like if we put in 10 million dollars on a mini trading run on this this would be a much better yeah

**[1:27:55]** for very large models those experiments are going to be quite expensive and so you're going to look more at like can you build up this capability by generalization uh from things like mini math problems programming problems

**[1:28:08]** working with small networks yeah yeah fair enough um I actually saw Scott Aronson was one of my professors in college um and I took his Quantum information class and I didn't do

**[1:28:19]** Abby I did okay in it but um he he uh he recently wrote a blog post where he said you know I had you before take my Quantum information test and it got a B and I was like damn I gotta see on the final so yeah yeah I've updated and um

**[1:28:33]** uh the direction that you know I get like you know like seems getting a view on the test like you probably understand Quantum information pretty well with different areas of strengths and weaknesses than the human students sure

**[1:28:42]** sure would it be possible for this sort of intelligence explosion to happen without any sort of Hardware progress if Hardware progress stopped would this feedback loop still be able to produce some sort of explosion with

**[1:28:56]** only software yeah so if we say that the the technology is frozen which I think is is not the case right now the yeah Nvidia has managed to deliver significantly better chips for AI workloads for the last few Generations

**[1:29:11]** uh h100 a100 V100 if if that stops entirely then what you're left with um and maybe we'll Define this as like no more nodes Moore's Law is over at that point the kind of gains you get and amount of compute available come

**[1:29:27]** from actually constructing more chips um and there are economies of scale you could still realize there so right now a chip maker has to amortize the r d cost of developing the chap and then the Capital Equipment is

**[1:29:44]** created like you build a Fab its peak profits are going to come in the few years when the chips it's making are at The Cutting Edge later on has a cost of compute exponentially Falls the you know you

**[1:29:58]** keep the Fab open because you can still make some money given that it's built um but of all of the profits the Fab will ever make right now they're relatively front loaded because when it's technology is near near The Cutting

**[1:30:10]** Edge so in a world where Moore's Law ends then you wind up with these very long production runs where you just you can keep making chips that stay at The Cutting Edge and where the r d costs

**[1:30:25]** get amortized over a much larger base so the r d basically drops drops out of the price and then you get some economies of scale from just making so many Fabs in the way that you know when we have the Auto industry expands and then this is

**[1:30:40]** in general across Industries when you when you produce produce a lot more uh costs fall because you have right now like asml has many you know incredibly exotic suppliers that make some bizarre part of

**[1:30:54]** the thousands of parts in one of these asml machines you can't get it anywhere else uh they don't have standardized equipment for their thing because this is the only only use for it and in a

**[1:31:06]** world where we're making 10 100 times as many uh chips at the current node then they would benefit from scale economies and all of that would become more uh mass production industrialized and so you could you combine all of those

**[1:31:21]** things and it seems like Capital costs of like buying a chip would decline but the energy cost of running the chip would not and so right now energy costs are a minority of the cost but they're not they're not they're not trivial you

**[1:31:37]** know they pass yeah they pass one percent a while ago um and they're you know they're inching up towards 10 and Beyond uh and so you can maybe get like another order of magnitude uh cost decrease uh

**[1:31:52]** from getting really uh efficient in the sort of Capital Construction but like energy would still would still be a limiting factor after the end of uh sort of actually improving the chips themselves got it good uh and when you

**[1:32:04]** say like there would be a greater population of AI researchers because are we using population as a sort of thinking tool of how they could be more effective or do you literally mean that the way you expect these um AIS to

**[1:32:16]** contribute a lot to research is by just having like a million copies of this of like a researcher thinking about the same problem or is it just like a useful thinking model for what it would look like to have a million times moderator

**[1:32:27]** AI working on that problem that's definitely a lower bound uh sort of model and often I'm meaning something more like effective population or like you'd need this many people to have this effect and

**[1:32:39]** so we were talking earlier about the trade-off between training and inference and in in board games and so you can get the same performance by having a bigger model or by calling the model more times and in general it's

**[1:32:54]** it's more effective to have a bigger smarter model and call it less timed up up until the point where the costs equalize between them and so we would be taking some of the gains of our larger compute on having bigger models that are

**[1:33:08]** individually more capable and there would be a division division of labor so like the tasks that were most cognitively demanding would be done by these giant models but some very easy task you don't want to expand that giant

**[1:33:20]** model if one one a model 1 100 is this the size can take that task and so larger models would be in the positions of like researchers and managers and they would have swarms of AIS of different sizes those tools that they

**[1:33:35]** could make API calls to and whatnot okay we accept the model and now we've gone to something that is at least as smart as Alias let's cover on all the tasks relevant to a progress and you can have so many copies of it what happens in the

**[1:33:49]** world now what are the next months or years or whatever timeline is relevant look like and so and to be clear um what what's happened is not that we have something that has all of the abilities and advantages of humans plus

**[1:34:03]** the AI advantages what we have is something that is like possibly by doing things like doing a ton of calls to make up for being individually less capable or something it's able to drive forward AI progress

**[1:34:17]** that process is continuing so AI progress has accelerated greatly in the course of getting there and so maybe we go from our eight month doubling time of software progress uh in effective compute uh to four months

**[1:34:32]** um or two months and so so there's a report uh by Tom Davidson at the open philanthropy project um which is by note of um

**[1:34:43]** work I had done previously and so um I advised and uh and and helped with that that project but Tom I really carried forward and produced a very nice uh report and model which Epoch is

**[1:34:57]** hosting uh you can plug in your own versions of the parameters um and there is a lot of work estimating uh the the parameter things like what's the rate of software progress what's the return to additional work how

**[1:35:12]** does performance scale at these tests as you as you boost the models and in general as we were discussing earlier they sort of like broadly uh human level in every domain with all the

**[1:35:28]** advantages is pretty pretty deep into that and so if already we can have an eight-month doubling time uh for software progress then by the time you get to that kind of uh point it's maybe more like four

**[1:35:45]** months two months um going going into one month and so if the thing is just proceeding at full speed then each doubling can come more rapidly

**[1:35:58]** and so we can talk about what are the spillovers of like so how's the models get more capable they can be doing other stuff in the world you know they can spend some of their time making Google search more

**[1:36:12]** efficient they can be you know hired as chat Bots with some inference compute and then we can talk about sort of if that intelligence explosion process is allowed to proceed then what happens is

**[1:36:27]** okay you you improve your software by a factor of two the demand the the efforts needed to get the next doubling are larger but they're not twice as large maybe they're like 25 35 larger

**[1:36:43]** uh so each one comes faster and faster until you hit limitations like you can no longer make further software advances with the hardware that you have um and looking at I think reasonable parameters in that model uh it seems to

**[1:37:01]** me if you have these giant training runs you can go very far and so the way I would see this play out is has the AIS get better and better at research they can work on different problems they can work on improving

**[1:37:15]** software they can work on improving Hardware they can do things like create new Industrial Technologies new energy technology they can manage robots they can manage human workers as like

**[1:37:27]** Executives and coaches uh and whatnot you can you can do all of these things and ai's wind up being applied where the returns are highest and I think initially the returns are especially high in doing more software

**[1:37:42]** and the reason for that is again if you improve the software you can update all of the gpus that you have access to um you know your your Cloud your Cloud compute is suddenly more potent if you

**[1:37:57]** design a new new chip design um it'll take a few months to produce uh the first ones and it doesn't update all of your old old chips so you have an ordering where you start off with the

**[1:38:12]** things where there's the lowest dependence on existing stocks and you can more just take whatever you're developing and apply it immediately and so software runs ahead you're getting

**[1:38:25]** more towards the limits of that software and I think that means things like having all the human advantages but combined with AI advantages and so we discussing I think that means

**[1:38:39]** given the kind of compute that would be involved if we're talking about this hundreds of billions of dollar trillion dollar training run there's enough compute to run tens of millions hundreds of millions of sort of like human scale

**[1:38:55]** mines they're probably smaller than human scale um to be like a similarly efficient at the limits of algorithmic progress because they have the advantage of a million years of education they have the

**[1:39:06]** other advantages we talked about you so you've got that wild capability and the software further software gains are running out uh or like they start to slow down again because you're just getting towards the limits of like you

**[1:39:21]** can't do any better than the best and so what happens then yeah um by the time they're running out have you already hit super intelligence or yes you're okay your your Wildlife we've loved the Galaxy

**[1:39:34]** just by having the abilities that humans have uh and then combining it with being very well focused and trained in the task beyond what any human could be and then running faster and such got it got it all right sorry continue yeah so I'm

**[1:39:47]** not I'm not going to assume that there's like huge qualitative improvements you can have I'm not going to assume that humans are like very far from the efficient Frontier of software except with respect

**[1:39:58]** to things like yeah we had limited lifespan so we couldn't train superintensively we couldn't incorporate other software um into our brains we can copy ourselves we couldn't run at fast speeds

**[1:40:11]** yeah so you've got all of those those capabilities um and now I'm skipping ahead of like the most important months in human history um and so I can talk about uh sort of

**[1:40:26]** you know what it looks like if it's just the AIS took over they're running things that they like uh how do things expand I can talk about things as how does this go um you know in a world where we've

**[1:40:43]** roughly or at least so far managed to um retain control of where these systems are going um and so by jumping ahead I can talk about how would this translate into the physical world and so this is something

**[1:40:57]** I think is a stopping point for a lot of people in thinking about well what would an intelligence explosion look like and they have trouble going from well there's stuff on servers and Cloud compute and oh that gets very smart but

**[1:41:11]** then how does what I see in the world change how does like industry or military power change if there's an AI takeover like what does that look like are there killer robots and so yeah so one course we might go

**[1:41:25]** down is to discuss um during that wildly accelerating transition how did we manage that uh how do you avoid it being catastrophic uh at another route we could go is how did the

**[1:41:41]** translation from Wild wildly expanded scientific r d capabilities intelligence on these servers translate into things in the physical world so you're moving along in order of like what has uh the quickest impact

**[1:42:00]** largely or like where you can have uh yeah an immediate intermediate change um so one of the most immediately accessible things is

**[1:42:13]** where we have large numbers of devices or artifacts or capabilities that are already AI operable with Milli you know hundred hundreds of millions equivalent researchers you can

**[1:42:28]** like quickly solve self-driving cars um you know make make the the algorithms much more efficient do great uh testing and simulation and then operate a large number of cars in parallel uh if you need to get some additional data to

**[1:42:46]** improve the simulation in recently and although you know in fact humans with quite little data uh are able to achieve human level driving performance so after you've really maxed out uh the

**[1:42:59]** easily accessible algorithmic improvements in this software-based intelligence explosion that's mostly happening on server Farms then you have you have mines that have been able to really perform on a lot of digital only

**[1:43:12]** tasks that they're doing great on video games they're doing great at predicting what happens uh next in a YouTube video If you have a camera that they can move they're able to predict what will happen at different angles humans do this a lot

**[1:43:28]** where we naturally move our eyes in such a way to get um images from different angles and different presentations and then predicting combined from that

**[1:43:37]** um and yeah and you can operate many cars Many Robots at once to get very good robot controllers so you should think that all the existing robotic equipment or remotely controllable equipment that is wired for

**[1:43:52]** that the areas can operate that quite well I think some people might be skeptical that existing robots given their current Hardware have their dexterity and the maneuverability to do a lot of

**[1:44:07]** physical labor that Indiana wanted to do do you have reason for thinking otherwise there's also not very many of them uh so production of sort of industrial robots is hundreds of thousands per year

**[1:44:17]** um you know they can do do quite a bit uh in place uh Eli musk is promising a a robot in the tens of thousands of humanoid rather than tens of thousands of dollars uh you know that may take a lot longer than uh he is sad as this

**[1:44:33]** happened with other Technologies but I mean that's a a direction to go but most immediately so hands are actually probably the most scarce thing um but if we consider what what do human

**[1:44:46]** bodies provide so there's the brain uh and in this situation uh we have now an abundance of high quality brain power that will be increasing has the AIS will have designed new Chips which will be rolling out from the tsmc factories and

**[1:45:02]** they'll have ideas and designs for the production of new Fab Technologies new nodes and additional Fabs but yeah looking around the body so there's legs to move around uh not only that necessary Wheels work pretty well

**[1:45:17]** being in a place you don't need most people most of the time uh in factory jobs and office jobs office jobs many of them can be fully uh virtualized um but yeah you some amount of legs Wheels other transport uh you have hands

**[1:45:33]** and hands um are something that are you know on the expensive end uh in robots we can we can make them they're made in very small production runs partly because we don't have the control software to use them

**[1:45:45]** well what in this world the Control software is fabulous and so people will produce much larger production runs of them over time possibly using technology we recognize possibly with quite different technology but just taking

**[1:46:00]** what we've got um so right now the robot arm uh industry industrial robot industry produces hundreds of thousands of machines a year um some of the the nicer ones are like

**[1:46:13]** fifty thousand dollars uh in aggregate the industry has tens of billions of dollars of Revenue by comparison the automobile industry uh produces like I think over 60 million cars a year it has revenue of over two trillion dollars per

**[1:46:30]** annum and so converting that production capacity over towards robot production would be one of the things if they're not something better to do would be one of the things to do and in World War II

**[1:46:46]** um you know industrial conversion of American industry uh took place over several years uh and really amazingly um you know ramped up military production uh by converting existing civilian industry

**[1:47:02]** and that was without the aid of superhuman intelligence and management at every step in the process so yeah every part of that would be very well well designed you'd have

**[1:47:16]** AI workers who understand stood every part of the process and could direct human workers even in a in a a fancy Factory most of the time uh it's not the the hands doing a physical motion

**[1:47:32]** uh that a worker is being paid for they're often like looking at things or like deciding deciding what to change the the actual the time spent in manual motion uh is a limited portion of that and so

**[1:47:45]** in this world of abundant AI cognitive abilities where the human workers are more valuable for their hands than their heads then you could have

**[1:47:57]** a worker even a worker previously without training and expertise in the area who has a smartphone maybe a smartphone on a on a headset and we have billions of smartphones which have eyes and ears

**[1:48:10]** and methods for communication for an AI to be talking to a human and directing them in their physical motions with skill as a a guide and coach that is beyond any human there could be a lot better at telepresence and remote

**[1:48:27]** work and they can provide VR and augmented reality guidance as to to help people get better at doing the physical motions uh that they're providing in the construction so you convert

**[1:48:39]** you convert the Auto industry to robot production if it can produce an amount of of mass of machines that is similar to what it currently produces that's enough for you know

**[1:48:53]** billion billion human-sized robots a year the the value per uh per kilogram of of cars uh somewhat uh less than high-end robots but

**[1:49:09]** um yeah you're also cutting out most of the wage bill because most of the wage bill is payments ultimately to like human capital and education not to the physical hand motions um and you know lifting objects and and

**[1:49:23]** that that sort of task yeah so at the sort of existing scale of the audio Industries you can make a billion robots a year at the auto industry is two or three percent of the existing economy you're replacing

**[1:49:34]** these these cognitive things so if if right now physical hand motions are like 10 of the work um redirect humans into those tasks and you have like in the World At Large

**[1:49:49]** right now um mean income is on the order of ten thousand dollars a year but in rich countries skilled workers uh earn more than a hundred thousand per year and some of that is just like you know

**[1:50:02]** it's not just management roles of which only a certain proportion of the population can have but just being an absolutely um you know exceptional Peak and human performance

**[1:50:14]** of some of these construction and and so trolls yeah just raising productivity to match the most productive workers in the world um you know is is room to make uh a very

**[1:50:30]** very big gap and with AI replacing skills that are scarce in many places where there's you know abundant uh currently low wage labor you bring in the AI coach and someone who is previously making very

**[1:50:45]** low wages can suddenly be super productive by just being the hands for an AI and so you know on a naive view if you ignore the delay of capital adjustment of like building new tools

**[1:50:59]** for the workers say like yeah just like raise typical productivity uh for workers around the world to be more like rich countries um and get 5x 10x like that get more productivity by with AI handling the

**[1:51:19]** difficult cognitive tasks reallocating people from like office jobs to providing physical motions and since right now that's a small proportion of the economy you can expand this sort of hands for manual labor by like an order

**[1:51:34]** of magnitude like within a rich country by just because most people are sitting are sitting in an office or even in a factory floor or not continuously moving uh so you've got billions of hands flying around in humans

**[1:51:48]** could be used in the course of constructing earwaves of robots and now once you have a a quantity of robots that is approaching the human population and they work 24 7 of course

**[1:52:03]** um the human labor will no longer be valuable his hands and legs but at the very beginning of the transition just like new software can be used to update all of the gpus to run the latest AI humans are sort of Legacy population

**[1:52:20]** which with an enormous number of underutilized hands and feet uh that the AI can use for the initial robot construction cognitive tasks are being automated and the production of them is greatly expanding and then the

**[1:52:35]** physical tasks which complement them are utilizing humans to do the parts that robots that exist can do is the implication of this that you're getting to that you know World production would increase just a tremendous amount or

**[1:52:47]** that yeah I could get a lot done of whatever motivations it has or yeah so there's an enormous increase in production uh for humans who just switching over to the role of providing hands and feet

**[1:53:02]** um for AI where they're limited and this robot industry is a natural uh place to apply it and so if you go to something that's like 10x the size of like the current car industry in terms of its uh in terms of

**[1:53:17]** its production which would still be like a third of our current economy and the aggregate productive capabilities of the society with AI support are going to be a lot larger they make 10 billion humanoid robots a year and then

**[1:53:31]** I mean if you do that uh you know the the Legacy population of a few billion human workers uh is no longer very important for the physical tasks and then they the new automated industrial base can just

**[1:53:46]** produce more factories produce more robots and then the interesting thing is like what's the doubling time how long does it take for a set of computers robots factories and supporting equipment to produce another equivalent

**[1:54:03]** quantity of that for gpus brains uh this is really really easy really solid there's an enormous uh margin there we're we're talking before about um yeah skilled human workers uh getting paid a hundred dollars an hour uh is

**[1:54:20]** like quite uh quite normal in developed countries for very in-demand skills um and you make a GPU uh that can do that work

**[1:54:33]** right now these gpus are like tens of thousands of dollars if you can do a hundred dollars uh of wages each hour than in you know in a few weeks uh you pay back your costs if the thing is more productive and as we

**[1:54:53]** were discussing you can be a lot more productive than a sort of a typical high-paid human professional by being like the very best human professional and even better than that by having a million years of education and working

**[1:55:04]** all the time yeah then you could get even shorter payback times uh like yeah you can generate the dollar value of like the cost initial cost of that equipment

**[1:55:16]** within a few weeks for robots so like a human factory worker uh can earn 50 000 uh dollars a year you know really top-notch Factory workers earning earning more and working working all the time if they can produce a few hundred

**[1:55:34]** thousand dollars of value per year and buy a robot that costs fifty thousand to replace them then you know that's that's a payback time of some some months that is about the financial return yeah and

**[1:55:49]** we're going to get to the uh because those are going to diverge in this scenario right yeah because right now because it seems like it's going to be a given that like all right these super intelligent zombies gonna be able

**[1:55:59]** to make a lot of money um it could be like very valuable can you like physically scale up what we really care about are like the actual physical operations that a thing does yeah how much do they

**[1:56:10]** contribute to these these tasks um and I'm using this as a as a start uh to try and uh get back to the physical replication times but so I guess I'm wondering what is the implication of this because I think you started off

**[1:56:24]** this by saying like people have not thought about what the physical implications of superintelligence would be what is the bigger uh takeaway what are we wrong about when we think about what the world will look like with super

**[1:56:35]** diligence with robots that are optimally operated uh by AI so like extremely finely operated and with building technological designs and equipment and Facilities under AI Direction how much

**[1:56:51]** can they produce for for doubling any of the AIS to produce stuff that is uh in aggregate at least equal uh to their to their own cost

**[1:57:05]** uh and so now we're pulling out these things like labor costs uh that no longer apply and then trying to zoom in on like what these these Capital costs will be you're still going to need the raw

**[1:57:16]** materials you're still going to need the the robot time building the next robot I think it's pretty likely that with the advanced AI work that can design some incremental improvements with the industry scale up that you can get

**[1:57:29]** tenfold and better cost reductions on um you know on the system by making things more efficient and replacing the human human cognitive labor and so maybe that's like you need five thousand dollars of yeah of of costs under our

**[1:57:49]** sort of current environment but the the big change in this world is we're trying to produce this stuff faster if we're asking about the doubling time of the whole system and say one year

**[1:58:03]** if you have to build a whole new Factory to like double everything you don't have time to amortize the cost of that factory like right now you might build a factory and use it for 10 years and like buy some equipment and use it

**[1:58:16]** for five years and so that's part of your that's your Capital cost and you know on an accounting context you know you depreciate each year a fraction of that Capital purchase

**[1:58:27]** but if we're trying to double our entire industrial system in one year then those Capital costs have to be multiplied so if we're going to be getting most of the return on our effector in the first

**[1:58:41]** year instead of 10 years waited waited appropriately then we're going to say okay our Capital cost has to go up by tenfold because I'm building an entire Factory

**[1:58:53]** for this year's production I mean it will do more stuff later but it's most important early on instead of over 10 years and so that's going to raise

**[1:59:05]** the costs of that reproduction and so and seems like going from you know current like decade kind of cycle of amortizing factories and and Fabs and whatnot and shorter for some things

**[1:59:20]** um the longest are things like big buildings and such yeah that could be like a 10-fold increase from moving to a double the physical stuff each year uh in capital costs and given the savings that we get

**[1:59:33]** in the story from scaling up the industry from removing the payments to human cognitive labor uh and then from just adding new technological advancements and like super high quality cognitive supervision

**[1:59:46]** like apply more of it than was applied today and it looks like you can get cost reductions that offset that increased capital capital cost so that like you know your your fifty thousand dollar improved robot arms uh

**[2:00:02]** or industrial robots it seems like that can do the work of a human factory worker uh so it would be like the equivalent of hundreds of thousands of dollars uh and like yeah they would you know by default they cost more than the

**[2:00:16]** fifty thousand dollar um arms today but then you apply all these other cost savings and it looks like then you get a period a robot doubling time that is less than a year I think significantly less than a year as

**[2:00:30]** you get into it uh so in this first first phase you have humans under AI Direction and like existing robot industry and converted Auto industry and expanded facilities making robots

**[2:00:46]** those over less than less than a year you've produced robots until they're combined production is exceeding that of like humans has armed arms and feet and then yeah you could have over a period Then

**[2:01:01]** with a doubling time of months um or less sort of clanking replicators robots as we understand them growing and then that's not to say that's the the limit of like the most that technology could do

**[2:01:18]** because biology is able to reproduce at faster rates and maybe we're talking about that in a moment but if we're trying to like restrict ourselves to like robotic technology because we understand it and sort of cost Falls

**[2:01:31]** that are reasonable from eliminating all labor massive industrial scale up and sort of historical kinds of technological improvements that lowered costs I think yeah you can get into a robot population industry uh doubling in

**[2:01:46]** months got it okay and then what is the implication of the biological doubling times and I guess this doesn't have to be a biological but you know you can have like you can do like uh you know Drexler

**[2:01:58]** like first principles how much would it cost to if you built a nanotech uh thing that like built more Nanobots I certainly take the human brain and other biological brains is like very relevant data points about what's possible with

**[2:02:10]** Computing and intelligence like with the reproductive capability of biological uh plants and animals and uh microorganisms I think is is relevant as I like this is you know you it's possible to for systems to reproduce at

**[2:02:25]** least this fast and so at the extreme you have bacteria that are heterotrophic so they're feeding on some abundant external food source and ideal conditions um and there's some that can divide like

**[2:02:37]** every 20 or 60 minutes so obviously that's absurdly absurdly fast that seems on the on the low end because ideal conditions require actually setting them up there needs to be

**[2:02:50]** abundant energy there um and so if you're actually having to acquire that energy by building solar panels um or like uh burning combustible materials or whatnot and then the

**[2:03:04]** physical equipment to produce those ideal conditions can be a bit slower cyanobacteria which are self-powered from solar energy the really fast ones in ideal conditions can you know double in a day a reason why cyanobacteria

**[2:03:21]** isn't like the food source for uh everyone and everything uh is it's hard to ensure those ideal conditions and then to extract them from the water I mean they do of course power The Aquatic ecology uh but they're like

**[2:03:34]** they're floating uh they're floating in liquid um getting resources that they need to them and out is tricky and then extracting uh extracting your product but like yeah one day doubling times are

**[2:03:47]** possible um powered by the Sun and then if we look at things like insects um so fruit flies can have hundreds of Offspring in a few weeks you extrapolate that over a year and you just fill up

**[2:04:03]** anything anything accessible certainly expanding a thousand fold right now Humanity uses less than one one thousandth of the solar energy or the heat on envelope of the Earth certainly you can get done with done

**[2:04:17]** with that in a year if you can ex reproduce at that rate your industrial base and then even an interestingly with the uh with the Flies uh they do have brains they have a significant amount of of

**[2:04:32]** computing substrate and so there's something of a pointer to well if we could produce computers in ways as efficient as the construction of brains then we could produce computers very effectively and then the

**[2:04:44]** big question about that is the kind of of brains that get constructed biologically uh they sort of grow randomly and then are configured in place it's not obvious you would be able to make them have an ordered structure

**[2:04:58]** like a top-down computer chip that would let us copy data into them and so something that where you can't just copy your existing AIS and integrate them is going to be less valuable than a GPU what are the things you couldn't copy a

**[2:05:14]** brain grows yeah um by cell division and then random connections are formed got it got it um and so every so every brain is different and you can't rely on just yeah we'll just copy this file into the brain for

**[2:05:29]** one thing there's no input output for that you need you need to have that but also like the the structure is different so you can't you wouldn't be able to copy things exactly whereas when we make we make a CPU or GPU

**[2:05:42]** um they're designed incredibly finely and precisely and reliably they break with you know incredibly tiny imperfections and they are set up in such a way that we can input large amounts of data copy a file and have the

**[2:05:55]** new GPU run an AI just as capable as any other whereas with you know a human child they have to learn everything from scratch because we can't just like like connect them to a fiber optic cable and they're immediately a productive adult

**[2:06:07]** so there's no genetic problem like you can just directly get this yeah and yeah you can you can share the benefits of these giant training runs and such and so that's a question of like how if you're growing stuff using biotechnology

**[2:06:20]** how you could sort of effectively copy and transfer data and now you mentioned sort of Eric drexler's ideas about um creating non-biological uh nanotechnology sort of artificial chemistry that was able to

**[2:06:36]** use covalent bonds um and produce in some ways have a more uh industrial approach to molecular objects now there's controversy about like will that work how effective would it be if

**[2:06:50]** it did um and certainly if you if you can get things however you do it that are like unto but biology in their reproductive ability but can do can do Computing or like

**[2:07:03]** be connected to outside Information Systems then that's pretty pretty tremendous you can you can produce physical manipulators and compute at ludicrous speeds and there's no reason to think in principle

**[2:07:18]** they couldn't right in fact in principle we we have every reason to think they could there's like the reproductive abilities absolutely yeah because even like nanotech right because biology does that yeah they're sort of challenges to

**[2:07:33]** uh the sort of the practicality of the necessary uh chemistry yeah I mean my my bet would be that we can move Beyond biology in some important ways for the purposes of this discussion I think it's it's better not to lean on

**[2:07:48]** that because I think we can get to many of the same uh conclusions on things that just are are more uh universally accepted the bigger point being that very quickly once you have super intelligence you could get to a point

**[2:08:02]** where the Thousand X greater energy profile that the sun makes available to the Earth is a great portion of it is used by the AI it can rap by the civilization sure empowered by it and that could be an a that could be a an AI

**[2:08:19]** civilization or it could be a human AI civilization it uh it depends on how well we manage things and what the underlying state of the world is yeah okay so let's talk about that should we start at when we're talking about how

**[2:08:30]** they could take over is it best to start at um a sort of subhuman intelligence or should we just talk at we have a human level intelligence and the Takeover or the lack thereof is uh how that would

**[2:08:41]** happen to me and different people might have somewhat different views on this but for me when I am concerned about either sort of outright destruction of humanity or

**[2:08:58]** um an unwelcome AI takeover of civilization um most of my the scenarios I would be concerned about pass through a process of AI being applied to improve AI capabilities and expand and so

**[2:09:17]** this process we were talking earlier about where AI research is automated you get to you know effectively research Labs companies a scientific Community running within the server Farms of our Cloud compute so open has been usually

**[2:09:33]** turned into like a program like a closed circuit yeah yeah and with like a large fraction of the world's compute probably going into whatever training runs and AI societies um that there be economies of scale

**[2:09:46]** because if you put in twice as much compute in this AI research Community goes twice as fast um you know that's a lot more valuable than having two separate training runs there would be some tendency to

**[2:09:59]** bandwagon uh and so like if you know you have some some small startup um you know even if they make an algorithmic improvement uh running it on 10 times 100 times or two times if it's like you're talking about say Google and

**[2:10:15]** Amazon teaming up I'm actually not sure which what the uh the precise ratio of their Cloud resources is since this sort of really these interesting intelligence explosion impacts come from the Leading Edge there's a lot of value in not

**[2:10:29]** having separated wallet Garden ecosystems and having the the results being developed by these AIS be shared have training larger training runs be shared okay so and so I'm imagining this is something like

**[2:10:43]** you know some very large company uh or Consortium of companies likely with you know a lot of sort of government interest and supervision possibly with Government funding yeah producing uh this enormous AI Society in their their

**[2:11:01]** Cloud which is doing all sorts of you know existing kind of AI applications and jobs as well as these internal r d tests and so this point somebody might say this sounds like a situation that would be good from a takeover

**[2:11:15]** perspective because listen if they if it's going to take like tens of billions of dollars worth of compute to continue this training for this AI Society it should not be that hard for us to pull the brakes if needed as compared to

**[2:11:29]** I don't know something that could like run on a very small like single CPU or something yeah yeah okay so uh how how would it you know it's like there's an AI Society uh that is a result of these training rides and now we can it is the

**[2:11:42]** power to improve itself on these servers would we would be able to stop it at this point and what does a um a sort of attempt yeah a takeover look like uh we're skipping over why that might happen

**[2:11:55]** um for that I'll just briefly uh refer to incorporate by reference um you know the some discussion by my open philanthropy uh colleague um she has a a piece about I think it's called something like

**[2:12:13]** the the default let's put the the default outcome of training AI on our without specific with that specific countermeasures um default outcome and say I take over and but yes uh so explore how basically

**[2:12:26]** we are training models that for some reason vigorously uh pursue a higher reward or lower loss and that can be because they wind up with some motivation where they want reward

**[2:12:40]** um and then if they had control of their own uh training process uh they can ensure that it could be something like they develop a motivation around a sort of extended concept of reproductive Fitness

**[2:12:54]** um not necessarily at the individual level uh but over the generations of training tendencies that tend to propagate themselves um sort of becoming more common and it could be that they have some sort of

**[2:13:09]** goal in the world which is served well um by performing very well on the training distribution but the Tendencies do you mean like power speaking Behavior or yeah so it so an AI that behaves well on the training distribution because say

**[2:13:26]** it wants it to be the case that its Tendencies wind up being preserved or selected by the training process well then like behave to try and get a very high reward um or low loss be propagated but you can

**[2:13:44]** have other motives that go through the same behavior because it's instrumentally useful so I mean an AI that is interested in say having a robot take over because it will like change some property

**[2:13:58]** of the world then has a reason to behave well on the training distribution um not because it values that intrinsically but because if it behaves differently then it will be changed by gradient descent and no longer you know

**[2:14:12]** its goal is less likely to be pursued and that doesn't necessarily have to be that like this AI Will Survive because it probably won't ai's are constantly spawned and deleted on the servers and like the new generation proceed but if

**[2:14:24]** an AI that has a very large General goal that is affected by these kind of macro scale processes could then have reason to over this whole range of training situations behave well and so this is this is a way

**[2:14:37]** in which we could have ai's trained that develop internal motivations such that they will behave very well in this training situation where we have control over their reward signal and

**[2:14:50]** their like physical computers um and basically if if they act out they will be changed and deleted their goals um will be altered until there's something that does behave well but

**[2:15:05]** they behave differently when we go out of distribution on that when we go to a situation where the AIS by their choices can take control of the reward process they can make it such that we no longer have power of them

**[2:15:21]** Holden uh who you had on uh previously uh mentioned like the the King Lear problem where King Lear offers uh rulership of his kingdom to the daughters that uh sort of you know loudly flatter him and Proclaim their

**[2:15:41]** devotion and then once he has transferred irrevocably the power over his kingdom he finds they treat him very badly because the factor of shaping their behavior uh to be kind to him when

**[2:15:57]** he had all the power uh it turned out that they internal motivation that was able to produce the behavior that won the competition actually wasn't interested

**[2:16:09]** out of distribution and being loyal when there was no longer an advantage to it and so if we wind up with this situation where we're producing these millions of AI instances tremendous capability they're all doing

**[2:16:22]** their jobs very well initially but if we wind up in a situation where in fact uh they're generally motivated to if they get a chance take control from humanity and then would be able to pursue their own

**[2:16:38]** purposes and at least and sure they're given the lowest loss possible uh or have whatever um motivation they attach to in the training process even if that is not what we would have liked and we may have

**[2:16:52]** in fact actively trained that like if an AI that had a motivation of always be honest and obedient and loyal to a human if there are any cases where we mislabel things say people don't want to hear the truth about their religion or polarized

**[2:17:08]** political topic or they get confused about something like the Monty Hall problem which is a problem that many people famously famously are confused about in statistics in order to get the best reward the AI

**[2:17:21]** has to actually manipulate us or lie to us or tell us what we want to hear and then the internal motivation of like always be honest to the humans we're going to actively train that away versus the alternative motivation of

**[2:17:37]** like be honest to the humans when they'll catch you if you lie and object to it and give it a low reward but lies in the humans when they will give that a high reward so how do you make sure it's not the uh the thing it learns is not to

**[2:17:52]** manipulate us into giving it rewarding it when we catch it not lying but rather to universally be aligned yeah I mean so this is the tricky I mean has Jeff Hinton was recently saying um there is no currently no known solution for this

**[2:18:10]** um what do you find most promising yeah General directions that people are pursuing is one you can try and make the training data better and better uh so there's fewer situations uh where like the dishonest generally

**[2:18:24]** generalization is favored and create as much as you can situations where the dishonest generalization is likely to slip up so if if you if you train in more situations

**[2:18:39]** where yeah even like quite a complicated deception gets caught uh and even in situations where that have been actively designed to look like you could get away with it but really you can

**[2:18:52]** um and these would be like adversarial examples uh and adversarial training do you think that would generalize to when it isn't a situation where we couldn't plausibly catch it and it knows we couldn't plausibly it's not it's not

**[2:19:03]** logically necessary uh it's possible uh no that it has we apply that selective pressure you'll wipe away a lot of possibilities so like if you an AI that has a habit of just sort of compulsive pathological

**[2:19:17]** line that will very quickly get noticed and that motivation system will get hammered down um and you know you keep doing that but you'll be left with still some distinct motivations probably that are compatible

**[2:19:30]** so like an attitude of always be honest unless you have a super strong inside view that checks out lots of mathematical consistency checks uh that yeah really absolutely super duper for

**[2:19:46]** Real uh this is a situation where you can get away yeah yeah uh with some sort of shenanigans that you shouldn't that motivation system is like very difficult uh to distinguish from actually be honest because the conditional the

**[2:20:01]** conditional and firing most of the time if it's it's causing like mild distortions and situations of telling you what you want to hear or things like that we might not be able uh to pull it out

**[2:20:12]** but maybe we could and human like humans are trained with simple reward functions uh things like the sex drive um food social imitation of other humans and we wind up with attitudes uh

**[2:20:31]** concerned with the external World although isn't the famously of the argument that these Revolution people people use condoms yeah um like you know the the richest uh most educated humans have sub replacement

**[2:20:44]** fertility on the whole or at least at a national cultural level um so there's a sentence in which like yeah Evolution uh often fails in that respect um and even more importantly like at the

**[2:20:59]** neural level so people have Evolution has implanted uh various things to be rewarding and reinforcers and we don't always pursue even those um and people can wind up uh in different uh

**[2:21:14]** consistent equilibria um or different like behaviors where they going quite different directions you have some humans who go from those from that in a biological programming to like have children others have no

**[2:21:28]** children you know some people go to great efforts to survive so why are you more optimistic um or are you more optimistic that then that kind of training in

**[2:21:41]** four years will produce a drives that we would find favorable does it have to do with the original point we're talking about with intelligence and evolution where since we are removing many of the disabilities of evolution with regards

**[2:21:53]** to intelligence we should expect intelligence to Revolution be easier is there a similar reason to expect alignment through uh gradient descent to be easier than alignment through Revolution yeah so in in the limit

**[2:22:04]** if we have positive reinforcement for certain kinds of food sensors triggering the stomach negative reinforcement for certain kinds of nociception and yada yada in the limit the sort of Ideal

**[2:22:20]** motivation system to have for that would be a sort of wire heading so this would be a mind uh that just like hacks and Alters those predictors and then all of those of those systems are recording everything is great

**[2:22:38]** Some Humans claim to have that or have it at least has one portion of their of their aims so like the idea of I'm going to pursue pleasure as such even if I don't get actually get food or these other reinforcers if I just like

**[2:22:55]** wirehead or take a drug yeah to induce that that can be motivating because if it was correlated with reward in the past that like the idea of oh yeah pleasure that's correlated with these it's a

**[2:23:09]** concept that applies to these various experiences that I've had before which coincided with the biological reinforcers and so thoughts of like yeah I'm going to be motivated by Pleasure can get developed in a human

**[2:23:21]** but also plenty of humans say no I wouldn't want to wirehead or I wouldn't want nozick's experience machine I care about real stuff in the world and then in the past having a motivation of like

**[2:23:33]** yeah I really care about say my child I don't care about just about feeling that my child is good or like not having heard about their suffering or their their injury because that kind of attitude in the past

**[2:23:51]** tended to cause Behavior Uh that would negatively rewarded or that was predicted to be negatively rewarded and so there's a sense in which okay yes our underlying reinforcement learning

**[2:24:04]** Machinery wants to wirehead but actually finding that hypothesis is challenging and so we can wind up with a hypothesis or like a motivation system like no I don't want a wirehead I don't want to go into the experience

**[2:24:19]** machine I want to like actually protect my loved ones uh even though like we can know yeah if I tried the super wire heading machine then I would wirehead all the time or if I tried you

**[2:24:33]** know super duper Ultra heroine uh you know some hypothetical thing that was directly and you know very sophisticated fashion and hacking your reward system you can know yeah then I would change my behavior Ever After but right now I

**[2:24:47]** don't want to do that because the heuristics and predictors that my brain has learned you don't want to get it yeah all right short circuit that process of updating they want to not expose the Dumber predictors in my brain

**[2:25:02]** that would update my behavior in those ways would uh so in this metaphor is alignment not wireheading because you can like I don't know if you include like using condoms as wire heading or not so the the AI that is always honest

**[2:25:16]** even when an opportunity arises where it could lie um and then hack the servers that's on and that leads between AI takeover and then it can have it's lost set to zero that's in

**[2:25:30]** some sense it's like a failure of generalization it's like the AI has not optimized the reward in this new circumstance so like human values like success successful human values is successful they they are themselves

**[2:25:46]** involve a misgeneralization not just at the level of evolution but at the level of neural reinforcement and so that indicates it is possible to have a system that doesn't automatically go to this optimal

**[2:26:02]** Behavior and the limit and so even if and ajaya's post she talks about like the training game an AI that is just playing the training game uh to get reward or void loss avoid being changed

**[2:26:13]** that attitude yeah it's one that could be developed but it's not necessary there can be some substantial range of situations that are short of having Infinite Experience of

**[2:26:25]** everything including experience of wire heading uh where that's not the motivation that you pick up and we could have like an empirical science if we if we had the opportunity

**[2:26:36]** to see how different motivations are developed short of the infinite limit like how it is that you wind up with some humans uh being enthusiastic about the idea of wire hiding and others not and you could do experiments with AIS to

**[2:26:53]** try and see well under these training conditions after this much training of this type and this much feedback of this type you wind up with such and such a motivation so like I can find like if I add in more

**[2:27:08]** of these cases where there are like tricky adversarial questions designed to try and trick the AI into line um and then you can you can ask how does that affect the generalization in other situations it's very difficult to study

**[2:27:26]** and it works a lot better if you have interpretability and you can actually read the ai's Mind by understanding its weights and activations but like it's not determined the motivation and AI will have at a given point in the

**[2:27:41]** training process by what in the infinite limit the training would go to and it's possible that if we could understand the insides of these Networks we could tell uh yeah this motivation

**[2:27:54]** has been developed by this training process and then we can adjust our training process to produce these motivations that legitimately want to help us and if we

**[2:28:05]** succeed reasonably well at that then those AIS will try to maintain that property as an invariant and we can we can make them such that they're relatively motivated to like tell us if they're having uh thoughts about uh you

**[2:28:21]** know have you have you had dreams about an AI takeover of humanity today and it's just a it's a standard practice uh that they're they're motivated to do to be transparent in that kind of way and so you could add a lot of features like

**[2:28:36]** this that restrict uh the kind of takeover scenario and there's not not to say this is this is all easy and requires developing and practicing methods we don't have yet but that's the kind of general direction you could go

**[2:28:50]** um so you you of course know eliezer's arguments that something like this is implausible with modern gradient descent techniques because we I mean with interoperability we can like barely see what's happening with a

**[2:29:02]** couple of neurons and you know what what is like the internal State there let alone when you have uh sort of like an embedding dimension of like tens of thousands or bigger how you would be able to catch

**[2:29:16]** what exactly is the incentive whether it's the where there's a model that is generalized don't lie to humans well or whatever whether it isn't do you yeah do you have some sense of why you disagree with somebody like

**[2:29:27]** Elias or on how plausible this is why it's not impossible basically I think I think they're actually um a couple of places it's something it's something difficult because although this argument is not

**[2:29:40]** um it's not fully explicit but uh he's he's been doing more lately I think that it's helpful um in that direction but so I'd say with respect to interpretability I'm relatively optimistic that the

**[2:29:54]** equivalent of like an AI lie detector um is something that's possible and the internal and so initially the internals of an AI are not optimized by at least by gradient descent uh

**[2:30:12]** absent gradient hacking to be impenetrable they're not designed to be resistant uh to an examination of the weights and activations showing what the AI thinking in the same way that like in our brains

**[2:30:27]** when circuits develop uh in our lives those circuits have not been shaped to be resistant to some super fmri being able to infer our behavior from them although although it's in the implication of the superposition stuff

**[2:30:40]** that in fact it is you're not gonna sorry this is inside baseball for the audience but basically you can't cleanly infer what uh what quality a single neuron stands for so it could be like a single neuron could be like this algebra

**[2:30:54]** is about Alexander the Great or this neuron is about my desire to conquer the world things can have multiple um you know multiple directions and interactions and so it's not as easy as just like oh yeah this is the neuron

**[2:31:08]** that always fires uh in cases of of deception um but the thing that makes me relatively optimistic here with respect to interpretability is that I think we can have reasonably

**[2:31:23]** robust experimental feedbacks um on a lot of these things and oh the the kind of the kind of setup um that I would be interested in is so you have an AI

**[2:31:38]** that is trained and rewarded for communicating to some audience maybe a human maybe another AI model um that like some claim uh is true or false like say that

**[2:31:56]** um you know a particular you know this can be from some past data particular company will succeed or fail um you could be like token prediction uh it could be like

**[2:32:07]** this computer program does not have a back door uh which if run in the servers could be used for an AI takeover um so they're like lots of of claims true and false um that you could train AIS to use their

**[2:32:21]** best efforts to advocate for and you can do that on things where you're later going to have a ground truth you're going to know in fact is there

**[2:32:33]** a back door uh in this program because you're where you're training and rewarding the AI for successfully slipping a back door through you also give it a penalty for being caught uh and so doing this kind of thing you

**[2:32:46]** can you can draw out at like a large generated data set on demand of this is what an AI putting forth its best efforts to

**[2:33:01]** pass through some deception to put a back door in some program this is what it looks like and we think it's it's doing its best efforts because we've trained it for that and like gradient descent if

**[2:33:13]** there's any immediate way to adjust its performance to do better gradient descent will apply that you can you can talk about ways in which uh maybe gradient descent um there could be subverted but I think

**[2:33:26]** it's not the most likely case that that really breaks things hard yeah I guess before we get into the details on this the the thing about maybe we want to address the layer above in the stack which is okay suppose

**[2:33:42]** this generalizes well into the early AIS the gpd6s and um okay so now we have kind of aligned gpt6 that is the precursor to the feedback loop in which EI is making itself smarter at some point they're

**[2:33:58]** going to become like super intelligent they're going to like see their own you know Galaxy brain uh and you know if they're like I don't want to be aligned with the humans they can like change it so at this point

**[2:34:09]** well what do we do with the alliance gpt6 so that the super intelligence that we eventually develop is also aligned to humans are pretty unreliable yeah if you get to a situation where you have AIS who are aiming at roughly the same thing

**[2:34:26]** as you at least as well as having humans do a thing you're in pretty good shape I think and there are ways uh for that situation to be to be relatively stable

**[2:34:40]** uh so like we can you can look ahead and see experimentally how changes are altering Behavior where each step is like a modest increment and so AIS that have not had that change uh made to them I

**[2:34:56]** get to supervise and monitor and see exactly how does this affect uh the experiment the experimental area so if you're sufficiently on track with earlier systems that are capable cognitively of representing a kind of

**[2:35:12]** robust procedure then I think they can handle the job of incrementally improving the stability of the system so that it rapidly uh converges to something that's quite stable um but the question is more about

**[2:35:28]** getting to that point in the first place and so Elias are will say that like well if we had human brain emulations uh that would be pretty good something much better than his current view of us being almost certainly doomed

**[2:35:44]** um I think yeah I thought we would have we'd have a good shot with that and so if we can get to the um human human-like mind with like rough enough human supporting aims

**[2:36:00]** remember that we don't need to be like infinitely perfect because I mean that's a higher that's a higher standard than brain emulation there's a lot of uh of noise and variation among the humans yeah it's a relatively finite standard

**[2:36:12]** it's not godly superhuman although a AI that was just like a human human with all the human advantages with AI advantages as well as we said is enough for intelligence explosion and sort of wild

**[2:36:25]** superhuman capability if you Crank It Up um and so it's very dangerous to be at that point but it's not you don't need to be working with a a Godly super intelligent AI to make something

**[2:36:40]** that is the equivalent of human emulations of like this is like a very very sober very ethical uh human who is like committed to a project of not seizing power for themselves and of contributing

**[2:36:56]** to like a larger legitimate process that's that's a goal you can aim for getting an AI that is aimed at doing that and has strong guard rails against the ways it could easily deviate from that so things like

**[2:37:11]** uh being averse to deception being averse to using violence and there will always be you know loopholes and ways in which you can imagine an infinitely intelligent thing getting around those but if you

**[2:37:25]** install additional guardrails like that fast enough they can mean that you're able to succeed at the project of making an aligned enough AI certainly an

**[2:37:39]** AI that was better than a human brain emulation before the project of AI is in their spare time or when you're not looking or when you're unable to appropriately supervise them and it gets

**[2:37:52]** around any down to logical prohibitions they may have take over and overthrow the whole system do you have a race between on the one hand the project of getting strong

**[2:38:03]** interpretability and shaping motivations that are roughly aiming at making this process go well and that have guard rails uh that will prevent like small deviations from exploding

**[2:38:16]** and on the other hand these AIS in their spare time or in ways that you don't perceive or monitor appropriately or they're only supervised by other AIS who conspire

**[2:38:28]** make the AI takeover happen and I guess we'll talk later about how that happens are these different AIS that are doing the race or is it just like different capabilities of the same AI the defining like what is what is a separate AI is

**[2:38:42]** tricky so like and we talk about gpt4 yeah yeah um and there are many instances of gpt4 on the servers at any given time and there are versions that have been fine-tuned uh to different purposes

**[2:38:56]** they don't necessarily have to be be separate so like gpt4 does work as a preference model where it's like predicting how humans will evaluate things and it also does work like giving answers that are

**[2:39:13]** evaluated as good by the preference model um I know you can say these are not separate in the sense that like well if they underline uh you know pre-trained or the early

**[2:39:24]** training GPT was like harboring a desire to conspire uh for an AI takeover than both the uh you know who's watching the Watchers the Watchers may also have um have the same motivation if you have a setup where humans have no

**[2:39:41]** hard power if the AIS conspired um all of the Safety and Security mechanisms involve AIS watching other AIS then they have the potential to just like well we'll all walk off the job at the same time

**[2:39:56]** if they're able to coordinate uh and so that's a failure mode if humans still have the hard power though if still you have situations where humans are looking at some of the actual outputs

**[2:40:10]** that are produced then they can apply gradient descent to be well every time a human looks at it things have got to be pretty good so if humans look at a thousand samples of

**[2:40:24]** like random lines of code being written by the AIS as they go and this is drawn from an independent distribution then 99 plus percent of the time the AIS have to not be doing stuff that's like

**[2:40:38]** downloading uh you know the the Hacker's guide to escaping open AI servers or inducing obvious Trojan vulnerabilities um and that's actually quite a different Dynamic than human law enforcement so if

**[2:40:55]** human law enforcement would catch one in a million crimes then that wouldn't influence the behavior of people committing crimes at all because they expect ah this is very unlikely to affect me

**[2:41:08]** with AI if you're able to draw a hundred samples or a thousand samples even if there are billions of AI instances and you're only looking at a small portion of them when you run gradient descent on the samples you'd

**[2:41:23]** arrive you're going to change the AI so that whenever humans look at it is delivering a good result and so that's just like quantitatively a very different functional form for how law

**[2:41:36]** enforcement works on AI when you can do these independent samples than it would for you know policing say like a human population that has a pre-existing psychology that isn't being

**[2:41:50]** Changed by this these observations because we when we do gradient descent on the samples we draw all the all of the next generation of the AI models has been altered in that way my picture of like a

**[2:42:03]** line to sub-human AI to this like the Superhuman AI being aligned is still murky if we can talk about that more concretely yeah I do want to clarify so where Elias are claims that were something like

**[2:42:19]** 95 90. yeah maybe likely to be killed uh in a AI takeover um I think that probably won't happen and later I can maybe give a more explicit breakdown of why

**[2:42:37]** um but I think it's a shockingly uh high risk um and so depending on the day I might say I might say one in four or one in five that we get an AI takeover

**[2:42:51]** um that Seattle seizes control of the future uh makes a much worse world than we otherwise would have had um and with like a big chance that we're all um killed in the process

**[2:43:06]** hey everybody I hope you enjoyed that episode as always the most helpful thing you can do is just share the podcast send it to people you think might enjoy it put it in Twitter your group chats Etc just

**[2:43:17]** splits the world appreciate your listening I'll see you next time cheers thank you
