# DoBL:RB
Dungeon of Bad Luck: Rebirth ~~is~~ will be a text multiplayer turn-based game running through a Discord bot.

## Dependencies
1. Python 3
2. discord.py

## Installation
1. Install the dependencies
2. Clone the repository
3. Make a `database.db` file, open it in sqlite3 and create the players table there with the following parameters:
```CREATE TABLE players (
	id             text NOT NULL UNIQUE,
	level          integer,
	strength       integer,
	dexterity      integer,
	intelligence   integer,
	charpts	       integer,
	maxhp          integer,
	hp             integer,
	PRIMARY KEY(id)
)
```
4. Make a `token.txt` and put your bot's token there
5. Launch main.py
