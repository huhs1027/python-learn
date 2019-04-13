import json
import requests
from requests.exceptions import RequestException
import re
import time
from lxml import etree 
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
# 猫眼电影网
def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page_xpath(html):
    list = []
    text = etree.HTML(html)
    indexs = text.xpath('//dd/i/text()')
    images = text.xpath('//dd/a/img/@src')
    titles = text.xpath('//dd/a/@title')
    actors = text.xpath('//dd//p[@class="star"]/text()')
    times  = text.xpath('//dd//p[@class="releasetime"]/text()')
    scores_1 = text.xpath('//dd//i[@class="integer"]/text()')
    scores_2 = text.xpath('//dd//i[@class="fraction"]/text()')
    
    for i in range(10):
        infor = {}
        infor['index'] = indexs[i]
        infor['image'] = images[i]
        infor['title'] = titles[i]
        infor['actor'] = actors[i].strip()
        infor['time']  = times[i]
        infor['score'] = scores_1[i] + scores_2[i]
        list.append(infor)
    return list
    

def parse_one_page_BeautifulSoup(html):
    list = []
    soup = BeautifulSoup(html, 'lxml')
    indexs = soup.find_all(class_="board-index")  
    images = soup.select('.board-img')
    titles = soup.select('.name a')
    actors = soup.select('.star')
    times  = soup.select('.releasetime')
    scores_1 = soup.select('.score .integer')
    scores_2 = soup.select('.score .fraction')
    
    for i in range(10):
        infor = {}
        infor['index'] = indexs[i].string
        infor['image'] = images[i].attrs['data-src']
        infor['title'] = titles[i].attrs['title']
        infor['actor'] = actors[i].string.strip()
        infor['time']  = times[i].string
        infor['score'] = scores_1[i].string + scores_2[i].string
        list.append(infor)
    return list


def parse_one_page_pyquery(html):
    list = []
    doc = pq(html)
    indexs = doc('dd').items()
    for index in indexs:
        print(index)
        infor = {}
        infor['index'] = pq(index)('.board-index').text()
        infor['image'] = pq(index)('a img.board-img').attr('data-src')
        infor['title'] = pq(index)('a').attr('title')
        infor['actor'] = pq(index)('.star').text().strip()
        infor['time']  = pq(index)('.releasetime').text()
        infor['score'] = pq(index)('.score .integer').text() + pq(index)('.score .fraction').text()
        list.append(infor)
    return list
    

def show_infor(item):
    
    text = '\n第{}名   {}\n\n{}    {}     评分：{}\n'
    print(text.format(item['index'], item['title'], item['actor'], item['time'], item['score']))
    

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page_BeautifulSoup(html):
        show_infor(item)
        print('*'*90)
    

if __name__ == '__main__':
    
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
