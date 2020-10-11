init python:
    class fighter(object):
        """
                The fighter class creates a class of fighters. I mean, this is the class that gets cloned
                when you make a fighter for your game.
                Args:
                        FTR (str): Fighter's name. Usually the character's given name.
                        ALIVE (bool): Fighter dead or alive?
                        ATK (dbl): Fighter's attack strength.
                        DEF (dbl): Fighter's defense stat.
                        SPD (dbl): Fighter's speed stat.
                        MG (dbl): Fighter's magical damage stat.
                        HP (dbl): Fighter's health/hitpoints.
                        MP (dbl): Fighter's mana/stamina.
                        ELEM (str): Fighter's elemental affinity.
                        skill_set (list): Fighter's list of skills.
                        pic_card (str): Path to fighter's portrait that will appear inside the battleUI screen.
                        pic_sprite (image): Image object representing the fighter on the battlefield.
                        sprite_pos(list): List dictating XY-coordinates of the fighter's sprites.                           
        """
        def __init__(self, FTR = "", ALIVE=True, ATK=0, DEF=0, SPD=0, MG=0, HP=0, MP=0, ELEM="", skill_set=[], pic_card="", pic_sprite="", sprite_pos=[]) :
            self.FTR = FTR
            self.ALIVE = ALIVE
            self.ATK = ATK
            self.DEF = DEF
            self.SPD = SPD
            self.MG = MG
            self.HP = HP
            self.MP = MP
            self.ELEM = ELEM
            self.skill_set = skill_set
            self.pic_card = pic_card
            self.pic_sprite  = pic_sprite 
            self.sprite_pos =  sprite_pos
        
        def registerSkill(self, skill_name):
            """
                registerSkill is a function that takes a declared skill and appends it into the fighter's
                list of skills.
                Args:
                        skill_name (fighter_skill): Predefined fighter_skill object.
            """
            self.skill_set.append(skill_name)
        
        # Hold up, does this shit even work?
        def  normalizeStats(self):
            print "Normalizing stats."
            stat_list  = [self.ATK, self.DEF, self.SPD, self.MG, self.HP, self.MP]
            for i in stat_list:
                if i <= 0:
                    i = 0
                    
        # This one's recommended.
        def normalize_stats(self):
            print "Normalizing stats."
            for index, value in enumerate(self.stat_list):
                if value <= 0:
                    self.stat_list[index] = 0
            return self.stat_list
                    
                    
                    
                    
                    
                

            
   

