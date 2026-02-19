---
layout: default
type: transcript
series: dwarkesh
episode: 0
guest: ""
title: "Francois Chollet — Why the biggest AI models can't solve simple puzzles"
source_url: "https://www.youtube.com/watch?v=UakqL6Pj9xo"
analysis_url: /transcripts/dwarkesh/77_francois_chollet_why_the_biggest_ai_models_can_t_solve_simple_puzzles.analysis/
permalink: /transcripts/dwarkesh/77_francois_chollet_why_the_biggest_ai_models_can_t_solve_simple_puzzles/
---

# Transcript: Francois Chollet — Why the biggest AI models can't solve simple puzzles

Source: https://www.youtube.com/watch?v=UakqL6Pj9xo

---

**[00:00]** LMS are very good at memorizing CTIC programs if you scale up the size of your database you are not increasing the intelligence of the system one bit I feel like you're using words like memorization which we would never use

**[00:11]** for human children if they can just solve any arbitrary algebraic problem you wouldn't say like they' memorized algebra they say they've learned algebra so we got a million dollar price pool and there's a $500,000 price for the

**[00:23]** first team that can get to the 85% Benchmark if Ark survives 3 months from here we'll we'll up the price opening I basically Le back progress towards higi by probably like 5 to 10 years they caus this complete closing down of Frontier

**[00:36]** research publishing and now LMS have uh sucked the oxygen out of the room like everyone is just doing LMS okay today I have the pleasure to speak with franois chol who is a AI researcher at Google and creator of kasas and he's launching

**[00:54]** a prize in collaboration with Mike kou the co-founder Xavier who will also be talking to in a second a million dollar prize to solve the arc Benchmark that he created so first question what is the arc Benchmark and why do you even need

**[01:07]** this prize why won't the biggest llm we have in a year be able to just saturate it sure so Arc is intended as a kind of IQ test for machine intelligence and what makes it different from most benchmarks out there is that it's

**[01:20]** designed to be resistant to memorization so if you look at the way LMS work they're basically this big interpolative memory and the way you scale up their capabilities is by trying to cram as much uh knowledge and patterns as

**[01:35]** possible into them and uh by contrast Arc does not require a lot of knowledge at all it's designed to only require what's known as core knowledge which is uh basic knowledge about things like um Elementary physics objectness counting

**[01:52]** that sort of thing um the sort of knowledge that any four-year-old or 5-year-old uh possesses right um but what's interesting is that each puzzle in Arc is novel is something that you've probably not encountered before even if

**[02:07]** you've memorized the entire internet and that's what that's what makes it sorry that's what makes makes Arc challenging for LMS and so far LMS have not been doing very well on it in fact the approaches that are working well are

**[02:21]** more towards uh discret program search program synthesis so first of all I'll make a comment that I'm glad that as a skeptic of llm you have put out yourself a benchmark that is it accurate to say that suppose that the biggest model we

**[02:38]** have in here is able to get 80% on this then your view would be we are on track of to AGI with llms how would you think about that right um I'm pretty skeptical that we're going to see llm do 8% in a year uh that said if we do see it you

**[02:53]** would also have to look at how this was achieved if you just uh train the model and millions or billions of puzzle similar to Arc so that you're relying on the ability to have some overlap between the tasks that you train on and a t that

**[03:08]** you're going to see a test time then you're still using memorization right and maybe maybe it can work you know hopefully um Arc is going to be good enough that it's going to be resistant to this sort of attempt and put forcing

**[03:21]** um but you know you never know maybe maybe it could happen I'm not saying it's not going to happen Arc is not a perfect Benchmark maybe maybe it has flawed flaws maybe it could be hacked in that way I'm so I guess I'm curious

**[03:34]** about what would gbtf have to do that you're very confident that you know it's on the path to AGI what what would make me change my mind about that Al is basically if I start seeing uh a critical mass of cases

**[03:49]** where you show the model with something it has not seen before a task that's actually novel from the perspective of its training data something that's not in a training data if it can actually adapt on the Fly um and this is true for

**[04:03]** LS but really this would catch my attention with any for a any AI technique out there if I can see the ability to adapt to novelty on the fly to pick up new skills efficiently then uh I would be extremely interested I I

**[04:18]** would I would think this is on the pass to AI so the advantage they have is that they do get to see everything maybe I'll take issue with how much they are relying on that but let's suppose that they are relying obviously they're

**[04:29]** relying on not that more than humans do to the extent that they do have so much IND distribution to the extent that we have trouble distinguishing whether a sing an example is in distribution or not well if they have everything in

**[04:42]** distribution then they can do everything that we can do maybe it's not in distribution for us why why is it so crucial that it has to be out of distribution for them uh you know why can't we just leverage the fact that

**[04:52]** they do get to see everything right what you're asking basically what's the difference between actual intelligence which is the ability to adapt to things you've not been prepared for and pure memorization like reciting uh what

**[05:05]** you've seen before and it's not just some semantic difference uh the big difference is that you can never uh pre-train on everything that you might see at test time right uh because the world changes all the time so it's not

**[05:21]** just the fact that the space of possible tasks is infinite and if even if you're trained on millions of them you've only seen 0% of the total space it's also the fact that the world is changing every day right um this is why we the human

**[05:37]** species has developed intelligence in the first place if there was such a thing as a distribution for the world for the universe for our lives then we would not need intelligence at all in fact uh many uh creatures many insects

**[05:51]** for instance do not have intelligence instead what they have is uh they have in their in their connectum uh in their genes hardcoded programs behavioral programs that map some stimul to appropriate response and they can

**[06:05]** actually navigate their lives their environment in a way that's very evolutionary fit that way without needing to learn anything and well if for environment was static enough predictable enough uh what would have

**[06:19]** happened is that Evolution would have found the perfect behavioral program a hardcoded cic behavioral program would have written it uh into our genes we would have a hardcoded connectum and that's what we will be running on but no

**[06:32]** that's not what happened instead we have general intelligence so we are born with extremely little knowledge about the world but we are born with the ability to learn very efficiently and to adapt in the face of things that we we we've

**[06:46]** never seen before and that's what makes us unique and that's what that's what is really really challenging to recreate in machines I want to Rabbit Hole on that a little bit but before I do that maybe I'm going to Overlay some examples of

**[06:58]** what an arc like challenge look like for for the YouTube audience but maybe for people listening on audio can you just describe what what what would an a sample Arc challenge look like sure so one Arc puzzle it looks kind of like an

**[07:10]** IQ test puzzle you've got a number of demonstration input output pairs so uh uh one pair is made of two grids so one grid shows you an input and the second grid shows you uh what you should produce as a response to that input and

**[07:27]** you get a couple uh pairs like this to demonstrate the nature of the task to demonstrate what you're supposed to do with your inputs and then you get uh a new test input and your job is to produce the corresponding uh test output

**[07:42]** you look at the demonstration Pairs and from that you figure out what you're supposed to do and you show that you've understood it on this new test pair and um importantly in order to the sort of like knowledge basis that you

**[07:58]** need in order to approach this these challenges is you just need core knowledge and core knowledge is uh it's basically the knowledge of what makes an object uh basic counting basic geometry topology symmetries and that

**[08:12]** sort of things so extremely basic knowledge LMS for sure possess such knowledge any child possesses uh such knowledge um and what's really interesting is that each puzzle is new so it's not something that you're going

**[08:26]** to find uh uh Elsewhere on the internet for instance uh and that means that whether it's as a human or as a machine every puzzle uh you have to approach it from scratch you have to actually reason your way through it you cannot just

**[08:40]** fetch the response from your memory so the core knowledge one contention here is we are only now getting multimodal models who because of the data they're trained on are trained to do spatial reasoning

**[08:57]** whereas obviously not only humans but but for billions of years of Revolution we've had our ancestors have had to learn how to understand abstract physical and spatial properties and recognize the patterns there and so one

**[09:12]** view would be in the next year as we gain models that are multimodal native that isn't just a sort of second class citizen add-on but the multimodal capability is a priority that it will understand these kinds of patterns

**[09:26]** because that's something would see natively whereas right now what mares is some Json string of 1 1 0 0 and it's supposed to recognize a pattern there and even if you showed a human such a like a just a sequence of these kinds of

**[09:39]** numbers it would have a challenge making uh making sense of what what kind of question you're asking it so why won't it be the case that as soon as we get the multimodal models which we're on the path to unlock right now they're going

**[09:49]** to be so much better at archetype spal reasoning that that's an empirical question so I guess we're going to see the answer within a few month but my answer to that is you know all grids de just uh discret to degrad of symbols

**[10:02]** they're pretty pretty small like it's not like uh if you flatten an image as a sequence of pixels for instance uh then you get something that's actually very very difficult to pass but that's not true for Arc because the grids are very

**[10:14]** small uh you only have 10 possible symbols so there's these two degrees that are actually very easy to flatten uh as sequences and Transformers llms they're very good at crossing the sequences in fact uh you can show that

**[10:27]** LMS do fine uh with processing AR CL data uh by simply functioning uh L llm on uh some subsets of the tasks and then trying to test it on small variations of these tasks and you see that yeah the the llm can encode just fine solution

**[10:47]** programs for tasks that it has seen before so it does not really have a problem passing the input of figuring out uh uh um the program the reason why uh s uh don't do well on Arc is really just uh the unfamiliarity aspect the

**[11:04]** fact that each new task is different from every other task you cannot basically you cannot memorize the solution programs in advance you have to synthesize a new solution program on the Fly for each new task and that's really

**[11:18]** what LMS are struggling with so before I do more Devil's Advocate I just want to step back and explain why I'm especially interested in having this conversation and obviously the million dollar Arc Pride I'm excited to actually play with

**[11:31]** it myself and hopefully um The vvus Challenge which was Nat fredman's prize for solving uh decoding squirrs the winner of that decoding the squirrels from that were buried in the volcanoes in the herculanum library that was

**[11:46]** solved by a 22-year-old who was listening to the podcast Luke Fator so hopefully somebody listening will find this challenge intriguing and find a solution so I'm and the reason I I've had on recently A lot of people who are

**[12:00]** bullish on llms and I've had discussions with them before interviewing you about how do we explain the fact that llms don't seem to be natively performing that well on Arc and I found their explanations somewhat contrived and I'll

**[12:13]** try out some some of the reasons on you but it is actually an intriguing fact that they actually these are some of these problems are relatively straightforward for humans to understand and they do struggle with them if you

**[12:24]** just input them natively all of them are very easy for humans like any any smart human should be able to do 90% 95% on Arc smart human a smart human but even a fivey old so with very very little knowledge they could they could

**[12:37]** definitely do over 50% so let's talk about that because you I agree that smart humans will do very well on this test but the average human will probably do you know mediocre

**[12:53]** not not really a so we actually tried with aage humans uh the score about 85 that was with Amazon mechanical twk workers right I'm I honestly don't know the demographic profile of Amazon Mechanical twerk workers but imagine

**[13:04]** just interacting with uh the platform that Amazon has set up to do remote work that's not the median human across the planet I'm guessing I mean the broader Point here being that so we see the Spectrum in humans where humans

**[13:18]** obviously have AGI but even within humans you see a spectrum where some people are relatively dumber and they'll do perform work on IQ like tests for example Ravens Progressive m if you look at how the average person performs on

**[13:31]** that and you look at the kind of questions that is a sort of Hit or Miss half of people will get it right half of people will get it wrong some of them are like pretty triv for us we might think like this is this looks kind of

**[13:39]** trivial and so humans have hii but from relatively small tweaks you can go from somebody who misses these kinds of basic IQ test questions to somebody who gets them all right which suggests that actually if these models are doing

**[13:52]** natively um we'll talk about some of the previous performances that people have tried with these models but somebody with a jack Cole with 240 million parameter model got 35% doesn't that suggest that they're on this on this

**[14:04]** spectrum that clearly exists within humans and they're going to saturated pretty soon yeah so that's there a bunch of interesting points here so uh there is indeed a um a branch of llm approaches suspended by Jack Cole that

**[14:18]** are doing quite well that are in fact uh state-of-the-art uh but you have to look at uh what's going on there so there are two things the first thing is that uh to get these numbers you need to pre-train your llm on millions of generated Arc

**[14:33]** tasks and of course if you if you compare that to a 5-year-old child looking at art for the first time uh the child has never done an acute test before has never seen something like like an art before the only overlap

**[14:44]** between what they know and what they have to do in the test is core knowledge is knowing about like counting and objects and symmetries and things like that and still uh they're going to do really well and they're going to do much

**[14:56]** better than D llm train on Millions of similar tasks and the second thing that's uh that's um something to note about the Jack Cod approach is um one thing that's really critical to making the model work at all is test time

**[15:11]** fine-tuning and that's something that's really missing by the way from llm approaches um right now is that you know most of the time when you're when you're using an llm it's just doing static inference the model is frozen and you're

**[15:25]** just uh prompting it and then you're get you're getting an answer so the model is not actually learning anything on the Fly it's its state is not adapting uh to the to the task at hand and what jao is actually

**[15:37]** doing is that for every test problem is on the Fly is fine tune in a version of d llm uh for that task and that's really what's unlocking performance if you don't do that you get like 1% 2% so basically something completely

**[15:53]** completely negligible and if you do test time fine tuning and you add a bunch of tricks on top then you end up with interesting performance numbers so I think what he's doing is trying to address one of the key limitations of

**[16:05]** LMS today uh which is the lack of active insurance is actually adding active Insurance to LMS and that's working extremely well actually so that's fascinating to me that there's so many interesting rabbit holes

**[16:17]** there should I take them in sequence or deal with them all at once let me let me just start so a the point you made about the fact that you need to unlock the adapter compute SL test time compute a lot of the scale maximalist I I think

**[16:30]** this will be interesting Rabbit Hole to explore with you because a lot of the scaling maximalist have your broader perspective in the sense that they think that in addition to scaling you need these kinds of things like unlocking

**[16:42]** adaptive compute or doing some sort of RL to get the system to working and their perspective is that this is a relatively straightforward thing that will be added to top the capab the representations that a scaled up model

**[16:55]** has greater access to No it's it's not it's it's not just a technical detail it's not a straightforward thing it is everything it is the important part and the the the scale uh a maximalist argument it boils on to

**[17:11]** um you know these people they refer to scaling lass which is this this empirical relationship that you can draw between how much compute you spend on training a model and the performance you're getting on benchmarks right and

**[17:24]** the the key question here of course is well how do you measure performance what it is that you're actually uh uh improving by adding more comput and more data and well it's it's Benchmark performance right and the thing is the

**[17:37]** way you measure performance is not a technical detail uh it it's it's not it's not an afterthought because it's going to uh narrow down the set of questions that you're asking and so accordingly it's going to narrow down

**[17:50]** the set of answers that that you're that you're looking for if you look at uh the benchmarks we're using for LMS they're all memorization based benchmarks like sometimes they're literally just knowledge based like like a school test

**[18:03]** and even if you look at the ones that are uh uh you know explicitly about reasoning you realize if you look closely that it's uh in order to solve them it's enough to memorize uh a finite set of uh uh resoning patterns uh and

**[18:19]** then you just reapply them they they're like static programs LMS are very good at memorizing static programs small static programs and and they've got this sort of like B of uh solution programs and when you

**[18:32]** give them a new puzzle uh they can just fetch the appropriate program apply it and it's looking like it's reasoning but really it's not doing any sort of on thefly program synthesis all it's doing is program fetching so you can actually

**[18:45]** solve all these benchmarks with memorization and so what what you're scaling up here like if you look at the models they are uh uh big parametric curves uh fitted to data distribution this

**[18:59]** so they are basically these big interpolative uh databases interpolative memories and of course if you scale up the size of your database and you cram into it uh more knowledge more patterns and so on uh you are going to be

**[19:14]** increasing its its performance as measured by memorization Benchmark that's that's kind of obvious but as you're doing it you are not increasing the intelligence of the system one bit you are increasing the skill of the

**[19:28]** system you you are increasing its usefulness its uh scope of applicability but not its intelligence because skill is not intelligence and that's the fundamental confusion um that that that people run into is that they're

**[19:42]** confusing skill and intelligence yeah there's a lot of fascinating things to talk about here so skill intelligence interpolation um I mean okay so the the thing about their fittings some manifold into that Maps the input data there's a

**[19:56]** reductionist way to talk about what happens in the human brain that says that it's just axons firing at each other but we don't care about the reductionist explanation of what's Happening we care about what the the the

**[20:09]** sort of meta at the at the macroscopic level what happens when these things combine as far as the interpolation goes so okay let's look at one of the benchmarks here there's there's one Benchmark that does great school math

**[20:22]** and these are problems that like a smart high schooler would be able to solve um it's called GSM 8K and these models get 95% on these like basically they always nail memorization bitk okay let's talk about what that means so here's one

**[20:36]** question about from that Benchmark so 30 students are in a class 1/ fifth of them are 12 year olds 1/3 are 13y old one 10th are 11 year olds how many of them are not 11 12 or 13 years old so I agree like this is not rocket science right

**[20:50]** you can write down on paper how you go through this problem and a high school kid at least a smart high school kid should be able to solve it now when you say memorization it still has to reason through how to think about fractions and

**[21:02]** what is the context of the whole problem and then combining the different calculations is doing it depends how you how you want to Define reasoning but there there are two definitions you can use so one is I have available uh a set

**[21:15]** of program templates it's it's like the structure of the puzzle which which can also generate its solution and I'm just going to identify the right template which is in my memory um I'm going to input the new values into the template

**[21:29]** run the program get the solution and you could say this is reasoning and I say yeah sure okay uh but another definition we can use reasoning is the ability to when you're faced with a with a puzzle given that you don't have already a

**[21:43]** program in memory to solve it you must synthesize on the fly a new program based on bits of pieces of existing programs that you have you have to do on the Fly program synthesis and it's actually dramatically harder than just

**[21:57]** fetching the right memorized program and replying it so I think maybe we are overestimating the extent to which humans are so sample efficient they also don't need training in this way where they have to drill in these kinds

**[22:13]** of Pathways of reasoning through certain kind of problems so let's take math for example yeah it's not like you can just show a baby the AXS of SE Theory and now they know math right so they they when they're growing up you had to do years

**[22:26]** of teaching them pre-algebra then you got to do a year of teaching them doing drills and going through the same kind of problem in algebra then geometry pre-calculus calculus absolutely so training yeah but isn't that like the

**[22:37]** same kind of thing where you you you can't just see one example and now you have the program or whatever you actually had to drill it these models also had to drill with a bunch of fruit training data sure I mean in order to do

**[22:46]** on the Fly program synthesis you actually need uh building blocks to work from so knowledge and memory are actually tremendously important in the process I'm not I'm not saying it's memory

**[22:59]** versus reasoning in order to do effective reasoning you need memory but it sounds like it's compatible with your story that through seeing a lot of different kinds of examples these things can learn to reason within the context

**[23:12]** of those examples and we can also see within bigger and bigger models so that was an example of a high school level math problem um let's say a model that's like smaller than gpt3 couldn't do that at all as these models get bigger they

**[23:24]** can they seem to be able to pick up bigger and bigger it's not really a size issue it's more like a training data issue in this case well bigger models can pick up these kinds of circuits which smaller models apparently don't do

**[23:35]** a good job of doing this even if you were to train them on this kind of data doesn't that just suggest that as you have bigger and bigger models they can pick up bigger and bigger Pathways or more General ways of reasoning

**[23:44]** absolutely but then isn't that intelligence no no it's not if you scale up your database and you keep adding to it more knowledge uh more program templates then sure it becomes more and more skillful you can apply to more and

**[23:56]** more tasks but General in intelligence is not task speciic skill scaled up to many skills it because there is an infinite space of possible skills general intelligence is the ability to approach any problem any skill and very

**[24:11]** quickly Master it using very little data because this is what makes you able to face anything you might ever encounter this is what makes uh uh this this is the definition of generality like generality is not specificity scaled up

**[24:25]** it is uh the ability to fly on mind to anything at all to arbitrary things and this requires fundamentally this requires the ability to adapt to learn on the Fly efficiently so I my claim is that by doing this free training on

**[24:41]** bigger and bigger models you are gaining the capacity to then generalize very efficiently let me give you an examp let me let me give you an example so your own company Google in their paper on Gemini 1.5 they had this very

**[24:54]** interesting example where the um they would give in context they would give the model the grammar book and the dictionary of a language that has less than 200 living speaker so it's not in the pre-training data and

**[25:09]** you just give them the the dictionary and it basically is able to speak this language and translate to it including the complex and organic ways in which language are languages are structured so a human if you showed me a dictionary

**[25:21]** from like English to Spanish I'm not going to be able to pick up the how to structure sentences and how to say things in Spanish the the fact that because of the representations that it has gained through this pre training it

**[25:33]** is able to now extremely efficiently learn a new language doesn't that show that uh this kind of pre- training actually does increase yourability to learn new tasks if you're right if you were right llms would do really well on

**[25:44]** Arc puzzles because Arc puzzles are not complex each one of them requires very little knowledge each one of them is is very low on complexity you don't need to think very hard about it uh they're actually extremely obvious for humans

**[25:56]** like even children can do them but LMS cannot uh even even LMS that have you know 100,000 times more knowledge than you do they still cannot and the only thing uh that makes AR special is that it was designed with this intent to

**[26:11]** resist memorization this is the only thing and this is the huge blocker uh for LM performance right and so you know I think if if you look at LMS closely it's pretty obvious that they're

**[26:27]** not really like synthesizing new programs on the fly to to Sol the task that they're faced with they're very much replying things that they've uh they've stored in memory for instance um one thing that's very striking is llms

**[26:40]** can solve a Cesar Cipher you know like Cesar Cipher like transposing uh letters to to to code uh a message um and while that's a fairly complex algorithm right uh but it comes up quite a bit on the internet so they've basically memorized

**[26:56]** it and what's really interesting is that they can can do it uh for a transposition length of like three or five because they are very very common numbers in examples provided on the internet but if you if you try to do it

**[27:07]** with an arbitrary number like nine it's going to fail because it does not encode the generalized form of the algorithm but only specific cases has memorized specific cases of the algorithm right and if if it could actually synthesize

**[27:21]** on the Fly the solver algorithm uh then the value of n would not matter at all because it does not increase the problem complexity I I think this is true of humans as well where what was the study that humans use memorization P matching

**[27:36]** all the time of course but humans are not limited to memorization better matching they have this very unique ability to adapt to new situations on the Fly this is exactly what enables you to navigate uh every new day in your

**[27:50]** life I I forgetting the details but there was some study that chess Grandmasters will perform very well within the context of the moves that excellent example because chess at the highest level is all about memorization

**[28:00]** just memorization game okay sure we can leave that aside what is your explanation for the original question of um why can uh why in context the gpt1 sorry Gemini 1.5 was able to learn a language including the complex grammar

**[28:15]** structure doesn't that show that they can pick up new knowledge I would assume that it has simply mind from its extremely extensive and imaginably vast uh training data it has mined uh the the required template and then it's just

**[28:27]** reusing is in it we know that LM have a very poor ability to synthesize new program templates like this on the flight or even adapt existing ones they're very much limited to fetching suppose there's a programmer at Google

**[28:40]** they go into the office in the morning at what point are they doing something that 100% cannot be due to fetching some the template that could could even if they suppose they were an llm they could not do if they had fetched some template

**[28:52]** from their program like at what point do they have to use this so-call extreme generalization capability forget about Google software developers every every day of their lives is full of Novel things that they've not been

**[29:02]** prepared for you cannot navigate your life based on memorization alone it's impossible I I'm sort of denying the premise that they're you also agree they're not doing like quote unquote memorization they you're it seems like

**[29:15]** you're saying they're less capable of generalization but I'm just curious of like the kind of generalization they do you if you if you you get into the office and you try to do this kind of generalization you're going to fail at

**[29:26]** your job what is the first point you're programmer what is the first point when you try to do that generalization you would you would you would lose your job because you can't do the extreme generalization I I don't have any

**[29:35]** specific examples but literally like take this situation for instance you've never been here in this room uh maybe you've been in in in this in this city a few times I don't know but there's a fair amount of novelty

**[29:49]** you've never been been you know uh interviewing me there's a fair of notin every hour of every day in your life and it's in fact uh um by and large more novelty than uh any any llm could handle like if you just put llm in in robot it

**[30:04]** could not be doing all the things that you've been doing today right um or take I know like cell driving cars for instance you take a cell driving car operating in the in the barrier do you think you could just drop it in New York

**[30:17]** City or drop it in London where people drive on the left uh no it's it's going to fail so not not only can you drop not like make it generalized to uh a chance of rules um uh of driving rules but you cannot even make it generalized to a new

**[30:33]** city it needs to be trained on each specific environment I mean I agree that self-driving cars aren't AGI um but is the same type of model they Transformers as well I mean I don't know also have brains with neurons in them but they're

**[30:48]** less intelligent because they're small not the same architect we can get into that but so I still don't understand what like a concrete thing of we all needs training that's why education exists that's why we had to spend the

**[31:00]** first 18 years of our life doing drills we have a memory but we are not a memory we are not limited to just I'm denying the F that that's necessarily the only thing these models are doing and I'm still not sure what is the what is the

**[31:13]** task that a a remote worker would be do have to like suppose you subed out a remote work with an llm and they're they're a programmer what is the first point that would you realize this is not a human this is an llm what about I just

**[31:24]** send them a knock puzzle and see how they do no like part of the job you know but you you have to deal with novelty all the time okay so if you is there a world in which all the programmers are replaced and then we're still saying ah

**[31:38]** but they're only doing memorization lateen programming tasks but they're still producing a trillion dollars of uh worth of you know output in the form of code software development is actually a pretty good example of a job where

**[31:48]** you're dealing with novelty all the time uh or if you're not well I'm not sure what you're doing so I personally use genv very all in my my software development job and before before L think I was also using stack Overflow

**[32:03]** very little you know some people maybe are just copy pasting stuff from stack Overflow or nowadays copy pasting stuff from from an llm um personally I try to focus on problem solving the syntax is just a technical detail what's really

**[32:17]** important is the problem solving like the essence of programming is engineering uh mental models like mental representations of the you're trying to solve but you can you know we have many people can interact with these systems

**[32:33]** themselves and you can go to chat GPT and say Here's a specification of the kind of program I want they'll build it for you as long as there are many examples of this program on like GM and S and so on sure they will fetch the

**[32:45]** program for you from their memory but you can change arbitrary details you can say I needed to work on this different kind of server it I I need if if that were true there would be no software Engineers today I I I agree we're not at

**[32:57]** a full age yet in the sense that these models have let's say less than a trillion parameters a human brain has somewhere around the order of 10 to 30 trillion synapses I mean if you're just doing some naive math you're like at

**[33:09]** least 10x underparameterized so I agree we're not there yet but it I'm I'm sort of confused on why we're not on the Spectrum where yes I agree that there's many kinds of generalization they can do but it seems like they're on this kind

**[33:22]** of smooth spectrum that we see even within humans where Some Humans would have a hard time doing an arc type test we see that based on their performance on Progressive Ravens matrices type IQ tests I I'm not a fan of IQ test because

**[33:33]** for the most part you can train uh on IQ tests and get better at them so they're very much memorization based and this is actually the main Pitfall that Arc tries not to full fall I'm I'm still not so if um if all remote jobs are automated in

**[33:49]** the next five years let's say um at least that don't require you to be like sort of a service it's not like a salesperson where you need you want the human to be talking but like programing whatever in that World um would you say

**[34:01]** that that's not possible because a lot of what a programmer needs to do definitely requires things that would not be in any pre-training corporate sure I mean in five years there will be more software Engineers than there are

**[34:11]** today not not but but I just want to understand so um still not sure I mean I know how to I study computer science like if I had become a Code Monkey out of college like what would I be doing I go to my job what is the first thing my

**[34:24]** boss tells me something to do when does he realize I'm an llm if I was an llm probably on the first day you know again uh if if it were true that uh uh llms

**[34:39]** could generalize to novel problems like this and and actually uh develop software to solve a problem they've never seen before you would not need software Engineers anymore in practice if I look at how people are using LMS in

**[34:51]** their software engineering job today they're using it uh as a as a stack oflow replacement so they're using it as uh a way to copy paste code Snippets to perform very common actions and this is what they actually need is a database of

**[35:05]** good Snippets they don't actually need uh any of the abilities that actually make them software Engineers I mean when we talk about um interpolating between stack Overflow databases if you look at the kinds of math problems or coding

**[35:17]** problems maybe to say that they're um maybe let's step back on interpolation and let me ask the question this way why can't creativity why isn't creativity just interpolation in a higher Dimension where if a bigger

**[35:31]** model can learn a more complex manifold we're going to use the M language and if you look at read a biography of a scientist right it doesn't like they're not zero shotting new scientific theories they're playing with existing

**[35:42]** ideas they're trying to ju toose them in their head they try out some slight like slightly ever in the tree of evolu um intellectual descendants they try out a different evolutionary path we you you sort of run the experiment there in

**[35:55]** terms of publishing the paper whatever it seems like a similar kind of thing humans are doing there's like at a higher level of generalization and what you see across bigger and bigger models is they can they seem to be approaching

**[36:05]** higher and higher level generalization where gbt2 couldn't do a great school level math problem that requires more generalization that it has cap capability for even that skill than gbt three and four can so not quite so uh

**[36:17]** gbt 4 has a higher degree of skill and higher range of skills I semantics here but generalization I don't want to get any semantics here but the question of why why can't creativity be um just interpolation on a higher higher

**[36:31]** Dimension I think interpolation can be creative absolutely and you know uh to your point I do think that uh on some level humans also do a lot of memorization a lot of reciting a lot of pattern matching and aot of

**[36:43]** interpolation as well so it's it's very much a spectrum U between between pattern matching and true reasoning it's a spectrum and humans are never uh really at one hand end of the spectrum they never really do doing pure pattern

**[36:59]** matching or pure reasoning they're usually doing some mixture of both even if you're uh doing something that seem very reasoning heavy like proving a mathematical theorem uh as you're doing it sure you're doing quite a bit of

**[37:11]** discrete search in your mind quite a bit of actual reasoning but you're also uh very much Guided by intuition Guided by thech Guided by the shape of proofs that you've seen before by by your knowledge of mathematics so it's it's never really

**[37:26]** you know all of our thought everything we do is a mixture of this solar flak interpolative memorization based thinking this Sol of flak type one thinking and uh type two thinking um why are bigger models More Sample efficient

**[37:43]** because they have more reasonable uh building blocks uh that they can lean on uh to pick up uh new patterns in that training data and does that pattern keep continuing as you keep getting bigger and bigger to the extent that the new

**[37:57]** patterns you're you're giving the model to learn are good match for what it has learned before if you present something that is actually novel that is not in sta distribution like an arc puzzle for instance it will fail uh let me make

**[38:09]** this claim the program synthesis I think is a very uh very useful intuition pump why can't it be the case that what's happening in the Transformer is the early layers are doing the figuring out how to represent the inputting tokens

**[38:22]** and what the middle layers do is this kind of program search program synesis where they combine the inputs to the to the you know all the circuits in the model where they they go from the low level representation to a higher level

**[38:34]** representation near the middle of the model they use these programs and they do they they combine these Concepts then what comes out the other end is the reasoning based on that high level uh intelligence possibly why not um but you

**[38:48]** know if uh if these models were actually capable of synthesizing synthesizing novel programs however simple they should be able to do Arc because for any oask if you write down the solution program in Python it's not a complex

**[39:03]** program it's extremely simple and and and humans can figure that so why why can LMS not do it okay that I think that's a fair a fair point and if I turn the question around to you so suppose that it's the case that in a year a

**[39:19]** multimodal model can solve Arc let's say get 80% whatever the average human would get then AGI po possibly yes I think if you if you start so honestly what I would like to see is uh an llm type model solving AR at like 80% but after

**[39:38]** having only been trained on core knowledge related stuff but human kids I don't think we're necessarily just traded n it's not just that we have in our gen perence let me rephrase that uh only trained on information that is not

**[39:54]** um explicitly trying to anticipate what's going to be in the arc test set but isn't the isn't the whole point of Arc that you can't sort of it's a new chart of type of intelligence test every single time the point so if Arc were a

**[40:06]** perfect Flawless Benchmark it would be impossible to anticipate within the test set and you know AR was released uh more than four years ago and so far it's been resistant to memorization so I think it has uh to some extent passed a test of

**[40:20]** time um but I don't think it's perfect I think if you try to make by hand uh1 of thousands of AR tasks and then you try to multiply them uh uh by programmatically generating variations and then you end up with maybe hundreds

**[40:36]** of millions of tasks uh just by brute forcing the task space there will be enough overlap between what you train on and what's in the test set that you can actually score very highly so you know with enough scale you can always cheat

**[40:49]** if you can do this for every single thing that supposedly requires intelligence then what good is intelligence apparently you can just Brute Force intelligence if if the world if your life were a static distribution

**[40:59]** uh then sure you could just Brute Force the space of possible behaviors you could like you know the way we think about intelligence there are several metaphors s likees but one of them is you can

**[41:11]** think of intelligence as a pth finding algorithm in future situation space like I don't know if you're familiar with scam development like RTS scam development but you have a map right and and you have it's like a 2d 2D 2D map

**[41:26]** and um you have part information about it like there is some fog of War on your map there are areas that you haven't explored yet you know nothing about them and then there are areas that you've explored but um you only know how they

**[41:38]** were like in the past you don't know how they like today and um think and and now instead of thinking about TOA think about the space of possible future situations that you might encounter and how they're connected to each other

**[41:52]** intelligence is a path finding algorithm so once you set a goal it will tell you how to get there optimally um but of course it's it's constrained by the information you have uh it it cannot pass find in an area that you know

**[42:08]** nothing about it cannot also anticipate uh uh changes and um the the the thing is if you had complete information about the map uh then you could solve the past finding Problem by simply memorizing every possible path every mapping from

**[42:26]** uh point A to point B uh you could you could solve the problem with pure memory but where the reason you cannot do that in real life is because you don't actually know what's going to happen in the future life is Ever Changing I feel

**[42:40]** like you're using words like memorization which we would never use for human children if if you like your kid learns to do algebra and then like now learns to do calculus you wouldn't say they've memorized Calculus if they

**[42:48]** can just solve any arbitrary algebraic problem you wouldn't say like they memorized algebra they say they've learned algebra humans are never really doing pure memor position of pure reasoning but that's only because you're

**[42:58]** semantically labeling when the human does the skill it's a memorization when the exact same skill is done by the LM as you can measure by these bench marks and you can just like plug in any sort of math problem sometimes humans are

**[43:07]** doing the exact same as yell L is doing which is just for instance I know if you learn to add numbers you're memorizing an algorithm you're memorizing a program and then you you can reapply it you are not synthesizing on the Fly uh the

**[43:20]** addition program so obviously at some point some human had to figure out how to do addition but like the way a kid learns it is not that that they sort of figure out from the accents of set theory how to do addition I think what

**[43:31]** you learn in school is mostly memorization right so my claim is that listen these models are vastly underparameterized relative to how many flops or how many parameters you have in the human brain and so yeah they they're

**[43:44]** not going to be like coming up with new theorems like the smartest humans can but most humans can't do that either um what most humans do it sounds like a similar to what you calling memorization which is memorizing skills or memorizing

**[43:58]** um you know uh techniques that you've learned and so it sounds like it's compatible in your tell me if this is wrong is it compatible in your world if like all the remote workers are gone but they're doing skills which we can

**[44:10]** potentially make synthetic data of so we record everybody's screen and every single remote worker screen we sort of understand the skills they're performing there and now we've trained a model that can do all this all the remote workers

**[44:21]** are unemployed we're generating trillions of dollars of economic activity from AI uh remote workers in that world are we still in the memorization regime so sure uh with memorization you can automate almost

**[44:32]** anything MH as long as it's it's a static distribution as long as you don't have to deal with change are are most jobs part of such a static distribution potentially there are lot there are lots of things that you can automate yeah and

**[44:44]** llms are an excellent tool for Automation and I think that's and but you have to understand that automation is not the same as intell I'm not saying that LMS are useless I've been a huge proponent of deep learning for many

**[44:55]** years uh and and you know for many years I've been saying two things I've been saying that if you keep scaling up deep planning it will keep paying off and at the same time I've been saying if you keep scaling up the planning this will

**[45:06]** not lead to AI uh so we can automate more and more things and yes this is economically valuable and yes potentially there are many jobs you could automate way like this and that would be economically avilable uh but

**[45:18]** you're not still not going to have intelligence so you can ask you know okay so what does it matter if we can generate all this economic value maybe we don't need intelligence after all well you need intellig

**[45:27]** the moment you have to deal with change with novelty with uncertainty as long as you're in a space that can be exactly described in advance you can just um you can just make a pure memorization right in fact you can always solve any problem

**[45:44]** you can always display uh arbitrary levels of skills uh uh on on any task um without leveraging any intelligence whatsoever as long as it is possible to describe the problem and its solution very very precisely but when they do

**[46:02]** deal with novelty then you just call it interpolation right and so no not interpolation is not enough to deal with all kinds of novelty if it were U then llms would be would be AI I agree they're not AI I'm just trying to figure

**[46:15]** out how do we figure out we're on the path to Ai and I think a sort of corrects here um is maybe that it seems to me that these things are on a spectrum and we're clearly covering the earliest part of the spectrum with l I

**[46:27]** and oh okay interesting but here's another sort of thing that I think is evidence for this grocking right so clearly even within deep learning there's a difference between the memorization regime and the

**[46:39]** generalization regime where at first it'll just memorize the data set of you know if you're doing modular addition how to add digits and then at some point if you keep training on that they'll learn the skill so the fact that there

**[46:52]** is that distinction suggests that there the the the generalized circuit the Deep learning can learn uh there is a regime it enters where it generalizes if you have an overparameterized model which we don't have in comparison to all the

**[47:02]** tasks we want these models to do right now gring is very very old phenomenon we've been we've been observing it for decades it's it's basically an instance of the minimum description length principle where sure you can given a

**[47:16]** problem you can just memorize uh an input a pointwise input to Output mapping which is completely overfit so it does not generalize at all but it SVS uh the problem on the train data uh and uh from there you can actually keep

**[47:32]** pruning it keep making uh your mapping simpler and simpler and more compressed and at some point it will start generalizing and so that's something called the the minimum uh description leg principle it's de idea that the

**[47:46]** program that will generalize best is the shortest right um and uh it doesn't mean that you're doing anything other than memorization but you're doing memorization plus regularization right AKA generalization yeah and that

**[48:01]** absolutely that leads to to generalization right and then so you do that within one skill but then the pattern you see here of metal learning is that it's more efficient to store a program that can perform many skills

**[48:11]** rather than one skill which is what we might call fluid intelligence and so as you get bigger in R models you would expect it to go up this hierarchy of generalization where it generalizes to a skill then it generalizes across

**[48:21]** multiple scales that's correct that's correct and you know llms they're not infinitely large uh they have only a fixed number of parameters and so they have to compress their knowledge as much as possible and in practice so llms are

**[48:35]** mostly storing reusable bits of programs like vector programs and uh because they have this need for compression it means that every time they're learning a new program they're going to try to express it in terms of existing bits and pieces

**[48:49]** of programs that they've already learned before right isn't isn't this the generalization absolutely oh wait so this is why you know clearly LMS have some degree of generalization and this is precisely why it's because they have

**[49:03]** to compress and why why is that intrinsically limited why can't you just go it at some point it has to learn a higher level of generalization higher level and then the highest level is the fluid intelligence it's in intrinsically

**[49:13]** limited because the substrate of of your model is a big parametric curve and all you can do with this is local generalization uh if you want to go beyond this to broader or extreme generalization

**[49:27]** you have to move to a different type of model and my Paradigm of choice is discrete program search program synthesis so and if you want to understand that you can sort of like compare compare it contrast it with de

**[49:40]** planning so in De planning your model is a a parametric curve differentiable parametric curve in program synthesis your model is a discrete graph of operators so you've got like a set of logical operators like a domain specific

**[49:56]** language uh you're picking uh instances of it you're structuring that into a graph that's a program and that's actually very similar to like a program you might you might write in in in python or C++

**[50:08]** and so on and uh in deploying your learning engine because we're doing match learning here like we're trying to automatically learn these models uh in deing your learning engine is gradiant descent right uh and gr and descent is

**[50:22]** very computer efficient because you have this very strong informative feedback signal about uh where the solution is so you can get to the solution very quickly but it is very data inefficient uh meaning that in order to make it work

**[50:36]** you need a dense sampling of the operating space you need a dense sampling of the data distribution and then you you're limited to un need generalizing within that data distribution and the reason why you have

**[50:47]** this limitation is because your model is a curve and meanwhile if you look at discrete program search um The Learning engine is comunal search you're just trying a bunch of programs until you find one that actually miss uh your spec

**[51:01]** this process is extremely data efficient you can learn a generalizable program from just one example two examples which is why it works so well on Arc by the way but uh the big limitation is that it's extremely uh comput inefficient

**[51:15]** because you're running into uh communal explosion of course and so you can you can sort of see uh here how the planning and discrep program search uh they are very compl uh complimentary strength and limitations as well like every

**[51:30]** limitation of deep learning has a strength a corresponding strengths in in in program synthesis and and inversely and I think the PA forward is going to be to merge the two to basically start doing so another way you can think about

**[51:44]** it is uh so this these parametric curves uh train with ground descent they are great fit for everything that's a system one type thinking like pattern cognition intuition uh memorization and so on and discret program search uh uh is is great

**[52:02]** fit for a type two thinking system two thinking uh for instance planning reasoning uh quickly figuring out a generalizable model that matches just one or two examples like for an arc puzzle for instance and um I think

**[52:18]** humans are never doing pure system one or pure system to they're always mixing and matching both and right now we have all the tools for system system one we have almost nothing for system two The Way Forward is to create a hybrid system

**[52:32]** and I think the the form it's going to take is it's going to be uh mostly system too so the the outer structure is going to be a discret program search system uh but you're going to fix the fundamental limitation of discri progam

**[52:45]** search which is Comm explosion you're going to fix it with deep learning you're going to leverage deep learning to guide uh to provide intuition uh in program space to guide the the program search and I think that's very similar

**[52:58]** to um what you see for instance when when when you're playing chess or when you're trying to prove a theorem is that um it's mostly a reasoning thing but you start that with some intuition about the shape

**[53:14]** of the solution and that's very much something you can get uh via a de planning model Via de planning models they're very much like intuition machines uh they're pattern matching uh machines so you you you start from this

**[53:27]** uh shape of the solution and then you're you're going to do actual explicit discret program search um but you're not going to do it uh via Brute Force you're not you're not going to try things kind of like randomly um um you're actually

**[53:43]** going to ask another deep planning model for suggestions like here's the best likely next step here's where in the graph you should be going and you can also use yet another de planning model for feedback but well here's what I have

**[53:57]** so far is it looking good should I just backtrack and try something new so um I think discrit program search is going to be the key but you want to make it dramatically better orders of magnitude more efficient by leveraging Deep

**[54:10]** learning and by the way another thing that you can use the planning for is of course things like um Common Sense knowledge and and knowledge in general um and I think you're going to end up with this sort of system where you have

**[54:22]** this uh on the Fly uh synthesis and engine that can adapt to new situations but the way it adapts is that it's going to fetch um from a bank of patterns uh modules that could be themselves uh curves that could be U differentiable

**[54:41]** modules and some others that could be algorithmic in nature it's going to assemble them uh via this process that's intuition guided and it's going to give you for every new situation you might be faced with it's going to give you with

**[54:54]** uh a generalizable model that were synthesized using very very little data and that something like this would solve Arc that's actually a really interesting um a prompt because I think an interesting Crux here is when I talk

**[55:09]** to my friends who are extremely optimistic about llms and expect AGI within the next couple of years they also in some sense agree that scaling is not all you need but that the rest of the progress is undergirded and enabled

**[55:27]** by scaling and but still you need to add the system to the test time compute top these models and their perspective is that it's relatively straightforward to do that because you have this library of representations that you built up from

**[55:42]** free trading but it's almost talking like you know just like skimming through textbooks you need some more deliberate way in which it engages with the material it learns in context learning is extremely sample efficient but to

**[55:57]** actually distill that into the weights you need the model to like talk through the things that sees and then add it back to the weights as far as the system to goes they talk about adding some kind of RL setup so that it is encouraged to

**[56:09]** proceed on the reasoning traces that end up being correct and they think this is a relatively straightforward stuff that will be added within the next couple of years that's an empirical question so I think we'll see uh your intuition I

**[56:19]** assume is not that I'm curious my intuition is in fact this whole like system to architecture is the hard part is the very hard and not obvious part scaling up the interpolative memory is the easy part all you need is is uh like

**[56:35]** it's literally just a big curve all you need is more data it's a representation of a data set an Interpol representation of data set that's the easy part the hard part is the architecture of intelligence memory and intelligence are

**[56:47]** separate components we have the memory we don't have the intelligence yet and I agree with you that well having the memory is actually very useful and um if you just said the intelligence but it was not hooked up to an extensive memory

**[56:59]** it would not be that useful because it would not have enough material uh uh to work from yeah the alternative hypothesis here that a former guest Trenton brooken uh Advanced is that intelligence is just um hierarchy

**[57:13]** Associated memory where higher level patterns when Sherlock Holmes goes into a crime scene and he's extremely sample efficient he can just like look at a few Clues and figure out who was a murderer and the way he's able to do that is he

**[57:24]** has learned higher higher level sort of associations it's memory in some fundamental sense but so here's one way to ask a question in the brain supposedly we do program synthesis but it is just synapses

**[57:39]** connected to one each other and so physically it's got to be that you just query the right circuit right you are yeah yeah yeah you know it's it's a matter of degree but if you can learn it if if you know training in the

**[57:51]** environment that the human ancestors have trained in means you learn that those circuits tra training on the the same kinds of outputs that humans produce which to replicate require these kinds of circuits wouldn't that train

**[58:00]** the same kind of um whatever humans have you know it's it's matter of degree um if you have a system that has a memory and is only capable of of doing local generalization from that it's not going to be very adaptable um to be

**[58:17]** regener you you need the memory plus the ability to search uh to quite some depth uh to achieve you know broader even extreme generalization um you know like one one of my favorite psychologist so Jean P was the the founder of

**[58:34]** Developmental Psychology he had a a very good quote about intelligence he said intelligence is what you use when you don't know what to do and it's like as as a human living your life in most situations you already know what to do

**[58:48]** because you've been in this situation before you already have the answer right um and you're you're only going to need to use intelligence when your bed with uh with novelty with with something you didn't expect with something that you

**[58:59]** weren't prepared for either by uh your own experience your own life experience or by your evolutionary history like this day that you're living right now is different in some important ways from every day you've lived before but it's

**[59:15]** also different from any day ever lived by any of your ancestors and still you're capable of of being functional right how is it possible I'm not denying that generalization is extremely and is basis for intelligence I that's not the

**[59:29]** correct the correct is like how much is of that is happening in the models but um okay let me ask a separate question we we might keep going in the circle here the differences in intelligence between humans maybe the intelligence

**[59:41]** test because of reasons you mentioned are not measuring it well but clearly there's differences in intelligence between different humans sure what is your explanation for what's going on there because I think that's sort of

**[59:50]** compatible with this my story that there's a spectrum of generality and that these models are climbing up to a human level and even Some Humans haven't even climbed up to the Einstein level or the

**[1:00:00]** uh the the Fran level but so that's a great question you know um there is extensive evidence that intelligence difference intelligence are mostly genetic in nature right meaning that if you take someone who is not very

**[1:00:13]** intelligent there is no amount of training of like training data you can expose that person to that would uh uh make them become Einstein and this kind of points to the fact that you really need uh a better architecture you need a

**[1:00:28]** better algorithm and more training data is not in fact all you need I think I agree with that I think what maybe a way I might phrase it is that the people who are smarter have in ml language better initializations it just they the neuro

**[1:00:45]** wiring if you just look at it's it's more efficient they have maybe greater density of um firing and so some some part of the story scaling there is some correlation between brain size and intelligence

**[1:00:56]** and we also see within the context of quote unquote scaling that people talk about within the context of llms architectural improvements where a model like Gemini 1.5 flash is performed as well as gp4 did when gp4 was released a

**[1:01:11]** year ago but is 57 times cheaper on output so the part of the scaling story is that the architectural improvements are we're in like extremely low hanging fruit uh territory when it comes to those okay we're back now with the

**[1:01:25]** co-founder of zapier Mike K we had to restart a few times there and you're funding this prize and you're running this prize with franois and so tell me about how this came together how how what prompted you guys to launch this

**[1:01:41]** prize yeah um I guess I've been sort of like AI curious for 13 years uh I've been I co-founded Z zapper been running it for the last 13 years and I think I first got introduced to your work in during Co um I kind of went down the

**[1:01:53]** rabbit hole we had a lot of free time um and it was right after you um published your onmeasure of intelligence paper you sort of introduced the concept of AGI this like efficiency of skill acquisition is like the right definition

**[1:02:04]** and in the arc puzzles but I don't think the first kagle contest was done yet I think it was still running and so I kind of it was interesting um but I just parked the idea uh and um I had bigger fish to fry at Zapp here we're in this

**[1:02:17]** middle of this big turnaround of trying to get to our second product um and then uh it was January 2022 when the Chain of Thought paper came out that really like awoken me to sort of the progress I I gave a whole presentation to the zapier

**[1:02:30]** on like the gbd3 paper even I i' sort of felt like I had priced in everything that Elms could do and that paper was really shocking to me in terms of oh these just latent capabilities that Elms have that um I didn't expect that they

**[1:02:41]** had and so I actually gave up my uh exact team rooll at app I was running half the company at that point I went back to be an individual contributor and just du to go do AI research alongside Brian my co-founder um and ultimately

**[1:02:54]** that led me to back toward WS Arc I was looking into it again and I had sort of expected to see uh this you know saturation effect that you know mlu has that GMS 8K has and when I looked at the scores and the progress that since the

**[1:03:08]** last four years um I was really again shocked to see actually we've made very little objective progress towards it and um it felt very it felt like a really really important eval and as I sorted spent the last year asking people

**[1:03:20]** quizzing people about it in sort of my network and Community um very people few people even knew it existed and uh that that felt like okay if it's right that this is a really really like globally singularly unique um AGI eval and it's

**[1:03:34]** different from every other eval that exists that are more that more Nar you know narrowly measures AI skill um like more people should know about this thing uh I had my own ideas on how to beat the arc as well so like I was working on

**[1:03:45]** nights and weekends on that and I flew up to meet France wat earlier this year um to sort of quiz him show them my ideas and ultimately I was like well you know why don't you think more people know about art um I think you should

**[1:03:56]** actually answer that I think it's a really interesting question like why why don't you think more people know about Arc sure you know I think benchmarks that gain uh Traction in the research Community are benchmarks that are

**[1:04:06]** already fairly tractable because the dynamic that you see is that some research group is going to make some initial breakthrough then this is going to catch the attention of everyone else and so you're going to get followup

**[1:04:18]** papers with with people trying to uh beat the first team and so on and for AR this has not really happened because Arc is actually very hard for existing eii techniques kind of Arc requires you to try new ideas and that's very much the

**[1:04:32]** point by the way like the point is not that yeah you should just be able to apply existing technology and and solve Arc the point is that existing technology uh as reach a plateau and if you want to go beyond that if you want

**[1:04:45]** to start being able to tackle problems that you haven't memorized that you haven't seen before uh you need to try new ideas and um Arc is not just meant to be um uh this s of flag uh measure of how close we are to a it's also meant to

**[1:05:02]** be a s a source of inspiration like I want I want researchers to look at these puzzles and be like hey it's really strange that these puzzles are so simple and most humans can can just do them uh very quickly why is it so hard for

**[1:05:17]** existing AI systems why is it so hard for LS and so on this is true for LS but Arc was actually released before LS were really a thing and um the only thing that made it special at the time was that it was designed to

**[1:05:30]** be a resistance to memorization and the fact that it has survived llms and gen and so well uh kind of shows that yes it is actually resistant to memorization this is what nerds s me um because I went and took a bunch of the puzzles

**[1:05:43]** myself I've showed it to all my friends and family too and they're all like oh yeah this is like super easy um are you sure AI can't solve this like that that's the reaction and and the same one for me as well and the where you dig in

**[1:05:54]** you're like okay you there's not just empirical evidence over the last four years that it's unbeaten but there's theoretical like Concepts behind why um and I I completely agree at this point that like new ideas basically are needed

**[1:06:05]** to be dark and there's a lot of current trends in the world that are actually I think working against that um happening basically I think we're actually less likely to generate new ideas right now um you know I think one of the kind of

**[1:06:17]** Trends is the closing up Frontier research right the gp4 paper from opena had no technical detail shared uh the Gemini paper had no technical detail shared and like the longer context uh part of that work and and yet that open

**[1:06:28]** Innovation open progress and sharing is what got us to Transformers in the first place that's what got us to Elms in the first place um so it's it's kind of it disappointing a little bit actually that like so much Frontier work has gone

**[1:06:39]** closed it's really making a bet that like these individual labs are going to be the have the Breakthrough and not the ecosystem um is going to have the Breakthrough and I think sort of the internet open source has shown that

**[1:06:48]** that's like the most powerful Innovation ecosystem that's ever existed probably in the entire world I think that's that's actually really sad that uh Frontier research is no longer being published uh if you look if you look

**[1:06:58]** back you know four years ago um well everything was just openly shared like all the set of theart results were were published and this is no longer the case and it's very much you know open single-handedly uh changed the game and

**[1:07:11]** I think um open air basically set back uh progress towards AI by quite a few years probably like five to 10 years for two reasons and one is that well they they cause this complete closing down uh of research Frontier research publishing

**[1:07:28]** uh but also uh they trigger this uh initial uh burst of hype uh around llms and now llms have uh sucked the oxygen out of the room like everything everyone is just doing LMS um and I see LMS as more of an offramp on the on the path to

**[1:07:48]** AGR actually um and all these new resources uh they're actually going to LMS instead of everything else that could be they could be going to and you know if you look uh further into the past to like 2015 2016 there were like a

**[1:08:03]** thousand times fewer people doing AI back then and yet I feel like the rate of progress was higher because people were exploring more directions um the world felt felt more open-ended like you could just go and try like have a cool

**[1:08:19]** idea of a launch and try it and get some interesting results so there was there was this this energy and now everyone is very much doing some variation of the same thing and the big Labs also tried their hand on Arc but because they got

**[1:08:33]** bad results they didn't publish anything like you know people only publish uh positive results um I wonder how much effort people have put into trying to prompt or scaffold do some sort of maybe Devon type approach into getting the

**[1:08:51]** frontier models and the frontier models of today not just a year ago because a lot of post training has has gone into making them better so claw through Opus or gbd4 into getting good Solutions on Arc I um I I hope that one of the things

**[1:09:05]** this episode does is get people to try out this open competition where they have to put in an open source model to compete but also to like figure out if there maybe the late capability is latent in CLA Opus and just see if you

**[1:09:18]** can show that I I think that would be super interesting so let's talk about the prize how much do you win if you solve it you know get whatever percent on Arc how much do you get if you get the best division but don't crack it so

**[1:09:30]** we got a million dollar actually a little over a million dollar is the price pool running the contest uh on an annual basis we're GNA we're starting it today um through the uh middle of November and the goal is to get 85%

**[1:09:41]** that's the lower bounded human average that you guys talked about earlier and uh there's a $500,000 prize for the first team that can get to the 85% Benchmark we're also going to run we don't expect that to happen this year

**[1:09:53]** actually um one of the early um uh stats at zappier gave me this line that has always stuck with me uh that the the longer it takes the longer it takes so my prior is that like Arc is going to take years to solve um and so we're

**[1:10:05]** going to keep we're also going to break down and do a progress price this year so we're there's $100,000 progress price which we will pay out to uh the top scores so $50,000 is going to go to the top objective scores this year on the

**[1:10:18]** kle leaderboard which is we're hosting it on kaggle and then we're going to have a $50,000 pot set for a a paper award um for the best paper that explains conceptually the the scores that they were able to achieve and one

**[1:10:30]** of the I think interesting things we're also going to be doing is um we're going to be requiring that in order to win the prize money that you put the solution or your paper out into public domain um the reason for this is you know tend

**[1:10:42]** typically with contest you see a lot of like closed up sharing people are kind of private secret they want to hold their Alpha TOS during the contest period and because we expect it's going to be multiple years um we won an eny

**[1:10:52]** game here so the the plan is you know end of November you will award the $100,000 prize money to the top progress prize and then use the downtime between December January February to uh share out all the knowledge um from the top

**[1:11:06]** scorers and the approaches folks were taking in order to rebaseline the community up to whatever the state-ofthe-art is and then run the contest again next year and keep doing that on a yearly basis until we get 85%

**[1:11:16]** I I'll give some people some context on why I think this priz is very interesting I was having conversations with my friends who are very much Believers and models as they exist today and first of all it was intriguing to me

**[1:11:28]** that they didn't know about Arc these are experienced ml researchers and so you show them the this is this happened a couple nights ago we went to dinner and I showed them an example problem and they said of course an llm would be able

**[1:11:40]** to solve something like this and then we take a screenshot of it we just put it into our Chad GPT app and it doesn't get the pattern and so I think it's very interest like it is a notable fact I was SED Playing devil's advocate against you

**[1:11:51]** on these kinds of questions but this is a very intriguing fact and I'm extreme I think I think this say prize is extremely interesting because we're going to learn we're going to learn something fascinating one way or another

**[1:12:00]** um so with regards to the 85% separate from this prize I'd be very curious if somebody could replicate that result because obviously in Psychology and other kinds of fields which this result seems to be analogous to when you run

**[1:12:16]** test on some small sample of people often they're hard to replicate so I'd be very curious if you try to replicate this how what does the average human perform on Arc um as for the difficulty on how long it will take to crack this

**[1:12:27]** Benchmark it's very interesting because the other benchmarks that are now fully saturated like MML math actually the people who made them Dan hendris and Colin Burns who did mlu in math I think they were grass students or college

**[1:12:41]** students when they they made it and the goal when they made it just a couple of years ago was that this will be a test of AGI and of course it got totally saturated I I I know you'll argue that these are test of memorization but I

**[1:12:52]** think the pattern we've seen in fact Epoch AI has a very interesting graph that I'll sort of overlay for the YouTube version here where you see this almost exponential where it gets you know 5% 10% 30% 40% as you increase the

**[1:13:06]** compute across models and then it just shoots up and in the gb4 technical report they had this interesting graph of the human eval problem set which was 22 coding problems and they had to graph it on the mean loog pass curve basically

**[1:13:22]** because early on in training or even smaller models can have the right idea of how to solve this problem but it takes a lot of reliability to make sure they stay on track to solve the whole problem and so you really want to upwade

**[1:13:35]** the signal where they get it right at least some of the time maybe one in 100 times one in a thousand and then so they go from like one in, one in 100 one in 10 and then they just like totally saturate it I guess the question I have

**[1:13:46]** this is all leading up to is why won't the same thing happen with Arc where people had to try really hard make bigger models um and then now they figured out these techniques that Jack Cole has figured out with only a 240

**[1:13:58]** million parameter language model that can get 35% shouldn't we see the same patter we saw across all these other benchmarks where you just like sort of eek out and then once you get the general idea then you just go all the

**[1:14:08]** way to 100 that's an imperical question so we see in practice what happens um but what what Jack is doing is actually very unique it's not just pre- training an nlm and and then prompt in it is actually trying to do active inference

**[1:14:21]** he's doing test time right he's doing like test time F test time f and this is actually trying to lift one of the key limitations of the LS which is that at inference time they cannot learn anything new they cannot adapt on

**[1:14:33]** the flight what they're seeing and is actually trying to uh uh learn so what he doing is effectively a form of program synthesis um because dlm contains a lot of useful building blocks like

**[1:14:47]** programming building blocks and by find units on the task at test time you are trying to assemble these building blocks into the right pattern that matches the that matches the task this is exactly what what program syn is about and the

**[1:15:00]** way I would contrast this approach uh with uh discret program search is that in discret program search so you're trying to assemble a program from a set of Primitives you have very few Primitives so people working on on this

**[1:15:14]** progam sear on Arc for instance they tend to work with dsls that have like 100 to 200 uh primitive programs so very small DSL but then they're trying to combine these Primitives uh into very uh complex programs so there's a very deep

**[1:15:30]** uh depth of search and uh on the other hand um if you look at what Jackal is doing with with LMS is that um he he's got this sort of like vector program uh database DSL of millions of building blocks in the llm that are mined by

**[1:15:48]** pretraining dlm not just on a ton of programming problems uh but also on millions of generated AR tasks uh so you have an extraordinar large DSL and then the fun tuning is very very shallow Rec combination of these Primitives so

**[1:16:05]** discret program search very deep Rec combination very small set of of primitive programs and the llm approach is the same but on the complete opposite end of that Spectrum where you scale up the memorization by a massive factor and

**[1:16:20]** you're doing very very shallow search but they are the same thing yeah just just different ends of the spectrum and I think where you're going to get uh the most value um for your for your compute Cycles is going to be somewhere in

**[1:16:35]** between you want to uh leverage memorization to build up a richer more useful Bank of reative programs and you don't want them to be hardcoded like what we saw for for the typical RDS you want them to be learned from examples

**[1:16:51]** but then you also want to do some degree uh uh of deep search as long as you're only doing very Shadow search you are limited to local generalization if you want to generalize further more broadly uh this this uh uh depth of search is

**[1:17:05]** going to be critical I I might argue that the reason that he had to rely so heavily on the synthetic data was because the he used a 240 million parameter model because the kago competition at the time required him to

**[1:17:20]** use a p100 GPU which has like a tenth or something of the flops of an h100 and so obviously he can't use if um uh if you believe that sort of scaling will solve this kind of reasoning then there you can just rely on the generalization

**[1:17:36]** whereas if you're using a much smaller for context for the listeners by the way the frontier models to are literally a THX bigger than that and so for your competition I from what I remember you the the submission you have to submit

**[1:17:50]** can't make any API calls can't go online no access and had to to run on Nvidia Tesla T4 p00 p00 oh is a p00 yeah okay so again it's like significantly less 12 hour on time limit basically there there's a forcing function of efficiency

**[1:18:05]** in the eval but here's the thing you only have 100 test tasks so the amount of comput you available for each task is actually quite a bit especially if you if you contrast that with the Simplicity of each task so it would be seven

**[1:18:17]** minutes per task basically which for you know people have tried to do these estimates of how many flops does a human brain have and you can take them with a grain of salt but as a sort of anchor they it's basically the amount of flops

**[1:18:29]** that h100 has and I guess maybe you would argue that well a human brain can solve this question in faster than 7.2 minutes so even with a t to the compute you should be able to do it in seven minutes um obviously we have less memory

**[1:18:42]** than you know like pedabytes of Fast Access Memory in the brain and with these you know 29 or whatever gigabytes in this uh h100 anyways I guess the BR question I'm asking is I um I wish there's a way to also test this

**[1:18:57]** prize with some sort of scaffolding on the biggest models as a way to test whether scaling is the path to get to um uh you know solving Arc absolutely so in the context of the competition we want to see how much progress we can do with

**[1:19:12]** limited resources but you're entirely right that it's a super interesting open question what could the biggest model ad there actually do on AR so we want to actually also make available a private sort of like oneoff uh track where you

**[1:19:27]** can submit to us a VM and so you can put on it uh any model you want like can you can take one of the largest open source models out there find youit do whatever you want uh and and you just give us an image and then you run it on the h100

**[1:19:41]** forac 24 hours or something and you see what you get I think it's worth pointing out that um there's uh two different test sets there is a public test set that's in the public GitHub repository that anyone can use to train you know

**[1:19:53]** put it in an open AP call whatever you'd like to do and then there's the private test set which is the 100 that is actually measuring the state of the art um so I think it is pretty openend and interesting to have folks attempt to at

**[1:20:03]** least use the public test set and go try it now there is an aster on any score that's reported on against the public test set because it is public it could have leaked into into the training data somewhere and this is actually what

**[1:20:14]** people are already doing like you can already try to prompt uh one one of the best models like the latest G the latest GPT 4 uh with tasks from the public Evolution set and you know again the problem is that these tasks are

**[1:20:27]** available as CH and files on GitHub these models are also trained on GitHub so they actually trained uh on these tasks uh and yeah that kind of that kind of creat uncertainty about if they can actually Sol some of the tasks is that

**[1:20:41]** because they memorize the answer or not um you know maybe you would you would be better off trying to create your own uh private AR clack a very novel test Set uh don't make the task difficult don't make them complex make them very obvious

**[1:20:56]** for humans but make sure to make them original as much as possible make them unique different and see how much your your your GPT 4 and so on or gp5 does on them well they're having test on whether these models are being overtrained on

**[1:21:10]** these benchmarks scale recently did this where on the GSM really interesting they basically replicated The Benchmark where with different questions and so some of the models actually were extremely overfit on The Benchmark like uh misol

**[1:21:23]** and so forth and the frontier models Claude and gbt actually did as well on their novel Benchmark that they did on the specific questions that were in the um existing public Benchmark so I would be relatively optimistic about them just

**[1:21:37]** sort of training on the Json I was joking with Mike that you should allow API access but sort of keep a an even more private validation set of these uh AR questions and so allow API access people can sort of play with gp4

**[1:21:54]** scaffold to enter into this contest and if it turns out maybe later on you run the validation set on the API and if it performs worse than the test set that you allowed the API access to originally that means that open AI is training on

**[1:22:07]** your API calls and you like go public with this and show them like oh my God they're you know they've like leaked your data we do want to make we want to evolve The Arc data set like that is that is a goal that we want to do I

**[1:22:17]** think France PA you mentioned you know it's not perfect yeah no Arc is not perfect for perfect B I mean I I made it like four years ago over four years ago almost five now um this was in a time before lams and I think we learned a lot

**[1:22:30]** actually since about uh what potential flaws there might be I think there is some redundancy in in the set of tasks which is of course against the goals of the Benchmark every task is supposed to be unique in practice that's not quite

**[1:22:43]** true uh I think there's also uh every task is supposed to be very novel but in practice they might not be they might be structurally similar to something that you might find online somewhere so we want to keep iterating and release an

**[1:22:57]** arc two version later this year and I think when we do that we're going to want to make uh the old private test Set uh available so maybe we won't be releasing it publicly but what we could do is uh just create a test server um

**[1:23:13]** where you can query get a task you submit a solution and of course you can use whatever Frontier Model you want there uh so that way because you actually have to quer this API you're making sure that no one is going to by

**[1:23:25]** accident train on this data it's unlike like the current public AR data which is literally on GitHub so there's no question about whether the models actually train on it yes they are because they're train on GitHub uh so by

**[1:23:36]** by sort of like getting uh access to quaring this CI would would avoid this issue and then we would see you know uh for people who actually want to uh try whatever technique they have in mind using whatever resources they they want

**[1:23:50]** uh that would be a way for them to get an answer I I wonder what might happen I not sure one answer is that they've come up with a whole new algorithm for AI with something some explicit program synthesis that now we're on a new track

**[1:24:03]** and another is they did something hacky with the existing models in a way that actually is valid which reveals that movie intelligence is more of getting getting things to the right part of the distribution but then it can reason and

**[1:24:17]** in that world I guess that that will be interesting and maybe that'll indicate that you know you had to do something hacky with current models is they get better you won't have to do something hacky um I'm also going to be very

**[1:24:28]** curious to see how these multimodal models if they will perform natively much better at ARK like test if Arc survives three months from here we'll we'll up the price uh I think we're about to make a really important moment

**[1:24:38]** of like contact with reality by blowing up the price putting a much big price pool against it we're going to learn really quickly if there's like lwh hanging fruit of ideas again I think new ideas are needed uh I think anyone

**[1:24:48]** listening this might have the idea in their head um and I'd encourage everyone to like give it a try um and I I think as time goes on uh that adds strength to the argument that um like we've sort of stalled out in progress and that new

**[1:24:59]** ideas are necessary to be dark yeah that's that's the point of having a money price is that you attract more people you get them uh to try to solve it and if there's an easy way to hack The Benchmark that reveals that The

**[1:25:10]** Benchmark is for then you're going to know about it in fact that was the point of the original uh C competition back in 2020 for Arc um I was running this competition because I had released this data set and I wanted to know if it was

**[1:25:24]** hackable if you could cheat uh so there was there was a a small money priz at the time that was like 20K uh and it were this was right around the same time as gpt3 was released H so people of course tried gpt3 on the on the public

**[1:25:37]** data it's scored zero um but I think uh what what the first context the first contest uh taught us is that there is no obvious shortcut right um and well now there's more money there's going to be more more people looking into it uh well

**[1:25:54]** we we're going to find out we're going to see if if the Benchmark is going to survive and you know if we end up with a solution uh that is not like trying to put Force the space of possible AR tasks that's just trained on core knowledge I

**[1:26:10]** don't think it's necessarily going to be in and by itself hii but it's probably going to be a huge milestone on the way to hii because what it represents is uh the ability to uh synthesize uh task a problem solving program from

**[1:26:28]** just two or three examples and that alone is a new way to program it's a it's an entirely new paradigm for software development where you can start programming potentially quite complex programs that will generalize very well

**[1:26:43]** and instead of programming them by uh coming up with the shape of the pro the the program in your mind and then typing it up um you're actually just showing the computer what ad put you want and you let the

**[1:26:56]** computer figure it figure it out I think that is extremely powerful I want to riff a little bit on what kinds of solutions might be possible here and which you would consider sort of defeating the purpose of Arc and which

**[1:27:08]** are sort of valid I'll one here here's one I'll mention which is um my friends Ryan and buck stayed up last night and because I told them about this and they were like oh of course solve this than for spring the word of course Al's going

**[1:27:21]** solve this and then so they were trying to prompt I think CLA Opus on this and they say they got 25% on the public Arc test um and what they've done did was have other examples of some of the arc tests and in context explain the

**[1:27:36]** reasoning of why you went from one output to another output and then now you have the current problem and I think also maybe expressing the Json in a way that is more amendable to the tokenizer and another thing was using

**[1:27:50]** the code interpreter so I'm curious actually what if if you think the code interpreter which keeps getting better as these models get smarter is just the program synthesis right there because what they were able to do was the actual

**[1:28:03]** output of the cells uh that the Json output they got through the code interpreter like right the Python program that gets right output here do you think that the program synthesis kind of researcher talking about will

**[1:28:14]** look like just using the code interpreter in large language models I think what solution we see that will score well is going to probably need to leverage some aspect from the planning models and llms in particular we've

**[1:28:27]** shown already that llms can do quite well that's basically the the Jack code approach we've also shown that pure descript PR search from a small DSL does very very well before jackco this was the stateof thee art in fact it still

**[1:28:39]** extremely close to the state of the art and there's no deing involved at all in these models so we have two approaches that have basically no overlap that are doing quite well and they're very much at two opposite ends of one Spectrum

**[1:28:53]** where on one and you have these extremely large Banks of millions of vector programs but very very shallow Rec combination like simplistic comination and on the other hand you have um very simplistic dsls very simple

**[1:29:06]** like 100 or 200 Primitives but very deep very sophisticated program search um the solution is going to be somewhere in between right so the people are going to be uh winning uh the AR competition and that we're going to be making the most

**[1:29:21]** progress towards near ter en are going to be S that managed to merge the Deep learning Paradigm and the discret for search Paradigm into one elegant way and you know you you ask like what would be uh legitimate and what would be cheating

**[1:29:36]** for instance so I think you want to add a code code interpreter uh to the system I think that's great that's so legitimate the part that would be cheating is try to uh anticipate what might be the test set

**[1:29:49]** like Brute Force the space of possible tasks and then train a memorization system on it and then rely on the fact that you're generating so many tasks like millions and millions and millions that inevitably there's going to be some

**[1:30:01]** of your lab between what you're generating and what's in in the test set I think that's defit uh the purpose of Benchmark because then you can just solve it without any need to adapt just by fetching a memorized solution uh so

**[1:30:13]** hopefully Arc will resist to that but you know nothing no Benchmark is necessarily perfect so maybe maybe there's a way to hack it and I guess we're going to get an answer very soon although I think some amount of fine

**[1:30:23]** tuning is valid because these models don't natively think in terms of especially the language models alone which the open source models that they would have to use to be competitive here compete here they're you know they're

**[1:30:33]** like natively language so they like need to be able to think in the in this kind of um yes the Arc Type way you want to input core knowledge like Ark like core knowledge into the model but surely you don't need tens of millions of tasks to

**[1:30:47]** do to do this like coaly is extremely basic if you look at some of these archetype questions I actually do think they rely a little bit on things I have seen throughout my life and for the same re like for

**[1:31:02]** example like something bounces off a wall and comes back and you see that pattern it's like I've played arcade games and I've seen like pong or something and I think for example when you see the Flyn effect and people's

**[1:31:12]** intelligence has measured on veren Progressive matrices increasing on these kinds of questions it's probably a similar story where since now since childhood we actually see these sorts of patterns in TV and whatever spatial

**[1:31:22]** patterns and so I don't think this is sort of core knowledge I think actually this is also part of the quote unquote fine-tuning that humans have as they grow up of seeing different kinds of spatial

**[1:31:33]** patterns and trying to pattern match to them I would definitely file that under core knowledge like uh core knowledge includes basic physics for instance bouncing or trajectories that would be included but yeah I think I think you're

**[1:31:45]** entirely right the reason why as a human you're able to quickly figure out the solution is because you have this set of building blocks this set of patterns in your mind that you can recombine is core knowledge required to attain

**[1:31:56]** intelligence any any algorithm you have does the core knowledge have to be in some sense hard-coded or can even the core knowledge be learned through intelligence core knowledge can be learned and I think in in the case of

**[1:32:06]** humans uh some amount of core knowledge uh is something that you're born with like we're actually born with a small amount of uh knowledge about the world we're going to live in we are not blank slates uh but most cor knowledge is

**[1:32:18]** acquired through experience but the the thing with scho knowledge that it's not going to be acquir like for instance in school it's actually acquired very very early in the first like three to four years of your life and by age four you

**[1:32:31]** have all the core knowledge you're going to need as an adult okay interesting uh so I mean on the prize itself I'm super excited to see both the open source versions of maybe with a llama uh 70b or something where people can score in the

**[1:32:45]** competition itself than if to sort of test specifically the scaling hypothesis I'm very curious to see if you can prompt on the public version of Arc which I guess won't be compet you won't be able to submit to this competition

**[1:32:58]** itself but I'd be very curious to see how if people can sort of crack that and get Arc working there and if that would update your reviews on AI it certainly be motivating we're going to keep running the contest until somebody puts

**[1:33:07]** a reproducible open source version into public domain so even if somebody privately beats EV or beats the arc eval we're going to still keep the price money until someone can reproduce it and put the public reproducible version out

**[1:33:18]** there yeah exactly like the goal is to accelerate progress towards the GI and a key part of that is that any sort of meaningful bits of progress needs to be shared needs to be public so so everyone can know about it and can try to iterate

**[1:33:31]** on it if there's no sharing there's no progress what I'm especially curious about is sort of disaggregating the bets of like can can we make an open version of this versus is this a thing that's just possible with scaling um and we can

**[1:33:44]** I guess test both of them based on the the public and the private version we're making contact with reality as well with this right we're going to learn a lot I think about what the actual limits of the compute were if someone showed up

**[1:33:53]** and hey here's a closed Source model that like I'm getting 50 plus% on I think that would probably update us on like okay perhaps we should increase the amount of compute that we give on the private test set in order to balance you

**[1:34:02]** know some of the decisions initially are somewhat arbitrary in order to learn about okay what's what do people want what does progress look like and um I think both of us are sort of committed to evolving it over time in order to be

**[1:34:11]** the best or the closest to perfect as that we can get it awesome and where can people go to learn more about the prize and maybe give their hand at it Parc pri.org which goes live today so it's live now $1 million is on the line

**[1:34:23]** people good thank you guys for coming on the podcast this is super fun to go through all the cruxes on intelligence and get a different perspective and also to announce a prize here so this is awesome thank you for helping break the

**[1:34:32]** news thank you for finding us
