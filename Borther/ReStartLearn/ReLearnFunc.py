#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
# 空函数

def test1():
    pass

test1()


def test2():
    return 1, 2

print(test2())  # 多个返回值返回的是元组.


def test3(x, n=2):
    print(x + n)

test3(1,)  # 函数默认参数  默认参数必须指向不变对象！ 不然会记录上一次的数据


def test4(*number):  # 可变参数  可变参数在函数调用时自动组装为一个tuple
    summ = 0
    for i in number:
        summ += i
    print(summ)
test4(1, 2, 3, 4)

list = [1, 2, 3, 4]
test4(*list)  # 这个方法和上面的差不多 注意 *把list 变成可变的了.


def test5(name, age, **kw): # 关键字函数 这个允许传入原本没有的对象 (必填选填的问题)
    print('name', name, 'age', age, 'other', kw)

test5('zhang', '19', city='beijing')
extra = {'city': 'beijing', 'job': 'engineer'}
test5('han', 24, **extra)



def test6(name, age, *, city, job): # 命名关键字函数必须传入 参数名
    print(name, age, city, job)

# test6('zhang', 19, city='yantai', school='chang') # 报错了
test6('zhang', 19, city='yantai', job='chang')

def test7(name, age, *, city ='beijing', job): # 命名关键字 可以有默认参数
    print(name, age, city, job)

test7('zhang', 19, job='chang')


tuplee = (1, 3, 4)
kww = {'nme': 'zhang'}

def test8(a, b, c, *k, **kw):
    print(a, b, c, k, kw)
test8(*tuplee, **kww)


# 装饰器

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


# 装饰器的作用 这里相当于是执行了 函数 log(name)
# 这样就是调用这个函数执行的相当于是 调用这个now 执行的是log中返回的wrapper
@log
def now():
    print('12345')

print(now.__dir__())
print(now.__name__)     # wrapper 这个时候调用的 name 是wrapper 因为返回的是wrapper

now()  # call now():12345


def Tlog(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@Tlog
def Tnow():
    print('12355')

print(Tnow.__dir__())
print(Tnow.__name__)    # Tnow



# 偏函数 partial 定义一个新的函数 (相当于原来函数的扩展 这个实现的是 int 直接给一个默认值的操作.)

print(int('11111111', base=2))  # 输出int类型 (1111111 是一个二进制 转为int 类型)

int2 = functools.partial(int, base=2)

print(int2('11111111'))



