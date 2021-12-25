import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
from discord_components import *
import weather
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
            keycontent,
            components=[
                Button(style=ButtonStyle.red,label = "當天天氣",custom_id="當天天氣"),  # custom_id每個button獨特的id
                Button(style=ButtonStyle.blue,label = "一周天氣",custom_id="一周天氣"), 
            ],
        )      

        while True:
            event = await self.bot.wait_for("button_click" )   #點擊button
            if event.channel == msg.channel:
                await event.respond(                      # 回傳訊息
                        content=keycontent 
                )
                
                if event.custom_id == '當天天氣' :

                    # 當天天氣
                    embed=discord.Embed(title="今天天氣", url="https://www.cwb.gov.tw/V8/C/W/week.html",color=0x4895a8)
                    embed.add_field(name=keycontent, value=weather.today(keycontent), inline=False)
                    print(weather.today(keycontent))
                    await msg.channel.send(embed=embed)
                if event.custom_id == '一周天氣':
                    # 這周天氣
                    week = weather.weekly(keycontent)
                    week = weather.weekly(keycontent)
                    week = weather.weekly(keycontent)
                    week = weather.weekly(keycontent)
                    embed=discord.Embed(title="一周天氣", url="https://www.cwb.gov.tw/V8/C/W/week.html", description=keycontent, color=0x5592d3)
                    date = []
                    for d in week.keys():
                        date.append(d)
                    print(week)
                    embed.add_field(name=str(date[0]), value=str(week[date[0]]), inline=False)
                    embed.add_field(name=date[1], value=week[date[1]], inline=False)
                    embed.add_field(name=date[2], value=week[date[2]], inline=False)
                    embed.add_field(name=date[3], value=week[date[3]], inline=False)
                    embed.add_field(name=date[4], value=week[date[4]], inline=False)
                    embed.add_field(name=date[5], value=week[date[5]], inline=False)
                    embed.add_field(name=date[6], value=week[date[6]], inline=False)
                    await msg.channel.send(embed=embed)
            
            


def setup(bot):
    bot.add_cog(Event(bot))