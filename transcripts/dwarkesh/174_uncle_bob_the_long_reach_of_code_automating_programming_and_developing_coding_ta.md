---
date: 2024-01-01
layout: default
type: transcript
series: dwarkesh
episode: 174
guest: ""
title: "Uncle Bob - The Long Reach of Code, Automating Programming, and Developing Coding Talent"
source_url: "https://www.youtube.com/watch?v=ldTPVd3vO9Q"
analysis_url: /transcripts/dwarkesh/174_uncle_bob_the_long_reach_of_code_automating_programming_and_developing_coding_ta.analysis/
permalink: /transcripts/dwarkesh/174_uncle_bob_the_long_reach_of_code_automating_programming_and_developing_coding_ta/
---

# Transcript: Uncle Bob - The Long Reach of Code, Automating Programming, and Developing Coding Talent

Source: https://www.youtube.com/watch?v=ldTPVd3vO9Q

---

**[00:00]** okay today i'm talking with robert martin who needs no introduction so let's begin with talking about the future of programming will gpt-25 be able to automate programming will i not have a job in 25

**[00:11]** years what is gpt 25 what is that gbt3 is the program that openai just released and it seems to be able to do some basic make some basic methods like making a

**[00:23]** palindrome because they just did deep learning over a bunch of github repositories so the future of ai basically going to be able to automate programming no

**[00:34]** pretty straightforward answer there's there's a fundamental reason behind this um in order to um finally replicate programming if you wanted a machine that could program like a human that

**[00:47]** machine would have to have human sentience and we are very very very far away from that kind of a machine why would we need human sentience because

**[00:59]** someone has to specify the the way the program is going to work and that specification is in fact the program no other specification will suffice so a business user comes along and he he

**[01:16]** he creates a rough specification but is depending on the human intuition and the human intelligence of the programmers to fill in all the horrible little blanks that the the business person omitted

**[01:32]** we programmers are detail managers we deal with all the mess we we're the ones who deal with the fact that text files sometimes uh terminate lines with backslash n but sometimes terminate lines

**[01:48]** with backslash and backslash r for reasons that go back 50 years because of teletypes and eunuchs and dos and all this crap and we're the ones writing the dumb little if statements to deal with the

**[02:00]** bizarre little exceptions that no business person wants to even think about if we tried to make a a a deep learning machine that could deal with all that stuff we

**[02:14]** would wind up with a hal 9000 something that has human intelligence and and we are so far away from that that it does not concern me in the slightest that some some deep learning machine will

**[02:27]** eventually take over all the programmers jobs i'm happy to hear that then but how about this uh potential which is that the development environments and the tools that programmers use will become

**[02:39]** so advanced that'll be almost like a symbiotic peer programming kind of assignment where uh you know you're working with the machine to write the code instead of just like writing it

**[02:48]** on the machine sure i mean that we've already had that for for the entire span of programming we've been doing that and the original programs were written in

**[02:58]** binary right so alan turing working on the the automated computing engine was literally writing things in binary because there were no languages and then

**[03:09]** eventually we made an assembler can you imagine the benefit of an assembler over binary all that horrible binary math that you had to do you don't have to do anymore and you can write your code in

**[03:22]** symbolic form that's already a huge advantage and then along comes john baucus with the fortran spec in 1953 and what a huge advantage that was over assembly language algol came along pretty quickly by 1966

**[03:37]** you've got oleo handle and christian nygard inventing objects this is you know 20 years after alan turing was doing binary programming you've got the first object-oriented language

**[03:50]** c comes along in 68 two years later c plus plus comes along 12 years after that and we've got this massive progression of of incredible amounts of help to the programmer

**[04:05]** then in the in the late 90s we start getting this wild stuff in our tools the intellisense and the refactoring tools and the inspectors and the duplication finders so a modern ide is a

**[04:19]** treasure trove of of tools that allow a programmer to do immensely more complex things than we used to be able to do so yes i hope that machine learning continues

**[04:34]** to make our tools more powerful but that will never alleviate the need for the programmer to be there and supervise those tools i'm a pilot i fly a plane

**[04:46]** the plane has a beautiful autopilot i can turn it on and the plane will fly itself all the way to my destination and i watch that thing like a hawk because it's a

**[04:56]** a machine and it's going to do the wrong thing at exactly the wrong time so i sit there and i watch that autopilot and every time it's supposed to do something i make sure it does that thing i'm still

**[05:09]** in charge it's not [Laughter] but once you get these advanced tools well the future of programming just look incredibly different from what

**[05:19]** programming machine is like now you've written about how um the the way that touring wrote the first programs is not that dissimilar to how we write programs now is that sort of continuity something we

**[05:31]** should expect in the future or is the interface going to completely get modified well i so i mean the interface has been completely modified since you bring but but the act yes

**[05:42]** programming is still sequence selection and iteration yes programmers still arrange programs in little units of sequence selection and iteration will we continue to do that well i i

**[05:55]** think that's a very interesting question and we've had some hints about other possibilities if you've ever programmed in prologue for example you see that the sequence selection and iteration gets transformed into

**[06:10]** something else equally detailed but it's not sequence selection iteration anymore it's it's declarative truth i'm not going to go deep into prologue but but

**[06:23]** if you want to bend your brain around a concept that you're not familiar with study prologue for a couple of days but but in the end are we going to get to a a situation similar to my autopilot

**[06:37]** where i can set up some parameters in a tool and then watch the tool as it starts to develop a program and then i as the programmer watching what it's doing start tweaking

**[06:51]** parameters around the outside saying no no not that not that this this go in this direction will i be able to do that yeah i'd say that's probably very likely sometime in the next

**[07:03]** uh couple of decades that that the way we program computers will be more like training a dog rewarding it in the right circumstances and punishing it in the others

**[07:19]** we'll see how that goes we'll see how that goes but under no circumstances will there not be a programmer involved someone with the same skills that you and i have today someone who is deeply analytical and a detail manager and is

**[07:33]** watching out for all the dumb little gotchas that the machine has no clue and no strategy for addressing i'm happy to hear that our teams and programmers less creative

**[07:44]** than individuals programming alone uh teams of programmers are far more creative than programmers working alone but they also go in many different directions at once so

**[07:56]** they need there's you need a leader a team has to have a leader one of the problems that we have had in the agile community is that there's a certain faction of agilists who believe there should not be

**[08:09]** a leader that the entire team is homogeneous and equal in a mass egalitarian society where everyone is the same and my experience is that that doesn't work at all

**[08:22]** uh a team needs a leader and then the team is generating ideas just like crazy the team generates ideas and the leader is the one who acts like you know jean-luc picard

**[08:34]** this one not that one interesting um now let's talk about educating future programmers i i watched an interview with linus torvalds where he was expressing concern that the complexity

**[08:48]** of the ecosystem has grown so much that he's not sure that somebody in his position could come up with such a grand innovation they're just not a um a rock to hold on to it like get that

**[08:58]** level of expertise at such an early in age are you is do you have that kind of concern that the ecosystem has developed so much that it's harder for young people to kind of

**[09:06]** get to the frontier it takes longer now because there's so much more croft that you have to wade through when i was a young programmer the machine that i was working on was

**[09:22]** initially a pdp-8 i've got a little mock-up of a pdp-8 sitting right there uh it must have gone through a power failure because it's not doing what i usually have it do but that was a very simple machine it

**[09:33]** was a 4k machine 12-bit word half megahertz clock rate and there were no libraries there were no frameworks there was no nothing right if if something executed in that machine

**[09:45]** it's because you wrote it and a programmer in those days could know everything about the computer and it wouldn't take very long it would take a matter of months to to eventually get to the point where

**[09:59]** you just knew everything those days are long gone it's it's now not feasible to point at a computer system and say well i know everything about my

**[10:10]** macbook pro no you don't it's just too much crud in there so there is a much longer learning curve to become as adept at programming as those of us who started 50 years ago and had to climb that tree

**[10:30]** while we were working on the other hand it is not like being a doctor yet if you want to become a doctor you must specialize there's there's no way to go forward in medicine without specializing even a general

**[10:46]** practitioner is a specialist nowadays because they have to exclude all this other stuff they they cannot do and and we are not there yet a programmer over a period of

**[11:00]** five years say can become adept at gui programming middleware programming database programming telecommunications programming threads all of this stuff can become um well healed inside of a five-year

**[11:16]** experienced programmer 10 years even better right so it's not like being a doctor or a lawyer where you absolutely must specialize and narrow your focus down to a razor

**[11:29]** programmers can still be real general practitioners gotcha let's talk about the factories which manufacturer programmers uh to become universities if you had to change one thing about how

**[11:42]** computer science has taught in universities what would it be and how would you change it i would not teach it at universities really i don't i don't think it's a

**[11:50]** university kind of thing again this is a discipline that is only 70 years old there is there is not that much in it there's there's far more cruft in it than there is

**[12:03]** actual knowledge actual you know solid you know teachable knowledge and the the vast majority of the skills that a programmer needs are trade-like skills not educational based

**[12:18]** skills right or or not university kinds of skills if you want to be in electrical engineers you have to go to university there's just a tremendous amount of stuff you've got to learn there

**[12:27]** if you want to be a doctor you've got to go to a hell of a lot more than a university right but to be a programmer and a good programmer this is a skill that you can learn at a

**[12:38]** community college or in a trade school over a period of a year maybe a year and a half get a good job with some mentors and learn it that route learn it that way i think that is a much better way

**[12:53]** for young programmers to become programmers not go to university it's not worth a four-year education the amount of money you'll spend on that for four-year education

**[13:03]** is not going to be worth the programming knowledge you get now it might be worth a whole bunch of other knowledge it's not worth the programming knowledge you're going to get if you want to be a computer programmer and you're just

**[13:14]** getting out of high school i've been looking at a trade program at some kind of a trade school or a boot camp or something like that some of these boot camps are not very good so i'd be real careful about that

**[13:25]** but some kind of pro program like that where you can you can spend a few months learning a learning a language like java or c-sharp or something like that and then move on to a job which has a

**[13:38]** mentorship or an apprenticeship program uh i mean university is studying computer science right now so i wish i heard that two years ago but in any case can you explain to me how it is then

**[13:50]** that we have an industry where to get in is not that hard in terms of just the education you need at least maybe there's like traits that are rare but getting in is not that hard the demand keeps growing

**[14:00]** very fast how is it that people are still becoming corporate lawyers when there's a job that pays really well that doesn't require that much education to get that you can get into real fast what

**[14:10]** what explains this in equilibria i'm going to try and interpret that question uh carefully there are there are when when i was a young programmer

**[14:23]** i thought anybody could do this that was my my fundamental hypothesis anybody could learn this it's ones and zeros i mean how hard is ones and zeros it took me a very long time and a number of

**[14:35]** very expensive mistakes hiring people uh to realize that not everybody can do this and in fact the the number of people who can do this is much smaller than i had at first thought it it's it is not a rare talent

**[14:53]** but it is not a massively common talent either and the talent requires a number of things right there's there's this need to be a deeply analytical

**[15:05]** and there is this need to be able to focus focus on very narrow things for very long times and there are people who simply cannot do that it's just not in there

**[15:18]** in their mental wiring they cannot do it uh but some programmers can or some people can and they can become programmers so you ask the question why are we putting out corporate lawyers

**[15:29]** well they have a very different kind of interest and mindset although they're analytical and they can focus they focus on different kinds of things we programmers focus

**[15:41]** on boolean decisions ones and zeros blacks and whites lawyers you know they're looking at people people are much more complicated than computers it's a very different kind of

**[15:54]** mindset uh if you have to estimate what percent of the population do you think has a repertoire necessary to become a programmer oh tough question for to ask um

**[16:07]** what percentage of the of the human population has the aptitude for programming i think there are 100 million programmers in the world right now that's just a guess but i think that's

**[16:21]** about right and that would be what 1 80th of the population so we we've got some demonstration that at least one percent of the population has this skill

**[16:35]** close to one one percent maybe it's as high as five to ten percent could be that high could be i know i've i've got i've had a number of experiences

**[16:46]** trying to teach people to program and not being able to get through after about 10 minutes you know their brain just goes somewhere else they can't can't do it uh and

**[17:00]** um that seems to be much more common than the other pic talent which is where the person that you're trying to teach gets excited and focuses in with you and that is much rarer

**[17:15]** so if going to university is not the best idea for somebody wanting to become a programmer if somebody wants to solve highly technical problems they think well it seems like i would need a good education

**[17:25]** to be able to do this maybe i need to know a lot of math would you recommend that they go to go to university and get a math degree so that they have the technical background

**[17:34]** i used to think that was true and i actually hired someone because they had a they got a master's degree in mathematics and i thought okay you know math master's degree in mathematics

**[17:43]** you're going to be able to think this way you're going to be able to focus you're going to be able to do this and i've found myself very disappointed with the way this person

**[17:52]** became a programmer now eventually they succeeded but it was not the quick success that i had expected it took a lot of of working and a lot of failure uh to get this person's mindset

**[18:06]** into the programming mindset as opposed to the mathematics mindset so there's a difference there now is it worthwhile knowing mathematics as a programmer yeah in certain fields it certainly is i

**[18:20]** mean if you're going to be doing any kind of you know physics work you know you're going to be writing the code for a particle accelerator probably want a little bit of math right if if you're going to be doing uh

**[18:32]** a really deep interesting financial stuff going to be one of the quants in a in a stock exchange or something like that probably need to know a little bit of good math right on the other hand if you're

**[18:44]** uh a run-of-the-mill programmer writing code for uh oh i don't know maybe uh yeah siri just yelled at me for saying run of the mill um uh if you're going to be writing the

**[19:00]** code that runs inside my refrigerator for example the machine control software inside my refrigerator um probably you don't need a tremendous amount of math

**[19:10]** for that a good high school algebra would probably do enough maybe a little bit of pre-calc probably enough i don't think you need you know deep math theory for that kind of stuff

**[19:20]** even the guys who do um game work even though that's pretty heavy physics stuff all that physics stuff is already in the physics engines so most of the time there i think you

**[19:30]** don't need all that math is it important for a programmer to know the business they're going into and the answer to that is yes right if you're going into an insurance business you better know the insurance

**[19:44]** business if you're going to be a programmer in the telephone company you better understand the telephone company uh and and so much of the early education of a programmer in a

**[19:56]** mentorship program at a company is really about the company and not about programming this is what we this is our our field of expertise this is what we do this is what

**[20:07]** an insurance claim is this is what all these other things are this is how we think about it uh it's so that you can you can effectively apply the business knowledge

**[20:20]** to the problem of writing code and that brings us full circle because you had asked me originally and you'd said well aren't we going to eventually have these machine learning things that can write

**[20:29]** code and the answer to that is probably not because it's the the intuitive knowledge of knowing the business you're in that allows you to make these low-level decisions that the business people don't

**[20:42]** want to make from that does it follow that if you want to become a very competent programmer you should try to specialize in a specific industry where

**[20:51]** or where the application programming is best exercise or should you try to develop first a broad range of experience and expertise uh both actually so as you take on a job you want to you want to specialize in

**[21:05]** the business that you're in for a period of n years whatever n is might be two might be three uh probably that short though uh and and get to know that business and then

**[21:18]** see if you can move to a different business domain and and spend two or three years on that and then try another business domain and spend two or three years in that and by that time you've got a

**[21:29]** nice broad business domain and that will allow you to infer other business domains because you know business domains have similarities and differences but once you've got

**[21:40]** three or four of them in your head you can start to triangulate now when you are considering hiring somebody as a programmer and they don't have a lot of experience so you can't just

**[21:50]** you can't just look for somebody to vouch for them what is it that they can do to signal to you that they would become a competent programmer that's a heck of an interesting question

**[22:00]** and one that i've struggled with for a very long time now a number of decades and i have found no reliable test i used to make people uh so back when i thought it was math i used to make people solve uh

**[22:17]** newton's method for uh calculating a square root i just draw it on the board i draw parabola on the board and say okay here's the slope you know it's the derivative of the function now come up

**[22:28]** with an algorithm and i'd let them use any language they wanted and i you know i thought that was a pretty good approach and then and then i found people that were very good at fat

**[22:38]** but could not do other things then i thought okay i'm going to describe the siva veritosthenes beautiful algorithm for finding prime numbers right i'm going to describe that

**[22:50]** in in simple terms and have them write some pseudocode and show me that they can actually build a doubly nested loop right and that was also not reliable

**[23:01]** although it was better it was not reliable so what i've the conclusion i've come to now is that there is no simple test what what you need to do is spend a fair bit of time

**[23:17]** with someone and observe how well they learn over a period of time and how well they apply that learning how well they can focus how well their how well they can deal with a problem analytically

**[23:30]** and that period of time is probably weeks so the the kind of interviewing that i would prefer to do now and i by the way i don't hire people anymore i'm now just kind of

**[23:43]** me but but i know people who do hire people and one of the one of the ways that they do it is to ask them to join an apprenticeship program

**[23:54]** and in that apprenticeship program they will be given a series of ever greater challenges not all of which are programming challenges some of them are writing challenges

**[24:05]** some of them are speaking challenges some of them are presentation challenges but a sequence of ever increasing um uh challenges and then at the end of that

**[24:17]** an assessment is made by everyone that they have talked to and they're offered a job or not and in some cases there's a stipend salary for that apprenticeship program in other cases there's not

**[24:30]** interesting do you suspect that the traits that are required to become a programmer these are developed in your childhood through the experiences you have in early life or maybe through high school

**[24:40]** and middle school or is it something that some people are probably just born with on some level it's hard to know um i i i think there's a certain amount of

**[24:51]** just neural wiring you know some some character defect that causes you to be a programmer um that not all people have however i have seen people who were not at all

**[25:06]** interested acquire the interest and acquire the talent um at different stages of life my son for example who is now a programmer and a very accomplished one

**[25:18]** had showed no interest at all in early grade school when i got interested i was 12 years old right so i thought oh okay everybody's going to be interested at 12. now my son didn't show any interest at

**[25:30]** all until he left home and became a or or close to leaving home late late high school early university and came back with this interest and skill my daughter um has just

**[25:45]** turned 30 and is suddenly very interested and is acquiring a significant amount of skill so i've seen this happen at different stages the switch turns on and and all of a sudden they've got all the all

**[26:01]** the motivation and the focus energy and the analytical skill they need so i don't know i you know it's a a deep mystery to me are there advantages to learning this

**[26:13]** material and adopting these skills early in life or do you get a more mature perspective if you learn it later on in life had you asked me that question 20 years ago i would have said

**[26:24]** there's obviously an advantage to teaching young children i mean if you can get the young children immersed into computer as well obviously they're going to turn into

**[26:33]** much better programmers and i'm not so sure that's true now so the counter examples are the vast number of um programming toys and and they span a huge um a huge

**[26:53]** period of time so nowadays you've got like things like lego mind blocks and um or mindstorm and and you've got a whole bunch of other tools that try to encourage young people to become programmers you

**[27:06]** know kids that are 12 13 14. in the early days we invented languages that would help young people become programmers the logo language for example was all about you know driving a little

**[27:19]** mechanical turtle on the floor and letting it raise a pen and draw on a piece of paper and kids you know they would they would issue it commands go forward 10 turn right 90 degrees go forward 10

**[27:32]** drawing squares and circles on a paper and what we found through all of these through all this long period of time attempting to make tools that would appeal to children is that

**[27:47]** it did not have a profound effect there's a whole bunch of children that would sit and drive the turtle around for a little while and then lose interest and never develop the the more

**[27:58]** interesting skills of of putting things in variables and calling functions those just went they didn't happen uh and we see the same thing with things like lego mindstorms

**[28:09]** now there are children who do grab it and you can tell they want to become programmers but then the question is well wouldn't they have just grabbed it anyway why did they need this tool is are these educational

**[28:23]** props actually incentivizing more people to become programmers or are they just helping the ones who would become programmers anyway and i don't know the answer to that i'm

**[28:37]** i'm skeptical nowadays interesting um so you you're not bullish on mandatory coding classes in middle in high school i think everybody should have a and uh everybody should get the experience i

**[28:52]** see um probably you know for a uh what a four-week or a six-week period everybody should do a little you know basic programming or

**[29:04]** ruby programming something you know i want to be careful there because turn people into ruby and put you know it's a very complicated language when you get into it but you know maybe a little little bit

**[29:14]** of coding a little scripting a little something so that you know basically what it's about but other than that i don't think there's any any need to like push a year-long course i don't think that's necessary

**[29:26]** i think the ones who are interested are going to do that on their own right right um let me ask you about the sense of style that a programmer develops over time is this at all related to what has been

**[29:37]** called the elusive writers here where a writer over time develops a sense of prose and style is is that sense related to the one that one develops for programming

**[29:50]** michael feathers coined a term 20 years ago which he called design sense and he he's threatened to write a book on this for the last 20 years i haven't seen him write it yet

**[30:03]** but the basic idea is that yeah there is this um there is this sense that a programmer develops over a long period of time that a uh a a bit of code or a design of a system or an

**[30:21]** architecture of a system somehow feels right and it's an elusive kind of sense it's the the judgment of beauty you know it's like oh a beautiful thing

**[30:34]** and and the word beauty ought to be used here because there are beautiful designs there are beautiful architectures there are beautiful functions which can be

**[30:47]** described as beauty and understood as beauty only by people who have the experience to look and say oh my goodness that's beautiful i was watching a a program on on netflix yesterday

**[31:02]** it's called queen's gambit it's a new one it's about a a young girl who becomes a chess master and in the midst of this someone asked her you know why are you so interested in chess and

**[31:13]** she leaned back and she said it's beautiful or it can be beautiful and i think the same thing applies to software hmm christopher hitchens who was known for his excellent writings suspected at some

**[31:25]** point that the sense of writing was uh tempered by a sort of musical intelligence about cadence and prose do you think musical intelligence plays into your ability to code well or beautifully

**[31:37]** well um there is and and this has been known for some time there is a very strong correlation between programmers and musicians people who study music or have played an instrument or have developed a musical

**[31:52]** sense often become programmers uh why that's true i don't know it could be the the rhythmic thing the the mathematical uh layout of the of the scales the who

**[32:04]** knows if you look at a a a musical composition if you look at a sheet music it is a program it's got if statements it's got while loops it's got sequins

**[32:13]** it's got everything so maybe it's something like that i don't know but there's definitely a correlation interesting um so let's talk about your idea for

**[32:25]** or your claim that we need some sort of body within software engineering that decides who has the ethical and the technical competence necessary to become remain a programmer

**[32:37]** um i don't know if you change your view on this or if i and i'll let you elaborate what you mean by this but somebody who is concerned about this might say well this is exactly what has happened in other

**[32:47]** industries where occupational licensing that's keeping people out of the industry so that the labor pool is artificially reduced to the advantage of the people already in the industry

**[32:58]** and there's also the added wrinkle with the um increasing calls for censorship and cancel culture we could have expect that this body might itself become a tool for removing

**[33:10]** people who challenge orthodoxies how do you respond to these challenges well so the the problem the problem is that programming has become an entirely essential

**[33:27]** job function for our society to exist human society can no longer exist without programmers and that dependency is growing at an exponential rate so you know you look around the

**[33:40]** room here and you'll just see dozens and dozens of little electronic things that have code running in them that just make life doable and all of the things that we used to depend upon that

**[33:52]** did not have code running in them all now have code running in them so your microwave oven and your refrigerator and your car telephone your television all has code running in it

**[34:02]** our society can't exist anymore without programmers and there is no constraint on programmers to behave ethically to have any standards to have any disciplines so that's an unstable

**[34:16]** situation it can't go on like that how do we address it do we need uh something akin to the ama the american medical association who provides you know licensure for doctors

**[34:31]** uh do or do we need um something else do we need maybe a guild structure maybe a whole set of little organizations that that license their own programmers with different

**[34:45]** sets of standards and ethics and disciplines and then let the market decide you know those guys did better than those guys i think we'll hire them

**[34:55]** i don't know where that's going to come down i um my fear is that it will be forced upon us by government before we can develop that solution and i'm hoping that we can develop that

**[35:09]** solution uh before government sticks their little fingers in there and screws it up completely there are a number of companies that have begun to do this

**[35:18]** right so you look out in the world out there of cons especially software consulting firms and there are software consulting firms out there that have based themselves on a set of principles ethics and

**[35:28]** disciplines and they advertise themselves that way and i think there will be more and more of that so that's kind of the direction i think the industry is going to go at least i hope

**[35:40]** it goes that way and i hope we get there before government sticks their foot in it and kicks us all to hell i hope so too i wanted to ask you why um tech of all industries

**[35:53]** seems to be so political in the sense that specific companies seem to have a clear political orientation uh that doesn't seem to be true in many other areas of work

**[36:04]** do you have a sense of why that is um no well yes and no i guess and and it's it's been a deep puzzle um if you let's let's do this differently if you

**[36:24]** look at the political bias geographically right there is a definite political bias in the united states you've got the two coasts they tend to be liberal blue states on each coast cities tend to be more liberal

**[36:38]** rural areas tend to be more conservative the midwest tends to be more conservative if you get um go to a company in kansas city and you find a company there you know that has a hundred programmers

**[36:53]** odds are those programmers are going to be conservative it's just you know because of the geographical bias go to san francisco odds are the programmers there are going to be

**[37:03]** liberal that's just the geographical bias is there anything else in software that drives people in a certain political direction

**[37:19]** well maybe it turns out to be easy to become a programmer we talked about this before right you don't really need to go to university you don't really need to to get a full

**[37:34]** full education right you can become a programmer without a lot of experience and and because our industry continues to invent new um new schemes all along

**[37:48]** right there are people who can jump into these schemes very early so for example html um html was invented you know 20 years ago and the and a whole bunch of high school

**[37:59]** kids suddenly got really good at html and of course they went out to get jobs without a lot of university training without a lot of anything so it's easy there's there's a low uh barrier to to um

**[38:14]** acceptance early on and that i think has led to a good thing which is a bunch of marginalized folks folks who live in marginalized communities managed to get in very easily and they

**[38:31]** get experienced and they develop skills and that's also good and then i think and this is a guess on my part i think they use that skill

**[38:43]** and that and that um technology that gives them a voice and that voice has been turned and in a way that is sometimes very detrimental now i don't want to cast you know

**[38:57]** aspersions on every marginalized community but i have noticed that there are some that suddenly develop a very loud voice and in uh in a lot of cases they wind up driving the cancel culture just

**[39:12]** just you know the way that looks like it's been happening from my you know my middle age no i'm not middle aged i'm actually old now from my old conservative white bias right that's what it looks like to

**[39:26]** me interesting uh let me ask you about quotas i i i think you let a really good argument in your blog uh about why quotas don't necessarily help the groups you're trying to help

**[39:39]** does the argument you laid out there and i'll let you explain it apply and generalize to other places where things like what is replied like universities for example

**[39:51]** i think it does i think it always does um i mean the idea behind a quota is is always very well intentioned right there's there's a marginalized group they're not getting uh

**[40:02]** serviced properly we need to relax the barrier of entry for that marginalized group so that more of them can join well-intentioned you know everybody wants the best

**[40:15]** but what's the end result the end result is that you lower the standards the standards have to come down which hurts the entire industry and it doesn't help

**[40:28]** the marginalized folks to let them in under low standards but expect the high standards on exit right because then you'll see this this failure and we see that in universities and we see it in

**[40:40]** in employment as well is that the dropout rate or the failure rate is higher it doesn't help i once sat with a woman a very accomplished woman um and we were at a conference and i

**[40:53]** i was giving a keynote and she was giving a keynote and we were just talking about this issue and she looked at me and she said i hope to hell that they did not ask me to do this keynote just because i'm a

**[41:04]** woman and you know i i could feel that angst the devaluing of her of her ability to do a keynote talks because she was invited just to become a woman so her fear

**[41:20]** her fear was that she was being devalued by a quota system that she didn't even know if that existed i think in general the only way to deal with issues like this is to do it entirely on merit

**[41:37]** right if you're going to be a programmer we will you know i'm perfectly happy to hire anybody don't i don't care what your you know political biases your sexual biases your race

**[41:48]** your racial situation i don't care about any of that stuff as long as you can write the code i'm happy to work with you i don't want to suddenly or or i don't want to

**[41:58]** relax the standards for a certain subgroup i don't think that's fair to anybody just me yeah yeah i completely agree i did malcolm gladwell was in a debate once and

**[42:10]** i i i actually really liked malcolm level but he started off by saying first of all i think it's scandal that nobody on this stage is a woman and there's a point there but then i thought about it i realized

**[42:20]** well imagine being the woman who just came on stage because malcolm gladwell wanted a woman you know what i mean like imagine being in that situation um anyways let me ask you finally about

**[42:31]** advice you would give to a 20 year old who wants to become a programmer well okay being becoming a programmer is not particularly difficult in our in our day and age yet it may be at some point in time but right now it's not

**[42:45]** uh if you're if you think you want to be a programmer and you think you have the aptitude it is stupidly simple to get on youtube now or get on a bunch of other websites and learn to code and it doesn't take a

**[43:00]** lot of effort if you've got a laptop if you've got a computer at your disposal if you can go onto youtube or any of the other sites out there just find

**[43:09]** some site that'll walk you through an initial java program and then experiment with that as much as you can learn learn how to write this code read other people's code go onto github

**[43:22]** download their code read it understand it it'll be hard but that's okay you know you can do it there's a whole bunch of books out there tons and tons and tons of very good books that you can

**[43:35]** start out with simple books like you know the joy of java or you know java for for dummies in 10 days or you know learn c in 21 days any one of these books um that will just help you immensely

**[43:49]** find a mentor someone who's been at it for a while most of them will be overjoyed to have someone that they can teach and work with and help

**[44:02]** um if you can get into a a trade trade school for programming uh that would be great not necessary but it would be great um if you've got the means to go to university and you want to spend the

**[44:16]** ridiculous amounts of money that universities now cost and go into horrific debt for you know the rest of your life okay you can do that too and i'm not gonna stop you

**[44:26]** and you'll learn a whole bunch of really cool stuff there stuff that some of which you'll even be able to apply later on in in your career but if you don't have that means if you don't have the means to go to university

**[44:40]** that's okay i mean you can get this you can acquire these skills you can become a programmer with a minimum amount of investment just find some people to mentor you along find a company that's

**[44:53]** willing to hire a beginner and they're a lot because the demand is immensely high right now and and will continue very high for a long time and find a way to get in and it's not that

**[45:05]** hard right so that would be my advice read like crazy read inhale as much as you can study like crazy watch videos and do exercises just you know fill your

**[45:20]** brain with this stuff and then it ought to be simple after that [Laughter] excellent well thank you very much for uh talking with me today this is very

**[45:31]** fascinating it's a pleasure i enjoyed it very much hey if you enjoyed this podcast please consider sharing it with your friends and posting it on social media

**[45:39]** word of mouth is incredibly valuable for a new and a small podcast like this one so thanks for watching [Music]
