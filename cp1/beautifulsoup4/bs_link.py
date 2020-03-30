from bs4 import BeautifulSoup
html = """
<html><body>
    <ul>
        <li><a herf="http://www.naver.com">naver</a></li>
        <li><a herf="http://www.daum.com">daum</a></li>
    </ul>
</body><html>
"""

soup = BeautifulSoup(html, 'html.parser')

# a 태그 추출
links = soup.find_all("a")

print(type(links))
for a in links:
    herf = a.attrs['herf']
    text = a.string
    print(text, ">", herf)