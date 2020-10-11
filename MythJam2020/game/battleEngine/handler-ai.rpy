init python:
    import random
    def aiTargetSelection(target_list):
        """
            aiTargetSlection returns a target from a list of targets.
            Args:
                target_list (list): A list containing fighters from the opposing party.
        """ 
        target = random.choice(target_list)
        while not target.ALIVE:
            target = random.choice(target_list)
        return target
     
    def aiSkillSelection(initiator):
        """
            aiSkillSelection returns a skill that is to be executed by an AI fighter.
            Args:
                initiator (fighter): The fighter who will use choose a skill.
        """
        initiator.normalize_stats
        skill_set = initiator.skill_set
        skill_set.append(GenericAttack)
        skill = random.choice(skill_set)
        while skill.COST >= initiator.MP:
            skill =  random.choice(skill_set)
        return skill
