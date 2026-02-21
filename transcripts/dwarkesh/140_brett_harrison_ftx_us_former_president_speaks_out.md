---
date: 2024-01-01
layout: default
type: transcript
series: dwarkesh
episode: 140
guest: ""
title: "Brett Harrison — FTX US former president speaks out"
source_url: "https://www.youtube.com/watch?v=yXgDlIlB93A"
analysis_url: /transcripts/dwarkesh/140_brett_harrison_ftx_us_former_president_speaks_out.analysis/
permalink: /transcripts/dwarkesh/140_brett_harrison_ftx_us_former_president_speaks_out/
---

# Transcript: Brett Harrison — FTX US former president speaks out

Source: https://www.youtube.com/watch?v=yXgDlIlB93A

---

**[00:00]** you are probably gonna be fired for this letter that you wrote Sam is going to destroy your professional reputation like where do you think you're gonna be able to work after FTX it was he was threatening me when I knew Sam when he

**[00:12]** was 21 22 years old he was like a happy healthy looking kid when I got to FTX I saw someone who was very different than that person I remember and it felt like he was spending virtually no time helping the company move forward it was

**[00:28]** so much about image and brand and PR media was primed for the archetype that was Sam doesn't matter how little time he spent with the company doesn't matter how he treated employees internally architect it makes it really easy to

**[00:42]** access kind of all corners of the digital asset ecosystem okay today I have the pleasure of speaking with Brett Harrison who is now the founder of architect which provides Traders with infrastructure for accessing digital

**[00:57]** markets before that he was the president of FTX us and before that he was the head of ETF technology at Citadel and he has a large amount of experience in leadership positions in finance and Tech so this is going to be a very

**[01:12]** interesting conversation thanks for coming on the lunar Society Brett yeah thanks for coming out to Chicago yeah my pleasure my pleasure is the growth of ETFs a good thing for the health of markets there's one view

**[01:25]** that as there's more passive investing you're kind of diluting the power of smart money and in fact where these active investors are doing with their fees is subsidizing the price discovery that makes markets efficient and with

**[01:38]** passive investing you're sort of free writing off of that um you were head of ETF technology at Citadel so you're the perfect person to ask this it's bad that there's so much passive investing

**[01:49]** I think on net it's good I think that most investors in the market shouldn't be trying to pick individual stock names and the best thing people can do is invest and sort of Diversified instruments and it is far far far less

**[02:04]** expensive to invest in like indices now than it ever was in history because of the Advent of ETFs yeah so maybe it's good for individual investors to put their money in passives uh Investments but what about like the

**[02:23]** health of the market as a whole is it hampered by how much money it goes into passive Investments it's hard to it's hard to be able to tell what it would look like if there was less money in passive investment now yeah I do think

**[02:34]** one of the potential downsides is ending up creating extra correlated activity between instruments purely by virtue of them being included in index products so you know if like when Tesla gets added

**[02:49]** the S P 500 like Tesla doesn't like suddenly become a different company who's you know market value is like fundamentally changing but yet it's going to start moving very differently you know in terms of its beta

**[03:03]** correlation between other instruments and S P 500 purely as a function of all the passive investing that moves these instruments in the same direction so that's the sense in which I think it could be detrimental but naively you

**[03:14]** would assume that like um efficient market hypothesis would say that if people know that Tesla stock price would irrationally climb when it's including the S P 500 then people would short it and then it

**[03:25]** there should be no impact from this irrelevant information why isn't that the case like why it probably mostly is um I think that sometimes there can be liquidity differences that cause at least temporary dislocations and stocks

**[03:38]** like I mean the simplest example is like you have an ADR like an American depository receipt that's sort of expungible for some underlying foreign stock and these two things should be like almost the same value at all times

**[03:52]** like of currency conversion and conversion ratios but if one of the markets is highly illiquid or difficult to access then there's going to be dislocations in price and that's like the job of like the James streets of the

**[04:04]** world to kind of Arbitrage away the price over time and so long run you wouldn't expect these things to be Associated for that long so I'm sure there are people who are understanding like the fundamentals of individual

**[04:16]** names the S P 500 and when there's like American news and the entire s p Falls they are you know maybe buying s p and selling individual names and spectracking that relative value spread to come in over time speaking of by the

**[04:30]** way these firms how International Civics but how similar are the strategies for Market making or trading that James freed versus Citadel and these four percent is it the same sorts of strategies or are they pretty different

**[04:43]** I think a lot more differences Than People appreciate from the outside um different companies have they establish different niches and areas like James Street established its

**[04:55]** early Niche and ETFs um at kind of like a mid frequency level um so not like Ultra fast but not like long-term year-long discretionary macro whereas maybe you are you know Citadel Securities uh kind of firm got you know

**[05:12]** built their Niche more on like lower latency you know options Market making so like it could be like all over the place there are some where they are trying to optimize for really short-term like microstructure Alphas like trying

**[05:25]** to predict where the order book is going to move over the course of anywhere from milliseconds to seconds there are firms that care more about the like relative conversions of instruments over the course of hours to days there's you know

**[05:39]** sophisticated quantitative trading firms that are doing longer term you know days to weeks to months long trays too a lot of the infrastructure can be similar like either way you need to be able to connect to exchanges download

**[05:51]** market data establish simulation platforms build like tools for Traders to be able to grasp what's going on in the market and especially be able to visualize like their own proprietary models and Alphas uh but beyond that the

**[06:04]** actual strategies and the ways they make money can be very different famously in other kinds of development there's these like very famous hacks and algorithms right so in gaming and Graphics John Carmack has the famous passenger square

**[06:18]** root for doing Graphics calculations normalizing vectors faster um you were not only a developer in finance I know the exact term is for that um but you led you know teams of

**[06:31]** hundreds of people who are doing that kind of development are there famous examples like this in finance the equivalent of Passenger square root but for the kinds of calculations you guys do yeah they're like all over the place

**[06:41]** there's tons of you know hacks and tricks and things like that I think like for example here's uh a famous One not famous I think I read it in a paper and like a bunch of other you know developers from different other

**[06:54]** companies told me about this it's not something I saw at the places that I worked but if you're sending a message to let's say NASDAQ to buy stock and you want to get there as fast as

**[07:04]** possible well what is a message to NASDAQ it's a you know TCP IP wrapped you know message with a particular proprietary protocol that NASDAQ implements well let's say your goal is you know you

**[07:17]** know you're going to trade Apple but you're not sure like what price and at what time and you're kind of waiting for some signal to buy apple as fast as possible so what you can do is you can

**[07:29]** pre-construct the entire TCP message like first put the TCP header on there and the IP header then like the kind of outer protocol that NASDAQ specifies and the inner protocol except for like the bytes slot where you put in the price

**[07:44]** and then pre-load that message into the network cards sending buffer so that once you're ready to send you can just like pop in the price and send it off and incur as little latency as

**[07:57]** possible that's awesome I think the analogy to video games is a good one because like just like in you know video game Graphics what's the end goal it's not like to produce the most theoretically perfect simulation of

**[08:09]** environmental Graphics it's to have something that like looks good enough and is fast enough for the user and that's also true in like hft and quantitative Finance where like the goal is to get to like the approximately

**[08:21]** right trade as fast as you can it's not to have like the perfect theoretical model of you know underlying price dynamics that is so fascinating um but this actually is an interesting question

**[08:33]** you if you have some sort of algorithm like this that gets you a few nanoseconds faster to the NASDAQ exchange and that's why you have Edge where you've like lease microwave Towers to get from New Jersey to Chicago faster

**[08:43]** or you've bought an expensive server in the same place at like NASDAQ um is housed what fundamentally is the advantage to society as a whole from us getting that sort of information faster is this just sort of a zero-sum

**[08:57]** game of who can get that incorporate that signal faster like why is it good for a society that people so much so many resources and so much brain power is spent on these kinds of hacks and these kinds of optimizations

**[09:10]** yeah so I think if you start from the premise that having liquid tight efficient markets is important for the world and you say like how do I design a system that you know optimizes for that I think you want

**[09:26]** smart sophisticated technologists competing at the margins and of course the more they compete the smaller the margins become to the point where you think like the little extra activity people are doing

**[09:39]** to get slightly better don't seem to be you know greatly affecting the whole system as much as if you know as it was in the earlier days maybe when things were slower and tick sizes were wider I think it's difficult to imagine

**[09:51]** designing a market where you say like okay everyone should innovate up until this point and then stop competing and then just stay stasis you know and maybe you can create certain regulatory or Market structures to try to prevent that

**[10:02]** but I think on average you want people competing at the margins even if they seem like they are you know minuscule but at the same time I think it's not zero-sum for Society for you know

**[10:14]** technologists to be creating like super fast like ultra low latency very sophisticated algorithms like maybe I don't know we have a lot of geopolitical instability in the world who knows if like the our microwave Network that we

**[10:28]** built out in the US could have like greater use cases than just for quantitative Finance but like quantitative Finance subsidize the creation of these towers okay but so that that's sort of like a

**[10:40]** contingent potential benefit I guess people tell us another story about NASA right in this case literally microwaves that they tested as a lot of the science that ended up becoming becoming into products so that's a that's an

**[10:50]** interesting account of the benefits of finance that it has the same yeah whatever tricks they come up with might be useful elsewhere but that's not a story about how it's directly useful to have

**[11:02]** you know nanosecond level latency for filing your like Apple stock or something like that why is that useful directly I mean if there is some kind of news that happens in one part of the world and

**[11:16]** that should affect the current price of stock in a different part of the world I think that if you care about efficient markets you want the gap between like source of Truth events and ultimate price Discovery to

**[11:32]** be as small as possible I think if you believe if you want to question whether getting you know a few extra like milliseconds or microseconds or nanoseconds is worth it I think you're then putting some kind

**[11:46]** of like value judgments on like the what is the optimal time it takes to get from to price Discovery and saying like you know a second is too slow but a millisecond is too fast or millisecond is too slow but a microsecond is too

**[12:01]** fast and I just don't think we're like in a position to do that I think we kind of always want as close to instantaneous price Discovery as possible um I I'm only asking more about this because this is really interesting to me

**[12:12]** there are some level of resources where we would say that at this point it's not worth it right like let's say five trillion dollars a year was spent on getting it down from like two nanoseconds to like one nanosecond I

**[12:24]** know that that's probably not a realistic number but just like there's some margin at which for some weird reason that there's a society are just putting so many resources on it would you say that we haven't reached

**[12:34]** that margin yet where it's not socially useful the amount of brain power and resources that are spent on getting these tight spreads and I don't know how large a percentage of like GDP prop trading is I suspect it's

**[12:48]** not that large uh so I don't think we're close to that you know theoretical image of where I would start to feel that it's a waste but I also think like there's a reason why they're willing to spend the money on this kind of Technology because

**[13:03]** they're obviously profiting from doing so and it has to come from somewhere so somehow like the market is subsidizing the creation of this technology which means that there's still ability for Value capture which

**[13:16]** means there's still a service that's being provided in exchange for some kind of profit I think we wouldn't spend 500 five trillion dollars in a microwave Network because there isn't five trillion dollars of

**[13:27]** extra value to be created in doing so got it has being a market maker change your views about civilizational tailor risk because you're worried and like you're worried about personally getting run over right by some sort of weird

**[13:44]** event in adverse election does that change how we think about societies getting run over by a similar thing or is is it are the mental models isolated so I think working in you know high-speed Finance teaches you

**[13:59]** to understand how to more correctly estimate the probability of rare events and in that sense you know working in finance makes me think more about the likelihood of you know civilization

**[14:12]** ending you know problems but it doesn't suggest to me sort of different solutions you know there's a very big difference uh being in a financial setting where you know your positions are numbers that you can put

**[14:25]** in a spreadsheet and you can model like what happens if like every single position goes against me you know 3x the wrong way and what instruments would I have to buy or sell in order to be able to hedge that portfolio that's like a

**[14:36]** closed system that you can actually model and do something about having like a traitor mentality on you know future pandemics I don't think helps you much I think maybe it slightly changes your ability to kind of

**[14:50]** estimate the probability of such events but the actual solutions to these problems are a combination of like you know Collective action problems plus you know being able to sort of model the particular type of you know unknown

**[15:03]** Unknown about whatever the event is uh and I think those kinds of you know Solutions should be left to the experts in those particular fields and not up to traders in other words I don't think like having the trader mentality around

**[15:15]** rare events in like normal civilization outside of Finance really kind of helps you much and maybe in some ways has let people to think more heuristically that they can do something about it gee who could we talk to be talking about

**[15:27]** um but that's really interesting you would say that um I would have like famously uh you know these Market making firms really care about having their employees be well calibrated and good at sort of thinking about risk uh

**[15:41]** I'm surprised you think that the transfer between thinking about that in the financial context and thinking about that in other context is uh that low yeah again I think it helps you at estimating probability of air events but

**[15:53]** it does not translate super well to what action then do you take in the face of knowing those rare events where your circles or people in finance earlier to recognize the dangers of covid

**[16:07]** that's a good question um I think that people in my circles were quicker to take action in the face of knowing about covid um you know a lot of people who like

**[16:22]** kind of stuck around in you know cities and that kind of their existing like you know particular situations like not knowing kind of where this was going to head long term and I think if you have the like the

**[16:35]** fortune of having the financial flexibility to be able to do something like this a lot of like the people in kind of financial circles kind of immediately recognized okay there's this like big risk this unknown and I don't

**[16:47]** want to get like adverse selected against in terms of being able to like get out of the like locus of you know bad pandemic activity and so people immediately were fleeing cities I think faster than other people

**[17:00]** that seems point in the opposite direction of them not being able to you know estimate and deal with geopolitical risk well I mean there there you have like an actual event that has occurred and then in the face of the

**[17:12]** event what do you do right now yeah I think that's different than like what do we do about the potential for you know AI to destroy civilization in the next hundreds of years yeah or or what do we do about the next potential you know

**[17:27]** biological weapon or the next pandemic that could occur yeah uh speaking of it you were at you were head of semi-systemic Technology at Citadel when covet Hood right yes exactly what how did you know these hft firms react to

**[17:44]** covet what was what was it like during covet because obviously the market moved a lot but uh on the inside was a good bad or yeah I mean all the companies I mean Citadel Securities and but really all of the ones in this sort of uh just

**[17:59]** Finance fear I think were extremely resilient I think a lot of them found that their pre-existing ideas that in order for the team to succeed everyone needed to be in the exact same place and it was

**[18:11]** very important from like uh you know IP perspective to make sure that people weren't taking a lot of this work home with them completely went out the window and people had to completely adjust to the idea that actual trading teams that

**[18:23]** are used to be able to have like eye contact with each other at all times need to adjust to this you know pandemic world and they largely did I think at least from a profitability perspective it was some of the best years of you

**[18:36]** know hft firms you know P L's in recent history matching engines already have to deal with the fact that you can have orders coming from like Illinois you can have orders coming from Japan and given light speed they're not going to arrive

**[18:49]** at the same time you still kind of have to work around that is there any hope of a single market and matching engine for once Humanity goes into our planetary or Interstellar could we ever have a market between like us and Alpha Centauri or

**[19:03]** even us with Mars or is it lack too much for that to be possible yeah so I mean without making any changes to a matching engine there is nothing that you know says that when an order comes in it

**[19:16]** can't be older than you know X time right what it does mean is that like the the actual sender if like they're sending a market order from halfway across the world by the time the order reaches the exchange they might end up

**[19:30]** with a very different price than the one they were expecting when they sent it and therefore like there's probably a lot of adverse selections sending a market order from halfway across the world and in a collocation facility

**[19:40]** so you can technologically run an Interstellar you know exchange this might not be good for that person living on uh on the moon is there any way to make it more fair yeah so I think

**[19:52]** there's actually a kind of real world analog about which is like automated market makers on slow blockchains because if you're used to working on NASDAQ where you know NASDAQ processes

**[20:06]** like a single message in somewhere between like tens and hundreds of nanoseconds per order a blockchain like ethereum processes what like you know 15 to 50 messages per second so significantly slower by like numbers of

**[20:23]** orders of magnitude and yet they've been able to establish like pretty mature like Financial marketplaces by saying that rather than you having to like send orders with prices on them and then cancel them when

**[20:37]** the prices aren't good anymore like there will be kind of an automated function that moves the prices at the matching engine and so whenever your order reaches the exchange it'll always be kind of a

**[20:49]** predetermined fair price based on the kind of prevailing liquidity at the time so one can imagine like building a NASDAQ for like you know Interstellar Market is kind of similar to building like uniswap now on ethereum in terms of

**[21:05]** water magnitude and speed but there's other things you can do too like you could establish like periodic auctions instead of like continuous matching and things like that and that could potentially help mitigate some of these

**[21:16]** issues yeah essentially something else I want to ask you about what do you what is your opinion of periodic you know frequent batch auction systems should we have more of that instead of So in theory they help mitigate the advantages

**[21:29]** of high frequency trading yeah because if you know there's going to be an auction every 30 seconds and it's not going to be by time priority it's going to be by price then it doesn't matter if

**[21:42]** you send that order at the beginning of the 30 second period or the end of 30 second period like it's it's really like the price that determines whether you get failed not something to do with like particular latency to The Exchange I

**[21:53]** think in practice the couple of exchanges around the world that used to have those have switched away from them like I think the like Taiwan stock exchange used to have periodic auction system

**[22:03]** and I just thought the like the liquidity and price Discovery wasn't good and it was like complaining about a lot and they eventually moved off of it to a continuous matching system so I guess in practice it doesn't quite work

**[22:14]** as well um but it's hard to tell it's really hard to tell what country I mean in your long experience of dribbling Financial infrastructure what country do you feel has the best

**[22:26]** uh infrastructure and setup for good markets I would say the United States except what's happened is U.S companies like NASDAQ have licensed their exchange matching engine technology to other exchanges around the

**[22:42]** world so like the NASDAQ omx technology Powers a number of the exchanges in Europe and some in Asia so it's hard to sort of say that like the is the technology American like I guess so I'm not sure exactly who wrote A lot of the

**[22:57]** stuff underneath you know the NASDAQ technology but I do think the U.S markets are some of the most you know efficient and low latency and expansive and products that allowed in the world how do adverse selection in trading and

**[23:15]** hiring differ in hiring there are one many more opportunities for positive selection versus the negative selection you usually encounter in finance

**[23:27]** and the other thing is that most financial markets are like you know in the US when you think about like trading in general you're thinking about like liquid markets the hiring Market is highly inefficient

**[23:42]** you know maybe the like pipeline of you know orders from like Harvard MIT Princeton Yale to Jane Street and cital securities is like a very liquid pipeline but like there are many many universities and colleges throughout the

**[23:57]** country in the world that have extremely talented individuals whose resumes will like never end up on your doorstep so you might end up with like a resume from you know some you know graduating senior from college who has no internship

**[24:09]** experience and your Trader mindset might think okay it's a terrible adverse selection but it actually could be that like that person if he's willing to you know put themselves out there and apply to

**[24:21]** your company from this like a relatively unknown University then that might be the signal that is like the best person in that entire region and that might be a positive selection so I think that it's not exactly the same like adverse

**[24:34]** lotion Dynamics as there is in the traditional trading worlds yeah yeah definitely especially if you have like I guess Mission oriented companies have a especially good way of getting rid of adverse election right yeah yeah exactly

**[24:45]** like the companies with really strong brands uh I mean that's one of the things we saw at Jane Street was like I heard stories in the old days of Jane Street that like the first resume is from Harvard where like the people were

**[24:56]** terrible like they couldn't do like basic math and they just wrote this like the worst candidates compared to other people that they were able to find and then they established this brand and this recruiting Pipeline and this

**[25:06]** reputation for having very difficult interviews and for paying people really well and having this like amazing work environments that all of a sudden all the people getting through the pipeline from Harvard were like really

**[25:16]** really great and it wasn't like the quality of students at Harvard changed there's probably a bell curve there like there is everywhere else it was just like the positive selection resulting from The Branding efforts and the like

**[25:26]** Mission driven like you know focus of the company that really brought that positive selected Potbelly into them yeah that's really interesting should Jane Street replace okmul with rust

**[25:38]** no because there's too much infrastructure already you know camel yeah but starting from scratch so I guess the world is um if they could like Snap their fingers and suddenly replace all their account

**[25:48]** number sure with rust at like zero cost yeah like would it be worth it yeah um in that case I would say yes because I think that you get a lot of the sort of static typing and compile time safety in

**[26:00]** rest that you get from Oak Hamel but the base level program that you can write in Rust is much much faster than one you can write no camel because of the way all camel's design where there's this kind of automatic

**[26:14]** garbage collection the worst thing you can do in high-speed Finance is do any memory allocation that results in garbage collection and so you have to write very very careful oh camel it almost ends up

**[26:27]** looking like C in order to end up you know staying in functional programming land but not actually creating tons of memory on the Heap or the stack that ends up getting collected later

**[26:37]** I guess you've been playing around with the rush a lot recently right yeah what is your impression of the language have you been enjoying it it's great and it's come a very long way in the last three to five years and I think crypto has

**[26:50]** something to do with that it seems to be like one of the like languages of choice for people to write like blockchains and smart contracts and so there's been enormous amount of like open source uh contribution to rust

**[27:02]** and so comparison when I had like last looked at it a couple years ago it's a lot easier to write like really good sophisticated uh programs now in Rust and get all of like the type safety and the speed that you get which is like

**[27:16]** very comparable to C plus plus on the speed side well when I'm writing programs they're not large code bases with many people contributing so what not used for us it's just like a huge pay and like why is I just want to do

**[27:28]** something very simple why do I have to put like an arc instead of a box instead of an option like just but um I can totally understand if you have something where like billions of dollars are at stake there's definitely a learning

**[27:38]** curve and I think for basic scripting you want to use something like python right um but exactly if you're writing like low latency distributed infrastructure that has to never fail Russ is a pretty

**[27:49]** good choice yeah speaking of Jane Street why does a company pay interns like 16 or 17K a month for their summer internships is the opportunity cost for one of these smart students that high in the summer

**[28:04]** the short answer is yes but the long answer to why I think they do that is you know the starting salary for the top people in not just Finance but in Tech he is sort of in this like low to mid six figures now and you can like debate

**[28:21]** whether you think that's like the appropriate starting salary for a person with like no experience coming out of college or not but just sort of the reality is that the talents pool is extremely competitive from the employer

**[28:30]** side so if you start with that as like a reasonable you know salary plus bonus for an employee I think Jane Street's mentality is these interns who are coming here like they're doing real work it should be paid like a

**[28:42]** full-time employee just like prorated for the time when they're actually here and so that like ends up like checking out to be like the right numbers wait uh on net our interns I mean forget about the salary like are they actually on net

**[28:55]** contributing given that subtracting away the time of the traders who are training them maybe it sort of breaks even if you consider like the time to train them um but it's extremely worthwhile because when those interns come back full time

**[29:09]** and Jane Street hires a significant percentage of its incoming classes from their internship program that they're already trained they're ready to go day one they're almost immediately useful because they've had that like three

**[29:21]** month period where they got trained and only the ones that really liked it and were good come back so it's like rather than wait for them to come on site train people and maybe half of them aren't good

**[29:34]** or at half and don't fit with the culture and you kind of don't know what to do with them the internship program provides like a really good place to get like on-the-job training and then only kind of select on both sides for the

**[29:44]** ones that are the best is there a free rider problem with internships where if like a company like Jane Street puts in the effort to train somebody for three months they might get some of them to work for them but they've also trained

**[29:53]** some people who might work for the competition and like is there some sort of free writer problem there there for sure is which is why the companies have to work as hard as possible to make their experience as good as possible

**[30:07]** which is like it's it's good for the interns you know like when you go to a gene Street like not only do you like learn a lot but like they pay you really well and also like you get to you know visit one of the foreign offices for

**[30:20]** like a week or something also like to have all these like really fun programs where they bring like famous speakers to come to the office and speak to the whole you know intern class and they have you know like parties and all sorts

**[30:30]** of stuff and it it adds to like the experience of thinking like okay this is the place I want to work I don't want to like take my training and go to the competitor I want to come to you yeah I clearly got in the wrong business with

**[30:41]** podcasts why did you pursue um Finance Dev instead of uh trading well why did that appeal more to you yeah so in college I studied computer science

**[30:55]** and math and um I really liked programming but I think I didn't quite know what a career and programming looked like I think the conventional wisdom at least like in 2009 when I was applying for

**[31:09]** internships was like okay I'm gonna sit in the cubicle and like stare at a screen for 16 hours a day I'm gonna be miserable and it's not gonna be a very social job I consider myself like a pretty social person

**[31:19]** and I had a lot of friends who had had these like various internships and quantitative Finance like mostly from the trading side and so when eventually I went to Jane Street as an intern um I had kind of like a hybrid summer

**[31:31]** like doing some Dev stuff and some trading stuff and to me I thought like okay the Traders are much more much closer to like the real action of the company like I want to be a part

**[31:43]** of that and so when I joined jeans street I was hired as a Trader on the ADR desk and I realized like very soon into that that one no like actually the the developers have like just as much if not more impact on the outcome of

**[31:59]** success of the company and two I just like enjoyed it a lot more it was just much more out my alley and my training and so I ended up going that route instead I want to ask about the culture at these sorts of places like uh Citadel

**[32:12]** or Jane Street I mean you spend some time in Silicon Valley and around like traditional sort of like startup scene as well um what is the main difference between Silicon Valley Tech culture versus you

**[32:23]** know Quant uh New York culture sure work at Chicago culture yeah so I have a ton of personal experience like in in the Silicon Valley culture or like a tech culture since I've only really worked at kind of finances like finance places my

**[32:36]** whole life but the sense I get is that they're kind of New York Chicago want Finance Dev culture is one about stream pragmatism like you know what the outcome is it's like you know be the most profitable at

**[32:52]** the strategy and you kind of try to draw a straight line between what you're doing and that profitability as fast as you can compare it to I think the Silicon Valley culture is

**[33:03]** much more about like creativity and doing things that are like new that no one else has done before healthy amount of cross-pollination will be good for both where I think a lot of trading firms are doing like the exact

**[33:18]** same things that all the other trading firms are done and some like healthy you know injection of creativity into some of that stuff to maybe think slightly outside the box of like you know as you said earlier like get slightly faster to

**[33:30]** go to NASDAQ or something which is like okay that's probably fine but it's like not not that creative um would be good for those plot firms at the same time they're like sheer approach to pragmatically getting

**[33:42]** something done and out there and sold and making money would help a lot of Silicon Valley firms that kind of like hang out in this sort of creative land for too long and don't end up getting a product to Market yeah I know it

**[33:53]** definitely it seems like there should be one founder from both those cultures of every single startup it's similar to what you were saying earlier with like SPF and like Visionaries versus pragmatist in that context

**[34:04]** um how conspicuous I mean you were just mentioning earlier that these Traders are making mid six figure salaries to begin with let alone where they arise over their careers how conspicuous is their spending and lifestyle is it close

**[34:18]** to Wolf of Wall Street is it just a Walmart t-shirt it's like where where are we talking uh it's not a lot closer to Walmart t-shirts than it is off of Wall Street um I mean certainly it is now even when

**[34:29]** I started it was pretty inconspicuous I don't think it was that way in like the previous decade or two before I joined Finance I guess I'm not really sure but I get the sense that the current culture around inconspicuous consumption is sort

**[34:44]** of a function of millennial consumption habits where you know people are focusing a lot more on like experiences than you know having shiny material objects I think that's had a lot large effect on

**[34:57]** kind of like the high earning Tech and finance culture that exists today well I guess are they spending that much money on experiences either because how expensive is a flight to Hawaii right and

**[35:09]** um even after you subtract that like where is this money going are they just saving it maybe it's not like just a flight to Hawaii but it's like bring your 10 friends to Hawaii with you or something or it's uh

**[35:22]** you know get involved in like a charitable organization in a way that like someone who is 24 like normally wouldn't be able to do surely by able to being able to like donate a lot yeah what is the

**[35:35]** social consequence for lack of a better word of having a bunch of young nerdy people often male often single having this extraordinary level of wealth like what impact does it have I don't know if a society is right word like what is it

**[35:51]** what is the broader impact of that that class of people I think we'll have to play this out over the next decade or two to really see where this goes if I'm going to be an optimist about this I'd like to think that

**[36:05]** when it was like older you know single or married males you know getting you know hoarding a large amount of wealth that for the most part they captions themselves and kind of wait until later in life to do anything

**[36:19]** with it and we're the kind of people who really like stated their same career their whole lives as opposed to if younger and younger Generations are amassing wealth through you know the what what they can actually perform with

**[36:33]** their skills then I think that hopefully injects more dynamism into the distribution of that wealth later on because those Millennials will then like or gen Z or whoever will go on to like found new companies and maybe they'll

**[36:45]** you they'll be able to see the company themselves their own money and have a lot easier time like bringing like interesting new things to Market or they'll be able to donate to like really interesting causes or they'll be able to

**[36:56]** you know help out their friends and family more easily from a young age or they'll be more selective in the kinds of things that they you know give to you or contribute to that don't just involve like getting their name on like a

**[37:07]** building of a school or something yeah yeah that's a very optimistic story I hope that's the way it plays out um to tell me about the psychology of being a Quant or a Trader or a developer in that space because you're responsible

**[37:22]** like one wrong keystroke and you're you've lost millions of dollars you know one bug in your code and there are you know historical cases of this like where entire firms go down because of a bug like what is the sort of like day-to-day

**[37:35]** psychological impact of that kind of uh responsibility maybe the the job selects for the people who don't kind of crumble under the like theoretical stress of that job but personally like I don't lose sleep

**[37:49]** overnight at night over that because within any like mature financial institution like a trading firm there are typically like many layers of safeguards in place like you know limits on like how many dollars you can trade

**[38:05]** in a minute and how much you can trade overall or for your desk or like how many messages you can send to The Exchange and then there's like limits on like the individual Trader and guest level and firm level and there's like

**[38:16]** layers of different checks often there are actual rules like regulatory rules to comply with a market access checks like you know Fender has like 15 c35 and so when you're writing new code it's not like a completely like Blank Slate thing

**[38:30]** where you're connecting directly to an exchange like hoping for the best usually you're embedding some piece of code within some very large established framework where the goal is to make something Trader

**[38:40]** proof no matter what some Trader clicks on or does or configures with their system there's like a limit to how uh how bad they can actually go um and so especially in my particular role as a developer

**[38:54]** like actually being able to understand the technological stack and say like oh I can tell and can sort of you know verify that like these particular safeguards in place and it is like actually as Trader proof as I think it

**[39:06]** is like I sort of I can sleep at night knowing like nothing too bad is going to happen I mean the times I actually lose sleep are like you know uh a Trader in like London or Hong Kong calls me like the middle of the night to say like hey

**[39:18]** uh can you explain how this thing works I need your help like those are the times where like I actually lose sleep but it's not over like being concerned about risk yeah uh that's interesting if you asked the people who work in

**[39:30]** these firms what is the social value you're creating separate from the question of what the correct answer to that question is what would the majority of them say that like I'm doing something really valuable

**[39:42]** with them would they say like um it's like I'm indifferent to it but it's earning me a lot of money like how what is what is their understanding of value they're creating it really depends on the company and it

**[39:53]** depends how diffuse the culture is at like older firms that have like um you know sort of fewer people impacting the culture on any significant way I I think you might not get a clear answer on this

**[40:08]** I think for a place like Jane Street where you know the firm is really run by like 30 or so you know partners and Senior employees who have like been there for a really long time and have carried

**[40:21]** through the core culture of that company up to the present day and with that like large number of people at the top in a very flat environment have actually been able to like propagate that culture and maintain it throughout the company I

**[40:35]** think you'll find a much more kind of homogeneous view on their social value which I think they would say is that they provide like the best like pricing and access to markets that are critical for

**[40:49]** facilitating a capital allocation throughout the world and allow people to very efficiently invest in vehicles that are Global in nature that seems very abstract and while while like it it is probably very well correct

**[41:05]** and is very valuable for society it might not seem that like tangible to somebody who's working in that space is there some technique that these firms have of this making visceral the impact these

**[41:17]** Traders have I don't know do they do they bring out some like child who benefited from efficient markets or something I think well it's probably not like children I think it's more like anecdotes about like the pension

**[41:30]** like fund behind this like state government like needed to get exposure to you know some Diversified asset class and came to one of these companies and said like we want to move like a five billion dollar portfolio can you help us

**[41:46]** do it in an efficient way and it ends up saving them like significant numbers of like percents or basis points over what would happen if like they went to the market and you can say well like there's like a direct connection between like

**[41:59]** the price that someone like James Street gives them and the amount of money that they ultimately get to save and ultimately pass on to the people in their state who are part of their pension plan and so like there's like a

**[42:09]** direct connection there okay let's start by addressing the elephant in the room which is FTX let's begin uh at Jane Street which is where you met SBF can you tell us sort of the origin story of how you first met him and what your

**[42:25]** first impressions were yeah absolutely so I was at Jane Street from 2010 to 2018 in uh Sam was at Jane Street for a couple years in the middle of that I think 2013 to 2017. and one of the things I did at Jane Street was I

**[42:38]** started this program called oh camel boot camp it was a yearly course for the new Trader hires to spend four weeks with me learning programming uh in in ocamo which was like the esoteric programming language that we used at

**[42:53]** Jane Street along with a lot of our other proprietary systems and Sam was in our was in one of the first cohorts of students uh and so I got to meet him through that experience got it okay and what was your impression of him

**[43:05]** yeah he was a smart kid he was nice uh he kind of got along well with other people in his class you know he was definitely you know above average but not like you know completely stand out at the top although then again the bar

**[43:18]** was extremely high at Jane Street so I think that's already sort of a compliment but uh yeah but you know people liked him a lot and thought he had a lot of promise but you know he was a young guy like everyone else got it

**[43:29]** and did that perception change over time while you were at Jane Street uh it slowly started to you know um Sam was on one of the largest trading desks at Jane Street uh and you know had 50 or 60 people on it he had several

**[43:43]** managers and one of my roles at Jane Street was to work with all of the different trading desks on the designs of their particular strategies and systems and so I would frequently go over to his desk and talk with his

**[43:55]** managers about stuff and they started pulling him into conversations more and more uh specifically to talk about some of the like lower latency etfr stuff we were doing some of of the original like OTC automation things we were working on

**[44:09]** and so he started actually contributing more to the actual like design and thought behind some of these systems and thought he was you know precocious and had a lot of really good intuitions about markets got it okay

**[44:19]** um and so what exactly was Euro LED Jane Street at this time and what was his yeah so at this time I was sort of leading the group of software developers building the technology that was closest to actual trading you can think in a hft

**[44:33]** or any kind of sort of trading firm there's lots of different developers people who work on you know stuff really relating specifically to the trading technology people who work on kind of the core systems networking kind of

**[44:46]** internal automation tools tools for developers so we were in the part of the spectrum that was closest to actual trading and so my job was to like go over to different trading desks within the company talk to them about their

**[44:55]** specific strategy for the products they traded understand how to like their priorities about what venues they want to connect to what different systems they want to create what different parameter changes they need in their

**[45:06]** like automated trading systems what kind of research tools will help them do their job better what user interface would make it easier for them to understand what's going on in the market and kind of all of that okay and did svf

**[45:17]** at this point have any sort of reputation of either being uncooperative or being cooperative or anything ethical or professional that's not worthy of this time I don't think

**[45:29]** there was much that stood out although you know he was again you know pretty either precocious at that particular time period one anecdote that sort of Drew me closer to him was Jane Street's offices were in 250 vesi uh they still

**[45:42]** are in New York City and there's a big food cart on like the second floor and so I once went down to meet with a development person from a uh a non-profit that works in animal welfare and something that my wife and I had

**[45:55]** donated to for a long time and I met with this guy and he said you know you're the second person I met from Jane Street today which was wild because entry was like only a couple hundred people there it's just like a pretty

**[46:04]** Niche you know organization and I was like that's crazy you know who did you meet and they said oh you know Sam bankman freed and I was like you know Sam I just came down from talking with him upstairs and so I went back and we

**[46:17]** sort of realized we had this kind of shared interest in helping kind of animal welfare causes we were both you know vegans uh and we sort of bonded over that that's how we kind of became friendly got it and

**[46:29]** it was so it seems then his interest in effective altruism was genuine at this point and early on it was there was a history of this yeah you know it wasn't like EA was super popular at Jane Street I feel like that's a bit of like recent

**[46:43]** sampling bias among this like younger crew of uh Jane streeters there definitely I think it was because of a lot of Association prior to joining Jane Street uh that the sort of were into effective altruism but there were a

**[46:56]** couple people there who really were fairly vocal about the fact that they were you know donating the majority of their yearly salary and bonus to charitable causes and Sam was one of them and uh and yeah started to become

**[47:08]** known for that got it okay so I guess fast forward to uh he's no longer a James Street you're no longer at Jane Street and you're at Citadel he started FTX actually before we go there were you in contact with him up

**[47:23]** until the point where you had started talking about a potential yeah off and on uh you know when when I first left Jane Street and he left sorry yeah we both left Jane Street around around the same time him before

**[47:35]** me you know he had told everyone at Jane Street that he was leaving to join the senator for Effective altruism full-time and I guess he did that I'm not sure you know if it actually happened because he very soon after started this trading

**[47:46]** firm and tried to pull lots of James free people to join him to do this trading firm which didn't make people super happy uh but it was funny he we had a phone call and he told me that it wasn't really going super well

**[47:58]** um he said it was really great in the beginning like they made a lot of money they had this Arbitrage trade and then a few things kind of went by the wayside and you know they had taken out these huge loans to be able to get their

**[48:09]** initial capital for Alameda and also there was a big fracture within the company you know half the company split people left he really didn't tell me much about that at the time and he said he's probably gonna do something else

**[48:21]** and when I asked him he said I think I'm going to work on like political prediction markets and I was like okay it doesn't sound super exciting to me I'm going to continue on with what I was doing which

**[48:31]** was moving to Chicago taking a new role but then fast forward I guess that idea maybe he wasn't telling me the whole truth at the time but I guess that idea became FTX and he had supposedly like resuscitated Alameda in the process yeah

**[48:44]** yeah that's really interesting do you have some sense of what it was that went sideways so I pieced together some details over the years because he told me a little bit more after I first joined I heard a

**[48:58]** little bit more later from other people then saw some reporting kind of post FDX collapse I think there were two things um one was the infrastructure they had built I think was really poor in the beginning a

**[49:10]** lot of like Python scripts like slapped together and a couple times they had sent tokens to the wrong wallet and ended up like losing millions in the process and they had some big non-arbitrage directional bet on in some

**[49:25]** token it might have been eth or something and it went against them and so they lost a lot of their trading capital and then the other thing was that after some of their technical problems there was internal

**[49:37]** disagreements supposedly this is what Sam told me about how to move forward with tech you know there was half the crew that wanted to kind of rewrite everything from scratch in a different programming language there's another

**[49:49]** half that said like okay we can make some small incremental changes from here and fix things up and Sam and Gary and ashad were more in that ladder crew that former crew kind of broke off and started their own thing and that's what

**[50:01]** originally happened okay got it and were you aware of the extent of this at the time or you know something not at all I mean Sam told me a little bit about it but this was over the course of you know years

**[50:13]** now where I had two different roles one at Headlands one at Citadel Securities Sam was starting Alameda we spoke maybe once a year briefly on the phone um so all this stuff was happening in the background and I had no clue like

**[50:27]** the first time I even heard about FTX was one of my colleagues from Citadel security has told me hey do you did you ever work with this like sandbagman freed guy and I was like yeah a little bit why and they're like

**[50:37]** do you know he's like a billionaire and he has this like Hong Kong crypto exchange like what no what since when and then start to see him Pop Up In Articles there was like a Vox article about him

**[50:50]** and a few other things especially related to his political donations and that's kind of when I got back in touch with him we started talking a little bit when was it that he called you to say that there's potentially troubles and

**[51:01]** I'm considering starting a political prediction Market that was in 2018. okay yeah uh so I it was right after I left Jane Street got it okay and so now you've moved on to Citadel and so you I guess you're still in touch at this

**[51:16]** point yeah like very briefly you know a text every now and then okay and then at some point you're uh you become president of FTX UI so do you um do you want to talk about like I guess how he approached you about that

**[51:31]** and what was going on at the time yeah it was it was interesting so at the time I was uh running what was called the semi-systematic trading technology at Citadel Securities and so this was the group of technologists working on

**[51:45]** systems for adrs ETFs options and OTC market equities so it's around 100 software Engineers or so that rolled up to me and you know that was going well um but you know Sam and I started talking it was I guess March of 2021

**[52:01]** and you know he was like telling me a couple things going on at FTX and then he said you know if you're interested in coming over to FTX we would still love to have you

**[52:12]** and I thought still if we never never talked about doing this before but sure like once I entertain this and then we started talking and he had me meet him and Gary and nashad uh Over You Know video call I was in Chicago they were in

**[52:26]** Hong Kong at the time these calls were taking place like late at night my time and very quickly like an offer came together and I thought you know this is like a really cool opportunity to jump into a field and pick a role that was

**[52:39]** very different from stuff I've done in the past and I signed up got it okay um and what what where was FTX at this point in terms of its sort of Business Development yeah so FTX was doing quite well I mean it was basically finished

**[52:54]** its first its second year operation and it was maybe the fourth or fifth largest Exchange in the world by volume if you include you know crypto spot crypto and crypto derivatives and it was also one of the primary

**[53:10]** destinations for institutions you know proprietary trading firms hedge funds to trade crypto and derivatives especially because of how it was designed and so it was doing really well fjx us was virtually non-existent you

**[53:26]** know they had started the they formed the entities they had started the exchange I think in either December 2020 or January 2021 uh but it had like de minimis volume compared to the other you know exchanges around the world

**[53:39]** especially in the US too and you know Sam talked to me a lot about a lot of the aspirations for the US business you know it wanted to grow the spot exchange of course uh two was to be able to find a regulated path for bringing some of

**[53:53]** these offshore products like you know Bitcoin and ether Futures and options onshore in a regulated way and on top of that Sam had also told me about kind of longer term desires to be a single app or Marketplace for

**[54:09]** everything not just crypto so be you know just launching a stocks trading platform as well and so that was like one of the reasons I think he wanted to bring me on was because I had all this experience kind of inside of regulated

**[54:19]** broker dealers and sort of knew roughly what it took to get that started okay got it and so he and the initial offer was specifically for uh president of FTX us right yeah and Sam wasn't someone who loved thinking hard about titles and

**[54:35]** even like what my original title is going to be was like a point of contention but I'm not sure it was clear exactly what my role was going to be I think Sam wanted me to like write software for FTX and FTX us sorry for

**[54:48]** FTX us but to me I sort of thought there was like this bigger opportunity to kind of kind of work with Sam to lead this other startup which was ftxus and kind of build it up and sort of file in ftx's

**[55:01]** footsteps and its success and that was the part that was most exciting to me because this is what I've been doing now for years is like managing large teams of people thinking about strategy getting people together you know

**[55:11]** occasionally doing some software development myself but you know that was the primary reason for wanting to join got it got it and what was the relationship between FTX and ftxus at that time where they kind of

**[55:23]** subsidiaries where they separate entities they were separate entities they weren't subsidiaries there was technology sharing between them so like the FTX US exchange technology was like licensed from FTX you can think of

**[55:36]** ftxtus was like FTX stripping away like most of the interesting parts of FTX right because it was just you know a dozen or two spot tokens and when I joined there were very few people within FTX us you know maybe like two or three

**[55:50]** dedicated people so over the course of the next year or so you know my job that I sort of you know fit for myself was to like open up some offices like hire a bunch of people establish

**[56:02]** like separate compliance and legal and operational and support teams start to build out these regulated entities with Chicago the initial base of that operation yeah I mean for selfish reasons

**[56:15]** my family is here you know and uh you know I wasn't going anywhere but also I thought Chicago was a great place for FTX us because if our main goal was to establish you know regulated derivatives like Chicago is really the place where

**[56:29]** that happens we have like the CME uh we have many of the top proprietary trading firms a lot of like the Futures commission merchants and various Brokers are all here you know historically like the kind of the floor of like the

**[56:43]** Chicago Board of Trade and like the the Chicago Mercantile Exchange like they're here and so it kind of felt like a good place to be and at this point I I guess before you joined did you get a chance to ask him about the

**[56:58]** relationship between FTX and Alameda yeah I did I mean it it was definitely of interest to me like you know because I mean for the primary reason being that I wasn't interested in doing prop again you know like I I worked at James trade

**[57:12]** I worked at Headlands Tech outside Studio Securities if I wanted to continue doing prop Trading I would have stayed at one of those places you know so I I wanted to do this exchange

**[57:24]** business and what Sam told me it was the same thing he said publicly everywhere which is that yeah like Alameda is basically running itself all of Sam's times on FTX they're kind of Walled off from the FTX people and you know their

**[57:37]** access to the exchange is just like any other Market maker like there's like the public API feeds you know there's you know benefits from market makers that trade enough volume but it's not like you know Alameda had any special

**[57:48]** privileges in that sense and so I thought they were just basically separate and did you ask to I guess audit their sort of financials or this relationship before you joined no I mean I don't know about you but I've never

**[58:02]** like gotten an offer to a company and said like before I signed I'm sure you show me your audited finances and just like not a thing that happens right right okay um fair enough so you join FTX and then

**[58:15]** you mentioned some of the stuff you were working on the operational illegal um getting the organization set up but yeah feel free to talk in more detail about what were the things that came up during your tenure and what are the

**[58:27]** accomplishments you're you know proud of yeah I guess on a the professional and personal front so I guess on a professional front I'm you know most proud of like establishing out our team and making significant Headway

**[58:39]** to a lot of our goals to establish these regulated businesses so for example Ledger X you know we acquire Ledger X and we had this application to the cftc to enable kind of real-time direct to customer 24 7 margining and

**[58:54]** cross-coateralization and it was an extremely Innovative proposal and it felt like we were making real progress towards establishing like new and very exciting regimes for you know cfpc regulated

**[59:08]** derivatives in the U.S I also established a broker dealer in the U.S for the purposes of letting people trade stocks like similar to Robin Hood I wrote like 90 of all the code for that stocks platform myself

**[59:23]** um and yeah I was very proud of that accomplishment and then it was on a personal front I it was great to get embedded into the crypto industry I was very excited by everything that I saw it was great to make all the connections

**[59:35]** you know through FTX with like the different people in the crypto ecosystem and you know become friends with these people and that certainly has an influence where I am today um so I'm so proud of all of that how

**[59:48]** did you manage the management of I don't know how big the team was I to speak and it sounds like you were heavily I mean involved as an understatement in the actual engineering how we were able to manage both roles at the same time yeah

**[1:00:01]** so we were like between 75 and 100 total people in the US and it was challenging it was one of my biggest complaints which I'm sure we'll get into which was that you know yes I can write code but I feel like that's my comparative

**[1:00:15]** advantage is helping kind of to leverage teams of people to get them to you know work towards the common goal of building out large distributed systems that are you know complex and multivariate nature and

**[1:00:30]** the best use of my time was not you know me programming between the hours of like 10 p.m and 2 A.M every night while trying to keep on board with like what all the Personnel were doing yeah so I really wanted to grow the US team

**[1:00:43]** significantly to at least be you know more than a handful of like developers uh and so yeah that was one of the initial points of contention okay so speak more about that so he was opposed to Growing the team Sam would frequently

**[1:00:58]** talk publicly about how proud he was that all of FTX was built by two developers and all of these crazy organizations that hire thousands of developers and can't get anything done like they should learn from me about how

**[1:01:12]** like a small lean team can be you know much more effective and there's some truth to that you know I do think the conventional wisdom now is a lot of big tech companies over hired for software engineers and Not only was it

**[1:01:28]** sort of an expense on the balance sheet but it was also expensive in terms of slowing down the kind of operational efficiency of the organization and having a small lean team can help you get to your you know your first or your

**[1:01:39]** nth product a lot more quickly that's great for a startup but once you're like uh north of 10 billion dollar valuation company like promising the world to like customers and investors

**[1:01:54]** too software developers doesn't really cut it anymore I mean at some point you have to like you know grow up and and face the reality that it's time to actually grow an organization into a real kind of managed Enterprise with

**[1:02:08]** teams of software Engineers specializing in certain tasks and so there was always pushback you know people will tell me like look we're not trying to be like Jane Street or Citadel in terms of our number of software

**[1:02:20]** Engineers like we want to stay lean that's our comparative advantage and most importantly they didn't want two separate development teams like one in the U.S one and then the Bahamas like they wanted to keep the Nexus of

**[1:02:34]** software development underneath you know nashad and Gary in the Bahamas which I just thought wasn't going to be sustainable long term like if you run a broker dealer in the U.S you need to have staff that is specifically

**[1:02:46]** allocated towards broker-dealer activities it can't be that if you so finra comes and says like well who's working on the broker dealer you say well it's like this Gary guy who like lives in the Bahamas who sometimes awake

**[1:02:58]** at like 4am haven't spends 20 minutes a day thinking about stocks like that can't fly right right and has no images of him yeah um okay so uh we're so where nashad and Gary contributing code to the FTX us

**[1:03:13]** code base remember like FTX U.S side of things was I was like strict subset of FTX so like in that sense it kind of flowed into FTX us with the exception of the like FTX us derivatives The Ledger X stuff was like actually a completely

**[1:03:30]** separate team because that was through an acquisition when you're talking about the code of like the matching engine or things like that was the code shared between FTX and FTX us yes okay that who like who was in charge of ultimately

**[1:03:43]** like the the push uh the poor work like approving the pull request basically of the xpx US code base yeah I was like all Gary and nashad okay got it and so the coach you were contributing was also going to the sort of like Universal

**[1:03:56]** Global code base yeah got it did you have sort of access to um the entire code base or just the FTX us side or yeah again it was one share of repo I mean there was an enormous amount of code and one of the big

**[1:04:10]** problems another problem that I raised while I was there was that you know 90 plus percent of all the code of FTX was written by these two people and it was very hard to follow I don't know if you've ever seen like a large python

**[1:04:25]** code base before and so whenever there were issues that arose you know oh like there's like this particular problem with like an account on the exchange the only answer was like call the shot call Gary

**[1:04:38]** which I also knew to be like unsustainable from the organizational perspective like one of the like guiding principles at James tree for example was you know Mentor your Junior Dev so that you can hand off all your

**[1:04:50]** responsibilities to them and the process of handing off responsibilities you make the code better more automated more robust problems more easily you know debuggable in real time if you hoard everything to yourself in your own brain

**[1:05:04]** it's you end up with a code base that is just only understandable by that one person and so it was the kind of thing where a lot of people talked about this internally like if if Gary like got hit

**[1:05:15]** by a bus and like couldn't come to work anymore it's done exactly exactly so what do you think was the motivation um behind this was it just that he wanted to he wanted to avoid as a sort

**[1:05:29]** of like Google growing to a hundred thousand people kind of thing or was there something else going on like why did it why why this sort of concentration clearly there was something else going on

**[1:05:38]** um I think an open question now only thinking about this in hindsight was how much of this like very oystered organizational decision around the

**[1:05:52]** development team was a function of the various things they were doing that they were hiding from the rest of the company or was it really this sort of like one Ultra paranoia about growing

**[1:06:05]** too large too quickly and getting losing control of the organization and two uh and almost like sort of cult-like belief in this small team like being the butt for cause of all past present and future success

**[1:06:23]** what was the discretion that you had at FTX us it sounds like you weren't even given the capacity to like hire more Engineers if you wanted to right what was the things you did what were the things you did control yeah hiring for

**[1:06:36]** example like I began pushed for many months that we should hire more people eventually I you know got permission for us to interview people but then those would ultimately have to get finally approved by the people in the Bahamas

**[1:06:49]** and they would frequently say no to people who I you know thought were good candidates finally we hired one person and this person was doing well he was here in Chicago and they invited him to go spend like a

**[1:07:04]** month in the Bahamas to kind of hang out with them and you know supposedly just like ramp up on the system and this person comes back to Chicago and they say you know what like I really want to move to the Bahamas they really kind of

**[1:07:14]** convinced me to do it and it was so frustrating right I was just posting from your own company exactly it was such a constant battle and at some point I kind of gave up on this idea that I was going to be able to actually grow

**[1:07:26]** the separate developer team so I mean the bottom line is you know I I'm kind of like the day-to-day operational stuff um especially the decisions within some of the things I was responsible for like

**[1:07:38]** the stocks uh you know creating platform that I was working on you know I had a fair amount of discretion and people certainly looked up to me for you know management and advice and Direction but ultimately the discretion ended up with

**[1:07:56]** this small group in the Bahamas who not only you know had final say on decisions but would often make decisions and not communicate with the senior people on the U.S side and we would just sort of find out things were happening is there

**[1:08:11]** a specific example or set of examples that comes to mind sure you know I the biggest example for me was this just sort of posts my kind of effective resignation but some of these strategic Acquisitions that were being done in the

**[1:08:24]** U.S during the summer of 2022 I would find out from like the news or or like it would sort of be mentioned on a signal chat or something that this was happening and there was like no opportunity to actually like wade into

**[1:08:39]** the discussion about how this is like gonna greatly affect like the US business it's gonna greatly affect our priorities and it wasn't clear if this was like a good decision or a bad decision it was like a unilateral

**[1:08:50]** decision that was made like oh this cup we're acquiring this company or where we had the option to acquire this company are there decisions that were made from the Bahamas that stick out to you as being

**[1:09:02]** unwise uh that like I don't know you try to speak out against um I I mean you mentioned some of them right like not hiring enough people and uh not getting more yeah not getting more developers but are there other

**[1:09:13]** things like that that stick out to you as bad decisions a lot of the spending I mean on everything from like lavish real estate to all of these like Partnerships to like very very large Venture deals like these were the kinds

**[1:09:31]** of things in the company where people asked like when does it stop like to one end are we doing a lot of these things and you know some of those resulted in sort of like direct confrontations like just you know

**[1:09:43]** why are we doing yet another deal with like a sports person or a celebrity this is like this is ridiculous like it's not doing anything for the company and we're completely distracting from the role

**[1:09:54]** that we thought we all had which is to build a really great core product for you know people trading crypto and crypto derivatives yeah and did you bring this up directly with SPF yeah multiple times and how would he respond

**[1:10:06]** sometimes he was you know nice about it and he would say you know like yeah like I see where you're coming from I do think what we've done so far has been really valuable and we probably should do some more of

**[1:10:18]** it but maybe at some point we should stop you know a lot of this sort of like hedging language that was ultimately non-confrontational non-committal I mean he was a very non-confrontational person very conflict avoidant person within the

**[1:10:29]** company so and then at worst it was just you know there were other times where I brought up like specific things that I thought like he was doing wrong there was one really unfortunate time where I

**[1:10:41]** it was the first time I visited the Bahamas uh in it was like November of 21. and I'm the kind of person who like if I see something wrong in a company it doesn't

**[1:10:51]** matter what company I worked at or how junior or senior I've been like I like to go to the person most senior in charge and tell them like this thing seems wrong to me and that's I feel like is one of my superpowers uh I'm just

**[1:11:02]** like not being afraid of just like saying when something seems wrong to me and sometimes like I'm just totally wrong and don't understand the full picture and sometimes it results in something better happening and people

**[1:11:12]** will you know thank me for having been honest and bringing to attention something that's actually wrong uh and so I said to Sam you know I think you're doing way too much PR and media like

**[1:11:25]** first of all it's really diluting you and the FTX brand to constantly be doing PT interviews and podcasts and you know flying to Banking and private Equity conferences and you know it was so much

**[1:11:44]** time spent on this stuff and also it was completely taken away from the management of the company you know people would sometimes say I'm a slack or signal messages and not get responses for weeks at a time

**[1:11:55]** and it felt like he was spending virtually no time helping the company move forward it was so much about image and brand and PR and he was really angry at hearing this criticism directly how did he react I

**[1:12:10]** mean he was just he was sort of emotional he was worked up he told me like I got completely disagree with you I mean he said like I think you're completely wrong he said I

**[1:12:21]** think the stuff that I've done for PR is maybe the greatest thing that's happened to this company I should do more of it I didn't think it was physically possible to do more of it um and

**[1:12:31]** it I realized at that moment that this was not really going to work super well long term like if we're not in a relationship where I can give sort of my direct Superior like real honest you know constructive criticism

**[1:12:45]** um that I thought was for the good of the company that this wasn't really going to work he actually did my podcast about I don't know eight months ago or something and while I was like very grateful he did it

**[1:12:55]** even at the time I'm like I don't know if I would have agreed to this if I was in charge of a 30 billion dollar Empire uh yeah but sometimes like some reporters would say to me like you know do you can you like get me in touch

**[1:13:10]** with Sam and I would say you know why like I'm not really his keeper you could contact him yourself um they're like oh because we want to come to Bahamas and do a special on him and I would say like okay you're gonna

**[1:13:20]** be like the sixth one this month there's an exclusives here so I guess to steal a man his point he did get a lot of good PR at the time right potentially well not potentially like actually

**[1:13:35]** um uh too much and in a way that like really created a at the time sort of like the king of crypto sort of image so I mean was he right about the impact of the pr at the time

**[1:13:47]** or maybe maybe yeah let me ask a question different way how did he create this image I mean people were saying that he's the JP Morgan of crypto like you could don't do no wrong even things that in retrospect seem like clear

**[1:13:59]** mistakes like only having a few developers on the team universally praised you know huge Empire run by a few developers how how was this image created I think that media was primed for

**[1:14:13]** the archetype that was Sam this sort of young upstart Prodigy in the realm of fintech you know we have a lot of these characters in the the world of you know big Tech and I

**[1:14:29]** think that he had a particular role to play in the world of finance and by making himself so accessible all the time he gave people a drug that they were addicted to which was like that constant

**[1:14:43]** access I feel like any time of day or night someone could text Sam and get him on the phone with them if they were in media and they loved it it was like getting access to a direct expert who was also this famous person who was also

**[1:14:58]** this billionaire who was also this extremely well connected person who was also this um very insightful person who knew a lot was going on in the industry and can give them like insight and tips

**[1:15:09]** and I think there was some amount of well I like to call like reputation laundering going on here where it was like okay so you get the famous celebrity to endorse Sam which makes you know this

**[1:15:24]** you know politician think highly of Sam because they also like that celebrity and then also the investors are writing really great positive things online about it but also the media is enforcing how cool it is that Sam is doing all

**[1:15:37]** these other things and it all sort of fed into this like flywheel of building up Sam's image over time in a way that didn't necessarily need to like match the the underlying reality of who he was at the company and what was

**[1:15:52]** the reaction of other employees at FTX of this sort of not only the media hype train but also the amount of time Sam was spending with the media you know on one hand I think people were growing frustrated within the company

**[1:16:07]** because of the lack of Direction and some of like the power vacuums that resulted from Sam's continual absence on the other hand so many people within the company just hero worship Sam you know when you hear all like the

**[1:16:23]** really tragic stories now of all the employees who kept all of their like funds and life savings on FTX they really really believed in Sam and doesn't matter how little time you spent with the company it doesn't matter

**[1:16:38]** how he treated employees internally it was like he was this sort of Genius Pioneer and that image couldn't be shaken and I certainly don't blame anybody for it I I interviewed him I try to do a lot of research before I

**[1:16:52]** interview him and I certainly was like totally taken with this right I thought he was the most competent person who would ever grace crypto but so what was he actually like as a manager and leader

**[1:17:04]** um other than I guess obviously the micromanaging aspect of it um or feel free to speak more on that as well but in terms of the decisions he would make in terms of Business Development and prioritizing things can you describe

**[1:17:15]** this sort of management style and leadership in the beginning when I joined FTX my initial Impressions were that he had

**[1:17:26]** pretty clear intuition and insight into the simple things to do that would work you know it in in many ways as you think about what STX did uh it wasn't really super complicated it was like just be

**[1:17:43]** operationally good and give your trading customers as predictable of an experience as possible with regards to Collateral management and Auto Liquidation and matching engine behavior and latency

**[1:18:00]** and so they did it I would say aside from the intuition Sam wasn't a details man like that was usually left up to the people below him to really take care of it's like to drive a project to completion to figure

**[1:18:15]** out all the details that had to be done I think besides that as a leader I I thought he was you know fairly incompetent I thought he was you know very conflict avoidant you know he didn't like to get into direct

**[1:18:28]** confrontation with any of his employees where most of the reasons why people needed to talk to him were because they were you know significant issues you know a lot of those were Personnel or otherwise

**[1:18:40]** and he just blew them off I mean that was a frequent occurrence in the company I mean he was he was if you went to Bahamas and I went to only a couple of times to actually visit the office

**[1:18:52]** he was if he was in the office he was there all day on calls all day whether those were with investors or with media podcasts whatever it was just consistently just doing that and I saw

**[1:19:09]** very very little time where he actually got up and talked to anyone else within the company about anything you know so I think to me that was the primary impression I got of his leadership was virtually that

**[1:19:21]** there was none which you know made me feel a lot like I and others needed to step up and sort of take you know that role in the absence got it and then so who was making these day-to-day decisions in the absence of Sam

**[1:19:34]** on the foreign side and in the Bahamas nishad was really like the number two person there I mean he was making a lot of decisions there were a couple others in the Bahamas who were taking kind of

**[1:19:46]** swaths of the company whether it was like Investments or marketing or legal things like that on the U.S side we had like a different crew trying to make decisions where we could on for like U.S regulated matters uh but again it was

**[1:20:02]** always we were always sort of below the decision-making Authority that was happening in the Bahamas especially inside of the home where they were all living so it seems like FCX was a really good product compared

**[1:20:16]** to other crypto exchanges I've heard a lot of like Traders praise it was this um was this competent sort of built while SPF was still doing Media stuff or was this built before he kind of uh went on the pr rate

**[1:20:31]** and like how was this product built while the CEO was kind of distracted so I think the core of the product was built before my time and my understanding was in the transition from Alameda to FTX where there was no

**[1:20:48]** publicity around Alameda there wasn't any posted around FTX it was very much like heads down build mode for several months and just think think about the core product having been a Trader on these different

**[1:21:01]** exchanges around the world that also offer derivatives and knowing all their problems like for example if you had an ether futurist position and also an ether spot position on just one Exchange

**[1:21:16]** you could get liquidated on your ether Futures position even if you had enough ether spot is collateral because you needed to have that spot crypto within the ether future spot lateral wallet which was different than the ether spot

**[1:21:29]** wallet and so it was this game of Shifting assets around to different wallets to make sure you kept meeting your collateral requirements which was just an operational Nightmare

**[1:21:41]** and so Sam told and worked with you know Gary and Nasha to build basically a cross-collateralization system where you have just one wallet with all of your assets all you know haircutted appropriately

**[1:21:56]** based on volatility and liquidity but then summing up to a single collateral value that represents you know what you can put on in terms of margin for all your positions or having an Auto Liquidation system that doesn't just the

**[1:22:10]** second that you're slightly below your margin fraction send a giant market order into the book and dislocate the you know the order book by ten percent it would automatically start liquidating small

**[1:22:21]** percentages of your portfolio at a time to try to minimize Market impact and then if the position got too underwater it would auction that position off to backstop liquidity providers a number of them who would then take on that

**[1:22:36]** position again without having to kind of rip through the book and cause dislocation and so it was much more orderly it was much more predictable and that had to have come from the initial intuitions that Sam and his

**[1:22:49]** colleagues got from being Traders on these exchanges and thinking how should this work if it were perfect so I do think in the beginning they were really working on that product together and then once the success came

**[1:23:01]** and Sam got you know drunk on the celebrity of of being so you know out there and known and having all these Newfound connections that things are to go by the wayside you mentioned that one of these things

**[1:23:17]** that he was doing was you know making these sort of exorbitant deals and with celebrities with Acquisitions branding what was your understanding at the time of where the money to do this was coming

**[1:23:29]** from yeah so for example when I joined the company the FTX is just Inked that Miami Heat deal and I think it was something like 19

**[1:23:39]** million a year and I was like well that sounds like a lot of money right but at the time you could see the public publicly reported volume on FTX it was something around 15 to 20 billion in notional per day

**[1:23:55]** uh the fee schedule was also public so even at like the the highest volume tiers the you know the take feat would be something like two basis points per trade so if you just did like 20 billion

**[1:24:09]** dollars traded per day times two basis points times 365 which because like crypto trades every single day you can get a sense of how much money FTX was making a year and at the time I think the Run rate for

**[1:24:24]** FTX was something like close to a billion dollars in income and you think okay is 19 million dollars a reasonable percentage of the total income to spend on a very significant

**[1:24:37]** important marketing play I don't know it feels kind of reasonable like how much does Coca-Cola spend per year on marketing of as a percentage of their income it's probably somewhere between like 50

**[1:24:47]** and 130 you know I don't actually know what it is it doesn't seem crazy yeah but if you add on top of that the real estate the other sort of acquisition first of all that stuff came

**[1:24:59]** later um and secondly a lot of that wasn't known to the employees within the company most of the Venture deals the value of

**[1:25:11]** the real estate Etc was non-public within the company there were you know 100 plus million dollar investments into various companies and other investment funds that were never discussed openly at least to the U.S people so like it

**[1:25:27]** wasn't like there was sort of this clear internal accounting where people could look at it and say hey like are you really spending all this money on all this stuff no I think Sam very deliberately kept all that stuff within

**[1:25:39]** like his innermost Circle for a reason because he didn't want the criticism on what he was spending on and did you have access to or did you ask to see I guess a balance sheet or any of the sort of financial documents I had zero access to

**[1:25:53]** like you know bank account stuff or financials on the ftx.com side on the US I had some but you know remember now knowing what we now know about uh even like recent uh like the guilty pleas from the shot and

**[1:26:10]** seeing like the complaints from like the SEC cfdc they were like deliberately falsifying information that went into ultimately the audited financials so in order to like actually

**[1:26:25]** have suspected anything one would have to not only like disagree with all of the kind of internal you know conventional wisdom around how the company was doing but also have to basically distrust

**[1:26:36]** audited financials coming back to the company combined with having any concerns about income when it seemed like we were generating income faster than any startup in history

**[1:26:47]** so I think it was very difficult for anyone within the company especially on the US side to have a clue what was going on sure let's talk about Alameda so I guess again the maybe the best point to start

**[1:27:00]** this story is also with Jane Street um where Caroline Ellison who I went out to become the CEO of Alameda was um was a traitor did you happen to cross paths with her at Jane Street so I it's hard to

**[1:27:16]** remember because it was like the early days but I'm pretty sure she was also one of my boot camp students um it all starts there yeah but um uh but besides those early interactions I barely interacted with Caroline this not

**[1:27:29]** in the same way that I had done with Sam just based on the trading desk he was on and when I joined the company you know the FTX U.S people communication wise were walled off from excuse me from Alameda so we didn't really

**[1:27:44]** cross paths almost at all what was your understanding of the relationship between Alameda and FTX it was this is a completely separate company Sam doesn't really do anything for them

**[1:27:57]** anymore because he is 100 focused on FTX you know it's separately being run by you know Caroline and Sam Trabuco they have the same access to the exchange like data feeds and API as any other Market maker on the exchange and also

**[1:28:13]** you know especially towards the time that I left uh that Alameda wasn't even a significant percentage of the exchange volume anymore you know they weren't in like the top 20 market

**[1:28:22]** makers on ftx.com or something like that yeah you mentioned that you had you were contributing to the code base and you had access to the code base it's people have been speculating about whether Gary or nashad had hard-coded

**[1:28:34]** some sort of special limit for Alameda did you see any evidence of that in the code base or I mean definitely not you mentioned that you visited the Bahamas offices a few times and there um like the Alameda there's like four huts

**[1:28:50]** and there's there's like a meeting room there's where Sam and the engineers are um there's the future fund and then there's like the Alameda Hut yeah did the physical proximity between the offices and of course the fact that the

**[1:29:05]** leaders were living together uh was that something you like inquired about or concerned with I never visited the places where they lived in that Albany section of of the Bahamas so I think I didn't fully grasp the extent to

**[1:29:21]** which they were all like living in this particular Arrangement but I understood that you know as long as Sam was going to be the 90 you know owner or something of Alameda he would want oversight there

**[1:29:36]** and so having them close by made sense but the actual Hut set up was such it had like physical separation from minute to minute so it wasn't like Alameda could overhear stuff happening on the exchange or

**[1:29:48]** people in The Exchange could overhear stuff that was happening at Alameda so just to some extent I felt like well at least they're you know going through the right motions of setting up like physical separate buildings I mean also

**[1:29:57]** this is not uncommon Within like trading firms and investment Banks right like if you imagine there needs to be wall separation between like buy side and sell side at you know different institutions and the way they do that is

**[1:30:11]** they put them like on different floors in the same building right and sure like they can meet each other for lunch in the lobby but like they they set up some actual physical separation this is like super par for the course when it comes

**[1:30:22]** to financial firms that have these businesses that need to be you know walled off from each other and so that didn't seem like uh a particularly strange thing to me at all were there is there anything that in retrospect seems

**[1:30:34]** to you like a yellow flag or a red flag even if at the time it's something that might make sense in the grand scheme of things yeah the most obvious thing only in hindsight was that Sam liked to do uh bonuses for the

**[1:30:53]** employees twice a year and you know once the end of June once the end of December so there were like semester bonuses and in the previous semesters he had paid them like early like you know in May for the first semester in November or just

**[1:31:06]** early December for the second one and he was extremely late in doing the mid-year 2021 uh 2022 bonuses so much so that people within the company started to freak out because there was a lot of bad news in

**[1:31:23]** the Press about other companies doing layoffs or folding and it was you know two to three months late and people were like expecting to get bonuses to pay rent and you know do whatever and this was just there's very little

**[1:31:37]** communication around this and people were very concerned so at the time you know people said look Sam's like really busy he's flying to DC every week he has all this stuff going on like he just hasn't gotten around to

**[1:31:51]** it but don't worry it's coming in hindsight I felt like there was some clear you know liquidity issues you know that was probably the most obvious thing I think everything else is all just things that were red flags about the

**[1:32:04]** organization not red flags about you know potential liquidity issues are fraud things like you know the complete inability to hire you know more people especially on the developer side not allowing me to like establish

**[1:32:18]** separate sort of c-level staff on the U.S side that would have you know Authority that was really separate from the ones in the Bahamas how completely tightly controlled uh the dev team was around access to

**[1:32:35]** the code base and the inner workings of all the exchange and really wanting to keep that Nexus of developer the developer group in the Bahamas next to Gary and nashad those seem like red flags now

**[1:32:47]** hmm yeah but not at the time did you notice anything weird during the Terra Luna collapse because in the aftermath people have said that that's probably what an Alameda defaulted on some loans and maybe some um uh the the sort of

**[1:33:03]** like whole dug itself deeper really nothing at all okay um I mean maybe that's a function of being here in Chicago and just not seeing a group of people freaking out but nothing seemed wrong at all in fact we

**[1:33:19]** started having conversations around you know paying out mid-year bonuses a couple weeks later after Tara an announcement and everything seemed very normal say I'm like sent out an announcement to the

**[1:33:30]** whole company basically saying like Okay like we're gonna be paying out bonuses soon people should expect they're going to be like a little bit lower because we have very similar Revenue to last year but we've also grown in size and

**[1:33:42]** also like the market is slowing and we need to be a little bit more conservative so all the signs pointed to like things as normal you said so you had a threat sort of

**[1:33:52]** boiling down this experience on Twitter and one of the things you pointed out there is that you saw the um sort of symptoms of uh sort of mental health or um issue or addiction issue at the time

**[1:34:07]** are you uh there are you referring to these sort of management um mishaps and bad decision making or is there was there something more that made you come to this conclusion I think it was more than that you know when I knew

**[1:34:20]** Sam when he was 21 22 years old he was like a happy like healthy looking kid who was you know very positive very talkative uh got along super well with his you know cohort of traitors uh the people on the

**[1:34:39]** desk really liked him when I got to FTX I think over the course of my time there I saw someone who was very different than that person I remembered I think he was angrier seemed more depressed more

**[1:34:54]** anxious um you know he couldn't get through a conversation without shaking his leg that wasn't yeah James Ruth he wasn't like that not something I remember at all

**[1:35:03]** you know he would snap easily he would not respond to messages for long periods of time um and people have different theories I mean people would attributed to the

**[1:35:12]** unbelievable stress of being in the position that he was in the complete lack of sleep uh like his diet lack of exercise I mean people had you know plenty of uh you know thoughts about what could be causing it all but

**[1:35:24]** something definitely had deteriorated like mentally and physically about him from who I remembered if you had to yes most likely cause of that what would you say I don't know I I think that's uh

**[1:35:37]** up for a you know professional with uh credentials that I don't have but I do think it was probably a combination of everything that the the lack of sleep the stress he probably was under not

**[1:35:51]** just being in his role but having kept the secret for so many years around you know whatever was happening with the holes in the exchange and the lying he was doing to his own employees to investors to Auditors maybe that weight

**[1:36:08]** on him maybe he had something to do with his medications and he had just had to be just a plain deterioration in mental state or some kind of you know personality disorder or different kind of anxiety disorder I really don't know

**[1:36:21]** maybe a mixture of everything yeah got it you said you uh gave him a sort of ultimatum uh letter where he said unless you change these things I'm resigning what were the things you asked that be changed in that letter

**[1:36:37]** yeah so the top three things were one to communicate more with me in particular um I could probably count on one hand the number of times I had like a one-on-one phone call with Sam which probably seems insane given like the

**[1:36:54]** position I was supposed to be in I I basically said like we have to talk every week it's impossible for me to get anything done if I don't have the authority but I have the responsibility to be able to push this company forward

**[1:37:05]** and we're not talking at all so that was number one uh number two was to establish oh separate you know especially sea level management

**[1:37:19]** staff on the U.S side if Sam was going to be so busy doing what he was doing at least he needed to delegate that responsibility to like I said a professional managers who could actually take care of the day-to-day

**[1:37:32]** operations within the company and it felt like things were starting to unravel in the absence of that and then the third was to grow the tech team and move a lot of the authority and management of that team

**[1:37:45]** away from nashot and Gary so that we could actually spread the knowledge and be able to keep up with a lot of the tasks that we were you know assigning ourselves and trying to build all these new business lines that pretty much

**[1:37:58]** summarizes it yeah how regularly were you talking and it wasn't regular I was on chat groups that he was in and so you know occasionally he would respond to something I say on that group

**[1:38:13]** but one-on-one conversations I think there were fewer than 10 for my entire tenure wow okay and that was over a year right year and a half year and a half five so about like less than one every two months yeah

**[1:38:29]** how did he respond to this letter so it took a little while before we got on the phone and he went through every point and refuted everyone he starting with communication he said I

**[1:38:45]** think phone calls are a waste of time I think that if I you know promise people regular phone calls they will use it to waste my time and it's not an efficient mode of communication he said I think we have the best

**[1:38:56]** developer team in the world and I think anyone who's just otherwise is completely wrong and if we add more depth a lot more people to the dev team if we move them to the US and you know move them away

**[1:39:06]** from the Bahamas we're going to be worse as an organization he kind of ignored the point about separate leadership I think he hated the idea of giving other people kind of titles that would reflect kind of

**[1:39:17]** Greater responsibility within the company and then so that conversation ended with us kind of not knowing what the future was going to be because hibiscus said like look

**[1:39:27]** I'm going to resign if you don't fix this he said we're not fixing anything and then what happened next was he had deputized uh another person within a company to come here to Chicago

**[1:39:42]** and pull me into a side room and say you are probably gonna be fired for this letter that you wrote and not only are you going to be fired but your Sam is gonna you know destroy your

**[1:39:55]** professional reputation like where do you think you're gonna be able to work after FTX after all this happened and it was he was threatening me and then not only that uh he had said

**[1:40:09]** if you are going to have any hope of staying and if you can forget about getting paid bonuses uh you need to write Sam an apology letter and show it to me first because I'm going to edit it and I'm going to tell you what to say

**[1:40:22]** and I said like absolutely not like this isn't like a mafia organization and this is like this is extremely unprofessional and and I knew at that point there was absolutely no way I was staying and it was a matter of when not if

**[1:40:39]** and but what I did know was that like I'm still a professional I'm still loyal to the company I still believe the company itself had an incredible potential to continue it sort of road to

**[1:40:51]** profitability and I really liked all my employees here on the U.S side and I wasn't going to abandon them so I sort of thought like a three to six month time period is about standard to take the time to unwind responsibilities

**[1:41:03]** to finish the stocks platform that I was working on to you know get my team in a position where I knew they would be in good standing and they wouldn't be like retaliated against after I left and took the time to do that before officially

**[1:41:19]** resigning in kind of the end of the summer in early fall and did that happen like did after you left did the did he like try to enjoy your professional reputation and you did

**[1:41:34]** the the most the acute thing that happened was so Sam I actually offered to stay on longer you know I said like I could stay on for a couple more months and help this transition to whomever you name as

**[1:41:47]** the successor president of FTX us and he said no like I want you gone you know more quickly and so I should say he said that but he was communicating through other people he wasn't talking to me directly at that

**[1:41:58]** point and so he said like I want you gone on September 27th so okay that's fine with me on September 27th not only did he announce to the company my resignation he also announced that he was closing

**[1:42:13]** the Chicago and San Francisco offices and that everyone had to move to Miami and basically if like they didn't move to Miami by a certain date they were like not going to be at the company anymore

**[1:42:25]** so the employees were distraught and what I learned later from several investors and reporters who had talked to me was that when they talked to Sam about my leaving Sam told them

**[1:42:40]** that my my leaving was a combination of resignation and firing and that one of the reasons that I had to leave was because I refused to move my family to Miami

**[1:42:55]** so basically like I was constructively fired um that he had closed down this office that I would that I had built and that like if I wasn't going to move that I couldn't I know roloffed at the company

**[1:43:04]** and so that took a little bit to crawl out from you know I had to tell people like well it's completely false it didn't happen at all and uh and yeah and he was telling people that he fired me and when

**[1:43:17]** he said that he was still at a sort of like peak of hype so to speak right absolutely so I mean did the idea of forming architect have already uh you already had that idea by by this point yeah knowing that I was going to leave I

**[1:43:31]** started thinking what I was going to do next and thought well like if I think I can run a company better than Sam I should like put my money where my mouth is and start a company yeah but I had this you know a couple of ideas and I

**[1:43:41]** had this particular idea for architect and it was starting to really form kind of towards the end of my time at FTX but I hadn't started anything and so finally like I left FTX and then took a little bit of time off and then

**[1:43:53]** started to talk to investors about you know maybe raising some money for starting this company and there were a few investors that basically said like you know do you have Sam's blessing to

**[1:44:04]** do this and why do I need Sam's blessing I've resigned I don't work there anymore I said like we really wouldn't feel more comfortable if we could talk to Sam first and kind of like you know make sure things are okay and uh kind of

**[1:44:19]** figure out what he's doing find out if he wants to invest to uh before we kind of talk to you further and it was impossible to escape that like the Sam kind of hype bubble even having left the company

**[1:44:32]** why do you think they were so concerned about were they like trying to invest in FTX in the future or they were existing FTX investors okay and I think it really mattered to them what Sam thought of them and if they didn't know the full

**[1:44:45]** story and if they were being told that like Sam fired me then I think they were concerned about you know potential conflict investing in me too it was any part of that because Sam had a reputation as I don't know if

**[1:44:58]** like an investor invested in somebody he disapproved of he would get upset in some way or no I I if that well if that happened I don't know about it but I think it was just Sam had such a uh kind of magical hold over the entire

**[1:45:13]** industry from investors to Media to politicians that they look to him for approval okay yeah so at this point you've left FTX us and you're starting to work on your

**[1:45:28]** um your own company and what when is this exactly this is uh so I left at the end of well my official resignation was the end of September I had like stopped working earlier than that and so I kind of started to start

**[1:45:42]** working on fundraising for the company in October and then a month later the thing implodes so when did you hear the first inkling that there might be some potential trouble the first thing I heard was the

**[1:46:00]** night before the announcement that Finance might be buying FTX I was just looking at Twitter and just saw all of this fear-mongering uh it was like okay well CZ says he's selling ftt

**[1:46:15]** and so FTP is going to go down and people are saying well that means alameda's toast and then once Alameda goes under oh that's going to be a problem for FTX pull your funds from FTX

**[1:46:27]** and I was just sort of laughing at this because like whatever I'm used to people saying things on Twitter that seem nonsensical and first of all Sam and Caroline are great Traders like

**[1:46:40]** if anything like maybe they'll like profit from all this volatility and tokens and they don't understand like there's there's no way anything's gonna happen to Alameda but also what this connection between the price of ftt

**[1:46:52]** token and the ability for customers to withdraw their funds from the exchange like this is did not compute for me at all so I was like well you know this will blow up oil over in a couple days like everything else

**[1:47:05]** and the next morning you know I was actually busy talking to like my own lawyers and investors for the company because we were actually closing up our investment round um actually the closing docks for my

**[1:47:19]** investment round went out that morning the morning that STX announced they were going to be bought by binance it was like the worst timing in crypto fundraising history

**[1:47:31]** um and so I was busy all morning and then I went you know online and checked Twitter and then saw Sam's tweet that said you know like what comes around goes around and we're gonna get acquired by finance

**[1:47:44]** and I I don't know I felt dizzy I had no idea what was going on in the world at FTX I I just couldn't put the pieces together in my head it just didn't make any sense to me

**[1:47:57]** so before then like you you did not think this was possible and then so I I kept a bunch of money on the exchange I was still an equity holder in FTX and FTX us like I was still very very Pro FTX in spite of

**[1:48:16]** my you know experience with Sam and then how did that week unfold for you you were I guess almost about to close around what happened to the round and then how were you processing the information I mean it was like a crazy

**[1:48:29]** week on Twitter right yeah um the deal falls apart bankruptcy hacking anyways tell me about that week for you sure so I mean first the investors you know we all had to hit pause I mean

**[1:48:43]** first of all architect became you know priority number one thousand on everyone's list uh secondly a number of those investors were trying to do damage control themselves you know they either they

**[1:48:56]** were themselves investors in FTX or ftt they had companies who part of their Runway was held on on FTX or they were expecting to get investment from FTX so people were just trying to assess like what was happening with their own

**[1:49:12]** companies they were not writing checks into new companies anymore so like I had to hit pause on the whole thing I mean for their sake and for my sake and yeah just what could one do in that situation

**[1:49:24]** except for just read the news all week because everything that came out was something brand new and unbelievable more unfathomable than the thing before and it was a mixture of like rumors on

**[1:49:40]** Twitter and articles coming out in you know major media Publications and the kind of the announcements of the bankruptcy it was just information overload and it was very difficult to parse path back from fiction and so it

**[1:49:54]** was an emotional time yeah yeah I understood man right all right so we've kind of done the whole story of you joining to the company collapsing I want to do a sort of like overview of I I guess like what exactly was

**[1:50:11]** happening that caused the company to collapse and I guess the lessons there right so okay so in the aftermath SPF has been saying that ftxtus is fully solvent they wanted to they could start processing withdrawals he had a soft

**[1:50:26]** stack recently in January where he said that it had 400 million dollars more in assets and liabilities what is your understanding of the sort of relationship between a dissolvency of FTX us

**[1:50:39]** because your answer is I really don't know you know if you had asked me about the solventy of text us at the time that I left I would have said why are you asking about this like of course everything's fine right

**[1:50:49]** um now it's very difficult to understand what is going on I mean first the level of deception that was

**[1:51:02]** you know created by this Inner Circle of Sam's and now report it through like the various complaints and indictments from doj they were doing things to intentionally manipulate internal records in order to

**[1:51:18]** fool like the employees and Auditors and investors so everything's out the window at that point um and then secondly it sounded like in the week prior to the bankruptcy there was this

**[1:51:30]** like flurry of inter-company transfers and given all that that's happened it's impossible to say what state we are in now compared to where we were several months prior so

**[1:51:43]** it's impossible to know who took over management of FTX us when you left I'm not sure it wasn't a single individual or was it just rested back to the Bahamas I really don't know I mean I've totally cut off from everything FTX at

**[1:51:56]** the time that I left uh before you left where the assets of ftxus custody separately to FTX International's assets yes they were okay so we had like a separate set of bank accounts separate set of crypto wallets you know the

**[1:52:11]** exchange itself was like a separate database of customers it ran in like a different AWS Cloud than the one you know that the International Exchange ran on okay got it and you had you had full access to this and

**[1:52:25]** like it checked out basically or more assets and liabilities right but remember that the thing that makes them not separate is the fact and this was completely public that

**[1:52:36]** Sam was the CEO of FTX naftax us and Gary was the CTO of FTX and FTX us and Nasha was a director of engineering for FTX and fxus and so as long as there wasn't this like completely separate walled off governance that we were

**[1:52:51]** trying to establish while I was there there was never going to be perfect separation between the companies this was like a known problem and you know that's what makes it so difficult to sort of understand the

**[1:53:05]** nature of what was potentially happening behind the scenes so I guess we've been talking about the sort of management organizational issues of FTX were these themselves not like some red flag to you that

**[1:53:19]** I don't know something really weird could be happening here even if it wasn't like fraud right like there these people are responsible for tens of billions of dollars worth of assets they don't seem that competent they

**[1:53:31]** don't seem to know what they're doing they're making these mistakes was that was that itself not something where that like concerns you I mean it concerned me and I tried to raise concerns multiple times if you raise concerns multiple

**[1:53:42]** times and they don't listen what can you do other than you know leave but you have to understand that every company I've ever worked at and I would think any company ever anyone's ever worked at has management problems and

**[1:53:57]** growing problems and especially for a super high growth startup like FTX it's a very natural progression to have the Visionary CEO who brings that product to product Market fit who enjoys that sort of

**[1:54:13]** explosive success and then the brains of the company are eventually handed over to professional managers who sort of take it into its maturation phase and I thought well really I'm not that

**[1:54:28]** person because you know Sam and I have interpersonal issues but there's a hundred plus major investors in FDX someone will figure out how to install the correct management of this company over time and we'll bring it to a good

**[1:54:42]** place like one way or another this is going to succeed there are too many people with vested interest in doing so and so no I wasn't concerned that you know FTX wasn't somehow figure this out I I still thought FTX had an extremely

**[1:54:56]** bright future but there might be I guess these sorts of Visionaries a lot of them might have like you know problems to put it a uh in a in that kind of language but I don't know I

**[1:55:08]** don't know how many of them would make you suspect that there's like mental health issues or there's addiction issues that for somebody who's in charge of a multi-billion Dollar Empire I don't know it seems like something that's uh I

**[1:55:21]** can't quite speak to like whether people would think there are you know mental health issues of like other like you know people who are supposed to be the kind of figureheads of large companies but remember like at this point Sam is

**[1:55:32]** not leading the day-to-day operations of the company like many other people are right and as the kind of public figurehead of the company same with obviously doing a very good job he was extremely successful at raising money he

**[1:55:46]** was extremely successful at building a positive image for the company and so in that sense that was all going fine and the rest of the company was being run by other people so you know I I didn't witness anything

**[1:55:58]** like you know the addiction stuff firsthand I definitely thought he was not as happy a person as I met you know a long time ago but could you blame a person for you know inheriting a 20 30 billion dollar company and you know not

**[1:56:11]** taking it super well when you're 29 years old right I think so I mean you mentioned that like given the fact that all hundreds of accredited investors presumably had done good due diligence uh that that you know that

**[1:56:23]** like gave you some comfort about the ultimate I guess soundness of the company but potentially those hundreds of investors who are relying on the experienced high-level Executives that SBF had brought on that is thinking that

**[1:56:38]** listen if somebody from Citadel and Jane Street is working at FTX that's a good indication that you know they're doing a good job and so in some implicit way you're lending your credibility to FTX right

**[1:56:52]** and so I guess was there just a sort of Circle of trust where the investors are assuming if this person who has tons of leadership experience in traditional Finance is coming to FDX they must have

**[1:57:05]** done the due diligence themselves and then you are assuming that the investors have done this and then so it's like nobody's role to be the you know the guy who's like this was my job and I was a person remember regardless of how

**[1:57:18]** experienced or inexperienced people within the company are regardless of how many or few investors there are how many senior lateral hires there are if a very small group of individuals who are very smart and very capable

**[1:57:34]** intentionally putting put forth schemes that deceive people within the company and outside the company about the veracity of Records

**[1:57:47]** what can you do what is one supposed to do in that situation if the public reporting matches private reporting if investors have done their own diligence

**[1:57:59]** if we've you know joined the company and we see nothing wrong within the company from a financial perspective if we can see the public volume on the exchange and it all like matches up with our internal reporting and we know how much

**[1:58:13]** fees we'll be able to collect and all that and it seems like a lot of income compared to our expenses for a two or three hundred person company at what point do you like go against all of that and say in spite of the

**[1:58:26]** overwhelming evidence of the contrary I think something is wrong yeah but someone might look at this and say um listen Brad you're wearing like a junior Trader who was like right out of MIT or something who just joined um FTX you

**[1:58:38]** have uh more than 10 years of experience in finance you like saw Lehman happen you you know you've like managed really large teams and uh dratify and then you have you have the skills and the experience and if somebody with your

**[1:58:52]** skills and experience and not only that your position in FTX as president of FTX us if you can't see it coming and maybe you couldn't right whose job was it to see it coming like it doesn't seem that anybody other than the Inner Circle

**[1:59:07]** could have been in a better position and maybe nobody could have seen it but like is there somebody who outside of the Inner Circle you think should have been able to see it coming I don't know it's a it's a good question

**[1:59:18]** of like when a major fraud happens in such a way where it was you know very expertly crafted to be hidden from the people who could have done something about it what should one do I mean one answer is

**[1:59:36]** never trust anyone right like every company I ever work for in the future every time like we say we've like done some transaction I will ask them to show me the bank records and like give me the you know the number of the bank teller I

**[1:59:50]** can call to have them like independently verify every single banking transaction I mean this is sort of like impractical and ridiculous it just like it doesn't happen and so I think like it sounds like the the counterfactual here is one

**[2:00:03]** where okay first I have to believe that there is some kind of fraud which I don't then I have to say Okay I I would like to start auditing all Bank transactions oh actually I want to start auditing all

**[2:00:18]** Bank transactions for the company that I don't work for also I want to like disbelieve audited financials from respective third-party auditors

**[2:00:29]** I also want to look into the possibility that Sam is like lying under oath in Congressional hearings about segregation of customer funds also I should disbelieve all of the trusted media outlets and also a hundred

**[2:00:43]** financial institutions that have invested in FTX it's like the the chain that you have to go through in order to get to a point where you start to be able to figure out something is wrong

**[2:00:56]** is I think really impossible and I think the bottom line is they're you know for sure should be mandated you know at certain stages of company growth

**[2:01:12]** independent boards and I think that a lot of that has to do with like where the like Nexus of control of the company really is and making sure it's in a place where there

**[2:01:24]** is appropriate regulatory oversight and appropriate Financial oversight um I think that maybe could have helped but besides that I think this is ultimately a job for enforcement like people will

**[2:01:37]** commit crimes and there's nothing one can do to stop all people from committing all possible future crimes what gun can do is come up with the right structures and incentives so that we can build like a trust-based system

**[2:01:49]** where people can innovate and build great companies and the people who are Bad actors can get flushed out which is ultimately what I think is happening but I guess they're not letting you hire people they're like

**[2:02:01]** they're like overseeing writing the actual code for FTX who has run the Bahamas yeah not something that makes you think like why are they doing this you know it's like a little odd I just thought it was not the right way to run

**[2:02:11]** the company there's a very large Chasm between I don't think they're doing a good job running the company and I think that customer funds are at risk right yeah fair enough

**[2:02:24]** what should someone who sees bad organizational practices there's no board they're making a ton of really weird Investments and Acquisitions um and not only that like most

**[2:02:37]** importantly they are responsible for managing uh tens of billions of dollars worth of other people's assets what should somebody do when they're seeing all this happening I mean obviously it's like

**[2:02:48]** very admirable and uh that you put this in like writing to him you give it to him and then you resigned when he refused to abide by it but so maybe the answer is just that but like is there something else that

**[2:03:01]** somebody should do I would say within any company and I would expect that like the overwhelming majority of companies if you see badge management mad management it does not imply fraud

**[2:03:13]** um but there's lots of places with bad workplace culture and people are making bad management decisions and it should be that if you're in find yourself in that position there is someone you can go to to talk to it

**[2:03:26]** might be your manager might be your manager's manager it could be someone in your HR department but there should be like a designated person within the company for you as an employee that you know you have a safe

**[2:03:39]** space to bring complaints about the workplace and about the company strategy and then you should see how they handle it you know do they take it seriously do

**[2:03:50]** they make changes do they look into the stuff you're talking about do they encourage you know Cooperative positive discussion do they threaten you do they retaliating us against against you in some way do they start excluding you

**[2:04:03]** from conversations do they you know threaten to withhold pay like if you're in that ladder Camp what do you do at that point it's easy for for me to say and I've been in some fortunate positions within

**[2:04:14]** companies and have you know personal flexibility it might not be so easy for the average person to sort of get up and leave a job but I do think that at some point you have to start making plans because like what can you do in the face

**[2:04:26]** of a giant organization that you disagree with other than leave let's talk about regulators and your relationship with them while you're at FTX I mean obviously as head of FTX us I imagine

**[2:04:39]** we're heavily involved with talking to them what was their attitude towards FTX like before it fell all the The Regulators were I think in the common belief that crypto was a large and viable asset

**[2:04:54]** class and in order for it to grow in a responsible way it needs to come within the regulatory envelopes that already exist in whatever way that's appropriate for

**[2:05:06]** crypto and crypto could mean a lot of different things we have to maybe distinguish between centralized and decentralized finance here but uh I would say Regulators saw FDX as at least one of the companies

**[2:05:20]** that was very willing to work directly and collaboratively with Regulators as opposed to trying to kind of skirt around the regulatory system well when I Was preparing to interview SPF actually I got a chance to learn

**[2:05:34]** about your you know proposal to the cfdc to we were just talking about you were explaining this earlier but the Auto Liquidation and cross-margining system bring that not only to crypto in the US

**[2:05:43]** but to derivatives for stocks and other assets I thought and I still think it's a good idea but do you think there's any potential for that now given that the company was associated with that has been uh blown

**[2:05:56]** up like what what is the future of that Innovation to the financial system look like yeah I definitely think it's been set back um you know it's interesting uh Walt Luken from the Futures industry

**[2:06:08]** Association in a conference that was shortly after the class of FTX you know talked about FTX and sort of a speech but specifically made a call to the fact that in spite of what happened to FTX

**[2:06:21]** the idea of building a future system that can evolve with a 24 7 world is still a worthwhile Endeavor and something that we should consider and pursue and be ready for we are 3D

**[2:06:38]** printing organs and coming up with like specially designed mRNA vaccines but like you still can't you know get a margin call on a Saturday for uh S P 500 future there's like some real lack of evolution

**[2:06:51]** in Market structure in a number of areas of traditional Finance and I think it's still a worthwhile Endeavor to pursue it I think the F The Ledger X proposal

**[2:07:03]** makes a lot of sense I think it's understandable where some of the concerns were around how that could really dramatically alter the landscape for you know derivatives regulatory structure and Market structure and they

**[2:07:16]** were still unaddressed questions there um but I I still think that it was the right idea during those hearings I guess the establishment you know CME and others brought up criticisms like oh we have

**[2:07:29]** these sort of biscuit relationships with our clients and if you just have this algorithm take its place you can have these liquidation Cascades where illiquid assets you know you they start getting so that drop drives a price even

**[2:07:42]** lower which causes more liquidations from this algorithm and you have the sort of cascade where the bottom falls out and even though it might not be an accurate way to describe what happened with ftt and FTX because there was like

**[2:07:55]** obviously more going on do you think that they maybe had a point given how FTX has played out a lot of fcms have Auto Liquidation there are there's one you know particular one where like they actually

**[2:08:10]** automatically close you every day at 4 pm and they do it like in a really bad way so like the idea of Auto Liquidation is not new uh the idea of

**[2:08:20]** direct to customer clearing is not new the idea of cross-collateralization is not new the thing I think that was novel about FTX was putting all all together

**[2:08:34]** it was direct to customer margining cross-cladralization Auto Liquidation and so in order for the like Regulators get comfortable with the application they had to understand

**[2:08:47]** that ftx's one entity was performing the roles that typically multiple different entities perform and one you always need to ask yourself the question of like was there something worthwhile about having those different

**[2:09:00]** entities be separate or not is it just sort of like Legacy regulatory structure um I think that remains to be seen I think we don't have enough you know experience especially in the US with

**[2:09:13]** that kind of model to be able to say whether it actually works better or worse I think either way it was worth a try and I think maybe the biggest misconception about the application was

**[2:09:23]** that you know if we got approved it meant suddenly FTX is going to list like everything from like corn to soybeans to oil to S P 500 overnight and completely you know destroy the existing

**[2:09:35]** derivatives landscape I think what would have actually happened was FTX would have gotten permission to list like one contract on this kind of small size and there would have been you know experience with the platform and it

**[2:09:48]** would have like you know been assessed compared to the alternatives on traditional ccps and if it was worse changes would have been made and if it was better it would evolve and the market would basically decide what

**[2:09:59]** people wanted to trade on I do think like the Auto Liquidation part was the main piece that people were hung up on which was like how do you provably show the kind of worst case scenario in Auto Liquidation Cascade

**[2:10:14]** then again on large gcps now in the US and Europe there are margin breaches all the time like the current system is far from perfect backing up to I guess regulation more generally I mean many people saw crypto

**[2:10:29]** as a sort of regulatory Arbitrage where because regulations are so broken in finance I guess evidence would be that you're not allowed to do this manually right you had to go through the lengthy approval process if you're a giant

**[2:10:42]** company to begin with the entire point of crypto was to get around the regulators and not go through them to get approval for things and hand over that kind of overflow process to them do you think that working with the

**[2:10:54]** regulators and then also being part of crypto was a sort of like it kind of defeated the part of crypto or I think I disagree with the premise like I don't think the point of crypto is record for Arbitrage I think the

**[2:11:06]** while crypto remains unregulated it is easier to get some things done in crypto than if it were regulated that's sort of like total logical I also think that most people especially on the institutional side who traded

**[2:11:21]** crypto believe that we are in a temporary state that cannot last forever which is that crypto is largely unregulated or has a weird Patchwork of you know regulatory Authority you know maybe it's like the 50 state Regulators

**[2:11:35]** in the U.S or it's some combination of like you know money transfer and uh you know cfd or broker dealer activity in Europe so I think this is it's absolutely a worthwhile Endeavor knowing that there's going to be some regulation

**[2:11:51]** for at least part of the crypto ecosystem to work with Regulators to make sure that it's done well one very important question about the whole objects thing is like what did the conventional narrative about how it went

**[2:12:02]** down and why it went down what did it get wrong given that you were on the inside like what do you know was uh different than what has been reported I actually think

**[2:12:13]** not much and I think the reason for that is you know typically when something like this goes wrong and it becomes this media frenzy there's like plenty of opportunity for misinformation to spread

**[2:12:25]** but to the credit of the investigators working on this case they moved so quickly that you know they had you know unsealed indictments within what two months of this going down and so having

**[2:12:40]** kind of a lot of the sort of the truth you know being able to be spelled out in facts in a public written document I think quelled a lot of the opportunity for misinformation to proliferate

**[2:12:55]** and whether that's from like a Twitter troll or if it's from Sam fagment freed himself you know trying to like spread Mr information about what happened I think a lot of it wasn't really given the room to breathe what did you make of

**[2:13:08]** his press tour in the aftermath well like why did he do it and like yeah what was your impression of it I'm not gonna really speculate what's inside Sam's head I think

**[2:13:21]** Sam had built up his Empire through Bartley his control over media and he did that by being available all the time and being you know ostensibly open and

**[2:13:36]** honest with them all the time and probably thought why can't the same strategy work now and maybe I can sway public opinion if I can say public opinion maybe I can sway you know regulators and you know law

**[2:13:51]** enforcement and it turns out that is definitely not true so I don't really know it could just be an addiction to the media he couldn't stand people talking about him and him not being part of the

**[2:14:02]** conversation yeah yeah and I guess the earlier account you gave of his day-long media Cycles kind of lends Gruden's to that mentality I have a question about the future of the people

**[2:14:16]** who are at FTX there's many different organizations who um have had their alumni go on to have really incredible careers and Technology famously PayPal

**[2:14:29]** had a mafia so-called Mafia where they wanted to found YouTube with Elon Musk you know SpaceX Tesla so many other companies came out of the people who came out of PayPal and burn Hobart has this interesting Theory

**[2:14:42]** the reason that happens is when a company exits too fast you still have these people who are young and ambitious in the company who go then go on to you know do powerful things with the network and the skills they've accumulated

**[2:14:53]** um do you think that there will be an FTX Mafia the the number of the like most talented people within FTX are are leaving uh FTX in a slightly different position than you know the people exiting uh PayPal

**[2:15:07]** acquisition I would say they're uh in positions more like actual Mafia people uh but so I'm not sure it's going to be like some giant you know FTX Mafia but I do think there are like a ton of talented people at FTX who are going to

**[2:15:23]** look to do something with their careers and and also a lot of those people you know came from very impressive backgrounds prior to FTX so I expect them to want to continue to you know get back on track

**[2:15:34]** and build something great and so I do think you're going to see at least a couple of people who emerge from this and do something really great that's a good note to close the FTX chapter of the interview on sure let's talk about

**[2:15:46]** architect your new company do you want to introduce people to what architect is doing and what problem is solving sure so the goal of architect is to provide a single unified infrastructure that makes it really easy for individuals and

**[2:16:03]** institutions to access kind of all corners of the digital asset ecosystem you know everywhere from Individual crypto spot exchanges that are centralized to D5 protocols to qualified custodians and self-custody and

**[2:16:19]** everything in between yeah I I I'm not sure I have enough context to understand all of that so I I don't know a few grade levels below like backing up a very high level so let's say you are someone who wants to

**[2:16:35]** trade you know crypto in some way or you know what do you actually have to do yeah so imagine you want to do something slightly more than just like sign up for coinbase and like click the buttons there like let's say you would like to

**[2:16:47]** find the best price across multiple exchanges um let's say that you not only want to find the best price across multiple exchanges you also want to occasionally do borrow and lending from defy maybe

**[2:16:59]** not only that you also want to like store your assets in like off exchange custody as much as possible well aside from doing all that manually by like opening up all the different tabs in your browser and like clicking all

**[2:17:15]** the buttons to move assets around and connect all these different exchanges if you actually want to build a system that like unifies all these things you have this buy versus build choice and the the build Choice looks like

**[2:17:28]** higher like five to ten software developers and get them to write code that understands all the different protocols and different exchanges all the interesting distinction to them and it downloads Market data that stores the

**[2:17:40]** market data that connects to these different custodians that kind of bridges all these things together and provides some kind of like user interface it pulls it all together it's a significant amount of work that up

**[2:17:52]** till now basically all of these different companies are just reproducing again they're all solving like the same problem and as a Trader you want to focus your time on like strategy development and

**[2:18:03]** Alpha and monetization and not on like how do I connect to random Exchange so the goal of architect is to build this sort of like commodity software that people can then sort of deploy out of

**[2:18:17]** the box that gives them access to all of these different venues all at the same time and so it sounds like this is a solution for people with significant levels of assets and investment in crypto I'm

**[2:18:31]** assuming it's not for so I think that's like the place we want to start yeah but one phenomenon in crypto that I think is somewhat new and exciting is the fact that okay if you're if you want to get into

**[2:18:45]** like sophisticated equities Trading well what do you have to do I mean you usually have to either establish a broker dealer or you know get hooked up to an existing broker you need to get Market data which can be very expensive

**[2:18:59]** like the you know full depth of book feed from NASDAQ costs like tens of thousands of dollars per month if you want to compete on latency you have to get like a co-located server in the NASDAQ Colo which is also going to cost

**[2:19:13]** you tens of thousands of dollars per month is a significant time and money overhead to doing all this which is why it's so hard to compete in that space against all like the incumbent players

**[2:19:23]** whereas in crypto many of the markets are just in the cloud like in Amazon's cloud or alibaba's cloud and you can just very cheaply and easily spin up like a server in the air for like a couple dollars a

**[2:19:35]** month and have the same access as like a big hft or all the market data is free the order entry is free the protocols are usually fairly simple like you can use like you know Json uh over a websocket as opposed

**[2:19:50]** to speaking like fix over some you know private you know line as a result there is this large and growing class of kind of like semi-professional individual traders that have grown where there are people who are smart individuals who

**[2:20:05]** have like maybe some wealth amassed and they want to be able to do kind of professional trading whether that's like manual quick trading or like simple Algos using python or whatever and they can do that and experiment easily

**[2:20:16]** because of the Open Access of crypto markets and so there's a much wider customer base for something like this which includes these kind of like high-powered individuals in addition to your small medium large

**[2:20:28]** hedge funds and Prop Shops and different institutions and is the goal to is crypto the ultimate Market you're targeting or are there other asset classes that you also want to provide the service to we're

**[2:20:42]** building very general infrastructure and you know we think crypto is you know a viable asset class but it's one of many and our goal is to provide like institutional grade connectivity and software to anyone who wants to

**[2:20:57]** participate in trading and us you know semi-sophisticated way so I think you know over time we'll want to grow our offering as much as possible given the fact that you know NASDAQ or whatever already have these

**[2:21:10]** barriers is it possible for someone to remove those barriers with a solution like yours or um I mean I I guess like an analogy that comes to mind is you know I guess nobody before Mark Cuban's

**[2:21:22]** whatever pharmaceutical company just try to go outside the insurance system and directly sell drugs to people is it possible to do something like that for well stack yeah you can't like connect to NASDAQ without you know connecting to

**[2:21:34]** NASDAQ you can't like not go through a broker dealer but I think that you know we could eventually try to get the appropriate licensing required to be an intermediary that is focused on being like a technology

**[2:21:48]** forward you know interface towards people being able to do more program trading and so if the mission of our company is to like provide better access I think we can do so within the existing system I guess this race is a broader

**[2:22:03]** question of if you're initially trying to solve for the problems that these exchanges should natively have solutions to at least or some of the problems are the ones that these exchangers natively have solutions to do why why haven't

**[2:22:15]** this these exchanges built this stuff already I mean you you're a part of one such exchange um and maybe function better than the other ones but I mean you know they have they're highly profitable they have a

**[2:22:26]** bunch of money why haven't they invested in making their infrastructure really great so in many cases their infrastructure is very good it's it's more a question of what's the incentive of the exchange and

**[2:22:37]** I think if you're no matter what no single exchange is going to have all the market share so there's always going to be this like uh Market fragmentation problem and the question is whose responsibility is it

**[2:22:50]** to make software that helps solve that problem if I'm some centralized Exchange my incentive is not to build software to make it easier for my customers going all the other exchanges it's like make my exchange better so I'm going to put

**[2:23:02]** all of my r d dollars into like providing new products and you know offering you different kinds of services or maybe investment advisory or you know lowering the uh the barrier to entry to connecting to my own exchange but not

**[2:23:15]** creating this sort of like pan asset class pan uh exchange interconnectivity software got it got it and given the fact that you're trying to connect these different exchanges I mean

**[2:23:29]** currently most of the volume in crypto is in centralized exchanges is are like what is your estimate of the relative trading volume of um C5 versus D5 do you think it'll change over time

**[2:23:43]** so I do think it'll change over time I think my view is I can't predict what way it's going to change so you know people after FTX had asked me like hey why don't you try to start your own exchange like take all your

**[2:23:57]** knowledge from FTX us and you know maybe even like raise money to buy the IP at a bankruptcy and like start a new exchange and my feeling is I don't wanna personally on the exact direction of crypto Trading like I could see it

**[2:24:12]** continuing status quo where like your coin bases and biases that were all kind of maintained market share I could see it moving significantly to defy where people feel like this is the true Spirit of crypto it's in this sort

**[2:24:25]** of non-custodial like fully centralized trading environment I could also see it going to complete opposite direction and having the existing highly regulated exchange players like nice uh noisy and NASDAQ and sibo like start to enter the

**[2:24:41]** game on spot trading and where is the ultimate like flow going to end up between these three possibilities I have no idea so I'm much more excited about providing the kind of uh kind of connectivity layer to all them and

**[2:24:55]** saying regardless of where the liquidity ends up we'll be able to facilitate it we'll be speaking of FTX how has your experience with FTX informed development of architect yeah I mean first of all working at FTX you know has

**[2:25:08]** given me an appreciation for just how behind a lot of the infrastructure is on other exchanges you know people really like trading on FTX institutions especially really like

**[2:25:20]** trading FTX because the API like made sense it like really did follow kind of the kind of standard State machine of any kind of financial you know essential limit order book that you would see on a place like NASDAQ or CME whereas there

**[2:25:32]** are a lot of exchanges that have crazy behavior like you send a cancel for an order you get acknowledge that your order has been canceled and then you get a fill

**[2:25:42]** and you actually like get traded on your thing that you supposedly thought you canceled and like things that you think shouldn't be possible or possible so actually my time at FTX is interesting with relation to architect because you

**[2:25:53]** know FTX it gave me an appreciation for how to design a good API for especially institutions to want to be able to trade all the time and the protocols and some of these other exchanges like aren't quite as good so I think it informed how

**[2:26:09]** much the focus of Architects should be kind of wrapping up the complexity of these different exchanges and providing like a really good API for institutions and individuals on our side and that's like

**[2:26:20]** thing one thing two is obviously would happen with FTX people are much less likely to trust a centralized institution with their personal information especially things like the keys that allow you to trade on

**[2:26:37]** their exchange account or the keys that give you access to their wallet and so we're thinking a lot about how to design Architects such that the user can connect to all these places and you know hook up their wallets without needing to

**[2:26:50]** ever give us any of their private credentials and so that's like another you know particular inspiration from everything that's happened in sdx what is your opinion of crypto in general at this point like uh how has

**[2:27:04]** your sort of perception of his promise changed if at all given the things yeah I mean I feel the same way now as I did then which is it's a you know one to three trillion dollar asset class that is traded by every

**[2:27:17]** major institution that is being invested in by every major institution and so it's totally viable and it needs good mature infrastructure to support its growth got it but

**[2:27:31]** is the motivation also informed by a view that I don't know crypto is going to be even bigger or in some way going to solve use really big use cases or is it simply that like listen this Market

**[2:27:45]** exists I don't know what it's going to be good for but it needs this solution it is I think you know I certainly do believe that that is like a likely future for crypto but to me like the the interest in it starts with knowing that

**[2:27:59]** this is a huge asset class with like that needs better infrastructure for trading it and in the aftermath of FTX and other things I mean all crypto companies have like a special scrutiny on them and fairly or unfairly if

**[2:28:15]** there's like FTX alumni it'll be even more so like how how are you convincing potential clients investors that you know there's crypto is safe FDX alumni are safe yeah on the ethics alumni side I just personally haven't had those

**[2:28:31]** issues really uh you know in like recent months as we've been building out architect you know I hired like three almost five now employees from performing at FTX to come work with me but by the way is that is that like some

**[2:28:44]** sort of R basically that the overall hiring Market is over corrected on them or something 100 yeah and not just an FTX like right now like it is you know March 2023 as we're recording this like

**[2:28:56]** there's like a huge ARB in the hiring Market I mean all the layoffs in Tech and crypto all of like the fear around various Financial Services means that like we basically didn't need to work on recruiting I had like the best people

**[2:29:10]** who worked at me for me at FTX us I had you know ex-colleags of mine um you know from former jobs that come work with me here and we actually didn't have to like you know do any formal recruiting efforts because of just how

**[2:29:24]** much Supply there now is on the you know the job market for you know especially in Tech and finance luckily you know I've had a long career history prior to FTX and even at FTX you know we've built really great stuff we

**[2:29:39]** had a very good connections relationships with our customers and our investors you know there will be times where like on Twitter I would answer like uh you know customers you know support question at

**[2:29:50]** two o'clock in the morning and I maintained a lot of those relationships even through the collapse and these are the kinds of people who are reaching out and like offering support like offering to test out stuff we want to be

**[2:29:59]** customers who are also having problems existing crypto tools and looking for something better so all that stuff has remained intact so I I don't really have a concern there what is um institutional interest in crypto like at this point

**[2:30:10]** even what's happened I I think it is just as great as it was before every like major you know Investment Bank in the U.S has announced some like plan to do something with blockchain technology still even like

**[2:30:26]** post FTX the top trading institutions of the world are all continuing to trade it I think as of what we're speaking about right now you know volumes are down because people are sort of generally fearful uh but I expect that to turn

**[2:30:39]** around pretty quickly and the institutional interest Still Remains really high people are definitely expecting and waiting for you know proper regulatory oversight especially in the US that's

**[2:30:50]** still happening people are waiting for you know higher grade professional tools that make it safe for them to trade and invest in crypto I think that's obviously in the works for various things architect and otherwise

**[2:31:01]** um but otherwise the interest is all completely there a broader question somebody could have about crypto at this point is or maybe not crypto generally but crypto trading is why is it good to have more

**[2:31:12]** crypto trading at least with stocks and bonds and other kinds of traditional assets as we were talking about earlier you can tell a story that listening to helps Capital allocation um projects that need funding we'll get

**[2:31:25]** funding and so on why is it good if the price of Bitcoin is efficient why is building a product that enables that something that's socially valuable I mean I think it boils down to like first of all do you think it's important

**[2:31:40]** for people to be able to trade Commodities like how how important is it for the world that people can you know trade gold efficiently or they can trade oil efficiently I think the answer is like if people have a use for the

**[2:31:55]** underlying commodity then it's it's important and so like what's maybe that is like what's the use of crypto well I think on each you know crypto token might have its own use I don't think everyone has a good use I think that

**[2:32:06]** there's a bunch that do but if you know you believe in Bitcoin as sort of like a store of value in a great medium of exchange then it's important that there's a good fair price for Bitcoin to enable that if you think that you know

**[2:32:20]** the ether token is important for like the the gas fees required to run like a decentralized computer and you think that the program is running out of decentralized computer are important then it's important for there to be like

**[2:32:31]** a good price for ether that's fair so I think it really depends on if you kind of believe in the underlying use case at all in the same way you would for kind of any commodity yeah and sometimes there are tokens that have more

**[2:32:43]** security-like properties where they are like trading Apple stock you know basically like they there is a was an initial offering of that token and then if people bought it actually directly funded the product behind the

**[2:32:56]** token and then the efficient trading of that token is sort of a barometer for the health of that particular company and they can like sell more tokens to raise more capital and secondary offerings in which case it looks very

**[2:33:07]** much exactly like the stock market that's a great leading to the next question which is will there ever be a time when um things that are equivalent to stocks or other kinds of equities will be

**[2:33:20]** traded on change and some sort of decentralized way I think it's likely um I think the primary reason is that existing settlement systems in traditional markets seem to be very slow and built on very outdated technology

**[2:33:37]** that's like highly non-transparent and very error prone so equities are a prime example of this like it still requires two business days to settle a stock and a frequent occurrence uh when I was at trading

**[2:33:51]** firms was that you know you would get your settlement file that one told you like what trades were settled and two told you things like if any corporate actions had occurred overnight like paying a dividend or share split and

**[2:34:03]** they would frequently be wrong like the dividend would be wrong or would be missing or we could share a split amount was for the wrong amount or they missed the day that had happened or they messed up some trades didn't get reported

**[2:34:13]** properly they're just frequently mistakes and it feels like there should be some like easy transparent kind of open decentralized settlement layer for like all things that you could trade and rather than try to retrofit

**[2:34:28]** the existing settlement technology to be faster and better starting from scratch with something like blockchain could make a lot of sense which is why you hear about a lot of like these investment Banks working on settling

**[2:34:38]** fixed income products on chain because fixed income products have an even worse settlement Cycles than equities should the marginal uh crypto Trader stop trading like I mean maybe this is this might also be a good

**[2:34:53]** question to ask by like the marginal Trader for I don't know on Robin Hood or something but I think I have a couple thoughts about this so the first is that I don't think crypto markets are as efficient as Equity markets yeah so

**[2:35:05]** there's probably more opportunities for short and long-term Edge as a Trader in crypto then there would be in equities that being said I think there's still an enormous amount of room

**[2:35:18]** in both like traditional and crypto markets or even individuals to have and derive information that gives them profitable trading ideas and I actually think it's the wrong conventional wisdom to think that if you

**[2:35:34]** are not Jane Street or Citadel or Hudson River or Tower or you know jump trading then you have no chance of being able to profit in Marcus except for luck I do think there are a lot of people who trade and it's like pure speculation

**[2:35:48]** it's not really like on me to tell them like they shouldn't speculate they probably like derive some personal enjoyment from speculation besides the opportunity for profit uh but I do think the access to more sophisticated

**[2:36:00]** instruments and information has helped what have traditionally been you know players that have been unable to compete in the market actually be able to do so in a way that's systematically profitable okay so that is I think a

**[2:36:14]** good point to end the conversation we got to talk a chance to talk about a lot of things let's let the audience know where they can find out more about architect and also like where they can find your you know Twitter and other

**[2:36:25]** sorts of links sure yeah so architect's website is architect.xyz uh we also have architect underscore XYZ on Twitter and I'm Brett harrison88 on Twitter okay perfect awesome Brett thank you so much for being on the lunar Society this was

**[2:36:39]** a lot of fun thank you so much hey everybody I hope you enjoyed that episode just wanted to let you know that in order to help pay for the bills associated with this podcast I'm turning

**[2:36:53]** on paid subscriptions on my step stack at warcashpatel.com no important content on this podcast will ever be paywalled so please don't donate if you have to think twice before buying a cup of coffee but if you have

**[2:37:08]** the means and you've enjoyed this podcast or gotten some kind of value out of it I would really appreciate your support as always the most helpful thing you can do is just share the podcast send it to

**[2:37:18]** people you think might enjoy it put it in Twitter your group chats Etc just splits the world appreciate your listening I'll see you next time cheers [Music]
