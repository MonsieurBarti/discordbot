import discord
from discord.ext import commands
from dotenv import load_dotenv
import random
import os
import requests

load_dotenv()
token = os.getenv('BOT_TOKEN')
description = '''Monsieur Barti\'s Discord Bot'''
bot = commands.Bot(command_prefix=('$','!','`'), description=description, self_bot=True)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name="bot", description="Call the bot")
async def on_message(ctx):
    await ctx.send('What do you need {0}?'.format(ctx.author.mention))

@bot.command(name="bitcoin", description="Ask for the bitcoin market value")
async def bitcoin_value(ctx):
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await ctx.send('Bitcoin value: {0}$'.format(value))

@bot.command(pass_context=True)
async def clear(ctx, limit: int=None):
    async for msg in bot.logs_from(ctx.message.channel, limit=limit):
        await bot.delete_message (msg)
    embed = discord.Embed(description="Action completed! :smile:", color=0x00ff00)
    await bot.say (embed=embed)

bot.run(token)
