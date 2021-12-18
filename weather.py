# coding: utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
#一周天氣預報
def today(city_name):
    url = 'https://www.cwb.gov.tw/V8/C/W/week.html'

    #啟動模擬瀏覽器
    driver = webdriver.Chrome(r'C:\\Users\\liyin\Downloads\\chromedriver_win32\\chromedriver.exe')

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

    # city_name = '臺中市'
    for tr in table:
        th = tr.th
        if(th.span.text==city_name):
            td = tr.find('td',{'headers':'day1'})
            sp = td.find('span',{'class':'tem-C'})
            # print(sp.text)
    #     #取得下個標籤內的文字
    #     name = td.text
    #     print(name)
        # #把字串中測站名稱去除，留下觀測時間
        # sp = td.text.split()
        # print(sp)
        # #date = 01/1907:00
        # date = sp[1]
        
        # #date = 201901/1907:00
        # date = year + date

        # #字串轉為datetime格式
        # date = datetime.datetime.strptime(date, '%Y%m/%d%H:%M')

        # #測站異常時，溫度='-'
        # if not th.nextSibling.text == '-':
        #     temp = float(th.nextSibling.text)
        # else:
        #     temp = -99

        # print(name, temp, date)

    #關閉模擬瀏覽器       
    driver.quit()
    return sp.text