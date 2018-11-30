# -*- coding: utf-8 -*-
import scrapy
class BitautoSpider(scrapy.Spider):
    name = 'bitauto'
    start_urls = ['http://car.bitauto.com/hafu-196/']

    def parse(self, response):
        print(123)
        pass
        
