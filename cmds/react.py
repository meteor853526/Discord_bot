import discord
import random
import json
import sys
sys.path.append('./')
import Crawler
import earthq
from discord_components import *
# pip install discord-components
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json', mode='r',encoding='utf-8') as jFile: 
    jdata = json.load(jFile)


class React(Cog_Extension):
    @commands.command()
    # 本機圖片庫
    async def weather(self,ctx):
        pic = discord.File(jdata['pic'])
        await ctx.send(file=pic)

    @commands.command()
    #網頁瀏覽器圖片
    async def web(self,ctx):
        pic = random.choice(jdata['url_pic'])
        await ctx.send(pic)

    @commands.command()
    #爬蟲 - 氣象圖片
    async def craw(self,ctx):
        await ctx.channel.send(
            "圖片選項",
            components=[
                Button(style=ButtonStyle.blue,label = "雷達"),
                Button(style=ButtonStyle.red,label = "雨量"),
            ],
        )
        res = await self.bot.wait_for("button_click")
        if res.channel == ctx.channel:
            await res.respond(
                content='雷達圖顯示成功'
            )
            await ctx.channel.send(Crawler.crawler(2))

        
        res2 = await self.bot.wait_for("button_click")
        if res2.channel == ctx.channel:
            await res2.respond(
                content='雨量圖顯示成功'
            )
            await ctx.channel.send(Crawler.crawler(3))

    @commands.command()
    #爬蟲 - 地震表
    async def earthq(self,ctx):
        await ctx.send(earthq.earth())

def setup(bot):
    bot.add_cog(React(bot))