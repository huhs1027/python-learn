import json
import re

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    referer = "https://www.bilibili.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    url = "https://www.bilibili.com/video/av48640518/"
    response = requests.get(url, headers=headers).text
    # print(response)
    bs = BeautifulSoup(response, "lxml")
    # print(bs.prettify())

    # window.__playinfo__= 要找这个内容.
    print(
        '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    pattern = r'\<script\>window\.__playinfo__=(.*?)\</script\>'
    result = re.findall(pattern, response)[0]
    print(result)
    obj = json.loads(result)

    item = obj['data']['dash']['video']
    print(item)

    list = []

    for it in item:
        # print(it)
        print(it['baseUrl'])
        list.append(it['baseUrl'])

    print(list)
