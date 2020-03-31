from bs4 import BeautifulSoup
import re # 정규 표현식 모듈

html = """
<ul>
    <li><a herf="hoge.html">hoge</li>
    <li><a herf="https://example.com/fuga">fuga*</li>
    <li><a herf="https://example.com/foo">foo*</li>
    <li><a herf="http://example.com/aaa">aaa</li>
</ul>
"""

soup = BeautifulSoup(html, "html.parser")
li = soup.find_all(herf=re.compile(r"^https://")) # 정규 표현식을 통해 https가 붙은 태그만 추출
for e in li : print(e.attrs['herf'])