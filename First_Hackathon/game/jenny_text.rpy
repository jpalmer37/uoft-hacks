
label jenny_text:
    scene jenny room
    hide screen goangie
    hide screen govictor
    hide screen gojenny
    show Jenny Smiling with moveinright
    j "Hey! Wanna see some cool hacker stuff?"
    "*types ‘tree’ in terminal while giggling*"
    hide Jenny Smiling
    show Jenny Sweating
    j "Isn’t that awesome?"
    hide Jenny Sweating
    show Jenny Smiling
    you "Wow, that’s so cool Jenny! *rolls eyes slightly*"
    j "Haha thanks!"
    hide Jenny Smiling
    show Jenny Yelling
    j "So what cool coding tricks do you know!"
    hide Jenny Yelling
    show Jenny Smiling
    you "Umm honestly ... I don’t really know many tricks."
    hide Jenny Smiling
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
    show Jenny Sad Cry
    j "I don't have any personal projects yet."
    you "Oh really?"
    you "When you signed up for the hackathon, were you scared about what others would say? Being less experienced and all…"
    hide Jenny Sad Cry
    show Jenny Yelling
    j "No way!!"
    hide Jenny Yelling
    show Jenny Smiling
    j "I joined so I could meet new people and learn new skills!"
    you "Really? I was scared that I wouldn’t have the skills to contribute to the team. I thought I wasn’t good enough."
    hide Jenny Smiling
    show Jenny Neutral
    j "It’s okay that you’re less experienced!! You’re here to have a new experience and try your best! "
    j "No matter what happens, at least you’ll learn something new and meet new people!"
    you "I guess you’re right… I just don’t want to hold my team back!"
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
    hide Jenny confused
    show Jenny Smiling
    j "I guess we have a lot to learn together!"
    you "{i}I’m glad I reached out and connected with Jenny. Knowing that there are others with my level of experience is comforting.{\i} "
    you "{i}Maybe I can help her in the same way that others can help me. {\i}"
    hide Jenny Smiling

    python:
        jennyflag = True
    jump choicescreen
