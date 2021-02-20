# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Victor", color='#065535')

image Victor Angry = "Victor_Angry.png"
image Victor Chilling = "Victor_Chilling.png"
image Victor Frustrated = "Victor_Frustratedpng.png"
image Victor Serious = "Victor_Serious.png"
image Victor Smiling = "Victor_Smiling.png"
image Victor Suprised = "Victor_Suprised.png"
image Victor Very Angry = "Victor_VeryAngry.png"

define j = Character("Jenny", color='#6da7e8')

image Jenny Blushing Crying = "Jenny_bluhsing_crying.png"
image Jenny Blushing = "Jenny_Blushing.png"
image Jenny confused = "Jenny_confused.png"
image Jenny Little Smile = "jenny_Little_smile.png"
image Jenny Neutral = "Jenny_Neutral.png"
image Jenny Sad Cry = "Jenny_SadCry.png"
image Jenny Smiling = "Jenny_Smiling.png"
image Jenny Sweating = "Jenny_Sweating.png"
image Jenny Yelling = "Jenny_yelling.png"

define a = Character("Angie", color='#ff0066')

image Angie Angry = "Angie_Angry.png"
image Angie Concerned = "Angie_concerned.png"
image Angie Confused = "Angie_Confused.png"
image Angie Crying = "Angie_crying.png"
image Angie DuckFace = "Angie_DuckFace.png"
image Angie Embarrassed = "Angie_Embarrassed.png"
image Angie Happy = "Angie_happy.png"
image Angie Motivated = "Angie_motivated.png"
image Angie Smile = "Angie_Smile.png"
image Angie Shook = "Angie_Shook.png"
image Angie Very Embarrassed = "Angie_VeryEmbarrassed.png"
image Angie Whatever = "Angie_Whatever.png"





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
    show screen goangie
    show screen govictor
    show screen gojenny
    "You should talk to one of your teammates and get to know them better! Click the teammate you would like to talk to."



    # This ends the game.

    return
