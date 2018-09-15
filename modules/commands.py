import sqlite3
import os

statList = ['strength','dexterity','intelligence']

def ping():
    return 'Pong!'

def mkchar(plid):
    data = sqlite3.connect('database.db')
    c = data.cursor()
    # id, level, strength, dexterity, intelligence, charpts, maxhp, hp
    # CREATE TABLE players (id text, level integer, strength integer, dexterity integer, intelligence integer, charpts integer, maxhp integer, hp integer)
    c.execute('SELECT * FROM players WHERE id=?',[plid])
    if not (c.fetchone() is None):
        data.commit()
        data.close()
        return '<@{}> already has a character.'.format(plid)
    stats = (plid,0,0,0,0,1,250,250)
    c.execute('INSERT INTO players VALUES (?,?,?,?,?,?,?,?)', stats)
    data.commit()
    data.close()
    inv = sqlite3.connect(os.path.join('inv','{}.db'.format(plid)))
    c = inv.cursor()
    c.execute('CREATE TABLE inv (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT NOT NULL, type TEXT NOT NULL, maxDamage INTEGER, damageType TEXT)')
    inv.commit()
    inv.close()
    return '<@{}>\'s character has been created.'.format(plid)

def getstats(plid):
    data = sqlite3.connect('database.db')
    c = data.cursor()
    c.execute('SELECT * FROM players WHERE id=?', [plid])
    stats = c.fetchone()
    if stats is None:
        return '<@{}> doesn\'t have a character.'.format(plid)
    data.commit()
    data.close()
    stats = """```markdown
LVL         {0[1]}
STR         {0[2]}
DEX         {0[3]}
INT         {0[4]}
Stat Points {0[5]}
HP          {0[7]}/{0[6]}```""".format(stats)
    return stats

def putpoint(plid,stat,num=1):
    for i in range(0,len(statList)):
        if stat in statList[i]:
            stat = i
            break
    if isinstance(stat,str):
        return 'Wrong stat name! Must be one of:\n`{0!s}`'.format(statList)
    data = sqlite3.connect('database.db')
    c = data.cursor()
    c.execute('SELECT {}, charpts FROM players WHERE id=?'.format(statList[stat]), [plid])
    stats = list(c.fetchone())
    stats[0]+=num
    stats[1]-=num
    if stats[1] < 0:
        return 'Not enough points!'
    c.execute('''UPDATE players
    SET {} = ?, charpts = ?
WHERE id = ?'''.format(statList[stat]),(stats[0],stats[1],plid))
    data.commit()
    data.close()
    upstat = list(statList)
    for i in range(0,len(upstat)):
        upstat[i] = upstat[i][:3].upper()
    stats = """```markdown
{0}         {1[0]} (+{2})
Stat Points {1[1]} (-{2})```""".format(upstat[stat],stats,num)
    return stats

def delchar(plid):
    data = sqlite3.connect('database.db')
    c = data.cursor()
    c.execute('SELECT * FROM players WHERE id=?', [plid])
    if c.fetchone() is None:
        return '<@{}> doesn\'t have a character.'.format(plid)
    c.execute('DELETE FROM players WHERE id=?', [plid])
    data.commit()
    data.close()
    os.remove(os.path.join('inv','{}.db'.format(plid)))
    return "<@{}>'s character has been deleted.".format(plid)

#to-do?
#def showinventory(plid):
#    data = sqlite3.connect('database.db')
#    c = data.cursor()
#    c.execute('SELECT * FROM players WHERE id=?', [plid])
#    if c.fetchone is None:
#        return '<@{}> doesn\'t have a character.'.format(plid)
#    data.commit()
#    data.close()
#    inv = sqlite3.connect(os.path.join('inv', '{}.db'.format(plid)))
#    cursor = inv.cursor()
#    cursor.execute('SELECT * FROM inv')
#    if cursor.fetchone() is None:
#        return '<@{}> doesnt\'t have an items.'.format(plid)
#    else:
#        return '```Work In Progress```'
