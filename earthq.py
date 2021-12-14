import urllib.request as req
import bs4
import pandas as pd

def earth():
    df = pd.DataFrame()
    for i in range(0,4):
        url = f'https://scweb.cwb.gov.tw/zh-tw/earthquake/world/'
        df = pd.concat([df, pd.read_html(url)[0]]) # 爬取+合併DataFrame
    return df