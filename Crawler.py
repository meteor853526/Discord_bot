import urllib.request as req
import bs4
# 安裝套件 pip install beautifulsoup4
from datetime import datetime
def crawler(choice):

    # 抓取 soft job 版的網頁原始碼(HTML)
    if choice == '雲層' :
        bac = datetime.now().strftime('%Y-%m-%d-')
        res = datetime.now().strftime('%Y-%m-%d_%H%M')
        org = int(res[13] + res[14])

        lasttime = int(int(((int(res[13] + res[14]) + 60)-30) % 60) /10)
        lasttime = lasttime*10
        hour = int(res[11] + res[12])
        if org < 30:
            hour = hour - 1
        if lasttime == 60:
            lasttime = str('00')
        if hour < 10 :
            hour = str('0') + str(hour)
        if lasttime == 0:
            lasttime = str('00')
        source = 'https://www.cwb.gov.tw//Data/satellite/LCC_IR1_CR_2750/LCC_IR1_CR_2750-'+bac + str(hour) +'-'+ str(lasttime) + '.jpg'
        return source


    if choice == '雷達':
        url = "https://www.cwb.gov.tw/V8/C/W/OBS_Radar.html"
        # 建立一個 Request 物件 , 附加 Request Headers 的資訊
        request = req.Request(url,headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
        })
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")
        #print(data)
        # 解析原始碼. 取得每篇文章的標題
        
        root = bs4.BeautifulSoup(data,"html.parser") #讓 BeautifulSoup 協助我們解析 HTML 格式文件
        #titles = root.find_all('div', 'zoomHolder') #尋找 class = "title" 的 div 標籤 # find 是bf4的內建套件
        titles = root.find_all('img')
        #print(titles)

        bac = datetime.now().strftime('%Y%m%d')
        res = datetime.now().strftime('%Y%m%d%H' + '%M')

        lasttime = int(int(res[10] + res[11]) / 10) *10
        hour = int(res[8] + res[9])

        if lasttime >= 10:
            lasttime = lasttime - 10
            if lasttime == 0 :
                lasttime = str(lasttime) + '0'
        elif lasttime == 0:
            lasttime = 50
            hour = hour - 1

        if hour == 0:
            hour = str('00')
        if lasttime == 0:
            lasttime = str('00') 
        bac = bac + str(hour) + str(lasttime)

        for img in titles:
                if 'src' in img.attrs:
                    if img['src'].endswith('.png'):
                        source = "https://www.cwb.gov.tw" + img['src']
                        source = source[:-4] +'_'+ bac + '.png'
                        break;

        return source

    if choice == '雨量':
        

        bac = datetime.now().strftime('%Y-%m-')
        res = datetime.now().strftime('%Y-%m-%d_%H%M')
        org = int(res[13] + res[14])
        lasttime = int(int(res[13] + res[14]) / 30) 
        hour = int(res[11] + res[12])
        day = int(res[8] + res[9])
        if lasttime == 0:
            lasttime = 30
            if hour == 0:   # 00:00到00:29之間 抓23:30的圖片
                hour = 23
                day = day-1
            else:
                hour = hour - 1
        else:
            if org-30 <= 10:
                lasttime = str('00')
            else:
                lasttime = 30

        if hour == 0:
            hour = str('00')
        if int(hour) < 10 and int(hour) != 0:
            hour = str('0') + str(hour)
        source = 'https://www.cwb.gov.tw/Data/rainfall/'+bac+str(day)+ "_" + str(hour) + str(lasttime) + '.QZJ8.jpg'   # + 時間.QZJ8.jpg
        return source
    
