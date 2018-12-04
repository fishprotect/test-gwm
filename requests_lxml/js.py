from selenium import webdriver
import time
from scrapy.selector import Selector
driver = webdriver.PhantomJS()
driver.get('http://car.bitauto.com/hafuh1/peizhi/')
data = driver.title
driver.set_page_load_timeout(60)  #设置超时时间
data = driver.page_source  
# data = Selector(data)
detail2 = driver.find_elements_by_css_selector('#CarCompareContent > table > tbody > tr:nth-child(14) td').text  # 通过css方式定位
# print(detail1)
print(detail2)