#
import requests
import os 
from scrapy.selector import Selector

User_Agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'

url = 'https://price.pcauto.com.cn/price/nb845/'

r = requests.get(url,headers={'User_Agent':User_Agent})
sel = Selector(r)
next_urls = sel.css('.bigPic .thBig .tit a::attr(href)').extract()
print(next_urls) 
#https://price.pcauto.com.cn/sg4580/config.html
for i in next_urls:
    url = 'http://price.pcauto.com.cn'+i+'config.html'
    print(url)
with open('res.html','w') as f:
    f.write(r.text)
print("SUCCESS")