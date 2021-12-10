import discord
from discord.ext import commands
from core.classes import Cog_Extension


class Main(Cog_Extension):
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000,2)} (ms)')

    @commands.command()
    async def hi(self,ctx):
        await ctx.send('ABCD')

    @commands.command()
    async def em(self,ctx):
        embed=discord.Embed(title="天氣預報", description="關於今天", color=0x47e1ba)
        embed.set_author(name="中央氣象局", url="https://www.cwb.gov.tw/V8/C/W/week.html")
        embed.add_field(name="早上", value="18 - 27", inline=True)
        embed.add_field(name="晚上", value="15 - 19", inline=True)
        embed.set_footer(text="footer name")
        await ctx.send(embed=embed)

# 註冊code
def setup(bot):
    bot.add_cog(Main(bot))