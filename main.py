#!/usr/bin/python3

import discord
import modules.commands as com
import modules.extralib as ext
import asyncio
from shlex import split as shplit
from platform import python_version
import os
import sys

client = discord.Client()

dmid = '260146161975820288' #replace this into your discord id

man = {
	'ping': 'Syntax: `*ping`',
	'getstats': 'Syntax: `*getstats`',
	'mkchar': 'Syntax: `*mkchar`',
	'man': 'Syntax: `*man <command>`',
	'putpoint': 'Syntax: `*putpoint <stat> [number]`',
	'delchar': 'Syntax: `*delchar`'
}

@client.event
async def on_ready():
	if os.path.isfile('.doblrest'):
		with open('.doblrest','r') as tmp:
			chan = tmp.read()
		os.remove('.doblrest')
		await client.send_message(discord.Object(chan),'Restart successul.')
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	await client.change_presence(game=discord.Game(name='w/ code'))

@client.event
async def on_message(message):

    if message.content.startswith('*ping'):
        if len(shplit(message.content)) == 1:
            await client.send_message(message.channel, com.ping())
        else:
            await client.send_message(message.channel, man['ping'])

	elif message.content.startswith('*getstats'):
        if len(shplit(message.content)) == 1:
            await client.send_message(message.channel, com.getstats(message.author.id))
        elif len(shplit(message.content)) == 2:
            if message.author.id == dmid or "Dungeon Keeper" in [y.name.lower() for y in message.author.roles]:
                await client.send_message(message.channel, com.getstats(shplit(message.content)[1]))
            else:
                await client.send_message(message.channel, 'Access denied!')
        else:
            await client.send_message(message.channel, man['getstats'])

	elif message.content.startswith('*mkchar'):
        if len(shplit(message.content)) == 1:
            await client.send_message(message.channel, com.mkchar(message.author.id))
        else:
            await client.send_message(message.channel, man['mkchar'])

	elif message.content.startswith('*putpoint'):
        if len(shplit(message.content)) == 2:
            await client.send_message(message.channel, com.putpoint(message.author.id, shplit(message.content)[1]))
        elif len(shplit(message.content)) == 3:
            await client.send_message(message.channel, com.putpoint(message.author.id, shplit(message.content)[1], int(shplit(message.content)[2])))
        else:
            await client.send_message(message.channel, man['putpoint'])

	elif message.content.startswith('*delchar'):
        if len(shplit(message.content)) == 1:
			ext.plExist()
			if True:
				await client.send_message(message.channel, 'Are you sure that you wanna delete the character? (Yes/No)')
				response = client.wait_for_message(author = message.author, timeout = 15)
				if response.clear_content.lower() == 'yes':
					await client.send_message(message.channel, com.delchar(message.author.id))
				elif response.clear_content.lower() == 'no':
					await client.send_message(message.channel, 'Action canceled.')
				elif response is None:
					await client.send_message(message.channel, 'Action timeout.')
				else:
					await client.send_message(message.channel, 'Wrong chosen actions.')
        elif len(shplit(message.content)) == 2:
            if message.author.id == dmid or "Dungeon Keeper" in [y.name.lower() for y in message.author.roles]:
				await client.send_message(message.channel, com.delchar(message.author.id))
			else:
				await client.send_message(message.channel, 'Access denied!')
        else:
            await client.send_message(message.channel, man['delchar'])

	elif message.content.startswith('*man'):
        if len(shplit(message.content)) == 1:
            await client.send_message(message.channel, "Commands: ```\n*{}```".format('\n*'.join(man)))
        elif len(shplit(message.content)) == 2:
            await client.send_message(message.channel, man[shplit(message.content)[1]])
        else:
            await client.send_message(message.channel, man['man'])

	elif message.content.startswith('*restart'):
        if len(shplit(message.content)) == 1:
            if message.author.id == dmid:
                with open('.doblrest','w') as tmp:
                    tmp.write(message.channel.id)
                os.execv(__file__, sys.argv)
            else:
                await client.send_message(message.channel, 'Access denied!')

	elif message.content.startswith('*shutdown'):
        if len(shplit(message.content)) == 1:
            if message.author.id == dmid:
                await client.send_message(message.channel, 'Shutting down...')
                raise SystemExit
            else:
                await client.send_message(message.channel, 'Access denied!')

with open('token.txt') as f:
	token = f.read()
token = token[:-1]

client.run(token)
