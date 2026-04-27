---
date:   2026-04-27
title:  "10 years of code smell - Part III: The Missing Review"
description: Making sense out of this mess, the impact of usefulness, and homework for the reader.
tags:   [10-years-of-code-smell, project]
image:  '/images/blog/10-years-of-code-smell-the-missing-review.jpg'
category: blog
---
This is the third and final post in a series about revisiting an old project I worked on in my last year of high school, ten years ago. I recommend taking a look at [the previous part](./10-years-of-code-smell-self-archeology) at least, in which we do a deep dive into the project's (awful) code.

In this post, I explain a bit about the aftermath of the project, some conclusions I reached regarding its implementation, my thoughts on the engineering process, and recommend some further software engineering reading material if you are into that kind of stuff.

# Professionalism and the hostility of the internet

Besides the awful code in Spanish, the whole UI was also in Spanish, because well, I didn't think that english speaking people would be interested. This was only intended to be used by my Spanish-speaking friends and no one else, so when a guy (who previously blocked me for asking him some stuff about Steam profile backgrounds he designed, mind you) asked me if we could work on translating the program together, I was taken aback. Unfortunately, I had to decline as I lost the source code back then, but something I made was useful enough for other people outside my circle to want to use it. I had never had that happen before; it was a nice feeling for sure.

This whole project also included my first ever experience with asking a question to Stack Overflow. I cannot find it right now, I may have deleted it because I feel ashamed, but I was getting this thing in which the text in the UI was transparent, and I could see behind the programs window, which was a bit awkward. So I asked about it and basically got told that I suck and shouldn't expect people to do the work for me.

Mind you, I probably worded my question super badly without the necessary context and in a very broken english, but it made me sad how hostile the answer was that I never ever asked anything in the site again. I am sure there are a lot of unnecessary/badly asked questions in the site made every day that may make useful things harder to find, and the effect that the answer had might have helped improve that by making me avoid asking dumb questions anymore. But I would lie if I say I deserved to be treated like that, and nowadays I would say that such questions are easy targets for other nerds to take it out on an unrelated, easy target. 

Fortunately enough I didn't have such low self-esteem to affect me that deeply, but I can definitely see how, on a bad day, such comments can make an individual walk away from the programming field in its entirety. It's a shame that internet interactions have required us to grow a thicker skin to resist such exchanges, and I am afraid that elitism and lack of empathy have started to make the rounds in real life for some years now, regardless of the field (although I guess you could argue it has always been there).

Nowadays, if I have to ask a question and I cannot find it anywhere on the internet, I would probably go to a subreddit instead. Not that its user base are excellently well behaved either, but my interactions there have been net positives all these years. The thing is tho, when faced with such high friction in online interactions, of course, people would go ask a brainless machine that doesn't judge them for what they ask, regardless if the answer they get is useful or not. Which ties back to my thoughts on the problem of solutions visibility when searching for errors that we may be facing in the close future from the [first part of this series](./10-years-of-code-smell-falling-for-cs).

In more light-hearted topics, one of the guys in this gaming forum I participated in made me the slickest icon ever for the calculator, and it's probably the coolest part of the project:

<p align="center"><img src="/images/blog/10-years-of-code-smell-the-missing-review/steam_calculator_icon.png"></p>

As a thank you to all the people who gave me a hand testing this (and because I thought it was funny, I guess), I also released a version with insulting comments when the user got an error. I guess it was fun given my age back then, but nowadays I it wouldnt even cross my mind to do something like this. So I have either gotten more professional with the years, or more boring. Probably both.


# The perfect text that none will read, quality as a resource, and journey before destination

I have analysed a lot of the project's code in the [second part of this series](https://originalnicodr.github.io/blog/10-years-of-code-smell-self-archeology), and if I said most of it was awful, it wouldn't quite cut it. However, despite the bad code, Spanish UI, and all, at the end of the day, the most important aspect of the project is that it is. [It exists](https://steamcommunity.com/sharedfiles/filedetails/?id=652649833). I took my free time and made something that other people found useful with it. A lot of people go on in this field without ever working or finishing any personal project; they have never felt the rush of wanting to go back to sleep because you are tired, but you are also excited to wake up tomorrow full of energy to keep working on something you enjoy. That feeling, that drive of making something out of nothing, something that you are the target user of and know what aspects to work on or what to add to make it as useful as it can be, and for other people to also find it handy, is why I am still doing this.

The source code, as we have seen, must be one of the worst written pieces of code I have in my hands that I have worked on. However, the fact that I kept it around means something. It's proof that, even if the code is bad, the project as a whole is not. The project is (or was at the time, at least) a good addition to the whole social gaming ecosystem; it was useful, and that's all that matters to the people who used it. And I believe that's something we often forget as software engineers. We may get so deep into the architecture and design of code that we lose if we are actually working on something that is worth it. We might spend time with useless tasks to keep us busy instead of wondering on what would make the most impact for the user. How many pieces of software have contributed positively to the world without having the most perfect code? I have lost track of how many games famously have gigantic “if” chains that were pretty bad, but shipped at the end, and lo and behold, the medium has been better because of them.

We can keep iterating and refactoring all we want to try to achieve an idealized, but also inexistent, perfect architecture. This doesn't mean that you shouldn't iterate and try to come up with better designs (after all, the beauty of design work is to try to find the best plan that achieves your goals upfront to avoid wasting resources in missteps), and I do consider the act of iteration a necessary skill to acquire and polish for any software engineer worth their salt. But there comes a point where the effort you put in produces fewer and fewer benefits. There are write-ups about [when is a good point to stop refactoring](https://wiki.c2.com/?WhenToStopRefactoring) if you want to get a bit deeper into that, but my thought on this is, don't pursue a perfect design, and instead use what you learned from the mistakes in your current personal project to work on the next one. Don't stale on the same project, hoping that by eternally polishing it, you would somehow reach design illumination. By trying your hand with such different projects, you will get to face new and different problems, but most importantly, feel fresh and happy while doing so. And, hopefully, leaving the world, internet, or that niche community you made this for, a little better.

I guess I should also mention how different projects require different mindsets. If your aim with a personal project is not monetary but just to have fun while also solving a problem that's bothering you and potentially others, it doesn't need the most advance architecture and layers of abstractions that you can put in. Especially if it has an expiration date maintaining-wise. However, if you are working on a project, whether personally or professionally, that will be maintained for a very long time, in which you and maybe other maintainers will be interacting with, then I consider it a must to work on it consciously engineering-wise. To make sure your changes align with the project architecture and to make future maintainers' lives better. Of course, if you want to practice good engineering principles on little personal projects, go for it! That's awesome actually, but I consider time and mental power resources.

And while applying good engineering principles can make for a very robust architecture, it can also create unnecessary friction if the project state is experimental and requirements are expected to change constantly. By restraining your design to the first iteration of a solution, you are solidifying aspects of the project that may still need to be flexible (which kinda goes against the ideas that David Farley goes in his book "Modern Software Engineering" which I discussed briefly in [my previous blogpost](./10-years-of-code-smell-self-archeology), if you think about it). Some things can just be a proof of concept, to assert if the idea you have to solve a problem makes sense or not in the first place.

Mind you, there is more than one project that started as a one-thing only and sprawled into a whole thing with years of engineering maintaining process behind it; those things happen. Just make sure to have the strength of mind to toss the original implementation if it was messy and start over if necessary. As we discussed in [the previous part](./10-years-of-code-smell-self-archeology), please learn how to kill your children.

I guess that nowadays you can get an LLM model to oneshoot a project like this. And would definitely make it better structure and architecture wise. So if we follow the previous line of thinking, where what matters is the end project and its impact, then the means that we use to reach such output doesn't matter, right?

Well, that feels like a pretty nihilistic way of seeing software engineering, doesn't it? I like to believe that the project itself had a positive impact on my development, just like it had on the internet. Without taking these (many) wrong steps throughout its development, I am not sure if I would be in the same spot skill-wise. Being able to contrast how I did things 10 years ago vs how I do them now has given me quite a perspective on where I am at, which one can easily ignore with how focused we are on our day to day problems, not only professionally, but on life in general.

# Impact, future, and time capsule

I should be able to do this project in Typescript nowadays, which was what I would have liked to do as a kid, but I didn't even know what technologies I would have needed. Having said that, I don't think Steam as a gaming social network is as popular nowadays as it was back then (or maybe I have become older and don't interact with it as much as I used to).

I should mention, however, that after I published this project, other web Steam calculators have popped up (mainly on sites that sell entire badges to increase your Steam profile level). Whether I am partially responsible for that, I do not know. However, from the calculators I have seen, none of them have the granularity mine does, so I guess I did something right there.

This has been an interesting experiment. I have looked back to the past to where I was when I first started working, but not so far away as before university. Hell, the mere fact that I am able to write all of this blog post in English, while I struggled to string two words together in my first work team meeting ever, already says a lot.

So realizing how much I have gone through and learned all of these years has been wild, and I would lie if I say it hasn't improved by mood learning about it. I hope I don't become too self indulgent to sleep on my laurels, but I have the rest of my professional life in front of me to teach me humility again if needed.

Tho I am wondering what will happen in ten years from now. Hopefully by then I am on my path to become one of those all knowing wizards that can crack open any problem, but also with my feet on the ground, still open to learn from my mistakes and to keep improving every day.

# Further reading

If you liked all of the good practices nonsense that I rambled about, I will leave you with some further reading material if you are interested:

- 1: [Modern Software Engineering](https://www.goodreads.com/en/book/show/57345270-modern-software-engineering) by David Farley: Great book, and super easy to digest, that goes deep into what makes good engineering in general, and how making things modular and flexible to change are the main pillars of most good designs. He goes in depth about good practices, why they work, and the common principles behind such ideas so that you can incorporate them better by understanding them instead of just following some rules without context. It's the closest thing I have read that has put into words the learnings I have gotten from the best places I have worked on.

  One of my favorite chapters talks about the relationship between the “craft” and “engineering” aspects of software engineering, how the former feeds the latter by using creativity to solve problems laterally, and how ultimately we need to force ourselves to engineering practices and follow the scientific process in order to do better work. 

- 2: [Game Programming Patterns](https://www.goodreads.com/book/show/15499449-game-programming-patterns?ref=nav_sb_ss_1_25), by Robert Nystrom: Don't let the name fool you; despite using game engineering as examples to explain design patterns, this is one of the best resources I have found that not only teaches how to apply each of the patterns it touches on, but also variations, and maybe most importantly, when not to use them. It does help that game development has some of the most difficult problems to solve in the entire software industry (and some of the most interesting ones!).

  Normally, one would read such a book about patterns by jumping around depending on what you need to use next. However, Roberts' book reads so easily and is full of great insights that it's worth reading from start to end. And you can even [do so for free on his website](https://gameprogrammingpatterns.com/contents.html)!

- 3: [Refactoring Guru](https://refactoring.guru/): I have already linked it when talking about Singletons in the [previous part](./10-years-of-code-smell-self-archeology), but this is my go-to place whenever I need a refresher on a design pattern. Maybe mentioning it doesn't sound as pretentious as recommending a book, but at the end of the day, what we need are easy-to-understand, reference, and share information, and this website excels at all three and more. It has real life analogies as examples, diagrams, and code to help you internalize every single design pattern. I highly recommend checking it out.

  I wish I had more books and blogs to recommend here, but my backlog has a couple that I still need to get through before I can decide on recommending them or not. But who knows, maybe I will come back after another 10 years with a new retrospective and more reading suggestions for y'all. If I don't, then consider that as a sign that I left the field and opened a carpentry shop.

<hr>

And that's the end! Hopefully, this series of write ups help anyone trying to get into software engineering, working on getting better at it, or sparked other engineers to think about their own experience and where they are standing now. And once again, if you are not sure if any of the things I mention make sense based on your own professional (or hobbyist!) experience, please feel free to write about it in the comments so we can keep the discussion going.

Have a good one!
