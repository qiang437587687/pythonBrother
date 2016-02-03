#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("正则表达式")

# \s可以匹配一个空格  \d 数字   \w 字符或者数字

s = r'ABC\-011' # 前面加上r 是因为 正则和python 里面都是用 \做转义 所以 添加一个r 证明是正则


import re

# 匹配成功是返回的一个 match对象 匹配不成功返回None
print(re.match(r'^\d{3}\-\d{3,8}', '010-123456'))   # <_sre.SRE_Match object; span=(0, 10), match='010-123456'>
print(re.match(r'^\d{3}\-\d{3,8}', '010 123456'))   # None

if re.match(r'\d{0,3}\-\w{5}', '3-zhang'):
    print('匹配成功')
else:
    print('匹配失败')


# 用正则来分割字符串

restr = 'a   b    c'
restr1 = 'a,b, c  d'
    # 正常分割
print(restr.split(' '))   # ['a', '', '', 'b', '', '', '', 'c']
    # 正则分割
print(re.split(r'\s+', restr))   # ['a', 'b', 'c']

print(re.split(r'[\s\,]+', restr1)) # ['a', 'b', 'c', 'd']




# 分组功能
    #用正则去提取子串 用 ()表示的就是要提取分组 Group

rem = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

if rem:
    print('(\d{3})-(\d{3,8})$ 匹配成功')

print(rem.group(0))     #  group0 里面的永远是原始的字符串
print(rem.group(1))     #  第一组也就是010
print(rem.group(2))     #  第二组也就是12345
# print(rem.group(3))   #  超过限制会报错




# 贪婪匹配 (也就是 正则会尽量多的匹配符合的选项)

print('采用贪婪匹配:', re.match(r'^(\d+)(0*)$', '102300').groups())   # ('102300', '') 也就是说 \d+ 采用了贪婪匹配方式
print('禁止采用贪婪匹配方式', re.match(r'^(\d+?)(0*)$', '102300').groups())  # 禁止采用贪婪匹配方式 ('1023', '00')


# 采用预编译的方式 能节省正则的重复次数  也比较清晰

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')  #  一般写到上面哦~~~
print(re_telephone.match('010-10000').groups())






















