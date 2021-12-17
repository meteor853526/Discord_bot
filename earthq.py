import urllib.request as req
import bs4
import pandas as pd
import json
import requests
def earth():
    for i in range(0,4):
        df = pd.DataFrame()
        url = f'https://scweb.cwb.gov.tw/zh-tw/earthquake/world/'
        df = pd.concat([df, pd.read_html(url)[0]]) # 爬取+合併DataFrame
    return df
def twearthquake():
    url = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=CWB-52C9B737-834C-4B2A-A760-12C990B1E01E&limit=1&offset=0&format=JSON&areaName=%E5%AE%9C%E8%98%AD%E7%B8%A3&stationName=string")
    data = url.text
    data2 = json.loads(data)
    dict1 = {}

    earthquake = data2['records']['earthquake']

    earthquake = dict(earthquake[0]) # list轉dict
    
    source = earthquake['reportImageURI']
    # 修改中
    return source