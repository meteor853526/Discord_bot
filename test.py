import discord
import sys
sys.path.append('./')
import weather
from discord_components import *
# pip install discord-components
from discord.ext import commands
import discord
class c(commands.Cog):
    @classmethod
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

