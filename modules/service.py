import sqlite3

def checkchar(plid): # to check the presence of the character in the bot code
    data = sqlite3.connect('database.db')
    с = data.cursor()
    if c.fetchone() is None:
        return False
    data.commit()
    data.close()
    return True