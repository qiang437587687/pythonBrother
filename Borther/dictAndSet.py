#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# dict的key必须是不可变对象。
d = {'michael': 76, 'zhang': 35, "xianqiang": 89}
d.pop('xianqiang')
print('输出结果是%s'%d)
print(d["zhang"])

# set
s = set([1, 2, 3])
print(s)
s.add(4)
print(s)
# set 并不能重复添加元素
s.add(4)
print(s)

a = ['c', 'v', 'a']
a.sort()
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
