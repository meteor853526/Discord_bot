import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000,2)} (ms)')

    @commands.command()
    async def how(self,ctx):
        embed=discord.Embed(title="關於指令意思", color=0xe17e2d)
        embed.add_field(name="$help", value="顯示可使用的指令列", inline=False)
        embed.add_field(name="$earthq", value="顯示全球最新的地震資訊", inline=False)
        embed.add_field(name="$tweq", value="顯示台灣最新編號的地震資訊", inline=False)
        embed.add_field(name="$craw", value="顯示氣象天氣圖", inline=False)
        embed.add_field(name="直接輸入縣市", value="顯示所在縣市天氣資訊", inline=False)
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)


    # @commands.command()  //複讀機
    # async def sayd(self,ctx,*,msg):
    #     await ctx.message.delete()
    #     await ctx.send(msg)

    # @commands.command()  
    # async def clean(self,ctx,num:int):
    #     await ctx.channel.purge(limit=1)

# 註冊code
def setup(bot):
    bot.add_cog(Main(bot))