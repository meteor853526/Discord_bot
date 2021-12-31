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
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(916496197928251445)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime("%H%M")
                with open('setting.json','r',encoding = 'utf-8')as jFile:
                    jdata = json.load(jFile)
                # week = weather.weekly(jdata["location"])
                if(now_time==jdata["time"] and self.counter == 0):
                    
                    await self.channel.send('im working!')
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