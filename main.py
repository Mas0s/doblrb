#!/usr/bin/python3

import discord
import modules.commands as com
import asyncio
from shlex import split as shplit
from platform import python_version

client = discord.Client()

dmid = '260146161975820288'

man = {
    'ping': 'Syntax: `*ping`',
    'getstats': 'Syntax: `*getstats`',
    'mkchar': 'Syntax: `*mkchar`',
    'man': 'Syntax: `*man <command>`',
    'putpoint': 'Syntax: `*putpoint <stat> [number]`'
}

@client.event
async def on_ready():
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
            if message.author.id == dmid:
                await client.send_message(message.channel, com.getstats(shplit(message.content)[1]))
            else:
                await client.send_message(message.channel, 'Недостаточно прав!')
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
    # TODO: man command
with open('token.txt') as f:
    token = f.read()
token = token[:-1]

client.run(token)
