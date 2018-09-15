import sqlite3

possActions = {'n': 'n - do nothing', 'L': 'L - leave the dungeon'}

def plExist(plid):
    data = sqlite3.connect('database.db')
    c = data.cursor()
    c.execute('SELECT * FROM players WHERE id=?', [plid])
    if c.fetchone() is None:
        data.close()
        return False
    data.close()
    return True

def buildActions(plid, actions):
    acts = list(actions)
    for i in possActions:
        if i in actions:
            acts[actions.index(i)] = possActions[i]
    return '''<@{}>'s turn. ```markdown
{}
```'''.format(plid, '\n'.join(acts))
