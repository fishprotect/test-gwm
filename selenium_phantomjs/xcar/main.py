#
import requests
import time
import random
from scrapy.selector import Selector
from cars import car 
from detail import Requests_crawl

ERROR = '\033[0;31m %s \033[0m'
SUCCESS = '\033[0;32m %s \033[0m'
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'}

# run_function()函数，主要是调用detail.py，且每个网站允许失败3次
def run_function(url,title,count):
    try:
        crawl = Requests_crawl(url,title)
        crawl.main()
        success = "[info]:"+url
        print(SUCCESS % success)
    except:
        if count < 3:
            sleep_time = random.randint(1,3)
            time.sleep(sleep_time)
            run_function(url,title,count+1)
        else:
            error = '[ERROR]:'+url
            print(ERROR % error)

# 调用run_function()函数，执行
def main(list_car):
    for car in list_car:
        # http://newcar.xcar.com.cn/2658/config.ht
        url = 'http://newcar.xcar.com.cn/'+list_car[car]+'/config.htm'
        run_function(url,car,count=0)
        time_sleep = random.randint(1,3)   # 降低访问速度，随即延迟1-3妙
        time.sleep(time_sleep)


# 运行
main(car)
print('End of data collection')