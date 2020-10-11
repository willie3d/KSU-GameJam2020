label init_skills:
    #    init_skills is a label that is called to initalize skill fighter_skill objects.
    #    All skills should be declared here first otherwise if an undeclared skill is used by a fighter 
    #    inside label init_fighters, it will return an error.
    $ GenericAttack = fighter_skill(
        SKL = "Attack",
        DMG = 10,
        AOE = False,
        COST = 0,
        ELEM = "None",
        DESC = "Basic attack skill. Low effort, low damage, no cost.",
        GFX = "fire 1",
        SFX = "sfx/claw-135608256.ogg",
        PAUSE = 0.30
    )
    
    $ HigherAttack = fighter_skill(
        SKL = "High Attack",
        DMG = 100,
        AOE = False,
        COST = 40,
        ELEM = "None",
        DESC = "Big attack, big cost!",
        GFX = "fire 1",
        SFX = "sfx/claw-135608256.ogg",
        PAUSE = 0.30
    )

    $ AOEattack = fighter_skill(
        SKL = "AOE Test",
        DMG = 100,
        AOE = True,
        COST = 40,
        ELEM = "None",
        DESC = "Big attack, big cost!",
        GFX = "fire 1",
        SFX = "sfx/torch_movement_fireball_burst.mp3",
        PAUSE = 0.30
    )
