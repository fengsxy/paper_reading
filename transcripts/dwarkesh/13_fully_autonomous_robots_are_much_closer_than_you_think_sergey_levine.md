---
layout: default
type: transcript
series: dwarkesh
episode: 0
guest: ""
title: "Fully autonomous robots are much closer than you think – Sergey Levine"
source_url: "https://www.youtube.com/watch?v=48pxVdmkMIE"
analysis_url: /transcripts/dwarkesh/13_fully_autonomous_robots_are_much_closer_than_you_think_sergey_levine.analysis/
permalink: /transcripts/dwarkesh/13_fully_autonomous_robots_are_much_closer_than_you_think_sergey_levine/
---

# Transcript: Fully autonomous robots are much closer than you think – Sergey Levine

Source: https://www.youtube.com/watch?v=48pxVdmkMIE

---

**[00:00]** Today I'm chatting with Sergey Levven who is a co-founder of physical intelligence which is a robotics foundations model company and also professor at UC Berkeley and just generally one of the world's leading

**[00:11]** researchers in robotics RL and AI. Sergey, thank you for coming on the podcast. >> Thank you and thank you for the kind introduction. >> Let's talk about robotics. So before I

**[00:21]** pepper you with questions, I'm wondering if you can give the audience a summary of where physical intelligence is at right now. You guys started a year ago. Yeah. >> And what does the progress look like?

**[00:29]** What are you guys working on? >> Yeah. So, physical intelligence aims to build robotic foundation models. And that basically means general purpose models that could in principle control any robot to perform any task. Uh we

**[00:42]** care about this because we we see this as a very fundamental uh aspect of the AI problem. Like the robot is essentially uh encompassing all AI technology. If you can get a robot that's truly general, then you can uh

**[00:55]** do, you know, hopefully a large chunk of what people can do. And where we're at right now is I think we've kind of gotten to the point where we've uh built out a lot of the basics. And you know, I think those basics actually are pretty

**[01:08]** cool. Like they work pretty well. We can get a robot that will like fold laundry and that will go into a new home and like try to clean up the kitchen. But in my mind, what we're doing at physical intelligence right now is really the

**[01:18]** very very early beginning. It's just like putting in place the basic building blocks on top of which we can then tackle all these like really tough problems. >> And what's a year-by-year vision? So,

**[01:27]** um, one year in now, I got a chance to watch some of the robots and they can do pretty dextrous tasks like folding a box using grippers and it's like I don't know, it's like pretty hard to fold the box even with like my hands. Um, if you

**[01:39]** had to go year by year until we get to the full like robotics explosion, what is happening every single year? What is the thing that needs to be unlocked etc. So there are a few things that we need to get right. Uh I mean dexterity

**[01:51]** obviously is one of them and in the beginning we really wanted to make sure that we um understand whether the methods that we're developing have the ability to tackle like the kind of intricate tasks that people can do as

**[02:02]** you mentioned like folding a box uh folding different articles of laundry cleaning up a table uh making a coffee that sort of thing. And that's like that's good like that works. Uh you know I think that the results we've been able

**[02:12]** to show are pretty cool but again like the end goal of this is not to fold a nice t-shirt. the end goal was to just like confirm our initial hypothesis that like the basics are kind of solid. >> Yeah.

**[02:21]** >> But from there there are a number of really major challenges. And I think that you know sometimes when um results get abstracted to the level of like a 3minute video someone can look at this video like it's like oh that's cool like

**[02:32]** that's what they're doing but it's not like it's a very simple and uh basic version of what I think is to come. Like what you really want from a robot is not to tell it like hey please fold my t-shirt. What you want from a robot is

**[02:44]** to tell it like, "Hey, robot, like, you're now doing all sorts of uh home tasks for me. Uh, I like to have dinner made at 6 p.m. Uh, I wake up and go to work at 7:00 a.m. Uh, I'd like, you know, I like to do my laundry on on

**[02:57]** Saturday, so make sure that's ready. This and this and this. Uh, and by the way, check in with me like every Monday to see like, you know, what I want you to do to pick up when you do the shopping, right?" Like that's the

**[03:07]** prompt. And then the robot should go and do this for like, you know, 6 months, a year. like that's the duration of the task. So it's it's a it's >> ultimately if if this stuff is successful, it should be a lot bigger

**[03:20]** >> and it should have that ability to learn continuously. It should have the uh understanding of the physical world, the common sense, the ability to go in and pull in more information if it needs it. Like if I ask you like, hey, um tonight

**[03:31]** like uh you know, can you uh can you make me this type of salad? Okay, you should like figure out what that entails. Like look it up, go buy the ingredients. So there's a lot that goes into this. It requires common sense. It

**[03:41]** requires understanding that there are certain edge cases you need to handle intelligently, cases where you need to think harder. Uh it requires the ability to improve continuously. It requires understanding safety, being reliable at

**[03:52]** the right time, being able to fix your mistakes when you do make those mistakes. So there's a lot more that goes into this. Um but the principles there are you need to leverage prior knowledge and you need to have the right

**[04:04]** representations. >> So so this grand vision, what year if you had to give an est median estimate? >> Yeah. or 25 percentile 50 75 >> I think it's something where it's not going to be a case where we develop

**[04:17]** everything in the laboratory and then it's done and then you know come 20 30 something you get a robot in a box I think it'll be the same as what we've seen with AI assistance that uh once we reach some basic level of competence

**[04:29]** where the robot is delivering something useful it'll go out there in the world the cool thing is that once it's out there in the world they can collect experience and leverage that experience to get betterm So to me like what what I

**[04:42]** tend to think about a lot in terms of timelines is not the date when it will be done but the date when it will when like the flywheel starts basically. >> Okay. So when does the flywheel start? >> I think that could be very soon. Uh and

**[04:52]** I and I think there's some decisions to be made like the trade-off there is the more narrow you you you scope the thing the earlier you can get it out into the real world. Um so uh but soon as in like this is something we're already

**[05:04]** exploring. we're already trying to figure out like what are like the real things this thing could do that could allow us to start spinning the flywheel. But I think in terms of like stuff that you would actually care about that you

**[05:11]** would want to see. Um so I don't know but I think that singledigit years is very realistic. I'm really hoping it'll be more like one or two before some something is like actually out there. But it's hard to say.

**[05:22]** >> And something being out there means what? Like what what is out there? It means that there is a robot that does a thing that you actually care about that that you want done and it does so competently enough to like actually do

**[05:34]** it for real for real people that want it done. >> We already have LLMs which are like broadly deployed and that hasn't resulted in some sort of like flywheel. Um

**[05:43]** >> at least not some obvious flywheel for the model companies where the now claude is like learning how to do every single job in the economy or GPT is learning how to do every single job in the economy. So why did why doesn't that fly

**[05:54]** work for LLMs? >> Well, I think it's actually uh I think it's actually very close to working and I I I am like 100% certain that many organizations are working on exactly this. In fact, arguably there is already

**[06:07]** a flywheel in the sense that not an automated flywheel but a human loop flywheel where everybody who's deploying an LLM is of course going to look at what it's doing and it's going to use that uh to then modify its behavior. uh

**[06:20]** it it it it's complex because uh it comes back to this question of representations and figuring out the right way to derive uh supervision signals and ground those supervision signals in the behavior of the system so

**[06:33]** that it actually improves on what you want. >> And I don't think that's like a profoundly impossible problem. It's just something where the details get like pretty gnarly and challenges with

**[06:42]** algorithms and stability become pretty complex. So it's just it's something that's taken a while for uh the community collectively to get their hands around. >> Do you think it'll be easier for

**[06:50]** robotics or just that like this the state of this kind of uh techniques to label data that you collect out in the world and use it as a reward will just the the sort of like um the whole wave will rise and robotics will rise as real

**[07:06]** or is there some reason you think robotics will be will benefit more from this? Yeah, I don't think there's like a profound reason why robotics is that different, but there are a few small differences that I think uh make things

**[07:14]** a little bit more manageable. So, uh especially if you have a robot that's doing something in cooperation with people, whether it's a person that's supervising it or directing it, like there are very natural sources of

**[07:24]** supervision and there's a there's a big incentive for the person to provide the assistance that will make things succeed. Uh there are a lot of dynamics where you can make mistakes and recover from those mistakes and then reflect

**[07:35]** back on what happened and avoid that mistake in the future. And I think that when you're doing physical things in the real world, that kind of stuff just happens more often uh than it does if you're like an AI assistant answering a

**[07:45]** question. Like if you answer a question, you just like answered it wrong. It's like well it's not like you can just like go back and like tweak a few things like the person you told the answer to might not even know that it's wrong.

**[07:55]** Whereas if you're like folding the t-shirt and you messed up a little bit like it's pretty obvious like you can reflect on that, figure out what happened and do it better next time. >> Yeah. So okay, what in one year we have

**[08:03]** robots which are like doing some useful things. Maybe if you have some like relatively simple like loopy process, they can they can do it for you. It's just like you got to keep folding like thousands of boxes or something. But

**[08:15]** then there's some flywheel dot dot dot. There's some machine which will like just run my house for me. Uh as well as a human housekeeper would. Um what is the gap between this thing which will be deployed in a year that starts the

**[08:29]** flywheel and this thing which is like a fully autonomous housekeeper? Well, I think it's actually not that different than what we've seen with LLMs in some ways that it's a matter of scope. Like if you think about coding assistance,

**[08:41]** right? Like initially the best tools for coding, they could do like a little bit of completion. Like you give them a function signature and they'll like try their best to type out like the whole function and they'll maybe like get half

**[08:52]** of it right. Uh, and as that stuff progresses, then you're willing to give these things a lot more agency so that like the very best coding assistance now, like if you have if you're doing something relatively formulaic, maybe it

**[09:03]** can like put together most of a most of a PR for you for something, you know, fairly accessible, right? So, I think it'll be the same thing that that we'll see an increase in the scope that we're giving that we're willing to give to the

**[09:14]** robots as they get better and better where initially the scope might be like there is a particular thing you do like you're making the coffee or something. Uh whereas as they get more capable, as their ability to have common sense and a

**[09:26]** broader repertoire of tasks increases, then we'll give them greater scope. Now you're running the whole coffee shop. >> Um I get that there's a spectrum and I get that there won't be a specific moment that feels like we've achieved

**[09:34]** it. But if you had to give a year in which like that your median estimate of when that happens. >> I mean my my sense there too is that this is a probably a single-digit thing rather than a double- digit thing. But

**[09:44]** the reason it's so hard to really pin down is because as with as with all research, it does depend on figuring out a few question marks. And I think my my answer in terms of the nature of those question marks is I don't think these

**[09:55]** are things that require profoundly deeply different ideas, but it does require the right synthesis of the kinds of things um that we already know. And you know, sometimes synthesis, to be clear, is just as difficult as

**[10:09]** coming up with like profoundly new stuff, right? Uh so I I think it's intellectually a very deep and profound problem and and figuring that out is going to be like very exciting. Uh but it uh I think we kind of like know like

**[10:24]** roughly the puzzle pieces and it's something that we need to work on and I think if we work on it and we're a bit lucky and everything kind of goes as planned I think single digit is reasonable.

**[10:34]** >> Okay. I'm just going to do binary search until like a year. Um okay so it's less than 10 errors. So more than 5 years your median estimate I know it's like a >> I think five is a good median. >> Okay 5 years. So if it can fully

**[10:47]** autonomously run a house then I think you've like it can fully autonomously do most blue collar work. So your estimate is in 5 years it should be able to do most like blue collar work in the economy.

**[10:59]** >> So I think there's there's a nuance here. Uh and and the nuance is it becomes more obvious if we consider the analogy to the coding assistance right? It's not like the um the nature of coding assistance today is that there's

**[11:12]** a switch that flips and suddenly instead of writing software like suddenly like all software engineers get fired and everyone's using LMS for everything. Uh >> and that actually makes a lot of sense that the biggest gain in productivity

**[11:25]** comes from experts which is software engineers whose effect whose productivity is now augmented by these really powerful tools. >> Yeah. I mean separate from the question of uh whether people will get fired or

**[11:37]** not a different question is just like what will the economic impact be in five years? >> Yeah. >> Um the reason I'm curious about this is with LLMs the relationship between the

**[11:47]** revenues for these models to their inherent their seeming capability has been sort of mysterious in the sense that like you have something which feels like AGI you can have a conversation with that really like is like you know

**[11:59]** like passes a touring test. It really feels like it can do all this knowledge work. It's obviously doing a bunch of coding etc. But then the revenues for these AI companies are on like cumitively on the order of like 2030

**[12:09]** billion um per year and that's so much less than all knowledge work which is 30 $40 trillion. Um so in 5 years are we in a similar situation that LLMs are in now or is it more like we have robots deployed everywhere and they're actually

**[12:26]** like doing a whole bunch of real work etc. >> It's it's a very subtle question. I think what it probably will come down to is this is this question of scope, right? Like the reason that LLMs aren't

**[12:37]** doing all software engineering is because they're good within a certain scope, but there's limits to that and those limits are increasing to be clear every year. uh and I think that there's no reason that that we wouldn't see the

**[12:48]** same kind of thing with robots that um the scope will have to start out small because there will be certain things that these things that these systems can do very well and certain other things where more human oversight is really

**[13:00]** important and the scope will grow and what that will translate into is increased productivity and some of that productivity will come from like the robots themselves being valuable and some of it will come from the people

**[13:14]** using the robots are now more productive in their >> work productivity just like wearing gloves increases productivity or like I don't know but then it's like you want to understand something which like

**[13:24]** increases productivity 100fold versus like uh you know wearing glasses inc or something which has like a small increase so robots already increase productivity for uh workers right um where LLMs are right now in terms of the

**[13:38]** share of knowledge work they can do which is it's I guess probably like one 1,000th of the knowledge work that happens in the economy LLMs are doing at least in terms of revenue. Um are you saying like that fraction will be

**[13:51]** possible for robots but for physical work in 5 years? >> That's a very hard question to answer. Uh I think I'm probably not prepared to tell you what percentage of all labor work can be

**[14:03]** done by robots because I don't think right now off the cuff I have a sufficient understanding of uh what's involved in uh >> you know that big of a cross-section of all physical labor. Uh I think what I

**[14:15]** can tell you is this that I think it's much easier to get effective systems rolled out gradually in a human in the loop setup. And again, I think this is like exactly what we've seen with with coding systems. And I think we'll see

**[14:28]** the same thing with automation where uh basically robot plus human is much better than just human or just robot. Uh and and that just like makes total sense. It also makes it much easier to get all the technology bootstrapped

**[14:42]** because when it's robot plus human, now there's a lot more potential for the robot to like actually learn on the job, acquire new skills. It's just like you know it >> because the human can label what's

**[14:51]** happening >> and also because the human can help the can the human can give hints you know let me tell you this story like um we um when we were working on the uh pio5 project this was the paper that we

**[15:02]** released uh last April we initially controlled our robots with teleoperation in a variety of different settings and then at at some point we actually realized that we can actually make significant headway once the model was

**[15:15]** good enough by supervising it not just with low-level actions but actually literally instructing it through language. >> Now, you need a certain level of competence before you can do that. But

**[15:24]** once you have that level of competence, just standing there and telling the robot, "Okay, now now pick up the cup, put the cup in the sink, uh put the the dish in the sink just with words." Yeah. >> Already actually gives the robot

**[15:34]** information that it can use to get better. >> Right? >> Now, imagine what this implies for the the human plus robot dynamic. Like now, like basically learning is not for these

**[15:44]** systems is not just learning from raw actions. It's also learning from words eventually be learning from observing what people do from the kind of natural feedback that you receive when you're doing a job together with somebody else.

**[15:56]** And uh this kind of this is also the kind of stuff where that the prior knowledge that comes from these big models is tremendously valuable because that lets you understand that that interaction dynamic. So um I think that

**[16:07]** there's a lot of potential for these kind of human plus robot uh deployments to make the model better. >> Interesting. So, I got to go to Leo Box and see the robotic setup and try operating some of the robots myself.

**[16:19]** >> So, the thing is like these triggers, be very mindful of pressing them and don't do some like very fast movements. >> Keep it like kind of slow. >> Do I need to keep holding it? >> Sorry. Okay,

**[16:30]** >> that's okay. And don't move it very fast because he can get hurt actually. >> Yeah. Yeah. Okay. >> Okay. So, operating ended up being a bit harder than I anticipated, but I did get to see the label box team rip through a

**[16:41]** bunch of tasks. [Music] I also got to see the output data that labs actually have to use to train their robots and ask Manu Label box CEO about how all of this is packaged together. So

**[16:54]** what you're looking at is actually the final output that is then delivered to the labs which then they use to train the models. And so you can see on the left the visualization of the movements of the robot including its 3D model and

**[17:07]** so forth. And on the right you see all the camera streams synchronized with the configuration. LiBBox can get you millions of episodes of robotics data for every single robotics platform and subtask that you want to train on. And

**[17:20]** if you reach out through labelbox.com/workashe manu will be very happy with me. In terms of robotics progress, why won't it be like self-driving cars where we, you know, it's been more than 10 years

**[17:33]** since Google launched its um wasn't it 2009 that they launched the self-driving car initiative and then I remember when I was a teenager like watching demos where we would go buy a Taco Bell uh um and drive back and only now do we have

**[17:48]** them actually deployed and even then you know they may make mistakes etc. And so maybe it'll be many more years before most of the cars are self-driving. So why won't robotics, you know, you're saying 5 years to this like quite robust

**[18:02]** thing, but actually it'll just feel like 20 years of just like once we get the cool demo in 5 years and it'll be another 10 years before like we have the way and the Tesla FSD working. >> Yeah, that's a really good question. So

**[18:16]** one of the big things that is different now than it was in 2009 uh actually has to do with the technology for machine learning systems that understand the world around them. Uh principally for autonomous driving this is perception.

**[18:30]** Uh for robots it can mean a few other things as well. Uh and perception certainly was not in a good place in 2009. The trouble with perception is that it's one of those things where you can nail a really good demo with a

**[18:43]** somewhat engineered system, but hit a brick wall when you try to generalize it. Now, at this point in 2025, we have much better technology for generalizable and robust perception systems. And more generally, generalizable and robust

**[18:56]** systems for understanding the world around us. Like when you say that the system is scalable in machine learning, scalable really means generalizable. Um, so that gives us a much better starting point uh today. So, that's not an

**[19:08]** argument about robotics being easier than autonomous driving. It's just an argument for 2025 being a better year than 2009. >> But there's also other things about robotics that are a bit different than

**[19:18]** driving. Like, in some ways, robotic manipulation is a much much harder problem, but in other ways, it's a it's a problem space where it's easier to get rolling to start that flywheel with a more limited scope. Um, so to give you

**[19:31]** an example, if you're learning how to drive, you would probably be pretty crazy to learn how to drive on your own without somebody helping you. Uh, like you you would not trust your your your teenage uh child to learn to drive just

**[19:44]** on their own. Just drop them in the car and say like, "Go for it." Uh, and that's like a you know, a 16-year-old who's had uh a significant amount of time to learn about the world. You would never even dream of putting a 5-year-old

**[19:54]** in a car and telling him to get started. But if you want somebody to like clean the dishes, like dishes can break too, but you would probably be okay with a child trying to do the dishes uh without somebody constantly like, you know,

**[20:07]** sitting next to them with a with a with a break, so to speak. So for a lot of tasks that we want to do with robotic manipulation, there's potential to make mistakes and correct those mistakes. And when you make a mistake and correct it,

**[20:20]** well, first you you've achieved the task because you've corrected, but you've also gained knowledge that allows you to avoid that mistake in the future. With driving, because of the dynamics of how it's set up, it's very hard to make a

**[20:30]** mistake, correct it, and then learn from it because the mistakes themselves have significant ramifications. Um, now not all manipulation tests are like that. There are truly some like very uh safety critical stuff. And this is where the

**[20:43]** next thing comes in, which is common sense. uh common sense meaning the ability to make inferences about what might happen uh that are reasonable guesses but that do not require you to experience that mistake and learn and

**[20:56]** learn from it in advance that's tremendously important and that's something that we basically had no idea how to do uh about 5 years ago but now uh you we can actually use LLMs and VLMs ask them questions and they will make

**[21:09]** reasonable guesses like they will not give you expert behavior but you can say like hey there's a sign that says slippery floor like what's going to happen when I walk over that? >> It's kind of pretty obvious, right? Uh

**[21:18]** and no autonomous car in 2009 would have been able to answer that question. So, common sense plus the ability to make mistakes and correct those mistakes. Like, that's sounding like a off an awful lot like what what a person does

**[21:29]** when they're trying to learn something. >> All of that doesn't make robotic manipulation easy necessarily, but it allows us to get started with a smaller scope and then grow from there. So for years

**[21:40]** using I mean not since 2009 but we've had lots of video data language data and transformers for five seven eight years >> and lots of companies have tried to build transformer uh based robots with lots of training data including Google

**[21:58]** meta etc and what is the reason that they've been hitting roadblocks what has changed now >> yeah that's a really good question so I'll start out with uh maybe uh a slight modification to your comment is I think

**[22:12]** they they've made a lot of progress and in some ways a lot of the work that we're doing now at physical intelligence is built on the backs of lots of other great work that was done uh for example at uh at Google like many of us were

**[22:24]** actually at Google before we were involved in some of that work some of it is work that we're drawing on that others did so there's definitely like been a lot of progress there but um to make robotic foundation models really

**[22:34]** work it's not just a laboratory science uh kind of experiment. It's also uh it also requires kind of industrial scale uh building effort like it's it's like it's more like the Apollo program than it is

**[22:51]** like a science experiment and uh the excellent research that was done in the past in industrial research labs and I know I was involved in much of that uh was very much framed as a fundamental research effort and that's good like the

**[23:06]** fundamental research is really important but it's not enough by itself. uh you need the fundamental research and you also need the impetus to make it real and make it real means like actually put the robots out there, get data that is

**[23:18]** representative of the kind of tasks that they want that they need to do in the real world. Get that data at scale, build out the systems, get all that stuff right. Uh and that requires a degree of focus uh a singular focus on

**[23:29]** really nailing the robotic foundation model for its own sake. Not uh just as a way to do more science, not just as a way to like publish a paper uh and not just as a as a way to kind of like uh you know have a a research lab.

**[23:43]** >> What is preventing you now from continue scaling that data even more? Um, if data is a big bottleneck, why can't you just increase the size of your uh office 100x have 100x more operators were operating these robots and collecting more data?

**[24:01]** Yeah, why not ramp it up immediately 100x more? >> Yeah, that's a really good question. So, the challenge here is in understanding which axes of scale contributes to which axis of capability. Um, so if we wanted

**[24:15]** to expand capability horizontally, meaning like the robot knows how to do 10 things now and I'd like it to do 100 things later. Um, you know, that that that can be addressed by just directly horizontally scaling what we already

**[24:24]** have. But we want to get robots to a level of capability where they can do practical practically useful things in the real world. And that requires uh expanding along other axes too. It requires for example getting to very

**[24:37]** high robustness. It requires getting them to perform tasks very efficiently quickly. uh it requires them to recognize edge cases and respond intelligently and those things I think can also be addressed with scaling but

**[24:49]** we have to identify the right axis for that which means figuring out what kind of data to collect what settings to collect it in what kind of methods consume that data how those methods work right uh so answering those questions

**[25:01]** more thoroughly will give us uh greater clarity on the axes uh on the on those uh dependent variables on the things that we need to scale and we I don't fully know right right now what that will look like. I think we'll figure it

**[25:14]** out pretty soon. It's something we're working on actively, but we want to really get that right so that when we do scale it up, it'll directly translate into capabilities that are very relevant to practical use.

**[25:25]** >> Just to give an order of magnitude, um how does the amount of data we you have collected compared to internet scale pre-training data? And I know it's hard to do like a token by token count because

**[25:35]** >> yeah, what exact how does video information compare to internet information, etc. But like >> using your reasonable estimates at what fraction of >> that's right it's it's very hard to do

**[25:43]** because um robotic experience uh consists of time steps that are very correlated with each other. Uh so like the raw like bite representation is enormous but probably the information density is comparatively low.

**[25:55]** >> Um maybe a better comparison is to um the data sets that are used for uh for multimodal training. Yeah. And there it's uh I believe last time we did that count it was like between one and two orders of magnitude.

**[26:08]** >> The vision you have of uh robotics will not be possible until you collect like what 100x 1,000x more data. >> Well that's the thing that that we don't know that um uh it's certainly very reasonable to infer that like you know

**[26:21]** robotics is a tough problem uh and probably it requires you know as much experience as the language stuff. But because we don't know the answer to that, to me, a much more useful way to think about it is not

**[26:35]** how much data do we need to get before we're fully done, but how much data do we need to get before we can get started, meaning before we can get uh a data flywheel that represents a self- sustaining uh and ever growing data

**[26:48]** collection. >> Sustaining uh is this just like learning on the job or do you have something else in mind? learning on the job or uh acquiring data in a way that the process of acquisition of that data itself is

**[26:59]** useful and valuable. >> I see like just some kind of RL >> like doing something like actually real. >> Yeah. I mean ideally I would like it to be RL because you can get away with the robot acting autonomously,

**[27:10]** >> right? >> Which is uh easier. >> But that's it's not out of the question that you can have next autonomy. Uh you can you know as I mentioned before robots can learn from all sorts of other

**[27:19]** signals. Uh I described how we can have a robot that learns from a person talking to it. So there there's a lot of middle ground in between fully teleoperated robots and fully autonomous robots.

**[27:29]** >> Yeah. Okay. And how does the PI model work? >> Yeah. So the current model that we have uh basically is a vision language model that has been adapted for motor control. So uh to give you a little bit of like a

**[27:42]** fanciful brain analogy, a VLM, a vision language model is basically an LLM that has had a a little like pseudo visual cortex grafted to it, a vision encoder, right? So our models, they have a vision encoder, but they also have an action

**[27:56]** expert, an action uh decoder essentially. So it has like a little visual cortex and notionally a little motor cortex. And the way that the model actually makes decisions is it reads in the sensory information from the robot.

**[28:06]** It does some internal processing and that could involve actually uh outputting intermediate steps like you might tell it clean up the kitchen and it might think to itself like hey to clean up the kitchen I need to pick up

**[28:15]** the dish and I need to pick up the sponge and I need to put this and this and then eventually it works its way through that chain of thought generation down to the action expert which actually produces continuous actions and that

**[28:26]** that has to be a different module because the actions are continuous they're high frequency so they have have a different data format than uh text tokens but structurally it's an end to end transformer and roughly speaking

**[28:39]** technically it corresponds to a kind of mixture of experts architecture >> and like what is actually happening is that it's like it's like predicting I should do x thing then it's like there's an image token then some action tokens

**[28:51]** like what it actually ends up doing and then more image more uh text description more more action tokens basically if I'm like looking at what what stream is going on >> that that's right uh with the with the

**[29:01]** exception that the actions are actually not represented as discrete tokens it's it actually uses a flow matching kind diffusion because they're continuous and you need to be very precise with your actions for dextrous control.

**[29:10]** >> I find it super interesting that so you are I think you're using the open- source Gemma model which is like Google's uh LLM uh that the release open source and then adding the section expert on top. And I find it super

**[29:22]** interesting that the progress in different areas of AI is just based on this not only the same techniques but literally the same model that you can just use an open source LLM and then add this action expert on top. It is just

**[29:38]** notable that like you naively might think that oh there's like separate era of researchers robotics and there's a separate area of research called LLMs and uh natural language processing and no it's like it's literally the same.

**[29:49]** It's like the considerations are the same. the um the architectures are the same, even the weights are the same. I know you do more training on top of these model, open source models, but that I find super interesting.

**[29:59]** >> Yeah. So, one theme here that like I think is important to keep in mind is that the reason that those building blocks are so valuable is because the AI community has gotten a lot better at leveraging prior knowledge.

**[30:12]** >> And a lot of what we're getting from the pre-trained LLMs and VLMs is prior knowledge about the world. And it's kind of like it's a little bit abstracted knowledge. It like you know you can identify objects, you can figure out

**[30:24]** like you know roughly where things are in image that sort of thing. But I think if if I had to like summarize in one sentence the big benefit that recent innovations in AI give to robotics, it's really that prior the ability to

**[30:36]** leverage prior knowledge. And uh I think the fact that the model is the same model that's like that's kind of always been the case in deep learning. But it's that ability to pull in that prior knowledge that abstracted knowledge that

**[30:45]** has that can come from many different sources that's really powerful. >> Yeah. Today I'm here with Mark who is a senior researcher at Hudson River Trading. He has prepared for us a big data set of market prices and historical

**[30:58]** market data and we're going to try to figure out what's going on and whether we can predict future prices from historical market data. Mark, let's dig in. >> Happy to do it. So it sounds like the

**[31:07]** first fun thing to do is probably to start looking at what an order book actually looks like. >> Yeah, I think so. So I've given you like real order book data. That is snapshots of the top five levels of the order book

**[31:19]** both on the bid and ass side for a couple of different tech stocks Nvidia, Tesla, AMD etc. >> What is the shape of the prediction? Are we predicting >> what you uh take the data frame look at

**[31:31]** its y values and just kind of like histogram it? >> They are centered at zero. >> They're roughly centered at zero. But target of what exactly? >> So these things are changes in the mid

**[31:39]** price from like now to some short period of time in the future. >> This is actually quite interesting. It's like a mystery to solve. And each one of these can be like a sizable chunk of time for a a researcher.

**[31:48]** >> If this sounds interesting to you, you should consider working at Hudson River Trading. Mark, where can people learn more? >> Uh, they can learn more at hudson-trading.com/dorc.

**[31:57]** >> Amazing. I was talking to um this researcher uh uh Sander at GDM and he he works on video and audio models and he made the interesting point that the reason in his view we aren't seeing that much transfer learning between different

**[32:14]** modalities that is to say like training a language model on video and images doesn't seem to necessarily make it that much better at textual questions and um tasks is that images are represented at a semantic level than text. And so his

**[32:30]** argument is that text has this high level semantic representation within the model. Whereas images and videos are just like compressed pixels. There's not really semantic >> uh when they're embedded. There's not

**[32:42]** they're they don't represent some like high level semantic information. They're just like compressed pixels. Um and therefore there's there's no transfer learning at the level at which they're going through the model. And obviously

**[32:54]** this is super relevant to the work you're doing because your hope is that by training the model both on the visual data that the robot sees visual data generally maybe even in like from YouTube or whatever eventually plus like

**[33:05]** language information plus action information from the robot itself. Some that all of this together will like make it generally robust. Um and then you had a really interesting blog post about like why video models aren't as robust

**[33:17]** as language models. Um sorry this is not a super wellformed question. And I just wanted to do your reaction >> like what's up with that? >> Um >> yeah, so I I have uh maybe two things I

**[33:27]** can say there. I have some like bad news and some good news. >> So the bad news is what you're saying is really getting at the core of a longunning challenge with video and and image generation models.

**[33:44]** Like in some ways the idea of getting intelligent systems by predicting video is even older than the idea of getting intelligent systems by predicting text. But the text stuff turned into use practically useful things earlier than

**[34:01]** the video stuff did. I mean the video stuff is great like you can generate cool videos and I think that the work there that's been done recently is is like amazing but it's not but it's not like just generating videos and images

**[34:12]** has already resulted in systems that have this kind of like deep understanding of the world where you can like ask them to like do stuff beyond just generating more images and videos whereas with language clearly it has and

**[34:21]** I think that this this point about representations is really key to it. One way we can think about it is this that um if you um imagine pointing a camera outside this building, there's the sky, there's the clouds are moving around, uh

**[34:34]** the water, cars driving around, people. If you want to predict everything that will happen in the future, you can do so in many different ways. You can say, okay, there's people around, so let me get really good at understanding like

**[34:44]** the psychology of how people behave in crowds and predict the pedestrians. But you could also say like, well, there's clouds moving around. Let me like understand everything about water molecules and uh ice particles in the

**[34:53]** air. And you could go super deep on that. Like if you want to like fully understand like all you know down to the subatomic level everything that's going on like as a person you could spend like decades just thinking about that and

**[35:03]** you'll never even get to the pedestrians or the water, right? So if you want to really predict everything that's going on in that scene, there's just so much stuff that even if you're doing a really great job and capturing like 100% of

**[35:16]** something, by the time you get to everything else, like you know, ages will have passed. Whereas with text, it's already sort of been abstract into those bits that we as humans care about. So the representations are already there

**[35:24]** and they're not just good representations. They actually like focus in on what really matters. Okay. So that's that's the bad news. Here's the good news. The good news is that we don't have to just get everything out of

**[35:37]** like pointing a camera outside this building because when you have a robot, that robot is actually trying to do a job. So it has uh a purpose. >> Yeah.

**[35:45]** >> Uh and its perception is in service to fulfilling that purpose. And that is like a really great uh focusing factor. We know that for people this really matters. Like literally what you see is affected by what you're trying to do. Uh

**[35:57]** like there's been no shortage of psychology experiments showing that people have like almost a shocking degree of tunnel vision. Uh where they will like literally not see things right in front of their eyes if it's not

**[36:07]** relevant to what they're trying to achieve. And that is tremendously powerful. Like there must be a reason why people do that because you know certainly if you're out in the jungle seeing more is better than seeing less.

**[36:15]** So if you have that powerful focusing mechanism it must be darn important for getting you to achieve your goal. And I think robots will have that focusing mechanism because they're trying to achieve a goal.

**[36:23]** >> By the way, the fact that video models aren't as robust, is that bearish for robotics because it will so so much of the data you will have to use will not be I guess some of you're saying a lot of it will be labeled, but like ideally

**[36:38]** you just want to be able to like throw all of everything on YouTube, every video we've ever recorded and have it learn how the physical world works and how to like move about, etc. or just see humans performing tasks and learn from

**[36:50]** that. But if Yeah, I guess you're saying like it's hard to learn just from that and it actually like needs to practice a task itself. >> Well, let me put it this way. Like let's say that I um gave you lots of uh

**[37:02]** videotapes or lots of recordings of different sporting events and gave you a year to just watch sports. >> Uh and then after that year I told you, okay, now your job you're going to be playing tennis.

**[37:11]** >> Yeah. >> Okay. That's like that's pretty pretty dumb, right? Whereas if I told you first like you're gonna be playing tennis and then I and then I let you study up, right? Like now you you really know what

**[37:20]** you're looking for, right? So I think that actually >> like there's there's a very real challenge here. I don't want to understate the challenge, but I do think that there's also a lot of potential for

**[37:30]** foundation models that are embodied that uh learn from interaction from controlling robotic systems to actually be better at absorbing the other data sources because they know what they're trying to do. Uh I don't think that that

**[37:40]** by itself is like a silver bullet. I don't think it solves everything. But I think that uh it does help a lot and I think that we've already seen the beginnings of that where we can see that uh including web data in training for

**[37:54]** robots really does help uh with generalization and I I actually have the suspicion that in the long run it'll make it easier to use those sources of data that have been tricky to use up until now.

**[38:04]** Famously LMs have all these immersion capabilities that were never engineered in because somewhere in internet text is the data to train it to give it the knowledge to do a certain kind of thing. With robots it seems like you are

**[38:15]** collecting all the data manually. So there won't be this mysterious new capability that like is somewhere in the data set that you haven't purposefully collected which seems like it should make it even harder to then have

**[38:28]** uh robust out of distribution kind of uh capabilities. And so I wonder if the trek over the next 5 10 years will just be like each subtask you have to give it thousands of episodes and then it's very hard to actually automate much work just

**[38:45]** by doing subtasks. So if you think about what a barista does, what a waiter does, um what a chef does. Um very little of it involves just like sitting at one station and like doing stuff right. It's like you got to move around, you got to

**[38:56]** restock, you got to um fix the machine or um etc. um go between like the counter and the cashier and the machine etc. So yeah, will it just be like will there just be this long tail of things that you had to keep skills you had to

**[39:10]** keep like adding episodes for manually and labeling and seeing how well they did etc or is there some reason to think that it will progress more generally than that? >> Yeah. So there's a subtlety here.

**[39:26]** Emerging capabilities don't just come from the fact that internet data has a lot of stuff in it. They also come from the fact that generalization once it reaches a certain level becomes compositional.

**[39:37]** >> There was a a cute example that uh one of my students uh really like to use uh in some of his presentations which is um uh you know what international phonetic alphabet is? No. APA. So if you look in a dictionary uh they'll have the

**[39:52]** pronunciation of a word and written in like kind of funny letters. So that's basically international phonetic alphabet. So it's it's an alphabet that is pretty much exclusively used for writing down pronunciations of

**[40:02]** individual words in dictionaries. >> And you can ask an LLM to write you a recipe uh for like making some meal in international phonetic alphabet and it will do it. And that's like like holy crap. Like that is definitely not

**[40:14]** something that is that it has ever seen because IPA is only ever used for writing down pronunciations of individual words. So that's that's that's compositional generalization. It's putting together things you've seen

**[40:24]** like that in new ways. And it's like, you know, arguably there's nothing like profoundly new here because like yes, you've seen different words written that way, but you've figured out that now you can compose the words in this other

**[40:33]** language the same way that you've composed words uh in English. So um that's actually where the emerging capabilities come from. And because of this in principle if we have a sufficient diversity of behaviors the

**[40:47]** model should figure out that those behaviors can be composed in new ways uh as the the situation calls for it. And we've actually seen things even with our current models which you know I should say that I think there in the grand

**[40:58]** scheme of things like looking back 5 years from now we'll probably think that these are tiny in scale but we've already seen what I would call emerging capabilities. When we were playing around with some of our laundry folding

**[41:07]** policies actually we discovered this by accident. Uh, the robot accidentally picked up two t-shirts out of the bin instead of one, starts folding the first one, the other one gets in the way, picks up the other one, throws it back

**[41:16]** in the bin, >> and we're like, we we didn't know. We didn't know it would do that. Like, holy crap. And then we try to play around with it, and it's like, yep, it does that every time. Like, you can drop in,

**[41:24]** you know, it's it's doing its work, drops something else on the table, just pick it up, put it back, >> right? Okay, that's cool. Uh, shopping bag. It starts putting things in the shopping bag, the shopping bag tips

**[41:33]** over, picks it back back up, and stands it up, right? We didn't we didn't tell anybody to collect data for that. I'm sure somebody accidentally at some point or maybe intentionally picked up the shopping bag, but it's just you have

**[41:42]** this kind of compositionality that emerges when you do learning at scale and that's really uh where all these remarkable capabilities come from. And now you put that together with language, you put that together with uh all sorts

**[41:54]** of chain of thought reasoning and there's a lot of potential for the model to compose things in new ways, >> right? I had an example like this when I got a tour of the um robots by the way at your um office. So, it was folding

**[42:04]** shorts and I don't know if there was an episode like this in the um in the training set, but just for fun, I like took one of the shorts and like uh turned it inside out. >> Mhm.

**[42:15]** >> And then it was able to understand that it first needed to get so first of all the grippers are just like like this like two two limbs or just a pososeable finger and thumb like thing. And um it's actually shocking how much you can do

**[42:31]** with just that. Yeah, I'd understood that I first needed to fold it inside out before folding it correctly. I mean, what's especially surprising about that is it seems like this model only has like one second of context. So, as

**[42:44]** compared to these language models which can often like see the entire codebase and they're like observing hundreds of thousands of tokens and thinking about them before outputting and they're observing their own train of thought for

**[42:53]** thousands of tokens before making a plan about how to code something up. your model is like seeing one image of like what happened in the last second and it vaguely knows like it's supposed to fold this short

**[43:05]** >> um and it's seeing like the image of what's happened the last second and I guess it works. It's like crazy that it like know it will just see the last thing that happened and then keep executing on the plan. So fold it inside

**[43:16]** out then fold it correctly. But it's shocking that a second of context is enough to execute on a minute long task. Yeah. I'm curious why you made that choice in the first place and why it's possible to actually do tasks if a human

**[43:30]** could only like think I had like a second of memory >> and had to like do physical work. I feel like that would just be impossible. >> Yeah. I mean it's not that there's something good about having less memory

**[43:39]** to be clear. Like I think that uh adding memory, adding longer context, all that stuff, adding higher resolution images, I think those things will make the model better. But the reason why it's not the most important thing for the kind of

**[43:54]** skills that you saw when you visited us, it at some level I think it comes back to Moravik's paradox. So Morovik's paradox is basically that it's like you know if you know one thing about if you want to know one thing about robotics

**[44:06]** it's like that's that's the thing. Morovik's paradox says that basically uh in AI the easy things are hard and the hard things are easy. Meaning like the things that we take for granted like picking up objects, seeing you know

**[44:17]** perceiving the world, all that stuff, those are all the hard problems in AI. And the things that we find challenging like playing chess and doing calculus actually are often the easier problems. >> And I think this memory stuff is

**[44:27]** actually more of a paradox in disguise where we think that the cognitively demanding tasks that we do that we find hard that kind of cause us to think like, "Oh man, I'm sweating. I'm working so hard." Those are the ones that

**[44:38]** require us to keep lots of stuff in memory, lots of stuff in our minds. Like if you're solving some big math problem, if you're having a a complicated technical conversation on a podcast, like those are things we have to keep

**[44:48]** all those pieces, all those puzzle pieces in your head. >> If you're doing a well- rehearsed task, if you are an Olympic swimmer and you're swimming with perfect form and you're like right there in the zone, like

**[45:01]** people even say like it's in the moment. >> It's in the moment, right? you've practiced it so much you've baked it into your neural network, right? So, it really is just Morix Morovix's paradox manifesting itself.

**[45:19]** But that doesn't mean that we don't need the memory. It just means that if we want to match the level of dexterity and physical proficiency that people have, there's other things we should get right first and then gradually go up that

**[45:31]** stack into the more cognitively demanding areas, into reasoning, into context, into planning, all that kind of stuff. And that stuff will be important too. >> And how physically will So you have you

**[45:41]** have this like trillemma. You have three different things which all take more compute during inference that you want opt you want to increase at the same time. You have the inference speed and so humans are processing 24 frames a

**[45:54]** second or whatever it is that we're just like we can react to things extremely fast. Then you have the context length and for I think the kind of robot which is just like cleaning up your house. I think it has to kind it has to be aware

**[46:09]** of like things that happened minutes ago or hours ago and how that influences its plan about the next task it's doing and then you have the model size and I guess at least with LLMs we've seen that there's gains from increasing the amount

**[46:22]** of uh parameters and I think currently you have 100 millisecond uh inference speeds you have a second long context and then the model is what couple billion parameters how many okay and so each of these At

**[46:37]** least two of them are many orders of magnitude smaller than what seems to be the human equivalent, right? Like the model if a human brain has like trillions of parameters and this has like two billion parameters and then if

**[46:48]** humans are processing at least as fast as this model like actually a decent bit faster and we have hours of context. It depends on how you define human context but hours of context, minutes of context,

**[46:59]** >> sometimes decades of context. >> Yeah, exactly. So you have to have many order of magnitude improvements across all of this all of these three things which seem to oppose each other or like increasing one reduces the amount of um

**[47:14]** reduces the amount of compute we can dedicate towards the other one in inference. So how are we going to yeah how are we going to solve this? >> Yeah well that's a very big question. Um yeah let's let's try to unpack this a

**[47:26]** little bit. I think there's there's a lot going on in there. One thing that um I would say is a really interesting technical problem and I think that's it's something where we'll see perhaps a lot of really interesting innovation

**[47:38]** over the next few years is the question of representation for context. M >> so um if you imagine the like some examples you gave like if if you have a home robot that's doing something it needs to keep track as a person there's

**[47:52]** certainly some things where you keep track of them very symbolically like almost in language like you know I I have my checklist like I'm going shopping and I you know at least for me I can like literally visualize in my

**[48:03]** mind like my checklist like you know pick up the the yogurt pick up the milk pick up whatever and and I'm not like picturing the milk shelf with the milk sitting there I'm just thinking like milk, right? But then there's other

**[48:15]** things that are much more spatial, almost visual. Uh, you know, when I was uh trying to get to your to your studio, I was thinking like, okay, uh, here's the what this street looks like. Here's what that street looks like. Here's, you

**[48:27]** know, what I expect the doorway to look like. So, >> representing your context in the right form that captures what you really need to achieve, uh, your goal, uh, and otherwise kind of discards all the

**[48:38]** unnecessary stuff. I think that that's like that's a really important thing. And I think we're seeing the beginnings of that with multimodal models. But I think that multimodality has so much more to it than just like image plus

**[48:49]** text. And I think that that's a place where there's a lot of room for really exciting innovation. >> Oo. Do you mean in terms of um how we represent >> Mhm.

**[48:57]** >> Okay. >> Yeah. How we represent both context, both what happened in the past and also plans or reasoning as you can call it in LM world. Uh which is what we would like to happen in the future or intermediate

**[49:07]** processing stages in solving a task. I think do doing that in a variety of modalities including potentially learn modalities that are suitable for the job is something that has I think enormous potential uh to overcome some of these

**[49:19]** challenges. >> Interesting. Another question I have as we're as we're discussing these like um tough tradeoffs in terms of um uh inference is comparing it to the human brain and figuring out the human brain

**[49:32]** is able to have hours decades of context while being like being able to act on the order of 10 milliseconds while having 100 trillion parameters or however you want to count it. And I wonder if the best way to understand

**[49:46]** what's happening here is that human brain hardware is just way more advanced than the hardware we have in GPUs or that the algorithms for encoding video information are like way more efficient >> uh and maybe it's like some crazy

**[50:05]** mixture of experts where >> the active parameters is also on the order of billions billions or some mixture of the two basically If you had to think about like why do we have these models that are across many dimensions

**[50:19]** orders of magnitude less efficient is it hardware or algorithms than compared to the brain? >> Yeah, that's a really good question. So I definitely don't know the answer to this. Uh I I am not by any means well

**[50:33]** verssed in in neuroscience, but if I had to guess and also provide an answer that leans more on things I know, it's something like this that the brain is extremely parallel. uh it kind of has to be just out of just because of the

**[50:45]** biohysics. U but like it's even more parallel than your GPU. >> Yeah. >> Uh if you think about how a modern multimodal language model processes uh the input uh if you give it some images

**[50:59]** and some text like first it reads in the images then it reads in the text and and then proceeds uh one token at a time to generate the output. It makes a lot more sense to me for an embodied system to have parallel uh

**[51:11]** processes. Now mathematically you can actually make close equivalences between uh parallel and sequential stuff like transformers aren't actually fundamentally sequential like you kind of make them sequential by putting in

**[51:22]** position embeddings. Transformers are fundamentally actually very paralyzable things. That's what makes them so great. So I don't think that actually mathematically this this like highly parallel thing where you're doing

**[51:32]** perception and proprioception and planning all at the same time is actually actually necessarily needs to look that different from a transformer although its practical implementation will be different and you could imagine

**[51:41]** that the system will in parallel think about uh okay here's like my long-term memory like here's what I've seen you know a decade ago here's my short-term kind of spatial stuff here's my semantic stuff uh here's what I'm seeing now

**[51:53]** here's what I'm planning and all of that can be implemented in a that there's some, you know, very familiar kind of attentional mechanism, but in practice, all all running in parallel, maybe at different rates, maybe with a more

**[52:03]** complex things running slower, the faster reactive stuff running faster. >> I'm sure you've been seeing a bunch of fun images that people have been generating with Google's new image generation model, Nano Banana. My X feed

**[52:14]** is full of wild images. But you might not realize that this model can also help you do less flashy tasks like restoring historical pictures or even just cleaning up images. For example, I was reading this old paperback as I was

**[52:26]** prepping to interview Sarah Payne, and it had this really great graph of World War II allied shipping that I wanted to overlay in the lecture. Now, in the past, this would have taken one of my editors 20 or 30 minutes to digitize and

**[52:38]** clean up manually. But now, we just took a photo of the page and then dropped into into Nano Banana and got back a clean version. This was a one shot, but if Nano Manana doesn't nail it on the first attempt, you can try to just go

**[52:50]** back and forth with it until you get a result that you're super happy with. We keep finding new use cases for this model. And honestly, this is one of those tools that just doesn't feel real. Check out Gemini 2.5 flash image model,

**[53:01]** aka Nanobanana, on both Google AI Studio and the Gemini app. All right, back to Sergey. If in 5 years we have a system which is like as robust as a human in terms of interacting with the world, then what what what has happened that

**[53:17]** makes it physically possible to be able to run those kinds of models? um to have video information that is streaming at real time or hours of prior video information is somehow being encoded and considered while decoding in like a

**[53:31]** millisecond scale and with many more parameters. Uh is it just that like Nvidia has shipped much better GPUs or that you guys have come up with much better like uh encoders and stuff or like what's happened in the 5 years? I

**[53:43]** >> I I think there's there are a lot of things to this question. I think certainly there's like a really fascinating systems problem. Um I'm by no means a systems expert, but I would imagine that the right architecture in

**[53:54]** practice, especially if you want an affordable lowcost system, would be to externalize at least part of the thinking. Yeah. Uh you know, you could imagine maybe in the future you'll have a robot that has like uh you know, if

**[54:04]** your internet connection is not very good. The robot is in kind of like a dumber reactive mode, but if you have a good internet connection, then it can like be a little smarter. That's pretty cool. Um but I think there is there are

**[54:14]** also research and algorithms things that can help here. um like uh figuring out the right representations concisely representing both uh your past observations but also changes in observation right like you know your

**[54:26]** sensory stream is extremely temporally correlated which means that the marginal information gained from each additional observation is not the same as the entirety of that observation because the image that I'm seeing now is very

**[54:36]** correlated to the image I saw before. So in principle if I want to represent it concisely I can get away with a much more compressed representation than if I represent the images independently. So there's a lot that can be done on the

**[54:46]** algorithm side to get this right and that's really interesting algorithms work. I think there's also like a really fascinating systems problem. Uh to be truthful like I haven't gotten to the systems problem because you know you

**[54:56]** want to implement the system once you sort of know the shape of the of the machine learning uh solution but I think there's a lot of cool stuff to do there. >> Yeah maybe you guys just need to hire like the people run the YouTube data

**[55:05]** centers because like they know how to like encode video information. Um uh okay this actually raises an interesting question which is that with LLMs of course they're being theoretically you could run your own model on this laptop

**[55:18]** or whatever but realistically what happens is that the largest most effective models are being run in batches um of thousands millions of users at the same time uh not locally. Well, the same thing happened in

**[55:31]** robotics because of the inherent efficiencies of batching plus the fact that we have to do this incredibly computer uh comput inensive inference task. Um, and so you don't want to be carrying around like uh you know like

**[55:47]** $50,000 GPUs per robot or something. You you just want that to happen somewhere else. Um, so yeah, should this robotics world should we just be anticipating something where you need connectivity everywhere? you need robots that are

**[55:59]** like have like super fast um and you're streaming video information back and forth, right? Or at least video information one way. So, does that have interesting implications about like how this um how this deployment of robots

**[56:11]** will actually be instantiated? >> I I don't know. Uh but if I were to guess, I would guess that it'll we'll actually see both that we'll see lowcost systems with uh offboard inference and uh more reliable systems for example in

**[56:26]** settings where like if you have an outdoor robot or uh something where you can't rely on connectivity that are costlier and have onboard inference. >> Um a few things I'll say from a technical standpoint that might

**[56:38]** contribute to understanding this. While a real time system obviously needs to be controlled in real time, often at high frequency, the amount of thinking you actually need to do for every time step might be surprisingly low. Uh and

**[56:52]** again, we we see this in humans and animals. Uh when we >> plan out movements, >> there is definitely a a real planning process that happens in the brain. Like if you record like uh from a from a

**[57:05]** monkey brain, you will actually find neural coralates of planning. And there is something that happens in advance of a movement and when that movement actually takes place the shape of the movement correlates with what happened

**[57:17]** before the movement like that's planning right. Uh so that means that you put something in place and you know set the initial conditions of some kind of process and then unroll that process and that's the movement and that means that

**[57:27]** during that movement you're doing less processing uh and you kind of batch it up in advance >> but you're you're not like entirely in open loop. It's not like playing you're playing back a tape recorder. You are

**[57:37]** actually reacting as you go. you're just reacting at a different level of abstraction, a more basic level of abstraction. And again, this comes back to representations. Figure out which representations are sufficient for kind

**[57:47]** of planning in advance and then unrolling. Which representations require a tight feedback loop? And for that tight feedback loop, like what what are you doing feedback on? Like, you know, if I'm driving a vehicle, maybe I'm

**[57:56]** doing feedback on the position of the lane marker so that I stay straight. And then at a lower frequency, I sort of gauge where I am in traffic. And then so you have a couple lectures from a few years back where you say like even for

**[58:06]** robotics our role is in many cases better than imitation learning but so far the models are exclusively doing imitation learning. So I'm curious how your how your thinking on this has changed or maybe it's not changed but

**[58:19]** then you need to do this for the RL like why why can't you enter to do RL yet? >> Yeah. So the key here is prior knowledge. Yeah. Uh so in order to effectively learn from your own experience, it turns out that it's

**[58:30]** really really important to already know something about what you're doing. Otherwise, it takes far too long. Uh it's just like it it takes uh a person when they're a child a very long time to learn very basic things, to learn to

**[58:41]** write for the first time, for example. Once you already have some knowledge, then you can learn new things very quickly. So the purpose of training the models with supervised learning now is to build out that

**[58:52]** foundation that provides the prior knowledge so they can figure things out much more quickly later. And again this is not a new idea. This is exactly what we've seen with uh LLMs, right? LLM started off uh being trained purely with

**[59:04]** next token prediction and that provided an excellent starting point first for all sorts of synthetic data generation and then uh for RL. M so I I think it makes total sense that we would expect basically any foundation model effort to

**[59:17]** follow that same trajectory where we first build out the foundation essentially in like a somewhat brute force way and the stronger that foundation gets the easier it is to then make it even better with much more

**[59:27]** accessible training >> in um in 10 years will the best model for knowledge work also be a robotics model or have like a action expert attached to it and the reason I ask is like

**[59:38]** >> so far we've seen advantages from using more general models for things >> and will robotics fall into this bucket of we will just have the model which does everything including physical work and knowledge work or do you think

**[59:51]** they'll continue to stay separate? >> I really hope that they will actually be the same and um you know obviously I'm extremely biased. I I love robotics. I think it's like it's very fundamental to AI. I think that it's optimistically

**[1:00:04]** that it's actually the other way around that the robotics uh element of the equation will make all the other stuff better. And there are two uh reasons for this that that I could tell you about. One has to do with

**[1:00:18]** representations and focus. So what I said before with uh video prediction models, if you just want to predict everything that happens, it's very hard to figure out what's relevant. Yeah. If you have the focus that comes from

**[1:00:30]** actually trying to do a task now that acts to structure how you see the world in a way that uh allows you to more fruitfully utilize the other signals that could be extremely powerful. >> Yeah.

**[1:00:40]** >> The second one is that understanding the physical world at at a very deep fundamental level at a level that goes beyond just what we can articulate with language can actually help you solve other problems. M and we we see we we

**[1:00:51]** experience this all the time like when we talk about abstract concepts we say like this company has a lot of momentum >> right I I like you we'll use like social metaphors to describe inanimate objects like my computer hates me right like we

**[1:01:06]** experience the world in a particular way and our subjective experience shapes how we think about it in very profound ways and then we you use that as a hammer to basically hit all sorts of other nails that are far too abstract uh to handle

**[1:01:16]** any other way >> I guess but there there may be other considerations that are relevant to uh physical robots in terms of like inference speed and model size etc which might be different than the

**[1:01:27]** considerations for knowledge work but then maybe you can maybe that doesn't change maybe it's still the same model but then you can serve it in different ways and the advantages of co-raining are high enough that

**[1:01:38]** yeah whenever I'm like I'm wondering in five years if I'm using a model to code for me does it also know how to do robotic stuff and yeah maybe the advantages of code running on robotics are high enough that it's worth

**[1:01:49]** >> Mhm. Well, and I should say that the the coding is probably like the pinnacle of a of uh abstract knowledge work in the sense that like just by by the by the mathematical nature of computer programming, it's an extremely abstract

**[1:02:00]** activity which is why people struggle with it so much. >> Yeah, I'm a bit confused about why simulation doesn't work better for uh robots. Like if I look at humans, smart humans do a good job of

**[1:02:13]** >> if they're intentionally trying to learn, noticing what about the simulation is similar to real life and paying attention to that and learning from that. So if you have like pilots who are learning in simulation or F1

**[1:02:24]** drivers who are learning in simulation, should it be expected to be a case that as robots get smarter, they will also be able to learn more things through simulation or uh or is this cursed and we need real world data wherever?

**[1:02:36]** >> This is a very subtle question. Um, your example with a airplane pilot using simulation is really interesting, but something to remember is that when a pilot is using a simulator to learn to fly an airplane, they're extremely goal-

**[1:02:50]** directed. So, their goal in life is not to learn to use a simulator. Their goal in life is to learn to fly the airplane. They know there will be a test afterwards, and they know that eventually they'll be in charge of like

**[1:02:58]** a few hundred passengers, and they really need to not crash that thing. Um, and when we train um, models on data from multiple different domains, the models don't know that they're supposed to solve a particular task. They just

**[1:03:12]** see like, hey, here's one thing I need to master. Here's another thing I need to master. So maybe like a better analogy there is if you if you're like playing a video game where you can fly an airplane and then eventually someone

**[1:03:21]** puts you in the cockpit of a real of a real one. Like it's not that the video game is useless, but it's it's not the same thing. And if you're trying to play that video game and your goal is to like really like master the video game, um

**[1:03:31]** you're not going to go about it in quite the same way. >> Isn't um can you do some kind of meta RL on this, which is like almost identical actually to the there's this really interesting paper you wrote in 2017

**[1:03:44]** where maybe the loss function is not how well it does at a particular video game or particular simulation, but how well being trained at different video games makes it better at some other downstream task. I I did a terrible job explaining,

**[1:03:56]** but I understand what you mean. Yeah. Yeah. Maybe can you do a better job explaining what I what I was trying to say? >> So So I think what you're trying to say is basically that uh well maybe if we

**[1:04:03]** have like a really smart model that's doing metal learning, perhaps it can figure out that its performance on a downstream problem, a real world problem is increased by doing something in a simulator

**[1:04:13]** >> and then specifically make that the loss function. Right. >> That's right. But here's the thing with with with this. There's a set of these ideas that are all going to be like something like train to make it better

**[1:04:24]** on the real thing by leveraging something else. Yeah. And the key lynchpin for all of that is the ability to train it to be better on the real thing. >> Um the thing is like I actually suspect

**[1:04:33]** in reality we might not even need to do something quite so explicit because metalarning is emergent as you pointed out before right like uh LLMs essentially do a kind of metal learning via in context learning. I mean we can

**[1:04:45]** debate as to how much that's learning or not but the point is that large powerful models trained on the right objective on real data get much better at leveraging all the other stuff and I think that's actually the key and coming back to your

**[1:04:56]** uh airplane pilot like the airplane pilot is trained on a real world objective like their objective is to be a good airplane pilot to be successful to have a good career and all of that kind of propagates back into the actions

**[1:05:07]** they take and leveraging all these other data sources so what I think is actually the key here to leveraging auxiliary data sources including simul is to build the right foundation model that is really good that has those

**[1:05:18]** emergent abilities. >> And to your point uh to get really good like that it has to have the right objective. Uh now we know how to get the right objective out of real world data. Maybe we can get out of other things but

**[1:05:31]** that's that's harder right now >> right >> and I think that again we can look to the examples of what happened in other fields like these days if someone trains an LLM for solving complex problems

**[1:05:41]** they're using lots of synthetic data. Mhm. >> But the reason they're able to leverage that synthetic data effectively is because they have this starting point that is trained on lots of real data

**[1:05:49]** that kind of gets it and once it gets it then it's more able to leverage all this other stuff >> right >> so uh I think like perhaps ironically the key to leveraging other data sources

**[1:05:57]** including simulation is to get really good at using real data understand what's up with the world and then now you now you can fruitfully use >> so once we have this like um in 2035 2030 what basically the sci-fi world uh

**[1:06:12]** are Are you optimistic about the ability like true AGIs to build simulations in which they are rehearsing skills that no human or AI has ever had a chance to practice before? Um some you know they need to like practice via astronauts

**[1:06:26]** because we're building the Dyson sphere and they can just do that in simulation or like will the issue with simulation continue to be one regardless of how smart the models get? So here's what I would say that deep down at a very

**[1:06:38]** fundamental level the synthetic experience that you create yourself doesn't allow you to learn more about the world. It allows you to rehearse things. It allows you to consider counterfactuals but somehow

**[1:06:52]** information about the world needs to get injected into the system. So um and I think the way you pose this question actually elucidates this very nicely because in robotics classically people have often thought about simulation as a

**[1:07:05]** way to inject human knowledge because a person knows how to write down like differential equations they can code it up and that like gives the robot more knowledge than had before but I think that increasingly what we're learning

**[1:07:15]** from uh experiences in other fields from uh how like the video generation stuff goes from synthetic data for LLMs is that actually probably the most powerful way to create synthetic experience is from a really good model uh because you

**[1:07:27]** know the model probably knows more than a person does about those fine grain details but then of course where does that model get the knowledge from experiencing the world. Yeah. So in a sense what you said uh I think is

**[1:07:38]** actually quite right in that a very powerful AI system can simulate a lot of stuff but also at that point it kind of almost doesn't matter because viewed as a black box what's going on with that system is that information comes in and

**[1:07:50]** capability comes out and whether the way process that information is by imagining some stuff and simulating or by some model free method uh is kind of irrelevant in understanding it >> capability sense of what what the

**[1:08:00]** equivalent is in humans like whatever we're doing when we're daydreaming or sleeping thing or um I don't know if you have some sense of like what this auxiliary thing we're doing is but if you had to make an ML analogy for it,

**[1:08:13]** what is it? >> Well, uh yeah, I mean certainly when uh uh when you sleep, your brain does stuff that looks an awful lot like what it does when it's awake. Uh that looks an awful lot like playing back experience

**[1:08:24]** or perhaps generating new statistically similar experience. Um, and so I think it's like it's very reasonable to guess that perhaps simulation through a learned model is like part of how your brain figures out like counterfactuals

**[1:08:39]** basically. Yeah. >> But um something that's kind of even more fundamental than that is that optimal decision-m at its core regardless of how you do it requires considering counterfactuals. You

**[1:08:51]** basically have to ask yourself if I did this instead of that would it be better? And you have to answer that question somehow. And whether you answer that question by using a learn simulator or whether you you answer that question by

**[1:09:01]** using a value function uh or something like that by using a reward model in the end it's kind of all the same like as long as you have some mechanism for considering counterfactuals and figuring out which counterfactual is better

**[1:09:11]** you've got it. Yeah. >> Uh so that that I I like thinking about it this way because it kind of simplifies things. It tells us that the key is not necessarily to do really good simulation. The key is to figure out how

**[1:09:20]** to answer counterfactuals. >> Yeah. Interesting. So a stepping big picture again. The reason I'm interested in getting concrete understanding of when this robot economy will be deployed is because it's actually pretty relevant

**[1:09:33]** to understanding how fast AGI will proceed in the sense that well it's you know obviously the data flywheel but also if you just extrapolate out the capex for AI suppose by 2030 you know people have different estimates but many

**[1:09:48]** people have estimates in the hundreds of gigawatts 100 200 300 gawatt and then you can just like crunch numbers on like if you have 200 gawatts deployed deployed or 100 gig was deployed by 2030. The cap the marginal capex for Eur

**[1:09:59]** is like trillions of dollars. It's like 2 three 4 trillion a year. Um and that corresponds to actual data centers you got to build, actual um chip foundaries you have to build, actual um solar panel factories you got to build. And I'm very

**[1:10:15]** curious about whether by this time by 2030 if the big bottleneck we have is just like people uh to like lay out the solar panels next to the data center or assemble the data center whether the robot economy will be mature enough to

**[1:10:34]** helps significantly in that process. >> That's cool. So you're basically saying like uh how much concrete should I buy now to build the data center so that by 2030 I can power all the robots. >> Yeah. uh that that is a more ambitious

**[1:10:45]** way of thinking about it than uh that has occurred to me. But it's a cool question. I mean the good thing of course is that the robots can help you build that stuff, >> right? Well, but will they be able to by

**[1:10:53]** the time that like there's there's some like there's the non-rootic stuff which will also like mandate a lot of uh capex >> um and then there's a robot stuff where you actually had to build robot factories etc. But every just think

**[1:11:06]** there will be this industrial explosion across the whole stack and how much will robotics be able to speed that up or make it possible? >> I mean in principle quite a lot, right? Uh I think that we have a tendency

**[1:11:18]** sometimes to think about robots as like mechanical people. >> But that's not the case, right? Like people are people and robots are robots. Like the the better analogy for the robot, it's it's like your car or a

**[1:11:30]** bulldozer. Uh like uh it has much lower maintenance requirements. You can put them into all sorts of weird places and they don't have to look like people at all. You can make a robot that's, you know, 100 feet tall. You can make a

**[1:11:41]** robot that's tiny. Uh, so I think that if you have the intelligence to power very heterogeneous robotic systems, you can probably actually do a lot better than just having like you know mechanical people in effect. Uh, and it

**[1:11:55]** can be a big productivity boost for the real people. Uh, and it can allow you to solve problems that are very difficult to solve now. Yeah. uh you can you know for example I'm not an expert on data centers by any means but you could build

**[1:12:07]** your data centers in a very remote location because the robots don't have to worry about whether there's like a shopping center nearby >> and then do you have a sense of how so there's like where will the software be

**[1:12:17]** and then there's a question of how many physical robots will we have so like h how many of the kinds of robots you're training in physical intelligence like these tabletop arms are there physically in the world how many will there be by

**[1:12:30]** 2030 how many will be needed I mean these are tough questions like how many we needed for >> these are very tough questions and also you know economies of scale in robotics so far have not functioned the same way

**[1:12:42]** that they probably would in the long term right um just to give you an example when I started working in robotics in 2014 I used a uh a very nice research robot called a PR2 that cost uh $400,000 to purchase. When I started my

**[1:12:58]** research lab at UC Berkeley, I I bought robot arms that were $30,000. The kind of robots that we are using now at physical intelligence, each arm costs about $3,000 and we think they can be made for a small fraction of that.

**[1:13:11]** >> So these things >> what is it what is the cause of that learning rate? >> Well, uh there are a few things. So one of course has to do with economies of scale. So customuilt high-end research

**[1:13:21]** hardware of course is going to be much more expensive than um kind of more productionized hardware. But the other and then of course there's a technological element that as uh we get better at building actuated machines uh

**[1:13:35]** they become cheaper but there's also um a software element which is the smarter your AI system gets the less you need the hardware to satisfy certain requirements. So traditional robots and factories uh they need to make motions

**[1:13:49]** that are highly repeatable and therefore it requires a degree of precision and robustness that you don't need if you can use cheap visual feedback. So AI also makes robots more affordable uh and lowers the requirements on the hardware.

**[1:14:03]** >> Interesting. Okay. So do you think the learning rate will continue? Do you think it will cost hundreds of dollars by the end of the decade to buy mobile arms? That is a great question for my co-founder uh Adnan Esmile who is uh

**[1:14:16]** probably like the best person arguably in the world to ask that question of but certainly the drop in cost that I've seen has surprised me year after year. >> Okay. And how many arms are there probably in the world? Is it more than a

**[1:14:27]** million? Less than a million. >> So I don't know the answer to that question, but it's it's also a tricky question to answer because not all arms are made equal. Like arguably the kind of robots that are like assembling cars

**[1:14:37]** in a factory are just not the right kind to think about. So the kind you want to train on >> very few because they are not currently commercially deployed unlike the factory robots. So like less than 100 thousand

**[1:14:50]** >> I don't know but probably yeah >> okay and we want billions of robot like at least millions of robots if you're just thinking about like the industrial explosion that you

**[1:15:04]** need to um >> have this AI explosive growth um not only do you need the arms but then you need like something that can move around um basically I'm just trying to think about

**[1:15:14]** like will that be possible by the time that you need a lot more rate labor to power this um AI AI boom. >> Well, you know, economies are very good at filling demand when there's a lot of demand, right? Like that how many

**[1:15:27]** iPhones were in the world in in 2001, right? >> That's right. >> So, uh I think it's defin there's definitely a challenge there. Uh and I think it's something that is worth

**[1:15:37]** thinking about and a particularly important question for researchers like myself is how can AI affect how we think about hardware, right? Because there are some things that I think are going to be really really important. Like you

**[1:15:50]** probably want your thing to like not break all the time. Yeah. There's some things that are firmly in that category of like question marks like how many fingers do we need? Like you said yourself before that you were kind of

**[1:15:58]** surprised that a robot with two fingers can do a lot. Okay. Maybe you still want like more than that but still like finding the bare minimum that still lets you have good functionality. That's important. That's in the question mark

**[1:16:08]** box. And there's some things that I think like we probably don't need. like we probably don't need the robot to be like super duper precise because we know that feedback can compensate for that. So I think my my job as I see it right

**[1:16:19]** now is to figure out what's sort of the minimal package we can get away with and I really like to think about robots in terms of minimal package because I don't think that we will have like the one ultimate robot like sort of the

**[1:16:30]** mechanical person basically. Uh I think what we will have is a bunch of things that good effective robots needs to need to satisfy just like good smartphones need to have a touchcreen like that's something that we all kind of agreed on

**[1:16:42]** and then a bunch of other stuff that's kind of optional depending on the need depending on the cost point etc. And I think there will be a lot of innovation where once we have very capable AI systems that can be plugged into any

**[1:16:53]** robot to endow it with some basic level of intelligence, then lots of different people can innovate on how to get the robot hardware to be optimal for each niche it needs. >> In terms of manufacturers, is there some

**[1:17:03]** Nvidia of robotics? >> Not right now. Maybe there will be someday. Uh I I would really uh like maybe I'm being idealistic, but I would really like to see a world where there's a lot of heterogeneity in robots.

**[1:17:16]** >> What is the biggest bottleneck in the hardware today as somebody who's designed the algorithms that run on it? >> It's it's a tough question to answer mainly because things are changing so fast. Um I think that to me the things

**[1:17:28]** that I spend a significant amount of time thinking about on the hardware side is really more like reliability and cost. It's not that I'm that like that worried about cost. is just that cost translates to number of robots which

**[1:17:38]** translates to amount of data. And being an ML person, I really like having lots of data. So I really like having robots that are low cost because then I can have more of them and therefore more data. And reliability is important more

**[1:17:47]** or less for the same reason. >> Um >> but I think it's something that we'll get more clarity on as things progress because as we basically the AI systems of today are not pushing the hardware to

**[1:18:00]** the limit. So as the AI systems get better and better, the harder we'll get pushed to the limit and then we'll hopefully have a much better answer to your question. >> Okay. So this is a question I've had for

**[1:18:09]** a lot of guests and is that if you go through any layer of this AI explosion, you find that a bunch of the actual source supply chain is being manufactured in China. So other than chips obviously but then you

**[1:18:28]** know if you if you talk about data centers and you're like oh all the wafers for solar panels and a bunch of the cells and modules etc are manufactured in China then you just you just go through the supply chain and

**[1:18:40]** then um obviously robot arms are being manufactured in China and so if you live in this world where the hardware is just incredibly valuable to ramp up manufacturing of because each robot can produce some fraction of the

**[1:18:55]** value that a human worker can produce. And not only is that true, but the value of human workers or any kind of worker has just tremendously skyrocketed because we just need tons of bodies to lay out the tens of thousands of solar

**[1:19:10]** far acres of solar farms and uh data centers and um uh foundaries and everything. Um in this boom world, the big bottleneck there is just like how many robots can you physically deploy? How many can you manufacture? Because

**[1:19:22]** you guys are going to come up with the algorithms now. we just need the hardware. And so this is a question I've asked many guests which is that like if you look at the part of the chain that you are

**[1:19:34]** observing, what is the reason that China just doesn't win by default? Right? If they're producing all the robots um and you come up with the algorithms that make those robots super valuable um why why don't they just win by default?

**[1:19:46]** >> Yeah. Um so this is a very complex question. Um I'll start with the with the broader themes and then try to drill a little bit into the details. So one broader theme here is that if you want to have an economy where

**[1:20:06]** you get ahead by having a highly educated workforce by having people that uh have high productivity meaning that for each person's hour of work uh lots of stuff gets done. automation is really really good because automation is what

**[1:20:21]** multiplies the amount of productivity that each person has. Again, same as like LM coding tools. LM coding tools amplify the productivity of a software engineer. Robots will amplify the productivity of uh basically everybody

**[1:20:33]** that that is doing work. Uh now that's that's kind of like a final state like a desirable final state. Now there's there's a lot of complexity in how you get to that state, how you make that uh uh an appealing journey uh to society,

**[1:20:49]** how you navigate the geopolitical dimension of that. Like all of that stuff is actually pretty complicated and it requires making a number of really good decisions uh like uh you know good decisions about uh investing in a

**[1:21:01]** balanced uh robotics ecosystem uh supporting both software innovation and hardware innovation. Uh I don't think any of those are insurmountable problems. It just requires um a degree of kind of uh long-term vision and the

**[1:21:18]** right kind of balance of investment. But what makes me really optimistic about this is is is that that final state that if I think we can all agree that in the United States we would like to have the kind of society where people are highly

**[1:21:30]** productive where we have uh you know we have highly educated people doing high value work and because that that end state is seems to me very compatible with automation with robotics there's a lot of at some level there should be a

**[1:21:44]** lot of incentive to get to that state >> and and then from there uh we have to like solve for like all the details that will help us get there and that's not easy. Like I think there's a lot of like complicated decisions that need to be

**[1:21:54]** made on in terms of private industry, in terms of investment, in terms of the political dimension. But I'm very optimistic about it because it's like it seems to me like the light of the end at the end of the tunnel is kind of it's in

**[1:22:05]** the right direction. M I mean I yeah I guess there's a different question which is that if the value is sort of bottlenecked by hardware and so you just need to produce more hardware. What is the path by which hundreds of millions

**[1:22:18]** of robots or billions of robots are being manufactured in the US or with allies? I don't know how to approach that question but it seems like a different question than like okay well what is the impact on like human wages

**[1:22:28]** or something. So again, for the specifics of how how we make that happen, I think that's a very long conversation that I'm probably not the most qualified to speak to, but I think that in terms of the ingredients, um the

**[1:22:41]** ingredient here that I think is important is that >> robots help with uh physical things uh physical work. And if producing robots is itself physical work, then getting really good at robotics should help with

**[1:22:56]** that. It's a little circular, of course. And uh you know as with all circular things you have to like kind of bootstrap it and and try to get that that engine going. But >> it seems like it is a an easier problem

**[1:23:08]** to address than for example the problem of uh digital devices where work goes into creating you know computers, phones etc. But the computers and phones don't themselves help with the work. >> Right? I guess feedback loops go both

**[1:23:20]** ways. They can help you or they can help others. And it's a positive some world. So it's not necessarily bad that they help others, but um to the extent that a lot of the things which would go into this feedback loop, the subcomponent uh

**[1:23:33]** uh manufacturing and supply chain already exists in China, it seems like the stronger feedback loop would exist in China. And then there's a separate discussion like maybe that's fine. >> Um maybe that's good and maybe they'll

**[1:23:44]** continue exporting this to us. Um but it just like notable that I just find it notable that whenever I talk to a guest about different things it's just like oh yeah that you know within a few years the key bottleneck to every single part

**[1:23:57]** of the supply chain here will be something that China is like the 80% world supplier of something >> well yeah and and this is why I said before that I think something really important to get right here is a

**[1:24:07]** balanced robotics ecosystem right like I I think I think AI is tremendously exciting but I think we should also recognize that getting AI high right is not the only thing that we need to do. Uh and we need to think about how to

**[1:24:21]** balance uh our priorities, our investment, the kind of things that we spend our time on. Uh just as as an example at physical intelligence, we do take hardware very seriously actually. Uh we uh we build a lot of our own

**[1:24:35]** things. Uh and we want to have a hardware road map alongside our AI road map. But I think that you know that's just us. I think that for uh the United States, for you know, arguably for for human civilization as a whole, like I

**[1:24:49]** think we need to think about these problems very holistically. Um and I think it it is easy to get distracted sometimes when there's a lot of excitement, a lot of progress in one area uh like AI uh and we are tempted to

**[1:25:02]** lose track of other things including things you've said like hey like you know there's a hardware component, there's a there's an infrastructure component with compute and things like that. So I think that in general it's

**[1:25:11]** good to have a more holistic view of these things and I wish we had you know more holistic conversations about that sometimes >> I do think from the perspective of society as a whole how how should they

**[1:25:20]** be thinking about the advances in robotics and knowledge work and I think it's basically like society should be playing for full automation like there will be a period in which people's work is way more valuable because there's

**[1:25:31]** this huge boom in the economy we're like building all these data centers or building all these factories but then eventually humans can do things with their body and we can do things with our And there's not like some secret third

**[1:25:40]** thing. So what what should society be planning for? It should be full automation of humans. And there also be a society be much wealthier. So presumably there's ways to do this in a way that like everybody is much better

**[1:25:53]** off than they are today. But then like the end state, the light at the end of the tunnel is the full automation plus super wealthy society with some redistribution or whatever way to figure that out. Right. I don't know if you

**[1:26:05]** disagree with that characterization. So I think at some level that's a very reasonable uh way to look at things. But I think that if there's one thing that I've learned about technology, it's that it rarely evolves quite the way that

**[1:26:20]** people expect and sometimes the journey is just as important as the destination. So I think it's actually very difficult to plan ahead for an end state. But I think directionally what you said makes a lot of sense and I and I do think that

**[1:26:32]** it's very important for us collectively to think about how to structure the world around us in a way that is amenable to greater and greater automation across all sectors. >> But I think we should really think about

**[1:26:44]** the journey just as much as the destination because things evolve in all sorts of unpredictable ways and uh we'll find >> automation showing up in all sorts of places probably not the places we expect

**[1:26:55]** first. Uh so you know I think that the constants here that I think are really important is education is really really valuable. Yeah like education is uh the best buffer somebody has against the negative effects of change. Uh so if

**[1:27:12]** there is like one single lever that we can pull collectively as a society it's like more education because that's >> true. I mean the morax paradox is like the things which are like most beneficial form education for humans

**[1:27:23]** will might have be the easiest to automate because it's really easy to educate AIS you know you can throw the textbooks it would take you eight years of grad school to do at them in an afternoon

**[1:27:32]** >> well what education gives you is flexibility uh so it's uh it's less about the uh the particular facts you know as it is about your ability to acquire skills acquire understanding uh so it has to be good education Right.

**[1:27:48]** Okay. Sergey, thank you so much for coming on the podcast. Super fascinating. >> Yeah, this was uh this was intense. We ask tough questions. >> I hope you enjoyed this episode. If you

**[1:27:58]** did, the most helpful thing you can do is just share it with other people who you think might enjoy it. Send it to your friends, your group chats, Twitter, wherever else. Just let the word go forth. Other than that, super helpful if

**[1:28:08]** you can subscribe on YouTube and leave a fivestar review on Apple Podcast and Spotify. Check out the sponsors in the description below. If you want to sponsor a future episode, go to dwarcash.com/advertise.

**[1:28:22]** Thank you for tuning in. I'll see you on the next one.
