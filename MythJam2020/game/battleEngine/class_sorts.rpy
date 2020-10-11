init python:   
    def listStat(party, stat):
        """
                listStat returns a list with corresponding stat values of every fighter.
                Args:
                        party (list): List containing fighters.
                        stat (str): A string corresponding to what attribute the function should list and return.
        """
        listofstat = []
        for i in party:
            if stat == "HP":
                ws = i.HP
                listofstat.append(ws)
            elif stat == "MP":
                ws =i.MP
                listofstat.append(ws)
            else:
                print "Error"
        return listofstat
    
    def findEntry(who, charList):
        """
                findEntry is a function that determines whether a fighter is in the provided party or not.
                findEntry determines is currently used exclusively to check if a fighter is an enemy, so that
                it will be handled by the corresponding code.
                Args:
                        who (fighter): A fighter of unknown affliation.
                        charList: A list of fighters to check against.                        
        """
        clLen = len(charList)
        if clLen == 0:
            return False
        else:
            for i in charList:
                matchName = who.FTR 
                if i.FTR == matchName:
                    return i
                    break
                    
                
    


