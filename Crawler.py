import urllib.request as req
import bs4
import datetime

# 安裝套件 pip install beautifulsoup4
from datetime import datetime

def crawler():

    # 抓取 soft job 版的網頁原始碼(HTML)
    titles = root.find_all('img')
    #print(titles)

    from datetime import datetime
    #獲取當前時間
    bac = datetime.now().strftime('%Y%m%d%H')
    res = datetime.now().strftime('%Y%m%d%H' + '%M')
    lasttime = int(int(res[10] + res[11]) / 10) *10 
    if lasttime >= 10:
        lasttime = lasttime -10
    

    bac = bac + str(lasttime)

    if lasttime == 0:
        bac = bac + '0'
    
    for img in titles:

        if 'src' in img.attrs:
            if img['src'].endswith('.png'):
                source = "https://www.cwb.gov.tw" + img['src']
                source = source[:-4] +'_'+ bac + '.png'
                break;

    # for title in titles:
    #     if title.a !=None:#如果標題包含 a 標籤(沒有被刪除),印出來
    #          print(title.a.string)


    return source