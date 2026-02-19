---
layout: default
type: transcript
series: dwarkesh
episode: 0
guest: ""
title: "LLMs will hit the data wall if they can’t generalize – OpenAI cofounder John Schulman"
source_url: "https://www.youtube.com/watch?v=V6X_tLCxsZk"
analysis_url: /transcripts/dwarkesh/86_llms_will_hit_the_data_wall_if_they_can_t_generalize_openai_cofounder_john_schul.analysis/
permalink: /transcripts/dwarkesh/86_llms_will_hit_the_data_wall_if_they_can_t_generalize_openai_cofounder_john_schul/
---

# Transcript: LLMs will hit the data wall if they can’t generalize – OpenAI cofounder John Schulman

Source: https://www.youtube.com/watch?v=V6X_tLCxsZk

---

**[00:00]** so because there doesn't seem to be a model released since g54 that seems to be significantly better there's seems to be the hypothesis that potentially we're hitting some sort of plateau and that these models aren't actually

**[00:12]** generalizing that well and you're going to hit some sort of data wall Beyond which point the abilities that are unlocked by memorizing a vast Corpus to pre- training data won't actually help you get something much smarter than gbd4

**[00:25]** I mean I wouldn't draw too much from uh the uh time since gbd4 was released because I mean it does um um yeah it takes a while to um like train these models and to um like get all the uh do all the prep to um train a

**[00:43]** new generation of models so uh yeah I wouldn't draw too much from from that fact um I would say um there are definitely some challenges from the limited amount of data um but I wouldn't expect us to immediately hit the data

**[00:57]** wall um but I would expect uh the nature of um pre-training to somewhat change over time as we get closer to it I I think we've talked about some examples generically about generalization one example I was thinking of was the idea

**[01:13]** that there's transfer from langu code reasoning in code if you train a bunch of code it gets better at reasoning and language and if that's is that actually the case do you see things like that which suggest that there's all this crit

**[01:27]** positive transfer between different modalities so once you try training on a bunch of videos and images it'll get smarter and it'll get smarter from synthetic data or does it seem like the abilities that are unlocked are

**[01:38]** extremely local to the exact kind of labels and data you put into the the training Corpus in terms of like uh generalization from different types of pre-training data um I would say it's pretty hard to um do

**[01:55]** science uh on this type of question because you can't do that create that many pre train models so maybe uh you can't train a like a gbd4 Siz model you can't do ablation studies at gbd4 scale U maybe you can do like train a ton of

**[02:11]** um gpd2 size models or maybe even a GPD 3 size model with different data Blends and see what you get uh so I'm not like um aware of any results uh public like public results on um like ablations um involving code data and reasoning

**[02:27]** performance and so forth so that would be I would be very interested to know about those results with with regards to the sort of plateau narrative one of the things I've heard is that a lot of the abilities these

**[02:40]** models have to help you with specific things is related to the having very closely matched labels within the uh Super Wise fine tuning data set uh is that true like if if it can teach me how to use FFM pay correctly like there's

**[02:56]** somebody who's like doing figuring out seeing the inputs and seeing what flags you need to add and some human is figuring that out and smashing to that and is yeah do you need to hire like all these label rollers who have domain

**[03:12]** expertise in all these different domains um because if that's the case it seems like would be a much bigger SLO to get these models to be smarter and smarter over time right you don't exactly need that um because uh yeah you can get

**[03:24]** quite a bit out of generalization um so if you um like uh like the base model has already um been trained on tons of documentation tons of code uh with shell scripts and so forth so it it's already seen all the FFM Peg Man pages and uh

**[03:42]** lots of bash scripts and everything and uh it's um so uh like the base even just giving the base model a good Fus shop prompt you can get it to uh answer queries like this and uh just training a preference model uh like for helpfulness

**[03:59]** will um uh even if you don't train it on um probably even if you don't train it on any stem it'll somewhat generalize to stem so so you not only do you not need uh like examples of how to use FFM tag

**[04:12]** you might not even need anything with programming uh to get some reasonable behavior in uh the programming domain
