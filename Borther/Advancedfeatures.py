#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print("开始学习高级特性")

# 切片

# 切片来说注意这个的结果可不是 1 的位置开始 长度是2 而是 开始位置到结束位置.这个和iOS是有点不一样
L = ['M', 'S', 'Z', 'H', 'X']

print('Slice结果:', L[3:4])
print('Slice结果:', L[:2])

# 倒数开始的元素索引是 -1  # 倒数的位置

print('倒数的slice的结果是:', L[-1]) # 注意这里面如果是范围那么里面的分割符号应该是 :

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
print('倒数的一个str2', str2[-2: -1]) # 这个就表示 是一个-2 开始 -1结束的区域不包含后面的数字区域.
#  2.15 简单的 总结一下切片操作   就是对于一个 list(包含tuple, str)的操作 形式就是 [:] 可以写上负数代表从后往前


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
for x in range(1, 11):
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


# 2.15 简单写一下列表生成器

print('列表1 直接转换为list的方式', list(range(1, 11)))
print('列表2 for循环的形式')
list22 = []
for x in range(1, 11):
    list22.append(x*x)
print('list22 = ', list22)

print('列表3 类似匿名函数的形式 其实可以借鉴列表2的方法')
list33 = [x for x in range(1, 11) if x > 5]
print(list33)

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


# 2.15 看一下

listo = [x*x for x in range(1, 18) if x > 10]
print('方式1 这样的一个listo 就是一个生成器, 用到哪里就生成到哪里 因为是print 所以会全部有用的元素都会用到', listo)

print('方式2 就是一个函数含有一个yield的函数就是一个生成器')
def listOdd():
    print('step111')
    yield 1
    print('step222')
    yield 2
    print('step333')
    yield 5
oo1 = listOdd()
oo2 = listOdd()
print(next(oo1))  # 这两个的结果是一样的 说明他们是不同的对象
print(next(oo2))

print(next(oo1))
print(next(oo2)) # 记住 yield 就是返回值 下一个yield 是下一次的返回值

# 下面的这个是想输出一个数列 一个 n!

def nDown(max):
    n = 1
    # b = 0
    while n < max:

        yield n
        n += 1
    return 'down ok'

# 这是一个生成器  还没有循环的机制呢

def giveMeDown(max):
    for x in nDown(max):
        print(x)

print('nDown(100) => ', giveMeDown(10))
print('成功了O(∩_∩)O哈哈~')

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



s = '%d000%s' % (100.111, 'zhang')
print(s)


