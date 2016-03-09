#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

print('重新学习一下基础语法 这里面是实现的一个栈')

for i in range(0, 100):
    print('item %d' % i)

print('')


# 实现一个栈

class Stack():
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1

    def Full(self):
        if self.top==self.size:

            return True
        else:
            return False


    def Push(self, content):
        if self.Full():
            print('stack is full!')
        else:
            self.stack.append(content)
            self.top = self.top + 1

    def Empty(self):
        if self.top == -1:
            print("stack is empty!")
            return True
        else:
            print('stack Not empty')
            return False

    def Out(self):
        if self.Empty():
            print('empty')
            return None
        else:
            self.top = self.top - 1
            return self.stack[self.top]


q = Stack(3)
q.Empty()

q.Push('hello')
q.Empty()

print(q.Out())



# 检测一个 list 的使用

list31 = ['zhang', 'xian', 'qiang', 'han', 'xiu', 'juan']

list312 = []

for str in list31:
    print(list31.index(str))
    # list31[1] = 'dabao'
    list31[list31.index(str)] = 'dabao'
    print(list31)
    list312.append(str)
'''
1.index 可以取到对应的元素在数组中的位置
2.后面的参数 第一个是 规定起始的位置 第二个是规定结束的位置
'''
print(list31)
print(list312)



sssss = '1234567890123'

print(re.split(r'[27]', sssss))

print(sssss.split('2'))
# print(sssss.split('2 or 3'))















