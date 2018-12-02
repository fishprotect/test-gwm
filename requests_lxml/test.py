#
import requests
import os 
from lxml import etree
from lxml.cssselect import CSSSelector
import re
import js2xml
from bs4 import BeautifulSoup

User_Agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:63.0) Gecko/20100101 Firefox/63.0'

url = 'http://car.bitauto.com/hafuh9/peizhi/'

r = requests.get(url,headers={'User_Agent':User_Agent})
reg = re.compile('^carCompareJson = (.*?)]]]$')
text = reg.findall(str(r.text))
print(r.text)
print(text)
