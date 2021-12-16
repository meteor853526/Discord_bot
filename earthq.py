import urllib.request as req
import bs4
import pandas as pd

import pandas as pd
 
 
bus_table = pd.read_html("https://www.ubus.com.tw/Booking/FareInquiry")
print(bus_table)