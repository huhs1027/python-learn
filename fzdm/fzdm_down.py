import os
import re

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
    head = {
        # ':authority': 'manhua.fzdm.com',
        # ':method': 'GET',
        # ':path': '/39/001/',
        # ':scheme:': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        # 'cookie': 'BAIDU_SSP_lcr=https://www.baidu.com/link?url=1weleiCdaN2yD6Q_Ocm9ZuVgNGjlLqMjmfwlL3EMbafvZ1VyQCjkBEnr95crfEUR&wd=&eqid=becf08560000080f000000045cafebea; picHost=p3.xiaoshidi.net; Hm_lvt_cb51090e9c10cda176f81a7fa92c3dfc=1555053796,1555054213,1555054222,1555054501; Hm_lpvt_cb51090e9c10cda176f81a7fa92c3dfc=1555054830',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'upgrade-insecure-requests': '1',
        'referer': 'https://manhua.fzdm.com/39/'
    }

    page = 1

    base_dir = "C:\huhongsen\pythonspace\picture\jvren"
    indx_url = ''
    indx_m_url = '002'
    next_url = ''

    while True:
        # 进击的巨人
        url = "http://manhua.fzdm.com/39/{}/{}".format(indx_m_url, indx_url)
        print('htmlUrl:' + url)
        r = requests.get(url=url, headers=head)
        if r.status_code == requests.codes.ok:
            html = r.text
            bs = BeautifulSoup(html, 'lxml')
            # print(bs.prettify())
            pattern = 'var mhurl="(.*?)"'
            imgs = re.findall(pattern, html)
            # 标题
            title = re.findall('var Title="(.*?)"', html)[0]
            next_url = re.findall('var nexturl="(.*?)"', html)[0]
            tupiandizhi = "http://p0.xiaoshidi.net/{}".format(imgs[0])
            print("picUrl:" + tupiandizhi)
            # 获取下一页
            indx_url = 'index_{}.html'.format(str(page))

            juan_dir = base_dir + "\\" + title
            if not os.path.exists(juan_dir):
                os.makedirs(juan_dir)

            # 获取图片
            response = requests.get(tupiandizhi, headers=head)
            file = open(juan_dir + "\\" + str(page) + ".jpg", 'wb')
            file.write(response.content)
            file.close()
            response.close()
            page += 1
        else:
            print("下一画")
            page = 1
            indx_url = ''
            indx_m_url = next_url
