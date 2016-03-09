#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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



def worm181(url):

    html = requests.get(url)
    selector = etree.HTML(html.text)

    content = selector.xpath('/html/body/div[6]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/img')
    name = selector.xpath('/html/body/div[6]/div[2]/div[2]/div/div/div[1]/div[1]/div[2]/div[1]')

    print(url, content, name)



# for url in urlList:
#     worm181(url)
#     print('-------------')

import re

def worm181():

    # view-source:http://181.52pk.com/gif/6653164.shtml#image45
    html = requests.get('http://181.52pk.com/gif/6653164.shtml#image45')
    # tr = r'<div class="content">(.*?)<!'
    print(html.text)
    chinese = re.findall(r'"id":0,"title":"(.*?),', html.text, re.S)
    print(chinese)
    print(len(chinese))
    print(chinese[0])


worm181()



