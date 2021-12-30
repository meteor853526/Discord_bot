from datetime import datetime
import json
import requests

with open('setting.json', mode='r',encoding='utf-8') as jFile: 
    jdata = json.load(jFile)

def astron_sun(where):
    url1 = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/A-B0062-001?Authorization=CWB-51EBE041-95F2-44A9-9DA8-4BE9C74EEEE5&timeFrom=2022-01-01&sort=dataTime")
    data1 = json.loads(url1.text)
    # url1 為 01-01日 到 06-29日 的資料
    diction1 = data1["records"]["locations"]

    url2 = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/A-B0062-001?Authorization=CWB-51EBE041-95F2-44A9-9DA8-4BE9C74EEEE5&timeFrom=2022-06-30&sort=dataTime")
    data2 = json.loads(url2.text)
    # url2 為 06-30日 到 12-26日 的資料
    diction2 = data2["records"]["locations"]
    # 把d2加到d1裡面

    url3 = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/A-B0062-001?Authorization=CWB-51EBE041-95F2-44A9-9DA8-4BE9C74EEEE5&timeFrom=2022-12-27&sort=dataTime")
    data3 = json.loads(url3.text)
    # url3 為 12-27日 到 年底 的資料
    diction3 = data3["records"]["locations"]
    # 把d3加到d1裡面

    # for country in all :
    #     # 分別的縣市名稱-->變成list
    #     get = country["locationName"]
    #     list1.append(get)
    
    # bac為目前的時間(因為設計從2022開始，所以跨完年會把下一行打開)
    # bac = str(datetime.now().strftime('%Y-%m-%d'))
    bac = "2023-03-09"
    # 上面為待修改的時間

    remember = {}
    for country in diction1["location"]:
        get = country["locationName"]
        # 找到正確的地點
        if(get == where):
            for i in country["time"]:
                # 找到正確的時間
                if(i["dataTime"] == bac):
                    remember["sun_out"] = i["parameter"][1]["parameterValue"]
                    remember["cross_middle"] = i["parameter"][3]["parameterValue"]
                    remember["angle"] = i["parameter"][4]["parameterValue"]
                    remember["sun_in"] = i["parameter"][5]["parameterValue"]
                    break
    for country in diction2["location"]:
        get = country["locationName"]
        # 找到正確的地點
        if(get == where):
            for i in country["time"]:
                # 找到正確的時間
                if(i["dataTime"] == bac):
                    remember["sun_out"] = i["parameter"][1]["parameterValue"]
                    remember["cross_middle"] = i["parameter"][3]["parameterValue"]
                    remember["angle"] = i["parameter"][4]["parameterValue"]
                    remember["sun_in"] = i["parameter"][5]["parameterValue"]
                    break
    for country in diction3["location"]:
        get = country["locationName"]
        # 找到正確的地點
        if(get == where):
            for i in country["time"]:
                # 找到正確的時間
                if(i["dataTime"] == bac):
                    remember["sun_out"] = i["parameter"][1]["parameterValue"]
                    remember["cross_middle"] = i["parameter"][3]["parameterValue"]
                    remember["angle"] = i["parameter"][4]["parameterValue"]
                    remember["sun_in"] = i["parameter"][5]["parameterValue"]
                    break
    return remember

def astron_moon(where):
    
    url1 = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/A-B0063-001?Authorization=CWB-51EBE041-95F2-44A9-9DA8-4BE9C74EEEE5&timeFrom=2022-01-01&sort=dataTime")
    data1 = json.loads(url1.text)
    diction1 = data1["records"]["locations"]
    
    url2 = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/A-B0063-001?Authorization=CWB-51EBE041-95F2-44A9-9DA8-4BE9C74EEEE5&timeFrom=2022-06-30&sort=dataTime")
    data2 = json.loads(url2.text)
    diction2 = data2["records"]["locations"]

    url3 = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/A-B0063-001?Authorization=CWB-51EBE041-95F2-44A9-9DA8-4BE9C74EEEE5&timeFrom=2022-12-27&sort=dataTime")
    data3 = json.loads(url3.text)
    diction3 = data3["records"]["locations"]
    
    # bac為目前的時間(因為設計從2022開始，所以跨完年會把下一行打開)
    # bac = str(datetime.now().strftime('%Y-%m-%d'))
    bac = "2023-05-09"
    # 上面為待修改的時間
    remember = {}
    for country in diction1["location"]:
        get = country["locationName"]
        if(get == where):   
            for i in country["time"]:
                if(i["dataTime"] == bac):
                    remember["moon_out"] = i["parameter"][0]["parameterValue"]
                    remember["moon_cross_middle"] = i["parameter"][2]["parameterValue"]
                    remember["moon_angle"] = i["parameter"][3]["parameterValue"]
                    remember["moon_in"] = i["parameter"][4]["parameterValue"]
                    break
    for country in diction2["location"]:
        get = country["locationName"]
        if(get == where):   
            for i in country["time"]:
                if(i["dataTime"] == bac):
                    remember["moon_out"] = i["parameter"][0]["parameterValue"]
                    remember["moon_cross_middle"] = i["parameter"][2]["parameterValue"]
                    remember["moon_angle"] = i["parameter"][3]["parameterValue"]
                    remember["moon_in"] = i["parameter"][4]["parameterValue"]
                    break
    for country in diction3["location"]:
        get = country["locationName"]
        if(get == where):   
            for i in country["time"]:
                if(i["dataTime"] == bac):
                    remember["moon_out"] = i["parameter"][0]["parameterValue"]
                    remember["moon_cross_middle"] = i["parameter"][2]["parameterValue"]
                    remember["moon_angle"] = i["parameter"][3]["parameterValue"]
                    remember["moon_in"] = i["parameter"][4]["parameterValue"]
                    break
    return remember

def img_get_moon():
    year = datetime.now().strftime('%Y')
    bac = datetime.now().strftime('%m')
    res = datetime.now().strftime('%d')
    source = 'https://www.cwb.gov.tw/Data/astronomy/moon/'+str(year)+str(bac)+str(res)+'.jpg'
    return source
