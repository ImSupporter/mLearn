from bs4 import BeautifulSoup
import urllib.request as req

# 2020년 3월31일 기준
url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')

price = soup.select_one("div.head_info > span.value").string
print("usd/krw = ", price)