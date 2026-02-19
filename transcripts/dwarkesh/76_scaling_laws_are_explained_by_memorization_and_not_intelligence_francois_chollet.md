---
layout: default
type: transcript
series: dwarkesh
episode: 76
guest: ""
title: "Scaling laws are explained by memorization and not intelligence – Francois Chollet"
source_url: "https://www.youtube.com/watch?v=rl7B-LHiaNo"
analysis_url: /transcripts/dwarkesh/76_scaling_laws_are_explained_by_memorization_and_not_intelligence_francois_chollet.analysis/
permalink: /transcripts/dwarkesh/76_scaling_laws_are_explained_by_memorization_and_not_intelligence_francois_chollet/
---

# Transcript: Scaling laws are explained by memorization and not intelligence – Francois Chollet

Source: https://www.youtube.com/watch?v=rl7B-LHiaNo

---

**[00:00]** general intelligence is not task specific skill scaled up to many skills because there is an infinite space of possible skills general intelligence is the ability to approach any problem any skill and very quickly Master it using

**[00:15]** Val old data because this is what makes you able to face anything you might have ear cont this is what makes uh uh this this is the definition of generality like generality is not specificity scaled up it is uh the ability to apply

**[00:30]** your mind to anything at all to arbitrary things and this requires fundamentally this requires the ability to adapt to learn on the Fly efficiently the scale uh a maximalist argument it boils down to these people they refer to

**[00:44]** scaling LS which is this this empirical relationship that you can draw between how much compute you spend on training model and the performance you're getting on benchmarks right and the the key question here of course is well how do

**[00:57]** you measure performance what it is that you're actually uh improving by adding more comput and more data and well it's it's Benchmark performance right and the thing is the way you measure performance is not a

**[01:10]** technical detail uh it it's it's not it's not an afterthought because it's going to uh narrow down the set of questions that you're asking and so accordingly it's going to narrow down the set of answers that that you're that

**[01:22]** you're looking for if you look at uh the benchmarks we're using for LMS they're all memorization based benchmarks like sometimes they're literally just knowledge based like like a school test and even if you look at the ones that

**[01:35]** are uh you know explicitly about reasoning you realize if you look closely that it's uh in order to solve them it's enough to memorize uh a finite set of uh uh resoning patterns uh and then you just reapply them they they're

**[01:51]** like static programs llms are very good at memorizing CTIC programs small CTIC programs and and they've got this sort of like Bank of uh solution programs and when you give them a new puzzle uh they can just fetch the appropriate program

**[02:07]** apply it and it's looking like it's reasoning but really it's not doing any sort of on thefly program synthesis all it's doing is program fetching so you can actually solve all these benchmarks with memorization and so what what

**[02:21]** you're scaling up here like if you look at the models they are uh big parametric curves uh fitted to a data distribution I descent so they are basically these big interpolative uh databases interpolative memories and of course if

**[02:36]** you scale up the size of your database and you cram into it uh more knowledge more patterns and so on uh you are going to be increasing its its performance as measured by memorization Benchmark that's that's kind of obvious but as

**[02:51]** you're doing it you are not increasing the intelligence of the system one bit you are increasing the skill of the system you you are increasing ining its usefulness its uh scope of applicability but not its intelligence because skill

**[03:05]** is not intelligence and that's the phenomal confusion um that that that people run into is that they're confusing skill and intelligence as far as the interpolation goes so okay let's look at one of the benchmarks here

**[03:19]** there's there's one Benchmark that does great school math and these are problems that like a smart high schooler would be able to solve um it's called GSS 8K and these models get 95% on these like basically they always nail memorization

**[03:34]** okay let's talk about what that means so here's one question about from that Benchmark so 30 students are in a class one/ fifth of them are 12 year olds 1/3 are 13y old 1110th are 11 year olds how many of them are not 11 12 or

**[03:47]** 13 years old so I agree like this is not rocket science right you can write down on paper how you go through this problem and a high school kid at least a smart high school kid should be able to solve it now when you say memorization it's

**[03:59]** still has to reason through how to think about fractions and what is the context of the whole problem and then combining the different calculations is doing it depends how you how you want to Define reasoning but there there are two

**[04:11]** definitions you can use so one is I have available uh a set of program templates it's it's like the structure of the puzzle which which can also generate its solution and I'm just going to identify the right template which is in my memory

**[04:28]** um I'm going to input the new value into the template run the program get the solution and you could say this is reasoning and I say yeah sure okay uh but another definition you can use is reasoning is the ability to when you're

**[04:40]** faced with a with a puzzle given that you don't have already a program in memory to solve it you must synthesize on the fly a new program based on bits of pieces of existing programs that you have you have to do on the Fly program

**[04:55]** synthesis and it's actually dramatically harder than just fetching the right memorized program and replying it I think maybe we are overestimating the extent to which humans are so sample efficient they also don't need training

**[05:09]** in this way where they have to drill in these kinds of Pathways of reasoning through certain kind of problems so let's take math for example yeah it's not like you can just show a baby the axum of SE Theory and

**[05:22]** now they know math right so they when they're growing up you had to do years of teaching them pre-algebra then you got to do a year of teaching them doing d and going through the same kind of problem in algebra then geometry

**[05:33]** pre-calculus calculus absolutely so training yeah but isn't that like the same kind of thing where you you you can't just see one example and now you have the program or whatever you actually had to drill it these models

**[05:42]** also had to drill with a bunch of fruit training data sure I mean in order to do on the-fly program synthesis you actually need uh building blocks to work from so knowledge and memory actually tremendously important in the process

**[05:55]** I'm not I'm not saying it's memory versus reasoning in order to do effective reasoning you need memory
