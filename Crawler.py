import urllib.request as req
import bs4
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

    for img in titles:
            if 'src' in img.attrs:
                if img['src'].endswith('.png'):
                    
                    source = "https://www.cwb.gov.tw/" + img['src']
                    break;

    
    # for title in titles:
    #     if title.a !=None:#如果標題包含 a 標籤(沒有被刪除),印出來
    #          print(title.a.string)
    return source