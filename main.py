#!/usr/bin/python3

import discord
import modules.commands as com
import asyncio
import aiohttp
import platform

client = discord.Client()

dmid = '260146161975820288'

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	return await client.change_presence(game=discord.Game(name='w/ code'))

@client.event
async def on_message(message):
    if message.content == '*ping':
        await client.send_message(message.channel, com.ping())
    elif message.content.startswith('*getstats'):
        if len(message.content) == 9:
            await client.send_message(message.channel, com.getstats(message.author.id))
        elif message.author.id == dmid:
            await client.send_message(message.channel, com.getstats(shlex.split(message.content)[1]))
        else:
            await client.send_message(message.channel, 'Недостаточно прав!')
    elif message.content == '*mkchar':
        await client.send_message(message.channel, com.mkchar(message.author.id))

with open('token.txt') as f:
    token = f.read()
token = token[:-1]

client.run(token)
