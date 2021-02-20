# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image basic classroom=im.Scale("basic_classroom.png",1920,1080)
define v = Character("Victor", color='#065535')
define scale = 1.5
define hasInputted = False
image Victor Angry = im.FactorScale("Victor_Angry.png",scale)
image Victor Chilling = im.FactorScale("Victor_Chilling.png",scale)
image Victor Frustrated = im.FactorScale("Victor_Frustratedpng.png",scale)
image Victor Serious = im.FactorScale("Victor_Serious.png",scale)
image Victor Smiling = im.FactorScale("Victor_Smiling.png",scale)
image Victor Suprised = im.FactorScale("Victor_Suprised.png",scale)
image Victor Very Angry = im.FactorScale("Victor_VeryAngry.png",scale)

define j = Character("Jenny", color='#6da7e8')

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

    "I've been thinking about changing my name."


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

    "*You nervously look around the room, while whipping your sweaty palms on your jeans*"
    "*You walk over to the table which you think is your group is seated at*"
    you "Hey guys is this Group 7?"
    show Angie Smile
    a "Yup, nice to meet you i'm Angie!"
    hide Angie Smile
    show Victor Chilling
    v "*Grunts and pushes glasses up*"
    hide Victor Chilling
    show Jenny Yelling
    j "Hey! Hey! I'm Jenny!"
    j "*Smirks* Wanna see something cool hacker stuff!"
    j "*Proceeds to type tree in command prompt while giggling*"
    hide Jenny Yelling
    show Jenny Smiling
    j "Now take a look at this!"
    you "Wow, that's so cool!"
    hide Jenny Smiling
    "*You roll your eyes*"
    while not(hasInputted):
        show screen goangie
        show screen govictor
        show screen gojenny
        "You should talk to one of your teammates and get to know them better! Click the teammate you would like to talk to."

    # This ends the game.
label end:
    show Angie Smile at left
    show Jenny Smiling
    show Victor Smiling at right
    "Placeholder text"
    return
