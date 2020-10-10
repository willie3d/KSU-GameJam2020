﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("MC (replace with variable later)")
define k = Character("Kimiko Inariou")
define t = Character("Taiki Tangou")
define h = Character("Himiko Amatera")
define r = Character("Reiki Omoi")
define hm = Character("Headmaster")
define prof = Character("Prof. Hayato")
define unknown = Character("??????")

# The game starts here.

label start:


    # These display lines of dialogue.
    "It's been almost a week since the situation with my father took place that changed my life forever.
    My mother and I have decided it would be best for the both of us to move far away from the city and
    live in a remote house in the countryside."

    "We found the house through a family friend and have been living with the Inariou family for the past week.
    They seem nice enough, but I havent really had much time to talk to their daughter who happens to be the same age as me."

    "I'm hopeful that me and my mother will be able to make a good life here and maybe I'll be able to make new friends as well."

    ###########TRAILER HERE############
    ###########TRAILER HERE############
    ###########TRAILER HERE############


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bedroomNight

    "UGG I can't seem to sleep.. again"
    "Maybe I should take a walk, and then hopefully, I might be able to sleep."

    scene backyardNight

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show kimikoFox

    #This waits for sometime
    pause 2

    "UMMM Did I see that correctly Kimiko just looked like a… fox?"
    mc "UMMMM..."

    show kimiko

    mc "Oh MY GOD! You're a fox!"

    k "W-What are you talking about? You must be blind."
    mc "I literally just saw your fox ears. You can’t say I’m crazy"
    k "I think you need to get your eyes checked, [sir, miss]. T-There’s this good eye place over at-"
    mc "I know what I saw! I am not blind. Maybe you should put on your own glasses you had before."
    k "No-no. I think you need some glasses... I’m going to go on my peaceful walk now-"

    "No, I can't leave the conversation at that. I know what I saw!"

    "(You grab Kimiko’s arm and prevent her from leaving.)"

    k "Let go of me. I told you. I am not a fox. You probably just saw the shadows or something."

    # This ends the game.
    return
