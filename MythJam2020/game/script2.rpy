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

label start2:
    hide kimiko happy
    scene black
    "Day 2"

    "(Your eyes are closed when they hear an alarm go off.)"
    #The screen slowly fills with light, and we are greeted by the MC’s Bedroom.)
    scene ProtagDormDay

    "It's been a while since I've slept this well. I'm excited to start my first day of class."

    "(As you greet the day, you get out of bed and get ready for your first day.)"

    scene CommonSpaceDorm
    show reiki

    "(As you leave your dorm room, you are greeted by Reiki standing in the kitchen making breakfast. You head towards him and open the Fridge to see what a human might be able to eat around here.)"

    r "So, as it turns out, I guess it looks like we’re dorm mates."

    "(Reiki sighs and shrugs his shoulders.)"

    mc "Oh yeah, I kinda registered last minute, so fortunately, they put me in the same dorm as my friend, Kimiko."

    r "You know Kimiko too. She was the person who convinced me to try sharing a dorm with others instead of living completely alone like I usually do."

    mc "Do you not like being with other people?"

    r "I don't really have a good experience with others, I guess that’s why I became a vengeful spirit to begin with."

    "A… Vengeful spirit… Yikes."

    return
