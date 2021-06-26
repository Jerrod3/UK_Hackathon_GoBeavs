import discord
import requests
import json
import os
from secrets import *
from commands import *

client = discord.Client()
TOKEN = get_token()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('$Next'):
        # placeholder of 10 years
        await message.channel.send(next(10))

    if message.content.startswith('$Start'):
        await message.channel.send(start())

    if message.content.startswith('$Initialize'):
        await message.channel.send(initialize())

client.run(TOKEN)
