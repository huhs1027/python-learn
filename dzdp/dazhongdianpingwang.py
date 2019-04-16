from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from lxml import etree
from pyquery import PyQuery as pq
import re
import json

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 30)

# 配置数据
url = 'https://www.dianping.com/'
KEYWORD = '火锅'
MAX_PAGE = 5
xpath_PageNum = '//div[@class="page"]//a[@class="cur"]'  
css_select_PageText = '.shop-wrap .shop-list.J_shop-list.shop-all-list'                 
show = '\n店名：{}\n\n地址：{}\n'

def index_page(page):
    """
    抓取索引页
    :param page: 页码
    """
    print('\n正在爬取第', page, '页')
    try:
        wait.until(EC.text_to_be_present_in_element((By.XPATH, xpath_PageNum), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_select_PageText)))
        get_merchant()
        if page != MAX_PAGE:
            submit = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'next')))
            submit.click()
    except TimeoutException:
        index_page(page)

def get_merchant():
    '''
    提取商户信息
    '''
    doc = pq(browser.page_source)
    html = doc('#shop-all-list')
    shop = re.findall('<h4>(.*?)</h4>', str(html) , re.S) 
    location = re.findall('<span class="addr">(.*?)</span>', str(html) , re.S)
    for i in range(len(shop)):
        merchant = {
            'shop': shop[i],
            'location': location[i],
            }
        print('*'* 30)
        print(show.format(merchant['shop'], merchant['location']))
        save_to_json(merchant)
    

def judge_handle(): 
    '''
    切换浏览器的当前窗口页面
    '''
    windows = browser.current_window_handle        #定位当前页面句柄
    all_handles = browser.window_handles           #获取全部页面句柄
    for handle in all_handles:                     #遍历全部页面句柄
        if handle != windows:                      #判断条件
            browser.switch_to.window(handle)       #切换到新页面

def save_to_json(result):
    """
    保存至text
    :param result: 结果
    """
    with open ('dazhongdianpingwang.json', 'a', encoding='utf-8') as file:
        file.write(json.dumps(result, indent=2, ensure_ascii=False))
    
def main():
    
    # 进入首页
    browser.get(url)
    # 找到搜索输入框以及按钮
    input = wait.until(EC.presence_of_element_located((By.ID, 'J-search-input')))
    # 输入关键字，并点击按钮
    input.clear()
    input.send_keys(KEYWORD)
    input.send_keys(Keys.ENTER)
    judge_handle()                 # 切换至当前窗口
    for i in range(1, MAX_PAGE+1):
        index_page(i)


if __name__ == '__main__':
    
    main()
