import discord
import random
import json
import sys
sys.path.append('./')
import Crawler
import earthquake,weather
from discord_components import *
# pip install discord-components
from discord.ext import commands
from core.classes import Cog_Extension
from time import perf_counter
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
            start = perf_counter()  

            event = await self.bot.wait_for("button_click",timeout=30)   #點擊button
            if event.channel is not ctx.channel:              
                return
            else:                                            # 不同命令間的按鈕會撞
                if event.channel == ctx.channel and (event.custom_id == "雲層" or event.custom_id == "雷達" or event.custom_id == "雨量"):
                    await event.respond(                      # 回傳訊息
                        content=event.custom_id+'圖顯示成功'  # custom_id + 圖顯示成功
                    )
                    await ctx.channel.send(Crawler.crawler(event.custom_id))  # 輸出圖片
        #已修復
        
    @commands.command() 
    async def eq(self,ctx):  
        
        await ctx.channel.send(
            "圖片選項",
            components=[
                Button(style=ButtonStyle.red,label = "全球地震",custom_id="全球地震"),  # custom_id每個button獨特的id
                Button(style=ButtonStyle.blue,label = "台灣地震",custom_id="台灣地震"), 
            ],
        )      

        while True:
            event = await self.bot.wait_for("button_click",timeout=30)   #點擊button
            if event.channel == ctx.channel and (event.custom_id == "全球地震" or event.custom_id == "台灣地震"):
                await event.respond(                      # 回傳訊息
                        content="顯示成功"  # custom_id + 圖顯示成功
                )
                if event.custom_id == '全球地震' :

                    first = {}
                    first = earthquake.earth() 
                    
                    embed=discord.Embed(title="全球地震報告",color=0xea8a8a)
                    embed.set_author(name="中央氣象局資料開放平台", url="https://scweb.cwb.gov.tw/zh-tw/earthquake/world/", icon_url="https://www.kindpng.com/picc/m/178-1780574_weather-forecast-icon-png-transparent-png.png")
                    embed.add_field(name="地震台灣時間", value=first['time'], inline=False)
                    embed.add_field(name="經度", value=first['longitude'], inline=True)
                    embed.add_field(name="緯度", value=first['latitude'], inline=True)
                    embed.add_field(name="深度", value=first['depth'], inline=False)
                    embed.add_field(name="規模", value=first['scale'], inline=False)
                    embed.add_field(name="地震位置", value=first['space'], inline=False)
                    
                    await ctx.channel.send(embed=embed)
                if event.custom_id == '台灣地震':
                    
                    Alldata = {}
                    Alldata = earthquake.twearthquake()  
                    # 呼叫 earthquake 中的 twearthquake() 並回傳Alldata字典
                    
                    embed=discord.Embed(title="地震報告", url=Alldata['web'], description="報告連結",color=0x505177)
                    embed.set_author(name="中央氣象局資料開放平台", url="https://opendata.cwb.gov.tw/devManual/insrtuction", icon_url="https://www.kindpng.com/picc/m/178-1780574_weather-forecast-icon-png-transparent-png.png")
                    embed.add_field(name="發生時間", value=Alldata['time'], inline=False)
                    embed.add_field(name="震央", value=Alldata['where'], inline=False)
                    embed.add_field(name="芮氏規模", value=Alldata['level'], inline=True)
                    embed.add_field(name="深度", value=Alldata['depth'], inline=True)
                    # embed.add_field(name="最大震度"+ str(Alldata['areaLevel']) +"級地區", value=Alldata['area'], inline=False)
                    
                    embed.set_image(url=Alldata['Image'])
                    await ctx.channel.send(embed=embed)
                       
    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.mention}')

    @commands.command()
    async def set_time(self,ctx,time):
        with open('setting.json','r',encoding = 'utf-8')as jfile:
            jdata = json.load(jfile)
        jdata["time"] = time
        with open('setting.json','w',encoding = 'utf-8')as jfile:
            json.dump(jdata,jfile,indent = 4)
    # @commands.command()
    # #爬蟲 - 地震表
    # async def tweq(self,ctx):
    #     Alldata = {}
    #     Alldata = earthquake.twearthquake()  # 呼叫earthq中的twearthquake()並回傳Alldata字典
                

    @commands.command()
    #爬蟲 - 地震表
    async def tweq(self,ctx):
        Alldata = {}
        Alldata = earthquake.twearthquake()  # 呼叫earthq中的twearthquake()並回傳Alldata字典
        
        embed=discord.Embed(title="地震報告", url=Alldata['web'], description="報告連結",color=0x505177)
        embed.set_author(name="中央氣象局資料開放平台", url="https://opendata.cwb.gov.tw/devManual/insrtuction", icon_url="https://www.kindpng.com/picc/m/178-1780574_weather-forecast-icon-png-transparent-png.png")
        embed.add_field(name="發生時間", value=Alldata['time'], inline=False)
        embed.add_field(name="震央", value=Alldata['where'], inline=False)
        embed.add_field(name="芮氏規模", value=Alldata['level'], inline=True)
        embed.add_field(name="深度", value=Alldata['depth'], inline=True)
        # embed.add_field(name="最大震度"+ str(Alldata['areaLevel']) +"級地區", value=Alldata['area'], inline=False)
        
        embed.set_image(url=Alldata['Image'])
        await ctx.send(embed=embed)



    @commands.command()
    async def fcu(self,ctx):
        
        # 這周天氣
        time = {}
        time= weather.FC()
        embed=discord.Embed(title="西屯區", url="https://www.cwb.gov.tw/V8/C/W/week.html", description="西屯區", color=0x5592d3)
                        
        embed.add_field(name= time['time0'], value=time['value0'], inline=True)
        embed.add_field(name= time['time1'], value=time['value1'], inline=True)
        embed.add_field(name= time['time2'], value=time['value2'], inline=True)
        # embed.add_field(name= week['day'][3], value=week[7], inline=True)
        # embed.add_field(name= week['day'][4], value=week[9], inline=True)
        # embed.add_field(name= week['day'][5], value=week[11], inline=True)
        # embed.add_field(name= week['day'][6], value=week[13], inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(React(bot))