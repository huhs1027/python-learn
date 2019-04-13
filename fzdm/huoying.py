import requests
from bs4 import BeautifulSoup

import common
import fzdm

if __name__ == '__main__':
    #取消https ssl验证警告
    requests.packages.urllib3.disable_warnings()
    baseDir = "C:\huhongsen\pythonspace\picture\火影忍者"
    # 目录页
    url = 'https://manhua.fzdm.com/1/'
    heads = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        # 'referer': url
    }

    html = requests.get(url, headers=heads, verify=False).text
    bs = BeautifulSoup(html, 'lxml')
    # print(bs.prettify())
    list = bs.find_all('li', attrs={'class': 'pure-u-1-2 pure-u-lg-1-4'})
    list.reverse()

    # 遍历话数
    for tag in list:
        ye = 0
        while True:
            # 下载
            htmlUrl = url + tag.find('a')['href'] + "/index_{}.html".format(str(ye))
            #print(htmlUrl)
            resp = requests.get(htmlUrl, headers=heads, verify=False)
            if resp.status_code == 200:
                html = resp.text
                bs = BeautifulSoup(html, 'lxml')
                # print(bs.prettify())

                tupiandizhi, title, next_url = fzdm.prase(html)
                print(tupiandizhi)

                # 下载
                dir = baseDir + '\\' + title
                file = dir + "\\" + str(ye + 1) + ".jpg"
                common.down(dir, file, requests.get(tupiandizhi, headers=heads).content)
                ye += 1
            else:
                print("下一话")
                break
