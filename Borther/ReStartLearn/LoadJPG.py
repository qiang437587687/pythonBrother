#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''

这里面学到的东西 总结一下吧, 还是遇到一点困难的.
1. 下载的东西存储到文件里面的方式 基本上就是 html.content
   然后调用 with open(filepath) as file:  file.write(html.content)
   注意其中的 with 方法  和 try catch的对比
2. 网页的编码问题 这个用chrome 找到对应的一个 编码格式 gb2312 这样的 不知道为啥都写成 gbk去解析.html.content.decode('gbk')
   注意这个里面是content 如果是用urllib 这样的话应该是 html.read() 这样的一个方式去读文件和修改对应的编码问题.
   然后直接就操作就行了 并不需要进一步的 utf-8 的操作 这个可能是是 python3 自动编码为 utf-8 有关系吧.
3. 针对这个界面解析的url 来说似乎不太适合用 xpath 这样的方法  因为 每个页面都是直接获取了 全部的数据内容
'''


'''
网上 看来的三种下载文件的方法
import urllib
import urllib2
import requests
print "downloading with urllib"
url = 'http://www.pythontab.com/test/demo.zip'
print "downloading with urllib"
urllib.urlretrieve(url, "demo.zip")

import urllib2
print "downloading with urllib2"
url = 'http://www.pythontab.com/test/demo.zip'
f = urllib2.urlopen(url)
data = f.read()
with open("demo2.zip", "wb") as code:
    code.write(data)

import requests
print "downloading with requests"
url = 'http://www.pythontab.com/test/demo.zip'
r = requests.get(url)
with open("demo3.zip", "wb") as code:
     code.write(r.content)

'''



"""
这里是重新理解一下with 的相关用法

eg1:

file = open("/tem/foo.txt")
data = file.read()
file.close()

eg2:
file = open("/tem/foo.text")
try:
    data = file.read()
finally:
    file.close()

eg3:
with open("/tem/foo.txt") as file:
    data = file.read()


"""


import requests


# 下面是一个 写文件的 demo

path = '/Users/zhangxianqiang/Desktop/pythonBrother/Borther/ReStartLearn'

url = "http://pic2.sc.chinaz.com/files/pic/pic9/201309/apic520.jpg"

name = '/Users/zhangxianqiang/Desktop/pythonBrother/Borther/ReStartLearn/1.jpg'

conn = requests.get(url)

with open(name, 'wb') as code:
    code.write(conn.content)


# 下面打算 爬取 181 上面 的一个专辑的image文件 然后写到文件里面
# 181.52pk.com


from lxml import etree
import logging

logging.basicConfig(level=logging.INFO)


# http://181.52pk.com/gif/6653164.shtml#image0
urlList = []
for i in range(1, 100 + 1):
    str = ('http://181.52pk.com/gif/6653164.shtml#image%d' % i)
    urlList.append(str)


#  保存的文件夹 /Users/zhangxianqiang/Desktop/181pic


# 这个path 去出来 之后全部都是 []
# def worm181(url):
#     html = requests.get(url)
#     selector = etree.HTML(html.text)
#
#     content = selector.xpath('/html/body/div[6]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/img')
#     name = selector.xpath('/html/body/div[6]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]')
#
#     print(url, content, name)

# for url in urlList:
#     worm181(url)
#     print('-------------')

import re


def worm181():  # 用这则匹配一下

    # view-source:http://181.52pk.com/gif/6653164.shtml#image45
    html = requests.get('http://181.52pk.com/gif/6653164.shtml#image45')

    content = html.content.decode('gbk')  # 难道gb2312 要直接写成gbk才行??

    # html.encode('utf-8')

    # tr = r'<div class="content">(.*?)<!'
    # print(html.text)
    # textt = html.decode('gb2312')
    # textt = textt.encode('utf-8')
    # html.decode("utf-8")
    # html.decode('gb2312')

    chinese = re.findall(r'{"id":0,"title":"(.*?),"bigImgPath"', content, re.S)

    for urll in chinese:
        listr = re.split('"originImgPath":"', urll)
        urll = listr[1].rstrip('"')   # 这个函数很吊啊. 直接能去掉 头和尾  strip  lstrip rstrip
        namesss = re.split('","', listr[0])[0]
        # print(len(namesss))
        # print(type(namesss))
        print(namesss)
        # 写到文件里面
        connn = requests.get(urll)
        pathh = '/Users/zhangxianqiang/Desktop/181pic/%s.gif' % namesss
        with open(pathh, 'wb') as codd:
            codd.write(connn.content)

worm181()  # 调用~

# import urllib.request
# import codecs
#
#
# #获取网页HTML信息
# url='http://181.52pk.com/gif/6653164.shtml#image45'
# html=urllib.request.urlopen(url)
# content=html.read().decode("gb2312")
# html.close()
#
# #通过正则匹配，获取图片链接
# img_tag=re.compile(r'data-url="(.+?\.gif)"')
# img_links=re.findall(img_tag, content)
#
# #下载图片 img_counter 为图片计数器
# img_counter=0
# for img_link in img_links:
#     img_name='%s.jpg'%img_counter
#     urllib.request.urlretrieve(img_link,"E:/邓肯/%s" %img_name)
#     print('正在下载第%d张图片'%(img_counter+1))
#     img_counter+=1
#
# if img_counter==0:
#     print('下载失败')
# else:
#     print('共下载了%d张图片'%(img_counter))


