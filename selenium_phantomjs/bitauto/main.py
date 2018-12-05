#
import requests
import time
from scrapy.selector import Selector
from detail import Selenium_PhantomJS
ERROR = '\033[0;31m %s \033[0m'
SUCCESS = '\033[0;42m %s \033[0m'
header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}
url = 'http://car.bitauto.com/hafu-196/'
r = requests.get(url,headers=header)
res = Selector(r)
res = res.css(' #data_table_MasterSerialList_0 div .img')
cars_list = []
for type_car in res:
    next_url = type_car.css('a::attr(href)').extract_first()
    next_url = 'http://car.bitauto.com'+next_url+'peizhi'
    cars_list.append(next_url)
print(cars_list)

for url in cars_list:
    try:
        run = Selenium_PhantomJS(url)
        run.fun_main()
        print_str = '[info]:'+url
        print(SUCCESS % print_str)
        # print("\033[1;33;40m%\033[0m"%("[INFO]"),url) 
    except:
        print_str = '[error]:'+url
        print(ERROR % print_str)
        print("\033[1;31;40m%\033[0m"%("[ERROR]"),url) 
    