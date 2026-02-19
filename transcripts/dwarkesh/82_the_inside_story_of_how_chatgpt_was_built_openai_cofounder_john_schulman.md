---
layout: default
type: transcript
series: dwarkesh
episode: 82
guest: ""
title: "The inside story of how ChatGPT was built – OpenAI cofounder John Schulman"
source_url: "https://www.youtube.com/watch?v=ERpNuLzKmJY"
analysis_url: /transcripts/dwarkesh/82_the_inside_story_of_how_chatgpt_was_built_openai_cofounder_john_schulman.analysis/
permalink: /transcripts/dwarkesh/82_the_inside_story_of_how_chatgpt_was_built_openai_cofounder_john_schulman/
---

# Transcript: The inside story of how ChatGPT was built – OpenAI cofounder John Schulman

Source: https://www.youtube.com/watch?v=ERpNuLzKmJY

---

**[00:00]** you let the creation of Chad jbt at what point do you did you realize first of all these llms are the pat to go and then a Chad bot would be or some way to instruct them would be a useful thing to do before chat gbt open AI had these

**[00:12]** instruction following models and uh that was B the idea there was um we had base models and people can um prompt them in elaborate ways um but uh they're also kind of hard to prompt you had to uh they basically do autocomplete so you

**[00:27]** have to set up a very good prompt with some examples so uh people at open AI uh were working on um just taking the base models and making them easier to prompt so that if you just wrote a question it would

**[00:39]** answer the question instead of giving you more questions or something uh so we had these instruction following models which were kind of like base models but a little easier to use um and those were the original ones deployed in the API or

**[00:52]** after um GPD 3 those were the next uh generation of models um then at the same time there were definitely lot of people thinking about um chat so uh so Google had some papers uh like they had uh Lambda and um earlier Mina so they had

**[01:10]** these chat Bots and it was more like um uh like you had a it was more like a base model that was really specialized to um the task of chat really good at chat and uh like I think at least looking at the examples from the paper

**[01:24]** it was more uh used for sort of fun applications like um where the model would would uh like take on some Persona and pretend to be that Persona it was not so functional like um like help me refactor my

**[01:37]** code um so yeah there are definitely people thinking about chat I had worked on a project before uh looking at chat called uh web GPT which was more about doing question answering with the help of web browsing and retrieval and well

**[01:55]** when you do question answering uh it really wants to be in a chat because um you always want to ask follow-up questions or sometimes you need a clar the the model should ask a clarifying question because the question

**[02:08]** is ambiguous so it was kind of clear after we did the first version of that that we should the next version should be conversational so anyway we started working on uh like a conversational chat assistant um and uh we uh this was built

**[02:25]** on top of GPD 3.5 which was done training at the beginning of 22 and uh that model was quite good at language and code so we quickly realized that it was actually uh quite good at coding help and that was one of the things we

**[02:39]** were excited about so yeah we worked on that uh we worked on that for for most of the year and we had we had browsing um as another feature and it though we ended up uh like deemphasizing that later on because the like the model's

**[02:54]** internal knowledge was so good that we didn't that the browsing um wasn't the most interesting thing about it um and then uh we were thinking about we had it out for beta testing or to friends and family for a while and we

**[03:08]** were thinking about doing a public release um but um at that time uh actually GPD 4 finished training in August or um yeah in August that year and um actually the um like the flagship RL effort at open AI was the instruction

**[03:26]** following effort because that was the models that were being deployed into Productions so um like the first fine tunes of gbd4 used that um that whole stack and that was um yeah those models were really good and everyone got really

**[03:41]** excited about that after seeing the uh like instru fine tun gp4s uh but so they were really really good they would occasionally give you amazing outputs but they were also like a little bit the model was clearly like pretty unreliable

**[03:55]** like it would sometimes hallucinate it a lot and it was like pretty it would sometimes give you pretty unhinged outputs so it was clearly not quite ready for prime time but it was like obviously very good um and uh yeah so I

**[04:08]** guess that um people forgot about chat for a little while after thatc about this like alternative Branch uh but then we we ended up um we pushed it further and we ended up like mixing together all the data sets like the instruct and the

**[04:22]** chat data and to try to get something that was the best of both worlds and uh I think the yeah the models we the chat models were like uh were clearly more um like it was an easy easier to use it was sort of more

**[04:37]** um it sort of uh like automatically had much more sensible behavior in terms of like the model knowing its own limitations the other thing about chat was that when we had these instruct models uh like the task of uh complete

**[04:50]** this text but in a nice way or in a helpful way that's like a pretty poorly defined task so I think uh like I think that task is like both confusing for the model and for the human who's supposed to do the data labeling whereas for chat

**[05:02]** um I think people had an intuitive sense of uh like what a helpful robot should be like so I think it was uh just much easier to tell people uh like uh to to get for people to get the idea of what what the model was supposed to do yeah

**[05:18]** um and uh so that so as a result I think the um like the model had a much more coherent personality and uh like it was much like easier to get um like Rob like sensible behavior um robustly is it the case that anybody could have made Chad

**[05:35]** gbt using your publicly available fine tuning API not exactly I mean uh they could have um I don't remember the status of Which models were available available for fine tuning uh you assuming we had 3.5 available for fine

**[05:52]** tuning at the time you could have made something pretty decently close but I'm not sure you would have um I don't think you would have been able to do just one iteration of fine-tuning where you have like Pur purely human written data and

**[06:05]** you fine tune on that I think you would want like You' want to do several iterations like if you're not going to do RL um which which we did um You' want to do some kind of iterative supervised fine-tuning where you have like humans

**[06:19]** edit the model generated outputs because it's really hard to get people to like if you train on human generated data even if it's really high quality it's just hard for a model to fit that data perfectly because it might not be like

**[06:32]** it might not be something a model is capable of outputting uh so you need to do something iterative that looks a little bit more like RL uh so I think if you had done that you could have gotten something pretty

**[06:44]** close but um that would have been kind of non-trivial um but we also had another uh like instruction following model train with RL that was released a little before

**[06:55]** chat gbt so I think if you put a chat like wrapper on that you would get something decently close uh but it like that model um like if you just prompted it with chat um so but that model had some uh differences in uh strengths like

**[07:13]** it was like that model was pretty good at writing and poetry and so forth but it wasn't uh it sort of it wasn't as good at knowing its limitations and uh at factuality and so forth
