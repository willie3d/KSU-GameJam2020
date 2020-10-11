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
define randoTeach =Character("Random Teacher")
define bob= Character("Bob the Bodyguard")
define k_friendship = 0
define k_romance = 0
define k_hatred = 0
define t_friendship = 0
define t_romance = 0
define t_hatred = 0
define h_friendship = 0
define h_romance = 0
define h_hatred = 0
define r_friendship = 0
define r_romance = 0
define r_hatred = 0
define intel=5
define charisma=5
define fun=5
image studentFighter = im.Scale("../images/char/MaleProtagSilhouette.png", 250, 1000)
image silhouette = im.Scale("../images/char/FemaleProtagSilhouette.png", 250, 1000)
image realschool = im.Scale("../images/bg/RealSchool.png", 1750, 750)
image oldschool = im.Scale("../images/bg/SchoolDisguise.png", 1300, 750)
image auditorium= im.Scale("../images/bg/MonsterAuditorium.png", 1500, 750)
image kitsunebackyard=im.Scale("../images/bg/Kitsune_Home_Backyard.png", 1750, 750)
image signuptable=im.Scale("../images/bg/MonsterHallway.png", 1500, 750)
image classroom=im.Scale("../images/bg/WelcomeClassroom.png", 1500, 750)
image dormcommonspace=im.Scale("../images/bg/CommonArea.png", 1500, 750)#smaller
image protagdormday=im.Scale("../images/bg/ProtagDormDay.png", 1750, 750)
image office=im.Scale("../images/bg/Monsterprincipal.png", 1750, 750)
image bedroomDay=im.Scale("../images/bg/mcbedroomnormal.jpg", 1750, 750)
image areanearsignuptable=im.Scale("../images/bg/animefield.png", 1750, 750)
image bedroomNight=im.Scale("../images/bg/McbedroomNight.png", 1750, 1000)
image randoteach= im.Scale("../images/char/RandoTeacher.png", 450, 650)

image tanuki = im.Scale("../images/char/Tanuki-Default.png", 1150, 650)
image tanuki angry=im.Scale("../images/char/Tanuki-Angry-Annoyed.png", 1150, 650)
image tanuki disgusted=im.Scale("../images/char/Tanuki-Annoyed-Disgusted.png", 1150, 650)
image tanuki blush=im.Scale("../images/char/Tanuki-Blushing.png", 1150, 650)
image tanuki sad=im.Scale("../images/char/Tanuki-Sad.png", 1150, 650)


image himiko = im.Scale("../images/char/Himiko-Default.PNG", 1150, 650)
image himiko angry=im.Scale("../images/char/Himiko-Angry.PNG", 1150, 650)
image himiko smug=im.Scale("../images/char/Himiko-Smug.PNG", 1150, 650)
image himiko blush=im.Scale("../images/char/Himiko-Blush.PNG", 1150, 650)
image himiko sad=im.Scale("../images/char/Himiko-Sad.PNG", 1150, 650)
image himiko happy=im.Scale("../images/char/Himiko-Happy.PNG", 1150, 650)

image reiki = im.Scale("../images/char/Reiki-Default.png", 1150, 650)
image reiki angry=im.Scale("../images/char/Reiki-Angry.png", 1150, 650)
image reiki happy=im.Scale("../images/char/Reiki-Happy.png", 1150, 650)
image reiki blush=im.Scale("../images/char/Reiki-Blushing.png", 1150, 650)
image reiki sad=im.Scale("../images/char/Reiki-Sad.png", 1150, 650)

image kimiko = im.Scale("../images/char/Kimiko-Default.png", 1150, 650)
image kimiko angry=im.Scale("../images/char/Kimiko-Angry.png", 1150, 650)
image kimiko happy=im.Scale("../images/char/Kimiko-Happy.png", 1150, 650)
image kimiko blush=im.Scale("../images/char/Kimiko-Blushing.png", 1150, 650)
image kimiko sad=im.Scale("../images/char/Kimiko-Sad.png", 1150, 650)

image kimiko human default= im.Scale("../images/char/Kimiko-HumanDefault.png", 1150, 650)
image kimiko human angry=im.Scale("../images/char/Kimiko-HumanAngry.png", 1150, 650)
image kimiko human blush=im.Scale("../images/char/Kimiko-HumanBlushing.png", 1150, 650)
image kimiko human surprised=im.Scale("../images/char/Kimiko-HumanSurprised.png", 1150, 650)

$ pronoun1 = ("") # he, she, they
$ pronoun2 = ("") # him, her, them
$ pronoun3 = ("") # his, her, their
$ pronoun4 = ("") # his, hers, theirs
$ pronoun5 = ("") # himself, herself, themself
$ pronoun6 = ("") # Sir, Miss, Comrade
$ beauty = ("") #cool, cute, new

# The game starts here.

label start:

    play music "../audio/mixkit-classique-63.mp3"

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
            $ beauty = "cool"
            $ defaultName = "Geophery"
            image silhouette = im.Scale("../images/char/MaleProtag4Silhouette.png", 250, 500)
        "She, Her, Hers":
            $ pronoun1 = "she"
            $ pronoun2 = "her"
            $ pronoun3 = "her"
            $ pronoun4 = "hers"
            $ pronoun5 = "herself"
            $ pronoun6 = "Miss"
            $ beauty = "cute"
            $ defaultName = "Bethany"
            image silhouette = im.Scale("../images/char/FemaleProtagSilhouette.png", 250, 500)
        "They, Them, Theirs":
            $ pronoun1 = "they"
            $ pronoun2 = "them"
            $ pronoun3 = "their"
            $ pronoun4 = "theirs"
            $ pronoun5 = "themself"
            $ pronoun6 = "Comrade"
            $ beauty = "new"
            $ defaultName = "Komrade"
            image silhouette = im.Scale("../images/char/MaleProtag4Silhouette.png", 250, 1000)

    # The phrase in the brackets is the text that the game will display to prompt
    # the player to enter the name they've chosen.
    $ player_name = renpy.input("What is your name, Human?")

    $ player_name = player_name.strip()
    # The .strip() instruction removes any extra spaces the player
    # may have typed by accident.
    #  If the player can't be bothered to choose a name, then we
    #  choose a suitable one for them:
    if player_name == "":
        $ player_name= defaultName

    # These display lines of dialogue.
    "It's been almost a week since the situation with my father took place that changed my life forever.
    My mother and I have decided it would be best for the both of us to move far away from the city and
    live in a remote house in the countryside."

    "We found the house through a family friend and have been living with the Inariou family for the past week.
    They seem nice enough, but I havent really had much time to talk to their daughter who happens to be the same age as me."

    "I'm hopeful that me and my mother will be able to make a good life here and maybe I'll be able to make some new friends."

    ###########TRAILER HERE############
    ###########TRAILER HERE############
    ###########TRAILER HERE############


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bedroomNight

    "UGG I can't seem to be able to sleep..."
    "Maybe I should take a walk, then I might be able to fall asleep."

    scene kitsunebackyard

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show kimiko

    #This waits for sometime
    pause 2

    "UMMM Did I see that correctly.. Did Kimiko just looked like a… fox?"
    mc "UMMMM...Kimiko"

    mc "Oh MY GOD! You're a fox!"

    k "W-What are you talking about? You must be blind."

    show kimiko human surprised
    mc "I literally just saw your fox ears."
    k "I think you need to get your eyes checked, [pronoun6]. T-There’s this good eye doctor at the bottom of the hill."
    mc "I know what I saw!"
    k "No-no. I think you need some glasses... Well I’m going to continue on my peaceful walk now-"

    "No, I can't leave the conversation at that. I know what I saw!"

    "(You grab Kimiko’s arm and prevent her from leaving.)"

    k "Let go of me. I told you. I am not a fox. You probably just saw the shadows or something."


    menu:

        "Look. If you are a fox, I’m not going to judge. Honestly you don’t have to tell me the truth if you don't want to.":
            $ k_friendship += 1
            show kimiko human default
            "Kimiko looks at you with a surprised look on her face, speechless."
            k "..."
            mc "Look. I just-"
            k "I’m sorry."
            "Kimiko touches your forehead, rendering you unconscious"
            mc "Wh-"
            k "Shhhh-"
        "But you were so cute with your ears and tail! Maybe a bit hot. Like H-O-T hot.":
            $ k_romance += 1
            show kimiko human blush
            "Kimiko looks at you with a surprised yet confused look, while blushing very slightly."
            k "W-Wh-What..?"
            mc "I think you’re cute."
            "Kimiko pulls her hand back and flicks your forehead."
            k "..."
            "You are a bit confused."
            mc "What was that-"
            "You pass out."
        "I’m not stupid. Maybe you should stop doubting me, fox girl. Maybe you’re the one that’s stupid.":
            $ k_hatred += 1
            show kimiko human angry
            k "You don’t even know me. Back off."
            "Kimiko shakes her arm violently to get you to let go and kicks you."
            #insert shake
            "BONK!"
            #shake text
            "You hit the ground with a big 'BONK!' to the head and are rendered unconscious from the blow to the head. "

    #insert fade to black slowly
    hide kimiko
    scene black
    with fade
    with dissolve



    #SCENE 2:
    #########


    #Insert creak sound
    play sound "../audio/BESTDOOR.mp3"

    scene bedroomDay
    "Wait, when did I get back to my bedroom? And what was that noise?"
    "(You get out of bed quickly and look outside your window to see whats happening.)"
    "(Suddenly you see Kimiko sneaking out the house and decide to get dressed so you can follow her.)"
    "(You put on a random hoodie and a pair of sunglasses hoping to remain inconspicuious. Then you on leave the house following Kimiko into the woods.)"

    "(You follow Kimiko into the deepest part of the woods. Hiding behind every tree you come across.)"
    scene oldschool


    scene oldschool at truecenter
    "(Suddenly you come cross a clearing in the woods and a large old school house comes into view)"

    "Why is Kimiko going into such a creepy school? Also since when was there a University this close to our home?"

    "(You follow Kimiko through the school gate.)"

    #(Suddenly, a bright light fills the screen and the background changes to an beautiful school)
    stop music
    play music "../audio/School song.mp3"

    scene realschool

    "What in the world is going on? I'm pretty sure this school didn't look this good two seconds ago."

    show kimiko at left
    show tanuki at right

    "Oh! Kimiko is over there. I better hide before she sees me."

    "(You watch Kimiko talk to a male student, and as you attempt to get a closer look, you trip over a tree branch. The male student points in your direction and Kimiko turns to look at you. Suddenly, she rushes to your side.)"

    k "What in the world are you doing here!"

    "More like what are you doing here??"

    "(Kimiko rummages in her backpack and pulls out a pair of cat ears and forces them under your hood onto your head. You look at her with a confused gaze and notice Kimiko’s friend walking towards you.)"

    t "Hey, Kimiko, when were you going to introduce me to your [beauty] friend?"

    k "Oh, this is my Nekomata friend, [player_name]."

    "Excuse me... A what now?"

    t "Hi [player_name], I’m Taiki, a Tanuki, if you couldn't tell by my ears. I've never seen you around before. When did you move here?"

    mc  "Well ummm… you see I just moved here a couple days ago, and I had no idea I was going to be coming to this school till today."

    t "Oh wow. Well, welcome. I hope you enjoy going here. I've heard it's the best school for all us mythical beings. If you have some free time later, I’d love to show you around."

    menu:
        "He doesn’t seem bad. \"Okay sure that sounds like fun.\"":
            $t_friendship= t_friendship+1

            "(Taiki looks at you with a happy expression.)"

            t "Great. I can't wait to show you the amazing history this place has to offer."
            play sound "../audio/betterschoolbell.mp3"

            t  "Oh, that's my cue. I hope to talk to you later."
        "That sounds like fun. Why not. \"Sure I'd love going on a tour with you. You seem very knowledgeable.\"":
            $t_romance=t_romance+1
            show tanuki blush at right

            "(Taiki looks at you with a slight blush.)"

            t "The school has a lot of interesting history and several secret locations I can't wait to share with you."

            play sound "../audio/betterschoolbell.mp3"

            t "Oh, that's the bell. I guess I'll have to leave now.  I'm excited for our next conversation!"
        "But I’m so lazy! \"Ugg..Do I have to.\"":
            $t_hatred=t_hatred+1
            show tanuki angry at right
            "(Taiki looks at you with an angry expression.)"

            play sound "../audio/betterschoolbell.mp3"

            t "Oh well. I'm not forcing you to do anything you don't want."

            t  "Well, I'm gonna get out of your way. Bye."

    hide tanuki

    "(Kimiko quickly pulls you aside and looks at you with a puzzled look.)"

    mc "What was that all about? I'm a Nekomata now? And your friend is a Tanuki! Where is this? What's going on!"

    k "I'm sorry I had to do some quick thinking before you got yourself hurt. This is the University of Amaterasu, a special school for all mythological beings. I have no idea how you were able to get in here, but we have to hurry and get you out before you're discovered."
    k "If they find out you're a human, they will kill you or steal your soul; both are not very good options."

    mc "Wait! You still didn't explain anything. How does this place even exist!"

    "(Suddenly, you notice a professor walking towards you and Kimiko. He stops in front of the two of you.)"

    prof "What are you guys still doing out here?! It's not safe after 8am to be standing near the school gates. We don't want any unnecessary human visitors. Now, hurry along, I'll escort you to the auditorium for the freshmen orientation."

    k "Wait, Prof Hayato, I left something at home, and I have to go back."

    mc "Yeah, it's really important that we leave and go home right now!"

    prof "I'm sorry it's too late to leave now. You know how dangerous it would be if we get noticed. Now hurry along."

    "(Whispered) \"Damn it, just follow my lead. We will leave at the end of the day!\""

    "(The professor leads you and Kimiko to the auditorium, where you notice students standing in *attention. Looking towards the stage, you see a beautiful lady standing at the podium looking down upon the students.)"
    "(Standing beside her, you notice what seems to be the Headmaster, who you can't see clearly as she stands in the darkness. As you stand in your place, the room begins to go quiet, and the students turn their attention towards the stage.)"

    scene auditorium

    hide kimiko
    show himiko smug

    h "Hello Everyone! My name is Himiko, and I am your class president. Welcome, freshman students, to the University of Amaterasu."
    h "The first university of its kind designed by my ancestors to introduce young mythological beings like yourselves to the human realm with classes from blending in to the human realm to taking a human soul."

    h "The goal of this university is to prepare you all for your lives outside, whether you take the boring option of becoming one with humans or the far more interesting option of taking human souls as your play things."
    h "I hope you find this university to be everything you have ever wanted, and if you need anything, feel free to talk to me as I said before this university is my family legacy. Now head outside and register for your first semester classes!"

    play sound "../audio/applause.wav"

    "(The auditorium burst into applause as the speech ended, and the students started walking out one by one, lining up to register for their classes. You follow Kimiko towards a table labeled \"Mythical Animal Registration\".)"

    scene signuptable

    "(On your way towards the registration table, you trip over someone's foot and end up pushing a male student to the ground. As you look down on the man you just pushed to the floor, you feel your embarrassment rise and attempt to help him up.)"

    show kimiko at left
    show reiki at right

    r "WHAT THE FUCK!"

    show reiki angry at right

    mc "OMG I’m so sorry! I was too focused on the table. I wasn't looking where I was going."

    "(The man grumbles and has a very displeased look on his face with his bangs somewhat over his eyes.)"

    r "Watch where you’re going! I don’t have time to get trampled by the likes of someone like you."

    menu:
        "Like I said, I’m sorry. I didn’t mean to bump into you. I apologize.":
            $r_friendship=r_friendship+1

            "(Reiki deeply sighs.)"

            show reiki at right

            r "Please watch where you’re going next time. You’re glad it was me and not one of the others. Also, you didn’t BUMP into me. You PUSHED me, but I will let it slide this time."

            mc "Okay… But-"

            rando "Hey Reiki! You gotta hurry and register for classes."

            "(Reiki leaves you alone, and you notice Kimiko waving you over to the table.)"

        "You help Reiki up. \"I apologize. I didn’t mean to. Please take this as a token of my apology.\" You give Reiki a corgi keychain.":
            $r_romance=r_romance+1
            "(Reiki looks a bit surprised.)"

            show reiki blush at right

            r "Oh- I actually… Really like these… H-How did you know?"

            "(Reiki blushes a bit.)"

            mc "Oh. I didn’t. I just also like them a lot."

            "(You smile.)"

            r "Thanks… Hey maybe-"

            rando "Hey Reiki! You gotta hurry and register for classes."

            r "Oh, I'm Sorry I have to get going, I hope we can talk again sometime soon."

            "(Reiki leaves you alone and you notice Kimiko waving you over to the table.)"

        "You cross your arms. \"I’m soooorry, princess.\"":
            $r_hatred=r_hatred+1

            show reiki angry at right

            "(Reiki stands up and looks at you in complete anger and disgust.)"

            r  "Princess? Who are YOU calling princess, asshole."

            "(Reiki steps closer to you, while you backs away a little bit.)"

            mc "Look. All I’m saying is that you don’t have to act so rude because I accidentally bumped you down."

            r "BUMPED into me? You full-force PUSHED me. I think you’ll need to grovel before me to truly apologize to me."

            mc "Yeah right-"

            rando "Hey Reiki! You gotta hurry and register for classes."

            r "You’re free this time. Just don't let me see your face again."

            "(Reiki leaves you alone and you notice Kimiko waving you over to the table.)"

    "Well, that certainly was an interesting conversation."

    hide reiki
    scene signuptable
    show kimiko at left
    show randoteach at right

    "(You follow Kimiko to the table you were walking towards before. While waiting in the line, Kimiko turns towards you.)"

    k "(Whispered) Okay, when you get to the table, tell them you want to register for: Introduction to Magical Beasts, Magical Beast Transformations, Introduction to the Human Race, and Introduction to Magical Abilities."
    k "These should all be easy classes for you to hide the fact that you're not supposed to be here. But don't worry, I’ll be standing behind you if you mess up."

    "(As you move closer to the table, you try to remember the classes Kimiko told you to register for. Then, finally, you are at the front of the line.)"

    randoTeach "Welcome to the University of Amaterasu, freshman! What classes will you be registering for today?"

    menu:
        "Hey, I didn't really have time to prepare for today so my friend-o here will tell you what classes would work best for me.":
            $fun=fun+1
            "(The person accepts your excuse and looks towards Kimiko.)"
            "[pronoun1] will register for Introduction to Magical Beasts, Magical Beast Transformations, Introduction to the Human Race, and Introduction to Magical Abilities."
            randoTeach "Alright. And can we get your name?"
            mc "[player_name]"
            randoTeach "All right you are registered. Here is the schedule. Have a good semester!"
        "I will register for Introduction to Magical Beasts, Magical Beast Transformations, Introduction to the Human Race, and Introduction to Magical Abilities":
            $intel=intel+1
            $charisma=charisma+1
            $k_friendship=k_friendship+1
            show kimiko happy

            "(Kimiko looks proudly at you.)"

            randoTeach "Those are all very good classes. Now can we get your name?"

            mc "[player_name]"

            randoTeach "All right you are registered. Here is the schedule. Have a Great Semester!"

        "I will register for Introduction to Magical Beasts, Magical Human Transformations, Introduction to Race, and Introduction to Magic":
            $intel=intel-1
            $charisma=charisma-1
            show kimiko angry

            "(Kimiko looks annoyed at you.)"

            randoTeach "I'm not sure we offer all those classes…"

            k "I'm sorry about [pronoun2] they are new here. [pronoun1] will register for Introduction to Magical Beasts, Magical Beast Transformations, Introduction to the Human Race, and Introduction to Magical Abilities"

            randoTeach "Oh okay then, and does [pronoun1] know their name?"

            mc "Oh yes my name is [player_name]."

            randoTeach "Seems like you do know how to answer questions... Alright you are registered. Here is the schedule."
    hide randoteach
    hide kimiko

    "(After registering for your classes, you stand to the side as you wait for Kimiko to finish her registration. While waiting, you notice a crowd start to gather in the center of the room and decide to move towards the crowd to see what's happening."

    "As you get closer, you notice the lady from the stage earlier surrounded by students rushing to talk to her. As you attempt to get closer, one of her bodyguards walks toward you and pushes you to the floor. While getting back up you notice the woman walk towards you as she offers you her hand.)"

    window hide
    call battle1
    window show

    show bob at left
    show himiko at right

    h "Seriously, Bob, how many times do I have to tell you to stop pushing people to the floor."

    bob "I'm sorry I didn't think [pronoun1] would be that weak"

    h "Seriously, we don't need another person trying to get money from my family,"

    "(Himiko moves closer to the MC)"

    h "Now are you okay, and can you stand?"

    mc "Yes, I think I'm okay."

    h "That's good. My name is Himiko. I'm a Sun Goddess and the daughter of the owner of the school."

    mc "Hi, my name is [player_name]"

    h "Hi [player_name]. Now I should be going, is there anything you want so that we can keep this incident quiet."

    menu:
        "No, it's really okay. I don't need anything.":
            $h_friendship=h_friendship+1

            show himiko happy at right

            "(Himiko looks at you with a happy expression.)"

            h "Okay, well if you ever need anything, feel free to talk to me. I feel like we could be good friends."

            "(Himiko walks away, and you are left standing alone as the crowd follows her out.)"
        "Well, maybe you could show me around the school some time.":
            $h_romance=h_romance+1

            show himiko blush at right

            "(Himiko looks at you with a slight blush.)"

            h "Sure, I'll look forward to it. I'll let you know when I’m free."

            "(Himiko walks away, and you are left standing alone as the crowd follows her out.)"


        "You could give me some money, and I might just forget about all of this.":
            $h_hatred=h_hatred+1
            show himiko angry at right

            h "Oh well, Bob, I'll let you deal with this."

            bob "Here is 10,000 yen. Don’t use it all at once."

            "(Himiko walks away, and you are left standing alone with the money you just earned as the crowd follows Himiko out.)"
    hide himiko
    hide  bob

    "Wow, that girl has a large fan club… Let me not incur the wrath of one of them."

    "(As you make your way back towards the table where you left Kimiko, you notice a male student rushing towards you. Suddenly, he phases in front of you and attempts to push you backwards. As you catch your balance, you look towards your assailant.)"

    scene areanearsignuptable
    show rando fightingboy

    rando "Who told you that you were allowed to talk to our Goddess Himiko!"

    mc "Um.. I don't know what you mean she talked to me first?"

    rando "Shut up, you pussy cat! You're not getting out of here without a fight!"

    #fighting squence occurs

    "(After your fight with the Random Student, you watch as he runs away from you with tears in his eyes.)"

    hide rando fightingboy

    "Serves him right attempting to fight me when I don't even know him."

    "(You turn away from him and return to the table where you see your friend Kimiko waiting for you.)"

    scene signuptable
    show kimiko

    k "Where did you go? We have to go to our classroom for the first day events."

    mc "Sorry, I noticed a bunch of people gathering around and thought I should check it out."

    k "Oh well, you should keep close to me. We don't want any unnecessary attention. Now let's head out so we can hurry up and get out of here."

    scene classroom

    "(You and Kimiko walk towards your first and only class for the first day of school. As you sit through the boring introduction lecture, you begin to tune out the professor and sit and reflect on the events of the day. You think back to each of the people you met thus far.)"

    #(An image with the name of each character flashes on screen.)

    scene allcharlineup

    menu:
        "I really enjoyed spending the day with Kimiko, I'm so glad we have this class together.":
            $k_romance=k_romance+1

        "Himiko was surprisingly nice. I really want to get to know her better.":
            $h_romance=h_romance+1

        "I enjoyed meeting Taiki this morning. I wonder when I will get to meet him again.":
            $t_romance=t_romance+1

        "Reiki was defininty a surprising person to talk to. I'm sure any conversation with him would be entertaining." :
            $r_romance=r_romance+1

        "None of these people were all that interesting. I would say I'm the coolest person here.":
            $fun=fun+1

        "All the people I met were super lame. I don't think I want to stay here much longer.":
            $k_romance=k_romance-1
            $h_romance=h_romance-1
            $t_romance=t_romance-1
            $r_romance=r_romance-1
    scene realschool
    stop music
    play music "../audio/leavingschool.mp3"
    "(At the end of your class, Kimiko grabs your hand and rushes you quickly out of the classroom. You find yourself back at the school's entrance and notice how you have arrived before any of the other students.)"
    "(Kimiko attempts to push you out of the gate when suddenly you're hit by an invisible force field and get thrown backwards. You look up at Kimiko questioning what just happened.)"

    show kimiko

    k "Oh no, oh no! I think you're stuck in here……."

    "Say WHAT?"

    mc "What do you mean I'm stuck here?!"

    k "Humans aren't supposed to be able to pass through the gate as it has a spell to keep them out. I guess something must have gone wrong and now you can't get out."

    menu:
        "How did I even get in here in the first place if that’s the case?":
            $intel=intel+1
            $k_friendship=k_friendship+1

            "(You look at Kimiko in a thinking pose.)"

            k "That’s a good question… However, we don’t really have the time or knowledge right now to figure that out. Let’s just head to the housing office and hope we can find you somewhere to stay for the night."

        "Well, if I’m stuck in here, can I stay where you’re staying? Wink. ;)":
            $k_romance=k_romance+1
            $fun=fun+1

            show kimiko blush

            "(You actually wink after that… Wow.)"

            "(Kimiko blushes a little bit and then composes herself, sighing a little bit.)"

            k  "I-I can’t promise anything. Now let’s go. We need to head to the housing office and hope we can find you somewhere to stay for the night."

        "You didn’t think this through?! What the hell!":
            $charisma=charisma-1
            $k_hatred=k_hatred+1

            show kimiko angry

            "(Kimiko sighs in disappointment.)"

            k "Okay. Look. I wasn’t the one who told you to follow me, okay? Now let’s go. We need to head to the housing office and hope we can find you somewhere to stay for the night."

            "(Kimiko grabs you by the ear and drags you along.)"

    scene office
    stop music
    play music "../audio/mixkit-classique-63.mp3"

    "(Kimiko escorts you to the housing office to hopefully find some on campus housing.)"

    k "(Whispered)\"Remember this is only temporary until we can find a way for you to get out of the forcefield.\""

    show rando at left
    show kimiko at right

    rando "Welcome, how may I help you today?"

    k "Hi, my friend here is wondering if there are any housing options left available... possibly in the same unit as me?"

    "(She coughs, slightly blushing.)"

    rando "Well, looking here, you two are in luck as we have one empty room in that unit."

    show kimiko happy

    mc "Oh Yes! I'll take that room!"

    rando "Very nice, here is the key to room 1312 B. Have a good semester!"

    hide rando
    hide kimiko

    scene dormcommonspace
    show kimiko

    "(Kimiko escorts you to the housing unit, and you take a short look around the common space before being escorted to your bedroom.)"

    scene protagdormday
    show kimiko

    k "Alright. This is your room. I'll be heading out to go grab some of your belongings, and I'll inform your mom of the current situation."

    mc "You are going to tell my Mom about all of this??"

    k "Weeeell, not exactly. Us, Kitsune, have the ability to influence people, and I can convince your mother that you agreed to attend this university."

    mc "Oh really.. I guess that makes it better knowing that she won't be worried about me."

    k "Just rest well. You had a weird and stressful day. I'll see you tomorrow for the first official day of school."

    "(After Kimiko leaves your room, you get ready for bed. As soon as you get into bed, you find yourself falling asleep after such a long and weird day. - We don’t blame you. Lol)"

    scene black

    "End of Day 1:"

    "Charisma: [charisma]"

    "Intelligence: [intel]"

    "Fun: [fun]"

    # This ends the game.

    call start2 from script2
