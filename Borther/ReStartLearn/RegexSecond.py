#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print('第二次学习一下正则')

import re

sercte_code = 'zfejdjsafkxxixxdaksflkafxxlovexxedfsdfsdfxxyouxxffffdf'

b = re.findall(r'xx.*xx', sercte_code)    # ['xxixxdaksflkafxxlovexxedfsdfsdfxxyouxx']
                                          # 这个返回的是一个 list 里面只有一个元素 .*的方式是贪婪匹配
c = re.findall(r'xx.*?xx', sercte_code)   # ['xxixx', 'xxlovexx', 'xxyouxx'] 加上一个? 那么就是一个非贪婪匹配

d = re.findall(r'xx(.*?)xx', sercte_code) # ['i', 'love', 'you'] 上面的基础上添加一个括号就是代表着输出括号里面的内容

sercte_code2 = '''zfejdjsafkxxixxdaksflka
fxxlovexxedfsdfsdfxxyouxxffffdf'''

# re.S 这个的作用是让 . 的匹配范围(原本 . 的匹配范围是 except a newline)超过一行 也就是 .能够包括换行符(\n)
e = re.findall(r'xx(.*?)xx', sercte_code2, re.S)

print(b)
print(c)
print(d)
print(e)



# search 确定了需要的内容只有一个那么就用这个来搜索吧.可以提高效率.

s2 = 'asdfxxIxx123xxlovexxdfd'

f1 = re.search(r'xx(.*?)xx123xx(.*?)xx', s2).group(1) # 记住这里面的group是指的匹配中的括号对应的位置
f2 = re.search(r'xx(.*?)xx123xx(.*?)xx', s2).group(2)
# f3 = re.search(r'xx(.*?)xx123xx(.*?)xx', s2).group(3) #这个是会报错的
f4 = re.search(r'xx(.*?)xx123xx(.*?)xx', s2).group() # xxIxx123xxlovexx
print(f1)
print(f2)
print(f4)

f5 = re.findall(r'xx(.*?)xx123xx(.*?)xx', s2, re.S)

print(f5)  # [('I', 'love')] 是一个list 里面包含了元组 同时满足多个的时候list 里面会有多个元组.
print(f5[0][1])  # love

s = '123rrrrr123'
# 把满足 正则条件的 表达式 替换成后面的形式.
output = re.sub(r'123(.*?)123', '123%d234' % 789, s)
print(output)


#匹配纯数字

a = 'asdfgg123456dddd4444'
a1 = re.findall(r'(\d+)', a)
a2 = re.findall(r'(\d+?)', a)

print(a1) # ['123456', '4444'] 匹配纯数字 这种是贪婪匹配
print(a2) #  ['1', '2', '3', '4', '5', '6', '4', '4', '4', '4'] 非贪婪匹配.

