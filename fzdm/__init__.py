import re


def prase(html):
    # 图片url
    imgs = re.findall('var mhurl="(.*?)"', html)[0]
    # 标题
    title = re.findall('var Title="(.*?)"', html)[0]
    # 下一话
    next_url = re.findall('var nexturl="(.*?)"', html)[0]
    # 图片url
    tupiandizhi = "http://p0.xiaoshidi.net/{}".format(imgs)
    return tupiandizhi, title, next_url