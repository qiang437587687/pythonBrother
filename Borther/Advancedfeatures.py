#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print("开始学习高级特性")

# 切片

# 切片来说注意这个的结果可不是 1 的位置开始 长度是2 这个和iOS是有点不一样
L = ['M', 'S', 'Z', 'H', 'X']

print('Slice结果:', L[0:2])
print('Slice结果:', L[:2])

# 倒数开始的元素索引是 -1
print('Slice结果:', L[-2:-1])
print('Slice结果:', L[-2:])

LL = list(range(99))
print(LL[:10])

# 复制一个LL
LL[:]


# tuple 本质上也是一种list 不可变 tuple也可以切片操作 操作完成也是tuple

ruple1 = (1, 2, 3, 4, 5)
print(ruple1[1:2])


# 字符串也是能用这个方法来做的
str2 = 'ABCDEF'
print(str2[1:4])


# 迭代

# 字符串迭代方式

for S in str2:
    print(S)

dictt = {'a': "1", 'b': "2", 'c': "3"}

for key in dictt:
    print(key)
    print(dictt[key])

for value in dictt.values():
    print(value)

for k, v in dictt.items():
    print(k)
    print(v)


# 列表生成器

# 创建一个列表的方法
# 方法1
list1 = list(range(1, 11))
print(list1)

# 方法2
L = []
for x in range(1,11):
    L.append(x*x)
print(L)

# 方法3 列表生成器

print([x*x for x in range(1, 11)])
print([x*x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'abc' for n in 'xyz'])
print([k + "=" + v for k, v in dictt.items()])

stt = 'ABCD'
sttList = ([v for v in stt])
print(sttList)
print([s.lower() for s in sttList])
print([s.upper() for s in sttList])


# 这个算一个练习题吗?
L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s, str)])



# 生成器 generator


L3 = [x * x for x in range(10)]
# 这个就是一个生成器了 前面是一个list 这个是一个 generator 可以通过next() 函数来打印 G3里面的数据
G3 = (x * x for x in range(5))
G4 = (x * x for x in range(3))

print(G3)
print("------", next(G3))
print(next(G3))

# 这个生成器就是用到哪里生成到哪里
for n in G3:
    print("for in ", n)

print("------")

for n in G4:
    print(n)


# 其中含有yield 关键字的就是 一个generator yield 这个就是返回的值.
def odd():
    print('step1')
    yield 1
    print('step2')
    yield 3
    print("step3")
    yield 5

o = odd()
print(next(o))
print(next(o))
print(next(o))

# next(o) # StopIteration

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:

        yield b
        a, b = b, a+b
        n = n + 1
    return "done"

f = fib(6)
print(f)

for n in fib(6):
    print(n)



# 开始一个小练习  杨辉三角  ----> 不会做 囧~


# def zib(number):
#
#     n = 0
#     m = 1
#     while n < number:
#
#         if n == 0 or n == number-1:
#             yield 1
#
#         yield m
#     m = number
#     n += 1
#
# z = zib(6)
#
# for n in z:
#     print(n)

from collections import Iterable
# 迭代器 可以调用 next() 函数并且不断返回 最后抛出 StopIteration 的称之为迭代器
print(isinstance([], Iterable))


listD = [1, 2, 3, 4, 5]

# tip a
for x in listD:
    pass

# tip b
it = iter(listD)
while True:
    try:
        x = next(it)

    except StopIteration:

        break
# tip a 和 tip b 其实是一样的





