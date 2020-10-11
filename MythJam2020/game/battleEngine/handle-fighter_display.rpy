init python:
    def zorderSprites(allCharacters):
        """
                zorderSprites returns a list of character arranged based on the z axis.
                This basically decides who is displayed first to last.
                Args:
                        allCharacters (list): A list of all characters.
        """
        order_list = sorted(allCharacters, key=lambda fighter: fighter.sprite_pos[1], reverse=False)
        return order_list
    
    def displayFighters(orderInitiators):
        """
                displayFighters is the actual function that does the displaying of characters.
                Args:
                        orderInitiators (list): A sorted list of fighters.
        """
        displayOrder = zorderSprites(orderInitiators)
        for i in displayOrder:
            # Pic_sprite as image, target in target pos is yourself, tag is variable name?
            fightTag = i.FTR
            fightTag = fightTag.replace(" ", "_")
            renpy.show(i.pic_sprite, at_list=[targetPos(i)], layer='battle_sprites', tag=str(fightTag))
            
    def hideFighters(orderInitiators):
        """
                hideFighters checks if a fighter is not alive, if so, it hides the respective fighter's sprite.                
               Args:
                        orderInitiators (list): A sorted list of fighters.     
        """
        displayOrder = zorderSprites(orderInitiators)
        for i in displayOrder:
            if not i.ALIVE:
                renpy.hide(str(i), layer=None)
        
    def hideFighter(target):
        """
                hideFighter is for single targets. Possibly useful for hide skills if ever implemented.
                This function shouldn't be used right now lol.
                Args:
                        target (fighter): A fighter that's probably dead or something?
        """
        targetTag = target.FTR
        targetTag = targetTag.replace(" ", "_")
        renpy.hide(targetTag, layer='battle_sprites')
        
init:
    # The following functions are dynamic.
    # targetPos is used during displaying fighters into the battlefield.
    # barsPos is used during displaying bars above the players or something.
    transform targetPos(i):     # Accepts a fighter object and extracts coordinates as a transform.
        xanchor 0.5 yanchor 0.5
        xpos  i.sprite_pos[0]
        ypos  i.sprite_pos[1]
        
    transform barsPos(i):       # Same as above, dictates where the bars appear per fighter.
        xanchor 0.5 #yanchor 0.5
        xpos float(i.sprite_pos[0])
        ypos  float(i.sprite_pos[1]) - 0.08  #0.1 or -0.1
        


