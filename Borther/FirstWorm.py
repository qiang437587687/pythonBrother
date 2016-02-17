#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import requests
import logging

logging.basicConfig(level=logging.INFO)

html = requests.get('http://www.qiushibaike.com')
print('html.url ===> ', html.url)
# html.encoding = 'utf-8'
print('html encoding ===>', html.encoding)  # 注意不同的编码之间可能需要转换
# print(html.text)  # requests 直接get一个html

tr = r'<div class="content">(.*?)<!'
# tr = r'title'

# A = ASCII = sre_compile.SRE_FLAG_ASCII # assume ascii "locale"
# I = IGNORECASE = sre_compile.SRE_FLAG_IGNORECASE # ignore case
# L = LOCALE = sre_compile.SRE_FLAG_LOCALE # assume current 8-bit locale
# U = UNICODE = sre_compile.SRE_FLAG_UNICODE # assume unicode "locale"
# M = MULTILINE = sre_compile.SRE_FLAG_MULTILINE # make anchors look for newline
# S = DOTALL = sre_compile.SRE_FLAG_DOTALL # make dot match newline
# X = VERBOSE = sre_compile.SRE_FLAG_VERBOSE # ignore whitespace and comments

# re.S 在字符串中，包含换行符\n，在这种情况下，如果不使用re.S参数，则只在每一行内进行匹配
# 如果一行没有，就换下一行重新开始。而使用re.S参数以后，正则表达式会将这个字符串作为一个整体，在整体中进行匹配

chinese = re.findall(tr, html.text, re.S)

# logging.info('chinese print is >>> %s ' % chinese)

list1 = ['zhang', '222']
# print(str.count())   # 这不是ios  数组list也不能 用 count  要用len(list) 的方式求长度
print(len(chinese))

for each in chinese:
    print(each)

# 现在取出来了 保存到一个txt文件里面
fw = open('/Users/zhangxianqiang/Desktop/pythonBrother/Borther/FirstWorm.txt', 'w')
for each in chinese:
    print(each)
    fw.write(each)
fw.close()






