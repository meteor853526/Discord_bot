import discord
import random
import json
import sys
sys.path.append('./')
import Crawler

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
        source = Crawler.crawler()
        await ctx.send(source)

def setup(bot):
    bot.add_cog(React(bot))