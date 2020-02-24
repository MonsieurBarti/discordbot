import discord
from discord.ext import commands
import random

description = '''Monsieur Barti\'s Discord Bot'''
bot = commands.Bot(command_prefix='$', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$bot'):
        await client.send_message(message.channel, "What can I do for you?")

# @bot.command()
# async def rename(ctx, name):
#     await bot.user.edit(username=name)

bot.run('NjUzOTcyNzQ2MTQ5MDM2MDYy.XlLxkQ.tU1R-ImGpBhLUQl16itMVtCbttc')
