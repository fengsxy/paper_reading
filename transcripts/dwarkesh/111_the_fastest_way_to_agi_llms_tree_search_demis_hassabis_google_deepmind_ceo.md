---
layout: default
type: transcript
series: dwarkesh
episode: 111
guest: ""
title: "The Fastest Way to AGI: LLMs + Tree Search – Demis Hassabis (Google DeepMind CEO)"
source_url: "https://www.youtube.com/watch?v=eqXfhejDeqA"
analysis_url: /transcripts/dwarkesh/111_the_fastest_way_to_agi_llms_tree_search_demis_hassabis_google_deepmind_ceo.analysis/
permalink: /transcripts/dwarkesh/111_the_fastest_way_to_agi_llms_tree_search_demis_hassabis_google_deepmind_ceo/
---

# Transcript: The Fastest Way to AGI: LLMs + Tree Search – Demis Hassabis (Google DeepMind CEO)

Source: https://www.youtube.com/watch?v=eqXfhejDeqA

---

**[00:00]** obviously deep minders at the frontier and has been for many years you know with systems like Alpha zero and so forth of having these agents who can like think through different steps to get to an end outcome um are will this

**[00:10]** just be is a path for llms to have this sort of uh tree search kind of thing on top of them how do you think about this I think that's a super promising Direction in my opinion so you know we've got to carry on improving uh the

**[00:22]** large models and we've got to carry on um basically making the more and more accurate predictors of the world so in effect making them more more reliable World models that's clearly a necessary but I would say probably not sufficient

**[00:34]** component of an AGI system um and then on top of that I would you know we're working on things like Alpha zero like planning mechanisms on top that make use of that model in order to make concrete plans to achieve certain goals in the

**[00:48]** world um and and perhaps sort of chain you know chain thought together or lines of reasoning together and maybe use search to kind of explore massive spaces of possibility I think that's kind of missing from our current large models is

**[01:02]** there any potential for the AGI to eventually come from just a pure RL approach like the the way we're talking about it it sounds like there'll be uh the llm will form the right prior and then this sort of research will go on

**[01:13]** top of that or is there possibility just like completely out of the I think I certainly you know that theoretically I think there's no reason why you couldn't go full Alpha zero like on it and there are some people uh here deep Google Deep

**[01:25]** Mind and and and in the RL Community who work on that right um fully uh no priors uh no data and and just build all knowledge from scratch um and I think that's valuable because of course you could you know those those ideas and

**[01:39]** those algorithms should also work when you have some knowledge too um but having said that I think by far probably my betting would be the quickest way to get to AGI and the most likely plausible way is to um use all the knowledge

**[01:51]** that's existing in the world right now on things like the web and that we've collected and we have these scalable uh algorithms like like um Transformers that are capable of ingesting all of that information and I don't see why you

**[02:04]** wouldn't start with a a model as a kind of Prior or or to build on and to make predictions that helps bootstrap your learning I just think it it doesn't make sense not to make use of that so my my my betting would be is that um you know

**[02:19]** the final AGI system will have these large multimodels um models as part of the the overall solution but probably U won't be enough on their own you will need this additional planning search on top how do you get past the sort of

**[02:32]** immense amount of compute that these approaches tend to require so even the alpago uh system was you know a pretty expensive system um because you had to do the sort of running an LM LM on each node of the tree uh how how do you

**[02:44]** anticipate that'll get more made more efficient well we focus a lot on efficient You Know sample efficient methods and and and reusing uh existing data things like experience replay um and also just looking at uh more

**[02:56]** efficient ways I mean the better your world model is the more efficient your search can be so one example I always give with Alpha zero our system to play go and chess and you know any game is that um it's stronger than world

**[03:08]** champion level human world champion level at all these games um and it uses a lot less search than a brute force method um like deep blue say to play chess deep blue one of these traditional stockfish or deep blue um systems would

**[03:22]** maybe look at millions of uh possible moves for every decision it's going to make alpha zero and Alpha go made you know looked at around T tens of thousands of um possible positions in order to make a decision about what to

**[03:35]** move next but a human Grandmaster a human world champion uh probably only looks at a few hundreds of moves even the top ones in order to make their very uh good decision about what to play next so that suggests that obviously the

**[03:49]** Brute Force systems don't have any real model other than theistic about the game Alpha Zer has quite a decent uh uh model but the but the human you know human top human players have a much richer much more accurate model than of go or chess

**[04:05]** so that allows them to make you know world-class decisions on a very small amount of search so I think there's still there's a sort of tradeoff there like you know if you improve the models then I think your search can be more

**[04:15]** efficient and therefore you can get further with your search yeah I have two questions based on that uh the first being with Alpha's go you had um a very conrete win condition of you know at the end of the day do I win this game ago or

**[04:26]** not and you can reinforce on that how when you're just thinking of like nlm putting out thought what will do you think there will be this kind of ability to discriminate uh in the end whether that was like a good good thing to

**[04:37]** reward or not well of course that's why we you know we pioneered and and Deep Mind sort of famous for using games as a Proving Ground um partly because obviously it's efficient to research in that domain but the other reason is

**[04:49]** obviously it's it's you know extremely easy to specify reward function winning the game or improving the score something like that sort of built into most games so that is the the that is the that one of the challenges of real

**[04:59]** wealth systems is how does one Define uh the right objective function the right reward function um and the right goals um and specify them in a in in you know in a general way but they're specific enough and and and actually points the

**[05:12]** system in the right direction
