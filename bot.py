import discord
from discord.ext import commands
import json
# import random
import os
from core.classes import Cog_Extension
# from discord_components.client import DiscordComponents # pip install discord-components
# from discord_components import DiscordComponents
with open('setting.json', mode='r',encoding='utf-8') as jFile: 
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())  # discord.py　api近期更新，需要去portal開啟intent以及在此行加入intents=discord.Intents.all()

@bot.event
async def on_ready():
    print("Bot is online")
    # DiscordComponents(bot)
@bot.event
async def on_message(message):
    print(message.channel.id)
    print(message)
    print(message.content)
    print("????")
    # mentions = message.mentions
    # if len(mentions) == 0 :
    #     await message.reply("Remember to give someone to get status!")
    # else:
    #     activ = mentions[0].activity
    #     if activ == None and not message.content.startswith('None'):
    #         await message.reply("None")
    #     else:    
    #         await message.reply(activ.name)

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

