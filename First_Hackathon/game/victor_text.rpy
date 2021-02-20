image Victor Angry = im.FactorScale("Victor_Angry.png",scale)
image Victor Chilling = im.FactorScale("Victor_Chilling.png",scale)
image Victor Frustrated = im.FactorScale("Victor_Frustratedpng.png",scale)
image Victor Serious = im.FactorScale("Victor_Serious.png",scale)
image Victor Smiling = im.FactorScale("Victor_Smiling.png",scale)
image Victor Suprised = im.FactorScale("Victor_Suprised.png",scale)
image Victor Very Angry = im.FactorScale("Victor_VeryAngry.png",scale)

label victor_text:
    show Victor Serious
    hide screen goangie
    hide screen govictor
    hide screen gojenny
    you "Hi! I don’t think you’ve introduced yourself yet!"
    show Victor Frustrated
    v " Why does it matter to you?"
    you "..."
    you "Um I’m ___."
    show Victor Serious
    v   "Victor"
    you "What’s this guy’s deal?"
    you "Um, would you mind helping me understand objects, I’m new to object-oriented programming"
    show Victor Angry
    pause(0.7)
    show Victor Frustrated
    v " Oh man, you’re REALLY new to this, aren’t you?"
    you "{i}Ouch, maybe I should talk to someone else. He’s so mean.{\i}"
    show Victor Serious
    v " Oh well, come on over here"
    show Victor Chilling
    v " Ok so when you declare an object…"
    show Victor Serious
    v " … Encapsulation is very important… Inheritance is used for…"
    v " Abstract classes…. Generics…"
    you "{i}I don’t understand anything he’s saying...{i}"
    v " And that is all."
    you "………"
    you "Umm I’m sorry can you please repeat that?"
    show Victor Serious
    v "*Sigh* Well you are a beginner."
    show Victor Smiling
    v " I remember when I was your level, I struggled with objects too."
    you "Victor?"
    you "You um seem like you’ve been programming for a long time"
    v " 14 years!"
    you "Why did you start programming?"
    v "I spent all my time playing pokemon as a kid…"
    v "And I wanted recreate the game"
    show Victor Suprised
    you "Woah really! I love pokemon!"
    you "What’s your favorite game???"
    show Victor Smiling
    v "Soulsilver!"
    you "Haha mine’s heartgold!"
    v " Great minds think alike!"
    v " Let’s continue talking about objects, so if we think of each pokemon as on object…"
    jump end
