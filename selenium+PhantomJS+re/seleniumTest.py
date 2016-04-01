from selenium import webdriver
import re
diver = webdriver.PhantomJS()

diver.get('http://www.qiushibaike.com/')

# print(type(diver.page_source))

# print(diver.page_source)

html = diver.page_source

tr = r'<div class="content">(.*?)<!'

chinese = re.findall(tr, html, re.S)

print(len(chinese))

for each in chinese:
    print(each)

# fw = open('/Users/zhangxianqiang/Desktop/qiushi.txt')

with open('/Users/zhangxianqiang/Desktop/qiushi.txt', 'w') as fw:
    for each in chinese:
        fw.write(each)





