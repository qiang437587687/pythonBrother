#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# map

def f(x):
    return x * x

r = map(f, [1, 2])
list1 = list(r)
print(list1)


# 还可以这么玩
print(list(map(str, [1, 2, 4, 5, 6])))


# reduce
from functools import reduce


def add(x, y):
    return x + y

print(reduce(add, [1, 2, 3, 4]))

print(sum([1, 2, 3, 4, 6]))

# 其中 lambda x, y: x * 10 + y 和 下面定义的函数是一样的作用!!!!

def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 2, 3, 4, 5]))

print(reduce(lambda x, y: x * 10 + y, [1, 2, 3, 4, 5]))


# filter 过滤函数接收的函数是过滤的条件

def is_odd(n):
    return n % 2 == 1

list3 = [1, 2, 3, 4, 5, 6, 7, 8, 0]
listT = list(filter(is_odd, list3))
print(filter(is_odd, list3))
print(listT)
print(list3)

list4 = ['2', '3', '4']

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, list4)))


def _not_divisible_temp(n):
    def temp(x):
        return x % n > 0
    return temp
print("_not_divisible_temp(n) = ", _not_divisible_temp(3))


def func(x):
    return x > 500


def _odd_iter():
    n = 1
    while True:

        n += 2
        yield n

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible_temp(n), it) # 构造新序列

def _not_divisible(n):
    return lambda x: x % n > 0

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

# 这个居然是反转字符串 好神奇~

str = "zhang"
print(str[::-1])

# 修饰器 Decorator


# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

import functools

def log(func):
    @functools.wraps(func) # 这个的作用是 为了后来的func.__name__ = func 而不是wrapper
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 加上这个能在调用这个函数之前先调用一次log
@log
def Dfunc():
    print("zhang")


f = Dfunc
print(f.__name__) # 如果上面不加上 @functools.wraps(func) 那么这里面输出的是wapper 加上输出的是Dfunc


# 偏函数  这个就是为了方便 创建一个函数带有别的参数

print(int('1345', base=16)) # 转换为 16 进制的数字

# 可以用这种方式来代替
def int16(m):
    return int(m, base=16)

# 偏函数可以这么用

int8 = functools.partial(int, base=8)
print(int8("23456"))

# 实际上就是这么回事
kw = {"base": 8}
print(int("23456", **kw))


print(max(1, 2))

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))

# 上面这个相当于是这样的
args = (10, 5, 6, 7)
print(max(*args))