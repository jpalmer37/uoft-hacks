image github = im.FactorScale("hello-world2.png",0.7)

label angie_text:
    hide screen goangie
    hide screen govictor
    hide screen gojenny
    scene basic_classroom
    show Angie Smile
    a "Hey! How’s it going?"
    you "Hey Angie! Its going okay! Did you guys already start coding?"
    show Angie Happy
    a "Way too early for that haha! Sit back and relax! We’re just sharing some of our past projects."
    you "Right… past projects..."
    show github at left
    you "{i}*sweating* Oh crap, I don’t have a single project…{\i}"
    hide github at left
    show Angie Motivated
    a "Wanna take a look at one of mine? Here’s one I did last weekend! Nothing too fancy."
    a "It's a gradient-boosted machine learning model to predict whether a tumor is cancerous or not!"
    you "{i}I didn’t understand a single word in that last sentence …{\i}"
    show Angie Happy
    a "...here’s my cross-validation … couldn’t decide between classifiers ... final accuracy was 95\%!"
    you "{i}I am so lost...{\i}"
    you "… You built that in one weekend?"
    show Angie Motivated
    a "Yeah! Really not that hard, honestly. Got any cool projects on your profile?? Any data analysis?"
    you "…Um, not quite.."
    a "… Oh! Then you must be a developer! Got any games??"
    you "…umm"
    show Angie Happy
    a "Anyways, specifics don’t matter! Show me a project of yours! Anything!"
    you "{i}Oh man, don’t look like a fool, say something!{\i}"
    you "Ahhh, wish I could, but I think my GitHub account got deactivated or something"
    show Angie Confused
    a "Really? Hmm, I’ve never heard anything like that happen before"
    you "{i}Ugh, who am I kidding with that line{\i}"
    you "Okay wait, I’m sorry. Full honesty, I have no past projects. This is my first hackathon."
    show Angie Motivated
    a "Whoa!! No way! Your first one?? That’s awesome!"
    you "{i}Wait, what?? Awesome?{\i}"
    show Angie Happy
    a "Don’t be ashamed of it! No need to hide it."
    a "Everyone has to start somewhere! Good on you for taking the first steps! Those can be the hardest!"
    you "What? You’re not upset? I thought you’d be frustrated that I'm a beginner! You’re so experienced!"
    show Angie Happy
    a "Not at all! I'd love to share my knowledge! Want me to introduce you to some packages we might be using?"
    you "{i}She's so experienced; I can't believe she's so willing to help! {\i}"
    you "Are you sure? I feel like a burden…"
    show Angie Motivated
    a "Hey none of that!! You’re doing FINE!"
    a "Others helped me when I was starting, so why can’t I help you?"
    you "Wow, thank you so much! Let's get started then!"
    you "{i}Who knew that connecting with others could make this experience so much better”{\i}"
    hide Angie Motivated
    jump choice_screen
