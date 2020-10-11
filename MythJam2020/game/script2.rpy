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
define rando= Character("Random Student")
define strongman= Character("Strong Man")
$ k_friendship = 0
$ k_romance = 0
$ k_hatred = 0
$ t_friendship = 0
$ t_romance = 0
$ t_hatred = 0
$ h_friendship = 0
$ h_romance = 0
$ h_hatred = 0
$ r_friendship = 0
$ r_romance = 0
$ r_hatred = 0
$ intel=0
$ charisma=0
$ fun=0
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
            $r_friendship=r_friendship+2
            "(Reiki smiles brightly at you.)"

            r "Thanks, I hope we can be friends too. Though I don't really know how to act with friends."

            mc "It's okay, all you have to do is be yourself, and know I'll be here whenever you need someone. Unironically. Since we live in the same dorm."

            r "Thanks [MC Name], I feel better knowing you're on my side!"

            "Suddenly you hear a room open as Kimiko leaves her dorm room."

        "Oh. What happened to you, if you don't mind me asking. I don't want to make you relive unpleasant memories.":
            $r_romance=r_romance+2
            "(Reiki blushes slightly at you.)"

            r  "It happened so long ago now. I didn't think anyone would be willing to listen."

            mc "Of course if you're willing to trust me I would love to hear about lil Reiki before he became a vengeful spirit."

            r  "My story is a common one, but what made it so much worse was the fact that it was my last day of high school senior year. I had completed everything I needed to do to graduate smoothly and when I least expected it the person I trusted most stabbed me in the back. I would tell you more, but the specific memories of that moment have disappeared from my mind and all I have left is the hate I felt for my only friend."

            mc "I’m so sorry that happened to you. I hope one day you will be able to trust people again."

            r "(Whispered) \"With you I might just be able to.\""

            mc "What was that?"

            r  "Oh nothing… So how did you end up here?"

            mc "My story is similar to yours in the fact that it happened my senior year. I had completed graduation and was looking forward to my future, when my father, who is totally a nekomata like me, well let’s just say something terrible happened and me and my mother moved out here."

            r  "I guess we have something in common. Though I am sorry to hear that something happened to your Father. If you ever want to talk more about it I'm here."

            mc "Thanks and I'm here for you too."


        "Wow! Now I know why you're such an unlikable person.":
            $r_hatred=r_hatred+4
            "(Reiki looks so annoyed at you. Like seriously, he’s about to pop a freaking vein. A VEIN.)"

            r "I-so-fucking-hate-you-you-piece-of-shit. Why am I talking to you again..."

            "(Reiki sighs.)"

            mc "Because of the lucky convenience of living together. So, prepare for the worst. Wink"

            "(You actually winked at him. Good job. Prepare your grave.)"

            "Suddenly you hear a room open as Kimiko leaves her dorm room."

        "Wow, I'm so shocked that happened to you. COUGHnotreallyCOUGH":
            $r_hatred=r_hatred+4
            "Reiki looks annoyed and sighs."

            r "Anyways... "

            "Suddenly you hear a room open as Kimiko leaves her dorm room."
    "(You watch as Kimiko makes her way towards you and Reiki in the kitchen.)"

    show kimiko

    k "Oh hey guys. I see you two have met each other already."

    r "Yes we met yesterday during class sign up."

    k "Oh nice so we can skip the introductions. Also [MC NAME], I brought the stuff you asked me from home and it's in my room if you want to pick it up later"

    mc "Oh yes. thank you so much."

    k "It's no big deal. Though I should let you know, we have two other dorm mates, whom we will probably see sometime soon."

    mc "Really who-"

    "(Just as you are about to ask that question, two doors open, and you see Taiki and Himiko exit their rooms.)"

    show taiki
    show himeko

    t "Kimiko, how come you didn't invite me to this little party you seem to be having?"

    k "It's not a party. We all just happened to end up in the common space at the same time."

    h "Are you sure you aren't all here to greet me and give me your daily offerings?"

    "(Kimiko sighs.)"

    k "Oh Himiko... I told you when you joined our dorm unit, we wouldn't be praising you. Wasn't that the whole appeal of joining us instead of the leaders of your fan club?"

    "(Himiko flips her hair sarcastically.)"

    h "Yeah, I guess you're right. It's nice to be able to just leave my room without people crowding around me."

    k "So, what's you guys’ plans for free period today? I’m probably going to the library to find some new books."

    t "Well, I was hoping to take [MC Name] around campus since we didn't get a chance to talk for long yesterday?"

    mc "Sure, that sounds like fun where are you taking me?"

    hide kimiko
    hide himeko
    hide reiki

    t "On a date. Wink."

    "(Taiki winks.)"

    "O-On a... wha-"

    t "Just kidding. It’s just a surprise, so you better be ready."

    mc "Oh okay. Any hints on what we are doing?"

    t "Well…. just be ready for anything!"

    show kimiko
    show himeko
    show reiki

    k "Ohh sounds like fun, what are the rest of you planning?"

    h "I'll probably just be surrounded by my fans all day again today."

    "(She sighs)"

    r "I'll probably hide away from everyone in my room and listen to music like usual."

    h "You mean that weird Emo Sad stuff you call music? Come on, man. How are you supposed to make friends when you just lock yourself away all the time?"

    r "More like, how are you supposed to make friends when you're surrounded by people who praise you all day…"

    hide reiki

    t "Come on guys. We are gonna be living together for a while, so let's not already start some bad blood."

    "(Taiki huddles everyone together in a bear-hug.)"

    k  "He is right; I know you don't get along, but you should at least attempt to make friendly with each other."

    "(Reiki and Himiko sigh and push Taiki away.)"

    k "Anyway, we should hurry up since me and [MC Name] have class together in a little while."

    h "Oh ummm…. I was hoping to walk with [MC Name] to class. They could be a good protection from my fan club, and I've been meaning to educate [her/him] on this school's diverse history."

    menu:
        "Oh well. I was already planning on walking with Kimiko, but maybe next time.":
            $k_romance=k_romance+2
            $charisma=charisma+2

            "(Kimiko blushes at you and Himiko looks sad.)"

            k "Really? Are you sure? Himiko seems to really want to go with you."

            mc "I said I would go with you, and I really enjoy hanging out with you."

            h "Well if you want to go with her, I guess I can’t stop you..."

            k "Well if you're sure."

            hide himeko
            show kimiko
            scene hallway

            "(You and Kimiko leave the dorm room after an enjoyable breakfast. As you're walking down the hall, you decide to start a conversation.)"

            mc "Thanks for everything you have done for me, Kimiko. You have really helped me out after I caused you so many problems."

            k "It's fine. I should have done a better job of explaining my situation to you on the first day, then maybe you wouldn't have followed me all the way here."

            mc "No, you shouldn't blame yourself. You really are a good person, Kimiko."

            k "I really don't think I am a good person; you know what the main traits of a Kitsune are. We trick people using our charisma to entice unknowing humans. Everyday, I'm reminded of that fact as I attend this school filled with mythical beings. We were all created to hurt humans, but I don't think I want to. Especially after meeting you. I wish I wasn't born a Kitsune and then maybe I could have lived a normal life."

            mc "You know I like you even if you are a Kitsune. You haven't once tried to trick me with your powers which proves you are a good person."

            k "Do you really think so?"

            mc "I know so."

            k "Thank you [MC Name]. It looks like we have arrived. I'll see you after class."

            "(You and Kimiko arrive at the door to your classroom and walk inside.)"

        "Yeah, I have been meaning to learn more about this school’s history too, Himiko.":
            $r_romance=r_romance+2
            $intelligence=intel+2
            "(Himiko blushes and Kimiko looks sad.)"

            h "Nice! I knew you would make the right choice!"

            k "Yeah I think it would be good for you and Himiko to get closer."

            mc "Alright. I'll see you later, Kimiko."

            hide kimiko
            scene hallway

            "(You and Himiko leave the dorm room and start the walk towards your classroom. As you are walking down the hall, you notice a group of people staring at you menacingly. )"

            h "Don't mind them. They basically follow me everywhere, but they never get the courage to actually talk to me."

            mc "Really? That's crazy. What's it like having your own fan club?"

            h "Honestly, it's really annoying. I know they love me and everything, but they have never really taken the time to get to know me. Kimiko was the first person to ask me to dorm with her and before her everyone always just followed me expecting me to be this great light that will bless them just by looking at me."

            mc "I'm sorry you have to go through all that. It must be hard on you."

            h "It's fine, this is all part of my duties as a Sun Goddess. I knew I would have to deal with all the expecting eyes from day one. It's just no one tells you how hard it is to be the person everyone looks up to. I have to contemplate my every move thoroughly."

            mc "Well, I hope you don't feel like you have to be a perfect person with me. If one day you decide to break down your walls and become who you want to be, I will continue to stay by your side!"

            h "Thanks [MC Name] I knew it was a good decision to ask you to join me today."

            mc "I'm glad I could be here with you today too."

            h "Well this is your stop. I hope you have a good day!"

            "(You and Himiko arrive at the door to your classroom and you walk inside.)"

        "Sorry Girls, I'm a free spirit and don't want anyone holding me down. But, maybe next time." :
            $t_friendship=t_friendship+1
            $intel=intel-1
            $fun=fun+2


            "(Himiko and Kimiko look sad.)"

            t "That's my [girl/boy] us free spirits roam together!"

            "(Kimiko and Himiko sigh as you high five Taiki.)"

            k "Well, I'll let this free spirit find [his/her] own way to class then."

            hide kimiko
            hide himeko
            hide taiki
            scene hallway

            "(You quickly realise your mistake as you leave the dorm room to complete the long treacherous walk to wherever your classroom may be… While walking, you notice a random student and decide to ask them for directions.)"

            mc "Excuse me do you know the way to classroom 112."

            rando "Ummm you’re on the wrong side of the school. You need to go to the end of the hall, make a left, then a right, and another right, then another left."

            mc "Ummm…. Sure."

            "(As you attempt to follow the directions the Student gave, you notice Kimiko walking down a hallway. You rush towards her grabbing onto your last hope to get to class.)"

            show kimiko

            k "Look who decided to show up."

            mc "I'm really sorry, Kimiko. I'm so lost. Can you please show me the way to class...?"

            k "Alright. Hurry and follow me. We don't want to be late."

            "(You follow Kimiko and arrive at the door to your classroom just in time.)"
    scene magicalclass

    "(After arriving to class, you sit down in your seat and turn your attention towards Prof. Hayato. He starts the lecture for Introduction to Magical Beings. As you sit and listen to the lecture, you notice yourself tuning the Prof out.)"
    show professor Hayato

    menu:
        "You force yourself to continue listening to the lecture even though it's soooo… boring. Yaaawn ":
            $intel=intel+2

            "(While listening to the lecture, you learn more about the Nekomata species giving you a better idea of how to blend into the school.
            Suddenly, one of Himiko's fans throws a pencil at you, and you turn your attention towards the attacker. While  looking away, Prof. Hayato yells at you to get your attention.
            )"

            prof "Excuse me, [MC Name]. It seems like my lecture wasn’t interesting enough for you. Maybe you would find it far more interesting in the Headmaster’s Office."

            mc "WHAT! I looked away for one second."

            prof "And now you're talking back. I think you should head straight to the Headmaster's Office Now!"

            mc "Fine...."

            "(As you leave the classroom, you bid Kimiko goodbye, and take the lonely walk towards the Headmaster's Office.)"

        "You tune the lecture out as you think about the fun Manga you started last night. The story was far more interesting than whatever the teacher is talking about.":
            $intel=intel-1
            $fun=fun+2

            "(While daydreaming about the amazing life of the Main Character of your favorite Manga, you notice someone rush by the classroom window and turn to look out the window. While looking away, Prof. Hayato yells at you to get your attention.)"

            prof "Excuse me, [MC Name]. It seems like my lecture wasn’t interesting enough for you. Maybe you would find it far more interesting in the Headmaster’s Office."

            mc "Oh well... Maybe it would be more interesting than whatever you were talking about..."

            prof "Excuse me! Yes, I think you should start making your way straight to the Headmaster's Office Now!"

            mc "Fine...."

            "(As you leave the classroom, you bid Kimiko goodbye, and take the lonely walk towards the Headmaster's Office.)"
        "You take out some paper and decide to write Kimiko a note instead of paying attention to the lecture.":
            $charisma=charisma+2
            $intel=intel-1
            $k_friendship=k_friendship+1

            "(You begin your note to Kimiko like most notes passed in school. You write on the paper the simple words \“IM BORED…..\”)"

            "(As you yeet the paper across the class room to Kimiko, she picks up the note and looks at you smiling.)"

            "After opening and responding to the note, she throws it back to you with the words \“Well, maybe you should try paying attention. They are talking about the Nekomata species.\""

            "You reply to the note with the words: \“But the professor is so boring…\” As you throw the note once again across the classroom, you realize a little too late that your aim was off and the note lands right in front of Prof. Hayato. He turns his attention to you as he opens the note and reads the words you had written."

            prof "Excuse me, [MC Name]. It seems like my lecture was so boooring that you felt the need to tell me with this note. I think it would be best if you made your way straight to the Headmaster's Office Now!"

            mc "Fine…."

            "(As you leave the classroom, you bid Kimiko goodbye, and take the lonely walk towards the Headmaster's Office.)"
    scene hallway

    "As you make your way to the Headmasters office, you feel your anxiety rise. You have yet to meet her, but for some reason you could tell that you didn't want to be anywhere near her."

    scene principal office

    "(After arriving at the headmaster's office, you introduce yourself to the lady at the front desk, who tells you to go right in and wait as someone would be on their way to talk to you. As you sit in the leather chair waiting for your fate, you hear the door open and instead of the headmaster a strong muscular man walks in.)"

    strongman "The Headmaster isn't available right now so I've been told to come here and interrogate you. This should be simple and easy as long as you are not a human."

    "(You feel your panic rise as he brings up the word “human”. You quickly decide the best way to fix this situation is to fight your way out of it.)"




    return
