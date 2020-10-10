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

    menu:

        "I couldn't tell. You seem like a great person to me and I hope we can become good friends.":
            $rFriendship=rFriendship+2
            "(Reiki smiles brightly at you.)"

            r "Thanks, I hope we can be friends too. Though I don't really know how to act with friends."

            mc "It's okay, all you have to do is be yourself, and know I'll be here whenever you need someone. Unironically. Since we live in the same dorm."

            r "Thanks [MC Name], I feel better knowing you're on my side!"

            "Suddenly you hear a room open as Kimiko leaves her dorm room."

        "Oh. What happened to you, if you don't mind me asking. I don't want to make you relive unpleasant memories.":
            $rRomance=rRomance+2
            "(Reiki blushes slightly at you.)"

            r  "It happened so long ago now. I didn't think anyone would be willing to listen."

            mc "Of course if you're willing to trust me I would love to hear about lil Reiki before he became a vengeful spirit."

            r  "My story is a common one, but what made it so much worse was the fact that it was my last day of high school senior year. I had completed everything I needed to do to graduate smoothly and when I least expected it the person I trusted most stabbed me in the back. I would tell you more, but the specific memories of that moment have disappeared from my mind and all I have left is the hate I felt for my only friend."

            mc "I’m so sorry that happened to you. I hope one day you will be able to trust people again."

            r "(Whispered) \”With you I might just be able to.\""

            mc "What was that?"

            r  "Oh nothing… So how did you end up here?"

            mc "My story is similar to yours in the fact that it happened my senior year. I had completed graduation and was looking forward to my future, when my father, who is totally a nekomata like me, well let’s just say something terrible happened and me and my mother moved out here."

            r  "I guess we have something in common. Though I am sorry to hear that something happened to your Father. If you ever want to talk more about it I'm here."

            mc "Thanks and I'm here for you too."


        "Wow! Now I know why you're such an unlikable person.":
            $rHatred=rHatred+4
            "(Reiki looks so annoyed at you. Like seriously, he’s about to pop a freaking vein. A VEIN.)"

            r "I-so-fucking-hate-you-you-piece-of-shit. Why am I talking to you again..."

            "(Reiki sighs.)"

            mc "Because of the lucky convenience of living together. So, prepare for the worst. Wink"

            "(You actually winked at him. Good job. Prepare your grave.)"

            "Suddenly you hear a room open as Kimiko leaves her dorm room."

        "Wow, I'm so shocked that happened to you. COUGHnotreallyCOUGH":
            $rHatred=rHatred+4
            "Reiki looks annoyed and sighs."

            r "Anyways... "

            "Suddenly you hear a room open as Kimiko leaves her dorm room."


    return
