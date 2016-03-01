#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
tip : 1. //      定位根节点
tip : 2. /       往下层寻找
tip : 3. /text() 提取文本内容  其实就是把其中的内容转换为 str
tip : 4. /@xxx   提取属性内容
"""

from lxml import etree
import re
import requests
import logging
import json
logging.basicConfig(level=logging.INFO)

# import sys
# reload(sys)
# sys.setdefaulten

html = requests.get('http://www.qiushibaike.com')

# html2 = requests('GET', 'http://www.qiushibaike.com')

# print(html.text)

selector = etree.HTML(html.text)

content = selector.xpath('//*[@id="content-left"]/div')

print(type(content))
print(len(content))
# print(content)
print('------')

for each in content:

    cc = each.xpath('div[@class="content"]/text()')  # 在查找出来的那些 div 依次寻找content  # 这里面解析出来的内容 遇到节点(<br>等)分离其中的元素了
    # print('out cc %s' % cc)
    if len(cc) >= 1:
        # cc.replace('\n', '')
        # cc.replace('\n', 'python')

        dd = []

        for str in cc:
            # print('str first %s ' % str)
            # print(len(str))
            str = str.strip('\n')
            dd.append(str)
            # print('str after %s ' % str)
            # print(len(str))

        # print('in cc %s' % cc)

        print('\n'.join(dd))

        # print(json.loads(cc[0]))
        # print(json.loads(cc[0].replace('<br>', '')))
        # print(json.loads(cc[0].replace(' ', '')))

    # print(type(dd))
    # print(len(dd))
    # print(dd)


# //*[@id="qiushi_tag_115320313"] //*[@id="content-left"] //*[@id="qiushi_tag_115320313"]
# //*[@id="qiushi_tag_115320313"]/div[2]  article block untagged mb15  //*[@id="qiushi_tag_115320153"]/div[2]





# xpath 学习

lhtml = '''
<?xml version="1.0" encoding="ISO-8859-1"?>

<bookstore>

<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>

<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

</bookstore>
'''

lselector = etree.HTML(lhtml)

content1 = lselector.xpath('bookstore') # 选取此节点的所有子节点
# content1 = lselector.xpath('/html') # 从根节点开始选取(绝对路径). 感觉一般不会这么干
# content1 = lselector.xpath('//section')      # // 表示从后面的开始选择  不管位置.

# content1 = lselector.xpath('//section/.')      # // .选取当前节点
# content1 = lselector.xpath('//section/..')      # //.. 表示选择上层节点



print(type(content1))
print(len(content1))
for each in content1:
    print(each.text)






