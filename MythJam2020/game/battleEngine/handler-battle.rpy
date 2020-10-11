init python:
    import random
    def  executeBattle(alllies, enemies, orderInitiators):
        """
            executeBattle starts the battle itself. When a certain condition is met, it returns a number
            corresponding to the victorious party.
            Args:
                allies (list): A list containing fighters friendly to the player character.
                enemies (list): A list containing fighters hostile to the player character.
                orderInitiators (list): A list containing the order in which fighters execute actions.
        """
        displayFighters(orderInitiators)
        renpy.with_statement(dissolve, always=False)
        renpy.block_rollback()
        onBattle = True         # Battle is ongoing.
        turnNum = 0             # Total turn number a.k.a how many loops.
        pstringStart =  "Engagement started!"
        narrator(pstringStart,  interact=False)
        renpy.pause (normal_settings.dialogue_pause)
        # hp_stats and mp_stats list returns lists containing original hp/mp stat values per fighter.
        hp_stats = listStat(allies+enemies, "HP")
        mp_stats = listStat(allies+enemies, "MP")
        print hp_stats
        print mp_stats
        while onBattle:
            turnNum += 1        # Increment turn count.
            print "turn " + str(turnNum)
            renpy.show_screen("turn_counter", turnNum)
            if  normal_settings.with_bars:
                renpy.show_screen("stat_bars", allies+enemies, hp_stats, mp_stats)
            for x in orderInitiators:
                xEnemy = findEntry(x, enemies)  # Determine if x is an enemy.
                initiator = x
                initiator.normalize_stats
                if xEnemy:
                    if initiator.ALIVE:
                        print "AI is active."
                        selectedAction = random.choice(["engaging", "defending"])
                        selectedSkill = aiSkillSelection(initiator)
                        if selectedAction == "engaging":
                            pstring07  = initiator.FTR + " is engaging."
                            print pstring07
                            narrator(pstring07,  interact=False)
                            renpy.pause (normal_settings.dialogue_pause)
                            if selectedSkill.AOE:
                                selectedTarget = allies
                            else:
                                selectedTarget = aiTargetSelection(allies)
                                x = damageTarget(initiator, selectedSkill, selectedTarget)
                                renpy.block_rollback()
                        else:
                            answer = increaseDef(initiator)
                            renpy.block_rollback()
                    else:
                        print "AI is dead."
                else: # If current  is an AI:
                    if initiator.ALIVE:
                        selectedAction = renpy.call_screen("battleUI", turnNum,  initiator, enemies, allies, useage="action")
                        if selectedAction == "engaging":
                            selectedSkill = renpy.call_screen("battleUI", turnNum,  initiator, enemies, allies, useage="skill")
                            print "AOE: " + str(selectedSkill.AOE)
                            if selectedSkill.AOE:
                                selectedTarget = enemies
                                x = damageTarget(initiator, selectedSkill, selectedTarget)
                                renpy.block_rollback()
                            else:
                                selectedTarget  = renpy.call_screen("battleUI", turnNum,  initiator, enemies, allies, useage="target")
                                x = damageTarget(initiator, selectedSkill, selectedTarget)
                                renpy.block_rollback()
                        else:
                            answer = increaseDef(x)
                            renpy.block_rollback()
                    else:
                        print "Player is dead."
                # Evaluate if battle is finished.
                conBattle = wonBattle(allies, enemies)
                onBattle = conBattle[0]
                victorBattle = conBattle[1]
                if not onBattle :
                    pstring03 = "Engagement end!"
                    narrator(pstring03, interact=False)
                    renpy.pause (normal_settings.dialogue_pause)
                    # The following lines hide the bars, sprites, turn counter with a fade transition.
                    renpy.hide_screen("stat_bars",layer='screens')
                    renpy.scene(layer='battle_sprites')
                    renpy.hide_screen("turn_counter",layer='screens')
                    renpy.with_statement(fade, always=False)
                    return victorBattle
                    break
