#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('struct test 切记千万不要自己写一个strut.py文件这样会报错的!!!!')

import struct  ## 这个还需要再看看

print(struct.pack('>I', 10240099))


import hashlib  ##  这个提供的是一个MD5 sh1
                # 的加密工具

zhang = 'zhang'
md5 = hashlib.md5()
md5.update('zhang'.encode('utf-8'))
print(md5.hexdigest())
    # 数据量比较大的时候就多次上传
md5.update('xianqiang'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('zhang'.encode('utf-8'))
print(sha1.hexdigest())

import itertools

# itertools 的count()会生成一个无限迭代器
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)    #  1 2 3 4 5 6 7 8....as

# cs = itertools.cycle('abc')
# for c in cs:
#     print(c)  #  A B C A B C A ....

# 如果不提供后面的参数 告诉循环次数 那么久无线循环了
# ns = itertools.repeat("zhang", 3)
# for n in ns:
#     print(n)

# 无限序列会只有在for循环的时候才会无限的循环下去
# 可以用takewhile()等函数根据条件来街去除一个有限序列

natualsTake = itertools.count(1)
nsTake = itertools.takewhile(lambda x: x <= 10, natualsTake)
print(list(nsTake))  # 输出结果是 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# chain()
for c in itertools.chain('ABC', 'XYZ'):
    print(c)    # A B C X Y Z


# groupby()
for key, group in itertools.groupby('AAABBBCCAA'):
    print(key, list(group))

for key, group in itertools.groupby('AAAbbCCccDD', lambda x: x.upper()):
    print(key, list(group))


# 注意itertools 模块提供的全部都是处理迭代功能的函数, 返回的不是list 而是Iterator 只能用for 循环来迭代的时候才真正计算.

# strt = 'zhang'   # list  和 str 相互之间的转换
# print(list(strt))
# listt = ['z', 'h', 'a', 'n', 'g']
# print(type(str(listt)))
# listtt = list(listt)
# print(listtt)





