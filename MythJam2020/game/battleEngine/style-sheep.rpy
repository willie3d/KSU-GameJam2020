init -10 python:
    
    ## default block
    style.sheepstorm = Style(style.default)
    style.sheepstorm_window.background = Frame("sf_250-25.png", 30, 30)
    style.sheepstorm_frame.background = Frame("sf_250-25.png", 30, 30)
    ## battleUI
    style.sheepstorm_battle_frame.background = Frame("sf_250-25.png", 30, 30)
    style.sheepstorm_battle_frame.xalign = 0.5
    style.sheepstorm_battle_frame.yalign = 1.0
    style.sheepstorm_battle_frame.xsize = 780
    style.sheepstorm_battle_frame.ysize = 180
    style.sheepstorm_battle_frame.xpadding = 25
    style.sheepstorm_battle_frame.ypadding = 25
    ## bars
    style.sheepstorm_hp_bar.left_bar = "hp.png"
    style.sheepstorm_hp_bar.right_bar  = "empty.png"
    style.sheepstorm_hp_bar.xsize = 70
    style.sheepstorm_hp_bar.ysize = 15
    style.sheepstorm_hp_bar.left_gutter = 0
    style.sheepstorm_hp_bar.right_gutter = 0
    style.sheepstorm_hp_bar.thumb = None
    style.sheepstorm_hp_bar.thumb_shadow = None
    style.sheepstorm_hp_bar.thumb_offset = 0
    ### HA? ###
    style.sheepstorm_mp_bar.left_bar = "mp.png"
    style.sheepstorm_mp_bar.right_bar  = "empty.png"
    style.sheepstorm_mp_bar.xsize = 70
    style.sheepstorm_mp_bar.ysize = 15
    style.sheepstorm_mp_bar.left_gutter = 0
    style.sheepstorm_mp_bar.right_gutter = 0
    style.sheepstorm_mp_bar.thumb= None
    style.sheepstorm_mp_bar.thumb_shadow = None
    style.sheepstorm_mp_bar.thumb_offset = 0
