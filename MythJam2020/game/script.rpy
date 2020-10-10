# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#  $ Symbol required to use base python functions

define mc = Character("MC (replace with variable later)")
define k = Character("Kimiko Inariou")
define t = Character("Taiki Tangou")
define h = Character("Himiko Amatera")
define r = Character("Reiki Omoi")
define hm = Character("Headmaster")
define prof = Character("Prof. Hayato")
define unknown = Character("??????")
$ kFriendship = 0
$ kRomance = 0
$ kHatred = 0
$ tFriendship = 0
$ tRomance = 0
$ tHatred = 0
$ hFriendship = 0
$ hRomance = 0
$ hHatred = 0
$ rFriendship = 0
$ rRomance = 0
$ rHatred = 0
$ pronoun1 = ("") # he, she, they
$ pronoun2 = ("") # him, her, them
$ pronoun3 = ("") # his, her, their
$ pronoun4 = ("") # his, hers, theirs
$ pronoun5 = ("") # himself, herself, themself
$ pronoun6 = ("") # Sir, Miss, Comrade

# The game starts here.

label start:

    #this is how to make selections and stuff
    menu:
        "Please select your preferred pronouns..."

        "He, Him, His":
            $ pronoun1 = "he"
            $ pronoun2 = "him"
            $ pronoun3 = "his"
            $ pronoun4 = "his"
            $ pronoun5 = "himself"
            $ pronoun6 = "Sir"
        "She, Her, Hers":
            $ pronoun1 = "she"
            $ pronoun2 = "her"
            $ pronoun3 = "her"
            $ pronoun4 = "hers"
            $ pronoun5 = "herself"
            $ pronoun6 = "Miss"
        "They, Them, Theirs":
            $ pronoun1 = "they"
            $ pronoun2 = "them"
            $ pronoun3 = "their"
            $ pronoun4 = "theirs"
            $ pronoun5 = "themself"
            $ pronoun6 = "Comrade"

    # The phrase in the brackets is the text that the game will display to prompt
    # the player to enter the name they've chosen.
    $ player_name = renpy.input("What is your name, Human?")

    $ player_name = player_name.strip()
    # The .strip() instruction removes any extra spaces the player
    # may have typed by accident.
    #  If the player can't be bothered to choose a name, then we
    #  choose a suitable one for them:
    if player_name == "":
        $ player_name="Shuji"

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
    show kimiko fox

    #This waits for sometime
    pause 2

    "UMMM Did I see that correctly Kimiko just looked like a… fox?"
    mc "UMMMM..."

    show kimiko happy

    mc "Oh MY GOD! You're a fox!"

    k "W-What are you talking about? You must be blind."
    mc "I literally just saw your fox ears. You can’t say I’m crazy"
    k "I think you need to get your eyes checked, [pronoun6]. T-There’s this good eye place over at-"
    mc "I know what I saw! I am not blind. Maybe you should put on your own glasses you had before."
    k "No-no. I think you need some glasses... I’m going to go on my peaceful walk now-"

    "No, I can't leave the conversation at that. I know what I saw!"

    "(You grab Kimiko’s arm and prevent her from leaving.)"

    k "Let go of me. I told you. I am not a fox. You probably just saw the shadows or something."

    menu:

        "Look. If you are a fox, I’m not going to judge. Honestly you don’t have to tell me the truth if you don't want to.":
            $ kFriendship += 1
            "Kimiko looks at you with a surprised look on her face, speechless."
            k "..."
            mc ""
            k ""
            "Kimiko touches your forehead, rendering you unconscious"
            mc "Wh"
            k "Shhhh"
        "But you were so cute with your ears and tail! Maybe a bit hot. Like H-O-T hot.":
            $ kRomance += 1
            "Kimiko looks at you with a surprised yet confused look, while blushing very slightly."
            k "W-Wh-What..?"
            mc "I think you’re cute."
            "Kimiko pulls her hand back and flicks your forehead."
            k "..."
            "You are a bit confused."
            mc "What was that-"
            "You pass out."
        "I’m not stupid. Maybe you should stop doubting me, fox girl. Maybe you’re the one that’s stupid.":
            $ kHatred += 1
            k "You don’t even know me. Back off."
            ""


    #insert fade to black



    call start2 from script2
