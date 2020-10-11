
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
        skill_set = [SmartAttack,],
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
        MP = 200,
        ELEM = "Water",
        skill_set = [SmartAttack],
        pic_card ="images/pipo-enemy031.png",
        pic_sprite =  "blackSheep", #"images/pipo-enemy031.png",
        sprite_pos = [0.5, 0.5]
        )

    $ blackSheep2 = fighter(
        FTR = "Black Sheep 2",
        ALIVE = True,
        ATK = 100,
        DEF = 10,
        SPD = 420,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [SmartAttack],
        pic_card ="images/pipo-enemy031.png",
        pic_sprite =  "creamSheep", #"images/pipo-enemy031.png",
        sprite_pos = [0.4, 0.5]
        )

    $ creamSheep1  = fighter(
        FTR = "Cream Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 10,
        SPD = 420,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [SmartAttack],
        pic_card ="images/pipo-enemy031.png",
        pic_sprite =  "creamSheep", #"images/pipo-enemy031.png",
        sprite_pos = [0.6, 0.5]
        )

    $ creamSheep2 = fighter(
        FTR = "Cream Sheep 2",
        ALIVE = True,
        ATK = 100,
        DEF = 10,
        SPD = 420,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [SmartAttack],
        pic_card ="images/pipo-enemy031.png",
        pic_sprite =  "creamSheep", #"images/pipo-enemy031.png",
        sprite_pos = [0.1, 0.5]
        )

    $ pinkSheep1 = fighter(
        FTR = "Pink Sheep 1",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [SmartAttack],
        pic_card = "images/pipo-enemy031a.png",
        pic_sprite = "pinkSheep", #"images/pipo-enemy031a.png",
        sprite_pos = [0.9, 0.5]
        )


    $ pinkSheep2 = fighter(
        FTR = "Pink Sheep 2",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [SmartAttack],
        pic_card = "images/pipo-enemy031a.png",
        pic_sprite ="pinkSheep",# "images/pipo-enemy031a.png",
        sprite_pos = [0.9, 0.5]
        )

    $ pinkSheep3 = fighter(
        FTR = "Pink Sheep 3",
        ALIVE = True,
        ATK = 100,
        DEF = 60,
        SPD = 840,
        MG = 10,
        HP = 420,
        MP = 200,
        ELEM = "Water",
        skill_set = [SmartAttack],
        pic_card = "images/pipo-enemy031a.png",
        pic_sprite = "pinkSheep",#"images/pipo-enemy031a.png",
        sprite_pos = [0.9, 0.5]
        )

    $ brownBear1 = fighter(
        FTR = "Brown Bear 1",
        ALIVE = True,
        ATK = 200,
        DEF = 560,
        SPD = 340,
        MG = 10,
        HP = 420,
        MP = 300,
        ELEM = "Fire",
        skill_set = [SmartAttack],
        pic_card = "images/pipo-enemy037.png",
        pic_sprite = "brownBear", #"images/pipo-enemy037.png",
        sprite_pos = [0.1, 0.5]
        )
