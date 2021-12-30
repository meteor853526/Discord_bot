import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
from discord_components import *
import weather
import astron
from bs4 import BeautifulSoup
from selenium import webdriver

with open('setting.json', mode='r',encoding='utf-8') as jFile: 
    jdata = json.load(jFile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword = ['基隆市','臺北市','新北市','桃園縣','新竹市','新竹縣',
        '苗栗縣','臺中市','彰化縣','南投縣','雲林縣','嘉義市','嘉義縣','臺南市',
        '高雄市','屏東縣','臺東縣','花蓮縣','宜蘭縣','澎湖縣','金門縣','連江縣']
        keycontent = msg.content
        if (msg.content in keyword) and (msg.author != self.bot.user):
            await msg.channel.send(
                "圖片選項",
                components=[
                    Button(style=ButtonStyle.green,label = "日出日落",custom_id="日出日落"), 
                    Button(style=ButtonStyle.blue,label = "月出月落",custom_id="月出月落"), 
                ],
            )
            while True:
                event = await self.bot.wait_for("button_click")   #點擊button
                if event.channel == msg.channel and (event.custom_id == "日出日落" or event.custom_id == "月出月落"):
                    await event.respond(                      # 回傳訊息
                            content="顯示成功"  # custom_id + 圖顯示成功
                    )
                    if event.custom_id == '日出日落' :
                        where = msg.content
                        get = {}
                        get = astron.astron_sun(where)

                        embed=discord.Embed(title="天文報告-"+str(where),color=0xea8a8a)
                        embed.set_author(name="中央氣象局資料開放平台", url="https://scweb.cwb.gov.tw/zh-tw/earthquake/world/", icon_url="https://www.kindpng.com/picc/m/178-1780574_weather-forecast-icon-png-transparent-png.png")
                        embed.add_field(name="日出時刻", value=get['sun_out'], inline=True)
                        embed.add_field(name="日沒時刻", value=get['sun_in'], inline=True)
                        embed.add_field(name="太陽仰角", value=get['angle'], inline=False)
                        embed.add_field(name="太陽過中天", value=get['cross_middle'], inline=True)
                        
                        await msg.channel.send(embed=embed)
                    if event.custom_id == '月出月落' :
                        where = msg.content
                        get = {}
                        get = astron.astron_moon(where)

                        embed=discord.Embed(title="天文報告-"+str(where),color=0xea8a8a)
                        embed.set_author(name="中央氣象局資料開放平台", url="https://scweb.cwb.gov.tw/zh-tw/earthquake/world/", icon_url="https://www.kindpng.com/picc/m/178-1780574_weather-forecast-icon-png-transparent-png.png")
                        embed.add_field(name="月出時刻", value=get['moon_out'], inline=True)
                        embed.add_field(name="月沒時刻", value=get['moon_in'], inline=True)
                        embed.add_field(name="月亮仰角", value=get['moon_angle'], inline=False)
                        embed.add_field(name="月亮過中天", value=get['moon_cross_middle'], inline=True)
                        embed.set_image(url=astron.img_get_moon())
                        await msg.channel.send(embed=embed)




    # @commands.Cog.listener()
    # async def on_message(self,msg):
    #     keyword = ['基隆市','臺北市','新北市','桃園縣','新竹市','新竹縣',
    #     '苗栗縣','臺中市','彰化縣','南投縣','雲林縣','嘉義市','嘉義縣','臺南市',
    #     '高雄市','屏東縣','臺東縣','花蓮縣','宜蘭縣','澎湖縣','金門縣','連江縣']
    #     keycontent = msg.content
    #     if (msg.content in keyword) and (msg.author != self.bot.user):
    #         await msg.channel.send(
    #             keycontent,
    #             components=[
    #                 Button(style=ButtonStyle.red,label = "當天天氣",custom_id="當天天氣"),  # custom_id每個button獨特的id
    #                 Button(style=ButtonStyle.blue,label = "一周天氣",custom_id="一周天氣"), 
    #             ],
    #         )  
    #         while True:
    #             event = await self.bot.wait_for("button_click",timeout=100)   #點擊button
    #             if event.channel == msg.channel and (event.custom_id == '當天天氣' or event.custom_id == '一周天氣'):
    #                 await event.respond(                      # 回傳訊息
    #                         content=keycontent 
    #                 )
                    
    #                 if event.custom_id == '當天天氣' :

    #                     # 當天天氣
    #                     embed=discord.Embed(title="今天天氣", url="https://www.cwb.gov.tw/V8/C/W/week.html",color=0x4895a8)
    #                     embed.add_field(name=keycontent, value=weather.today(keycontent), inline=False)
    #                     print(weather.today(keycontent))
    #                     await msg.channel.send(embed=embed)
    #                 if event.custom_id == '一周天氣':
    #                     # 這周天氣
    #                     week = weather.weekly(keycontent)
    #                     week = weather.weekly(keycontent)
    #                     week = weather.weekly(keycontent)
    #                     week = weather.weekly(keycontent)
    #                     embed=discord.Embed(title="一周天氣", url="https://www.cwb.gov.tw/V8/C/W/week.html", description=keycontent, color=0x5592d3)
    #                     date = []
    #                     for d in week.keys():
    #                         date.append(d)
    #                     print(week)
    #                     embed.add_field(name=str(date[0]), value=str(week[date[0]]), inline=False)
    #                     embed.add_field(name=date[1], value=week[date[1]], inline=False)
    #                     embed.add_field(name=date[2], value=week[date[2]], inline=False)
    #                     embed.add_field(name=date[3], value=week[date[3]], inline=False)
    #                     embed.add_field(name=date[4], value=week[date[4]], inline=False)
    #                     embed.add_field(name=date[5], value=week[date[5]], inline=False)
    #                     embed.add_field(name=date[6], value=week[date[6]], inline=False)
    #                     await msg.channel.send(embed=embed)
                    

        
            


def setup(bot):
    bot.add_cog(Event(bot))