import scrapy


class Book2Spider(scrapy.Spider):
    name = 'book2'
    start_urls = [
        'https://wikibook.co.kr/list/'
    ]

    def parse(self, response):
        li_list = response.css('.book-url')
        for a in li_list:
            href = a.css('::attr(href)').extract_first()
            text = a.css('::text').extract_first()

            href2 = response.urljoin(href)

            yield {
                'text': text,
                'url': href2
            }
