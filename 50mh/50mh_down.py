import json
import os
import re

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

    baseDir = 'C:\huhongsen\pythonspace\picture\巨人'
    page = '7900'

    while True:
        url = "https://www.50mh.com/manhua/jinjidejuren/{}.html".format(page)
        response = requests.get(url)
        html = response.text
        bs = BeautifulSoup(html, 'lxml')
        print(bs.prettify())

        # 取标题
        head = bs.find('div', attrs={'class': 'head_title'}).find('h2').text

        print(head)
        picDir = baseDir + '\\' + head
        if not os.path.exists(picDir):
            os.makedirs(picDir)

        # var chapterImages = ["1539167722LrZ_71jczKgMrULj.jpg", "1539167730jrRge_Q2yPOTvl2_.jpg", "1539167732DFXpGGrJykNhrloe.jpg", "1539167725kgbDwEKOzaT8NXsX.jpg", "1539167725HX74i7xtWanSVwW5.jpg", "1539167725s-OjQDgQH62lnToX.jpg", "1539167767J9i_OQGXCoFXypn3.jpg", "1539167769g5rdkQK10L11i_Ki.jpg", "1539167763gpyWXvYSP9s3wtcd.jpg", "1539167781DVAsTAmj_CNlhaLi.jpg", "1539167773vUxXjL9c_DdaWbHX.jpg", "1539167771IN125x-tLhEwR_Lv.jpg", "15391678017MlHwEj97FKTQe8Z.jpg", "1539167812aEArIAfSvJ-K7w9-.jpg", "15391678148fRr5OZRXYeZVe1L.jpg", "1539167820SLeDbOOQb0ZvBWMq.jpg", "1539167814wMwg7yrIN34AhOh3.jpg", "1539167819D-zVwqRzIt6VMi19.jpg", "1539167839OqQxn9EG48NSEHm2.jpg", "15391678619Ig4sbHSXljTcoRW.jpg", "1539167867RoCOvjml68r0l_Hh.jpg", "1539167857_-9emqwwA2XGydnl.jpg", "1539167855RUNH0jESD7JPYmYx.jpg", "1539167873pIOQiifINVUaIyYi.jpg", "1539167871XuXSRA_izagrWRIf.jpg", "15391678992UStBsE4GBBUAmZE.jpg", "1539167899rZOA0mXA6LGioKhR.jpg", "1539167898gp3O5wacfMSxQX2s.jpg", "1539167913albjG3KDlFjs-MV1.jpg", "1539167915l2T-3Jqp9ab7zO6P.jpg", "1539167916fbCnA38kGNVkuG6Y.jpg", "1539167937rsJo0ySogXUVte02.jpg", "1539167939Bw-jABRacWSAJ-93.jpg", "1539167941Hp75MH5ouJ8P2xCb.jpg", "1539167954lMze8ssbVxvG5DFg.jpg", "1539167967Xms0gEwClKvJWjRj.jpg", "1539167964bV_4SzOxwEOkOAgV.jpg", "15391679821B1WUFJZZ3xF8hEf.jpg", "1539167990APPaCY2J1CcC5oY1.jpg", "1539167982Zj2Lvs0HdZEq3gAC.jpg", "1539167989YTERmssVyqJG9D9e.jpg", "1539168001erqw7gZp3ZpplqpV.jpg", "15391680113RLv8YTrZjWktCCB.jpg", "1539168022nPwtH17cIzUlmlZ_.jpg", "1539168027lv_BD6jeUDxkM8WT.jpg", "1539168030LdTkkzzdgeK-lkmo.jpg", "1539168033jd1XIhmCYzDD4DIt.jpg", "15391680494Mae1Y_N1IirTlLc.jpg", "1539168047UsHZ-UiKEU2mkgck.jpg", "1539168048YqKd65fcQgx5ZFUP.jpg", "1539168052eCHD86E-VEPYAIDE.jpg"];
        pattern = r'chapterImages = (.*?);'
        pic_list = re.findall(pattern, html)
        print(pic_list)
        print(pic_list[0])
        j = json.loads(pic_list[0])
        chapterPattern = r'chapterPath = "(.*?)";'
        subUrl = re.findall(chapterPattern, html)[0]
        print(subUrl)
        ye = 1
        baseUrl = 'https://res02.333dm.com/'
        for picUrl in j:
            picutreUrl = baseUrl + subUrl + picUrl
            print("图片地址:" + picutreUrl)
            # 下载
            rsp = requests.get(picutreUrl)
            file = open(picDir + "\\" + str(ye) + ".jpg", 'wb')
            file.write(rsp.content)
            file.close()
            rsp.close()
            ye += 1

        # 下一话
        nextPagePattern = r'nextChapterData = (.*?);'
        nextPage = re.findall(nextPagePattern, html)[0]
        print(nextPage)
        nextPageJson = json.loads(nextPage)
        print(nextPageJson['id'])
        print(nextPageJson['name'])
        head = nextPageJson['name']
        page = nextPageJson['id']

    # browser = webdriver.Chrome()
    # browser.get(url)
    #
    # while True:
    #     #print(browser.page_source)
    #
    #     # 获取图片
    #     eleImg = browser.find_element_by_id('images').find_element_by_tag_name('img')
    #     picUrl = eleImg.get_attribute('src')
    #     index = eleImg.get_attribute('data-index')
    #     print(picUrl)
    #     print(index)
    #
    #     # 下载
    #     file = open('C:\huhongsen\pythonspace\picture\巨人\\' + index + ".jpg", 'wb')
    #     file.write(requests.get(picUrl).content)
    #     file.close()
    #
    #     # 下一页
    #     next = browser.find_element_by_class_name('img_land_next')
    #     #ActionChains(webdriver).move_to_element(next).click(next).perform()
    #     next.click()

# https://res02.333dm.com/images/comic/4/7900/1539167722LrZ_71jczKgMrULj.jpg
