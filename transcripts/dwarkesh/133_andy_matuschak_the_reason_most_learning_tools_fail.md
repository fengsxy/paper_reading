---
date: 2024-01-01
layout: default
type: transcript
series: dwarkesh
episode: 133
guest: ""
title: "Andy Matuschak — The reason most learning tools fail"
source_url: "https://www.youtube.com/watch?v=dmeRQN9z504"
analysis_url: /transcripts/dwarkesh/133_andy_matuschak_the_reason_most_learning_tools_fail.analysis/
permalink: /transcripts/dwarkesh/133_andy_matuschak_the_reason_most_learning_tools_fail/
---

# Transcript: Andy Matuschak — The reason most learning tools fail

Source: https://www.youtube.com/watch?v=dmeRQN9z504

---

**[00:00]** we under appreciate the role that memory has in our lives if what you're trying to do is to understand something pretty difficult your ability to understand that thing is still absolutely going to be bound on your memory of the

**[00:11]** constituent material for the meeting and student the education system mostly wants to make the student do things they don't want to do it's not about helping them achieve their goals more easily or more effectively for the most part it's

**[00:23]** about like achieving goals that aren't theirs the histories in educational psychology that I'm most aligned with are like the most robotic authoritarian kind of histories and also the ones that are most like kind of unschooling and

**[00:38]** Montessori s do llms make memorization more or less valuable llms depend on our ability to externalize things and to make them legible basically everyone in the education space are focused on really like the bottom quartile like not

**[00:51]** even medium okay today I have the pleasure of speaking with Andy matushak who is a researcher engineer and designer working on tools for thought in addition to this podcast on Andy's YouTube channel we did an interesting

**[01:06]** collaboration which I encourage you all to check out where I just watched Andy try to learn some new material so it was just an intro chapter of quantum mechanics and I honestly I was expecting to see some cool techniques or be

**[01:20]** impressed but I was way more surprised than I expected to be by the deliberateness the effortfulness of the practice how what was really I mean it was like 15 minutes of page in this textbook and any small thing that Andy

**[01:38]** thought like I don't fully understand this the author is trying to say something here he's trying to draw an analogy or relationship I'm not sure I totally comprehend the relationship between this you know classical

**[01:48]** mechanics equation and the quantum mechanics equation the author thinks is analogous just really delving deep in that so I was super I thought that was I thought that was really interesting that this is a way to

**[01:59]** um brush a new material yeah so in this conversation I would I'm looking forward to talking with Andy about not only that experience but a whole bunch of his other research and the other tools he's built well let me ask you this so that

**[02:11]** experience made me think listen this is somebody who actually hears about understanding the material if you're going through it this deliberately do you think people in general care about Act actually

**[02:22]** integrating and understanding the material they're consuming in books and textbooks don't you think they'd make more an effort to actually assimilate that information if they cared to yeah I mean I think the statement is just a

**[02:33]** little too General probably to comment on I mean so I think it's certainly the case that most students don't actually want to do this because they're they're learning stuff that they don't actually care

**[02:45]** about learning or even if they do care about learning it often like there isn't a clear connection between whatever reading or activity they're doing in the moment and like the thing that originally inspired them for the subject

**[02:57]** like what they actually want to do and so there's always something tenuous going on I think on the other hand like it's amazing to look at say subreddits and to look at the level of nerdery and Fascination that will be brought to bear

**[03:09]** on you know gardening equipment or like knots for instance you know people are competing to tie some very obscure uh 18th century not or whatever and they're flipping through almanacs from the period so like when people are

**[03:23]** interested and it connects to something that's truly meaningful for them I think they really do want to absorb and we see that in their behavior here's the second thing uh that I think it is relevant well to explain this I

**[03:37]** will reference Mortimer Adler and vandoren's how to read a book which is a great guide on on serious reading and they consider the case of people who often have books on their bedside table and sometimes they're like very

**[03:50]** difficult or demanding books these are kind of aspirational like oh I wish I could ring read King Lear I want to be the kind of person who reads King Lear you put it on your bedside table and people will like read it before bed and

**[04:01]** they'll find that they like fall asleep while they're reading it they're not really absorbing or understanding this book I mean it's not just an issue of memory it's like they they they simply are not apprehending the words on the

**[04:11]** page um and and the authors of how to read a book make the case that like the the issue here with these people who are falling asleep reading King Lear uh is in many cases it's not that they don't

**[04:22]** want to stay awake and to really deal with that text in many cases it's that they actually don't know how they butt their heads up against this very difficult wall of material it's almost like maybe a rock climber uh who's not

**[04:38]** very experienced going up against a wall that all it has is these like really subtle notches into an experience rock climber those subtle notches are like a ladder right like they can get right in there and start like making some

**[04:48]** progress and seeing what's up with this wall uh but if you're an inexperienced rock climber it just looks like a solid wall um so the claim maybe maybe this is an optimistic claim you can take me to task

**[05:01]** is that there is such a thing as being a more skillful reader and being a more skillful reader well actually in practice in many cases when the reading is aligned with your actual interests uh produce a more serious more

**[05:15]** understanding forward kind of reading um right so there's like two models of why people might fail to retain the material they're consuming one is they got it at some point but they forgot it and the other is they never understood in the

**[05:29]** first place and they just never notice that they never understood it and what was really uh what I found really interesting was you going paragraph by paragraph sentence by sentence have I got this and by the way this was

**[05:40]** material that I had tried to go through the week before and there were things when you dwelved on something I'm like actually I don't understand that either and I didn't notice I didn't understand that how do you how are you able to

**[05:52]** notice your confusion uh while you were going through this is the kind of habit it's a skill that can be built Adler and vandoren suggest that the first and most important rule of skillful reading

**[06:06]** active reading is asking questions and trying to answer them and that really if you just dwell on that and dwell on well what kinds of questions should I be asking and how should I go about asking them how should I go about answering

**[06:17]** them when the author isn't present and so on and so forth they don't get very far they also say conversely and like this isn't meant as a criticism an undemanding reader asks no questions and gets no answers and I certainly have

**[06:31]** read many many books that way particularly before I develop this habit and I often found myself falling into that second category of you know the issue was not that I failed to remember things but rather that my eyes just kind

**[06:45]** of skidded across paragraphs without even realizing if you're you know halfway through a chapter and you're thinking what it what is the chapter about okay so brighter question is now that we have all these online resources

**[06:56]** some of which you know you've helped develop Khan Academy and elsewhere it seems that the value of conscientiousness is a trait has dramatically increased if you can

**[07:08]** motivate yourself to learn these things the world is out there for you to absorb what are the sort of design or UI or even content modifications that can be made to give you a conscientiousness boost where in the past you have a

**[07:22]** professor you have peers you have in-person deadlines that motivate you is there something equivalent to a pen and paper or how that boosts your mathematical IQ for conscientiousness right so one enduring result in

**[07:36]** education psychology is that when you're doing a lot of cognition metacognition is difficult so what I mean by that is like when you're thinking really hard about the stuff on the page it's very difficult for you to like plan uh

**[07:48]** regulate yourself figure out what the best next action to do is reflect and evaluate uh you know whether you're understanding things you know all the stuff that we're talking about about asking questions that all

**[07:59]** that gets harder as um as the material gets harder and as it gets less familiar so uh one common thread at least in kind of learning science stuff has been to

**[08:11]** outsourced metacognition so some of the ways we Outsource that are actually very familiar they're things like somebody gives you a syllabus and tells you what to read when you reference that so that is a user interface like that is a

**[08:22]** design practice if you're a self-motivated student one thing you can do and that I've done is just go appropriate a syllabus from you know some graduate level course that corresponds to the text that you're

**[08:32]** reading and say like well then you know that might be a good guide as to you know what's most important how to approach this there are also lots of things that that one can build directly into the interfaces just as one example

**[08:45]** in Quantum country uh which was a textbook that Michael Nielsen and I developed to explore some ideas around augmented reading experiences we embedded a bunch of review questions every say 1500 words or so in this text

**[09:01]** on Quantum computation and our primary intention in doing this was to help people remember what they read and we we have this theory that part of what makes it hard to learn a complex subject is that there's all these new definitions

**[09:17]** and notation and terms and things being thrown at you at once and you're being asked to combine these things which are still unfamiliar and so you're constantly having to retrieve these elements and struggling to do it either

**[09:30]** it's taking a while or your success rate is low so anyway that was our motivation but uh had this other metacognitive benefit that was really important that you read 1500 words and now you're being asked these questions that is an

**[09:43]** opportunity for you to notice that you did not in fact absorb what was in that thing not that you don't remember but that like you know there's there's a word in the question that is apparently important that you simply didn't even

**[09:54]** notice and so not only does that give you feedback so it tells you oh maybe you need to go reread that specific section but it may also change your behavior towards future sections so in interviews

**[10:10]** readers told us for instance that after they reach the first set of questions or a particularly difficult set of questions they found themselves slowing down and reading more attentively or realizing

**[10:21]** actually that they're they're reading practices were ineffective in general you're kind of in the way that that you were mentioning towards the start of the conversation there's been a bunch of research on

**[10:31]** key phrase here is something like adjunct questions you know questions that go along with a text that's kind of like what I was just talking about and uh they have all kinds of effects so the adjunct questions have

**[10:42]** the the kind of effects on forward material I was just describing and they also have uh the effect of making you kind of reflect on what you've just learned and in addition to the questions being asked you might find yourself

**[10:54]** pondering uh well I'm being asked about this but why does this matter yeah on the point of adopting the syllabus from somebody else I mean one thing one problem you might have as a self-learner is you have some gold this is the reason

**[11:07]** I'm learning this and then you start thinking well do I really need this chapter or do I really need this content yeah at this point you're doing the metacognition that you were using you're trying to use a syllabus to avoid

**[11:18]** yeah um should if you are still trying to software then there is a resource that is a close approximation of the syllabus you want should you just like hey I don't know why I need the Shafter I'm

**[11:28]** just going to go through it or it's right just should you use your own judgment there this is I think like a pretty classic issue for learning in general uh you have this problem where you have to sort of to

**[11:42]** bootstrap yourself in a domain you have to Outsource the the question of what is necessary to know you might know for instance that you really want to build you know a model that can generate images given descriptions or something

**[11:56]** like that like mid-journey but you don't even know what you need to study to do that so you know you pick up some textbooks on machine learning and you're kind of Outsourcing the answer to this question to the author like what is

**[12:06]** necessary to know to build things and maybe you can find a book that's actually labeled what you need to know to make an image uh generating model but even then you're you're Outsourcing your answer to the author so you can take

**[12:18]** that answer as a start and treat it as tentative and you know revise it iteratively and as you become more skilled you can lean Less on it and you probably should I think like a very common mistake that people make is to

**[12:36]** feel like they need to do the thing the right way and that is exhaustive and completionist or something if they fail because they find themselves bored or unmotivated because the material doesn't actually

**[12:48]** seem to relate to what they want to know but but they're just kind of going on faith that like well if I follow what the author says you know everything will be good anyway they find themselves having trouble for that reason and then

**[12:56]** they just stop so this is bad and they would be better off just skipping around according to their interest and continuing one other thing I'll say about this is that uh

**[13:07]** the role that these syllabi play is as a scaffold this is sort of a term of art from learning science but it's actually it relates to the the thing we're familiar with if you want to get higher up a building you may not be able

**[13:23]** to climb it yourself but but you can build some scaffolding around it and then suddenly you know you can reach that top shelf or you know the top of that building where the metaphor breaks down

**[13:33]** is that although scaffolding is ubiquitous in in education we um we give you simpler versions of questions uh first that's that's a kind of scaffolding we partially work the answer first that's a kind of scaffolding we

**[13:46]** give you worked examples uh first uh where we might ask you to like predict the next step of the work example that's also within a scaffolding where the metaphor breaks down is is that once you become more capable we try to remove

**[13:58]** the scaffolding um it's called fading the idea is that once you have solved a lot of calculus problems you you don't need half of it worked out and you're just like filling in one of the blanks

**[14:10]** anymore um and in fact doing that would not be as effective a learning experience so the application with the syllabi might be something like if I'm studying something in computer

**[14:20]** science which is a domain that I know really well I don't need those syllabi not in the same way for most subjects and uh I think that's mostly just because uh the amount of

**[14:35]** cognitive demand that's placed on me by the subject is just much lower than it is for other subjects so much of it is familiar already that I can deploy my own planning more effectively as I go but it's also the case that um

**[14:49]** because I know so many things about the subject I can do a better job from the get-go of making a plan is making a plan requires kind of modeling a path or predicting a path or

**[15:05]** saying like well I guess I need to see how this connects to that or something like this and it if your destination and your starting point are very far away then you can't necessarily see all the things in between or how to draw those

**[15:16]** lines but if those things are only a couple hops away you can maybe kind of infer pretty accurately right I guess this maybe implies that if you do want to learn about a subject it might just be helpful to just do an

**[15:28]** intro to X subject course or textbook not necessarily because it is instrumentally valuable to I don't know whatever problem you're interested in but because it'll give you the context on by which to proceed on like the

**[15:43]** actual learning um that's true it's also the case that like you don't even know like you don't know all the stuff there is right and this is another key problem there's another reason why we Outsource stuff

**[15:54]** like uh there's a fundamental tension in unschooling for instance like doesn't let the kids pursue what they're interested in and like that's cool there's there's a lot of good things about that but also like say that a

**[16:06]** kid's like true passion turns out to be like I don't know ocean geology or something and they're in a landlocked country and there's just no one around them that talks about ocean geology uh then they're like missing out on some

**[16:19]** great opportunity but you know if the school had a program where they are like bringing in guest speakers or whatever and then there's a special lecture on Ocean geology from this person and it lights up the kids world uh even if they

**[16:31]** wouldn't have chosen that lecture like that's a good thing yeah unschooling is actually an interesting subject to talk to you about oh we'll get back to that but before that I want to ask you about this excerpt from a Paul Graham blog

**[16:42]** post yeah how you know that's the title of the post and it says reading and experience train your model of the world and even if you forget the experience or what you read its effect on your model of the world persists your mind is like

**[16:56]** a compiled program you've lost a source of it works but you don't know why so it's a compiled program you don't need the source code is it okay that we're forgetting so much of what we're reading yeah yeah I mean what he's saying is

**[17:09]** true to some extent whether or not that extent is sufficient is going to depend a great deal on the situation and on what you need if your aspiration actually depends on having a deep detailed understanding of the

**[17:23]** material then um the kind of imprint on your world view or on uh your your automatic responses or something like that made by the book may not be sufficient um on the other hand if what you want is

**[17:38]** to absorb a lot of different like ways of looking at the world like that knowing the details of these isn't necessarily important maybe you just want to know like well you know Confucius emphasizes community and

**[17:50]** society as a moral patient and contrast maybe to the individualism of a bunch of like humanist philosophers um and like that's kind of the level that you feel like you need to make decisions in that domain then I think

**[18:01]** that's fine very practically speaking it's funny that he uses the word compile uh because like one of the one of the prominent theories of of cognition that that is like how we come to know and learn

**[18:13]** things is this Theory called akdar by John Anderson and uh a key part of it is this this uh process equals knowledge compilation this is the process by which we take like individual facts and turn them into kind of higher level patterns

**[18:33]** that we can generalize and apply in more contexts um and I think that's what Paul is gesturing at that you read a book it contains like a story a case study and by reading it you learn

**[18:48]** to generalize to some extent and you apply it in other contexts when it seems relevant the reason why I bring up Anderson's theory is just that like here's a bunch of specific claims about like what's

**[19:00]** necessary for knowledge compilation to happen and like what you'll be able to do as a consequence of certain degrees of knowledge compilation and I think like he'd probably respond to this by saying

**[19:09]** something like you know actually in order to effectively compile things that you've learned into schemas that will match future scenarios effectively then you need to be exposed repeatedly to those things you need to like use them

**[19:22]** you need to do a variety of things that will basically show your brain that it is relevant to apply these things in combination and simply reading probably won't do that but if you read and you have a lot of conversations and you're

**[19:35]** in a context where it's kind of demanding and it's drawing on what you read then you may naturally do that kind of compilation step I've actually been thinking about this in preparation to talking with you

**[19:46]** where I look back on some of my old conversations and you know I've had the pleasure to talk to a lot of interesting people across a lot of different fields and at the time I interviewed them and had done all the prep I actually kind of

**[19:58]** had a lot more context than I could remember now sometimes I'll listen back to a conversation and I won't even remember the content in the conversation and I know I remember thinking after the conversation I knew so much more about

**[20:09]** this field and was compressed into this one hour interview right I had to prep other things that might come up and afterwards I'm like I don't even remember the things that were in this one hour but then the other part of me

**[20:19]** thinks well I'm getting better at doing the podcast that might imply that you know I've picked up something but it is a shame that I didn't have some sort of rigorous practice throughout the time of you know retaining the material that I

**[20:30]** was keeping well yeah I mean I expect the main way in which you're getting better is actually not really about any of the details of those materials I think it's about your practices uh as as an interviewer the way that you generate

**[20:44]** questions like you probably have a bunch of patterns whether you know it or not like you read a thing that a person has written in hopes of generating good questions about it and even though you don't have this

**[20:56]** habit for textbooks yet maybe of constantly demanding things of the textbook um you have I think started to develop this of essays or blog posts that interesting people you're interviewing

**[21:07]** have read and uh to point to this Anderson Theory like in the course of repeatedly doing that you've made it automatic parts of it automatic so that you don't need to do it consciously you

**[21:22]** can focus more on the material you can probably take on more difficult material or actually understand material at a higher level than you could have before because less of yourself is engaged in this kind of question of how do I make

**[21:36]** the questions from the material yeah I certainly hope so otherwise uh there's a question to be asked when I've been doing all these years so you know having interviewed some of these people who are Infowars and have

**[21:48]** consumed and continuously consume a lot of content this is something you also noticed uh and pointed out in your notes but you know Tyler Cohen for example I don't think he has any sort of note-taking practice you know you know

**[21:59]** uh just devours information yeah what is your theory of how these people are integrating things right that they're Tyler's Tyler's a good example I think he's actually a little easier than some others we might discuss so let's talk

**[22:12]** about Tyler for a second one of the other things that's so interest interesting about Tyler is his writing obligations so this is a man who's blogged every day since I don't know 2007 or something

**[22:22]** like this and uh has a Bloomberg column I think weekly something like 1500 words and also has published something like a book a year for I don't know a decade or more and occasionally publishes some academic articles plus like a bunch of

**[22:37]** other collateral so like that is notes um and I think it's also important to note that like the way that Tyler writes these blog posts and the way that Tyler does these columns and even the books is very different from the way that many

**[22:51]** other book authors work like Tyler the the blog posts often have this like real first draft mentality to them like he's just thinking out loud and he's got Decades of practice thinking out loud and like writing down

**[23:07]** a decent take the first time and so he you know he gets something pretty good the the first time much of the time and that that works for him so like that kind of is a note right like uh get doing the thing that or I guess like

**[23:18]** your initial thoughts on the subject is is kind of what you would write in a note yeah one of my former guests um Scott young was comparing Brian Kaplan into Tyler Cowan's books and he said you read a Brian Kaplan book and it's like a

**[23:29]** chess game right like you the the opponent is if you try to move a pawn up on this case for Education I've got this you know Rook that I can move here um with Tyler it's more like you know he's like shooting the on subject

**[23:41]** basically yeah on a separate question do um do llms make memorization more or less valuable right so there's a case you can make for both uh but on net are you is it more important to have more on key cards in

**[23:56]** your deck yeah maybe this is a good time to talk about what memorization is or like what it's for so we could use that word to refer to the practice of like learning more trivia for for instance like so for

**[24:08]** instance uh a thing that that I and uh some people I know have done is like gone through this this book cell biology by the numbers which says all of these things like uh how big exactly is a nucleotide like how much volume does it

**[24:21]** take up it's kind of helpful occasionally to know that it's about a nanoliter um and that that can help you model things so you can just like commit all of those things to memory right that's

**[24:29]** one kind of memorization we could talk about how LMS affect that but I I just want to make the case that so much of what you do and experience day to day is memory bound uh or is memory influenced in important ways

**[24:44]** so just for instance your ability to understand a difficult argument even in the course of a text is memory bound some of that's working memory but um your ability to understand an argument that has many

**[25:02]** steps in it more steps than you can keep in your working memory depends on your ability to think of some of those steps in terms of some stuff that you already know so that you can kind of reduce it or abstract it

**[25:14]** likewise in Creative work there's a bunch of studies trying to catalog case studies of how it is that people have flashes of insight you know it's a little hard to talk

**[25:24]** about that but one of the things that's a pretty consistent source for insight for people is noticing a surprising connection or a surprising contradiction it probably feels pretty familiar right like you're you know you're reading

**[25:36]** through the newspaper and you see like you know people have finally figured out how to do X and you're like wait a minute that means if I combine it with this other thing like we'd be able to do why or something like that you know

**[25:46]** um now that's only possible if the other thing uh is in your memory like if you have to think to look up the other thing uh then the newspaper wouldn't seem so Salient to you likewise like

**[26:00]** and in just really boring ways early on in my time in Khan Academy I just um learned in in a very thorough way using memory systems just a whole lot of details about the education Market

**[26:13]** uh and this let me be in you know high level executive kind of conversations where we're trying to figure out strategy stuff and somebody would propose a particular direction or you know

**[26:24]** this what about that I could say like well you know the the the total budget spending for instructional materials is this and like that market is growing by this percent per year and 10 of students in the US

**[26:34]** are in this place and you know and so on and so forth and so basically like on the fly I can evaluate ideas in a way that others can't so anyway this and other things are kind of just part of my rant about people I think in

**[26:48]** general we we under appreciate the role that memory has in our lives so just to come back to the question explicit memorization or um explicit making sure that you can recall the thing reliably we can test it

**[27:00]** against these things so it for the case of the creative Instinct for instance noticing the contradiction noticing the connection I imagine that we will have future notebooks that will do some of this noticing

**[27:13]** with us and that will decrease our need to be able to rely on our own sense of salience or something like that but I I I guess I don't know how much I I I'm skeptical

**[27:28]** that like my own experience coming up with with weird ideas that feel very new uh is that it feels very personal if yours it feels very inquite I often haven't been able to describe textually the constituents of the thing very

**[27:44]** clearly um there's just kind of a feeling that something in this general direction is connected with something in that general direction or there's attention and so that makes me a little hesitant

**[27:54]** llms depend on our ability to externalize things and to make them legible back to the learning point about the role of memory if what you're trying to do is to understand something pretty difficult you your ability to understand

**[28:06]** that thing is still absolutely going to be bound on your memory of the constituent material dude do you think there's value in there's pedagogical value in forgetting so I guess some sort of anecdotal or unrelated evidence is in

**[28:21]** you know a neural networks sometimes you can improve performance by pruning some of the weights obviously we forget things right so clearly we don't remember everything when we sleep we lose a lot of our memories is it

**[28:33]** possible that if we're getting the details and only getting the gist that actually helps us better generalize the insights we're getting from texts and things like that what do you think of that way of thinking yeah it could be so

**[28:42]** memory is very connected to attention um and we can't attend everything right so one of the rules of memory is to help guide us to the things that are important you know so like maybe maybe I happen to know uh you know the magnitude

**[28:57]** and energy of an electron volt that's something I can draw on because of the memory system stuff but I also don't like I don't want that to be like front and center in my mind all the time I want to be hyper Salient the way that I

**[29:07]** don't know some very important design principle is to me so yeah there's there's some role there there's also there's some theories that um the reason we have forgetting is that our environment our ancestral

**[29:19]** environment was very traumatic and so our episodic memory in particular we would like to maybe not be all that faithful um I I actually I don't know the status of those theories probably why we forget

**[29:31]** dreams as well right like dreams are pretty traumatic if you if you thought of them at the same as a real life experience yeah so I mean another weird thing about memory is that as far as we can determine memories aren't lost

**[29:43]** exactly at least not completely that there's a bunch there's a series of interesting experiments that people have used to demonstrate that you know decades later like things are still there if you can cue them right uh

**[29:53]** people can bring things back uh even things that they they feel are lost uh and of course like you can also cue people in ways that are hallucinatory uh so we need to be careful about that but I guess the reason why I bring that up

**[30:07]** is that it flies in the face of this view that like there's a limit like one of the things that I think is kind of weird about this memory system stuff or like memory Champions ships or something like that it's people like oh if you do

**[30:18]** if you do these things like will you start to forget other like normal human stuff um and what's weird is like no you know I've been doing this memory system stuff for years

**[30:28]** um like I just know more stuff now and this is aligned with the the experimental literature which seems to suggest that like there's probably upper bounds but we're not close to them and some of these memory Champions have

**[30:42]** memorized I mean truly absurd quite you know orders of 90 maybe two orders of magnitude more things than I've practiced certainly people who are multilingual uh have uh really really absurd

**[30:55]** numbers of things memorized so there isn't like a resource management argument uh well if there isn't why do we forget so many things is there some reason the the brain just yeah

**[31:09]** maybe they're just not the we were training the ancestral environment to find certain things the alien that are just don't map onto books no it's a good question so we're getting to uh we're getting to a part of the cognitive

**[31:21]** science space that that I'm less familiar with and also that I suspect we simply know less about um but let me just riff a little bit one of the things that we sort of know is this idea of spreading activation um

**[31:34]** so when you go to try to look something up or when you try to deal with a particular situation there's something almost kind of like DNS exchanges or like routing on a network or something where okay like we start

**[31:49]** from some point that it's like a stimulus and uh just speaking very informally like we kind of expand outwards from there and there are effectively like weights on those connections and by tuning those weights

**[32:01]** effectively we like route the packets on the network effectively memory is is encoded in these weights at least partially so if you didn't forget things then you might just have this like weird cacophony on the the network and in

**[32:15]** particular like what's Salient what to do next like which response seems most appropriate to this question like you might answer those kinds of things very ineffectively because all this stuff is coming up for

**[32:28]** you that is like much less relevant like one of the theories about how well we remember stuff in what circumstances is actually called predictive utility Theory and it suggests that like the probability of retrieval of a particular

**[32:41]** item in a given situation actually does correspond with basically a model of how like to what extent the brain predicts it will be useful right and in the prediction but it doesn't necessarily map on to doesn't necessarily exactly

**[32:55]** and so like you know when you repeatedly access something when you practice retrieving it the prediction of the utility of the thing goes up yeah and when you do it in a variety of situations it goes up across a broader

**[33:07]** distribution okay so that this is interesting when did you start your memory practice presumably it was after after Apple yeah okay so let me ask you this so at Apple you were in charge of a bunch of

**[33:19]** important uh Flagship features on iOS and I'm guessing other things presumably you were you didn't have some sort of practice but since you were encountering these things day to day that natural frequency and way in which problems came

**[33:33]** up did you have a worse understanding of those problems and the things now knowing what you do uh and knowing having the practices you do you're able to comprehend now

**[33:42]** I don't know that question made sense no that's a great question so I mean like here's a fun thing I was much better at what I was doing then then I am at what I'm doing now um that's pretty funny so I mean

**[33:57]** it was just totally different uh let's talk about this a little bit this feels very very juicy for me most of what I was doing was engineering some of it very difficult engineering but mostly engineering mostly on

**[34:10]** like things that were fairly well understood so I wasn't trying to decide what what should be done usually sometimes I was from a technical perspective but certainly rarely from a product perspective was that a relevant

**[34:23]** question for me um I was kind of like a somewhat design-minded engineer and I did a bunch of kind of engineering and design-ish things on tasks which were set out for me at that point

**[34:34]** I've been programming for a really long time I had 13 years maybe by the time I joined Apple longer and programming in apples ecosystem for probably two-thirds of

**[34:50]** that time three quarters of that time so everything was just really familiar and like it was mostly flow all the time every day I was kind of like I was just in it uh I knew the stuff that I needed to know I was very well practiced and

**[35:03]** the space didn't change that much you know like Engineers most engineers at Apple most of the time are not like pushing the frontier of what is known like trying to discover they're like doing very

**[35:18]** difficult technical work mostly applying things that they already know and understand quite well to problems which are usually not always moderately well and but pretty well understood let's say

**[35:29]** memory was essential to me doing that job well but I had already built most of it by the time I got there I'd already built just tons of stuff for Apple's platform and I had to learn a lot of stuff I learned a ton of stuff about the

**[35:41]** internals of those systems but because I already had such a rich understanding both of Apple's platforms and of computer science and engineering in general uh I had this really rich Network for stuff to slot into

**[35:52]** so learning stuff is easier when you you have other stuff to connect it to is a nice principle metacognitive load on me was lighter because others were figuring out what we should be doing so just like by contrast now I'm doing

**[36:05]** research like I'm trying to discover things that are not known I'm trying to make things that didn't exist the hard questions that I answer are mostly like what should be done or like what should I do and that question is not just a

**[36:16]** technical one of like how should I implement this like feature that needs to get built but like what intervention on a reader should be taken that requires synthesizing lots of different unfamiliar literatures

**[36:30]** there's two different threads I want to go on maybe I'll just mention the other one this is also related to the thing we're talking about a few minutes ago uh with uh L alums and there's this thing that I'm sure you've talked about

**[36:40]** yourself as well the Swanson linking where this guy was just um I don't know Swanson like that okay actually uh Michael Nielsen is oh okay cool um but this guy was just somebody who read the medical literature and uh he was like

**[36:54]** familiar with a lot of esoteric results and one of the so different things would come up and he would be able to figure out what different things are connected for example I think he noticed in one case that headaches are linked to

**[37:09]** some other symptom and that other symptoms is linked to magnesium deficiency and so apparently a whole bunch of people's headaches were solved once they were given a magnesium supplement and you notice that

**[37:18]** connection again this is the kind of sort of um combinatorial thing uh that you wouldn't notice otherwise uh but on this on this subject itself so listen there's this natural way in which you're able to get up to speed in all the

**[37:31]** things that are happening at Apple and is it possible to be advantageous to do similar kinds of things in other fields for example instead of doing an explicit space repetition system when you're trying to absorb material from books you

**[37:43]** just read a cluster of books and hopefully things will just come up that are relevant to get them again or is there a value in having explicit practice of setting up cars and so on yeah right so so again the answer is

**[37:54]** going to be it depends I I think that that maybe the most familiar example of what you're talking about is immersion learning a new language right so immersion learning is like a great thing um and it's going to be more interesting

**[38:07]** and more effective than doing space repetition practice it's going to be integrative it's going to be um socially there's a bunch of stuff about social learning that's relevant a problem is though is that like say that

**[38:19]** you decide you want to learn Swahili today and you like go down to like the local Swahili Community Center uh and you're like cool I'm gonna immerse myself like good luck you know yeah you can't even get started yeah so through

**[38:32]** this lens explicit practice is a way to bootstrap yourself right likewise a great way to become a better musician all of the best pianists at sight reading that I knew in in University uh played with churches they were so good

**[38:48]** at sight reading because you know they had to show up every Sunday and they're playing a different thing uh new him every Sunday right so this is immersion also um and you know over time they're

**[38:57]** learning all these cadences and these things that are really common and whatever um but like you can't show up and be the church pianist every Sunday in the first place if you don't already have like

**[39:06]** some decent foundation so this is sort of a bootstrapping argument that like one role for explicit practice of this kind is to get yourself into a position where you can more naturalistically reinforce I see okay got it but there's

**[39:19]** still going to be instances where the naturalistic reinforcement isn't going to work so for example the linking that you brought up one issue for doctors is rare diagnoses yeah so if it's only going to be once every couple of years

**[39:32]** that you see a patient that's going to present with these symptoms that's not going to be frequent enough to naturally reinforce your memory of that and you're going to need some out of band mechanism and unfortunately I think for many kind

**[39:45]** of creatively creative insights that may be closer to the regime that we're in yeah that makes a lot of sense where in many fields you just have the things you're regularly doing is the thing you need to reinforce it makes a lot of

**[39:58]** sense that if you're a researcher the long tail of events that might come up is a thing you're you know it might happen once every few months but the regularity is not a thing that matters right it's sort of effect on your work

**[40:07]** here's a question I actually have so when we were doing the practice or when we're doing the the quantum mechanics textbook it was like three hours and afterwards I was just exhausted and I was actually surprised that you went the

**[40:21]** entire three hours of that Interruption and so afterwards I was packing up and you're like hey I'm about to actually go to my piano lesson right I was so confused at how you had a stamina to keep going is the stamina just uh

**[40:35]** inherent in you or is that something you did to develop so one of the things that I I think is funny about stamina is first off there's some kind of weird Grass Is Always Greener kind of situation where like I often feel struck

**[40:45]** by other people's stamina and feel like I have very little of it I struggle with energy I've actually written extensively about all my struggles with energy and like ways of managing energy I spent a lot of time thinking about it and like

**[40:56]** managing my energy levels structuring my day around it so I think there is something where like one often feels maybe lower stamina than one actually is because one misapprehends other stamina okay so in that particular situation how

**[41:10]** do I explain why three hours of studying Etc first off social so uh if I were alone and studying that book for three hours um and I weren't effectively trying to perform for you uh

**[41:24]** it wouldn't have been nearly as energizing for me and I definitely would have taken breaks I still would have been able to go for three hours I think um and part of the reason for that is that it's simply way less hard than

**[41:38]** things I normally do in some sense learning quantum mechanics like should be like much harder and it kind of is cognitively demanding in a lot of ways right

**[41:47]** um it's much more cognitively demanding in kind of a direct way than what I actually do day to day but it's much less it's much less demanding on what William James calls the energies of men which is something like like a life

**[42:02]** force that permits you to act according to your will or something like that maybe it's gumption maybe it's willpower maybe you know some people call it spoons I don't know these aren't all the same thing exactly but um

**[42:15]** sitting and staring at a page and deciding what you should do next on a research project is incredibly draining on that resource the not knowing sitting and not knowing is like the hardest thing that I do in

**[42:29]** my work and so there's something it's like a wonderful vacation to be presented with uh oh great somebody else is going to tell me what to do right this is great so although it might be less demanding than your usual work it

**[42:43]** is definitely more demanding than the way in which I or most people approach uh textbooks or other material in the sense that you know I would just like read through and then once I get to the exercise I'm like let's see what I

**[42:56]** didn't understand um whereas just the attention and the intensity to go through sentence by sentence and constantly being paying attention seems like way more exhausting than yeah I mean so this is sort of true

**[43:09]** like and it's definitely the case that I will occasionally do some of this like before bed reading where I think like oh like you know let me just do a little bit more you know and it's like it's basically useless yeah

**[43:19]** um but I want to make the case that there is a kind of pocket that you can fall into maybe you call it flow I don't know where like the demandingness that you're bringing to Bears match to your ability

**[43:29]** the book is not overwhelming like you feel like you can make your way through it and um this is actually more engaging uh so I occasionally will find myself reading as an undemanding reader and

**[43:43]** finding my attention kind of slipping because I I feel like I'm just not that attached to the text emotionally I'm kind of reading dutifully I'm like trying to get through it that produces sometimes like an

**[43:58]** adversarial aspect where the text is in my way uh or it's kind of something to be I don't know like like accomplished yep um and often then I will find that I need to bring more gumption to Bear to

**[44:15]** kind of power through and like you know make myself sit there and keep flipping the pages then I need if if I actually just like open my curiosity and open my my attention and really start engaging with the book there are sorts of ideas

**[44:28]** that people come up with or different pedagogical tools which um or mediums that give closer connection to the reader one is you know you have some sort of fiction account where a concept is introduced and reinforced uh

**[44:43]** or you have a video game with characters you care about and as far as I know there isn't something that has really taken off uh using these sorts of new mediums what what do you think that is is it just an

**[44:54]** inherent limitation of everything about text and lectures or people just haven't given it the right uh content and yeah uh design yeah I'm fascinated by this question let's see I can say a few things about it one is that I I would

**[45:07]** argue that uh one medium is taken off in an absolutely enormous way in this video people love video like people will watch Grant Sanderson spend you know an hour going through some explanation of an esoteric math problem people who would

**[45:19]** never crack like a springer graduate textbook in mathematics or something like that the issue is that like they will in general not walk away from that interaction with much understanding yeah but they're much more engaged yes

**[45:34]** so that's cool that's suggestive you know and suggest the question like well but like is there a version of that that actually produce detailed understanding maybe one approach to producing that might be like a game my my favorite

**[45:48]** example of this is the witness by Jonathan Blow you played the witness okay I I think the witness is an absolutely extraordinary work of art um so it's a game that that has no text at least no text that's relevant to the

**[46:00]** game elements um in kind of classic missed style you you wake up on an island figure out what's going on and the game proceeds to explain to you without using words but just by shaping your

**[46:15]** environment a series of extremely complex mechanics basically of a system that exists in this in this world um so you learn a bunch of stuff and it

**[46:30]** gets to the point where it feels like you're in conversation with the game's designers it's like ah he's asking me to do this here no one's asking you right there's no text but you can feel that you are being asked and you perform

**[46:44]** some interaction in the environment and you feel that you have answered and The Game responds in kind this is very very interesting it's like it's a medium of action so people try to make educational games games which are explicitly about

**[46:58]** arithmetic or something Jonathan blows game is not about that it's the mechanics that you learn are they're like about the environment I don't think anybody has yet really succeeded in doing this about explicit subjects

**[47:10]** there are for instance things like Kerbal Space Program maybe people learn some things about project management or orbital mechanics from that zactronics has a bunch of games that are sort of about Assembly

**[47:22]** Language roughly speaking maybe you can learn some things about that the issue seems to be that games are ultimately they're an aesthetic form like the purpose of the game is to have an experience that feels a particular way

**[47:35]** and so they're sort of serving a different purpose than Grant's videos or a text Grant's videos are also serving a different purpose from the text like the text you might pick up because you're

**[47:50]** like I want to be able to build a robot like so you pick up a textbook on robotics or something and so is there something that you can pick up that's sort of like a game in so far as it's an active environment that you'd use in a

**[48:02]** similar situation to I want to learn to build a robot maybe kind of um we don't we don't quite have those yet we have some things that are kind of like that I don't know if you've seen like from

**[48:13]** nand to Tetris oh yeah yeah this is a very interesting project that's kind of along these lines uh and what characterizes it like games is doing it's active so when I was asking all

**[48:25]** those questions of the book that was active learning active reading nand to Tetris is naturally active so this is a course in which um you kind of start with basically nothing uh you start with memory and and

**[48:38]** you you build a virtual computer and you build Tetris you build it uh processor and stuff and um so the whole thing's active like the whole time you're you're making the computer grow this is doing a similar job to the

**[48:51]** question asking that I was doing except that um you don't have to regulate all of that yourself the regulation the choice of what activity to do is in the course

**[49:01]** is in the structure of the material I think there is waiting to be created some kind of mass medium that is like that but that can be applied in many many circumstances

**[49:15]** we have the non-mass medium version of it already and it's apprenticeship like if you want to be a good um yoga teacher you like go hang out in yoga studios if you want to be a good Surfer like you go to the beach when the

**[49:27]** other Surfers are there and you like participate peripherally uh you talk to them and about their tactics they might give you some feedback eventually and you'll start to participate less and less

**[49:40]** peripherally over time and eventually you'll be part of the community this is in a mass medium we can't print a billion copies of it really we can with a book what is the experience of watching George Haas on the stream a

**[49:51]** code of tiny grad how does that compare to just being in an office with him yeah um because even if you're in an office with them there's you know there's there'd be constraints on his time and how much engagement there would be

**[50:01]** why why isn't the video a scalable way to increase the partnership I incredibly excited about streaming actually as a medium for this so what we're kind of gesturing at a particular kind of of learning that needs to happen

**[50:16]** um it's often called tacit knowledge so like one of the things that you have to learn to do as an engineer is to learn to deal with a hundred thousand different like weird situations where something is not behaving the right way

**[50:28]** and eventually you've learned a kind of pattern recognition you learn ways of dealing with this and uh much of this is like not described in any book it's not explicitly taught you just kind of learn it by doing it over a long period of

**[50:40]** time so by watching George do it I think that people do absorb stuff they can absorb some of that knowledge that's part of how apprentices absorb that knowledge there's a few things that are missing you know you're not getting

**[50:54]** feedback there's a whole lot of chaff there like there's a whole lot of stuff that probably isn't all that meaningful it's also true for apprentices so I'm pretty actually I'm pretty excited about streaming videos I I have um I've

**[51:07]** complained loudly that there aren't more designer streamers so one of the things that I think is really interesting is that we have some disciplines like programming where there are like a million books on courses about how to

**[51:23]** learn to program uh and they don't they don't give you everything you need there's this task of knowledge stuff that you that you need to develop but like you know like if you work through these courses if you go through the MIT

**[51:32]** open courseware for computer science like you'll be able to build some stuff uh and and you'll be able to leave yourself up um this is not true in all domains you know if you're looking at uh well in particular design but lots of

**[51:45]** other domains that are sort of like that like music Al position or architecture or something like this nope like it's normally done in studio classes uh lots and lots of Hands-On feedback um stuff like the feedback is highly

**[51:58]** contingent it's highly contextual we just haven't figured how to communicate this um and so it's good to see lots of programmer streamers but I really want

**[52:08]** to see the streamers in these other domains right on the point about the more programming books ironically the reason why there's some more resources on programming is that it's just so legible but it already makes it easier

**[52:19]** to understand in the first place um so you just have this reinforcement but uh so you know the man to testress is let's say it's like a video game uh analog to learning uh maybe not just programming but how things in the

**[52:32]** internals of a computer work yeah but programming has an element where it already feels like a video game I have a friend who has a sort of intense sort of manic energy and he used to be addicted to video games when he was a teenager

**[52:44]** and now he just stays up all night in these coding binges it's just the same part of the brain are you optimistic about things like video games and fiction being able to work in fields that are

**[52:55]** not already kind of like a video game like programming I think what makes programming feel like a video game is this this sense of instantaneousness this sense of direct contact with the

**[53:10]** environment you're learning about a kind of a conceptual world but that world is is right underneath your hands and as you manipulate it you're constantly getting this feedback the red squiggly you're pressing command R regularly

**[53:23]** and uh you're you're seeing it fail and that feels great like there's this feeling that's that's very common for programmers and and it's it's Laden with doom the feeling is uh

**[53:37]** it's like 9 p.m and you've been working on a thing all day and it's almost working it's almost working and you know like if you just debug this one thing then like your project will be like done and you'll be able to like go to so

**[53:50]** you're like well I'll just stay up and like I'll debug this one last thing and then you start debugging it and you get it and you solve it and that feels great and then immediately you like run into like one more thing like oh it's almost

**[54:02]** running all the way through it's almost going end to end and you're like well I'll just stay up a little bit longer and you know before you know it it's like 2 A.M and you keep going because it it feels so good like you you feel the

**[54:12]** sense of forward progress you're not just staring at a wall I think like for the programming problems where you are at a brick wall it doesn't feel like this it feels bad um so can every field be transformed

**[54:24]** into something where you can feel the sense of forward progress you can get this rapid feedback cycle I think that's really hard I I think some fields like it's not clear to me that they can

**[54:35]** be transformed in that way I think we can like get a lot closer uh in most cases then then we're at right now so what's hard about designing the user interface

**[54:49]** um is that often there's this feeling of exploring kind of a combinatorial search space programming often feels like a search problem too you have a sense that there's like

**[55:01]** there's some right way to solve the problem there might be some set of right ways to solve the problem and you're kind of looking for it and you have some heuristics that guide you to like oh this might be a dynamic programming

**[55:11]** problem or like this might be something that that is solved well by you know separating concerns or something like that um design often feels less like that you have those heuristics too you have those

**[55:20]** patterns too often it just feels like nope I just need to try like 300 things uh and so there's this like characteristic where you'll look at a designer's figma file and like what you do in figma is you press command D this

**[55:34]** is like the core action of figma is to duplicate um so you have an artboard you tried something and you're like that didn't work so you've selected you press command D and what you end up with and

**[55:45]** you look at design Twitter and it's just all these screenshots of people's figmas with like a million artboards uh they're just trying stuff and you don't have this feeling or at least I don't and I think many designers don't have this

**[55:56]** feeling of like progress It's like you're just kind of exploring parts of the search space and like you're learning that parts of the search space don't work uh and you know eventually you stumble on one that does but you

**[56:10]** don't have this feeling of like getting closer often uh often there will be like weeks that go by without feeling like you're getting closer because what you're doing is just kind of like narrowing the search space

**[56:22]** interesting although there are people who are obsessed with design in there um and what is the sort of loop that keeps them obsessed with uh this process that doesn't feel intrinsically forward feeding so to some extent I think

**[56:38]** they are skillful so the people that I know who are like this It's a combination of their skillful often and like the nature of the

**[56:48]** problems that they're solving are highly tractable so like a kind of an example of a kind of thing that designers will often rabbit hole into is like designing a poster um it actually often used to be kind of

**[56:59]** a cliche um that at Facebook there were all these posters up on the wall of the office uh very very elaborate beautifully designed posters for like a talk that someone was coming to give at Facebook uh and it's

**[57:14]** like why why did somebody put all this effort into it like well it feels really good because a poster is this like really constrained it's like finite it's ephemeral

**[57:26]** um you you can start it and within a few hours like yeah there's a search space but you can find a decent part of the search space pretty rapidly and once you're there there's this beautiful and very enticing feeling of turning the

**[57:38]** crank and like making it better and polishing it and like trying this or that but when you're trying this or that like all the options are kind of okay and you're kind of trying them out of curiosity or like maybe it can be even

**[57:51]** better and that's very different from the kind of design where you're just like I simply don't know how to do this uh and I think it's part of why those designers loved making those

**[58:03]** posters it's like it's a it's a snack it's a treat it's also something they get to control uh whereas ordinarily they don't yeah just just don't tell the manager how many software engineering hours are used up in the poster

**[58:16]** designing at uh Facebook well yeah it's not no software engineering it's only designers got it but for the software Engineers I mean code golf is the equivalent right what is called golf you know in golf like you

**[58:28]** try to get the lowest score um so code golf you try to solve the problem uh as minimally as possible Right like ah you know I don't need this I can I can like combine this I can do it in three lines if I use Haskell I can

**[58:41]** do it in one line that's a that's a kind of thing programmers do that's that's like this but just endless refactoring is another thing that's kind of like this you have the thing working but it could be more beautiful right well so it

**[58:52]** seems like uh the tools and the ideas you're developing see especially geared towards very intelligent and very motivated students if they would be different how what

**[59:04]** would the tools um that you would develop for a median student the education system look like both in motivation and in other you know other traits yeah they'd be super different

**[59:17]** I kind of got out of the educational space in part because I don't like the framing of this problem like for the median student the education system mostly wants to make the student do things they don't want to

**[59:28]** do it's not about helping them achieve their goals more easily or more effectively for the most part it's about like achieving goals that aren't theirs obviously like

**[59:40]** that's not always true but for the meetings tonight I think it kind of is true I become very interested when I was at Khan Academy I was kind of thinking about this problem and one of the angles that I found really

**[59:52]** interesting was so Khan Academy we were mostly thinking about not just the median learner but like maybe the 25th percentile learner one of the angles that felt most relevant

**[1:00:03]** maybe not from an efficacy perspective but for me from like a breaking out of this getting them to follow goals that aren't their own perspective was to focus on inquiry learning and to focus on

**[1:00:14]** transforming The Learning Experience into something that actually is related to their goals that is we're asking questions that are authentically interesting that they authentically want to answer and that they can participate

**[1:00:28]** in in a way that feels natural I did a lot of experiments with Dynamic media representations of things the idea being that like you've probably seen you know maybe these like plastic blocks or things that people can play

**[1:00:44]** with when they're kids to get an idea of numbers and number systems kids will play with these things unprompted because they're fun like it's just it's a pleasure to handle them it's a pleasure to manipulate them

**[1:00:57]** when you have them in hand it's very natural to suggest like ah can you make a pattern like this like why you can't seem to make patterns like that why is that

**[1:01:12]** so you know for instance you can start to point out things like Cuisine air rods is the name for um a set of 10 rods that have basically unit length one to ten and they're all different colors and so you can do

**[1:01:27]** things like take eight and like the rod that represents eight and put two of the rods that represent four up next to it and show that like this one you can you can like divide into two rods effectively but then if you take seven

**[1:01:41]** like there aren't there is no other pair of rods that for the same color you can put it next to it so you get these different patterns so things kind of naturally suggest themselves

**[1:01:51]** um by experimenting with these materials and having conversations with people around these materials and so one of the things we were interested in was well are there things that are like that that are for more advanced topics like

**[1:02:07]** can we can we create something that's kind of like those rods but that is about a more advanced Topic in math or um are about

**[1:02:16]** uh debates in history or something like that one of our tactics was to lean heavily on social interaction people like talking about stuff with people if it's like a real conversation

**[1:02:30]** for you know and for the same reason that I had to use less willpower to study that quantum mechanics text because you were there with me a student who's engaged in like a real activity with a peer will need less willpower as

**[1:02:43]** well they'll also learn from their peer if you structure things right so social learning becomes interesting interesting but I think at a high level I I mostly have abandoned this question to others basically everyone in the

**[1:02:59]** educational space this isn't totally true but like you know 90 plus percent of people in the educational space are focused on really like the bottom quartile like not even medium

**[1:03:09]** um and there's a good reason for this like many not quite as many people who are in education they are motivated by um arguments of equity and opportunity and they want everybody to have the opportunities they had they

**[1:03:25]** they're very motivated by the injustices that they see in the differing access and the differing support that different people have and they're very motivated by the the very real disadvantages that accrue to the bottom quartile performing

**[1:03:40]** students it's also true that the the marginal impact that you'll have on that student's life will be much greater probably than the marginal impact on say an 80th percentile performance student or so the

**[1:03:53]** argument goes like that student will be fine which is like properly true but there's a there's a big marginal difference between fine and uh uh it's you know supercharged yeah yeah I mean that's

**[1:04:05]** true but any anyway I mean like I say all this to say like I I understand why the vast majority of people in education are focused on what they're focused on and I think it is good and I'm glad they're doing it and I'm I'm mostly uh

**[1:04:18]** have decided to let them do that I just focus elsewhere yeah yeah no yeah I I see tremendous value in focusing on the realistically like the cool new that's coming out you know where's that coming from and what what's the way to

**[1:04:31]** increase that yeah okay so but it's interesting to know that the same tools might not just work across the Spectrum yeah and nothing else to say like part of the trouble here is that like the cool is very likely to come

**[1:04:42]** from students who are like performing at the 20th percentile in school because they're like disaffected and bored and none of this stuff matters to them right and so like part of the trouble here is that

**[1:04:53]** bye like opting out of helping these people learn there there are all kinds of interesting intentions that could probably occur that aren't uh occurring so I don't quite know how to contend with that I guess basically I'm like

**[1:05:08]** trying to bite off a a piece of a problem that feels maybe tractable once you know all the tools are built you know when you're at the end of your career with the with the learning process is it supposed to feel fun

**[1:05:22]** or does it have to feel fun is there an element of even when all the tools are there that there's just like a level of David Goggins you know this is going to be miserable but I've decided to learn this in this way and I just had to go

**[1:05:33]** through it where does Misery come from hmm where does it come from I guess I'm asking this honestly not really rhetorically let me try to answer my own question I mean so let me say first off like I I think I am broadly speaking

**[1:05:47]** very opposed to what I understand to be David goggin's desk uh attitudes towards almost anything in this particular instance I think what I think is something like if I ask why is it miserable to learn a

**[1:06:00]** particular subject the answers that come to mind are things like first off I don't care about this subject and I think that's not what we're talking about like you're asking about a world in which these great tools

**[1:06:09]** exist and someone's using one of these tools to to try to do something they really care about so another reason why it could be miserable that I think is pretty common is that you have some idea about like

**[1:06:21]** you're not going fast enough or like you're failing or you're struggling and the misery comes from resisting that it comes from feeling like you're you're doing poorly and like you shouldn't be doing poorly like it's bad that you're

**[1:06:33]** doing it poorly uh and maybe you're feeling fearful like like others are gonna judge you or like you don't have enough time or something like that and I think that's

**[1:06:43]** basically like an emotional problem that needs to get healed rather than like a practical problem with learning in the case of something like organic chemistry where like you truly do just need to learn like you know 200 names or

**[1:06:57]** something one answer is that like okay that can be done very cheaply using modern memory systems actually so like organic chemistry students suffer through this and they don't need to but even with modern memory systems like

**[1:07:09]** you're probably going to spend a total of I don't know call it 100 minutes across some weeks uh start studying all of these um formulas and that still is unpleasant so can that be resolved and I think the

**[1:07:23]** answer is yes actually so um I was thinking about this in the context of the cell biology by the Numbers book I was telling you about where there's all of these um uh things like the the volume of the nucleotide I

**[1:07:35]** said as a nanolator so to like study the flash card what's the volume of a nucleotide is like not terribly Pleasant I'm not sure it constitutes suffering exactly it's fine uh you know I'll do it while like waiting in line

**[1:07:48]** um but I think there is a better version of that which is like uh solving an interesting Fermi problem which involves that term so something like if I have a vial of the covid vaccine

**[1:08:01]** like how many copies of the coveted RNA are likely to actually be in it uh if the vial is a milliliter large or something that's like kind of a fun little question uh uh and I can enjoy sitting and noodling on that and in

**[1:08:17]** doing so I will need to retrieve the the volume of the nucleotide to help me make that approximation so I think there's moves like that that you can use to kind of paper over any remaining stuff that feels kind of necessarily unpleasant or

**[1:08:30]** wrote I'm actually surprised to hear you say that because one way in which I read your stuff is at least some of your stuff is that this is actually a way of endorsing the traditional way of thinking about

**[1:08:42]** education but using new tools to get the traditional ends to give you an example of what I'm talking about you know you go back to like a Headmaster from the 1900s and you say is is it important to have the taxonomy of a subject memorized

**[1:08:55]** of course it is that's what you're going to spend a year in memorizing some economy and then you would say you know memorize it's actually important so that you have a dictionary but I wish to proceed on the subject so in those ways

**[1:09:06]** but you have sort of you know new systems we're doing the same kind of thing so I'm actually surprised to hear you say on this particular and the reason in this particular case I was expecting you to say that no that you

**[1:09:15]** have to be disciplined if you decide to learn something is I I expected that you know in the case of the three hours of uh intense learning followed by an intense piano session you were just like really tired at the end and you're like

**[1:09:27]** but no this is something I've had to do this evening so um yes I'm actually kind of surprised to hear you say that yeah yeah no I really enjoy this tension um and I'm probably over stating my I'm probably like

**[1:09:39]** reacting to the Goggins reference right like a bit of an over extreme over correction or something um but this really is how I feel and and I feel this tension all the time like the the histories in educational

**[1:09:51]** psychology that I'm most aligned with are like the most robotic like authoritarian kind of histories and also the ones that are most like kind of unschooling and and montessori-esque like I really have a ton of sympathy for

**[1:10:07]** for elements of both of these directions and there's kind of a weird synthesis of this in my head that I can't I guess fully externalize I guess part of what I'm saying is is aspirational like I mean it certainly is

**[1:10:19]** the case that I do in practice um uh use willpower to make things happen so just as an example of something that's totally contrary to everything I was saying I use a tool called b-minder

**[1:10:31]** which charges me if I don't do certain things right this sounds I don't know if it's you know kind of military but uh it's certainly more authoritarian than this kind of freewheeling butterflies kind of

**[1:10:42]** gesture I was making a moment ago and I use it to make sure that I do my memory practice shouldn't my memory practice be so joyful it's at the center of my research right it should be like the most interesting exciting part of my day

**[1:10:55]** but often it's not uh and so I use this to do it anyway so there's some tension here I think I do want to say you know the reason why I'm willing to endorse this headmaster's view about this taxonomy

**[1:11:07]** has to do with the price I did a bunch of memorization in high school and it was very inefficient and it was very uncertain so it was like it was emotionally difficult because like I wouldn't even feel confident that I had

**[1:11:20]** learned the stuff I didn't know what it was to learn something reliably like to be confident that I'd be able to recall it and it also like it was hugely time consuming because I didn't have techniques or

**[1:11:31]** tools and now you know part of why I respond so favorably to like yeah just learn the taxonomy is that like for me um it's just trivial like yeah sure whatever throw it in the deck you know like it'll it'll consume a total of 15

**[1:11:43]** minutes over the next few weeks and then I'll know it uh you know it just doesn't cost anything so like yeah okay fine um other things in in learning do still have real costs and um actually this is

**[1:12:00]** out uh unschooling and you're attitude towards now just let me ask you I think somebody on Twitter had this question which is your kids as they're growing up how are you how are you structuring their education well okay so to be clear

**[1:12:13]** I don't have kids right hypothetical kids and so yeah so you're going to hear the the foolish response of you know like a a person talking about uh what one would do hypothetically

**[1:12:25]** this is very difficult School of course has many purposes other than instructional right it has a social purpose it has a societal purpose yeah it has a behavioral purpose and it also has like

**[1:12:39]** a pragmatic purpose of basically babysitting those things can be unbundled I think it's pretty interesting to consider that if I actually did have a kid I would probably consider that project pretty thoroughly

**[1:12:48]** I think it's like pretty likely that some kind of um homeschooling situation would occur it probably wouldn't be me being the teacher but it would probably be the people I would

**[1:12:58]** hire I have some resources like I'm not wealthy but I have some resources like that that is uh maybe a difference but during the pandemic I was struck by Brian tobal started a company which is now defunct

**[1:13:12]** and so this is a fun example to bring up but it's called Schoolhouse and the idea was that he noticed that people were getting together in pods right that was the thing we did during the pandemic and in particular they got together in pods

**[1:13:24]** with like their classmates from school maybe five or six kids and some of these pods started hiring Elementary School teachers who were not working because of the pandemic and these Elementary School teachers would like come to the backyard

**[1:13:36]** of one of these people's houses and the five or six kids would get together with the elementary school teacher and like they do stuff all day buying this one teacher's time split five or six ways was actually really very attractable you

**[1:13:48]** know say you want to pay the person 50 an hour maybe that seems reasonable for a teacher it's not that hard to do and actually cost less substantially less than a private school I think Schoolhouse cost Something Like A fifth

**[1:13:59]** or whatever but the cost of an elementary school once you got to older grades you you need maybe Specialists um it's actually not clear if you do my friend Alec Resnick is working on a uh and a very interesting school called

**[1:14:13]** powder house in Somerville Massachusetts that um does something like the model I just described where you have adults who are in more of like a coaching role and they aren't necessarily domain

**[1:14:25]** Specialists but they'll connect people with domain Specialists so anyway I I would explore something like that model I'm sorry this is a little bit vague if you want to ask about this position uh let me ask you you got a 12 at this

**[1:14:37]** this child grows up and it's 12. yeah so at this point you know it's not just like a Forester of taught them arithmetic and reading and everything are there do you proceed and you have to learn your biology you have

**[1:14:51]** to learn chemistry or do you just say what are you interested in are you interested in Roman history oh let's learn about the aqueducts or is there an actual curriculum that proceeds until they get to College yeah this is really

**[1:15:00]** challenging so uh one one of the sort of the the heroes of the reformed School movement is this philosopher named John Dewey and uh he has a lovely book called experience in education sort of written near at the end of his time looking back

**[1:15:15]** on all of his efforts to reform schooling in a kind of unschooling-ish Direction he was never as Extreme as that but broadly Looking For Freedom on the child's part and uh

**[1:15:26]** he makes this wonderful argument that because these kids a 12 year old doesn't have a fully developed prefrontal cortex certainly doesn't have a fully developed

**[1:15:40]** kind of sense of self to let them do whatever it is that their whim commands them to do in any given moment is actually not freedom but rather is is chaining them to whatever that impulse

**[1:15:58]** is it makes them the the subject of these tides of impulse and I think that's a pretty compelling argument it doesn't authorize tyranny um but it also suggests that you know you got to be a little bit skeptical

**[1:16:12]** about the the planning the plans of 12 year olds I guess how skeptical should both be I don't know I think I would probably have stronger opinions on that if I had a 12 year old uh but my instinct as a foolish non-parent

**[1:16:25]** um would be something like a kind of mix I I would be interested in exposing the 12 year olds to lots of topics and possibilities I would be valuable in expressing the consequences of any particular actions like if they just

**[1:16:41]** want to compose music all day we could talk about like well what does that mean what kind of life does that look like I would try to be non-coursive in this as much as is possible and I think to some extent the the

**[1:16:55]** student should um or the child should be allowed to feel the consequences of their choices This is complicated by the fact that like you know again like I'm not wealthy but like

**[1:17:06]** any any child of mine would like have chances I guess you know like if they made some weird choice about a career path when they're 13 and so they didn't get into Harvard or whatever like that would be okay you know like they could

**[1:17:22]** do they could be 24 and finally figured out then or 32 and finally figured out then like it would probably turn out fine and so this this doesn't seem like reliable guidance you should notice I'm feeling

**[1:17:34]** very confused about it yeah no worries yeah okay so one question I have is historically and maybe even to the modern day it seems like improving education has been a very intractable problem and you did reference this

**[1:17:46]** earlier when we were talking about gearing towards the median student versus the whatever um percentile you're working with but I don't know but do you feel like there's been progress even in the percentile

**[1:17:56]** you're gearing your stuff towards and if not what is the explanation for the relative stasis I mean this is something you've talked about we have so many new tools with I.T whereas the well what explains the like the broader sort of uh

**[1:18:08]** stagnation here well the fun answer to your question is actually there's been a ton of progress uh like actually things but things look pretty good one thing is I think the stat is in 1900

**[1:18:19]** um six percent of uh teenagers graduated high school in the US now that doesn't mean that 94 like didn't have you know an education that we would regard as a high school education but it like kind of means that it roughly means

**[1:18:33]** that now I think these people are homeschooled it's also the case that a high school education um meant something lesser than a substantial fraction of high schoolers now study AP courses and complete them

**[1:18:47]** in high school and that's at the high end on the low end illiteracy uh was a very live situation a hundred years ago in in the US and is emphatically not now now it is the case that something like 10 to 15 of adults depending on which

**[1:19:07]** which polls you use are maybe would struggle to perform like simple kinds of number manipulation or reading or writing kind of tasks but um our bar is basically moved it used to be like can you read it all and

**[1:19:23]** these tasks are like maybe a little artificial like they're moving maybe not relevant to their day-to-day and that's actually why they're experiencing this so the the number of people

**[1:19:34]** if the fraction of the population who graduates uh you know at 17 or something knowing a particular amount of stuff has basically moved up monotonically and this is mostly about the bottom like portion of of the the population it used

**[1:19:49]** to be the majority uh were effectively on educating past in age 10 or something other than informally and in their trade and um really the story of the 20th century has has been in part one of Nast education uh where part of why we have a

**[1:20:07]** service economy an I.T economy is that basically all of our population is educated at a particular level if you look at there are these National tests of fourth eighth and 12th grade math and

**[1:20:22]** language proficiency you'll see really like pretty slow movement in in the 75th percentile in like practically none at all in in recent decades but you'll see like absolutely enormous movement in the in the bottom

**[1:20:37]** quartile and so in some sense the story especially the last 20 30 years has been closing what's often called like the performance of the GP Gap where certain groups part of underfunded schools or

**[1:20:51]** um who might have households that are unsupportive or or difficult you know we're just not having anything like the educational attainment of their peers um and that that story has changed one thing I'm curious about is every other

**[1:21:04]** part of the distribution has been moved upwards has the uh has this healing been raised significantly yeah uh well it depends on what we mean by the ceiling because you can go back like hundreds of viewers and the most learned people

**[1:21:18]** around it's just incredible you look back on how many books Thomas Jefferson read yeah there's some story where um Kennedy uh would have had a bunch of Nobel laureates and what was everything commission no valorius in the White

**[1:21:30]** House in 1963 or something and he says this is the greatest collection of genius and insight and wisdom that has been collected into this room ever since the time the Thomas Jefferson dined alone

**[1:21:44]** [Laughter] right I think it's very hard to raise the ceiling so the ceiling has aristocratic tutors uh the ceiling has whatever family Dynamics and uh heritable propensities produce uh

**[1:22:03]** tremendous intellectual greatness early 20th century schools produced Von women right um and it it's certainly not at all clear that they are now producing more of anointins or something like that in fact

**[1:22:17]** um Von women's production seemed to have probably very little to do with uh any kind of mass schooling that we would recognize as far as the very top I think that's that's difficult we're talking about

**[1:22:31]** an institution that was created for I guess the masses I guess that there have always been people who have been using resources outside of those kinds of systems so the mass system doesn't seem to help those people I guess that

**[1:22:45]** doesn't seem surprising by the way on the um on the Von Neiman thing uh okay my math system doesn't help him but what is the production function for Yvonne Neumann yeah so lots of people have studied this I actually am not a student

**[1:22:57]** of uh Von nomen's history I know that many of his peers the 20th century greats got something like aristocratic tutoring or came from uh small Eastern European uh incredible schools that there's stories about these things I

**[1:23:13]** actually don't know them I'm sorry I mean you I'm sure you've heard about that one high school and uh yes yes okay interesting are we getting worse at uh the Von Neumann production or is it just static

**[1:23:26]** I mean so I I don't know so let's see here 's a theory that seems kind of plausible if someone was going to have aristocratic tutors in the late 19th century would they now go to a fancy private school and would that experience

**[1:23:40]** now actually be less good for them I don't know I think it's probably more likely that they'd go to the fancy private school and also still have fancy tutors and then go to a a very exclusive University where they're going to get a

**[1:23:53]** bunch of Highly Hands-On kind of interaction with professors although the reason that might not be the case is the opportunity cost for people who might become teachers or aristocratic tutors is much higher now whereas the kind of

**[1:24:06]** person who would be you know your tutor can now directly be making lots of money on Silicon Valley or that's interesting okay so that would be an argument that maybe um it's not so much about the 20th

**[1:24:19]** century that we've gotten worse about this but more like over history you know maybe Aristotle was a tutor to Alexander the Great and now Aristotle would be like a full Professor take that job that might be so I mean I I think it's it may

**[1:24:34]** be the case that some tutors have been priced out of the market but it's not clear to me that the most expensive tutors actually would would be the best we there's there is a bunch of Empirical

**[1:24:45]** research on tutoring and like one of the questions they ask is like what kind of experience level do the tutors need to have um and it's interestingly how far you get in tutoring efficacy when the tutor

**[1:24:57]** doesn't necessarily know anything so like just having like another warm body there uh actually contributes a very large effect now I mean things get better as you get an expert and and I also I have a kind of healthy skepticism

**[1:25:08]** of these studies like I think part of the the role of having Aristotle as a tutor is communicating a world view it's not something that would show up on a you know a test or something that these studies would be measuring

**[1:25:19]** so having an extremely inspiring individual uh might actually be the important component and inspiring is going to be highly correlated with expensive I think not necessarily I don't know that feels complicated I mean

**[1:25:32]** it spells for you today the material is available what the tutor is bringing is the inspiration and the motivation not the exclusively but one of the large parts of their that's right they're not really responsible for instruction I

**[1:25:44]** mean I'll say also like know lots of people who have postdoc tutors right now you know these people as graduate students uh they're very pleased often to have you know a 60 an hour

**[1:25:58]** say uh tutoring kind of commission and that's a little sad but you know the pool of available postdocs to hires tutors I think is very large now compared to how it would have been 100 years ago the pool being bigger

**[1:26:13]** doesn't mean that the top you know one percent uh are getting more though so I think that's undecided there is a question of like have teachers gotten better at their jobs like over the last 50 years say and like

**[1:26:28]** there are some ways in which maybe they have uh there's been a bunch of projects of trying to disseminate you know certain research results like ways of instruction that are more effective in other ways like it's good to interleave

**[1:26:39]** stuff uh for instance like rather than doing blocked units where it's like okay like we're going to talk about the Civil War and then we're going to talk about women's suffrage you know it's better that those are somewhat far apart but

**[1:26:52]** it's better better to uh kind of weave these things into each other and not just in history but in general so that kind of dissemination has been happening more systematically in the last few decades I I actually am unaware of any

**[1:27:03]** kind of studies or results trying to establish anything about the efficacy of teachers Now versus long ago well I'm sure you've seen the the claim that one of the consequences of the very unfair circumstance of the 20th

**[1:27:17]** century or the mid 20th century was that one of the very few occupations uh an intelligent woman could pursue was teaching and now that other options are available um which is obviously on Neto hugely uh

**[1:27:29]** hugely good you know there's there's there's other competition for those same very intelligent women oh that's interesting I I haven't heard that claim yeah I think I'd have to I'd have to think about it

**[1:27:40]** I guess I I it's not clear to me how much intelligence matters like if you want to think of that as like some some kind of separable quantity or whatever trade is relevant to just that you you just had a

**[1:27:51]** population that was Hostage to either housework or teaching I guess what I'm saying is something like if that were true and there are like a bunch of people who are now you know astrophysicists or something you know

**[1:28:03]** it's not clear to me actually that they would have been teachers like being a good teacher is often about empathy and effective communication and Care uh

**[1:28:15]** it's it's very personal it's very intimate like you need to understand the subject but to teach a 15 year old or something you actually don't need to understand it at a like a postgraduate level necessarily

**[1:28:29]** it's very interesting to see that there's a bunch of studies of kind of the impact of domain knowledge on teaching efficacy I've read some in math I'm sure they exist in all fields and one of the things that comes up is like

**[1:28:41]** if you aren't very familiar or comfortable in math then you will struggle specifically to do like inquiry oriented classes classes that are more about like creative ways of thinking with math or

**[1:28:57]** um open-ended problems as opposed to like here's how to do this algorithm because um to conduct those kinds of classes you have to be able to think on your feet like you pose a difficult question to

**[1:29:07]** which there may not be just one appropriate answer and your students will throw all kinds of stuff at you and you have to be able to take that stuff and integrate it and show how one student's answer relates to another

**[1:29:19]** student's answer and show how those conceptions can be built upon in order to you know produce some useful understanding for what you had in mind anyway this this kind of improvisation requires a mathematical familiarity and

**[1:29:33]** ability but I don't think it requires anything like you know ability yeah yeah but um more than the extraordinary you haven't pulled out of teaching as a consequence yeah I guess I'm just wondering what the correlation

**[1:29:45]** is like if if it's the case that actually effective teaching is mostly about empathy then maybe it's anti-correlated like the people who are going to be good at uh particle physicists uh or actually like they

**[1:29:56]** wouldn't make good teachers anyway interesting Maybe why hasn't hypertext changed how people write more you know so often you know I write a blog post and I actually do wonder how much different it is with the

**[1:30:08]** knowledge that I can add footnotes and I can link to things but you just hope that you know I'm actually kind of a fan of how Wikipedia organizes content it is genuinely surprising how often the best explanation of a subject is just this

**[1:30:19]** like resource that is trying to explain every single subject because I think there's this practice of you don't need to do Exposition in every single topic you can just hide it behind links and things like that anyway so why hasn't uh

**[1:30:31]** hypertext changed writing more online writing at least this is a really good question so the reason why Wikipedia works as well as it does is that encyclopedia entries are already

**[1:30:46]** forced to stand on their own and that was true before hypertext existed in fact encyclopedias were already hypertextish before there was hypertext there are some other interesting kinds of

**[1:31:00]** hypertext that existed pre-computers there was this very interesting book called the syntopicon from Adler that if you want to understand what classical authors had to say about a topic like the father's responsibility to a

**[1:31:17]** daughter you can look that up in the syntopicon and you will get references across Rousseau Through the Bible and so on and so forth and those are kind of hyperlinks I mean they're printed on on dead trees but you were expected to you

**[1:31:30]** know get the books down and look up the appropriate Pages this in topicon wasn't that successful I think it's in part because those Concepts unlike the Wikipedia entries they don't quite stand on their own so cleanly

**[1:31:43]** you kind of need sinews you need linkages and actually I want to make the case that well Wikipedia is an astounding resource I find it rarely to be the best

**[1:31:53]** available introduction or explanation of a topic I find it often to be like a good jumping off point like it'll help me know the right thing to ask about it's good as a reference so hypertext is is a is a very effective navigational

**[1:32:06]** Aid it can help you get to a spot that you're looking for very quickly because it's about automating flipping through pages and so for a reference It's very effective

**[1:32:16]** if what you have is like a table of chemical uh and their properties of chemical compounds in their properties uh hypertext is going to let you navigate that book very effectively

**[1:32:29]** likewise dictionaries have been revolutionized by by hypertext um so navigating around thesaurus is by clicking on links to say like oh shaded a little bit more like that it's like a much better thesaurus so I guess I'm

**[1:32:40]** making the case that like there are certain kinds of text that are more amenable to hypertext because they are more amenable to having the reader dropped in the middle of them encyclopedias are like that dictionaries

**[1:32:51]** are like that most text is not like that and I guess like most concepts are not like that I guess most ideas are embedded in something kind of holistic or richer they require a narrative Arc they're

**[1:33:06]** difficult to excerpt not everything but things that are not so raw and atomically informational so there were all these dreams of hypertext novels for instance and some people wrote them and one of the

**[1:33:20]** problems that a hypertext novel has is actually could be seen in a Choose Your Own Adventure book that existed before there was digital hypertext and that's that the author is forced to write something like a lowest common

**[1:33:31]** denominator Story the page that is the destination of a hyperlink it has to work as the endpoint of all of its uh reference and so it can't establish

**[1:33:45]** any kind of coherent or consistent Arc unless there's a kind of sameness so all of the reference and the more that there's sameness to the reference like the less useful hypertext is so a lot of people have

**[1:33:59]** been disappointed by this conclusion I among them I'll say that I do find hypertext very useful in my own notes not really for reading I actually don't think it makes for a very good reading experience for others

**[1:34:14]** but I haven't being a reader you have a separate web page where you have your working notes right yeah for the Audience by the way it actually is like a very cool UI in the format to explore your thoughts thanks it does an

**[1:34:25]** interesting thing for me as as a writer it lets me build stuff up over time so today I was working on reading this um this very old cognitive psychology paper on the topic of Agilent questions which we discussed earlier the

**[1:34:42]** effects of asking questions while you read not on remembering the information covered in the questions but but actually just on kind of the general effect that it has on on stuff that isn't touched by the questions

**[1:34:52]** I have some notes on the design decisions of the mnemonic medium this Quantum country thing that I was talking about earlier interleaving the interleaving the questions into the text and those notes are kind of partial

**[1:35:06]** uh they evolve over time what was the impact of doing this my my notes about that they've come from interviews with readers they expand when I read a paper like this that's relevant to them

**[1:35:20]** and it means that when I go to design the next system and I'm thinking about the the role of questions in text I'll have sort of a place to look the role of hypertext in this is roughly as a kind of navigational Aid

**[1:35:37]** it's possible to do this without hypertext you just end up with uh like what Luman had you know a giant um something like a dresser but made of card files rather than drawers for uh clothing this actually

**[1:35:51]** goes back nicely to the original conversation we had about why people like Tyler are able to integrate so much information without an explicit note-taking system and in fact I just remembered another person who comes into

**[1:36:02]** my mind immediately when I think about a person like this is a burn Hobart and again you have an example of somebody who is extremely prolific a daily finances letter with there's like a tremendously detailed and insightful

**[1:36:13]** daily Financial newsletter so it's like oh it is like a daily note-taking practice Yeah in substance uh nothing quite accumulates for either of them at least not in the same way right um it's very interesting like they're

**[1:36:25]** they're doing the whole thing over again every day one thing I find kind of interesting about Matt Levine's newsletter is that when he's talking about a topic repeatedly like something that comes up like the the recent bank

**[1:36:36]** collapse or something he will have to explain some concept like uh interest rate risk uh over and over and over again for days uh like every day he has to explain it but every day he explains it Anew and every day

**[1:36:49]** the explanation is like colored a little bit by that day and this is an argument against the kind of note-taking that I do it's an argument for ephemerality for for like recreating the thing uh every

**[1:37:01]** day because it will change and it will become kind of inflected by by what you're thinking about now and your experiences I think it's pretty interesting and I I find myself these

**[1:37:12]** days doing kind of Nicks like like I have you know kind of like a journal that's about today and I'll do a bunch of writing and often I'm recapitulating stuff I've written before and I have these other things that are trying to

**[1:37:24]** be more durable be like a a youthful reference that can stand outside of time uh the combination feels useful I don't yet have like a clear model of like when one is better than the other well actually an interesting way to tighten

**[1:37:39]** what you just said with uh the hypertext is um so Burns newsletter is it doesn't give that much context on you know often you'll find yourself lost about what you

**[1:37:51]** know what is the concept being talked about here if you're not familiar with the um the topic and in fact I asked him at some point uh have you considered doing narrations of your blog post like Scott

**[1:38:02]** Alexander has somebody who has a podcast where they narrate his blog posts and he said I don't think it would work out as well for mine because I heavily rely on the old blogger spheres Norms around uh hypertext where you can add jokes and

**[1:38:17]** sarcasm based on um one example of this is he was talking he had to write up about SPF and his collapse and he said you know he had a bunch of links like if you want to learn more about margin calls read this you want to learn

**[1:38:29]** more about this and he goes and if you want to learn more about the psychology of utilitarian best read this and just a link to the Amazon page of Crime and Punishment so just that kind of stuff is harder to

**[1:38:39]** do yeah you're right so he's leaning more on his past explanations which is interesting because he can't update them like that format of writing a newsletter and then linking to past newsletters or as you say the um this is sort of a

**[1:38:51]** former blogosphere thing to do you have a series of six words and like each word is a link to a previous post I've certainly written stuff like that it's kind of funny I mean it's approximating the durable note thing I

**[1:39:03]** was writing about but without the ability to revise it over time and maybe for many topics like you don't need that ability it's certainly the case that well I wonder now at what fraction of of

**[1:39:15]** my notes are basically in the state they were the the when I did my first major revision of them it's probably at least a third it might be more than half what personal notes have you published I don't know uh you know by word count

**[1:39:30]** by by note so like for instance my journal notes are not published and there's one of those every day so there's a lot of them so if we're looking by note we're excluding all of those I also have like a note about all

**[1:39:41]** of the people in my life uh and the those are for the most part not public right unless they're public individuals you know and so there's a lot of notes that are not public but they're mostly not

**[1:39:54]** um durable they're like they wouldn't be all that meaningful to others the journals might be but they're also intimate or are they written in a way that would be intelligible to if you were to give that to somebody else it

**[1:40:05]** depends um but usually actually my journals are like complete sentences complete paragraphs usually um sometimes bullets sometimes kind of veering and breaking and changing to new

**[1:40:18]** subjects suddenly but they tend to be filled with links to the things that I'm talking about in part because I'm trying to accumulate context in those things how come there and why not just shorthand and um it's partially because

**[1:40:33]** past me is another person it's kind of a cliche you know but like I am routinely looking at journal entries from a year ago yeah this is partially like you could view that as a failure of this notewriting system like maybe in some

**[1:40:46]** ideal sense I shouldn't be looking at these journal entries because if something's important and it's going to be something I refer to a year later it should be in some durable Evergreen note I don't know like you don't you don't

**[1:40:59]** always want to do that it feels like um feels like prepping maybe there's an amount of prepping that's good we live in California and like maybe everybody should have like an earthquake kit right like maybe that's good but maybe you

**[1:41:11]** don't need to like hoard uh 300 cans of beans um so there's like an amount of prepping that feels like a reasonable amount to do and there's a map that feels kind of dutiful and unpleasant as a researcher

**[1:41:23]** who is in the sort of Silicon Valley circles what what is your opinion on the startup advice uh you know do things fast fail fast get to users immediately with an MVP as as somebody who is making products but is

**[1:41:37]** also in a sort of um in a different mode than a typical startup kind of making products how do you think about advice like that I have complicated feelings about this I need different advice on different days and of course different

**[1:41:48]** people need different advice on different days but when I was getting into this kind of work what that kind of advice led me to do practically speaking is to not think all that deeply about the ideas I was exploring and to look to

**[1:42:04]** basically like an idea would come up and I'd think like oh I could try that and then I would I would try that and then I'd learn something and then I'd repeat and there wasn't this sense of building a theory of like what the problem is and

**[1:42:19]** what it would mean to solve it instead it was just a theory of action like a theory of action as opposed to a theory of changes if you imagine like you're at some point uh your your current position and eventually you want

**[1:42:32]** to get to Some Coal State a theory of action is you look around you and you say like well what can I do what can I build what do I see is possible and a theory of change is to look at the endpoint to try to work

**[1:42:42]** backwards now the metaphor is imperfect because in research you actually usually don't exactly know what the end point is uh and you certainly don't know how to work backwards but I guess what I'm saying is that following that advice

**[1:42:54]** historically often has led me to try things that were straightforward I think the most powerful design work has ideas in it

**[1:43:09]** what makes a non-linear text editor that is like the text editors that we all know and love so powerful is this observation that

**[1:43:22]** writing is a non-linear process but writing with a pen linearizes it and many many other observations like that and on the nature of what it means to have a thinking environment is is how we got that

**[1:43:40]** particular interface likewise the way that we got powerful programming environments insofar as we have them is by people thinking very hard about what it means to specify a system

**[1:43:52]** and coming up with New Primitives that Express those ideas I think the most powerful interfaces are often the expression of new ideas or New Primitives that capture new ways of doing new kinds

**[1:44:09]** of objects that can be manipulated in Photoshop for instance you can manipulate a photo by means of a construct called a layer this is a very strange idea it has some precedent in dark rooms where you could

**[1:44:23]** potentially have kind of like sheets of film I don't mean like the um the negatives sheets of like gels that you could potentially put over the the lights to affect the exposure and to

**[1:44:37]** make there be you know more exposure here and less there but in Photoshop they're they're non-destructive and they're continuously manipulatable and the layers like it's a new primitive that that is introduced

**[1:44:49]** into the the activity of of photo editing and it utterly changed what you could do in photo editing so I I guess what I'm saying in a very long-winded and Confused way is that I

**[1:45:03]** think it's difficult to have ideas by means of building an MVP very rapidly now if you have an idea that you think is interesting uh it is good to test it rapidly

**[1:45:16]** and so part of why I'm confused is in my response here is that it's good advice once you have something worth testing it's just that for me adopting that mindset and I've lived in it for so long that it's very ingrained in me it makes

**[1:45:33]** me not sit in Stillness and in confusion and in contemplation with the ideas long enough for them to be good I mean very concretely so so Michael Nielsen and I made this this Quantum country thing

**[1:45:46]** when I was trying to think about what to do next the the most obvious or natural idea was like well what if we just try that with lots of other things and that idea occurred to me and the pandemic had just struck so I was feeling a little uh

**[1:45:59]** timid I guess creatively or emotionally I wanted something that felt kind of safe and I knew that I could do that like okay I can build a platform that like generalizes this thing that we did for this textbook so I did

**[1:46:11]** and I did it relatively quickly I did it in a few months and that wasn't the right thing to do it wasn't really the right question to be asking the idea wasn't

**[1:46:21]** that strong it wasn't the right way to test it like building this highly General version of it I would have been better building more one-offs rather than like a self-serve thing that anyone could use

**[1:46:31]** and this comes down to like the difference in AIM like I'm not trying to build some kind of scalable thing for the world at this moment I'm trying to build the idea the Prototype is an expression of the

**[1:46:42]** idea and once it arrives at a good place then maybe there can be some scalable solution um but it's not necessarily at that place and until it's at that place

**[1:46:53]** there's like a lot of thinking and sketching that goes along with the building and prototyping I think part of my confusion here is that often I still need to hear this advice like often I will just tie myself in knots in theory

**[1:47:03]** land and like what I really need to do is to have a friend sit me down and say like is there a piece of this that you can carve off and like build next week and so you're hearing a lot of tension interesting and then so what was the

**[1:47:17]** consequence of shipping orbit out uh I guess before it felt right at this scale I learned some things it was fine like it taught me a lot about where that particular format succeeds and fails in other venues it was just not a very

**[1:47:34]** effective way to find those things out I built this like very general it was an MVP in the sense that it has very few features and it's very simple but it was highly General I mean it's like it's a deployed thing that has

**[1:47:48]** infrastructure it has accounts it has like all this stuff that you do when you're building like a real thing and that's very different from like well let me like work with this one author and like see if I can make it work with this

**[1:47:59]** one other book that's very different from Quantum country to form like a specific question or a specific theory about like well it worked for this text like what's the next kind of text that would be good to test with

**[1:48:10]** uh and then to do that I I could potentially do it well I certainly could have done it much more rapidly why do you think of this idea of tools of thought uh has nerd sniped so many people in Silicon Valley

**[1:48:24]** well it contains this message for technologists that they can potentially be very powerful and that's always tantalizing for people I guess I think it also feels very actionable for people in a way that's actually super

**[1:48:36]** misleading I mean so I meet tons and tons of people who tell me that they're interested in tools for thought and 95 plus percent of them are engineers and the problem with this is that like building an interesting tool for thought

**[1:48:51]** is basically entirely a design problem and their design ideas are usually not very good or troubled in a variety of ways and yet they can make a thing [Music] they can make a thing that solves a

**[1:49:06]** problem maybe for them in their lives and that feels very tantalizing or encouraging it feels like uh something they get their hands around that I think I think we in Silicon Valley are very very interested in thought we are like a

**[1:49:20]** stinky people and people are very interested and engaged also with anything they could potentially expand our capacity there and so that too is tantalizing like what if I could think better

**[1:49:31]** it's also tantalizing because it's uh it's meta so there's all these cliches about people you know tinkering with their dot files endlessly or you know tinkering with their blog website uh which has two posts on it but they have

**[1:49:44]** to rewrite it because you know they want to do something else and now the new one will have three posts on it before they rewrite it again Tools For Thought also scratch that itch it's work about the work

**[1:49:55]** this sounds very cynical by the way I don't I don't mean for it to be I'm just trying to earnestly answer the question but um here's a more optimistic and generous response

**[1:50:06]** I think many of us got into Computing because computers portray a sense of personal empowerment and possibility we maybe remember growing up and you

**[1:50:19]** know being locked in our bedrooms at midnight or whatever like fooling around and we have this very powerful tool at our disposal and it's opening up these worlds for us and I think for many people here that it was like a formative

**[1:50:32]** part of their personal development and so anybody pointing it at and saying we can we can do more stuff like that uh is going to be pretty compelling I think okay this was uh interesting question

**[1:50:46]** from Matt Clancy on Twitter what are the characteristics of a good crowdfunded research project one of the maybe unfortunate things that I've learned in my crowdfunding experience is that there are some

**[1:51:02]** dynamics that seem hard to change so one of them is at churn rate uh you know like any subscription kind of Revenue business model I guess that's what I have you lose subscribers every month in my case it's about two percent and it's

**[1:51:17]** not that large but it does mean that I need a certain number of new subscribers all the time and one thing I've learned that's kind of interesting is that the trend rate is surprisingly insensitive to anything that I do

**[1:51:28]** you know I've experimented with a variety of things and it really hasn't meaningfully changed the churn rate what does change things is getting more people into the top of the funnel in other words marketing and there are some

**[1:51:40]** things that have maybe affected like the fraction of those people in the top of the funnel who convert or whatever I really hate this way of thinking about it um in summary the thing that I've

**[1:51:51]** discovered that's that's kind of sad is that I end up having to think about this a little bit and in particular I realize that this project only even slightly works the one that I'm doing for crowdfunding because it's

**[1:52:03]** understandable to others and it's interesting to others and it's already in a place where you know there's some results that maybe look kind of promising or people are like oh more like that but it's very

**[1:52:14]** easy to imagine other projects that like are not broadly applicable you know if I were doing Marine geology stuff uh you know I probably wouldn't have a big crowd of internet people not nearly as large anyway we're excited so that's one

**[1:52:30]** property this work is very general it applies to many many people it applies to people who have disposable income so if I were doing a research project on I don't know like writing practices of disadvantaged artists like I don't know

**[1:52:44]** like I think I think my audience might not have as much disposable income I have already made some progress I think that's probably important unfortunately um so it's probably very difficult to use crowdfunding in the very early days

**[1:52:55]** of a research project um I've already sort of chosen a research agenda or Direction like and I can kind of express it so I think this says that like crowdfunding applies probably

**[1:53:07]** after the first few stages of research have been completed there's probably something like the standard Grant advice where like at some point here I'm going to be using this crowdfunding like to figure out the next thing and I won't be

**[1:53:19]** able to explain it to anybody um there certainly are you know seedlings like that but you have to like have something in Flight I probably need to be able to say something about my progress with some kind of regularity so

**[1:53:31]** for instance um my wife is working on this study of biological markers of age in association with a delirium and traumatic brain injury and to do this she is basically signing up patients who show up to the hospital who have

**[1:53:50]** traumatic brain injury and once they agree to participate in the study taking you know various like blood samples and things like that from them and recruiting enough patients to get like the significance that she requires

**[1:54:03]** will take like you know two years or something like this she can report a little bit of intermediate stuff but like certainly not a monthly update or something like that right yeah weird patreon post yeah I mean I can't quite

**[1:54:17]** report monthly updates either but but I think like there's there's a Cadence that's necessary why bother with it at all I'm sure there's many uh what wealthy individuals who would be happy to single-handedly

**[1:54:27]** fund your research so it shows uh crowdfunding well those wealthy individuals are are very welcome to to reach out and offer to do so um you know I I I will say I've been I've been fortunate to have many uh High

**[1:54:41]** net worth individuals uh sponsors but I guess each of them is is you know providing it I guess on my patreon a sponsorship is a hundred dollars a month so like that is you know what I what I get from these people and you know I'm

**[1:54:55]** certainly not getting um you know wild offers for for more I think you're using the wrong tool going the distribution of your given the wealth distribution of your maybe there's a couple ways to interpret your

**[1:55:07]** question one question is like why crowdfund when I could appeal to high net worth individuals and another version is like why card run at all like as opposed to raising grants or talking to philanthropies or whatever are you

**[1:55:18]** mostly focused on the first of those um yes kind of be honest it's it's because it has worked the history of of the crowdfunding of this project is like many things in my life the result of

**[1:55:30]** goading from Michael Nielsen uh early on when we were working on this Quantum country project he suggested we set this up and I kind of hemmed in hard and I said like yeah you know it's going to be a distraction like we don't we don't

**[1:55:42]** really need this right now like let's let's deal with it later when we have something to show and he's like no no like let's just get it started you know it's gonna be a long time to get enough subscribers and so on

**[1:55:50]** um and it turned out he was right uh you know the the process of crowdfunding a project is it takes like maybe a couple of years at least in my experience to you know build up a subscriber base

**[1:56:01]** and starting earlier was better and if that hadn't worked or if we hadn't started early I think I probably would have just reached out and asked for individual help and I probably will if it fails on

**[1:56:13]** me I'll say also like when there have been specific projects that I've wanted to do that require say hiring people I I have reached out to high net worth friends and they've

**[1:56:25]** helped but you know and kind of like below five figure four-figure kind of range and that's great and I'm very grateful so I guess the answer may be a mix one of the big limitations to the crowdfunding

**[1:56:39]** thing is it seems pretty clear to me it can't sustain a team or institution or anything like that it could barely sustain me like my I earned somewhere between like a grad student and a junior

**[1:56:50]** faculty member you know and like that's kind of okay I guess and there's like a variety of reasons why that's okay for me that are like pretty particular to my circumstance but you know it certainly wouldn't be okay for

**[1:57:02]** everybody and uh even for me it doesn't allow me to support others right and it's even more I guess striking because in terms of the success of what what what a public intellectual is basically in some sense you're like a public

**[1:57:17]** researcher in the sense of like summary researchers public or you publish your research in a public-facing way even in a context someone if you're like pretty well known especially amongst the you know the kind of audience would be happy

**[1:57:28]** to fund this kind of thing if uh if the LeBron James of you know independent public research is like between a grad student and uh uh yeah it's a it's not a great sign in general for that I think it's worth considering that I'm also

**[1:57:40]** maybe not very good at this like I mean so first off like I'm not that successful as a researcher like I guess I kind of object to the LeBron James characterization it's true that I'm maybe the most successful crowdfunded

**[1:57:51]** researcher from Tech stuff and that's kind of weird weird but like the last couple of years you know I've like figured some stuff out but I guess I wouldn't say I've had any like spectacular hit kind of publication kind

**[1:58:01]** of things one thing that is true of this is that you know when I have big Publications I get a lot of new subscribers um so I think like there is some kind of Market Force that could be higher if I

**[1:58:14]** were you know like uh having a more spectacular success or whatever with my research I think it's also true that um is pretty systematically avoid marketing it that's kind of a self-protection thing like

**[1:58:25]** I am really worried about the corrosive influence of audience and marketing on inquiry honest inquiry um it is very easy very very easy to distort my work it's all it's almost a default

**[1:58:45]** to try to make it be something that people would be more likely to like rather than the thing that I actually want to investigate or to do the boring simple version of it rather than the

**[1:58:57]** interesting deep version so that I can publish more stuff more often like one thing that I've chosen not to do that is a choice that's definitely cost me financially is to publish what academics would call

**[1:59:09]** like minimum viable units of paper or something like that so that they have a pithier phrase than that minimum viable papers uh it's it's very common to take you know any new marginal Insight that is kind of above a particular bar and

**[1:59:25]** publish that it's a little thing and I I just haven't done that like you know I've written little informal letters to my patrons like hey I figured this thing out this month and like if I were an academic I I probably would have

**[1:59:35]** published that as a paper and if I were a marketing oriented crowdfunded researcher I probably would have like done some glossy thing and like promoted it and whatever like look at this thing I figured out but like actually I just

**[1:59:47]** don't think it's that big a deal and I'd rather get onto the next thing I have that choice uh I guess of waiting to publish but and that's not really what I'm worried about really what I'm worried about is

**[1:59:58]** like marketing man marketing it um it makes it so hard to be honest with oneself at least in my experience not only to be honest as I said with like what I think is interesting and what I think is important but even to be honest

**[2:00:12]** about the results like every paper is in some sense a little marketing piece trying to make the case that it's significant that its results are really exciting or really important and that is really corrosive to Discovery I mean

**[2:00:25]** it's true that you need to you need a a really strong emotional connection to the work I think in order to do good work and part of that emotional connection comes from a sense of excitement of

**[2:00:39]** maybe being hot on the tail of something really good but there's a temptation to kind of portray what you found in the best possible light and to kind of downplay its limitations and to take up space and

**[2:00:53]** to totalize and all of this is just um I think I think it's just death for Discovery it is interesting to hear that from somebody who inadvertently and without intentionally trying to do so

**[2:01:04]** has done a good job of spreading your material um you know I've known about you for a long time so but I do wonder if there's an element of I think if you get to a certain level of quality after that

**[2:01:15]** trying to Market your stuff not only doesn't help but it probably hurts you if you can try to think of somebody like I don't know Goran trying to like post YouTube shorts of his blog post or something like that it would just be

**[2:01:27]** like what are you doing man right where's it it's just so good that he doesn't need to promote it corn is an interesting example because there's a simpler failure mode and that's that I still routinely run into people who will

**[2:01:37]** tell me like oh I've really liked your work for a while I didn't know you had a patreon and that's kind of like a simple failure of a certain kind of marketing on my part and I think guern actually has this even worse uh I adore guern

**[2:01:53]** like I have learned so much from him and uh it is the case like you can go to his patreon page and he actually makes public his Revenue he makes on patreon like a tiny fraction of what I do uh I think this is inappropriate like corn is

**[2:02:08]** a much more impactful researcher than I am and he has a much bigger audience than I do so the fact that they aren't converting into patrons I think is mostly a matter of like the way that he talks about it and the way that he

**[2:02:21]** presents it and like it's not that he needs to Market more people to his web page I expect he has plenty of traffic and plenty large audience I think it's much larger than mine um I think it's more just like there are

**[2:02:33]** a bunch of variables about the way that you talk about this membership offering uh and none of us really want to think about them and I've ended up at a slightly more effective part of the space but I'm pretty sure that there's

**[2:02:45]** like much more effective ways to do whatever it is I'm doing yeah this is a really interesting problem because I have a sub stack where if people choose they can help uh contribute to the podcast and while broadened enough

**[2:02:58]** Revenue to help pay for certain episodes and traveling in comparison to now that I'm going to be doing ads in comparison to I'll be making in that it's like a small fraction and which is some people might say it's

**[2:03:12]** unfortunate that you have to do ads and I've spoke I'm maybe listeners will just be fighting off for the first time that they there was an option on sub stack but also you don't want to be in the position where you're asking listeners

**[2:03:23]** for money every episode right yeah I hate asking people for right I think this is a common issue for Creative people I hate it I really hate it um I probably need to get over this I do want to make one point though

**[2:03:35]** um I had much more success with my patreon when I recast it as like oh please like support me like subscribe to support my work like like the thing you were describing two something that I guess feels slightly more like what know

**[2:03:50]** an offering like become a member and like when you become a member like these things will happen where like these things are not terribly substantial necessarily but I guess what I'm saying is like there's a difference between a

**[2:04:02]** tip jar and a membership in people's minds and like becoming a member means something and if you could offer something small that feels membership-ish uh you might get very different results and guern uh has the

**[2:04:16]** kind of tip jar Vibe uh and I these days have kind of like a member Vibe and my instinct is that if you were to move to like a you know become like a member of guerns lab kind of thing he would have better results well he has a thing on

**[2:04:31]** patreon where it's like if you donate five bucks or eight bucks he will read an entire book and review it yeah this is crazy I don't know if anybody's ever taken him up on this yeah but I mean that's like valuing his time at a dollar

**[2:04:43]** right now yeah I I don't I don't quite understand this I mean I think it's all it's awesome like you'd probably have an easier to asking for subscriptions if you had a larger audience first like yeah you can

**[2:04:57]** build the audience for free and and then kind of uh have some bonus offering or something that that's behind a wall maybe I feel very conflicted about this actually maybe you can help me think about it well I just I have all these

**[2:05:08]** Patron essays um it's like where most of my writing is these days because I'm kind of waiting until I can collect enough things for the next big public piece I have a couple of like big public pieces in

**[2:05:20]** various stages of flight and uh so anyway I mean I'm writing a lot for patrons and I think probably much of my audience or people out there like don't even know that's there so like one challenge of member-only

**[2:05:34]** content is even making clear that it's there to others and um often people will try to achieve this by like tweeting about or sending newsletters out about this subscriber only content

**[2:05:46]** and I just can't bring myself to do it it feels terrible to say like oh here's a link but you can't view it uh yeah I can't I can't do it I don't know how you think about this or if you think about like subscriber only material for lunar

**[2:05:58]** Society I was actually just about to mention this to you which was you know I I'm a patron and I got a chance to read all your things only featured only essays and they're great and I'll get you thinking while I was reading them

**[2:06:11]** it's like really unfortunate that a person might not know they exist or if they're not familiar enough with their work to go ahead and sign up right just like behind the patreon so it's a shame that the way to fund public work is or

**[2:06:25]** one of the ways to find public workers to make some of that work less public I think it would be yeah there's some way to make it I think there are better ways to do this uh I I think there were like design Solutions uh so for instance like

**[2:06:38]** if it were the case that my work was kind of mostly all in one place rather than in these separate places and the the subset of the work that's public was kind of visually and structurally adjacent to the subset of the work

**[2:06:50]** that's private um it would be clear that there's like this additional stuff that's available and perhaps you can see the first bit of it in a sub stack has this kind of stuff as to get some sense of what it is that

**[2:07:00]** you'd be seeing I I just I've invested like zero effort into uh figuring out the inappropriate presentation of this stuff right and then also another thing to consider is to the extent that the this may not be the largest thing you

**[2:07:12]** hear about but it is a factor is that a big part of the impact of at least your writing work well one of the things in that equation is how many people will actually consume it yeah and the expected value on that is dominated by

**[2:07:25]** the probability goes viral sure and it just can't go viral if it's on like for example I think your recent post on you had this really insightful post based on your experience in Industry at Apple about the possibilities of a Vision Pro

**[2:07:38]** and in what ways it's living up to a knot and I think like that would have just oh thanks I mean I I did make it public I put it on Twitter and it was front page at Hacker News you're right and like usually I don't

**[2:07:52]** want this stuff to go viral like it's in medius race it's uh I think that the primary value that most of it has for people is kind of opening up a window into a particular very unusual kind of creative work that they don't normally

**[2:08:05]** get to see the behind the scenes of and most of it is kind of context Laden it's it's not really freestanding and I don't really want to ride it uh as if it could be freestanding I've occasionally had the experience of one of these kinds of

**[2:08:21]** things getting widely distributed and then getting all these comments of people like just like being kind of angrily confused about what I'm even talking about that's kind of discouraging I get I

**[2:08:31]** guess all of this to say when I want to write something for broad public consumption I write something for public consumption you know okay I've got some questions for Twitter from Twitter okay they bring it on Twitter this is

**[2:08:41]** actually another question from Matt Clancy are there other examples of beneficial knowledge work practices that perhaps mostly work because they are former space repetition practice with the participants don't realize it yeah I

**[2:08:53]** mean I think this is like uh this is embedded in our in our in our working world uh so for a researcher when you need to write papers regularly and you're writing those background sections and

**[2:09:07]** you're you're repeatedly explaining uh the the history of a particular line of research and citing the appropriate sources like that is a kind of space repetition when you have students and you're mentoring them in conversation

**[2:09:19]** about like oh in this kind of situation you really need to remember to do X um that is a kind of space repetition and all this stuff is is kind of accidental the doctors have grand rounds when you know even when they're they're

**[2:09:32]** not seeing patients regularly they're still exposed to uh to other patients and there's often a structure in this where like while the um the patient is being presented you're supposed to be kind of trying to think

**[2:09:44]** like you know what would I think to ask like what would my differential be uh you know before you hear it there's like covert retrieval happening so I think it's like it's everywhere in our world

**[2:09:54]** um and it's spaced and it's it's repeated the thing that differentiates the the kind of formal practice that that I've been exploring I think is mostly it focuses on material that you wouldn't otherwise normally have

**[2:10:07]** repeated either because you're you're too early with it to have a consistent practice or because it's just not firmly tethered enough in anything in your life this is a question from Ian vanagas what is the optimal amount of effort

**[2:10:21]** that should go into a personal website and I think you might have noticed the uh the amount of CSS that exists on two shot dot org or yeah which is very beautiful but uh I don't like it oh no this is what everybody says about their

**[2:10:36]** website right you know it's three years old that means I want to redesign it but I will not allow myself because it feels like a distraction yeah what's the right amount of effort you know I mean there's no General answer to that question of

**[2:10:46]** course that's going to be my answer but what can I say about it what's the job of the website what's it trying to do I think many especially Engineers do themselves a disservice by fretting over their websites unnecessarily building

**[2:11:00]** vast technical infrastructure when really what they want is like a place to post to markdown files um and they're better off just like getting a ghost installation uh and going to

**[2:11:12]** I think the main thing to think about is like what is it that you want to put out in the world what what is the ideal form of that thing and to try to find some way of organizing and expressing that we have these common patterns like a

**[2:11:25]** blog or um a portfolio and often people end up kind of forcing themselves into these patterns and people will end up using blogging software to make something that's kind of durable and I think like very interesting

**[2:11:40]** personal websites often come from people who are thinking about that question and kind of the shape of the thing that they want to put out into the world and making something that speaks to it often once you understand the shape

**[2:11:52]** making the thing is is not that effortful my website was not uh not an enormous project for me probably should have been a slightly larger one given that my income depends on people coming through it the working notes with the I

**[2:12:06]** mean if that was the weekend really yeah I feel kind of bad about it because uh it's made its way into tons of commercial projects now and people are like ah this is like this is the way to present Network notes and like there's

**[2:12:17]** actually I think it's not very good in a variety of ways I you know I spent like a couple days on it wow because I I thought this is where the question was alluding to is you must have spend months on this nope wow

**[2:12:27]** huh I mean it is a little bit of like the the yeah the thing about the mechanic like you know hitting one thing and kind of knowing the thing like okay I have designed intuitions that led me in a

**[2:12:37]** particular direction but there's lots of things I don't like about it I just haven't allowed myself to spend any more time on it because I just don't think it's important enough I have a question about actually your time at Apple before

**[2:12:47]** I asked the final Twitter question is we you know like like everybody have an iPhone and from the outside there just must be so many different trade-offs and constraints when a thing like this is being designed you know what is the

**[2:13:00]** supply of certain components and the cost what do different consumers want what um what features is the r d team ready to put forward uh and then at your time at Apple you were like responsible for a

**[2:13:10]** lot of these um Cornerstone Design uh features what like how is all that information integrated where a guy is like all right taking all these constraints into account this is the design like how does that happen I mean

**[2:13:22]** one thing that's very interesting is that it's very compartmentalized and like basically none of what you just said was relevant to me like it was all pre-specified so like the thing at Apple is is like

**[2:13:32]** you have a little domain that's like your own and like the boundaries of that domain are determined by like everybody others everybody else is little domain and so like there's a person who's responsible for thermals actually

**[2:13:43]** there's a team that's responsible for thermals and they kind of figure out like you know okay like how can I guess like what is our thermal budget like what how much can we have the CPU on uh during what kinds of working

**[2:13:56]** situations and I basically can't argue with that like those are just my constraints but but aren't those constraints informed by uh differential problems it is iterative so we'll run into stuff where like oh there's a thing

**[2:14:09]** we really want to do we can't pull it off because like it drains power too much right so hey Siri is an interesting example to be able to activate a voice command at any time without interacting with the device is great and people

**[2:14:22]** prototype that just like having a thing listening in the background and like watching for it but that requires having the the main CPU on all the time like processing audio buffers and like you simply can't do that it drains the

**[2:14:35]** battery and so that attempt uh led to eventually having this dedicated co-processor that runs at a lower power and it's very limited and restricted and it can be on when the main CPU is not on and it can listen for that sound so is

**[2:14:52]** there a person whose job it is to take all things into account and like I decided given everyone giving the memos from everybody that thermals you guys need to work on this you know you guys work on this

**[2:15:03]** um not exactly it's a little more push and pull so like a given team usually some of their priorities will be internally determined like The Thermals team has its hobby horses and it knows what it thinks is important and some of

**[2:15:18]** them will be externally determined there is an executive team that makes ultimate decisions about like you know the main priorities for next year's devices or whatever like ah next year we're we're going to do this like face ID thing to

**[2:15:29]** unlock the phone and we're not gonna have a home button like okay as soon as you like if you want to not have the home button and you want to have the screen go to edge to edge like this has all of these impacts like top to bottom

**[2:15:39]** on the device so that decision creates like lots of necessary work for lots of teams but some stuff is kind of handled at a I guess a more local level so for instance um

**[2:15:51]** more locally to the iOS team rather than at a top level executive team the director of iOS apps might decide like we have this problem that because the apps were built at the same time as the system Frameworks we end up building

**[2:16:09]** our apps using this like weird Frankenstein like partially internal framework partially the public one that our developers use and the internal one is always like a little bit different and like it's not always maintained

**[2:16:21]** reliably and so we have all these problems about the skew between the two so like a big priority for us is going to be to like you know rewrite all the pieces of our apps to only use the public bits and like you know so that

**[2:16:32]** they could be distributed on the App Store and that's kind of like a more local decision what I find really interesting about this is that it's possible for a two trillion dollar company to integrate all

**[2:16:43]** this information to ins to have some a cohesive hierarchy where so many different products so many different trade-offs are being made does that make you think that over time these very well-functioning Tech firms will

**[2:16:57]** get bigger and bigger that they can actually handle the cost of having this much overhead let me first just respond to this observation about the enormity of the company and then maybe we'll talk about

**[2:17:06]** the other firms I think the reason Apple's able to do this is because of the way that they delegate so while there is a very strong command and

**[2:17:15]** control structure and for important decisions um that they really are made by a small group of people at the top the individual leaders in the various areas at all levels of the hierarchy

**[2:17:29]** have an enormous amount of latitude and that's the only way that any of this can work so individual people are given very very strong responsibility and Authority within domains to make decisions

**[2:17:41]** and that's how you can have all of these these disparate products like Craig federiguez head of software at Apple what does that mean how can you be ahead like they have how many platforms do they have you know iOS iPad OS watch OS

**[2:17:54]** Vision OS Mac OS also there's like an operating system running in a bunch of the cables like on little chips in the cables right and like oh that is under correct what does that mean you know like in practice what it means is there

**[2:18:05]** is a set of software concerns that he's actually super concerned with and he's thinking about day to day like when I was at Apple I had Craig federici in my office like talking about gesture recognizer heuristics with me because

**[2:18:17]** like that was something that was hyper Salient to him at the same time he was basically completely ignoring you know 95 of software related decisions and he just fully delegated those things to others there's a really interesting

**[2:18:31]** Harvard Business Review piece from a few years back about Apple's management structure and about how they have a couple of different concentric rings of kinds of responsibility for any given leader there will be I don't remember

**[2:18:45]** exactly the breakdown you know call it five percent of things that you're responsible for that you have your hands on at all times and you were like directly manipulating controlling and then there's you know a ring outside of

**[2:18:56]** that that's a little bit bigger those are the things that you're keeping on eye on right so like they are Salient to you you're getting reports on them you were checking in on them you were thinking about them you're coming up

**[2:19:05]** with ideas and sending them down the chain but you're not directly controlling them and then there's a bunch of stuff that you've figured out how to delegate and you want to hear if there's problems

**[2:19:13]** um and they talk about how that structure's evolved um over time it's been now eight years since I've been at Apple and so I'm sure it's

**[2:19:23]** practically unrecognizable to me this is a question from basil Halperin on Twitter is the lack of space repetition adoption a market failure or is a lack of adoption efficient I think it's probably mostly efficient so in places

**[2:19:38]** where space repetition as it stands without substantial like novel cultural knowledge that's difficult to transmit and isolate where all of that is valuable we see a

**[2:19:51]** lot of space repetition usage so among medical students who are highly motivated have lots of reason to study and the material is shaped in a way that's highly amenable to space repetition usage there's tons of space

**[2:20:01]** repetition usage in fact the the med student Anki subreddit is like bigger than the Anki likewise among language Learners um space repetition in various forms is extremely common Duolingo has space

**[2:20:17]** and space repetition is kind of naturally present in the process of of immersion learning in fact modern space repetition tools between the Lightner box and Wozniak super memo they were both originally

**[2:20:30]** motivated by language learning so in language learning there's like a substantial market for space repetition and it could probably be used in a variety of more creative ways for instance uh

**[2:20:41]** Russell Simmons has pointed out to me that studying individual vocabulary words on flash cards often misses kind of Integrative opportunities which you really want is to kind of study lots of sentences or something like that or

**[2:20:53]** possibly to build up towards that and Duolingo does something kind of like that and people in space repetition for language learning subreddits mostly don't some of them do it's kind of complicated

**[2:21:03]** so there's edges at the market right where you need early adopters to kind of try things that have rough edges and the early adopters sometimes they get cut and they bleed a little bit and so that's why people aren't rushing into it

**[2:21:15]** as to why space repetition isn't widely used for instance to like learn quantum physics I think it's basically correctly priced you know I can use space repetition to learn quantum physics a bit faster it doesn't make it a fair

**[2:21:28]** complete or anything like that it's not like learning anatomy where basically if you study the deck you'll be done you need some more stuff and I'm working on some of that stuff and also you need like an incredible amount of very

**[2:21:40]** unusual knowledge that's largely tacit at the moment in order to use it in that way that's part of what motivated recording this other video is is to kind of show some of that in action so the fact that the market isn't acting on

**[2:21:52]** this thing that it kind of can't really act on seems pretty appropriate that's I think that's a good place to that to tie off that other collaboration and uh on this uh this project this was really interesting thank you so much this is

**[2:22:06]** many hours of just insights and um lots of food for thought wonderful thank you things are coming on hey everybody I hope you enjoyed that episode as always the most helpful thing you can

**[2:22:18]** do is just share the podcast send it to people you think might enjoy it put it in Twitter your group chats Etc just splits the world appreciate your listening I'll see you next time cheers

**[2:22:32]** foreign foreign
