
label init_fighters:
    #    init_fighters acts like a function that initializes fighter objects and their assigned attributes.
    #    Call this label when resetting battle stats back to their defaults.
    $ player1 = fighter(
        FTR = "You",
        ALIVE = True,
        ATK = 100,
        DEF = 10,
        SPD = 420,
        MG = 0,
        HP = 25,
        MP = 0,
        ELEM = "None",
        skill_set = [SmartAttack, CharismaAttack, FunAttack],
        pic_card ="images/pipo-enemy031.png",
        pic_sprite =  "blackSheep", #"images/pipo-enemy031.png",
        sprite_pos = [0.5, 0.5]
        )

    $ blackSheep1 = fighter(
        FTR = "Black Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 10,
        SPD = 420,
        MG = 10,
        HP = 420,
        MP = 0,
        ELEM = "Water",
        skill_set = [GenericAttack],
        pic_card ="images/pipo-enemy031.png",
        pic_sprite =  "blackSheep", #"images/pipo-enemy031.png",
        sprite_pos = [0.5, 0.5]
        )
    $ guard1 = fighter(
        FTR = "Guard 1",
        ALIVE = True,
        ATK = 100,
        DEF = 10,
        SPD = 420,
        MG = 10,
        HP = 15,
        MP = 0,
        ELEM = "Water",
        skill_set = [GenericAttack],
        pic_card ="images/pipo-enemy031.png",
        pic_sprite =  "blackSheep", #"images/pipo-enemy031.png",
        sprite_pos = [0.5, 0.5]
        )
