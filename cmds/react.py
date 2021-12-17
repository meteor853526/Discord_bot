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
                Button(style=ButtonStyle.green,label = "雲層",custom_id="雲層"),  # custom_id每個button獨特的id
                Button(style=ButtonStyle.blue,label = "雷達",custom_id="雷達"),     
                Button(style=ButtonStyle.red,label = "雨量",custom_id="雨量"),
            ],
        )

        while True:
            event = await self.bot.wait_for("button_click")   #點擊button
            if event.channel is not ctx.channel:              
                return
            else:
                if event.channel == ctx.channel:
                    await event.respond(                      # 回傳訊息
                        content=event.custom_id+'圖顯示成功'  # custom_id + 圖顯示成功
                    )
                    await ctx.channel.send(Crawler.crawler(event.custom_id))  # 輸出圖片
        #已修復
    @commands.command()
    #爬蟲 - 地震表
    async def tweq(self,ctx):
        Alldata = {}
        Alldata = earthq.twearthquake()  # 呼叫earthq中的twearthquake()並回傳Alldata字典
        
        embed=discord.Embed(title="地震報告", url=Alldata['web'], description="報告連結",color=0x505177)
        embed.set_author(name="中央氣象局資料開放平台", url="https://opendata.cwb.gov.tw/devManual/insrtuction", icon_url="https://www.kindpng.com/picc/m/178-1780574_weather-forecast-icon-png-transparent-png.png")
        embed.add_field(name="發生時間", value=Alldata['time'], inline=False)
        embed.add_field(name="震央", value=Alldata['where'], inline=False)
        embed.add_field(name="芮氏規模", value=Alldata['level'], inline=True)
        embed.add_field(name="深度", value=Alldata['depth'], inline=True)
        embed.add_field(name="最大震度"+ str(Alldata['areaLevel']) +"級地區", value=Alldata['area'], inline=False)
        
        embed.set_image(url=Alldata['Image'])
        await ctx.send(embed=embed)
        
   
def setup(bot):
    bot.add_cog(React(bot))