#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 尝试一下引入另外一个model里面的函数

from FirstLearn.func import my_abs
print('引用了上面的func 就把里面所有的打印都在这个module里面打印出来了这个真的合理吗?')
print('my_abs(-2)', my_abs(-2))

names = ['zhang', 'han']
for name in names:
    print(name)

# range 提供一个 函数用来 生成一个序列是 0 1 2 list声明为这个是一个是数组
print(list(range(3)))

sumnumber = 0
for x in range(101):
    sumnumber = sumnumber + x
print(sumnumber)

# 2.15 这个看完了~


