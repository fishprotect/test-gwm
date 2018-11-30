# -*- coding: utf-8 -*-
import scrapy


class BitautoSpider(scrapy.Spider):
    name = 'bitauto'
    allowed_domains = ['www.bitauto.com']
    start_urls = ['http://www.bitauto.com/']

    def parse(self, response):
        pass
