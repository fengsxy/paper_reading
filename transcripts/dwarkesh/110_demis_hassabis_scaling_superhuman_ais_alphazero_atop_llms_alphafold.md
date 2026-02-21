---
date: 2024-01-01
layout: default
type: transcript
series: dwarkesh
episode: 110
guest: ""
title: "Demis Hassabis — Scaling, superhuman AIs, AlphaZero atop LLMs, AlphaFold"
source_url: "https://www.youtube.com/watch?v=qTogNUV3CAI"
analysis_url: /transcripts/dwarkesh/110_demis_hassabis_scaling_superhuman_ais_alphazero_atop_llms_alphafold.analysis/
permalink: /transcripts/dwarkesh/110_demis_hassabis_scaling_superhuman_ais_alphazero_atop_llms_alphafold/
---

# Transcript: Demis Hassabis — Scaling, superhuman AIs, AlphaZero atop LLMs, AlphaFold

Source: https://www.youtube.com/watch?v=qTogNUV3CAI

---

**[00:00]** so I wouldn't be surprised if we had AGI like systems within the next decade it was pretty surprising to almost everyone including the people who first worked on the scating hypotheses that how far it's gone in a way I look at the large models

**[00:13]** today and I think they're almost unreasonably effective for what they are it's an empirical question whether that will hit an ASM toope or a brick wall I think no one knows when you think about superhuman intelligence is it like still

**[00:23]** controlled by a private company as Gemini are becoming more multimodal and we start ingesting audio visual d as well as text Data I do think our systems are going to start to understand the physics of the real world better the

**[00:36]** world's about to become very exciting I think in the next few years as we start getting used to the idea of what true multimodality means okay today it is a true honor to speak with Demis aavas who is the CEO of

**[00:49]** Deep Mind deis welcome to the podcast thanks for having me first question given your Neuroscience background how do you think about intelligence specifically do you think it's like one higher level General reasoning circuit

**[01:00]** or do you think it's thousands of independent subskills and humanistics well it's interesting because intelligence is so uh uh Broad and um you know what we use it for is is so sort of generally applicable I think

**[01:15]** that suggests that you know there must be some sort of high level uh uh common things in you know common kind of algorithmic themes I think around how the brain processes the world around us so um of course that then there are

**[01:30]** specialized parts of the brain that that do specific things um but I think there probably some underlying principles that underpin all of that yeah how do you make sense of the fact that in these llms though when you give them a lot of

**[01:42]** data in any specific domain they tend to get asymmetrically better in that domain uh wouldn't we expect a sort of like General Improvement across all the all the different areas well I think you first of all I think you do actually

**[01:53]** sometimes get surprising Improvement in other domains when you improve in a specific domain so for example uh when the large models sort of improve it coding that can actually improve their General

**[02:04]** reasoning so there there is some evidence of some transfer although I think we would put we would like a lot more evidence of that um but also you know that's how the human brain learns too if if we experience and practice a a

**[02:16]** lot of things like chess or you know writing creative writing or whatever that is we also tend to specialize and get better at that specific thing even though we're using uh sort of General learning techniques and general Learning

**[02:27]** Systems in order to uh you know to get good at that domain yeah what's been the most surprising example of this kind of transfer for you like you see language and code or images and text what's yeah I think probably um I mean I'm hoping

**[02:40]** we're going to see a lot more of this China to transfer but but I think uh things like getting better at coding uh and math and generally improving your reasoning um that is how it works with us as as human learners but uh I think

**[02:52]** it's interesting seeing that in in these in these artificial systems and can you see the sort of mechanistic way in which uh let's say in the language and code example there's like I I found the place in a neural network that's getting

**[03:03]** better with both the language and the code or is it is it that too too far down the we yeah well I don't think our analyst analysis techniques are quite sophisticated enough to be able to hone in on that um I think that's actually

**[03:14]** one of the areas that um a lot more research needs to be done on kind of mechanistic analysis of the representations that these systems build up and um you know I sometimes like to call it virtual brain analytics in a way

**[03:25]** it's a bit like doing uh fmri or single cell recording from from a real brain U what's the analogous sort of analysis techniques for these artificial minds and um there's a lot of great work going on on this sort of stuff people like

**[03:39]** Chris Ola uh I really like his work and a lot of computational Neuroscience techniques I think could be brought to bear uh on uh analyzing these current systems we're building in fact I Tred to encourage a lot of my computational

**[03:50]** Neuroscience friends to to to start thinking in that direction and applying their knoow um uh to the to the to the large models yeah what do what do other AI researchers not understand about human intelligence that you you you have

**[04:04]** some sort of like Insight on given your Neuroscience background I I I think um Neuroscience has added a lot uh if you look at the last sort of 10 20 years that that we've been at it at least and and you know I've been thinking about

**[04:15]** this for 30 plus years um I think in the earlier days of the sort of new wave of AI I think Neuroscience was providing a lot of interesting directional Clues so things like reinforcement learning combining that with deep learning you

**[04:29]** know some of our pioneering work we did there things like experience replay um even the notion of attention which has become super important um a lot of those uh original sort of Inspirations come from some understanding about how the

**[04:43]** brain works not the exact specifics of course you know one's an engineered system the other one's a natural system so it's not so much about a onetoone mapping of a specific algorithm it's more kind of inspirational Direction

**[04:54]** maybe some ideas for architecture or algorithmic ideas or representational ideas um and because you know you know the brains in existence proof that general intelligence is possible at all I think um you know the history of human

**[05:06]** Endeavors has been that once you know something's possible it's easier to push hard in that direction because you know it's a question of effort then uh and sort of a question of when not if um and that allows you to you know I think make

**[05:18]** progress a lot more quickly so I think neurosciences has had a lot of um uh has inspired a lot of the thinking uh at least in a soft way uh behind where we are today um but as for you know going forwards um

**[05:33]** I think that there's still a lot of interesting um things to be resolved around planning and um how does the brain construct the right World models um you know I studied for example uh how the brain does imagination or you can

**[05:47]** think of it as uh mental simulation so how do we create you know very rich visual spatial simulations of the world in order for us to plan better yeah actually I'm curious how you think that will sort of interface with llm so

**[05:59]** obviously deep minders at the frontier and has been for many years you know with systems like ala zero and so forth of having these agents who can like think through different steps to get to an end outcome um are will this just be

**[06:10]** is a path for LMS to have this sort of uh Tre search kind of thing on top of them how do you think about this I think that's a super promising Direction in my opinion so you know we've got to carry on improving uh the large models and

**[06:22]** we've got to carry on um basically making the more and more accurate predictors of the world so in effect making the and more reliable World models that's clearly a necessary but I would say probably not sufficient

**[06:34]** component of an AGI system um and then on top of that I would you know we're working on things like Alpha zero like planning mechanisms on top that make use of that model in order to make concrete plans to achieve certain goals in the

**[06:47]** world um and and perhaps sort of chain you know chain thought together or lines of reasoning together and maybe use search to kind of explore massive spaces of possibility I think that's kind of missing from our current large models um

**[07:01]** how do you get past the sort of uh uh immense amount of compute that these approaches tend to require so even the alago uh system was you know a pretty expensive system um because you had to do the sort of running an L LM on each

**[07:14]** node of the tree uh how how do you anticipate that'll get more made more efficient well I mean one thing is Mo law tends to tends to tends to tends to help uh if if you know over every every year of course um um more computation

**[07:26]** comes in but um we focus a lot on iici You Know sample efficient methods and and and reusing uh existing data things like experience replay um and also just looking at uh more efficient ways I mean the better your world model is the more

**[07:41]** efficient your search can be so one example I always give with Alpha zero our system to play go and chess and you know any game is that um it's stronger than world champion level human world champion level at all these games um and

**[07:54]** it uses a lot less search than a brute force method um like deep blue say to play chess deep blue one of these traditional stockfish or deep blue um systems would maybe look at millions of uh possible moves for every decision

**[08:07]** it's going to make alpha zero and Alpha go made you know looked at around T tens of thousands of um possible positions in order to make a decision about what to move next but a human grandmas a human world champion uh probably only looks at

**[08:22]** a few hundreds of moves even the top ones in order to make their very uh good decision about what to play next so that suggests that obviously the Brute Force systems don't have any real model other than theistic about the game Alpha zero

**[08:36]** has quite a decent uh uh model but the world but the human you know human top human players have a much richer much more accurate model than of go or chess so that allows them to make you know worldclass decisions on a very small

**[08:50]** amount of search so I think there's still there's a sort of tradeoff there like you know if you improve the models then I think your search can be more efficient and therefore you can get further with your search yeah I have two

**[09:01]** questions based on that uh the first being with Alpha's go you had um a very concrete wi condition of you know at the end of the day do I win this game ago or not and you can reinforce on that how when you're just thinking of like an llm

**[09:12]** putting out thought what will do you think there will be this kind of ability to discriminate uh in the end whether that was like a good good thing to reward or not well of course that's why we you know we pioneered and and Deep

**[09:22]** Mind sort of famous for using games as a Proving Ground um partly because obviously it's efficient to research that domain but the other reason is obviously it's it's you know extremely easy to specify reward function winning

**[09:34]** the game or improving the score something like that sort of built into most games so that is the the that is the that one of the challenges of real well systems is how does one Define uh the right objective function the right

**[09:44]** reward function um and the right goals um and specify them in a in in you know in a general way but they're specific enough and and and actually points the system in the right direction and um for real world problems that can be a lot

**[09:58]** harder but actually if you think about it uh in even scientific problems uh there are usually ways that you can specify the goal that you're after and then when you think about human intelligence you're just saying well you

**[10:09]** know the humans thinking about these thoughts are just super sample efficient um how Einstein coming up with relativity right there's just like thousands of possible permutations of the equations do you think it's also

**[10:18]** this sort of sense of like different humanistics of like I'm going to try out this approach instead of this or is it a totally different way of approaching coming with that solution uh than you know what offo does plan the next yeah

**[10:29]** well look I think it's different because there's our brains are not built for doing Monte Carlo treesearch right um it's it's it's just not the way uh uh our organic brains would work um so I think that in order to compensate for

**[10:42]** that you know people like Einstein have come up you know their brains have using their intuition and you know we maybe come to what intuition is but they use their sort of knowledge and their experience to build extremely you know

**[10:54]** in the Einstein's case extremely accurate models of physics including these sort of mental simulations I think if you read about Einstein and how he came up with things he used to visualize and sort of uh really kind of um uh feel

**[11:07]** what these physical systems should be like not just the mathematics of it but have a really intuitive feel for what they would be like in reality and that allowed them to think these these these sort of very outlandish thoughts at the

**[11:18]** time um so I think that it's it's it's the sophistication of the world models that we're building which then you know if you imagine your world model can get you to a certain node in a in a tree that you're searching and then you just

**[11:29]** do a little bit of search around that node that leaf node and that gets you to these original places but obviously if your model is and your judgment on that model is is very very good then you can pick which Leaf nose you should sort of

**[11:43]** expand with search much more accurately so therefore overall you do a lot less search I mean there's no way that you know any human could could do a kind of Brute Force search over any any kind of significant space yeah yeah yeah um a

**[11:56]** big sort of open question right now is whether RL will allow these models to do the selfplay synthetic data to get over dat data bottleneck it sounds like you're optimistic about this yeah I'm very optimistic about that I mean I

**[12:05]** think uh well first of all there's still a lot more data I think that can be used especially if one views like multimodal and video and these kind of things and uh obviously you know society's adding more data all the time um but I think uh

**[12:20]** uh to the internet and things like that but I think that uh there's a lot of scope for creating synthetic data um we're looking at that in different ways um partly through simul using very realistic games environments

**[12:32]** for example toate realistic data but also selfplay so that's where um systems um interact with each other or or or converse with each other um and in the sense of we know what very well for us with alphao and Alpha zero where we got

**[12:47]** the systems to play against each other and actually learn from each other's mistakes and and build up a knowledge base that way and I think there are some good analogies for that it's a little bit more complicated but to to to build

**[12:57]** a general kind of world data how do you get to the point where these models the um the sort of synthetic data they're outputting the self they're doing uh is is not just more of what they've already got in their data set

**[13:08]** but is something they haven't seen before do you know what I mean to actually improve the abilities yeah so there I think there's a whole uh science needed and and I think we're still in the nent stage of this of data cation

**[13:18]** and data analysis so actually analyzing uh the holes that you have in your data distribution uh and this is important for things like fairness and bias and other stuff to remove that from the system is to is to try and really make

**[13:30]** sure that your data set is representative of the distribution you're trying to learn and uh and you know there are many tricks there one can use like overweighting or replaying certain parts of the data or you could

**[13:40]** imagine if you identify some some Gap in your data set that's where you put your synthetic generation capabilities to work on yeah so you know but nowadays people are paying attention to uh the the RL stuff that Al deep-minded many

**[13:54]** years before what are the sort of either early research directions or something that was done way back in the past but people just haven't been pay attention to that you think will be a big deal right like there's a time where people

**[14:03]** weren't paying attention to scaling what's the thing now where it's like totally underrated well actually I think that you know there's the the history of the sort of last couple of decades has been things coming in and out of fashion

**[14:13]** right and and I I do feel like um a while ago when you know maybe five plus years ago when we were were pioneering with alphao and before that dqn where it was the first system with you know that worked on Atari our first big system

**[14:25]** really more than 10 years ago now that scaled up Q learning and reinforc learning techniques to deal you know combine that with deep learning uh to create deep reinforcement learning and then uh use that to scale up to complete

**[14:36]** some you know Master some pretty complex tasks like playing Atari games just from the pixels and uh I do actually think a lot of those ideas um need to come back in again and as we talked about earlier combine it with the new advances in

**[14:50]** large models and large multimodal models which is obviously very exciting as well so I do think there's a lot of potential for combining uh some of those older ideas together with the new ones uh is there any potential for something to

**[15:02]** come uh the AGI to eventually come from just a pure RL approach like the the way we're talking about it it sounds like there'll be uh the llm will form the right prior and then this sort of research will go on top of that is there

**[15:14]** possibility to just like completely out of I think I certainly you know that theoretically I think there's no reason why you couldn't go full Alpha zero like on it and there are some people uh here at Deep at Google Deep Mind and and and

**[15:25]** in the RL Community who work on that right um for uh assuming no priors uh no data and and just build all knowledge from scratch um and I think that's valuable because of course you could you know those those

**[15:39]** ideas and those algorithms should also work when you have some knowledge too um but having said that I think by far probably my betting would be the quickest way to get to AGI and the most likely plausible way is to um use all

**[15:51]** the knowledge that's existing in the world right now on things like the web and that we've collected and we have these scalable uh algorithms like like um Transformers that are capable of ingesting all of that information and I

**[16:03]** don't see why you wouldn't start with a model as a kind of Prior or or to build on and to make predictions that helps bootstrap your learning I just think it it doesn't make sense not to make use of that so my my my betting would be is

**[16:16]** that um you know the final AGI system will have these large multimodels um models as part of the the overall solution but probably U won't be enough on their own you need this additional planning search on top okay this sounds

**[16:32]** like the answer to the question I'm about to ask which is um what what is somebody who's been in this field for a long time and seen different Trends come and go what do you think that strong version of the scaling hypothesis gets

**[16:42]** right and what does it get wrong there just the idea that you just throw up computed a wide enough distribution of data and you get intelligence yeah look my my view is this is kind of an empirical question right now so I think

**[16:50]** it was pretty surprising to almost everyone including the people you know who who first worked on the scaling hypotheses that how far it's gone in a way I I mean I sort of look at uh the large models today and I think they're

**[17:02]** almost unreasonably effective for what they are you know um I think it's pretty surprising some of the properties that emerg things like you know it's clearly in my opinion got some form of Concepts and abstractions and some things like

**[17:14]** that and I think if we were talking five plus years ago I would have said to you maybe we need an additional algorithmic breakthrough uh in order to to do that like um you know maybe more like the brain works and and I think that's still

**[17:26]** true if we want explicit abstract Concepts NE Concepts but it seems that these systems can implicitly learn that another really interesting I think unexpected thing was that these systems have some sort of grounding um you know

**[17:38]** even though they don't experience the world multimodally or at least until more recently when we have the multimodal models and uh that's surprising that that the amount of information that can be uh and and

**[17:48]** models that can be built up just from language and I think I have some hypothesis about why that is um I think we get some grounding through the rhf feedback systems because obviously the human r

**[17:58]** are by definition grounded uh grounded people we're grounded right in in reality so our feedback is also grounded so perhaps there's some grounding coming in through there and also maybe language contains more grounding you know if in

**[18:11]** the if you if you're able to ingest all of it then we then we perhaps thought or linguists perhaps thought before so actually some very interesting philosophical questions I think we haven't we people haven't even really

**[18:21]** scratched the surface off yet uh the the looking at the advances that have been made um you know it's quite interesting to think about where going to go next but in terms of your question of like the you know large models I think we've

**[18:33]** got to push scaling as as hard as we can and that's what we're doing here and you know it's an empirical question whether that will hit an ASM toope or a brick wall and there are you know different people that argue about that but

**[18:44]** actually I think we should just test it I think no one knows um and but in the meantime we should also double down on Innovation and invention and this is something that that that that Google research and deep mind and Google brain

**[18:56]** have have have have you know we've pioneered many many things over the last decade that's something that's our bread and butter and um you know you can think of half our effort as to do with scaling and half our efforts to in do with

**[19:07]** inventing the next architectures the next algorithms that will be needed um knowing that you've got this scaled larger and larger model coming along the lines so I I I I my my betting right now but it's a loose betting is that you

**[19:20]** would need both um but I think you know it's you got to push both of them as hard as possible and we're in a lucky position that we can do that yeah I want to ask more about the ground so you can imagine two things that might change

**[19:30]** which would make the grounding more difficult one is that as these models get smarter they're going to be able to um operate in domains where we just can't generate enough human labels just because we're not smart enough right so

**[19:40]** if it does like a million line pull request you know how how do we tell it like this is this is within the constraints of our morality and the end goal we wanted and this isn't and the other is it sounds like you're saying

**[19:50]** more of the compute so far we've been doing you next token prediction and in some sense it's a guard rail because you're you have to talk as a human would talk and think as a human would think now if additional compute is going to

**[20:01]** come in the form of uh reinforcement learning where just get to the end objective uh we can't really Trace how you got there um when you combine those two how worried are you that the sort of grounding goes away well look I I think

**[20:14]** um uh if the grounding you know if it's not properly grounded the system won't be able to achieve those goals properly right I think so I think in a sense you sort of have to have the grounding or at least some of it in order for a system

**[20:26]** to actually achieve goals in the real world um I do actually think that as these systems and things like Gemini are becoming more multimodal um and we start ingesting things like video and and and

**[20:37]** and and and you know audio visual data as well as Text data and then you know the system starts correlating those things together um I do I think that is a form of of proper grounding actually so so I do think our systems are going

**[20:52]** to start to understand you know the physics of the real world better and then one could imagine the active vers version of that is being in a very realistic simulation or game environment where you're starting to learn about

**[21:03]** what your actions do in the world and um and how that affects uh uh uh uh uh the world itself the world stay itself but also what next learning episode you're getting so you know these RL agents we we've always been working on and

**[21:16]** pioneered like Alpha zero and Alpha go um they actually affect their active Learners what they decide to do next affects what uh the next learning uh piece of data or experience they're going to get so there's this interesting

**[21:28]** sort of feedback loop and of course if we ever want to be good at things like robotics we're going to have to understand how to act in the real world yeah so there's a grounding in terms of will the capabilities be able to proceed

**[21:39]** or will they be like enough in touch with reality to be able to like do the things we want and there's another sense of grounding of um we've gotten lucky in the sense that since they're trained on human thought they like maybe think like

**[21:48]** a human to what extent does that stay true when more of the compute for trading comes from just did you get the right outcome and not guard Real by like are you like proceeding on next token is a human wood maybe the broader question

**[22:00]** I'll like post to you is um and this is what I asked Shane as well what would it take to align a system that's smarter than a human maybe things in Alien Concepts uh and you can't like really monitor the million line employ request

**[22:10]** because it's you can't really understand the whole thing and you can't give labels look this is something Shane and I and many others here we've had that Forefront of our minds for since before we started Deep Mind and um because we

**[22:20]** plann for Success crazy you know 2010 no one was thinking about AI let alone AGI but we we already knew that if we could make progress with the system and these ideas it you know the technology that would be created being unbelievably

**[22:32]** transformative so we already were thinking you know 20 years ago about well what how you know what would the consequences of that be both positive and negative of course the positive direction is amazing science things like

**[22:43]** Alpha fold incredible breakthroughs in health and science uh and and maths and Discovery uh scientific discovery um but then also we got to make sure these systems are sort of understandable and controllable and I think there's sort of

**[22:55]** several you know this would be a whole sort of discussion in itself but there are many many ideas that people have from much more stringent eval systems I think we don't have good enough evaluations and benchmarks for things

**[23:06]** like can the system deceive you uh can it exfiltrate its own code sort of undesirable behaviors um and then there's uh you know ideas of actually using AI maybe narrow AIS so not General learning ones but systems that are

**[23:22]** specialized for a domain to help us as the the the the human scientists analyze and summarize what the more General system is doing right so kind of narrow AI tools um I think that there's a lot of Promise in in creating hardened

**[23:36]** sandboxes or simulations so that um that are hardened with cyber security uh uh Arrangements around the simulation both for to keep the AI in but also uh as cyber security to keep hackers out and and then you could experiment a lot more

**[23:53]** uh freely within that sandbox domain and I think um a lot of these ideas are uh and there's many many others um including the analysis stuff we talked about earlier where can we analyze and understand what the concepts are that

**[24:05]** this systems building what the representations are so maybe they're not so alien to us and we can actually um keep track of uh uh the kind of knowledge that it's building yeah yeah um stepping back a bit I'm curious what

**[24:16]** your timelines are so Shane said his like I think modal outcome is 2028 I think that maybe median yeah what is yours yeah well I you know I I I I I don't have prescrib kind of specific numbers to it because I think there

**[24:27]** there's so many unknown and uncertainties and and and um you know human Ingenuity and Endeavor comes up with surprises all the time so that could meaningfully move the the the the the timelines but I will say that when

**[24:39]** we started deep mine back in 2010 you know we thought of it as a 20-year project and and actually I think we're on track which is kind of amazing for 20 year projects because usually they're always 20 years away right so that's the

**[24:50]** joke about you know whatever it is quantum AI you know take your pick and um but I think we you know I think we're on track so I wouldn't be surprised if we had AGI like systems within the next decade M and do you buy the model that

**[25:03]** once you have an AGI you can have you have a system that basically speeds up further AI research maybe not like an overnight sense but you know over the course of months and years you have much faster progress than you would have by

**[25:12]** the right side I I think that's potentially possible um I I think it partly depends what we uh decide we as society decide to use the first AGI nent AGI systems or even Proto AGI systems for um so uh you know even the current

**[25:27]** llms seem to be pretty good at coding so uh and you know we have systems like Alpha code we also got the improving systems so one could imagine uh combining these ideas together and and and and and making them a lot better and

**[25:39]** then I I I could imagine these systems being quite good at at at at designing and helping us uh build future versions of themselves um but we also have to think about the safety implications of that of course yeah I'm curious what you

**[25:51]** think about that so I mean I'm not saying this is happening this year or anything but eventually you'll be developing a model where during the process of development you think you know there's some chance that once this

**[26:00]** is fully developed it'll be capable of like an intelligence explosion like Dynamic um what would have to be true of that model at that point where you're like you know I've seen these specific evals I've like i' I've like understand

**[26:12]** it's internal thinking enough and like it's future thinking that I'm comfortable continuing development of the system well look we need um we need a lot more understanding of the systems than we do today before I would be even

**[26:22]** confident of even explaining to you what we would need to tick box there so I think what we've got to do in the next few years in the time we have before those systems start arriving is is is come up with the right uh evaluations

**[26:35]** and metrics and maybe ideally formal proofs but you know it's going to be hard for these types of systems but at least empirical uh uh bounds around what these systems can do um and that's why I think about things like deception and as

**[26:49]** being quite root node traits that you don't want because if if you're confident that your system is is is is is tell is is sort of exposing what actually thinks then you could potentially that opens up possibilities

**[27:01]** of using the system itself to explain aspects of itself to you um the way I think about that actually is like um if I was to play a game of chess against Gary Kasparov right which which I played in the past or Magnus Carlson you know

**[27:13]** the amazing chess players Grace all time you you I wouldn't be able to come up with a move that they could but but they could explain to me um why they came up with that move and I could understand it uh uh post Hawk right and and that's the

**[27:27]** thing one could imagine uh one of the um capabilities that we could make use of these systems is for them to explain it uh to us and even maybe the proofs behind why they're thinking something certainly in a mathematical

**[27:41]** any mathematical problem got it um do do you have a sense of what the the converse answer would be so what would have to be true where tomorrow morning you're like oh man I I didn't anticipate this you see some specific observation

**[27:51]** tomorrow morning where like we got to stop Gemini 2 training like is what would specifically I could imagine that like um and this is where uh you know things like the sandbox simulations I I would hope we we're we're experimenting

**[28:02]** in a in a safe secure uh environment and then you know something happens in it where um very unexpected happens a new unexpected capability or something that we didn't want you know explicitly told the system we didn't want that it did

**[28:16]** but then lied about you know these are the kinds of things where one would want to then dig in carefully um you know n with the systems that are around today which are not dangerous in my opinion today but in a few years they might be

**[28:31]** have have potential um and then you would sort of ideally kind of pause and then really get to the bottom of um uh why it was doing those things before one continued yeah going back to Gemini I'm curious uh what the bottlenecks were in

**[28:46]** the development um like why not make it immediately one order of magnitude bigger uh if FL scaling works well look first of all there are practical limits how much compute that can you actually fit in one data

**[28:57]** and you know you're you're bumping up against very interesting um uh you know distributed computing kind of challenges right we unfortunately we have some of the best people in the world on on those challenges and and you know cross data

**[29:11]** center training all these kinds of things very interesting challenges Hardware challenges and we have our tpus and so on that we're building and designing all the time as well as using gpus and so um there's all of that and

**[29:23]** then you also have to the scaling laws you know they don't they don't just work by Magic you sort of you still need to scale up the hyper parameters and various Innovations are going in all the time with each new scale it's not just

**[29:34]** about repeating the same recipe at each new scale you have to adjust the recipe and uh and that's a bit of an art form in a way and you have to sort of almost get new data points if you try and extend your predictions extrapolate them

**[29:46]** say several orders of magnitude out sometimes they don't hold anymore right because um new capabilities they can be step functions in in terms of new capabilities and and and and some things just just some things hold and other

**[29:58]** things don't so often you you do need those intermediate data points actually to to correct uh uh some of your hyper parameter optimization and other things so that that the scaling law continues to be true so um so there's sort of

**[30:11]** various practical limitations onto onto that um so you know kind of one order of magnitude is about probably the maximum that you want to you want to carry on uh you want to sort of do between each uh each era oh that's so fascinating uh you

**[30:25]** know in the gp24 technical report they say that they were able to predict the the training loss um you know tens of thousands of times less compute than gbd4 they could see the curve but at the point you're making is that the actual

**[30:36]** capabilities that loss implies uh may not be the downstream capabilities sometimes don't follow from the you can often predict the the core metrics like training loss or or something like that but then um it doesn't actually

**[30:47]** translate into MML or math or or some other actual uh capability that you care about it's they're not they're not necessarily linear all the time so there're sort of nonlinear effect what was the biggest surprise to you during

**[30:58]** the development of Gemini of some something like this happening um well I I mean I I wouldn't say there was one big surprise but it's it was very interesting you know trying to train things at that at that size and and and

**[31:10]** learning about um uh all sorts of things from organization or how to babysit such a system and and to track it and and I think things like getting a better uh understanding of of the the metrics you're optimizing versus the the final

**[31:24]** capabilities that you want um I would say that still not a perfectly understood uh uh uh uh mapping but but it's an interesting one that we're getting better and better at yeah yeah there's a perception that maybe other

**[31:34]** lives are more compute efficient uh than de mind has been with Gemini I don't know what you make of that forcep uh I don't think that's the case I mean you know it's uh uh I I think that that actually Gemini 1 used roughly the same

**[31:47]** amount of comp maybe slightly more than than what was rumored for gp4 I don't know exactly what was was used so um I think it's was in the same ballpark um I think we're very efficient with our computer and we use our compute for many

**[31:58]** things one is not just the scaling but going back to earlier to these more Innovation and and ideas you've got to you know it's only useful a new innovation a new invention if it also can scale so so in a way um you also

**[32:12]** need quite a lot of compute to do new invention uh because you got to test many things at at least some reasonable scale and make sure that they work at that scale and also some new ideas may not work at a toy scale but do work at a

**[32:25]** larger scale and in fact those are the more valuable so you actually if you think about that exploration process you need quite a lot of compute to be able to do that um I mean the good news is is I think you

**[32:35]** know we we're pretty lucky at at Google that we I think we this year certainly we're going to have the most compute by far of of any sort of research lab and you know we hope to make very efficient and good use of that in terms of both

**[32:46]** scaling uh and the capability of our systems and also new inventions yeah what's been the biggest surprise to you uh if you go back to uh yourself in 2010 when you're starting Deep Mind in terms of what eii progresses look like did you

**[32:58]** anticipate back then that it would in some large sense amount to spend you know dumping billions of dollars into these models or did you have a different sense of what it would look like we thought that and actually you know if

**[33:07]** you I know you've interviewed my my colleague Shane and and and he he always thought that in terms of like um compute curves and and then maybe comparing roughly to like the brain and how many neurons and copses there are very

**[33:19]** Loosely but we're actually interestingly in that kind of regime now roughly in the right order of magnitude of you know number of copses in the brain and and and and the sort of compute that we have but I think more fundamentally you know

**[33:31]** we we always thought that um we bet on generality and learning right so th those were always at the core of the any Technique we would use that's why we triangulated on reinforcement learning and search and and and and deep learning

**[33:44]** right as three types of algorithms that that would scale and um and and would be very general and and not require a lot of handcrafted human priors which we thought was the sort of failure mode really of of the efforts to build AI uh

**[33:59]** in the '90s right places like MIT where where there were very you know logic based systems expert systems you know masses of hand coded handcrafted human information going into that turned out to be wrong or or too rigid so we wanted

**[34:12]** to move away from that I think we spotted that Trend early and uh became you know and obviously we we use games as our Proving Ground and we did very well with that and I think all of that was very successful and I think maybe

**[34:24]** inspired others uh to you know things like alphao I think was a big moment for inspiring many others to think oh actually these systems are ready to scale and then of course with the Advent of Transformers invented by our

**[34:35]** colleagues at Google you know research and brain that was the then you know the the the type of deep learning that allowed us to ingest massive of amounts of information and that uh of course is really turboed where we are today so I

**[34:47]** think that's all part of the same lineage um I you know we we couldn't have predicted every Twist and Turn there but I think the general direction we were going in um uh was the right one yeah and in fact it's it's like

**[34:58]** fascinating because if you like read your Ro papers or Shane's old papers uh Shane's thesis I think in 2009 he said like well you know the way we would test for AI is if can you compress wikkipedia and that's like literally the loss

**[35:07]** function of RMS or like your own paper in like 2016 before Transformers where you said like uh you were comparing neuroscience and um Ai and he said attention is what is needed and exactly exactly so we had these things called

**[35:18]** out and and actually we had some early attention papers but they weren't as elegant as Transformers in the end like new cheing machines and things like this yeah and then Transformers was the was the nicer and more General architecture

**[35:30]** of that yeah yeah yeah um when you when you extrapolate all this out forward and you think about superhuman intelligence or is um like what does that landscape look like to you is it is it like still

**[35:40]** controlled by a private company like what should the governance of that look like uh concretely yeah look I I would love um you know I think that this has to be uh uh this is so consequential this technology I think it's much bigger

**[35:53]** than any one company or or or or even industry in general I think it has to be a big collaboration with many stakeholders from Civil Society Academia government and the good news is I think with the popularity of the recent

**[36:07]** chatbot systems and so on I think that has woken up uh uh many of these other parts of society that this is coming and what it would be like to interact with these systems and that's great so it's opened up lots of doors for very good

**[36:19]** conversations I mean example of that was the safety Summit AT in the UK hosted few months ago which I thought was a big success to start getting this inter National dialogue going and and and you know I think the whole of society needs

**[36:31]** to be involved in deciding what do we want to deploy these models for how do we want to use them what do we not want to use them for you know I think we got to try and get some International consensus around that uh and then also

**[36:41]** making sure that the benefits of these systems uh uh benefit everyone you know for the good of everyone and Society in general and that's why I push so hard things like AI for Science and and I hope that you know with things like our

**[36:54]** spin out isomorphic we're going to start curing diseases you know terrible diseases with AI and accelerate drug Discovery amazing things climate change and other things I think big challenges that face us uh at face Humanity um

**[37:05]** massive challenges actually which I'm optimistic we can solve uh because we've got this incredibly powerful tool coming along down the line of AI uh that we can apply and I think help us and uh solve many of these problems so you know

**[37:18]** ideally we would have a big uh consensus around that and and and a big discussion you know sort of almost like the UN level if possible you know one interesting thing is if you look at these systems they you chat with

**[37:30]** them and they're they're immensely powerful and uh intelligent um but it's interesting to the extent of which they haven't like automated large section of the economy yet um whereas five years ago I showed you Gemini you'd be like

**[37:41]** wow this is like you know totally coming for a lot of things so how do you account for that like what's going on where it hasn't had had the broader impact yet yeah I think it's we're still I think that just shows we're still at

**[37:50]** the beginning of of of this new era um and I think that for these systems I think there are some interesting use cases you know um you know where you can use things to you know these these these chatbot systems to summarize stuff for

**[38:03]** you and and maybe do some simple writing and uh uh maybe more kind of boilerplate type writing but that's only a small part of what you know we we all do every day so I think for more General use cases um I think we need still need new

**[38:18]** capabilities uh things like um planning and search but also maybe things like personalization and memory episodic memory so not just on context windows but actually remembering what I what we spoke about a 100 conversations ago um

**[38:32]** and I think once those start coming in I mean I'm really looking forward to things like recommendation systems that that help me find better more enriching material whether that's books or films or music and so on you know I would use

**[38:44]** that type of system every day so I think we're just scratching the surface of uh uh what these AI say assistance could actually do uh for us in our general everyday lives and also in our work context as well I think they're not

**[38:57]** reliable yet enough to do things like science with them but I think one day you know once we fix factuality and grounding and other things um I think they could end up becoming like you know the world's best research assistant for

**[39:08]** for you as a as a scientist or as a as a as a as a clinician I want to ask about memory by the way um you had this fascinating paper in 2007 where you talk about the links between memory and Imagination and

**[39:20]** how they in some sense are very similar um uh you people often claim that these models are just memorizing how do you think about that claim that people make um is is memorization all you need because in some some deep sense that's

**[39:32]** compression or you know what's your intuition here yeah I mean sort of at the limit one one maybe could try and memorize everything but it wouldn't generalize out of out of your distribution and I think these systems

**[39:41]** are clearly I think the early the Early uh um criticisms of these early systems uh were that they were just regurgitating and memorizing but I think clearly the new era the gem and IG pt4 type era they are definitely

**[39:54]** generalizing to new constructs um so but actually you know in my thesis and and that paper particularly uh that started that area of imagination in Neuroscience was showing that you know first of all memory certainly at least human memory

**[40:07]** is a reconstructive process it's not a videotape right we sort of put it together back from components that seems familiar to us that The Ensemble and that's what made me think that imagination might be the same thing

**[40:17]** except in this case you're using the same semantic components but now you're putting it together into a way that your brain thinks is novel right for a particular purpose like planning and um and so I do think that uh that kind of

**[40:29]** idea is still probably missing from our current systems this sort of pulling together different um parts of your world model to simulate something new that then helps with your planning which is what I would call imagination yeah

**[40:43]** for sure so yeah now now you guys have the best models in the world um you know with the Gemini models uh do you do you have uh do you plan on putting out some sort of framework like the other two major AI Labs have of you know once we

**[40:54]** see these specific capabilities unless we have these specific safeguards we're not going to continue development or we're not going to ship the product out uh yes we we have actually we I mean we have already lots of internal checks

**[41:05]** and balances but we're going to start publishing actually you know sort of watch this Bas is we're working on a whole bunch of um blog posts and Technical papers that uh we'll be putting out in the next few months that

**[41:16]** um you know along the similar lines of things like responsible scaling laws and so on we have those uh uh implicitly internally and various safety councils and so on people like Shane and so on um but but uh it's time for us to talk

**[41:29]** about that more publicly I think so we'll be doing that throughout the course of the year yeah that's great to hear um and another thing I'm curious about is um so it's not only the risk of like uh you know the deployed model

**[41:39]** being something that people can use to do bad things but also uh Rogue actors foreign agents so forth being able to steal the weights and then find tune them to do crazy things um uh how do you think about securing the weights to make

**[41:51]** sure something like this doesn't happen making sure a very like key group of people have access to them and so forth yeah it's interesting so first of all there's sort of two partes there one is security one is open source maybe we can

**[42:01]** discuss but the security I think is super key like M just as sort of um normal cyber security type things and I think we're lucky at Google deepmind we're kind of behind Google's firewall and and Cloud protection which is you

**[42:14]** know I think best you know Best in Class in the world corporately so we already have that protection and then behind that we have specific uh uh deep mind uh uh uh protections within our codebase so it's sort of a double protection so I

**[42:27]** feel pretty good about that that that's I mean we you know you can never be complacent on that but I feel it's it's it's already sort of best in the world in terms of cyber uh uh defenses um but we got to carry on improving that and

**[42:39]** again things like the Harden sandboxes could be a way of doing that uh as well and and maybe even there are um you know uh specifically secure data centers or Hardware solutions to this too that we're thinking about I think that maybe

**[42:52]** in the next three four five years we would also want um air gaps and various other things that are known in the security community so I think that's key and I think all Frontier Labs should be doing that because otherwise you know

**[43:03]** nation states and other things rogue rogue Nation you know States and other other dangerous actors um that that there would be obviously a lot of incentive for them to to steal things like the weights um and then you know of

**[43:14]** course open source is another interesting question which is we're huge proponents of Open Source and open science I mean almost every you know we published thousands of papers and and things like Alpha fold and Transformers

**[43:24]** of course and Alpha go all of these things we put out there into the world uh uh published and and open source many of them uh graph cast most recently our weather prediction system but when it comes to uh uh you know the core

**[43:36]** technology the foundational technology in very general purpose I think the question I would have is um if you you know uh uh first open source proponents is that how does one uh stop Bad actors um individuals or Rogue you know up to

**[43:51]** Rogue States um taking those same open source systems and repurposing ing them because their general purpose for harmful ends right so we have to answer that question and and I haven't heard a compelling I mean I don't know what the

**[44:05]** answer is to that but I haven't heard a compelling clear answer to that from uh uh uh proponents of just sort of open sourcing everything so I think there has to be some balance there but um you know obviously it's a complex question of of

**[44:17]** to what that is yeah yeah I I feel like Tech doesn't get the credit deserves for like funding you know hundreds of billions of dollars worth of R&D um and you know obviously de bind with systems like and so on um but when we talk about

**[44:28]** securing uh the weights you know as we said like maybe right now it's not something that like is going to cause the end of the world or anything but as these systems get better and better the worry that yeah some a foreign agent or

**[44:38]** something gets access to them presumably right now there's like dozens to hundreds of researchers who have access to the weights how do you uh what's a plan for like getting into like the situation getting the weights in a

**[44:47]** situation rooms if you're like if you need to access to them you it's like you know some extremely strenuous process nobody nobody individual can really take him out yeah yeah I mean one has to balance that with with with allowing for

**[44:57]** collaboration speed of progress actually another interesting thing is you of course you want uh you know brilliant independent researchers from Academia or or things like the UK AI safety Institute and us one um to be able to uh

**[45:11]** uh uh uh kind of red team these systems so so one has to expose them to a certain extent um although that's not necessarily the weight um and then you know we have a lot of processes in place about making sure that um you know only

**[45:24]** if you need them that that you access to you know those people who need access have access um and right now I think we're still in the early days of those kinds of systems being at risk and as that as these systems become more

**[45:37]** powerful and more General and more capable um I think one has to look at the the access question uh so some of these other labs have specialized in different things uh relative to safety like anthropic for example with

**[45:47]** inoperability and um um do you have some sense of where uh you guys might have an edge where as so that you know now that you have the Frontier Model you're going to scale up safety where you guys are going to be able to put out the the best

**[45:57]** frti your research I think you know well we we helped Pioneer rhf and other things like that which can also be obviously used for performance but also for safety um I think that uh um you know a lot of the self-play ideas and

**[46:10]** these kinds of things could also be used potentially to to auto test uh a lot of the the the the boundary conditions that you have with the new systems I mean part of the issue is that um with these sort of very general systems uh there's

**[46:24]** so much surface area to cover like about how these systems behave so I think we are going to need some automated uh testing and and again with things like simulations and games Environ very realistic environments uh virtual

**[46:38]** environments I think we have a long history in in that and and and using those kinds of systems and making use of them for for for building AI algorithms so I think we can leverage all of that uh history um and then you know around

**[46:50]** at Google we're very lucky we have some of the world's best cyber Security Experts Hardware designers so I think we can bring that to bear in you know for security and safety as well great great let's talk about Gemini yeah um so you

**[47:03]** know now now you guys have the best model in the world um I'm so I'm curious you know the default way to interact with these systems has been through chat uh so far now that we have multimodal and all these new capabilities how do

**[47:14]** you anticipate that changing or do you think that'll still be the case yeah I think we're just at the beginning of actually understanding what a full multimodal model system uh how exciting that might be to interact with and and

**[47:26]** and uh it'll be quite different to I think what we're used to today with the chat Bots I think um uh uh the next versions of this over in the next year 18 months you know maybe we'll have some contextual understanding around the

**[47:37]** environment around you through a camera or whatever it is a phone um you know I could imagine that the next awesome glasses The Next Step um and then I think that that we'll start becoming more fluid in understanding oh let's

**[47:50]** let's let's let's sample from a video let's let's use voice um uh um maybe even eventually things like touch and and you know if you think about Robotics and other things uh you know sensors other types of sensors so I think uh the

**[48:04]** world's about to become very exciting I think in the next few years as we start getting used to the idea of what true multimodality means um on the robotics subject Ilia said when he was on the podcast that the reason opena I gave up

**[48:16]** on robotics was because they didn't have enough data in the domain at least at the time they were pursuing it um I mean you guys have put out different things like Robo Transformer and other things how do you think that's still a

**[48:26]** bottleneck for robotics progress or will we see you progress in the world of Adams as well as yeah well we're very excited about our progress with things like gate and and and and and rt2 you know robotic Transformer and uh and we

**[48:37]** actually think um so we've always liked Robotics and we've we've had you know amazing research in that we still have that going now because we like the fact that it's a data poor regime because that pushes us on some on very

**[48:50]** interesting research directions that we think are going to be useful anyway like sampling efficiency and data efficiency in general transfer learning uh learning from simulation transferring that to reality all of these very you know Sim

**[49:01]** toore all of these very interesting uh actually General challenges that we would like to solve um so the control problem so um we've always pushed hard on that and actually I think uh uh uh so so Ilia is right that that is more

**[49:15]** challenging because of the data problem um but it's also I think we're starting to see the beginnings of um these large models being transferable uh to the robotics regime learning in the general domain language domain and other things

**[49:28]** and then just treating tokens like gate as any type of token you know the token could be an action it could be a word it could be a part of an image a pixel or whatever it is and that's what I think true multimodality is and to begin with

**[49:40]** it's harder to train a system like that than a straightforward uh uh text language system um but uh actually you know going back to our early conversation of of transfer learning you start seeing that a true multimodal

**[49:54]** system the other modality benefit some some different modalities so you get better at language because you you now understand a little bit about video so um I do think uh it's harder to get going but actually ultimately um we'll

**[50:07]** have a more General more capable system like that uh whatever happened to G like that was super fascinating that you could have like play games and also do like video and also do yeah we're still we're still working on those kinds of

**[50:17]** systems but you can imagine we're just trying to uh those ideas we're trying to build into our future generations of Gemini you to be able to do all of those things and and and Robotics Transformers and you know things like that are kind

**[50:30]** of you can think of them as sort of follow-ups to that well we see asymmetric progress towards the domains in which the selfplay kinds of things you're talking about will be especially powerful so math and code you know

**[50:41]** obviously recently you have these papers out about this um or where yeah you can you can use these things to do um uh really cool novel things uh will they just be like superhuman coders but like in other ways they might be still worse

**[50:51]** than humans or how do you think about that sort of yeah so look I I think that that that um you know we're making great progress with math and and and and things like theor proving and and coding um but uh it's still interesting you

**[51:03]** know if one looks at uh I mean creativity in general and scientific Endeavor in general I think we're getting to the stage where our systems could help the best human scientists make their breakthroughs quicker like

**[51:14]** almost triage the search space in some ways uh or perhaps find a solution like Alpha fold does with a protein structure um but it can't it's they're not the level where they can create the hypothesis themselves or or ask the

**[51:27]** right question and any as any top scientists will tell you that that's the hardest part of science is actually asking the right question uh boiling down that space to like what's the critical question we should go after the

**[51:38]** critical problem and then formulating that problem in the right way to attack it and that's not um something our systems well we have really have any idea how our systems could do um but they can uh they are suitable for

**[51:50]** searching uh large combinatorial spaces if one can specify uh the problem in that way with a clear objective function so that's very useful for already uh many of the problems we deal with today but not the the most high level creative

**[52:03]** problems um when you so de M obviously has published all kinds of interesting stuff and you know speeding up science in different areas um how do you think about that in the context of if you think AGI is going to happen in the next

**[52:15]** 10 20 years uh why not just wait for the AGI to do it for you uh why build these domain specific Solutions well I think um we don't know how long AGI is going to be and we always used to say uh you know back even when we started deep mind

**[52:29]** that that uh uh we don't have to wait for AGI in order for to bring incredible benefits to the world um and uh especially and you know my personal passion has being AI for Science and and and health and and you can see that with

**[52:45]** things like Alpha fold and all of our various nature papers on different domains our Material Science work and so on I think there's lots of exciting directions uh and also impac in the world through products too I think it's

**[52:55]** very exciting uh and a huge opportunity unique opportunity we have as as part of Google of of of of the you know they you know they got dozens of of of billion user products right that we can immediately ship our advancers into and

**[53:09]** then uh billions of people uh can can you know improves their daily lives right and enriches their daily lives and enhances their daily lives so I think it's it's a fantastic opportunity for impact on all those fronts and I think

**[53:22]** the other reason from a point of view of of AI specifically is that it it battle tests your ideas right so you don't want to be in a sort of uh research bunker where you just you know theoretically are pushing things some things forward

**[53:35]** but then actually your internal metrics start deviating from uh uh real world things that would people would care about right or real world impact um so you get a lot of feedback uh direct feedback from these real world

**[53:48]** applications that then tells you whether your systems really are scaling or or actually is you know do we need to be more data efficient or sample efficient because most real world uh uh challenges require that right and so it kind of

**[54:01]** keeps you honest and um pushes you you know keep sort of nudging and steering your research directions to make sure they're on the right path so I think it's fantastic and of course the world benefits from that Society benefits from

**[54:14]** that on the way many many maybe many many years before AGI arrives yeah um well the development of Gemini is super interesting because it comes right at the heels of merging these different organizations uh brain and deep mind um

**[54:26]** yeah I'm curious what have been the challenges there what have been the synergies uh and it's been successful in the sense that you have the best model in the world now what well look it's it's it's been fantastic actually over

**[54:35]** the last year of course it's been challenging to do that like any any big integration coming together um but you're talking about two you know world-class organizations um uh long storied

**[54:45]** histories of inventing many many important things um you know from Deep reinforcement learning to Transformers and so it's very exciting actually pulling all of that together and and collaborating much more closely we

**[54:56]** always used to be collaborating but more on a on a on a you know sort of project by project basis versus uh a much deeper broader collaboration like we have now and Gemini is the first fruit of of that uh uh collaboration uh including the

**[55:10]** name Gem and I actually you know implying Twins and uh and of course a lot of other things are made more efficient like pulling compute resources together and ideas and Engineering which um I think at the stage we're at now

**[55:22]** where there's huge amounts of world-class engineering that has to go on to build the frontier systems um I think it makes sense to to coordinate that more closely yeah so I mean you you and Shane started Deep Mind um partly

**[55:34]** because you were concerned about safety um you saw AGI coming as like a live possibility do you uh do you think the people who were formerly part of brain the half of Google deep my now do they do you think they approach it in the

**[55:44]** same way have there been cultural differences there in terms of that question yeah no I think overall and this is why you know I I I think one of the reasons we joined forces we Google back in 2014 was I think um the entirety

**[55:54]** to Google an alphabet not just brain and Deep Mind take these questions very seriously of of responsibility and um you know a kind of Mantra is to try and be bold and responsible with these systems so you know I I would I would

**[56:06]** class it as I'm obviously a huge techno Optimist but I I want us to be cautious with that given the transformative power of what we're bringing bringing into the world you know collectively and um I think it's important uh you know I again

**[56:19]** going be one of the most important Technologies Humanity will ever invent so we we've got to put you know all our efforts to getting this right and be thoughtful and sort of also humble about what we know and don't know about uh uh

**[56:31]** uh the systems that are coming and the uncertainties around that and in my view the only the only sensible approach when you have huge uncertainty is to be sort of cautiously optimistic and use the scientific method to try and have as

**[56:43]** much foresight and understanding about what's coming down the line and the consequences of that before it happens you know you don't want to be live AB testing out in the world with these very consequential systems because unintended

**[56:54]** consequences maybe maybe quite severe so um you know I want us to move away as a as a field from sort of move fast and break things attitude which is you know maybe served the valley very well in the past and obviously created uh uh

**[57:07]** important Innovations um but but I think in this case you know we want to be uh uh bold with the with the positive things that it can do and make sure we realize things like medicine and Science and advancing all of those things whilst

**[57:20]** being um you know responsible and thoughtful with with uh as far as possible with with mitigating the risks yeah yeah and that's why it seems like the the responsible scaling policies or something that that is a very good

**[57:32]** empirical way to pre-commit to these kinds of things exctly um yeah and I'm curious if you have a sense of like for example when you're doing these evaluations if it turns out your next model um could help a lay person build a

**[57:42]** a pandemic class with bioweapon or something uh how you would think first of all of SEC making sure those weights are secure so that doesn't get out and second uh what would have to be true for you to be comfortable deploying that

**[57:53]** system how comfortable like how how would you make sure that that that Lan capability isn't exposed yeah well first I mean you know the the the secure model part I think we've covered with the cyber security and and make sure that's

**[58:04]** well classed and you're monitoring all those things I think um if the capability was was was discovered like that through red teaming or or external testing by you know uh uh uh government institutes and or Academia or whatever

**[58:17]** independent testers um then we would have to fix that that loophole depending what it was right um if that required more um uh a different kind of perhaps Constitution or or or different guard rails or more rhf to to avoid that or

**[58:32]** removing some training data um there could I mean depending on what the problem is I think there could be a number of of of mitigations and uh so the first part is making sure you detect it ahead of time so that's about the

**[58:43]** right evaluations uh and right benchmarking and right and right testing and then um the question is how one would fix that before you know you deployed it so but I think it would need to be fixed before it was deployed

**[58:54]** generally sure if if that was an exposure surface right right um final question um uh you know you've been thinking in terms of like the end go of Asia at a time when other people thought it was ridiculous in 2010 now that we're

**[59:06]** seeing um this like slow takeoff where we're actually seeing these like generalization and intelligence um what is like the psychologically seeing this what has that been like have it just like sort of priced into a world model

**[59:17]** so you like it's not new news for you or is it like actually just seeing live you're like wow like something's like really changed or what does it feel like yeah well for um yes it's it's already priced into my

**[59:27]** world mod of how things were going to go at least from the technology side but um obviously I didn't we didn't necessarily anticipate um the general public would be that interested this early in the sequence right of of things like maybe

**[59:40]** one could think of if we were to produce more if if say like a chat GPT and and chat Bots hadn't got the kind of got the interest they had ended up getting which I think was quite surprising to everyone that people were ready to use these

**[59:52]** things uh even though they they were lacking in certain direction right impressive though they are um then we would have produced more specialized systems I think built off of the main track like Alpha folds and Alpha goes

**[1:00:03]** and uh and so on and our scientific work and then um I think the the the the the general public may be um would have only paid attention later down the road where in a few years time we have more generally useful assistant type systems

**[1:00:17]** so that's been interesting so that's created a different type of environment that we're now all operating in as a as a as a a field so um and it's a little bit more chaotic because there's so many more things going on and there's so much

**[1:00:30]** VC money going into it and everyone's sort of almost losing their minds over it I think and and I and what I just the only thing I worry about is I want to make sure that as a field we act responsibly and thoughtfully and and

**[1:00:43]** scientifically about this and use the scientific method to approach this in a in a as I said an optimistic but careful way and I think that's the I've always believe that's the right approach for for for something like Ai and um I just

**[1:00:56]** hope that doesn't get lost in this huge rush sure sure well I think that's a great place to close Deon so thanks to thank you so much for your time and for coming on the podcast thanks it's been a real

**[1:01:06]** pleasure hey everybody I hope you enjoy that episode as always the most helpful thing you can do is just share the podcast send it to people you think might enjoy it put it in Twitter your group chats Etc just splitz the world I

**[1:01:20]** appreciate you listening I'll see you next time cheers n
