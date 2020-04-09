# -*- coding: utf-8 -*-
import scrapy


class Book3Spider(scrapy.Spider):
    name = 'book3'
    allowed_domains = ['https://wikibook.co.kr/']
    start_urls = ['http://https://wikibook.co.kr//']

    def parse(self, response):
        pass
