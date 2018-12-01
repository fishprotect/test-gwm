# -*- coding: utf-8 -*-
import scrapy
import os
class BitautoSpider(scrapy.Spider):
    name = 'bitauto'
    start_urls = ['http://car.bitauto.com/hafu-196/']

    def parse(self, response):
        x = response.css('#data_table_MasterSerialList_0 .img-info-layout-vertical.img-info-layout-vertical-center.img-info-layout-vertical-180120')
        for i in x:
            detail = i.css('ul.p-list li.name')
            name = detail.css('a::text').extract_first()
            next_url = detail.css('a[href]::attr(href)').extract_first()
            url = response.urljoin(next_url)
            os.mkdir('./'+name)
            with open('./'+name+'/'+name+'.txt',w+) as f:
                f.write(url)

        
        
