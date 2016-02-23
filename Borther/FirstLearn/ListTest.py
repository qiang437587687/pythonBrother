#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('list test')

list = ['zhang', 'xian', 'qiang', 'han', 'xiu', 'juan']


list.append('abc')

list.pop()

del list[2]  #下面这两个实验室一样的
list.pop(2)

print(list)

print(len(list))

print(list[1:2])

print(list[::-2])

list2 = ['XYZ', list]

print('list[1][1]', list2[1][0]) # 相当于二维数组


# tuple

tuple = (1, 2)

tuple1 = (1, )  #88i8 7这样是一个tuple  (1) 这个就是一个1

print(tuple[1])







