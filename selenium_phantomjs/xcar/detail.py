#
from openpyxl import Workbook
from scrapy.selector import Selector
class Requests_crawl(object):

    def __init__(url,title):
        headers = {'User-Agent':''}
        self.wb = Workbook()
        self.ws = self.wb.active
        self.title = title
        self.response = resquests.get(url,headers= headers)
        self.content = Selector(self.response)
    def row_title(self):
        title = self.content.css('tr#base_title > td[id^=mod_] >  a::text').extract()
        count_colunm = 2
        for i in title:
            ws.cell(row=1,column=count_colunm,value=i)
            count_cloumn += 1
    def column_title(self):
        title = self.content.css('')
