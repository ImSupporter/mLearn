import scrapy

class Book1Spider(scrapy.Spider):
    name = 'book'
    start_urls = [
        'https://wikibook.co.kr/list/'
    ]

    def parse(self, response):
        title = response.css('title')
        print(title.extract())