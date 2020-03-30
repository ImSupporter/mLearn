from bs4 import BeautifulSoup

html = """
<html><body>
    <h1>스크레핑이란?</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser') # 파서의 종류는 html.parser로 지정

h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling # 그냥 next_sibling을 하면 줄바꿈 문자가 출력되기 때문에 한번 더 next_sibling을 해서 그 다음 p태그가 나오도록 한다.

print("h1 = "+h1.string)
print("p = "+p1.string)
print("p = "+p2.string)