import requests

r = requests.get("http://wikibook.co.kr/logo.png")
# 2020.4.6
# wiki.png ->logo.png
# 파일을 열 수 없다고 뜰 경우 사이트에 들어가서 좌측 상단 이미지를 '검사' 후 주소 수정

with open("test.png", "wb") as f:
    f.write(r.content)

print("saved")