init python:
    def displayAnimation(initiator, skill, target):
        """ 
            displayAnimation is the function that displays a fighter_skill's animation attribute.
            displayAnimation only works for single-target skills.
            Args:
                    initiator (fighter): The current fighter in orderInitiators.
                    skill (fighter_skill): Skill in which to take the animation and sound from.
                    target (fighter): The targeted fighter.   
        """
        renpy.play(skill.SFX, channel='sound')
        renpy.show(skill.GFX, [targetPos(target)], layer='battle_anims')
        renpy.pause(skill.PAUSE)
        renpy.hide(skill.GFX, layer="battle_anims")
        return True

    def displayAOEanimation(initiator, skill, targets):
        """
            displayAOEanimation is pretty similar to displayAnimation except that it works
            only for AOE skills.
            Theoretically, the two functions can be merged but.
            Args:
                    initiator (fighter): The current fighter in orderInitiators.
                    skill (fighter_skill): Skill in which to take the animation and sound from.
                    targets (list): Every single fighter in the opposing party.
        """
        renpy.play(skill.SFX, channel='sound')
        for target in targets:
            if target.ALIVE:
                xTarget = target.sprite_pos[0]
                yTarget = target.sprite_pos[1]
                renpy.show(skill.GFX, [targetPos(target)], layer='battle_anims', tag=str(target))
        renpy.pause(skill.PAUSE)
        renpy.scene(layer='battle_anims')

        
