from time import asctime
import discord
from discord.ext import commands
import json, asyncio, datetime
import test
import weather
# 同樣繼承bot的屬性
class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.counter = 0
        
        async def time_task():
            with open('setting.json','r',encoding = 'utf-8')as jFile:
                    jdata = json.load(jFile)
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(916496197928251445)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime("%H%M")
                week = weather.weekly(jdata['location'])
                if(now_time==jdata['time'] and self.counter == 0):
                    allowed_mentions = discord.AllowedMentions(everyone = True)
                    await self.channel.send(content = "@everyone", allowed_mentions = allowed_mentions)
                    embed=discord.Embed(title=jdata['location'], url="https://www.cwb.gov.tw/V8/C/W/week.html", description="今天天氣", color=0x5592d3)
                    embed.add_field(name= "白天", value=week[0], inline=True)                
                    embed.add_field(name= "晚上", value=week[1], inline=True)
                    await self.channel.send(embed=embed)
                    
                    print("蝦")
                    self.counter = 1
                    await asyncio.sleep(1)
                # else if :印出一次後 等到下一分鐘 記數歸零才能確保24hr後可以執行
                elif(now_time!=jdata["time"]and self.counter == 1):
                    self.counter = 0
                    print('renew success maybe')
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass
                    
        
        self.bg_task = self.bot.loop.create_task(time_task())


        

def setup(bot):
    bot.add_cog(Cog_Extension(bot))