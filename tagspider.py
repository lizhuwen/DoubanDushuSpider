import requests
from bs4 import BeautifulSoup
import re
import random

#将豆瓣里面的书签全部提取保存为tags.txt
def get_agent():
    """
    从文件user_agents.txt文件中取出user-agent
    :return:
    """
    appent = []
    with open('user_agents.txt', 'rb') as lines:
        for line in lines.readlines():
            if line:
                appent.append(line.strip()[1:-1 -1])
    random.shuffle(appent) #方法将序列的所有元素随机排序。
    return appent

def get_tags():
    url = "https://book.douban.com/tag/"
    headers = {
        'User-Agent': random.choice(get_agent()),
        'Host': 'book.douban.com',
        'Upgrade-Insecure-Requests': '1',
    }

    response= requests.get(url=url,headers=headers)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    conntent = soup.find("div", id="content")
    patt = '/tag/\w+">(\w+)'
    tables = conntent.find_all("table", class_="tagCol")

    with open('tags.txt', mode='w+', encoding='utf-8') as f:
        for value in tables:
            for i in re.findall(patt,str(value)):
                f.write(i+ '\n')

if __name__ == '__main__':
    get_tags()
