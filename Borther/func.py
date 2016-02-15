#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

print(abs(-10))

print(max(1, 2, 3, 4, 5, 6, 7))

# 类型转换
print(int("1234"))
print(int(12.3455))
print(float("12.44"))
print(str(12.34))

strrrr = "strgggg"
# <class 'str'>
print(type(strrrr))

# 起一个别名 后面不能带那个 () 有了 () 相当于是执行这个函数 没有就是赋值了
a = abs
print(a(-1))

str1 = str(hex(100))
print(str1)
print(type(str1))

# 自定义一个函数 我靠了 这个下面要空两行啊 ?? 要不还有警告~? WTF.


def my_abs(x):
    if x >= 1:
        return x
    else:
        return -x

print(my_abs(-5))


# 定义了一个什么都不做的函数


def nooop():
    # 这个貌似是这个返回空的意思 返回的函数结果是 None
    pass


print(nooop())

# 检查参数的类型


def my_abs_add(x):
    if not isinstance(x, (int, float)):
        # raise 让程序报错~

        raise TypeError('bad operand type')

    if x >= 0:
        return x
    else:
        return -x

print(my_abs_add(3))


def myfunc(x, y, z):
    return x, y, z

# 返回多个值其实可以是一个元组的形式 其实下面的r 就是一个元组
r = myfunc(1, 2, 3)
print(r)


def power(x):
    return x*x


def powerr(x, n):

    s = 1
    while n > 0:

        n -= 1

        s = s * x
    return s

print(powerr(2, 50))

# 这个函数里面提供了一个默认的参数 n= 2 如果默认参数放在了前面那么就会有 non-default argument follows default argument
# 只有一个参数 并且这个提供了默认参数时候这个是可以的.

# def powerrr(n=2, x):
#     s = 1
#     while n > 0:
#         n -= 1
#         s = s * x
#     return s


def powerrr(x, n=2):
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return n

########## 下面是函数的参数默认参数 #############

# 1.函数要是提供默认参数 必须是不可变的参数 如果传入了可变参数那么这个参数会在多次调用的时候变化(尝试多次调用tip1) 函数貌似记录了上次的结果
# 2.函数提供了如果按照顺序写那么默认参数可以不用写对应的名字 如果是要跳过某一个后面的还是用默认的参数那么需要写上这个
#   参数的名字.(tip2 中就是用了默认的age 但是后面的city要写上的其实这个很简单)

# tip1


def add_end(L = []):
    L.append('End')
    return L
print(add_end())
print(add_end())
print(add_end())
print(add_end())
# tip2

# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
# enroll('Adam', 'M', city='Tianjin')


# 3.想要改进tip1 上面的例子 可以用下面的方法 定义一个不可变的变量 注意这里面的is是用来判断的 这个和 swift 一样哦

def add_end_tip1(L=None):
    if L is None:
        L = []
    L.append("End")
    return L

print(add_end_tip1())
print(add_end_tip1())
print(add_end_tip1())
print(add_end_tip1())


# 声明可变参数的方法,可变参数其实内部接收到的是一个tuple

def calc(*number):

    summ = 0

    for n in number: # 因为接收到的书一个tuple 所以才能这么干.

        summ = summ + n*n

    return summ

print(calc(1, 2, 3, 4, 4, 6))
print(calc(1, 2, 3))
print(calc())


# 如果已经有了一个list 或者是tuple那么掉用一个可变参数的函数时候可以在前面加上
# *来表示让这个list 或者是 tuple 里面的元素都变成可变的传入到可变参数里面.

numbers = (1, 2, 2)
numberss = [1, 2, 3]
print("numbers 的结果是:", calc(*numbers))
print("numberss 的结果是:", calc(*numberss))

# 关键字参数 (**kw) 这个参数是允许传入0个或者任意个参数这些参数在函数内部自动组装成一个dict(上面是组装成了tuple)
# 这个的应用场景一般是有必填选项和其他信息,这个**kw就是其他的一些信息


def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)

person("zhang", 27)
person("zhang", 27, city="beijing")
person(location="zhongguo", name="zhang", age=2) # 这个虽然看着是一样但是name,age还是原来的那种具体看输出


# 想要检测一个参数是不是存在那么可以是这样的方式

def person_check(name, age, **kw):
    if 'city' in kw:
        # 有这个参数
        pass


# 下面的方式是直接弄一个extra的dict 直接转换为关键字参数传进去了


extra = {'city': 'beijing', 'job': 'Engineer'}
person('jack', 24, **extra)


# 命名关键字参数 中间有一个 * 这个后面的参数必须是带有名字的参数 如果调用时候不添加参数那么报错

def person_xing(name, age, *, city, job):
    print(name, age, city, job)

# person_xing('zhang', 27, 'beijing', 'IT') this is wrong below is right
person_xing('zhang', 27,city='beijing', job='It')


# 参数的组合形式  参数的组合形式  可变参数不能和命名关键字参数混合 其他的都能混合使用 注意
# 顺序是 必选参数 默认参数 可选参数/命名参数 关键字参数


def f1(a, b, c=0, *args, **kw):
    print(a, b, c, args, kw)


# def f2(a, b, c=0, *, d, **kw):
#     print(a, b, c, d, kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 这两种调用的方式要好好的理解一下 是按照顺序一个一个的赋值的

args = (1, 2, 3, 4)
kw = {"d": 99, "x": "#"}

f1(*args, **kw)

argss = (1, 2, 3)
kww = {"d": 99, "x": "#"}

f2(*argss, **kww)

# 这样看来其实任意的函数都是能通过 func(*args, **kw)的方式进行调用.
# f2(*args, **kw) 刚才这个错了出的错误信息是 takes from 2 to 3 positional arguments but 4 positional arguments
# 这个问题也挺简单 就是说 这个地方的第四个参数已经是一个命名关键字参数了,而这里面有4个参数 所以不合法了

