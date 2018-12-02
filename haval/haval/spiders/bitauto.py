# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider,Request
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
            url = response.urljoin(next_url)+'peizhi/'
            print(url)
            yield Request(url,self.detail_parse)
    def detail_parse(self,response):
        title = []
        detail = response.css(' #CarCompareContent > table:nth-child(1) > tbody:nth-child(1)')
        # titles = .css('tr.trForPic')
            