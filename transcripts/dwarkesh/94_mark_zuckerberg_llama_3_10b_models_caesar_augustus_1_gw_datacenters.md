---
layout: default
type: transcript
series: dwarkesh
episode: 0
guest: ""
title: "Mark Zuckerberg — Llama 3, $10B models, Caesar Augustus, & 1 GW datacenters"
source_url: "https://www.youtube.com/watch?v=bc6uFV9CJGg"
analysis_url: /transcripts/dwarkesh/94_mark_zuckerberg_llama_3_10b_models_caesar_augustus_1_gw_datacenters.analysis/
permalink: /transcripts/dwarkesh/94_mark_zuckerberg_llama_3_10b_models_caesar_augustus_1_gw_datacenters/
---

# Transcript: Mark Zuckerberg — Llama 3, $10B models, Caesar Augustus, & 1 GW datacenters

Source: https://www.youtube.com/watch?v=bc6uFV9CJGg

---

**[00:00]** that's not even a question for me whether we're going to go take a swing at building the next thing I'm just incapable of not doing that there's a bunch of times when we wanted to launch features and then Apple's just like nope

**[00:11]** you're not launching that I was like that sucks are we set up for that with AI where you're going to get a handful of companies that run these closed models that are going to be in control of the apis and therefore are going to

**[00:22]** be able to tell you what you can build then when you start getting into building a data center that's like 300 megaw or 500 megawatts or a gigawatt just no one has built a single gigawatt data center yet from wherever you sit

**[00:35]** there's going to be some actor who you don't trust if they're the ones who have like the super strong AI I think that that's potentially a much bigger risk Mark welcome to the podcast hey thanks for having me big fan of your podcast oh

**[00:47]** thank you that's very nice of you to say um okay so let's start by talking about the releases that will go out a when this interview goes out um tell tell me about the models tell me about meta AI what's new what's exciting about them

**[00:59]** yeah sure so you know I think the the main thing that most people in the world are going to see is the new version of met AI right so it's um and you know the most important thing about what we're doing is the upgrade to the model we're

**[01:10]** rolling out llama 3 we're doing it both as open source for the the dev community and it is now going to be powering met AI um so you know there's a lot that I'm sure we'll go into around llama 3 but I think the bottom line on this is that

**[01:23]** with llama 3 we now think that meta AI is the most intelligent AI assistant that people can use that's freely available um we're also integrating Google and Bing for realtime knowledge um we're

**[01:34]** going to make it a lot more prominent across our apps so you know basically you know the top of WhatsApp and Instagram and Facebook and messenger uh you'll just be able to um you know use the search box right there to ask ask an

**[01:46]** any question um and there's a bunch of new creation features that we that we added that I think are pretty cool that I think people enjoy uh and I think animations is is a good one um you can basically just take any image and

**[01:58]** animate it but I think one that that uh people are gon to find pretty wild is uh it now generates high quality images so quickly I don't know if you've gotten a chance to play with this that it actually generates it as you're typing

**[02:11]** and updates it in real time so you're like typing your query and it's and it's kind of like honing in on and and you know it's like okay here um you know show me a picture of a a cow okay in a field with mountains in the background

**[02:23]** it's just like everything eating macademia nuts drinking beer and like just and and just like it's updating the image in real time it's pretty wild I think people are going to enjoy that um so yeah so that I think is that's what

**[02:35]** most people are going to see in the world right we're rolling that out um you know not everywhere but we're starting in um in a handful of countries and we'll do more over the coming weeks and months um so that's that I think is

**[02:46]** gonna be a pretty big deal um and I'm really excited to get that in people's hands it it it's a big step forward for Medi um but I think you know if you want to get under the hood a bit the Llama 3 stuff is is obviously the most

**[03:00]** technically interesting so you know we're we're basically to for the first version we're training three versions um you know an 8 billion and a 70 billion which we're releasing today and a 405 billion dense model um which is still

**[03:13]** training so so we're not releasing that today um but you know the 8 and 70 I mean I'm I'm pretty excited about how they turned out I mean it's um you know they're they're leading for for their scale um you know it's uh I we'll we'll

**[03:30]** release a blog post with all the benchmarks so people can check it out themselves and obviously it's open source so people get a chance to play with it um we have a road map of new releases coming uh that are going to

**[03:41]** bring multimodality more multilinguality um bigger context Windows to those as well um and then you know hopefully sometime later in the year we'll we'll get to roll out the four or five which I think is is um you

**[03:55]** know in training it's still training but uh for for where it is is right now in training it is already at um around 85 mlu and um and just we we expect that it's going to have leading benchmarks on a on a bunch of on a bunch of the the

**[04:12]** benchmarks so I'm I'm pretty excited about all that I mean the 70 billion is is um is is great too I mean we're releasing that today it's around 82 mlu and has leading scores on math and reasoning so I mean it's I think just

**[04:24]** getting this in people's hands is going to be pretty wild oh interesting yeah that's the first time hearing Benchmark that's super impressive ion is the 8 billion is um is nearly as as powerful as the biggest version of llama 2 that

**[04:37]** we released so it's like the smallest llama 3 is basically as powerful as the the biggest llama 2 okay so before we dig into these models I actually want to go back in time 2022 is I'm assuming when you started acquiring these

**[04:51]** h100s um or but you can tell me when um you're like stock price is getting hammered people are like what's happening with all this capex people aren't buying the metaverse and presumably you're spending that capex to

**[05:01]** get these h100s how back then how did you know to get the h100s how did you know we'll need the gpus um I think it was it was because we were working on reals so you know we got into this situation where um you know we always

**[05:16]** want to have enough capacity to build something that we can't quite see that we're on the horizon yet um and we got into this position with reals where we needed more gpus to train the models right it was it was this big

**[05:32]** evolution for our services where instead of just ranking content from people who you follow or your friends and and whatever Pages you follow um we made this big push to basically start recommending what we call unconnected

**[05:47]** content basically connect content from people or pages that you're not following so now kind of the the Corpus of of kind of content candidates that we could potentially show you expanded from you know on the order of thousands to on

**[06:00]** the order of hundreds of millions so completely different infrastructure and we um started working on on doing that and we were constrained on um on basically the infrastructure that we had to catch up to what Tik Tok was doing as

**[06:15]** quickly as we would have wanted to um so I basically looked at that and I was like hey we have to make sure that we're never in this situation again so let's order enough gpus to do what we need to do on reals and ranking content and feed

**[06:28]** but let's also double that right CU again like our normal principle is there's going to be something on the horizon that we can't see yet did you know it would be AI um well we thought it would be we thought it was going to

**[06:40]** be something that had to do with training large models right I mean but at the time I I thought it was probably going to be more something that had to do with content but I don't know I mean it's it's almost just the pattern

**[06:49]** matching and running the company is there's always another thing right so it's I I'm not even sure I had at that time I was so deep and just you know trying to get you know the recommendations working for reals and

**[07:01]** and other content because I mean that's just such a big unlock for Instagram and Facebook to now being able to show people content that's interesting to them that they're from people that they're not even following but

**[07:11]** um yeah I I that that ended up being a very good decision retrospect yeah yeah okay but it came from being behind it wasn't like I was I you know it wasn't like oh I was so far ahead actually most of the times I think where we kind of

**[07:24]** make some decision that ends up seeming good is because we messed something up before and just didn't want to repeat the mistake uh this is a total detour but I actually want to ask about this while we're on this we'll get back to an

**[07:34]** in AI in a second so you didn't sell for 1 billion but presumably there's some amount you would have sold for right did you write down in your head like I think the actual valuation of Facebook at the time is this and they're not actually

**[07:45]** getting the valuation right like they after $5 trillion of course you would have sold so what like how did you think about that choice yeah I don't know I mean look I think some of these things are just personal

**[07:57]** um I I don't know at the time that I was sophisticated enough to do that analysis I had all these people around me who were making all these Arguments for how like a billion dollars was you know it's like here's the revenue that we need to

**[08:11]** make and here's how big we need to be and like it's clearly so many years in the future like it was it was very far ahead of where we were at the time and I don't know I didn't I didn't really have the financial sophistication to really

**[08:23]** even engage with that kind of debate I just I I think I sort of deep down believe and what we were doing and I I did some analysis um I was like okay well what would I go do if I wasn't doing this it's like well I really like

**[08:40]** building things and I like helping people communicate and I like understanding what's going on with people and the Dynamics between people so I think if I sold this company I'd just go build another company like this

**[08:52]** and I kind of like the one I have so um so I mean you know what's why why right but um um I don't know I I I think a lot of the biggest bets that people make um are often just based on conviction and values um not it's it's actually usually

**[09:10]** very hard to do the analyses trying to connect the dots forward yeah so you've had um Facebook AI research for a long time uh now it's become seemingly Central to your company at what point did making AGI or

**[09:26]** whatever however you considered that mission at what point is that like this is a creek priority of what meta is doing yeah I mean it's been a big deal for a while so we we started Fair um about 10 years ago and the idea was that

**[09:41]** along the way to general intelligence or AI like full AI whatever you want to call it they're going to be all these different Innovations and that's going to just improve everything that we do so I we didn't kind of conceive it as a

**[09:55]** product it was more kind of a research group and over the last 10 years it has created a lot of different things that have basically improved all of our products um and advanced the field and allowed other people in the field to

**[10:09]** create things that have improved our products too so I think that that's been great but there's obviously a big change um yeah in the last few years when you know chat GPT comes out um the diffusion models are on image creation come out

**[10:23]** and like I mean this is some pretty wild stuff right that that I think is like pretty clearly going to affect how how people interact with like every app that's out there so I at that point we started a second group um the the Gen

**[10:39]** group um with the goal of basically bringing that stuff into our product so building leading Foundation models that would that would sort of power all these different products and initially when we started doing that um the theory at

**[10:54]** first was hey a lot of the stuff that we're doing is is pretty social right so you know it's helping people interact with creators helping um people interact with businesses to you know so the businesses can sell things or do

**[11:07]** customer support or um you know basic assistant functionality for um you know whether it's for our apps or the smart glasses or or VR like all these different things so initially it wasn't completely clear that you were going to

**[11:23]** need kind of full AGI um to be able to support those use cases but then through working on them I think it's actually become clear that you do right in all these subtle ways so for example you know for llama 2 when we were working on

**[11:35]** it we didn't prioritize coding and the reason why we didn't prioritize coding is because people aren't going to ask meta AI a lot of coding questions in WhatsApp no they will right well I don't know I'm not sure that WhatsApp is like

**[11:46]** the UI that people are going to be doing a lot of coding questions so you're like all right look in terms of the things that you know or or Facebook or Instagram or you know those those different Services maybe maybe the

**[11:55]** website right meta doai that we're we're launching I think but but the the thing that was sort of I think has has been a you know somewhat surprising result over the last um you know 18 months is that it it turns out that coding is important

**[12:10]** for a lot of domains not just coding right so even if people aren't asking coding questions to the models um training the models on coding helps them um just be more rigorous and answer the question and and kind of um help reason

**[12:23]** across a lot of different types of domains okay so that's one example where it's like all right so for llama 3 we like really focused on training it with of coding because it's like all right that's going to make it better on all

**[12:31]** these things even if people aren't answering aren't asking primarily coding questions reasoning I think is another example it's like okay yeah maybe you want to chat with a Creator or you know you're a business and you're trying to

**[12:43]** interact with a customer you know that interaction is not just like okay the person sends you a message and you just reply right it's a it's like a multi-step interaction where you're trying to think through how do I

**[12:54]** accomplish the person's goals and um you know a lot of times when a customer comes they don't necessarily know exactly what they're looking for or how to ask their questions so it's not really the job of the AI to just respond

**[13:05]** to the question it's like you need to kind of think about it more holistically it's really becomes a reasoning problem right so if someone else you know solves reasoning or makes good advances on reasoning and we're sitting here and

**[13:15]** with a basic chatbot then like our product is lame compared to what other people are building so it's like so okay so at the end of the day we've got we you know we basically realized we've got to solve general intelligence um and we

**[13:29]** just kind of Ed the anti and the investment to make sure that we could do that so the version of llama that um that uh that's going to solve all these use cases for users is that the version that will be powerful enough to like

**[13:43]** replace a programmer you might have in this building I mean I just think that all this stuff is going to be Progressive over time but in case Lama 10 um I I mean I think that there's a lot

**[13:55]** baked into that question I'm not sure that we're replacing people as much as giving people tools to do more stuff is a programmer in this building 10x more productive after I would hope more but um but no I mean look I I I'm not I

**[14:08]** don't believe that there's like a single threshold of intelligence for for Humanity because I mean people have different skills I at some point I think that AI is going to be um is is probably going to surpass people at most of of

**[14:20]** those things depending on how powerful the models are but um but I think it's Progressive and I I don't think AGI is one thing I think it's you're basically adding different capabilities so multimodality is is kind of a key one

**[14:33]** that we're focused on now initially with photos and images and text but eventually with videos and then because we're so focused on the metaverse kind of 3D type stuff is important um one modality that I'm pretty focused on that

**[14:47]** I haven't seen as many other people in the industry um focus on this is sort of like emotional understanding like I mean so much of of the human brain is just dedicated to understanding people and in kind of like understanding your

**[15:00]** expressions and emotions and think that that's like its own whole modality right that um I mean you could say okay maybe it's just video or image but it's like clearly a very specialized version of those too so there's all these different

**[15:12]** capabilities that I think you want to basically train the models to focus on as well as um getting a lot better at reasoning getting a lot better at memory which I think is is kind of its own whole thing it's I mean I don't think

**[15:23]** we're going to be you know primarily shoving context or or or kind of things into a query cont text window um in the future to to ask more complicated questions I think that there will be kind of different stores of memory or

**[15:35]** different custom models that um that are maybe more personalized to people but I don't know I think that these are all just different capabilities and then obviously making them big and small we care about both because you know we want

**[15:46]** to you know if you're running something like meta AI then we have the ability to that's pretty server based um but we also want it running on smart glasses and you know there's not a lot of space in smart glasses so um you want to have

**[15:58]** something that's efficient for that what is the use case that if you're doing tens of billions of dollars worth of inference or even eventually hundreds of billions of dollars worth of inference if you're using intelligence in an

**[16:08]** industrial scale what is the use case is it is it simulations is it the AI that will be in the metaverse where what we be using the data centers for um I mean our bet is that it's GNA this

**[16:21]** is basically going to change all of the products right so I I think that there's going to be a kind of meta AI General assistant product and I think that that will shift from something that feels more like a chatbot

**[16:34]** where it's like you just ask a question it kind of formulates an answer to things where you're increasingly giving it more complicated tasks and then it goes away and does them so that's going to take a lot of inference it's going to

**[16:44]** take a lot of compute in other ways too um then I think that there's a big part of what we're going to do that is um like interacting with other agents for other people so whether it's businesses or creators um I guess a big part of my

**[17:01]** theory on this is that there's not just going to be like One Singular AI that you interact with because I think um you know every business is going to like want an AI that represents their interests they're not going to like want

**[17:11]** to primarily interact with you through an AI that is going to sell their competitors customers so uh sorry they competitors products um so um uh so yeah so I think creators is going to be a big one I me we there are

**[17:25]** about 200 million creators on our platforms all basically have the pattern where um they want to engage their Community but they're limited by hours in the day and their Community generally wants to engage them but they don't have

**[17:37]** they're limited by hours in the day um so if you could create something where um an AI could basically or that Creator can basically own the AI and train it in the way that they want um and can engage their Community I I think that that's

**[17:52]** going to be super powerful too so um so I think that there's going to be a ton of Engagement across all these things um but these are just the consumer use cases I mean I think when you think about stuff like I mean you know I run

**[18:05]** like our foundation right Chan Zuckerberg initiative with my wife and you know we're doing a bunch of stuff on science and um and there's obviously a lot of AI work that where that I think is going to advance science and

**[18:16]** Healthcare and all these things too so I that it's like there's a this is I think going end up affecting basically every area of the products and and and the and the uh the economy the thing you mentioned about an AI that can just go

**[18:27]** out and do something for you that's multi-step is that a bigger model is that you'll make like llama 4 will still there'll be a version that's still 70b but will just be you'll just turn it on the right data and that will be super

**[18:38]** powerful how like what does the progression look like is it scaling is it just same size but different banks like you were talking about [Music] um I I don't know that we know the

**[18:51]** answer to that so I think one thing that is seems to be a pattern is that you have the Llama uh sorry the the the Llama model and then you build some kind of other application specific code around it right so some of it is is

**[19:07]** the fine tuning for the use case but some of it is just like Logic for okay how um like how Medi should integrate like should work with tools like Google or Bing to bring in real-time knowledge I mean that's not part of the Bas llama

**[19:21]** model that's like part of a okay so for llama 2 we had some of that and it was a little more kind of hand engineered and then part of our goal for llama 3 was to bring more of that into the model itself and but for llama 3 as we start getting

**[19:37]** into more of these agent-like behaviors I think some of that is going to be more hand engineered and then I think our goal for llama four will be to bring more of that into the model so I think at each point like at each step along

**[19:49]** the way you kind of have a sense of what's going to be possible on the horizon you start messing with it and hacking around it um and then I think that that helps you hone your intuition for what you want to try to train into

**[20:01]** the next version of the model itself interesting which makes it more General because obviously anything that you're hand coding is um you know you can unlock some use cases but it's just inherently brittle and

**[20:12]** non-general hey everybody real quick I want to tell you about a tool that I wish more applications used so obviously you've noticed every single company is trying to add an AI chat bot to their website but as a user I usually find

**[20:27]** them really annoying cuz to give these long generic often useless answers command bar is a user assistant that you can just embed into your website or application and it feels like you're talking to a friendly human support

**[20:40]** agent who is browsing with you and for you and it's much more personalized than a regular chatbot it can actually look up users history and respond differently based on that it can use apis to perform actions it can even practically nudge

**[20:56]** users to explore new features one thing that I think is really cool is that instead of just outputting text command bark can kind of just say here let me show you and start browsing alongside the user anyways they're in a bunch of

**[21:09]** great products already you can learn more about them at commandbar doccom thanks to them for sponsoring this episode and now back to Mark when you say into the model itself you train it on the thing that you want in the model

**[21:23]** itself but what do you mean by into the model itself well I mean I think like the the example that I gave llama 2 where you know it's we we really I mean for llama 2 the tool use was very very specific um whereas llama 3 has the

**[21:39]** ability to has much better tool use right so so we don't have to like hand code all the stuff to have it use Google to to go do a search um it just kind of can do that um so and similarly for coding and and kind of running code and

**[21:55]** just a bunch of stuff like that and um but I think once you kind of get that capability then you get a peak of okay well what can we start doing next okay well I don't necessarily want to wait until llama four is around to start

**[22:08]** building those capabilities so let's start hacking around it and um so you do you do a bunch of hand coding and that makes the um the products better if for the interim but then that also helps show the way of what we want to try to

**[22:19]** build into the next version of the model what is the community fine tune of llama 3 you're most excited by maybe not the one that will be most useful to you but justess you'll just enjoy playing it with the most

**[22:29]** they like fine tun it on Antiquity and you'll just be like talking to Virgil or something what are you excited about I don't know um I I think the nature of the stuff is it's like you get surprised right so I think like any any specific

**[22:44]** thing that I sort of thought would be valuable we'd probably be building right so um but I I think you'll get distilled versions I think you'll get kind of smaller versions I mean I mean one thing

**[22:58]** that that I think is 8 billion I don't think is quite small enough for for a bunch of use cases right I think like over time I'd love to get you know a billion parameter model or a two billion parameter model

**[23:11]** or even like a I don't know maybe like a 500 million parameter model and see what you can do with that because I mean as as they start getting if it if with 8 billion parameters were basically nearly as

**[23:21]** powerful as the largest llama 2 model then with a billion parameters you should be able to do something that's interesting right and faster um good for classification or a lot of kind of like basic things that people do before um

**[23:35]** kind of understanding the intent of a of a user query and feeding it to the most powerful model to to kind of hone what what the what the prompt should be um so I don't know I think that's one thing that maybe the community can help fill

**[23:46]** in but I mean we'll we'll also we're also thinking about getting around to distilling some of these ourselves but and right now the gpus are uh Peg training the 405 so what okay so you have all these gpus uh um uh I think you

**[24:00]** say 350,000 by the end of the year that's the whole Fleet I mean I was we we built two I think it's like 22 24,000 clusters that are kind of the single clusters that we have for training the big models I mean I obviously across a

**[24:15]** lot of the stuff that we do a lot of our stuff goes towards training like reals models and and like Facebook news feed and Instagram feed and then inference is a huge thing for us because we serve a ton of people right so our ratio of

**[24:27]** inference compute required to um to training is probably much higher than most other companies that are doing this stuff just because the sheer volume of the community that we're serving so yeah yeah that was really interesting in the

**[24:40]** material they shared with me before that you trained it on more data than is compute optimal just for training because the inference is such a big deal for you guys and also for the community that it makes sense to just have this

**[24:50]** thing have trillions of tokens in there yeah yeah although and one of the interesting things about it we saw even with the 70 billion is we we thought would get more saturated at um at you know it's like we trained on around 15

**[25:03]** trillion tokens we I guess our prediction going in was that it was going to ASM toote more but even by the end it was still learning right it's like we we probably could have fed it more tokens and it would have gotten

**[25:18]** somewhat better but I mean at some point you know you're running a company you need to do these meta reasoning questions of like all right how do I want to spend our gpus on like training this 70 billion model further do we want

**[25:29]** to kind of get on with it so we can start testing hypotheses for llama 4 so we kind of needed to to make um to make that call and I think we got it I think we got to a reasonable balance for for this version of the 70 billion um there

**[25:43]** will be others in the future where you know the 70 billion multimodal one that'll come um over the next period but um but yeah I mean it's that was that was fascinating that you can just that that it's the architectures at this

**[25:53]** point can just take so much data yeah that's really interesting so what does this imply about future models I you mentioned that the Llama 38b is better than the Llama 270b no no it's nearly as good okay I don't over but does that

**[26:06]** mean like the Lama magnitude does does that mean like the Llama 470b will be as good as the Llama 3 405b like what does the future this like this one of the great questions right that I think no one knows um is is

**[26:18]** basically you know it's it's one of the trickiest things in the world to plan around is when you have an exponential curve how long does it keep going for yeah and um I think it's likely enough that it will

**[26:31]** keep going that it is worth investing the um tens or you know 100 billion plus in building the infrastructure to um assume that if that kind of keeps going you're going to get some really amazing things that are just going to make

**[26:45]** amazing products but I don't think anyone in the industry can really tell you that it will continue scaling at that rate for sure right in general you know in history you hit bottlenecks at certain points and now there's so much

**[27:00]** energy on this that maybe those bottlenecks get knocked over pretty quickly but um but I don't know I think that that's that's an interesting question what does a world look like where there aren't these bottlenecks you

**[27:11]** know suppose like progress just continues uh at this pace which seems like plausible um like zooming out for they're gonna be different bottlenecks right so if not training then like yeah go ahead well I think at some

**[27:25]** point you know over the last few years I think there's this issue of um GPU production yeah right so even companies that had the models uh sorry that had the money to pay for the gpus um couldn't necessarily

**[27:39]** get as many as they wanted because there was there were all these Supply constraints now I think that's sort of getting less so now I think you're seeing a bunch of companies think about wow we should just like really invest a

**[27:52]** lot of money in building out these things and I think that will go for um for some period of time um I think there's a there is a capital question of like okay at what point does it stop being worth it to put the

**[28:06]** capital in but I actually think before we hit that you're going to run into energy constraints right because um I just I mean I don't think anyone's built a gigawatt single training cluster yet right and um and then you run into these

**[28:21]** things that just end up being slower in the world like getting energy permitted is like a very heavily regulated government function right so you're going from on the one hand software which is somewhat regulated I i' I'd

**[28:36]** argue that it is more regulated than I think a lot of people in the in the in the Tech Community feel although it's obviously different if you're starting a small company maybe you feel that less if you're a big company you know we just

**[28:46]** interact with people different governments and Regulators are you know we have kind of lots of rules that we need to kind of follow and make sure we do a good job with around the world um but I think that there's no doubt that

**[28:58]** energy and if you're talking about building large new power plants or large builds and then building transmission lines that cross other private or public land that is just a heavily regulated thing so

**[29:11]** you're talking about many years of lead time so if we wanted to stand up just some like massive facility um to power that I I think that that is that's that's a very long-term project right and um so I don't know I I think that

**[29:29]** that's I think people will do it I don't but but I don't think that this is like something that can be quite as magical as just like okay you get a level of AI and you get a bunch of capital and you put it in and then like all of a sudden

**[29:39]** the models are just gonna kind of like it just like I think you you do hit different bottlenecks along the way yeah is there something a project maybe I related maybe not that even a company like meta doesn't have the resources for

**[29:51]** like if you're R&D budget or your capex budget was 10x what it is now then you could pursue it like it's in the back of your mind but meta today and maybe you could like even you can't even issue stock or bond for it it's like just 10x

**[30:02]** bigger than your budget well I think energy is one piece yeah right um I think we would probably build out bigger clusters than we currently can if we could get the energy to do it so I think that that's um

**[30:18]** that's fundamentally money bottlenecked in the limit like if you had a trillion dollar I think it's time right um well if you look at it terms of but it depends on how far the the exponential curves go right like I think a number of

**[30:32]** companies are working on you know right now I think you know like a lot of data centers are on the order of 50 megawatts or 100 megawatts or like a big one might be 150 megawatts okay so you take a whole Data Center and you fill it up

**[30:43]** with just all the stuff that you need to do for training and you build the biggest cluster you can I think you're that's kind of I think a bunch of companies are running at stuff like that um but then when you start getting into

**[30:56]** building a data center that's like 300 megawatt or 500 megawatt or a gwatt I just I mean just no one has built a single gwatt data center yet so I think it will happen right I mean this is only a matter of time but it's it's not going

**[31:09]** to be like next year right it's um I think that some of these things will take I don't know some some number of years to to build out and then the question is okay well if you I mean just to I guess put this in

**[31:24]** perspective I think a gigawatt it's a like around the size of like a meaningful nuclear power plant only going towards training a model didn't didn't Amazon do this there's like they have a 950 G megawatt uh yeah

**[31:39]** I'm I'm not exactly sure what you did You' have to what they did you'd have to ask them um um but it doesn't have to be in the same place right if distributed training works it can be distri that I think is a big question right is

**[31:49]** basically how that's going to work and I I do think in the future it seems quite possible that more of what we call training for these big models is actually more along the lines of inference generating synthetic data to

**[32:05]** then go feed into the model so I don't know what that ratio is going to be but I I consider um the generation of synthetic data to be more inference than training today but obviously if you're doing it in order to train a model it's

**[32:17]** it's part of the broader training process so um I don't know that's an that's a an open question is to to kind of where what the balance of that and how that plays out if that's the case would that potentially also be the case

**[32:30]** with llama 3 and maybe like llama four onwards where you put this out and if somebody has a ton of compute then using the models that you've put out you can just keep making these things arbitrarily smarter like some Kuwait or

**[32:42]** UAE or some random country has a ton of compute um and they can just uh actually just use lamama for to just make something much smarter um I I do think that there are going to

**[32:54]** be Dynamics like that but I I also think that there is a fundamental limitation on um on kind of the network architecture right or the the kind of model architecture right so I think like a 70

**[33:10]** billion model that kind of we trained with the Llama 3 architecture can get better right it can it can keep going like I like I was saying it's you know we felt like if we kept on feeding it more data or rotated the high value

**[33:23]** tokens through again then then you know it would continue getting better but and and we've seen a bunch of other people around the world um you know different companies basically take the Llama 2 70 billion base like take that

**[33:37]** model architecture and then build a new model um it's still the case that when you make a generational Improvement to the kind of llama 3 70 billion or the Llama 3 45 there's nothing open source

**[33:48]** anything like that today right like a it's it's not I think that that's like it's a big step function and what people are going to be able to build on top of that I don't think can go infinitely from there I think it can there can be

**[34:01]** some optimization in that until you get to the next step function yeah okay so let's zoom out a little bit from uh specific models and even the many EUR lead times you would need to get energy approvals and so on like big picture

**[34:14]** these next couple of decades sure what's happening with AI um is does it feel like another technology like metaverse or social or does it feel like a fundamentally different thing in the course of human

**[34:26]** history um I think it's going to be pretty fundamental I think it's going to be more like the creation of computing in the first place right so um you'll get all these new

**[34:41]** apps in the same way that when you got the web or you got mobile phones you got like people basically rethought all these experiences and a lot of things that weren't possible before now became possible um so I think that will happen

**[34:55]** but I think it's a much lower level Innovation it's um it's it's going to be more like going from people didn't have computers to people have computers is my my sense um but it's also it's it's

**[35:10]** uh I don't know it's it's very hard to reason about exactly how this goes I I tend to think that you know in like the cosmic scale obviously it'll happen quickly over a you know couple of decades or something

**[35:25]** but I I do think that there there some set of people who are afraid of like you know it really just kind of spins and goes from being like somewhat intelligent to extremely intelligent overnight and I just think that there's

**[35:36]** all these physical constraints that make that so that that's unlikely to happen um I I I I just don't I don't really see that that playing out so I think you'll have I think we'll have time to kind of acclimate a bit but it will really

**[35:48]** change the way that we work and give people all these creative tools to do different things that they yeah I think I think it's going to be it's it's going to really enable people to do the things that they want a lot

**[36:01]** more is my view um okay so maybe not overnight but is it your view that like on a cosmic scale if you think like humans evolved and then like AI happened and then they like went out through the Galaxy or maybe it takes many decades

**[36:15]** maybe it takes a century but like Bill is that like the grand scheme of what's happening right now in history um sorry in what sense I mean in the sense that there were other Technologies like computers and even

**[36:26]** like fire but like the AI happening is as significant as like humans evolving in the first place I I think that's tricky um I think people like to you the history of humanity I think

**[36:39]** has been people basically you know thinking that certain aspects of humanity are like really unique in different ways and then coming to grips with the fact that that's not true but humanity is actually

**[36:57]** still super special right so it's um it's like we thought that the Earth was the center of the universe and it's like it's not but like it's like humans are still pretty awesome right and pretty unique um I think that another

**[37:13]** bias that people tend to have is thinking that intelligence is somehow kind of fundamentally connected to life and it's not actually clear that it is right I I think like like people think that

**[37:30]** um I mean I don't know that we have a clear enough definition of Consciousness or um or or or life to kind of fully um interrogate this but I there there's all this science fiction about okay you create intelligence and now it like

**[37:46]** starts taking on all these human like behaviors and and things like that but I actually think that the current incarnation of all this stuff at least kind of feels like it's going in a direction where intelligence can be

**[37:56]** pretty sep separated from Consciousness and agency and things like that that um I think just makes it a super valuable tool so I I don't know I mean obviously it's it's um it's very difficult to predict what direction the stuff goes in

**[38:09]** over time which is why I I don't think anyone should be dogmatic about you know how they plan to develop it or what they plan to do I think you want to kind of look at like each release you know it's like we're obviously very pro-op Source

**[38:22]** but I haven't committed that we're going to like release every single thing that we do but it's basically we I I'm I'm just generally very inclined to thinking that open sourcing it is going to be good for the community and and also good

**[38:33]** for us right because we'll we'll benefit from from the Innovations um but if it at some point like there's some qualitative change in what the the thing is capable of and we feel like it's just not responsible to open source it then

**[38:45]** we won't but um so I don't know it's it's it's all it's all very difficult to predict yeah um what is a kind of qualitative change like a specific thing you're training llama 5 Lama four and and you've seen this and like you know

**[38:59]** what I'm not sure about open sourcing it um I think that that it's a little hard to answer that in the abstract because there are negative behaviors that any product can exhibit that as long as you can mitigate it it's like it's okay

**[39:17]** right so um I me there's bad things about social media that we work to mitigate right there's bad things about llama 2 that we spend a lot of time trying to make sure that it's not like you know helping people commit violent

**[39:29]** Acts or things like that right I mean that doesn't mean that it's like a a kind of autonomous or intelligent agent it just means that it's learned a lot about the world and it can answer a set of questions that um we think it would

**[39:40]** be unhelpful for it to answer um so I um I don't know I think the question isn't really what behaviors would it show it's what things would we not be able to mitigate after it shows that and um

**[39:57]** and I don't know I I I think that there's so many ways in which something can be good or bad that it's hard to actually enumerate them all upfront if you even look at like what we've had to deal with in in um you know social media

**[40:10]** and like the different types of harms we've basically gotten to it's like there's like 18 or 19 categories of of harmful things that that people do and we've basically built AI systems to try to go identify what those things are

**[40:22]** that people are doing and try to make sure that that you know doesn't happen on our Network as much as possible so um yeah I think you you can over time I think you'll be able to break down um this into more of a taxonomy too and I I

**[40:33]** think this is a thing that we spend time researching too because we want to make sure that we understand that so one of the things I asked Mark is what industrial scale use of llms would look like you see this in previous

**[40:44]** technological revolutions where at first they're thinking in a very small scale way about what's enabled and I think that's what chat Bots might be for other LMS and I think the large scale use case might look something like what V7 go is

**[40:56]** and by the way made by V7 Labs who is sponsoring this episode so it's like a spreadsheet you put in raw information like documents images whatever and they become rows and the columns are populated by an llm of your choice and

**[41:11]** in fact I used it to prepare for Mark so I fed in a bunch of blog post and papers from meta's AI research and as you can see if you're on YouTube it summarizes as an extracts exactly the information I want as columns and obviously mine is a

**[41:25]** small use case but you can imagine for example a company like FedEx has to process half a million documents a day obviously a chatbot can't do that a spreadsheet can because this is just like a fire hose of intelligence in

**[41:37]** there right anyways you can learn more about them at V7 labs.com slgo or the link in the description back to Mark yeah like uh it seems to me it would be a good idea I I would be disappointed in a future where AI systems aren't broadly

**[41:51]** deployed and everybody doesn't have access to them um at the same time I want to better understand the mitigations um if the mitigation is theine tuning well the whole thing about open weights

**[42:02]** is that you can then um remove the fine tuning which is often superficial on top of these capabilities like if it's like talking on slack with a biology researcher and again I think like models are very far from this they're right now

**[42:14]** they're like Google search um but it's like I can show them my P Tre disc and they can explain like here's why your uh small pox sample didn't grow um here's what to change um how do you mitigate that because somebody can just like

**[42:26]** fine-tune that in there right yeah I mean that's true I think a lot of people will basically use the off-the-shelf model and some people who have basically bad faith are going to try to strip out all the bad stuff so I

**[42:40]** do think that that's an issue the um the flip side of this is that and this is one of the reasons why I'm I'm kind of philosophically So Pro open source is I do think that a concentration yeah of AI in the future

**[42:57]** has the potential to be as dangerous as kind of it being widespread so I think a lot of people are they think about the questions of okay well if we can do this stuff is it bad for it to be out wild like just kind of widely available

**[43:13]** um I think another version of this is like okay well it's probably also pretty bad for one institution to have an AI that is way more powerful than everyone else's AI

**[43:27]** right so if you look at like like I guess one security analogy that I think of is um you know it doesn't take AI to basically okay there's security holes and so many different things and if you

**[43:41]** could travel back in time a year or two years right it's like that's not AI it's like you just let's say you just have like one year or two years more knowledge of the security holes you pretty much hack into like any system

**[43:53]** right so it's not that farfetched to believe that a a very intelligent AI would probably be able to identify some holes um and and basically be like a human who could potentially go back in time a year or

**[44:05]** two and compromise all these systems okay so how have we dealt with that as a society well one big part is open source software that makes it so that when improvements are made to the software it doesn't just kind of get stuck in one

**[44:18]** company's products but it can kind of be broadly deployed to a lot of different systems whether it's Banks or hospitals or government stuff and like just everyone can kind of like as the software gets hardened which happens

**[44:30]** because more people can see it and more people can bang on it um and there and there are standards on how the stuff works um the world can kind of get upgraded together pretty quickly and I kind of think that a world where AI is

**[44:43]** very widely deployed in a in a way where it's gotten hardened um progressively over time and is one where all the different systems will be in check in a way that seems like it is fundamentally more healthy to me than one where this

**[44:58]** is more concentrated so there are risks on all sides but I think that that's one risk that I think people I don't hear them talking about quite as much I think like there's sort of the risk of like okay well what if the AI system does

**[45:13]** something bad I I I am more like you know I stay up at night more worrying well what if like some actor that whatever it's like from wherever you sit there's going to be some actor who you don't trust if they're the ones who have

**[45:26]** like the super strong AI whether it's some like other government that we that that is sort of like an opponent of of of our country or some company that you don't trust or what whatever it is um like I think that that's

**[45:40]** potentially a much bigger risk as in they could like overthrow our government because they have a weapon that like nobody else has cause a lot of mayem right it's I I think it's like I I I I mean I think the intuition is that this

**[45:56]** stuff ends up being pretty kind of important and and um and valuable for both kind of Economic and and kind of security and other things and um I don't know I just think yeah if if like if someone who you you don't trust or is an

**[46:09]** adversary of you gets something that is more powerful then um I think that that could be an issue and I think the probably the best way to mitigate that is to have good open- source um AI that that basically becomes the standard um

**[46:23]** and in a lot of ways kind of can become the leader and um in that way it just it just ensures that it's a much more kind of even and balanced playing field yeah that seems plausible to me and if that works out that would be the future I

**[46:36]** prefer um I I guess I want to understand like mechanistically how if somebody was going to cause Mayhem with AI systems how the fact that there are other open source systems in the world prevents that like the specific example of like

**[46:49]** somebody coming with a bio weapon um is it just that we'll do a bunch of like R&D in the rest of the world to like figure out vaccines really fast like what's happening if you take like the computer the security one that I was

**[46:59]** talking about I think someone with a weaker AI trying to hack into a system that is like protected by a stronger AI will succeed less right so so I think that that's um that's like in terms ofof how do you know everything in the world

**[47:12]** is like that like what if bioweapons aren't like that no I mean I I don't know that everything in the world is like that um um I I think that that's I guess one of the bioweapons are one of the areas where I think the people who

**[47:27]** are most worried about this stuff are focused and and I think that that's uh I it makes a lot of sense to think about that um the and I think that there are certain mitigations you can try to not train certain knowledge into the model

**[47:43]** right there's different things but um but yeah I mean at some level I if you get a sufficiently bad actor and you don't have other AI that can sort of balance them um and understand what's going on and what the threats are then

**[47:59]** um then that could be a risk so I think that that's one of the things that we need to watch out for um is there something you could see in the deployment of these systems where uh you You observe like you're training

**[48:11]** Lama 4 and it's like lied to you because you thought you weren't noticing or something and you're like whoa I what's going on here um not that you this this is probably not likely with L forti system but is there something you can

**[48:22]** imagine like that where you'd like be be really concerned about deceptiveness in and if like billions of copies of things are out in the wild um yeah I mean I think that that's not

**[48:34]** necessarily I mean right now it's we see a lot of hallucinations right so I think it's more more that um um I think it's it's an interesting question how you would tell the difference between a hallucination and deception but yeah I

**[48:47]** look I me I think there's a lot of risks and things to to think about the um the flip side of all this is that there also a lot of I tried to in in in running our company at least balance what I think of as these longer term

**[49:04]** theoretical risks um with what I actually think are quite real risks that exist today so like when when you talk about deception the form of that that I worry about most is people using this to generate misinformation and then like

**[49:19]** pump that through whether it's our networks or others so the way that we've basically combed a lot of the type of harmful content is by building AI systems that are smarter than the adversarial ones and I guess this is

**[49:33]** part of this kind of informs part of my theory on this right is if you look at like the different types of harm that people do or try to do through through social networks um there are ones that are not very

**[49:45]** adversarial so for example like uh hate speech I would say is not super adversarial in the sense that like people aren't getting better at being racist right they're just like it's you just like okay if you

**[50:02]** you kind of that's one where I think the AIS are generally just getting way more sophisticated faster than people are at those issues so we and we have issues both ways it's like people do bad things that whether they're trying to incite

**[50:15]** violence or something um but we also have a lot of false positives right so where we where we basically censor stuff that we shouldn't and I think understandably make a lot of people annoyed so I think having an that just

**[50:27]** gets increasingly precise on that that's going to be good over time but let me give you another example which is like nation states trying to interfere in elections that's an example where they are absolutely they have cuttingedge

**[50:38]** technology and absolutely get better each year so we block some technique they learn what we did they come at us with a different technique right it's not like a person trying to you know I know say say mean things right it's like

**[50:52]** it's it's they're they're basically they have a goal they're sophisticated they have a lot of techn techology um in those cases I I still think the ability to kind of have ouri systems grow and in sophistication at a faster rate than

**[51:05]** theirs have it's an arms race but I think we're at least currently winning that arms race um so I don't know I think that that's but this is like a lot of the stuff that I that I spend time thinking about is like okay yes it is

**[51:19]** possible that whether it's llama 4 or llama 5 or llama 6 yeah we need to think about like what behaviors we're we're observing and it's not just us I think part of the reason why you make this open source is that there are a lot of

**[51:29]** other people who study this too so yeah we want to see what other people are observing what we're observing what we can mitigate and then we'll make our our assessment on whether we can make it um open source but I I think for the

**[51:43]** foreseeable future I'm I'm optimistic we will be able to and in the near term I don't want to take our eye off the ball of what are actual bad things that people are trying to use the models for today even if they're not existential

**[51:56]** but they're like they're like pretty bad kind of day-to-day harms that we familiar with in running our services um that's actually a lot of what we have to I think spend our time on as well yeah yeah um actually I found the synthetic

**[52:10]** data thing really curious uh I'm I'm actually interested in why you don't think uh like current models it makes sense why there might be an ASM toote with just doing the synthetic data again and again if they get smarter and you

**[52:21]** use the kind of techniques you talk about in the paper or the blog post that's coming out um on the day this will be released where it it goes to the thought chain that is the most um correct why you why this wouldn't like

**[52:34]** lead to a loop that over of course it wouldn't be overnight but over many months or years of training potentially with a smarter model it gets smarter makes better output gets smarter and so forth um well I think it could within

**[52:46]** the parameter of whatever the model architecture is it's just that like it's some level I don't know I I think like today's billion parameter models I just don't think you're going to be able to

**[53:01]** get to be as good as the State ofthe art multi hundred billion parameter models that are incorporating new Research into the architecture itself um but those will be open source as well right well yeah but I think that that's

**[53:16]** if I mean subject to all the yeah questions that we just talked about but yes I mean we would we would hope that that'll be the case but but I think that at each point I don't know it's like when you're

**[53:28]** building software there's like a ton of stuff that you can do with software but then at some level you're constrained by the chips that it's running on right so there are always going to be different physical constraints and it's like how

**[53:42]** bigger the models is going to be constrained by how much energy you can get and um and use for inference um so I guess I'm simultaneously very optimistic that the stuff will continue to improve quickly and also a little

**[54:02]** more measured than I think some people are about kind of it's I I I just don't think the runaway case is like a particularly likely one I think it makes sense to keep your options open like

**[54:18]** there's so much we don't know um there's a case in which like it's really important to keep the balance of power so nobody becomes like a totalitarian dictator there's a case in which like you don't want to open source uh the

**[54:28]** architecture because like China's catch can use it to catch up to America's Ai and like there is an intelligence explosion and they like win that um yeah a lot of things possible just like keeping your options open considering

**[54:38]** all of them um seems reasonable yeah um uh let's talk about some other things uh okay uh metaverse what time period in human history would you be most interested in going into a 100,000 BCE to now you just want to see what it was

**[54:53]** like has to the Past huh it has to the Past um I don't know I mean I have the periods of time that I'm interested I I'm really interested in American history and classical history and

**[55:08]** um I'm really interested in the history of science too so I actually think seeing and trying to understand more about how some of the big advances came about I mean all we have are like

**[55:22]** somewhat limited writings about some of that stuff I'm not sure the metaverse is going to let you do that because I mean it's um you know we can't it's going to be hard to to kind of go back in time for things that we don't have records of

**[55:34]** but uh I'm actually not sure that going back in time is going to be that that that important of a thing for them I mean I think it's going to be cool for like history classes and stuff but um that's

**[55:46]** probably not the use case that I'm most excited about for the for the metaverse overall I mean it's um I think the main thing is just the ability to feel present with people no matter where you are I think that's going to be

**[55:56]** I mean there's um I mean in the AI conversation that we that we're having I it's uh you know so much of it is about physical constraints that kind of underly all all of this right and you want to move I think one

**[56:11]** lesson of technology is you want to move things from the physical constraint realm into software as much as possible because software is so much easier to build and and evolve and like you can democratize it more because like not

**[56:24]** everyone is going to have a data center but like a lot of people can can kind of write code and take open source code and and modify it um the metaverse version of this is I

**[56:35]** think enabling realistic digital presence is going to be just an absolutely huge difference for um for making it so that um people don't feel like they have to physically be together for as many things um now I mean I think

**[56:52]** that there are going to be things that are better about being physically together um so it's not I mean these things aren't binary it's not going to be like okay now it's you don't need to do that anymore but

**[57:02]** um but overall I mean I I think that this it's just going to be really powerful for for socializing for feeling connected with people for working um for I don't know parts of industry for medicine for like like so many things I

**[57:20]** I want to go back to something you said at the beginning of the conversation where um you didn't sell the company for a billion dollars and like the metaverse you knew going to do this even though the the market was hammering you for it

**[57:29]** and then I'm actually curious like what is the source of that edge and you said like oh values I have this intuition but like everybody says that right like what if you had to say something that's specific to you what is how would you

**[57:40]** express what that is like why were you so convinced about the metaverse um well I think that those are different questions so what I mean what what are the things

**[57:54]** that that kind of power for me um I think we've talked about a bunch of the themes so it's I mean I I just really like building things um I specifically like building things around how people communicate and sort of

**[58:10]** understanding how people Express themselves and how people work right when I was in college I was I was studied computer science and psychology I think a lot of other people in the industry St studied computer science

**[58:19]** right so um it's uh it's always been sort of the intersection of those two things for me but I think it's also sort of this like really deep Drive I don't know how to explain it but I just feel like in

**[58:35]** like constitutionally like I'm doing something wrong if I'm not building something new right and um so I think that there's like you know even when we're putting together the business case for you know

**[58:53]** investing like a hundred billion in AI or some huge amount in the metaverse it's like yeah I mean we have plans that I think make it pretty clear that if our stuff works it'll be a good investment but like you can't know for certain from

**[59:07]** the outset and um so there's all these arguments that people have you know whether it's like you know with advisers or or different folks it's like well how how could you like it's how are you confident enough to do this and it's

**[59:20]** like well the day I stop trying to build new things I'm just I'm going to go build new things somewhere else right it's like um it's like it is I I'm fundamentally incapable

**[59:35]** of running something or in my own life and like not trying to build new things that I think are are interesting it's like that's not even a question for me right it's like whether like whether we're going to go take a swing at like

**[59:48]** building the next thing it's like it's I like I'm I'm just incapable of not doing that um and I don't know I and I'm kind of like this in like all the different aspects of my life right it's like we built this like

**[1:00:04]** our family built this Ranch in Kawaii and like I just like work like design all these buildings I'm like kind of trying to like we started raising cattle and I'm like all right well I want to make like the best cattle in the world

**[1:00:18]** right so it's like how do we like how do we architect this so that way we can figure this out and like and build all the stuff up that we need to to try to do that um so I don't know that's me um what was

**[1:00:29]** the other part of the question look meta is just a really amazing tech company right they have all these great software engineers and even they work with Strife to handle payments and I think that's just a really notable

**[1:00:41]** fact that strip's ability to engineer these checkout experiences is so good that big companies like Ford Zoom Meta Even openai they work with stripe to handle payments because just think about how many different possibilities you

**[1:00:53]** have to handle if you're in a different country you'll pay a different way and if you're buying a certain kind of item that might affect how you decide to pay and stripe is able to test these fine grained optimizations across tens of

**[1:01:04]** billions of transactions a day to figure out what will convert people and obviously conversion means more revenue for you and look I'm not a big company like meta or anything but I've been using Stripes since long before they

**[1:01:15]** were advertisers stripe Atlas was just the easiest way for me to set up an LLC and they have these payments and invoicing features that make it super convenient for me to get money from advertisers and obviously without that

**[1:01:27]** it would have been much harder for me to earn money from the podcast and so it's been great for me go to stripe.com to learn more thanks to them for sponsoring the episode now back to Mark I'm not sure but that I'm actually curious about

**[1:01:38]** something else which is um um so 19y old Mark um reads a bunch of like Antiquity and Classics uh High School College what important lesson did you learn from it not just interesting things you found but like there aren't that many tokens

**[1:01:52]** who consume by the time you're 19 a bunch of them were about the classics clearly that was important in some way tokens you um I don't know that's a good question I

**[1:02:07]** mean one of the things I thought was really fascinating is um so when Augustus was first so he he became emperor and um and he was trying to establish peace and

**[1:02:26]** the there was no real conception of Peace at the time like the people's people's understanding of Peace was it is the temporary time between when your enemies will inevitably attack you again so you get like a short rest and and he

**[1:02:42]** had this view which is like look like we want to change the economy from instead of being so mercenary and like and kind of militaristic to like actually this positive some thing it's like a very

**[1:02:55]** novel idea at the time um I don't know I think that there's like something that's just really fundamental about that it's like in terms of the the bounds on like what people can conceive at the time of like

**[1:03:11]** what are rational ways to work and um I don't know going back to like I this applies to both the metaverse and the AI stuff but like a lot of investors and just different people just can't wrap their head around why we would open

**[1:03:24]** source this and it's like are like like I don't understand it's like open source that must just be like the temporary time between which you're making things proprietary right and it's um but but I actually think it's like this very

**[1:03:40]** profound thing in Tech that has actually it it creates a lot of winners right and it's and and um so I don't know I don't want to strain the analogy too much but but I do think that there's um there's a lot of times I think ways where you

**[1:03:58]** can that are just like models for building things that people can't even like they just like often can't wrap their head around how that would be a valuable thing for people to go do or like a

**[1:04:11]** reasonable state of the world that it's I I mean it's uh I think there's more reasonable things than people think that's super fascinating um can I give you my answer what I was thinking you might have

**[1:04:24]** gotten from it um this is probably totally off but um just how young some of these people are who have very important roles in the Empire like Caesar Augustus is like by the time he's 19 he's actually incredibly one of the

**[1:04:36]** most prominent people in Roman politics and he's like leading battles and forming the second tribe it I wonder if you like the 19-year-old is like I can actually do this because like this I think that's an interesting example both

**[1:04:47]** from a lot of history and American history too I mean it's um I mean one of my favorite quotes is it's this quote that all children are artists and the challenge is how do you remain an artist when you grow up and

**[1:05:00]** it's like basically I think because when you're younger I think it's just easier to have kind of wild ideas and you're not you know you have no there are all these analogies to the innovators dilemma that exist in your life as well

**[1:05:17]** as your company or whatever you've built right so you know you're kind of earlier on your trajectory it's easier to Pivot and take in new ideas without a disrup in other commitments that you've made to to different things and

**[1:05:30]** um so I don't know I think that's an interesting part of of running a company is like how do you how do you kind of stay Dynamic um going back to the investors in open source uh the 101 billion model

**[1:05:42]** suppose it's is totally safe you've done these evaluations and um unlike in this case the evaluators can also fine-tune the model um which hopefully will be the case in future models uh would you open source that the $10 billion model well I

**[1:05:55]** mean as long as it's helping us then yeah but would it like to $10 billion of R&D and then now it's like open source for any well I think here's I think a question which we we'll have to evaluate this as as time goes on too but

**[1:06:09]** um we have a long history of open sourcing software right we don't tend to open source our product right so it's not like we take we don't take like the code for Instagram and make it open source but we take like a lot of the

**[1:06:21]** low-level infrastructure and we make that open source right the the probably the biggest one in our history was open compute project where we took the designs for kind of all of our um our servers and network switches and data

**[1:06:35]** centers and made it open source and ended up being super helpful because you I mean a lot of people can design servers but now like the industry standardized on our design which meant that the supply chains basically all got

**[1:06:46]** built out around our design and the volumes went up so it got cheaper for everyone and saved us billions of dollars so awesome right okay so there's multiple ways where open source I think could be helpful for us one is if people

**[1:06:59]** figure out how to run the models more cheaply well we're going to be spending tens or like a hundred billion dollars or more over time um on all this stuff so if we can do that 10% more effectively we're saving billions or

**[1:07:11]** tens of billions of dollars okay that's probably worth a lot by itself um especially if there's other competitive models out there it's not like our thing is is like be giving away some kind of crazy Advantage um so is your view that

**[1:07:24]** the trading will be commodified um I think there's a bunch of ways that this could play out that's one the um the other is is that so commodity kind of implies that it's going to get very cheap

**[1:07:40]** because um there's lots of options the other direction that this could go in is qualitative improvements so um so you mentioned fine tuning right it's like right now it's it's um you know it's pretty limited what you can do with

**[1:07:52]** fine-tuning major other models out there and some options but generally not for the biggest models um so I think being able to do that and and be able to kind of do different app specific things or use case specific things or build them

**[1:08:07]** into specific tool chains um I think we'll not only enable kind of more efficient development it could enable qualitatively different things um here's one analogy on this is um so one thing

**[1:08:22]** that I think generally sucks about the mobile ecosystem is that like you have these two gatekeeper companies Apple and Google that can tell you what you're allowed to build and there are lots of times in our

**[1:08:34]** history so there's the economic version of that which is like all right we build something they're just like I'm going to take a bunch of your money but then there's the there's the um the qualitative version which is actually

**[1:08:44]** what kind of upsets me more which is there's a bunch of times when we've launched or wanted to launch features and then Apple's just like nope you're not launching that I like that sucks right and um

**[1:08:57]** so the question is what is like are we kind of set up for a world like that with AI where like you're going to get a handful of companies that run these closed models that are going to be in control of the apis and therefore are

**[1:09:11]** going to be able to tell you what you can build um well for one I can say for for us it is worth it to go build a model ourselves to make sure that we're not in that position right like I don't want any of those other companies

**[1:09:23]** telling us what we can build um but from an open source perspective I think a lot of developers don't want those companies telling them what they can build either um so then the question is what is the

**[1:09:35]** ecosystem that gets built out around that what are interesting new things how much does that improve our products um I that there's a lot of cases where if this ends up being like you know like our databases or caching systems or

**[1:09:49]** architecture we'll get valuable contributions from the community that will make our stuff better and then our app specific work that we do will still be so differentiated that it won't really matter right it's like we we'll

**[1:10:00]** be able to do what we do we'll benefit and all the systems ours and the communities will be better because it's open source there is one world where um maybe it's not that I mean maybe the model just ends up being more of the

**[1:10:12]** product itself in that case then I think it's um it's a trickier economic calculation about whether you open source that because then you you are kind of commoditizing yourself a lot but I don't from what I can see so far it

**[1:10:24]** doesn't seem like were're in that zone um do you expect to earn significant revenue from licensing your model to the cloud providers so they have to pay you a fee to actually serve the model um we we want to have an arrangement

**[1:10:37]** like that but I don't know how significant it'll be and we have this um this is basically our license for for llama yeah um you know in a lot of ways it's it's like a very permissive open source license except that we have a

**[1:10:51]** limit for the largest companies using it and this is why put that limit in is we're not trying to prevent them from using it um we just want them to come talk to us because if they're going to just basically take what we built and

**[1:11:02]** resell it and make money off of it then it's like okay well if if you're like you know Microsoft Azure or Amazon then yeah if you're going to reselling the model then we should have some Revenue share on that so just come talk to us

**[1:11:13]** before you go do that and that's how that's played out so for llama 2 it's um I mean we basically just have deals with all these major Cloud companies and llama 2 is available as a hosted service on all those clouds and um I assume that

**[1:11:29]** as we as we release bigger and bigger models that'll become a bigger thing it's not the main thing that we're doing but I I just think if others are if those companies are going to be selling our models it makes sense that we should

**[1:11:37]** you know share the upside of that somehow yeah um with with regards the other open source dangers I think you have like genuine legitimate points about the balance of power stuff um and potentially like the harms you can get

**[1:11:49]** rid of because we have better alignment techniques or something um I wish there was some sort of framework that meta had like other labs have this this where they say like if we see this ex concrete thing then the that's a no-o on the open

**[1:12:00]** source or like even potentially on deployment um just like writing it down so like uh the company is ready for it people have expectations around it and so forth yeah no I think that that's a fair point on the existential risk side

**[1:12:12]** right now we focus more on the types of risks that we see today which are more of these content risks so you know we have lines on we don't want the model to be basically doing things that are helping people commit violence or fraud

**[1:12:27]** or you know just harming people in different ways so um in practice for today's models and I would guess the next generation and maybe even the generation after that I I think while it is somewhat more maybe intellectually

**[1:12:44]** interesting to talk about the in the existential risks I I actually think the the real harms that need more energy being mitigated are things that are going to like to have someone take a model and do something to hurt a person

**[1:12:59]** with today's parameters of of of and kind of the types of kind of more mundane harms that we see today like people kind of committing fraud against each other things like that so um that I just don't want to Short change that I

**[1:13:13]** think we we have a responsibility to make sure we do a good job on that yeah met is a big company you can handle both yeah um uh okay so as far as the opening Source goes I'm actually curious if you think the impact of the open source from

**[1:13:25]** pytorch react open compute these things has been bigger for the world than even the social media aspects of meta because i' like talk to people who use these Services would think like it's plausible because a big part of the internet runs

**[1:13:36]** on these things um it's it's an interesting question I mean I think almost half the world uses our yeah that's cons so um so I I think it's hard to beat that but no I think I think open

**[1:13:53]** sources it's really powerful as a new way of building things and yeah I mean it's possible I me it's you know it may one of these things where I don't know like Bell Labs right where they you know it's like they were

**[1:14:10]** working on the transistor because they wanted to enable longdistance calling and and they did and it ended up being really profitable for them that they were able to enable long-distance calling and if you ask them 5 to 10

**[1:14:23]** years out from that um what was the most useful thing that they invented it's like okay well we enable longdistance calling and now all these people are longdistance calling but if you ask a hundred years later maybe it's a

**[1:14:34]** different question so um I think that that's true of a lot of the things that we're building right reality Labs um some of the AI stuff some of the open source stuff I think it's like the

**[1:14:47]** specific products evolve and to some degree come and go but I think like the advances for Humanity persist and that's like a I don't know cool part of what we all get to do um by when will the Llama models be trained on your own custom

**[1:15:02]** silicon um soon not not not llama 4 um the approach that we took is first we we basically built custom silicon that could handle inference for um our ranking and recommendation type stuff so

**[1:15:20]** reals news feed ads and um that was consuming a lot of gpus but when we were able to move that to our own silicon we now were able to use the more expensive Nvidia gpus only for training so um at some point we will

**[1:15:42]** hopefully have silicon ourselves that we can be using for probably first training some of the simpler things that eventually training these like really large models um but in the meantime I'd say the program

**[1:15:57]** is going quite well and we're just rolling it out methodically and have a long-term road map for it uh final question this is totally out of left field but um if you were made CEO of Google Plus could you have made it work

**[1:16:08]** Google Plus o well I don't know I don't know that's that's a that's a very difficult very difficult counterfactual okay then the real final question will be when Gemini was

**[1:16:21]** launched did you uh was there any chance that somebody in the office caraga Dinda EST no I think we're Tamer now cool cool aome yeah I don't know it's a good question I don't I don't know there the problem is there was no CEO of Goog plus

**[1:16:41]** it was just like a division within a company I think it's like and you asked before about what are the kind of scarcest Commodities but you asked about it in terms of dollars and I I actually think for most companies it's um it's

**[1:16:55]** of this scale at least it's Focus right it's like when you're a startup maybe you're more constrained on Capital um you know you you just are working on one idea and you you might not have all the resources I think you cross some

**[1:17:06]** Threshold at some point where the nature of what you're doing you you're building multiple things and you're creating more value across them but you become more constrained on what can you direct and to go well and

**[1:17:20]** like there's always the cases where something just random awesome happens in the organization I don't even know about it and those are that's great but like but I think in general the organization's capacity is

**[1:17:32]** largely limited by what like the CEO and the and the management team are able to kind of oversee and and kind of manage it's I I think that that's just been a a big Focus for us is like all right keep the as as I guess Ben Horwitz says keep

**[1:17:49]** the main thing the main thing right and and try to kind of stay focused on your key priorities yeah all right awesome that was excellent Mark thanks so much that was a lot of fun yeah really fun thanks

**[1:18:03]** for having me y absolutely hey everybody I hope you enjoyed that episode with Mark as you can see I'm now doing ads so if you're interested in advertising on the podcast go to the link in the description otherwise as you know the

**[1:18:16]** most helpful thing you can do is just share the podcast with people who you think might enjoy it you know your friends group chats Twitter I guess threads yeah hope you enjoyed and I'll see you on the next one

**[1:18:33]** [Music]
