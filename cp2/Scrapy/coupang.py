# -*- coding: utf-8 -*-
import scrapy


class CoupangSpider(scrapy.Spider):
    name = 'coupang'
    allowed_domains = ['coupang.com']
    start_urls = ['http://coupang.com/']

    def parse(self, response):
        pass
