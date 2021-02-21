
label victor_text:
    scene victor room
    hide screen goangie
    hide screen govictor
    hide screen gojenny

    show Victor Serious with moveinright
    you "Hey! How’s it going?"
    v "Fine"
    menu: 
        "Um I’m [you].":
            v "Victor"
        "...":
            v "Got anything else to add?"
            you "Oh uh, what's your name?"
            v "Victor."
    
    you "{i}Man, what’s this guy’s deal?{\i}"
    
    menu: 
        "Um... how much experience do you have?":
            hide Victor Serious 
            show Victor Chilling 
            v "9 years. Currently in a masters of applied computing."
            hide Victor Chilling 
            show Victor Serious 
            you "{i}Oh boy, this guy's a pro. Okay, don't freak out...{\i}"
        "What are you working on?":
            hide Victor Serious 
            show Victor Thinking 
            v "Figured I'd get a headstart on the backend of our app. Easy stuff."
            you "Oh wow, already?"
            hide Victor Thinking 
            show Victor Thinking2 
            v "I don't wait around for others."
            you "Do you have much coding experience?"
            hide Victor Thinking2 
            show Victor Chilling 
            v "9 years, with an undergrad and a masters."
            you "{i}Oh boy, this guy's a pro. Okay, don't freak out...{\i}"
            hide Victor Chilling 
            show Victor Serious


    v "You’ve seen our project plan, right? I work best alone, so just focus on the front-end classes and I’ll take care of the rest. "

    menu:
        "{i}...What even is front-end again? Oh man, I’m so lost{\i}"
        
        "Um, I’m pretty new to object-oriented programming. Could you help me understand inheritance?":
            hide Victor Serious 
            show Victor Frustrated 
            v "Oh man, you’re REALLY new to this, aren’t you?"
            hide Victor Frustrated 
            show Victor Serious 
        "Oh uh, by front-end you mean...?":
            hide Victor Serious 
            show Victor Frustrated 
            v "Oh man, you’re REALLY new to this, aren’t you?"
            hide Victor Frustrated 
            show Victor Serious 
    
    you "{i}Ouch, maybe I should talk to someone else. He’s so cold.{\i}"
    you "It’s okay, never mind. I’ll leave you be. I'll learn about it on YouTube or something."
    hide Victor Serious
    show Victor Thinking
    v "*sigh* Hmm..."
    hide Victor Thinking
    show Victor Talking
    v "Ah, no need for that. Here, I’ll show you a thing or two."
    hide Victor Talking
    show Victor Serious
    you "Oh really? I mean, if you can spare the time..."
    hide Victor Serious
    show Victor Thinking2
    v "A few minutes shouldn't hurt. Ok so when you declare an object…"
    hide Victor Thinking2
    show Victor Smiling
    v "… Encapsulation is very important… Inheritance is used for… Abstract classes…. Generic types…"
    
    menu:
        "{i}I’ve heard these words but I don’t understand a thing …{\i}"

        "Uh... sorry would you mind re-explaining ...":
            hide Victor Smiling
            show Victor Serious
            v "How much of that did you understand?"
        "...":
            v "...are available at runtime ... that's why you should be mindful of scope."
            hide Victor Smiling
            show Victor Serious
            v "You catch all that?"
    
    you "I … uh. I feel like I’m slowing you down. I’ll go learn on my own for now"
    hide Victor Serious
    show Victor Smiling
    v "Ha, shoot. That’s probably just me being a bad teacher. I’m no good at explaining the basics."
    v "Let me give it another go. I’ll do a better job this time."
    you "{i}I can't believe he still wants to help me?{\i}"
    you "Are you sure? You don’t have to teach me if you don’t want to"
    hide Victor Smiling
    show Victor Talking
    v "I'd like to. I remember when I was at your level, I struggled with more than just inheritance"
    you "Really? I can’t imagine YOU struggling given your skills and experience."
    you "{i}Whew, he’s much more relatable now that I got to know him better.{\i}"
    hide Victor Talking
    show Victor Smiling
    v "It takes time. Don’t fret. I’ve been programming for much longer than you. 9 years, in fact."
    hide Victor Smiling
    show Victor Thinking
    you "Yeah you mentioned that earlier! That's so impressive! What inspired you to start programming?"
    hide Victor Thinking
    show Victor Smiling
    v "I spent all my time playing Pokemon as a kid… And I wanted to recreate the game haha."
    you "Really?? I love Pokemon!"
    hide Victor Smiling
    show Victor Suprised
    v "Whoa, no way!"
    hide Victor Suprised
    show Victor Talking
    menu:
        "What's your favourite game?"

        "Pokemon Ruby!":
            hide Victor Talking
            show Victor Smiling
            v "Some of my favourite Pokemon are in Ruby! You have great taste!!" 
        "Pokemon Gold all the way!":
            hide Victor Talking
            show Victor Smiling
            v "No way!! I'm a big Silver fanboy myself!!"
    hide Victor Smiling
    show Victor Talking
    v "If you want, I can show you my Pokemon-inspired game a little later."
    you "That's so cool! Can't wait!"

    menu:
        "Did you code it all yourself?":
            hide Victor Talking
            show Victor Smiling
            v "Actually, no! I needed my friends help for this one." 
            you "{i}Oh? Victor working with others? Interesting...{\i}"
        "What language did you use?":
            hide Victor Talking
            show Victor Smiling
            v "Python! Packages make things pretty manageable..."
            
    you "Coding and Pokemon. Pretty cool we have some common interests!"
    hide Victor Smiling
    show Victor Talking
    v "Agreed! Here, I’ll explain inheritance using Pokemon as an example. If we design a class for one Pokemon … "
    you "{i}Wow, Victor was cold at first, but turned into a great colleague.{\i}"
    you "{i}I guess even if connecting with others feels difficult at first, it can be worthwhile to keep trying and not jump to conclusions too quickly. {\i}"
    hide Victor Talking
    python:
        victorflag = True
    jump choicescreen
