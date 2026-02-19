---
layout: default
type: transcript
series: dwarkesh
episode: 90
guest: ""
title: "Can synthetic data unlock AI recursive self-improvement? — Mark Zuckerberg"
source_url: "https://www.youtube.com/watch?v=9TU0XjJqpOg"
analysis_url: /transcripts/dwarkesh/90_can_synthetic_data_unlock_ai_recursive_self_improvement_mark_zuckerberg.analysis/
permalink: /transcripts/dwarkesh/90_can_synthetic_data_unlock_ai_recursive_self_improvement_mark_zuckerberg/
---

# Transcript: Can synthetic data unlock AI recursive self-improvement? — Mark Zuckerberg

Source: https://www.youtube.com/watch?v=9TU0XjJqpOg

---

**[00:00]** one of the interesting things about it we saw even with the 70 billion is we we thought it would get more saturated you know it's like we train it on around 15 trillion tokens we I guess our prediction going in was that it was

**[00:12]** going to ASM toote more but even by the end it was still learning right it's like we we probably could have fed it more tokens and it would have gotten somewhat better but I mean at some point you know you're running a company you

**[00:25]** need to there these meta reasoning questions of like all right how do I want to spend our gpus on like training this 70 billion model further do we want to kind of get on with it so we can start testing hypotheses for llama 4 so

**[00:37]** we kind of needed to to make um to make that call and I think we got it I think we got to a reasonable balance for for this version of the 70 billion that was that was fascinating that you can just that that it's the architectures at this

**[00:48]** point can just take so much data and I I do think in the future it seems quite possible that more of what we call training for these big models is actually more along the lines of inference

**[01:03]** generating synthetic data to then go feed into the model so I don't know what that ratio is going to be but I I consider um the generation of synthetic data to be more inference than training today but obviously if you're doing it

**[01:16]** in order to train a model it's it's part of the broader training process so um I don't know that's an that's a an open question is to to kind of where what the balance of that and how that plays out if that's the case would that potenti

**[01:30]** also be the case with llama 3 and maybe like llama 4 onwards where you put this out and somebody has a ton of compute then using the models that you've put out you can just keep making these things arbitrarily smarter like some

**[01:42]** Kuwait or UAE or some random country has a ton of compute um and they can just uh actually just use Lama for to just make something much smarter I do think that there are going to be Dynamics like that um actually I found the synthetic data

**[01:55]** thing really curious uh I'm I'm actually interested in why you don't think uh like current models it makes sense why there might be an ASM toote with just doing the synthetic data again and again but if they get smarter and use the kind

**[02:06]** of techniques you talk about in the paper or the blog post that's coming out um on the day this will be released where it it goes through the thought chain that is the most um correct why you why this wouldn't like lead to a

**[02:19]** loop that over of course it wouldn't be overnight but over many months or years of training potentially with a smarter model it gets smarter makes better output gets smarter and so forth um well I think it could within

**[02:31]** the parameter of whatever the model architecture is it's just that like at some level I don't know I I think like today's 8 billion parameter models I just don't think you're going to be able

**[02:45]** to get to be as good as the state-of-the-art multi- hundred billion parameter models that are incorporating new Research into the architecture itself when you're building software there's like a ton of stuff that you can

**[02:57]** do with software but then at some level you're constrained by the chips that it's running on right so there are always going to be different physical constraints and it's like how big are the models is going to be constrained by

**[03:11]** how much energy you can get and and use for inference um so I guess I'm simultaneously very optimistic that this stuff will continue to improve quickly and also a little more measured than I think some people are out I I I just

**[03:31]** don't think the runaway case is like a particularly likely one I think it makes sense to keep your options open like there's so much we don't know um there's a case in which like it's really important to keep the balance of power

**[03:43]** so nobody becomes like a totalitarian dictator there's a case in which like you don't want to open source uh the architecture because like China's catch can use it to catch up to America's Ai and like there is an intell explosion

**[03:54]** and they like win that um yeah a lot of things possible just like keeping your options open considering all of them um seems reasonable
