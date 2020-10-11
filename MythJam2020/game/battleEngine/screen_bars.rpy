screen stat_bars(party, hp_stats, mp_stats):
    $ x = 0
    for i in allies + enemies:
        if i.ALIVE:
            python:
                chp = i.HP
                cmp = i.MP
                mhp = int(hp_stats[x])
                mmp = int(mp_stats[x])
            vbox at barsPos(i):
                bar value chp range  mhp  style "sheepstorm_hp_bar" 
                bar value cmp range mmp style "sheepstorm_mp_bar"
        $ x += 1 


