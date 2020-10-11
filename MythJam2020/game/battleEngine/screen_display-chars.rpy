#       Deprecated under version 0.7.
screen showAll(allchars):
    $ displayOrder = zorderSprites(orderInitiators)
    for i in displayOrder:         
        if i.ALIVE:
            add i.pic_sprite:
                xanchor 0.5 yanchor 0.5
                xpos i.sprite_pos[0]
                ypos i.sprite_pos[1]
        else:
            add im.Grayscale(i.pic_sprite):
                xanchor 0.5 yanchor 0.5
                xpos i.sprite_pos[0]
                ypos i.sprite_pos[1] 


