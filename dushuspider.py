import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import quote
import json

url = "https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=0&type=T"
response = requests.get(url=url)
# print(response.status_code)
# print(response.headers)
#print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
items = soup.find("div", id="content")
fileName = open("dushu.json", 'wb')
code = {"link": "None","title": "None", "information": "None"}
for item in items.find_all("div", class_="info"):
    code['link'] = item.find("a")['href']
    code['title'] = item.find("a")['title']
    code['information'] = item.find("div", class_="pub").text.strip().split('/')
    text = json.dumps(dict(code), ensure_ascii=False) + "\n"
    fileName.write(text.encode('utf-8'))
    # author = information[0]
    # translators = information[1]
    # publisher = information[2]
    # date = information[3]
    # price = information[4]
    # print(title)
    # print(link)
    # print(information)
    # print("作者： %s " % author)
    # print("译者： %s" % translators)
    # print("出版社：%s" % publisher)
    # print("发行时间 %s" % date)
    # print("书籍价格：%s" % price)
fileName.close()
