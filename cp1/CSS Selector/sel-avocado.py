from bs4 import BeautifulSoup
fp = open("fruits_vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")

print(soup.select_one("li:nth-of-type(6)").string) # 잘 모르겠다
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)
print(soup.select("#ve-list > li[data-lo='us']")[1].string)
print(soup.select("#ve-list > li.black")[1].string)

cond = {"data-lo":"us", "class":"black"}
print(soup.find("li",cond).string)

print(soup.find(id="ve-list").find("li", cond).string)

li_list = soup.select("li")

for li in li_list:
    temp = li.string
    print(temp)
