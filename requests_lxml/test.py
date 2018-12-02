#
import requests
import os 
from lxml import etree

User_Agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'

url = 'http://car.bitauto.com/hafuh9/peizhi/'

content = requests.get(url,headers={'User_Agent':User_Agent})
html = etree.HTML(content.text)
title = html.xpath('/html/body/header/div[2]/div/div[1]/h1/a[2]')
title2 = html.cssselect(' #CarCompareContent > table:nth-child(1) > tbody:nth-child(1) tr')

print(title[0].text)
print(title2)
