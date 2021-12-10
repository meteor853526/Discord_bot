import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json', mode='r',encoding='utf-8') as jFile: 
    jdata = json.load(jFile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword = ['基隆市','台北市','新北市','桃園縣','新竹市','新竹縣',
        '苗栗縣','台中市','彰化縣','南投縣','雲林縣','嘉義市','嘉義縣','台南市',
        '高雄市','屏東縣','台東縣','花蓮縣','宜蘭縣','澎湖縣','金門縣','連江縣']
        if (msg.content in keyword) and (msg.author != self.bot.user):
            await msg.channel.send(msg.content)

def setup(bot):
    bot.add_cog(Event(bot))