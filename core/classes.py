from time import asctime
import discord
from discord.ext import commands
from discord_components import *
import json, asyncio, datetime
import weather

with open('setting.json', mode='r',encoding='utf-8') as jFile: 
    jdata = json.load(jFile)

# 同樣繼承bot的屬性
class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.counter = 0
        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(jdata['weather'])
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime("%H%M")
                city = jdata['location']
                if(now_time==jdata["time"] and self.counter == 0):
                    print('im in this it success')
                    # week = {}
                    # week = weather.weekly(city)
                    # embed=discord.Embed(title="未來一周天氣(白天)", url="https://www.cwb.gov.tw/V8/C/W/week.html", description=city, color=0x5592d3)
                    
                    # embed.add_field(name= week['day'][0], value=week[1], inline=True)
                    await self.channel.send('im working')
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

# @commands.command()
# async def set_channel(self,ctx,ch:int):
#     self.channel = self.bot.get_channel(ch)
#     await ctx.send(f'Set Channel: {self.channel.mention}')

# @commands.command()
# async def set_time(self,ctx,time):
#     with open('setting.json','r',encoding = 'utf-8')as jfile:
#         jdata = json.load(file)
#     jdata["time"] = time
#     with open('setting.json','w',encoding = 'utf-8')as jfile:
#         json.dump(jdata,jfile,indent = 4)
        

def setup(bot):
    bot.add_cog(Cog_Extension(bot))