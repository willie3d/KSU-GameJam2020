label init_skills:
    #    init_skills is a label that is called to initalize skill fighter_skill objects.
    #    All skills should be declared here first otherwise if an undeclared skill is used by a fighter
    #    inside label init_fighters, it will return an error.
    $ SmartAttack = fighter_skill(
        SKL = "Smarts",
        DMG = intel,
        AOE = True,
        COST = 0,
        ELEM = "None",
        DESC = "Smart attack?",
        GFX = "fire 1",
        SFX = "sfx/claw-135608256.ogg",
        PAUSE = 0.30
    )

    $ CharismaAttack = fighter_skill(
        SKL = "Charisma",
        DMG = charisma,
        AOE = True,
        COST = 0,
        ELEM = "None",
        DESC = "Charisma attack?",
        GFX = "fire 1",
        SFX = "sfx/claw-135608256.ogg",
        PAUSE = 0.30
    )

    $ FunAttack = fighter_skill(
        SKL = "Fun",
        DMG = fun,
        AOE = True,
        COST = 0,
        ELEM = "None",
        DESC = "Fun attack?",
        GFX = "fire 1",
        SFX = "sfx/torch_movement_fireball_burst.mp3",
        PAUSE = 0.30
    )

    $ GenericAttack = fighter_skill(
        SKL = "yeet test string",
        DMG = 5,
        AOE = True,
        COST = 0,
        ELEM = "None",
        DESC = "Fun attack?",
        GFX = "fire 1",
        SFX = "sfx/torch_movement_fireball_burst.mp3",
        PAUSE = 0.30
    )
