init python:
    action_desc = ""
    selected_skill = ""
    skill_desc = ""
    selected_target  = ""
        
screen turn_counter(turnNum): 
    #    turn_counter is used to display the current term. It is called exclusively inside executeBattle.
    #    Args:
    #            turnNum (int): A variable the contains the total count of loops the battle has gone 
    #            through.
    frame:
        background style.window.background 
        text "Turn: " + str(turnNum)
    
screen battleUI(turn_num, currentFighter, enemies, allies, useage):
    #   battleUI displays current fighter data, list of actions, list of targets, and list of skills.
    #   battleUI takes its style from an external style sheet.
    #   Args:
    #           turn_num (int): Current total turn count.
    #           currentFighter (fighter): Current fighter object in orderInitiators list.
    #           enemis (list): List of fighters hostile to player and friends.
    #           allies (list): List of friendly fighters.
    #           useage(string): What phase of the current term is the interface being used.
    style_group "sheepstorm"
    frame:
        style_group "sheepstorm_battle"
        has hbox spacing 20
        vbox:
            add currentFighter.pic_card size(80, 80)
            text currentFighter.FTR
        vbox:
            text "HP: " + str(int(currentFighter.HP))
            text "MP: " + str(int(currentFighter.MP))
            text "ATK: " + str(int(currentFighter.ATK))
            text "DEF: " + str(int(currentFighter.DEF))      
        if useage == "target":
            use selectTarget(enemies)
        elif useage == "skill":
           use selectSkill(currentFighter)
        elif useage == "action":
            use selectAction(currentFighter)
        else:
            $ print "Unable to load proper frame."
           

screen selectAction(currentFighter):
    #   selectAction is a screen that is part of battleUI under the useage "action".
    #   selectAction inherents its style from battleUI.
    #   Args:
    #           currentFigher (fighter): Current fighter object in orderInitiators list.
    vbox:
        textbutton "Engage":
            xsize 160
            hovered SetVariable("action_desc", "Engage opponents with abilities .")
            unhovered SetVariable("action_desc", "What should [currentFighter.FTR] do?")
            action Return("engaging")
    
        textbutton "Defend":
            xsize 160
            hovered  SetVariable("action_desc", "Sit this turn out and recover mana.  Also increases defense."), 
            unhovered SetVariable("action_desc", "What should [currentFighter.FTR] do?")
            #renpy.curried_invoke_in_new_context(increaseDef, currentFighter),
            action Return("defending")
    vbox:
        text action_desc 
 
screen selectSkill(currentFighter):
    #   selectSkill is screen that is included under battleUI under the useage "skill".
    #   selectSkill inherits its style from battleUI.
    #   Args:
    #           currentFigher (fighter): Current fighter object in orderInitiators list.
    vbox:
        textbutton "Attack":
            xsize 160
            hovered SetVariable("skill_desc", "Generic melee attack.")
            unhovered  SetVariable("skill_desc", "Select a skill.")
            action [SetVariable("selected_skill", GenericAttack), 
                    Return(GenericAttack)]
        for i in currentFighter.skill_set:
            if currentFighter.MP >= i.COST:
                textbutton i.SKL:
                    xsize 160
                    hovered  [SetVariable("selected_skill", i), SetVariable("skill_desc", i.DESC)]
                    unhovered  SetVariable("skill_desc", "Select a skill.")
                    action [SetVariable("selected_skill", i),
                        Return(i)] 
            else:
                textbutton i.SKL:
                    xsize 160
                    hovered  [SetVariable("selected_skill", i), SetVariable("skill_desc", i.DESC)]
                    unhovered  SetVariable("skill_desc", "Select a skill.")
                    action NullAction() 
    vbox:
        $ x = selected_skill
        if x== "":
            text skill_desc 
        else:
            text x.SKL
            text "Damage: " + str( x.DMG)
            text "Cost: " + str(x.COST)
            text x.DESC
            
screen selectTarget(enemies):
    #   selectTarget is the last screen included in battleUI. It only appears under the useage "targets".
    #   selectTarget also inherits its style from battleUI.
    #   Args:
    #           enemies (list): List of fighters from the opposing party.
    vbox:
        for i in enemies:
            if i.ALIVE:
                textbutton i.FTR:
                    hovered [SetVariable("selected_target", i)]
                    action [SetVariable("selected_target", i), Return(i)]xsize 170
    vbox spacing 0:
        $ x = selected_target
        if selected_target<>"":
            text x.FTR
            hbox spacing 10:
                text "Health: " + str(int(x.HP))
                text "Mana: " + str(int(x.MP))
            hbox spacing 10:
                text "Attack: " + str(int(x.ATK))
                text "Defense: " + str(int(x.DEF))

                    

