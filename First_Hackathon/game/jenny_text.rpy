
image Jenny Blushing Crying = im.FactorScale("Jenny_bluhsing_crying.png",scale)
image Jenny Blushing = im.FactorScale("Jenny_Blushing.png",scale)
image Jenny confused = im.FactorScale("Jenny_confused.png",scale)
image Jenny Little Smile = im.FactorScale("jenny_Little_smile.png",scale)
image Jenny Neutral = im.FactorScale("Jenny_Neutral.png",scale)
image Jenny Sad Cry = im.FactorScale("Jenny_SadCry.png",scale)
image Jenny Smiling = im.FactorScale("Jenny_Smiling.png",scale)
image Jenny Sweating = im.FactorScale("Jenny_Sweating.png",scale)
image Jenny Yelling = im.FactorScale("Jenny_yelling.png",scale)

label jenny_text:
    scene jenny room
    hide screen goangie
    hide screen govictor
    hide screen gojenny
    show Jenny Smiling
    pause(0.5)
    show Jenny Yelling
    j "Hey! Wanna see some cool hacker stuff?"
    "*types ‘tree’ in terminal while giggling*"
    hide Jenny Smiling
    show Jenny Sweating
    j "Isn’t that awesome?"
    hide Jenny Sweating
    show Jenny Smiling
    menu:
        "Wow, that’s so cool Jenny! *rolls eyes slightly*":
            j "Haha thanks!"
        "Haha good one Jenny!":
            j "Haha thanks!"

    hide Jenny Smiling
    show Jenny Yelling
    j "So what cool coding tricks do you know!"
    hide Jenny Yelling
    show Jenny Smiling
    you "Umm honestly ... I don’t really know many tricks."
    hide Jenny Smiling
    show Jenny confused
    pause(0.5)
    show Jenny Yelling
    j "Aw, come on!!! Don’t be shy, I just showed you one of my greatest tricks!"
    hide Jenny Yelling
    show Jenny Neutral
    you "{i}One of her 'greatest tricks’??? Okay then...{\i}"
    you "Well, I have one mini project where I built a web scraper"
    hide Jenny Neutral
    show Jenny confused
    j "Whoa, what’s that??"
    hide Jenny confused
    show Jenny Neutral
    you "Oh nothing special, it’s just a program that grabs data from websites haha."
    hide Jenny Neutral
    show Jenny Yelling
    j "Oh wow that’s so impressive!!"
    you "{i}She thinks that project is impressive? Wow, it’s nice to know I'm not the only inexperienced one{\i}"
    hide Jenny Yelling
    show Jenny Blushing Crying
    j "I don't have any personal projects yet."
    you "Oh really?"
    menu:
        you "When you signed up for the hackathon..."
        "Were you scared about what others would say? Being less experienced and all…":
                show Jenny Sad Cry
                pause(0.5)
                show Jenny Yelling
                j "No way!!"
        "What do you want to get out the event?":
                jump next
    label next:
        hide Jenny Yelling
        show Jenny Smiling
        j "I joined so I could meet new people and learn new skills!"
    you "Really? I was scared that I wouldn’t have the skills to contribute to the team."
    hide Jenny Smiling
    show Jenny Neutral
    j "It’s okay that you’re less experienced!! You’re here to have a new experience and try your best! "
    j "No matter what happens, at least you’ll learn something new and meet new people!"
    menu:
        "I guess you’re right… I just don’t want to hold my team back!":
            jump next1
        " I thought I wasn’t good enough to be here...":
            jump next1
    label next1:
        hide Jenny Neutral
        show Jenny Yelling
        j "Oh stop that!! Nobody expects you to be incredible or anything!"
    hide Jenny Yelling
    show Jenny Smiling
    you "Hmm … I guess you’re right, I shouldn’t feel scared because I'm less experienced. Everyone is at their own place, we’re all here to learn and better ourselves."
    j "Absolutely!!"
    hide Jenny Smiling
    show Jenny Neutral
    j "So you gonna show me that web straper? Sorry, web scraper?"
    you "Yeah sure thing! It’s on my GitHub!"
    hide Jenny Neutral
    show Jenny confused
    j "Git…? Hub…?"
    you "Oh haha... Might have to show you that too then!"
    show Jenny Smiling
    pause(0.5)
    show Jenny Yelling
    j "I guess we have a lot to learn together!"
    you "{i}I’m glad I reached out and connected with Jenny. Knowing that there are others with my level of experience is comforting.{\i} "
    you "{i}Maybe I can help her in the same way that others can help me. {\i}"
    hide Jenny Smiling

    python:
        jennyflag = True
    jump choicescreen
