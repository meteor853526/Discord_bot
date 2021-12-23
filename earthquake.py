import urllib.request as req
import bs4
import pandas as pd
import json
import requests
def earth():
   
    df = pd.DataFrame()
    url = f'https://scweb.cwb.gov.tw/zh-tw/earthquake/world/'
    df = pd.concat([df, pd.read_html(url)[0]]) # 爬取+合併DataFrame
    df = df.head(1)
    first_data = df.to_dict()
    ff={}
        
    ff["time"] = first_data["地震時間(臺灣時間)"][0]
    ff["longitude"] = first_data['經度'][0]
    ff["latitude"] = first_data['緯度'][0]
    ff["depth"] = first_data["深度(公里)"][0]
    ff["scale"] = first_data['規模'][0]
    ff["space"] = first_data['地震位置(點選可顯示震央位置圖)'][0]
        
    return ff

def twearthquake():
    url = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=CWB-52C9B737-834C-4B2A-A760-12C990B1E01E&limit=1&offset=0&format=JSON&areaName=%E5%AE%9C%E8%98%AD%E7%B8%A3&stationName=string")
    data = url.text
    data2 = json.loads(data)
    Alldata = {}
    
    earthquake = data2['records']['earthquake']

    earthquake = dict(earthquake[0]) # list轉dict

    info = earthquake["earthquakeInfo"]

    infoWhere = info["epiCenter"]                    #json資料解析，這資料長的真的噁心
    infoLevel = info["magnitude"]
    infoDepth = info["depth"]
    # infoArea = earthquake["intensity"]
    # infoArea = infoArea['shakingArea']
    # infoArea = infoArea[0]

    Alldata["time"] = info["originTime"]
    Alldata["Image"] = earthquake['reportImageURI']
    Alldata["web"] = earthquake['web']
    Alldata["where"] = infoWhere["location"]
    Alldata["level"] = infoLevel['magnitudeValue']
    Alldata["depth"] = infoDepth['value']
    # Alldata["area"] = infoArea['areaName']
    # Alldata['areaLevel'] = infoArea["areaIntensity"]['value']

    return Alldata
