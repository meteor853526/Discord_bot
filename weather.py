# coding: utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
import json
import requests

#一周天氣預報
def today(city_name):
    url = 'https://www.cwb.gov.tw/V8/C/W/week.html'
    
    #啟動模擬瀏覽器
    driver = webdriver.Chrome(r'C:\\chromedriver.exe')
    # tina的網址：C:\\Users\\123\Downloads\\chromedriver_win32 (1)\\chromedriver.exe
    # lili的網址：C:\\Users\\liyin\Downloads\\chromedriver_win32\\chromedriver.exe
    # An: C:\\chromedriver.exe
    #取得網頁代碼
    driver.get(url)
    time.sleep( 5 )
    #指定 lxml 作為解析器
    soup = BeautifulSoup(driver.page_source, features='lxml')

    #<table id='table1'>
    table = soup.find_all('tbody')
    # 儲存縣市的代碼以及名字
    city_id = {}
    for tr in table:
        th = tr.th
        # 得到id = 'Cxxxxx'->去找後面的headers
        city_id[th.span.text] = th.get('id')
    sp = "12"
    for tr in table:
        th = tr.th
        if(th.span.text==city_name):
            td = tr.find('td',{'headers':'day1'})
            sp = td.find('span',{'class':'tem-C'})
    sp = sp.text
    driver.quit()
    return sp

def weekly(city):

    url = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=CWB-52C9B737-834C-4B2A-A760-12C990B1E01E&locationName=&elementName=MinT,MaxT")
    data = url.text
    data2 = json.loads(data)

    loc = data2["records"]['locations']
    Temp = dict(loc[0])

    if city == "新竹縣":Temp = dict(Temp['location'][0])
    if city == "金門縣":Temp = dict(Temp['location'][1])
    if city == "苗栗縣":Temp = dict(Temp['location'][2])
    if city == "新北市":Temp = dict(Temp['location'][3])
    if city == "宜蘭縣":Temp = dict(Temp['location'][4])
    if city == "雲林縣":Temp = dict(Temp['location'][5])
    if city == "臺南市":Temp = dict(Temp['location'][6])
    if city == "高雄市":Temp = dict(Temp['location'][7])
    if city == "彰化縣":Temp = dict(Temp['location'][8])
    if city == "臺北市":Temp = dict(Temp['location'][9])
    if city == "南投縣":Temp = dict(Temp['location'][10])
    if city == "澎湖縣":Temp = dict(Temp['location'][11])
    if city == "基隆市":Temp = dict(Temp['location'][12])
    if city == "桃園市":Temp = dict(Temp['location'][13])
    if city == "花蓮縣":Temp = dict(Temp['location'][14])
    if city == "連江縣":Temp = dict(Temp['location'][15])
    if city == "臺東縣":Temp = dict(Temp['location'][16])
    if city == "嘉義市":Temp = dict(Temp['location'][17])
    if city == "嘉義縣":Temp = dict(Temp['location'][18])
    if city == "屏東縣":Temp = dict(Temp['location'][19])
    if city == "臺中市":Temp = dict(Temp['location'][20])
    if city == "新竹市":Temp = dict(Temp['location'][21])


    ALLdata = {}
    dayqueue = []
    min = Temp['weatherElement'][0]
    max = Temp['weatherElement'][1]

    for i in range(0,14):
        ALLdata[2*i] = min['time'][i]['elementValue'][0]['value']
        ALLdata[2*i+1] = max['time'][i]['elementValue'][0]['value']

    for i in range(1,15,2):
        day = min['time'][i]["startTime"]
        day = day[0:10]
        temp = pd.Timestamp(day)
        dayqueue.append(temp.day_name())

    for i in range(0,7):
        if dayqueue[i] == "Monday": dayqueue[i] = '星期一'
        if dayqueue[i] == "Tuesday": dayqueue[i] = '星期二'
        if dayqueue[i] == "Wednesday": dayqueue[i] = '星期三'
        if dayqueue[i] == "Thursday": dayqueue[i] = '星期四'
        if dayqueue[i] == "Friday": dayqueue[i] = '星期五'
        if dayqueue[i] == "Saturday": dayqueue[i] = '星期六'
        if dayqueue[i] == "Sunday": dayqueue[i] = '星期日'

    weekData = {}
    weekData['day'] = dayqueue
    for i in range(14):
        weekData[i] = ALLdata[2*i] + " ~ " + ALLdata[2*i+1]
    # print(weekData)
    # print(dayqueue)

    return weekData

def FC():
    
























#     url = 'https://www.cwb.gov.tw/V8/C/W/week.html'

#     #啟動模擬瀏覽器
#     driver = webdriver.Chrome(r'C:\\chromedriver.exe')

#         # #測站異常時，溫度='-'
#         # if not th.nextSibling.text == '-':
#         #     temp = float(th.nextSibling.text)
#         # else:
#         #     temp = -99
#     #取得網頁代碼
#     driver.get(url)

#         # print(name, temp, date)
#     #指定 lxml 作為解析器
#     soup = BeautifulSoup(driver.page_source, features='lxml')
#     time.sleep( 5 )
#     #關閉模擬瀏覽器       
#     #<table id='table1'>
#     table = soup.find('table',{'id':'table1'})
#     tbody = soup.find_all('tbody')
#     day = ['1','2','3','4','5','6','7']
#     # 儲存縣市的代碼以及名字
#     city_id = {}
#     for tr in tbody:
#         th = tr.th
#         # 得到id = 'Cxxxxx'->去找後面的headers
#         city_id[th.span.text] = th.get('id')
#     sp = []
#     # date存從接收指令那天開始的一周
#     date = []
#     # data：將星期與天氣做成物件
#     data = {}
#     for tr in tbody:
#         th = tr.th
        
#         if(th.span.text==city_name):
#             for i in day:
#                 # 找星期
#                 d = table.find('th',{'id':'day'+i})
#                 # 把日期跟\n去掉
#                 t = str(d.text)[-4]+str(d.text)[-3]+str(d.text)[-2]
#                 # 找溫度
#                 td = tr.find('td',{'headers':'day'+i})
#                 p = td.p
#                 temp = p.find('span',{'class':'tem-C'})
#                 # 把\u2002去掉
#                 tt = str(temp.text)[0]+str(temp.text)[1]+' - '+str(temp.text)[-2]+str(temp.text)[-1]
#                 sp.append(tt)
#                 data[t] = tt
#     driver.quit()
    #  return data

# # week = today("新北市")
# # print(week)
    