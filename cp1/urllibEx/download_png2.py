import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

mem = urllib.request.urlopen(url).read()  # 데이터 읽기(메모리 - binary)

with open(savename, mode="wb") as f:  # 파일 입출력 시 많이 사용되는 구문 >> with open(<파일명>, "모드") as <fd명>:
    f.write(mem)
    print("저장되었습니다...!")
