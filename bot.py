import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print("Bot is online")
    

@bot.event
async def on_message(message):
    

    if message.content.startswith('測試'):
        await message.channel.send('\OwO/')
   

bot.run('OTE3MDUxMjQ1NzIwNjU3OTMy.YazEhg.n5DXSkFRhwJr2xaCsydvsxRRU6o')

