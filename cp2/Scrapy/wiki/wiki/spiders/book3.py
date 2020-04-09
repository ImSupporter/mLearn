import scrapy


class Book3Spider(scrapy.Spider):
    name = 'book3'
    allowed_domains = ['wikibook.co.kr']

    start_urls = [
        'https://wikibook.co.kr/list'
    ]

    def parse(self, response):
        li_list = response.css('.book-url')
        for a in li_list[:5]:
            href = a.css('::attr(href)').extract_first()
            print(href)

            yield response.follow(
                response.urljoin(href), self.parse_book
            )

    def parse_book(self, response):
        title = response.css('.main-title::text').extract_first()
        img_url = response.css('.book-image-2d::attr(src)').extract_first()

        yield{
            'title': title,
            'img_url': response.urljoin(img_url)
        }
