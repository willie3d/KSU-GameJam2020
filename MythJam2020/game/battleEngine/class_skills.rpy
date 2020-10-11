init python:
    class fighter_skill(object):
        """
            fighter_skill is a class that contains attributes necessary in affecting fighters.
            TL;DR, this is the class for your fighter's skills.
            Args:
                SKL (str): Name of the skill. This is the one displayed in the selectSkill screen.
                DMG (dbl): Base damage of your skill.
                COST (int): How much MP will it cost your fighter to use this skill.
                ELEM (string): Element associated with this skill. Adds bonuses later on.
                DESC (str): Short description/flavor text.
                AOE (bool): If this is an area of effect skill or not.
                GFX (str): Name of gfx animation as string.
                SFX (str): Filepath to sfx as string.
                PAUSE (dbl): Amount of seconds needed to finish skill animation.               
        """
        def __init__(self, SKL = "", DMG="", COST="", ELEM="", DESC="", AOE=False, GFX="", SFX="", PAUSE = "") :
            self.SKL = SKL            
            self.DMG = DMG      
            self.COST = COST          
            self.ELEM = ELEM            
            self.DESC = DESC           
            self.AOE = AOE                  
            self.GFX = GFX              
            self.SFX = SFX                    
            self.PAUSE = PAUSE  
            
            
            
