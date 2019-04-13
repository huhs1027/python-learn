import os

import requests


def down(fileDir, fileName, url, headers):
    if not os.path.exists(fileDir):
        os.makedirs(fileDir)
    if os.path.exists(fileName):
        #print(fileName + "已存在")
        return
    file = open(fileName, 'wb')
    file.write(requests.get(url, headers=headers).content)
    file.close()
