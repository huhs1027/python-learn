import os
import re
import threading

import requests
from bs4 import BeautifulSoup


def downPic(html):
    print("线程启动,开始下载")
    pattern = r'narImg\[\d*\] = \'(.*?.jpg)'
    pic_list = re.findall(pattern, html)
    print(pic_list)

    for picUrl in pic_list:
        print(picUrl)
        fileDir = 'C:/huhongsen/pythonspace/pic/' + picUrl.split("/")[-2]
        if not os.path.exists(fileDir):
            os.makedirs(fileDir)
        fileName = fileDir + '/' + picUrl.split("/")[-1]
        if os.path.exists(fileName):
            print("文件已存在 跳过:" + fileName)
            continue
        file = open(fileName, 'wb')
        file.write(requests.get(picUrl).content)
        file.close()


if __name__ == '__main__':
    # 进击的巨人
    url = "http://juren.17dm.com/manhua/117854.html"
    while True:
        response = requests.get(url)
        response.encoding = 'gb2312'
        html = response.text
        bs = BeautifulSoup(html, 'lxml')
        # print(bs.prettify())

        # 改篇图片urlList
        # print(bs.find_all('script',type='text/javascript'))

        # 下一篇url
        next = bs.find('a', text='下一篇')
        nextUrl = next.get('href')
        if (nextUrl == ''):
            print("下一篇不存在,退出")
            break
        else:
            print("下一篇:" + nextUrl)
            url = nextUrl
            # 启动线程,爬下一篇
            threading.Thread(target=downPic, args=(html,)).start()
