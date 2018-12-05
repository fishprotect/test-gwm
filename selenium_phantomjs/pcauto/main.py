#
import requests
import time
from scrapy.selector import Selector
from detail import Selenium_PhantomJS

ERROR = '\033[0;31m %s \033[0m'
SUCCESS = '\033[0;42m %s \033[0m'


header = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}
url = 'https://price.pcauto.com.cn/price/nb845/'
r = requests.get(url,headers=header)
res = Selector(r)
res = res.css(' .bigPic .thBig .tit a::attr(href)').extract()
cars_list = []
for type_car in res:
    next_url = 'http://price.pcauto.com.cn'+type_car+'config.html'
    cars_list.append(next_url)

def run_function(url,count,SUCCESS,ERROR):
    try:
        run = Selenium_PhantomJS(url)
        run.fun_main()
        print_str = '[info]:'+url
        print(SUCCESS % print_str)
    except:
        if count == 3:
            print_str = '[error]:'+url
            print(ERROR % print_str)
        else:
            run_function(url,count+1,SUCCESS,ERROR)
for url in cars_list:
    count = 1
    run_function(url,count,SUCCESS,ERROR)
    # try:
    #     run = Selenium_PhantomJS(url)
    #     run.fun_main()
    #     print_str = '[info]:'+url
    #     print(SUCCESS % print_str)
    #     # print("\033[1;33;40m%\033[0m"%("[INFO]"),url) 
    # except:
    #     try:
    #         run = Selenium_PhantomJS(url)
    #         run.fun_main()
    #         print_str = '[info]:'+url
    #         print(SUCCESS % print_str)
    #     except:
    #         print_str = '[error]:'+url
    #         print(ERROR % print_str)
    #         # print("\033[1;31;40m%\033[0m"%("[ERROR]"),url) 
        