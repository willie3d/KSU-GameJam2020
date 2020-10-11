init python:
    import random
    def increaseDef(initiator):
        """
                increaseDef is a function that increases a fighter's defense during battle.
                Args:
                        initiator (fighter): The current figher that initiated the defend action.
        """
        xATK = initiator.ATK
        xDEF = initiator.DEF
        xSPD = initiator.SPD
        xMG = initiator.MG
        xHP = initiator.HP
        xMP = initiator.MP

        defBonus = (xSPD + xMG + xHP + xMP) / 4
        defBonus = defBonus  * 0.05
        recMana = initiator.MP * 0.10

        defBonus = float("{0:.2f}".format(defBonus))
        recMana = float("{0:.2f}".format(recMana))
        initiator.DEF += defBonus
        initiator.MP += recMana
        pstring02  = initiator.FTR + " is defending.  Defense increased by " + str(defBonus) +".  " + str(recMana) +" mana recovered."
        narrator(pstring02,  interact=False)
        #renpy.pause (normal_settings.dialogue_pause)
        initiator.normalize_stats
        return [int(defBonus), int(recMana)]


    def damageTarget(initiator, skill, target):
        """
                damageTarget handles damage calculation and calls animation for single-target skills.
                Args:
                        initiator (fighter): The current figher that initiated the defend action.
                        skill (fighter_skill): The skill as selected by the initiator.
                        target (fighter): The fighter chosen as target.
        """
        initiator.normalize_stats
        initiator.MP -= skill.COST
        initiator.normalize_stats
        if skill.AOE:
            pstring01 = initiator.FTR  + " used " + skill.SKL  + " on enemies as target."
            narrator(pstring01, interact=False)
            #renpy.pause (normal_settings.dialogue_pause)
            targets = target
            x_total = 0
            doneAni = displayAOEanimation(initiator, skill, targets)
            for i in targets:
                if i.ALIVE:
                    x = damageActual(initiator, skill, i)
                    x_total += x
            pstring04 =  str(x_total) + " damage afflicted on targets."
            narrator(pstring04,  interact=False)
            #renpy.pause (normal_settings.dialogue_pause)
            return x

        else:
            """ The following code calls the displayAnimation method and resultant strings."""
            if target.ALIVE:
                doneAni = displayAnimation(initiator, skill, target)
                pstring01 = initiator.FTR + " used " + skill.SKL  + " on "  +target.FTR + " as target."
                narrator(pstring01,  interact=False)
                #renpy.pause (normal_settings.dialogue_pause)
                x = damageActual(initiator, skill, target)
                pstring04 =  str(x) + " damage afflicted on target."
                narrator(pstring04,  interact=False)
                #renpy.pause (normal_settings.dialogue_pause)
            return x


    def damageActual(initiator, skill, target):
        """
                damageActual is the one that actually computes damage values.
                damageActual returns the damage done to target.
                Args:
                        initiator (fighter): The current figher that initiated the defend action.
                        skill (fighter_skill): The skill as selected by the initiator.
                        target (fighter): The fighter chosen as target.
        """
        iATK = initiator.ATK
        iDEF = initiator.DEF
        iSPD = initiator.SPD
        iMG = initiator.MG
        iHP = initiator.HP
        iMP = initiator.MP
        iELEM = initiator.ELEM

        tATK = target.ATK
        tDEF = target.DEF
        tSPD = target.SPD
        tMG = target.MG
        tHP = target.HP
        tMP = target.MP
        tELEM = target.ELEM

        sDMG = skill.DMG
        sCOST = skill.COST
        sELEM = skill.ELEM

        # This block calculates damages.
        modDMG = random.randint(90, 100)
        modDMG = modDMG / 100
        xDMG = sDMG * (iATK*modDMG) * (iMG/10)
        xDMG = sDMG - (tDEF*modDMG)
        if xDMG <= 0:
            xDMG = 0



        # This block actually deducts the damage from target's health.
        print str(xDMG) + " damage"
        target.HP =  target.HP -  xDMG
        initiator.normalize_stats
        # Following code changes the target's status depending on HP left.
        if target.HP <=0:
            target.HP = 0
            if not target.ALIVE:
                target.ALIVE = False
                print "Target was already dead."
            elif target.ALIVE:
                print "Killing target."
                target.ALIVE = False
                pstring00 = target.FTR + " incapacitated."
                hideFighter(target)
                renpy.with_statement(dissolve, always=False)
                narrator(pstring00,interact=False)
                #renpy.pause (normal_settings.dialogue_pause)
            else:
                print "Warning.  Something is not right"
        return int(xDMG)
