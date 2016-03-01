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

# 获取 10个页面 的url
urllist = []
for i in range(1, 20 + 1):
    str = ('http://s.5173.com/search/0ba72c47be2a46eeac63bf45d336b0ba-0-4cqwjk-b4mmjy-0-ltqp2z-0-0-0-a-a-a-a-a-0-0-0-%d.shtml' % i)
    urllist.append(str)
# print(urllist)

# 打开或者是创建文件

file = open('/Users/zhangxianqiang/Desktop/pythonBrother/Borther/ReStartLearn/5173.txt', 'w')
file.truncate() # 清空文件(每一次请求上一次就没用了那么就清空)
# fw.close()
# file = open('/Users/zhangxianqiang/Desktop/pythonBrother/Borther/ReStartLearn/5173.txt', 'a')

# xpath 爬取过程
def worm5173(url):

    str = '----------------第%d页----------------\n' % (urllist.index(url) + 1)  # 使用多线程爬取那么界面的页数是不准的!!!
    print(str)
    file.write(str)

    html = requests.get(url)
    # print(html.text)
    selector = etree.HTML(html.text)

    content = selector.xpath('/html/body/div[3]/div[2]/div[4]/div[2]/div[1]/div')  # 要取到单个的项目 div 但是div 返回到数组里面
    #
    # content = selector.xpath('/html/body/div[3]/div[2]/div[4]/div[2]/div[1]/div[1]/ul[1]/li[1]/h2/a/text()')
    # print(content)
    # print(type(content))
    # print(len(content))

    for each in content:
        text = each.xpath('ul[1]/li[1]/h2/a/text()')  # 这个开头前面不要多一个 / 加上是有错误的.
        text2 = each.xpath('ul[@class="pdlist_price"]/li/strong/text()')
        # print(text[0] + ' --------> ' + text2[0] + '元')
        file.write(text[0] + ' --------> ' + text2[0] + '元\n')  # 添加到文件.

# 逐个循环10url个爬取数据 (顺序是一定的 但是比多线程慢多了)

for url in urllist:

    worm5173(url)

file.close()  #file 用完了之后close()


# 多线程方式来实现一下爬取过程

# from multiprocessing.dummy import Pool as ThreadPool  # 这个是视频里面弄的 as 的作用就是起一个别名?
#
# pool = ThreadPool(4)
#
# results = pool.map(worm5173, urllist)
#
# pool.close()
#
# pool.join()

# 简单尝试一下多线程 (这样子和上面的引用方式是一样的)
# from multiprocessing import Pool
#
# poolCurrent = Pool(4)
#
# results = poolCurrent.map(worm5173, urllist)
#
# poolCurrent.close()
#
# poolCurrent.join()
#
# file.close()  #file 用完了之后close()

# 采用多线程的方式抓取的过程 应该是会快一点(具体没测可以添加time来测试) 但是顺序就不是正确的顺序了.



