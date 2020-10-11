init python:    
    def orderBattle(allCharacters):
        """
                orderBattle returns a descending list of fighters based on one of their stats.
                By default, they are sorted by fighter.SPD.
                Args:
                        allCharacters (list): A list of all characters.
        """
        order_list = sorted(allCharacters, key=lambda fighter: fighter.SPD, reverse=True)
        return order_list

    def totalHP(faction):
        """
                totalHP returns a total value derived from the sum of a party's fighter.HP stats.
                Args:
                        faction (list): Party in which we find the total health from.
        """
        party_health = 0
        for i in faction:
            party_health +=  i.HP
        return party_health
    
    def wonBattle(frList, enList):
        """
                wonBattle is a function that returns a victor based on attrition, meaning, the party that
                dies out, meaning whose total HP becomes zero, loses. Survival of the fittest basically.
                Args:
                        frList (list): A list containing fighters that is allied with the player.
                        enList (list): A list containing fighters that is hostile to the player.
        """
        
        #integrate checking
        fHP =  totalHP(frList)
        eHP  =  totalHP(enList)
        if fHP > 0 and eHP <=0:
            #friendlies win
            return [False, 1]
        elif fHP <= 0 and eHP > 0:
            #enemies win
            return [False, 2]
        else:
            return [True, 3]
