#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict的key必须是不可变对象。
d = {'michael': 76, 'zhang': 35, "xianqiang": 89}
d.pop('xianqiang')
print('输出结果是%s' % d)
print(d["zhang"])


    # 2.6 添加一下 dict 的创建方法

d1 = dict()
d1['a'] = 1
print('创建方式1(d1 = dict()):', d1['a'])

d2 = dict(a=1, b=2)
print('创建方式2(dict(a=1, b=2)):', d2['a'], d2['b'])

d3 = dict((('a', 1), ('b', 2)))
print('创建方式3dict = 元组的方式', d3['a'])

d4 = dict([('a', 1), ('b', 2)])
print('和上面一个创建方式不过用了[]', d4['a'])


    #######

# set
s = set([1, 2, 3])
print(s)
s.add(4)
print(s)
# set 并不能重复添加元素
s.add(4)
print(s)

a = ['c', 'v', 'a']
a.sort(key=None) # 这里面的key 还需要再查询一下.
print(a)

# b 是一个变量 而 agc 是一个常量 因此b是有对应的一个replace方法的
# b = 'agc'
# print(b.replace('a', 'F'))
# print(a)

# 实际上replace方法返回了一个新的字符串 'Fgc' 并没有改变原来的b 指向的字符串
b = 'agc'
c = b.replace('a', 'F')
print(c)
print(a)
