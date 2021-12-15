import discord
from discord.ext import commands
import json
# import random
import os
from core.classes import Cog_Extension
from discord_components.client import DiscordComponents # pip install discord-components
from discord_components import DiscordComponents
with open('setting.json', mode='r',encoding='utf-8') as jFile: 
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("Bot is online")
    DiscordComponents(bot)
@bot.event
async def on_message(message):
    
    if message.content.startswith('測試'):
        await message.channel.send('\OwO/')
    await bot.process_commands(message)

# load,unload,reload實作
@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done.')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un - Loaded {extension} done.')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re _ Loaded {extension} done.')


@bot.command()
async def test(ctx):
    await ctx.send("測試@bot.command成功運作")

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(jdata['TOKEN'])

