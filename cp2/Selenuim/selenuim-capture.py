from selenium.webdriver import Firefox, FirefoxOptions

url = "http://www.naver.com/"

option = FirefoxOptions()
option.add_argument('-headless')

browser = Firefox(options=option)

browser.get(url)

browser.save_screenshot("Website.png")

browser.quit()

# firefox diriver를
# https://github.com/mozilla/geckodriver/releases 에서
# 자신에게 맞는 운영체제를 선택한 다음
# 패키지들이 저장된 경로에 설치
# ~/venv/mLearn/lib/python3.7/site-packages/
