import requests
import json

apikey = "65dd111c0d71f1fc62ab05bfbb5ae254"

cities = ["Yongin,KR", "Tokyo,JP", "Beijing,CN"]

api = "http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"

k2c = lambda k: k-273.15

for name in cities:
    url = api.format(city=name, key=apikey)
    print(url)
    r = requests.get(url)

    data = json.loads(r.text)

    print(" + 도시 = ",data["name"])
    print(" | 날씨 = ", data["weather"][0]["description"])
    print(" | 최저 기온 = %.2f" % k2c(data["main"]["temp_min"]))
    print(" | 최고 기온 = %.2f" % k2c(data["main"]["temp_max"]))
    print(" | 습도 = ", data["main"]["humidity"])
    print(" | 기압 = ", data["main"]["pressure"])
    print("")

# 풍향과 풍속은 나라별로 제공하지 않는 부분이 있어서 삭제
# 기온은 소수점 아래 둘째자리까지만
