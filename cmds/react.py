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
                Button(style=ButtonStyle.green,label = "雲圖"),
                Button(style=ButtonStyle.blue,label = "雷達"),
                Button(style=ButtonStyle.red,label = "雨量"),
            ],
        )
        res1 = await self.bot.wait_for("button_click")
        if res1.channel == ctx.channel:
            await res1.respond(
                content='雲圖顯示成功'
            )
            await ctx.channel.send(Crawler.crawler(1))


        res2 = await self.bot.wait_for("button_click")
        if res2.channel == ctx.channel:
            await res2.respond(
                content='雷達圖顯示成功'
            )
            await ctx.channel.send(Crawler.crawler(2))

        
        res3 = await self.bot.wait_for("button_click")
        if res3.channel == ctx.channel:
            await res3.respond(
                content='雨量圖顯示成功'
            )
            await ctx.channel.send(Crawler.crawler(3))

        

    @commands.command()
    #爬蟲 - 地震表
    async def tweq(self,ctx):
        embed=discord.Embed(title="地震報告", url="https://opendata.cwb.gov.tw/dist/opendata-swagger.html", description="報告連結")
        
        embed.set_author(name="中央氣象局資料開放平台")
        embed.add_field(name="發生時間", value="undefined", inline=False)
        embed.add_field(name="震央", value="undefined", inline=False)
        embed.add_field(name="芮氏規模", value="undefined", inline=True)
        embed.add_field(name="深度", value="undefined", inline=True)
        embed.add_field(name="最大震度3級地區", value="undefined", inline=False)
        embed.add_field(name="最大震度2級地區", value="undefined", inline=False)
        embed.add_field(name="最大震度1級地區", value="undefined", inline=False)
        await ctx.send(embed=embed)
        await ctx.send(earthq.twearthquake())
   
def setup(bot):
    bot.add_cog(React(bot))