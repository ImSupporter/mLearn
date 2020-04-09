import scrapy


class Book4Spider(scrapy.Spider):
    name = 'book4'
    allowed_domains = ['wikibook.co.kr']
    start_urls = [
        'https://wikibook.co.kr/list'
    ]

    def parse(self, response):
        li_list = response.css('.book-url')

        for a in li_list[:5]:
            href = a.css('::attr(href)').extract_first()
            yield response.follow(
                response.urljoin(href), self.parse_book
            )

    def parse_book(self, response):
        title = response.url.split("/")[-2]
        img_url = response.css('.book-image-2d::attr(src)').extract_first()

        req = scrapy.Request(
            response.urljoin(img_url),
            callback=self.parse_img
        )

        req.meta["title"] = title
        yield req

    def parse_img(self, response):

        title = response.meta["title"]
        title = title.replace(r'[\/:*?"|.]+','_').strip()
        fname = title+'.jpg'
        with open(fname,'w') as f:
            f.write(response.body)
