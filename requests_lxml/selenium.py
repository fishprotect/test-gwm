import requests
from scrapy.selector import Selector
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}
splash_url = 'http://127.0.0.1:8050/render.html'
args = {'url':'http://car.bitauto.com/hafuh9/peizhi/','timeout':6,'image':0}
re = requests.get(splash_url,args,headers = headers)
sel = Selector(re)
x = sel.css('#CarCompareContent > table:nth-child(1) > tbody:nth-child(1) tr').extract()
print(x)

