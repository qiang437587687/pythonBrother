#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

print('Second Spider')


# if __name__ == '__main__':
#
#     classinfo = []
#     url = 'http://www.jikexueyuan.com/course/?pageNum=1'
#     jikespider = spider()
#     all_links = jikespider.changepage()

# 豆瓣悬疑电影
url = 'http://movie.douban.com/typerank?type_name=%E6%82%AC%E7%96%91&type=10&interval_id=100:90&action='
# url = 'http://www.qiushibaike.com'
headers = {'User-Agent': 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25'}
# 添加一个 headers
html = requests.get(url, headers=headers)
# html2 = requests.get(url)
print(html.text)

sr = r'<span class="movie-name-text">.*?</span>'

# sr = r'<span class="movie-name-text"> <a herf=".*?">(.*?)</a>'

moiveName = re.findall(sr, html.text, re.S)

print('moiveName list', moiveName)

for each in moiveName:
    print(each)
















