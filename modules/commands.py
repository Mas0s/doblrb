import sqlite3

#class plr():
#    def __init__(self):
#        self.level = 0
#        self.strength = 0
#        self.dexterity = 0
#        self.intelligence = 0
#        self.charpts = 1
#        self.maxhp = 250
#        self.hp = self.maxhp

def ping():
    return 'Pong!'

def mkchar(plid):
    data = sqlite3.connect('database.db')
    c = data.cursor()
    # id, level, str, dex, int, charpts, maxhp, hp
    stats = (plid,0,0,0,0,1,250,250)
    c.execute('INSERT INTO players VALUES (?,?,?,?,?,?,?,?)', stats)
    return 'Персонаж <@{}> создан.'.format(plid)
