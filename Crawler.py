import urllib.request as req
import bs4
# 安裝套件 pip install beautifulsoup4
from datetime import datetime
def crawler():

    # 抓取 soft job 版的網頁原始碼(HTML)
    
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

    from datetime import datetime
    #獲取當前時間
    bac = datetime.now().strftime('%Y%m%d%H')
    res = datetime.now().strftime('%Y%m%d%H' + '%M')
    lasttime = int(int(res[10] + res[11]) / 10) *10 - 10
    bac = bac + str(lasttime)

    for img in titles:
            if 'src' in img.attrs:
                if img['src'].endswith('.png'):
                    source = "https://www.cwb.gov.tw" + img['src']
                    source = source[:-4] +'_'+ bac + '.png'
                    break



    return source