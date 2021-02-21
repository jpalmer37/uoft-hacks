image github = im.FactorScale("hello-world2.png",0.7)

label angie_text:
    scene angie room
    hide screen goangie
    hide screen govictor
    hide screen gojenny
    show Angie Smile with moveinright
    a "Hey! How’s it going?"
    you "Hey Angie! Its going okay! Did you guys already start coding?"
    show Angie Happy
    a "Way too early for that haha! Sit back and relax! We’re just sharing some of our past projects."
    you "Right… past projects..."
    you "{i}*sweating* Oh crap, my only project is a tiny web scraper…{\i}"
    show Angie Concerned
    show Angie Motivated
    a "Wanna take a look at one of mine? Here’s one I did last weekend! Nothing too fancy."
    menu:
        "Sure, let me take a look":
            show Angie Happy
            a "Well this is a gradient-boosted machine learning model to predict whether a tumor is cancerous or not!"
        "Uhhh, I don’t know if I can really give you any valuable insight {\i}*sighs*{\i}":
            show Angie DuckFace
            a "Well, that's nonsense come take a look!"
            you "Oh fine let me take a look"
            show Angie Motivated
            a "I knew you'd wanna see it!"
            show Angie Happy
            a "Well this is a gradient-boosted machine learning model to predict whether a tumor is cancerous or not!"
        "I don't wanna see it {\i}*rolls eyes*{\i}":
            show Angie Whatever
            a "Your loss"
            show Angie DuckFace
            a "You won't get to see my see my cool gradient-boosted machine learning model to predict whether a tumor is cancerous or not!"
    you "{i}I didn’t understand a single word in that last sentence …{\i}"
    show Angie Happy
    a "...here’s my cross-validation … couldn’t decide between classifiers ... final accuracy was 95\%!"
    you "{i}I am so lost...{\i}"
    you "… You built that in one weekend?"
    show Angie Motivated
    a "Yeah! Really not that hard, honestly. Got any cool projects on your profile?? Any data analysis?"
    you "…Um, not quite.."
    a "… Oh! Then you must be a developer! Got any games??"
    menu:
        "Well no games, but I did make something, nothing too fancy ahah {\i}I look so dumb right now{\i}":
            a "Super cool!"
        "Uhhh, I mean, i don't know........":
            show Angie Confused
            show Angie Concerned
            a "You ok? You look a little flustered"
    show Angie Happy
    a "Anyways, specifics don’t matter! Show me a project of yours! Anything!"
    you "{i}Oh man, don’t look like a fool, say something!!{\i}"
    menu:
        "Ahhh, wish I could, but I think my GitHub account got deactivated or something.":
            show Angie Confused
            a "Really? Hmm, I’ve never heard anything like that happen before"
            you "{i}Ugh, who am I kidding with that line{\i}"
            you "Okay wait, sorry. In full honesty, my only project is a small web scraper. This is my first hackathon."
        "Im not the most experienced, my only project is a small web scraper.":
            show Angie Motivated
            a "A web scraper! That's so cool!"
            show Angie Happy
            you "{i}Woah what? She thinks it's cool?{\i}"
            you "By the way, This is my first hackathon. So I might be a little lost."
    show Angie Shook
    a "Whoa!! No way! Your first one?? That’s awesome!"
    show Angie Motivated
    you "{i}Wait, what?? Awesome?{\i}"
    show Angie Happy
    a "Don’t be ashamed of it! No need to hide it."
    show Angie Motivated
    a "Everyone has to start somewhere! Good on you for taking the first steps! Those can be the hardest!"
    you "What? You’re not upset? I thought you’d be frustrated that I'm a beginner! You’re so experienced!"
    show Angie Happy
    a "Not at all! I'd love to share my knowledge! Want me to introduce you to some packages we might be using?"
    you "{i}She's so experienced; I can't believe she's so willing to help! {\i}"
    menu:
        "Sure i'm down to take a look.":
            show Angie Happy
            a "great!"
            show Angie Smile
            a "Here take a look."
            a "{i}Turns laptop screen towards you.{\i}"
            show Angie Concerned
            you "I have no idea what I am looking at, I feel like such a burden."
        "Are you sure? I feel like a burden…":
            show Angie DuckFace
            a "Come on are we really doing this again!"
        "No, I don't wanna look at it!":
            show Angie Concerned
            show Angie Angry
            a "What's up with you?"
            show Angie Concerned
            a "Are still giving yourself a hard time about being not compenent enough or whatever."
            you "Hey! Look! I just don't wanna be a burden."
    show Angie Motivated
    a "I told you none of that!! You’re doing FINE!"
    show Angie Happy
    a "Others helped me when I was starting, so why can’t I help you?"
    menu:
        "Wow, thank you so much! Let's get started then!":
            show Angie Smile
            a "Awesome, i'm so happy you changed your perspective on todays hackathon."
            show Angie Happy
            a "I feel so relieved that you are now more comfortable with yourself and your skill set."
            show Angie Motivated
            a "I'm looking foward to wroking with you!"
            you "Like wise!"
        "Thank you so much, but i'm still feeling kind of nervous about this all.":
            show Angie Concerned
            a "You're still on about that."
            show Angie Motivated
            a "I told you to relax"
            you "I guess you're right, let's get going then."
            show Angie Happy
            a "Now that's what I wanna hear!"
            show Angie Smile
            a "I feel so relieved, you are now more comfortable with yourself and your skill set."
            show Angie Smile
            show Angie Motivated
            a "I'm looking foward to wroking with you!"
            you "I can't wait to work with you!"
    you "{i}Angie was so warm and welcoming even though I was inexperienced.{\i}"
    you "{i}Connecting with her showed me that people can look past your skills and experience, and appreciate you as a team member.{\i}"
    hide Angie Motivated
    python:
        angieflag = True
    jump choicescreen
