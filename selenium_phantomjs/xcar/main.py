#
import requests
import time
from scrapy.selector import Selector
from cars import car 

ERROR = '\033[0;31m %s \033[0m'
SUCCESS = '\033[0;42m %s \033[0m'
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}


def run_function(url,ERROR,SUCCESS):
    pass
car_list = []
for i in car:
    # http://newcar.xcar.com.cn/4021/config.html
    url = 'http://newcar.xcar.com.cn/'+car[i]+'/config.htm'
    # url = 'http://www.httpbin.org/user-agent'
    print(url)
    car_list.append(url)
for i in car_list:
    r = requests.get(i,headers=headers)
    # print(r.text)
    # code = 
    res = r.content.decode(r.encoding)
    res_code = Selector(r)
    title = res_code.css('title').extract_first()
    print(title)
    row_titles = res_code.css('tr#base_title > td[id^=mod_] >  a::text').extract()
    print(row_titles)
    title = res_code.css('').extract()
    print(title)

    print(title)

    with open('res.html','w',encoding=r.encoding,errors='ignore') as f:
        f.write(res)
    break
print('SUCCESS')