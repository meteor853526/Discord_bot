import urllib.request as req
import bs4

url="https://scweb.cwb.gov.tw/zh-tw/earthquake/data/"
#建立一個Request物件，附加Request Headers 資訊
request = req.Request(url,headers={
    "User.Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
})

# 利用request物件去打開網址
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# print(data)

root = bs4.BeautifulSoup(data,"html.parser")
titles = root.find_all("table")
print(titles)