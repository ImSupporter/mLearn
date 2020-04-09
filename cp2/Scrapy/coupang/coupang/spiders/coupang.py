import scrapy

from ..selenium_middleware import *


USER = "ID"
PASSWORD = "PW"


class CoupangSpider(scrapy.Spider):
    name = 'coupang'
    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "coupang.selenium_middleware.SeleniumMiddleware": 0
        }
    }

    def start_requests(self):
        selenium_get('http://login.coupang.com/login/login.pang')
        email = get_dom('._loginForm [name=email]')
        email.send_keys(USER)
        password = get_dom('._loginForm [name=password]')
        password.send_keys(PASSWORD)
        button = get_dom("._loginForm button[type=submit]")
        button.click()

        a = get_dom('#myCoupang > a')
        mypage = a.get_attribute('href')
        yield scrapy.Request(mypage, self.parse)

    def parse(self, response):
        items = response.css('.my-order-unit__item-info')
        for item in items:
            title = item.css(".my-order-unit__info-name strong:last-child::text").extract_first().strip()
            info = item.css(".my-order-unit__info-ea::text").extract_first().split('/')[0].strip()
            yield{
                "title": title,
                "info": info
            }
