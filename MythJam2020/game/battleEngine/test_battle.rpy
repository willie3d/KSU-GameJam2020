label battle:
    #This is a test battle.
    #   init_skills initializes fighter skills. Always initiate skills first.
    #   init_fighters initalizes fighter objects. Also resets their values. Do not use if fighters have
    #   dynamic stats linked to another stat system. TL;DR Do not use if fighter stats are fixed stats.
    #   init_skills and init_fighters probably only need to be called once.
    call init_skills
    call init_fighters
    #   Initialize fighters and parties.
    $ player = [creamSheep1]
    $ friends = []
    $ allies = player +friends
    $ enemies = [pinkSheep1, pinkSheep2, pinkSheep3]
    #   fighter.sprite_pos allows manual positioning of sprites.
    #   X-Y coordinates are fed to the attribute via a two-index list.
    #   Might be best if I replace this with a function that accepts a tuple.
    $ creamSheep1.sprite_pos = [0.1, 0.3]                #      left_top
    $ creamSheep2.sprite_pos = [0.1, 0.7]               #       left_bottom
    $ brownBear1.sprite_pos = [0.4, 0.5]
    $ pinkSheep1.sprite_pos = [0.9, 0.3]
    $ pinkSheep2.sprite_pos = [0.9, 0.5]
    $ pinkSheep3.sprite_pos = [0.9, 0.7]
    #   For demonstration purposes, you can also use registerSkill to add a skill to a fighter during
    #   runtime, provided that the skill itself has been initalized earlier.
    $ creamSheep1.registerSkill(AOEattack)
    $ creamSheep2.registerSkill(AOEattack)
    $ allchars = allies + enemies
    #   orderBattle returns a descending list of a characters by specified stat, e.g. SPD.
    #   executeBattle runs the actual sequence and should be left alone.
    #   You can create your own order manually by passing a list of fighters into the orderInitiators
    #   variable.
    #   executeBattle executes the actual battle itself and returns a victory result.
    $ orderInitiators = orderBattle(allchars)
    $ victorBattle = executeBattle(allies, enemies, orderInitiators)
    #   This last block of code is where you add branching statements/win-lose results or whatever.
    if victorBattle<> 3:
        $ config.allow_skipping = True
        if victorBattle == 1:
            "We won!"
        elif victorBattle == 2:
            "They won.  We lost.  Get lost."
    return
