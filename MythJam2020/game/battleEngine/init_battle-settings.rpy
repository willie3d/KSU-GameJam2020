init python:
     class battle_settings:
         """
                battle_settings will dictate overall handling in executeBattle.
                I don't know why I made this lol.
                *Implemented as of 6.18.2016.
                Args:
                        with_audio (bool): True if your battle has sfx.
                        with_effects (bool): True if your battle has gfx.
                        *with_bars (bool): True if you want to display bars.
                        fighter_layout (str): Normal or mobage layouts.
                        *dialogue_pause (dbl): How long before interaction continues..
         """
         def __init__(self, with_audio, with_effects, with_bars, fighter_layout, dialogue_pause ):
             self.with_audio = with_audio 
             self.with_effects = with_effects
             self.with_bars = with_bars
             self.fighter_layout = fighter_layout
             self.dialogue_pause = dialogue_pause
             
init:
    #   Default settings.            
    $ normal_settings = battle_settings(
        with_audio = True,
        with_effects = True,
        with_bars = True,
        fighter_layout =  "normal",
        dialogue_pause = 2.0
    )
         
