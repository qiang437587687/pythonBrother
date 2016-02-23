#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print("枚举")

from enum import Enum, unique

Month = Enum('Month', ('J', 'F', 'M', 'A', 'S'))

print(Month.M)

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
#
# J => Month.J , 1
# F => Month.F , 2
# M => Month.M , 3
# A => Month.A , 4
# S => Month.S , 5
#


@unique  # 这个是帮助我们检查是不是有重复值的(保证没有重复值) #例如下面的这个sat 重复 了就会报错Attempted to reuse key: 'Sat'
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
    # Sat = 7


print('Weekday.sat', Weekday.Sat, Weekday.Sat.value)

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Tue)
print(Weekday(1))
print(day1 == Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member, member.value)




# 元类 type()  当前可能看不懂这块 还需要看教程的


class Hello(object):

    def hello(self, name='world'):
        print("hello, %s" % name)

print(type(Hello))
h = Hello()
print(type(h))

# type() 黑魔法 创建一个类 不使用 class

#  先定义一个函数 这个就是 下面定义里面的函数 不过名字不是fn了
def fn(self, name='zhang'):
    print(name)

#  需要3个参数 第一个是类的名字 第二个是继承的类是哪一个 这个地方是一个元组 可以继承多个
#  第三个 是类里面的方法也就是hello方法相当于调用fn函数
HHlo = type('HHlo', (object,), dict(hello=fn))
hh = HHlo()
hh.hello()

print(type(HHlo))
print(type(hh))


#  metaclass
#  定义习惯 metaclass 的类名总是以Metaclass的形式结尾以便表示这就是一个metaclass
#  metaclass 是类的模板 所以必须冲type类型派生

class ListMetaclass(type):

    # __new__() 方法接受的参数依次是 1 当前准备创建类的对象  2 类的名字  3 类继承的父类合计 4 类的方法合集

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 创建一个类 这个类继承于list 指定通过metaclass来进行创建
class MyList(list, metaclass=ListMetaclass):
    pass























