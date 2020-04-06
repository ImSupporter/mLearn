from selenium.webdriver import Firefox, FirefoxOptions

options = FirefoxOptions()
options.add_argument('-headless')
browser = Firefox(options=options)

browser.get("https://www.google.com")

r = browser.execute_script("return 100+50")
print(r)