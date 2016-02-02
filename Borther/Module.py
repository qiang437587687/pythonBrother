#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import types

# 模块学习

'a test module'

__author__ = "zhang"


def test():

    args = sys.argv
    print('args = ', args)
    if len(args) == 1:
        print("Module")
    elif len(args) == 2:
        print("hello, %s!" % args[1])
    else:
        print('Too many arguments')

if __name__ == '__main__':
    test()


#  上面是一个py的标准模板  下面是创建类和对象.

class Student(object):
    pass

print(Student())
print(Student)

# 这个地方居然能直接绑定一个属性  这个和 OC 的 KVO 差不多~?
zhang = Student()
zhang.name = "zhang"
print(zhang.name)

################# 怎么再次调出补全代码呢???##################


class StudentNeed(object):

    def __init__(self, name, locationCode = 50, score=90, private="QQ"):
        self.name = name
        self.score = score
        self.__private = private
        self.__locationCode = locationCode

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get__private(self):
        return self.__private


    # 这么做可以有效的检查一下传入的参数是不是正确的范围
    def set_locationCode(self, code):

        if not isinstance(code, int):

            raise ValueError("shoule be int type")

        if 0 <= code <= 100:
            self.__locationCode = code
        else:
            raise ValueError('bad code')
    def get_locationCode(self):
        return self.__locationCode



han = StudentNeed(name='zhang')
print(han.name)
print(han.score)

# 类方法
StudentNeed.print_score(han)
# 实例方法
han.print_score()

juan = StudentNeed(name='juan', score=89, private='we')
juan.score = 79
# 这个里面虽然能赋值但是 juan里面的那个__private还是原来的we 也就是说private这个实际上是后添加的一个属性和原来的__private是没有关系的
juan.private = 'zz'
print(juan.name, juan.private)
print(juan.print_score())
# print(juan.__private)
print(juan.get__private()) # 这个就说明了 原来的这个还是we
# juan.set_locationCode(code="80") # 将会有error
juan.set_locationCode(code=90)
print(juan.get_locationCode())
# class 里面要注意不要用__name__这样的变量 因为这样的变量 python 可能会直接当成了一个系统变量 能直接访问你的那种就是别这么定义就好了



# 下面开始是继承和多态

class Animal(object):

    def chow(self):
        print('chow')

class dog(Animal):
    pass

class cat(Animal):
    pass

an = Animal()
dog.chow(an)

do = dog()
do.chow()

dog.chow(do)


# 多态


class inss(object):
    def c_print(self):
        print('zhang')

    def c_printTwice(self):
        self.c_print()
        self.c_print()

class ainss(inss):
    pass

# 这是一个一个传统的继承
ai = ainss()
ai.c_print()

# 这里面就出现了多态的概念了 bi.c_printTwice() 输出的是 han han 这个就是用了父类的方法子类也进行了重写 那么就可能有多态了
class binss(inss):
    def c_print(self):
        print('han')
bi = binss()
bi.c_printTwice()


# 类型判断

print(type(123))
print(type('str'))
print(type(None))
print(type(bi))
print(type(ai))

if type('213') == int:
    print('is int')


def fn():
    pass

# 这种方式也是可以的但是最好别这么用 用下面的方法比较时尚
# if type(fn) == types.FunctionType:
#     print("Function")

if isinstance(fn, types.FunctionType):
    print("is Function")
    pass

if isinstance(ai, inss):
    print('yes is inss')


if isinstance([1, 3], (list, tuple)):
    print('yes is list or tuple')

# 使用dir() 方法获取的是一个对象的所有方法和属性(用一个list方式包裹) 其中也包含了 里面对应的方法等等
# 例如 __len__ 方法

print(dir("abc"))

# 下面这两个是等价的.
print(len('abv'))
print('abv'.__len__())

# 自己写一个len方法 __kennnn__注意这个是方法可不是变量~~~ 变量不要这么定义!

class zhanglen(object):
    def __kennnn__(self):
        return 100

zhang = zhanglen()
zhang.__kennnn__()
zhanglen.__kennnn__(zhang)


# getattr()、setattr()以及hasattr() 方法试验

class yourClass(object):

    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

yob = yourClass()

if hasattr(yob, "x"):
    print('has x')

if not hasattr(yob, 'y'):
    setattr(yob, 'y', 19)
    print(yob.y)

print(getattr(yob, 'y'))
# print(getattr(yob, 'm'))  # 报错 没有m 这个属性
print(getattr(yob, 'k', '404'))    # 这个是后面直接输出了前面给的那个不存在的标志位404

if hasattr(yob, 'power'):
    fn = getattr(yob, 'power')
    print(fn())
    print('power done')
else:
    print("none")


class defClass(object):
    name = "Student"

class subDefClass(defClass):
    pass

# 实例属性添加的时候最好不要 和类 里面定义的 属性名字相同 这样会有屏蔽 和删除时候的输出问题~~~
dS = subDefClass()
dS.name = "zhang"
print(dS.name)
del dS.name
print(dS.name)




