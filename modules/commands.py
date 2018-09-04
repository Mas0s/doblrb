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
    c.execute('SELECT * FROM players WHERE id=?',[plid])
    if not (c.fetchone() is None):
        data.commit()
        data.close()
        return 'У игрока <@{}> уже есть персонаж.'.format(plid)
    stats = (plid,0,0,0,0,1,250,250)
    c.execute('INSERT INTO players VALUES (?,?,?,?,?,?,?,?)', stats)
    data.commit()
    data.close()
    return 'Персонаж игрока <@{}> создан.'.format(plid)

def getstats(plid):
    data = sqlite3.connect('database.db')
    c = data.cursor()
    c.execute('SELECT * FROM players WHERE id=?', [plid])
    stats = c.fetchone()
    data.commit()
    data.close()
    stats = """```markdown
LVL         {}
STR         {}
DEX         {}
INT         {}
Stat Points {}
HP          {}/{}```""".format(stats[1],stats[2],stats[3],stats[4],stats[5],stats[7],stats[6])
    return stats
