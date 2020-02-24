import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import os
import requests

load_dotenv()
token = os.getenv('BOT_TOKEN')
description = '''Monsieur Barti\'s Discord Bot'''
prefix = ('$','!','`')
client = commands.Bot(command_prefix=prefix, description=description)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command(name="bot", description="Call the bot")
async def on_message(ctx):
    await ctx.send('What do you need {0}?'.format(ctx.author.mention))

@client.command(name="bitcoin", description="Ask for the bitcoin market value")
async def bitcoin_value(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await ctx.send('Bitcoin value: {0}$'.format(value))

@client.command(name="clear", description="Clear a certain number of messages (!clear X)" ,pass_context=True)
async def clear(ctx, amount):
    messages = []
    async for msg in ctx.history():
        await msg.delete()
    embed = discord.Embed(description="Cleared {} messages ! :smile:".format(amount), color=0x00ff00)
    await ctx.send(embed=embed)

@client.event
async def on_member_join(member):
    role = get_role(member)
    await member.add_role(role)
    print(f"{member} was given {role}")

client.run(token)