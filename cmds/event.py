import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
import weather

with open('setting.json', mode='r',encoding='utf-8') as jFile: 
    jdata = json.load(jFile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword = ['基隆市','臺北市','新北市','桃園縣','新竹市','新竹縣',
        '苗栗縣','臺中市','彰化縣','南投縣','雲林縣','嘉義市','嘉義縣','臺南市',
        '高雄市','屏東縣','臺東縣','花蓮縣','宜蘭縣','澎湖縣','金門縣','連江縣']
        if (msg.content in keyword) and (msg.author != self.bot.user):
            # 當天天氣
            embed=discord.Embed(title=msg.content, description=weather.today(msg.content),color=0x4895a8)
            embed.set_author(name='今天天氣')
            await msg.channel.send(embed=embed)
            # 這周天氣
            # embed=discord.Embed(title="一周天氣", url="https://www.cwb.gov.tw/V8/C/W/week.html", color=0x5592d3)
            # embed.add_field(name="星期一", value="12 - 14", inline=False)
            # embed.add_field(name="星期一", value="12 - 14", inline=False)
            # embed.add_field(name="星期一", value="12 - 14", inline=False)
            # embed.add_field(name="星期一", value="12 - 14", inline=False)
            # embed.add_field(name="星期一", value="12 - 14", inline=False)
            # embed.add_field(name="星期一", value="12 - 14", inline=False)
            # embed.add_field(name="星期一", value="12 - 14", inline=False)
            # await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Event(bot))