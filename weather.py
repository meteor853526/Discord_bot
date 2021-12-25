# coding: utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
#一周天氣預報
def today(city_name):
    url = 'https://www.cwb.gov.tw/V8/C/W/week.html'

    #啟動模擬瀏覽器
    driver = webdriver.Chrome(r'C:\\Users\\liyin\Downloads\\chromedriver_win32\\chromedriver.exe')
    # tina的網址：C:\\Users\\123\Downloads\\chromedriver_win32 (1)\\chromedriver.exe
    # lili的網址：C:\\Users\\liyin\Downloads\\chromedriver_win32\\chromedriver.exe

    #取得網頁代碼
    driver.get(url)

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

def weekly(city_name):
    url = 'https://www.cwb.gov.tw/V8/C/W/week.html'

    #啟動模擬瀏覽器
    driver = webdriver.Chrome(r'C:\\Users\\liyin\Downloads\\chromedriver_win32\\chromedriver.exe')

        # #測站異常時，溫度='-'
        # if not th.nextSibling.text == '-':
        #     temp = float(th.nextSibling.text)
        # else:
        #     temp = -99
    #取得網頁代碼
    driver.get(url)

        # print(name, temp, date)
    #指定 lxml 作為解析器
    soup = BeautifulSoup(driver.page_source, features='lxml')

    #關閉模擬瀏覽器       
    #<table id='table1'>
    table = soup.find('table',{'id':'table1'})
    tbody = soup.find_all('tbody')
    day = ['1','2','3','4','5','6','7']
    # 儲存縣市的代碼以及名字
    city_id = {}
    for tr in tbody:
        th = tr.th
        # 得到id = 'Cxxxxx'->去找後面的headers
        city_id[th.span.text] = th.get('id')
    sp = []
    # date存從接收指令那天開始的一周
    date = []
    # data：將星期與天氣做成物件
    data = {}
    for tr in tbody:
        th = tr.th
        
        if(th.span.text==city_name):
            for i in day:
                # 找星期
                d = table.find('th',{'id':'day'+i})
                # 把日期跟\n去掉
                t = str(d.text)[-4]+str(d.text)[-3]+str(d.text)[-2]
                # 找溫度
                td = tr.find('td',{'headers':'day'+i})
                p = td.p
                temp = p.find('span',{'class':'tem-C'})
                # 把\u2002去掉
                tt = str(temp.text)[0]+str(temp.text)[1]+' - '+str(temp.text)[-2]+str(temp.text)[-1]
                sp.append(tt)
                data[t] = tt
    driver.quit()
    return data

# week = today("新北市")
# print(week)