import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import random
import astron,weather,earthquake,Crawler
from discord_components import *
from time import perf_counter
import json
with open('setting.json', mode='r',encoding='utf-8') as jFile: 
    jdata = json.load(jFile)

class Main(Cog_Extension):
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000,2)} (ms)')

    @commands.command()
    async def how(self,ctx):
        embed=discord.Embed(title="關於指令意思", color=0xe17e2d)
        a = "可使用的指令列"
        b = "全球最新地震資訊、台灣最新地震資訊"
        c = "氣象天氣圖"
        d = "定時發送訊息"
        e = "定時發送該地點的訊息"
        f = "所在縣市天氣資訊、日出日落、月出月落"
        embed.add_field(name= "$help", value=a, inline=False)
        embed.add_field(name= "$eq", value=b, inline=False)
        embed.add_field(name= "$craw", value=c, inline=False)
        embed.add_field(name="$set_time 時間",value=d, inline=False)
        embed.add_field(name="$set_location 地點",value=e, inline=False)
        embed.add_field(name="直接輸入縣市", value=f,inline=False)
        await ctx.send(embed=embed)
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)

    # event.py
    @commands.Cog.listener()
    async def on_message(self,msg):
        keyword = ['基隆市','臺北市','新北市','桃園市','新竹縣','新竹市',
        '苗栗縣','臺中市','彰化縣','南投縣','雲林縣','嘉義縣','嘉義市','臺南市',
        '高雄市','屏東縣','臺東縣','花蓮縣','宜蘭縣','澎湖縣','金門縣','連江縣']
        keycontent = msg.content
        if (msg.content in keyword) and (msg.author != self.bot.user):
            await msg.channel.send(
                "圖片選項",
                components=[
                    Button(style=ButtonStyle.grey,label = "日出日落",custom_id="日出日落"), 
                    Button(style=ButtonStyle.green,label = "月出月落",custom_id="月出月落"), 
                    Button(style=ButtonStyle.blue,label = "未來一周天氣(白天)",custom_id="未來一周天氣(白天)"), 
                    Button(style=ButtonStyle.red,label = "未來一周天氣(晚上)",custom_id="未來一周天氣(晚上)"), 
                ],
            )
            while True:
                event = await self.bot.wait_for("button_click",timeout=30)   #點擊button
                if event.channel == msg.channel and (event.custom_id == "日出日落" or event.custom_id == "月出月落" or event.custom_id == "未來一周天氣(白天)" or event.custom_id == "未來一周天氣(晚上)"):
                    await event.respond(                      # 回傳訊息
                            content="顯示成功"  # custom_id + 圖顯示成功
                    )
                    

                    if event.custom_id == '日出日落' :
                        where = msg.content
                        get = {}
                        get = astron.astron_sun(where)

                        embed=discord.Embed(title="天文報告-"+str(where),color=0xea8a8a)
                        embed.set_author(name="中央氣象局資料開放平台", url="https://scweb.cwb.gov.tw/zh-tw/earthquake/world/", icon_url="https://www.kindpng.com/picc/m/178-1780574_weather-forecast-icon-png-transparent-png.png")
                        embed.add_field(name="日出時刻", value=get['sun_out'], inline=True)
                        embed.add_field(name="日沒時刻", value=get['sun_in'], inline=True)
                        embed.add_field(name="太陽仰角", value=get['angle'], inline=False)
                        embed.add_field(name="太陽過中天", value=get['cross_middle'], inline=True)
                        
                        await msg.channel.send(embed=embed)
                    if event.custom_id == '月出月落' :
                        where = msg.content
                        get = {}
                        get = astron.astron_moon(where)

                        embed=discord.Embed(title="天文報告-"+str(where),color=0xea8a8a)
                        embed.set_author(name="中央氣象局資料開放平台", url="https://scweb.cwb.gov.tw/zh-tw/earthquake/world/", icon_url="https://www.kindpng.com/picc/m/178-1780574_weather-forecast-icon-png-transparent-png.png")
                        embed.add_field(name="月出時刻", value=get['moon_out'], inline=True)
                        embed.add_field(name="月沒時刻", value=get['moon_in'], inline=True)
                        embed.add_field(name="月亮仰角", value=get['moon_angle'], inline=False)
                        embed.add_field(name="月亮過中天", value=get['moon_cross_middle'], inline=True)
                        embed.set_image(url=astron.img_get_moon())
                        await msg.channel.send(embed=embed)
                    if event.custom_id == '當天天氣' :
                        # 當天天氣
                        
                        embed=discord.Embed(title="今天天氣", url="https://www.cwb.gov.tw/V8/C/W/week.html",color=0x4895a8)
                        embed.add_field(name=keycontent, value=weather.today(keycontent), inline=False)
                        print(weather.today(keycontent))
                        await msg.channel.send(embed=embed)
                    if event.custom_id == '未來一周天氣(白天)':
                        # 這周天氣
                        week = {}
                        week = weather.weekly(msg.content)
                        embed=discord.Embed(title="未來一周天氣(白天)", url="https://www.cwb.gov.tw/V8/C/W/week.html", description=keycontent, color=0x5592d3)
                        
                        embed.add_field(name= week['day'][0], value=week[0], inline=True)
                        embed.add_field(name= week['day'][1], value=week[2], inline=True)
                        embed.add_field(name= week['day'][2], value=week[4], inline=True)
                        embed.add_field(name= week['day'][3], value=week[6], inline=True)
                        embed.add_field(name= week['day'][4], value=week[8], inline=True)
                        embed.add_field(name= week['day'][5], value=week[10], inline=True)
                        embed.add_field(name= week['day'][6], value=week[12], inline=True)
                        await msg.channel.send(embed=embed)

                    if event.custom_id == '未來一周天氣(晚上)':
                        # 這周天氣
                        week = {}
                        week = weather.weekly(msg.content)
                        embed=discord.Embed(title="未來一周天氣(晚上)", url="https://www.cwb.gov.tw/V8/C/W/week.html", description=keycontent, color=0x5592d3)
                        
                        embed.add_field(name= week['day'][0], value=week[1], inline=True)
                        embed.add_field(name= week['day'][1], value=week[3], inline=True)
                        embed.add_field(name= week['day'][2], value=week[5], inline=True)
                        embed.add_field(name= week['day'][3], value=week[7], inline=True)
                        embed.add_field(name= week['day'][4], value=week[9], inline=True)
                        embed.add_field(name= week['day'][5], value=week[11], inline=True)
                        embed.add_field(name= week['day'][6], value=week[13], inline=True)
                        await msg.channel.send(embed=embed)

    # react.py
    @commands.command()
    # 本機圖片庫
    async def weather(self,ctx):
        pic = discord.File(jdata['pic'])
        await ctx.send(file=pic)

    @commands.command()
    #網頁瀏覽器圖片
    async def web(self,ctx):
        pic = random.choice(jdata['url_pic'])
        await ctx.send(pic)

    @commands.command()
    #爬蟲 - 氣象圖片
    async def craw(self,ctx):
        await ctx.channel.send(
            "圖片選項",
            components=[
                Button(style=ButtonStyle.green,label = "雲層",custom_id="雲層"),  # custom_id每個button獨特的id
                Button(style=ButtonStyle.blue,label = "雷達",custom_id="雷達"),     
                Button(style=ButtonStyle.red,label = "雨量",custom_id="雨量"),
            ],
        )

        while True:
            start = perf_counter()  

            event = await self.bot.wait_for("button_click",timeout=30)   #點擊button
            if event.channel is not ctx.channel:              
                return
            else:                                            # 不同命令間的按鈕會撞
                if event.channel == ctx.channel and (event.custom_id == "雲層" or event.custom_id == "雷達" or event.custom_id == "雨量"):
                    await event.respond(                      # 回傳訊息
                        content=event.custom_id+'圖顯示成功'  # custom_id + 圖顯示成功
                    )
                    await ctx.channel.send(Crawler.crawler(event.custom_id))  # 輸出圖片
        #已修復
        
    @commands.command() 
    async def eq(self,ctx):  
        
        await ctx.channel.send(
            "圖片選項",
            components=[
                Button(style=ButtonStyle.red,label = "全球地震",custom_id="全球地震"),  # custom_id每個button獨特的id
                Button(style=ButtonStyle.blue,label = "台灣地震",custom_id="台灣地震"), 
            ],
        )      

        while True:
            event = await self.bot.wait_for("button_click",timeout=30)   #點擊button
            if event.channel == ctx.channel and (event.custom_id == "全球地震" or event.custom_id == "台灣地震"):
                await event.respond(                      # 回傳訊息
                        content="顯示成功"  # custom_id + 圖顯示成功
                )
                if event.custom_id == '全球地震' :

                    first = {}
                    first = earthquake.earth() 
                    
                    embed=discord.Embed(title="全球地震報告",color=0xea8a8a)
                    embed.set_author(name="中央氣象局資料開放平台", url="https://scweb.cwb.gov.tw/zh-tw/earthquake/world/", icon_url="https://www.kindpng.com/picc/m/178-1780574_weather-forecast-icon-png-transparent-png.png")
                    embed.add_field(name="地震台灣時間", value=first['time'], inline=False)
                    embed.add_field(name="經度", value=first['longitude'], inline=True)
                    embed.add_field(name="緯度", value=first['latitude'], inline=True)
                    embed.add_field(name="深度", value=first['depth'], inline=False)
                    embed.add_field(name="規模", value=first['scale'], inline=False)
                    embed.add_field(name="地震位置", value=first['space'], inline=False)
                    
                    await ctx.channel.send(embed=embed)
                if event.custom_id == '台灣地震':
                    
                    Alldata = {}
                    Alldata = earthquake.twearthquake()  
                    # 呼叫 earthquake 中的 twearthquake() 並回傳Alldata字典
                    
                    embed=discord.Embed(title="地震報告", url=Alldata['web'], description="報告連結",color=0x505177)
                    embed.set_author(name="中央氣象局資料開放平台", url="https://opendata.cwb.gov.tw/devManual/insrtuction", icon_url="https://www.kindpng.com/picc/m/178-1780574_weather-forecast-icon-png-transparent-png.png")
                    embed.add_field(name="發生時間", value=Alldata['time'], inline=False)
                    embed.add_field(name="震央", value=Alldata['where'], inline=False)
                    embed.add_field(name="芮氏規模", value=Alldata['level'], inline=True)
                    embed.add_field(name="深度", value=Alldata['depth'], inline=True)
                    # embed.add_field(name="最大震度"+ str(Alldata['areaLevel']) +"級地區", value=Alldata['area'], inline=False)
                    
                    embed.set_image(url=Alldata['Image'])
                    await ctx.channel.send(embed=embed)
                       
    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'Set Channel: {self.channel.mention}')

    @commands.command()
    async def set_time(self,ctx,time):
        with open('setting.json','r',encoding = 'utf-8')as jfile:
            jdata = json.load(jfile)
        jdata["time"] = time
        with open('setting.json','w',encoding = 'utf-8')as jfile:
            json.dump(jdata,jfile,indent = 4)
    
    @commands.command()
    async def set_location(self,ctx,city):
        with open('setting.json','r',encoding = 'utf-8')as jfile:
            jdata = json.load(jfile)
        jdata["location"] = city
        with open('setting.json','w',encoding = 'utf-8')as jfile:
            json.dump(jdata,jfile,indent = 4)
    # @commands.command()
    # #爬蟲 - 地震表
    # async def tweq(self,ctx):
    #     Alldata = {}
    #     Alldata = earthquake.twearthquake()  # 呼叫earthq中的twearthquake()並回傳Alldata字典
                

    @commands.command()
    #爬蟲 - 地震表
    async def tweq(self,ctx):
        Alldata = {}
        Alldata = earthquake.twearthquake()  # 呼叫earthq中的twearthquake()並回傳Alldata字典
        
        embed=discord.Embed(title="地震報告", url=Alldata['web'], description="報告連結",color=0x505177)
        embed.set_author(name="中央氣象局資料開放平台", url="https://opendata.cwb.gov.tw/devManual/insrtuction", icon_url="https://www.kindpng.com/picc/m/178-1780574_weather-forecast-icon-png-transparent-png.png")
        embed.add_field(name="發生時間", value=Alldata['time'], inline=False)
        embed.add_field(name="震央", value=Alldata['where'], inline=False)
        embed.add_field(name="芮氏規模", value=Alldata['level'], inline=True)
        embed.add_field(name="深度", value=Alldata['depth'], inline=True)
        # embed.add_field(name="最大震度"+ str(Alldata['areaLevel']) +"級地區", value=Alldata['area'], inline=False)
        
        embed.set_image(url=Alldata['Image'])
        await ctx.send(embed=embed)



    @commands.command()
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