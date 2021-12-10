import discord
from discord.ext import commands
import json
import random
with open('setting.json', mode='r',encoding='utf-8') as jFile: 
    jdata = json.load(jFile)

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("Bot is online")
    

@bot.event
async def on_message(message):
    
    if message.content.startswith('測試'):
        await message.channel.send('\OwO/')
    await bot.process_commands(message)


@bot.command()
async def test(ctx):
    await ctx.send("測試@bot.command成功運作")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000,2)} (ms)')

@bot.command()
# 本機圖片庫
async def weather(ctx):
    pic = discord.File(jdata['pic'])
    await ctx.send(file=pic)

@bot.command()
async def web(ctx):
    pic = random.choice(jdata['url_pic'])
    await ctx.send(pic)

bot.run('OTE4NTI1NjU2MDEzMzQwNjcy.YbIhrQ.lI0du9unnlG9Yz9Kvp3nW7UyT18')

