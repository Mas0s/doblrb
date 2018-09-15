import sqlite3

def plExist(plid):
    data = sqlite3.connect('database.db')
    c = data.cursor()
    c.execute('SELECT * FROM players WHERE id=?', [plid])
    if c.fetchone() is None:
        data.close()
        return False
    data.close()
    return True
