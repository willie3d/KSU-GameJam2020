init python:
    class fighter_element(object):
        """
                fighter_element is a class that handles elemental damage and stuff I can't put into words.
                It basically lets me skip all the damn if-elses at the handling stage.
                Args:
                        ELM (str): Name of the element.
                        NMOD (float): Neutral modifier for any other element.
                        ADV (fighter_element): Element this element has an advantage over.
                        ADMOD (float): Mathematical advantage this element has over the other.
                        DDV (fighter_element): Element this element is at a disadvantage again.
                        DVMOD (fighter_element): Mathematical disadvantage this element has.
                         
        """
        def __init__(self, ELM ="", NMOD = 0, ADV="", ADMOD= 0, DDV="", DVMOD=0):
            self.ELM = ELM
            self.NMOD = NMOD
            self.ADV = ADV
            self.ADMOD = ADMOD
            self.DDV = DDV
            self.DVMOD = DVMOD
        
        def beatsElement(self, target):
            """
                beatsElement evalutes whether this elements beats the target's element.
                This function is where you dictate modifiers and stuff.
                Try changing the values here if it's too OP.
                Args:
                        target (fighter): A fighter object.
            """
            fighterElement = self.ELM
            targetElement = target.ELEM.ELM
            
init python:
    """
        Declare elements first without their ADV and DDV fields.
        Declare all elements outside of labels if you want their values to be fixed to a fault.
        In this example:
                Fire beats Wind
                Wind beats Earth
                Earth beats Water
                Water beats Fire
        Another pattern would be, not sure to be honest:
                Cavalry beats Archer
                Archer beats Swordsman
                Swordsman beats Pikeman
                Pikeman beats Cavalry
    """
    FIRE = fighter_element(
        ELM = "fire",
        NMOD = 0,
        ADMOD = 2.0,
        DVMOD = -3.0
        )
    
    WIND = fighter_element(
        ELM = "wind",
        NMOD = 0,
        ADMOD = 2.0,
        DVMOD = -2.0
        )
    
    WATER = fighter_element(
        ELM = "water",
        NMOD = 0,
        ADMOD = 2.0,
        DVMOD = -3.0
        )
    
    EARTH = fighter_element(
        ELM = "earth",
        NMOD = 0,
        ADMOD = 2.0,
        DVMOD = -3.0,
        )
    
    FIRE.ADV = WATER
    WATER.ADV = FIRE
            
        
            
        
