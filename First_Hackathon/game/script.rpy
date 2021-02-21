# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image basic classroom=im.Scale("basic_classroom.png",1920,1080)
image angie room=im.Scale("angie_scene.jpg",1920,1080)
image jenny room="jenny_scene.jpg"
image victor room="victor_scene.png"
define v = Character("Victor", color='#2EFF3F')
define scale = 1.5


image Victor Thinking = im.FactorScale("Victor_Thinking.png",scale)
image Victor Thinking2 = im.FactorScale("Victor_Thinking2.png",scale)
image Victor Chilling = im.FactorScale("Victor_Chilling.png",scale)
image Victor Frustrated = im.FactorScale("Victor_Frustrated.png",scale)
image Victor Serious = im.FactorScale("Victor_Serious.png",scale)
image Victor Smiling = im.FactorScale("Victor_Smiling.png",scale)
image Victor Suprised = im.FactorScale("Victor_Suprised.png",scale)
image Victor Talking = im.FactorScale("Victor_Talking.png",scale)

define j = Character("Jenny", color='#69EDFF')

image Jenny Blushing Crying = im.FactorScale("Jenny_bluhsing_crying.png",scale)
image Jenny Blushing = im.FactorScale("Jenny_Blushing.png",scale)
image Jenny confused = im.FactorScale("Jenny_confused.png",scale)
image Jenny Little Smile = im.FactorScale("jenny_Little_smile.png",scale)
image Jenny Neutral = im.FactorScale("Jenny_Neutral.png",scale)
image Jenny Sad Cry = im.FactorScale("Jenny_SadCry.png",scale)
image Jenny Smiling = im.FactorScale("Jenny_Smiling.png",scale)
image Jenny Sweating = im.FactorScale("Jenny_Sweating.png",scale)
image Jenny Yelling = im.FactorScale("Jenny_yelling.png",scale)

define a = Character("Angie", color='#ff0066')

image Angie Angry = im.FactorScale("Angie_Angry.png",scale)
image Angie Concerned = im.FactorScale("Angie_concerned.png",scale)
image Angie Confused = im.FactorScale("Angie_Confused.png",scale)
image Angie Crying = im.FactorScale("Angie_crying.png",scale)
image Angie DuckFace = im.FactorScale("Angie_DuckFace.png",scale)
image Angie Embarrassed = im.FactorScale("Angie_Embarrassed.png",scale)
image Angie Happy = im.FactorScale("Angie_happy.png",scale)
image Angie Motivated = im.FactorScale("Angie_motivated.png",scale)
image Angie Smile = im.FactorScale("Angie_Smile.png",scale)
image Angie Shook = im.FactorScale("Angie_Shook.png",scale)
image Angie Very Embarrassed = im.FactorScale("Angie_VeryEmbarrassed.png",scale)
image Angie Whatever = im.FactorScale("Angie_Whatever.png",scale)





# The game starts here.

label start:

    #"I've been thinking about changing my name."


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    define you = Character("[yourname]")
    python:
        yourname = renpy.input("What is your name?", length=32)
        yourname = yourname.strip()

        if not yourname:
            yourname = "Alex"


    scene basic_classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    "This is your first hackathon, and you're feeling overwhelmed."
    "Feelings of imposter syndrome... like you don't belong here."
    "*You nervously look around the room, while wiping your sweaty palms on your jeans*"
    "*You walk over to the table which you think is your group is seated at*"

    you "Hey guys is this Group 7?"
    show Angie Smile
    a "Yup, nice to meet you I'm Angie!"
    hide Angie Smile
    show Victor Chilling
    v "Oh hey."
    hide Victor Chilling
    show Jenny Smiling
    j "Hey! I'm Jenny!"
    hide Jenny Smiling

    # These are the flags indicating who has been interacted with
    python:
        jennyflag = False
        victorflag = False
        angieflag = False
    while True:
        show screen goangie
        show screen govictor
        show screen gojenny
        "You should talk to one of your teammates and get to know them better! Click the teammate you would like to talk to."


label choicescreen:
    while True:
        # If user has done every scene
        if jennyflag == True and victorflag == True and angieflag == True:
            jump conclusion
        if not jennyflag:
            show screen gojenny
        if not angieflag:
            show screen goangie
        if not victorflag:
            show screen govictor
        "You should talk to one of your teammates and get to know them better! Click the teammate you would like to talk to."


label conclusion:
    show Jenny Smiling
    show Angie Smile at left
    show Victor Smiling at right
    "As you can see, it doesn’t matter how skilled or talented you are. At the end of the day, we are here to learn."
    "Hackathons bring people together from all walks of life to learn from each other's successes and failures."
    "So next time you're at a hackathon remember you may encounter people like Angie, Jenny, and Victor."
    "They might have a wide range of experience, but that shouldn't impact you in how you feel about your own ability and self worth."
    "You are amazing and worth it! Thank you for taking time out of your day to play our little game!"
    "This game was made by Hammad, Kevin, and John for UofTHacks VIII with an emphasis on TELUS’S challenge of managing and improving mental health."

    return
