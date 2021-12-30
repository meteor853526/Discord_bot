import discord
from discord.ext import commands
import json, asyncio, datetime
# 同樣繼承bot的屬性
class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

        async def time_task():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(916496197928251445)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime("%H%M")
                with open('setting.json','r',encoding = 'utf-8')as jFile:
                    jdata = json.load(jFile)
                if(now_time==jdata["time"]):
                    await self.channel.send('Task Working')
                    await asyncio.sleep(60)
                else:
                    await asyncio.sleep(60)
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