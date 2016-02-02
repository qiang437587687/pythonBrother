
class zhang(object):
    pass
s = zhang()
s.name = 'zhang'
print(s.name)


#  可以给实例绑定一个方法 MethodType 这个方法可以给类或者实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(24)

# __slots__ 使用方法
# print(dir(zhang)) 查看了一下 里面并没有包括 __slots__ .. 不知道为什么

# 限制实例的属性添加  比方说下面的只允许添加name age 两个属性
class student(object):
    __slots__ = ('name', 'age')   # 用tuple定义允许绑定的属性名称
    pass

s = student()
s.name = "zhang"
s.age = 23
# s.score = 99     # 报错了.


class wang(student):
    pass

g = wang()
g.score = 100
print(g.score)   # 继承以后是允许添加的 ..除非也定义了__slots__


#  @property  (负责把一个方法变成属性调用)

class Person(object):

    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2016 - self._birth

s = Person()
s.birth = 60
print(s.birth)
print(s.age)



#  多重继承


class Money(object):

    def getMethod(self):
        print("you you check not")


class MAndP(Money, Person):
    pass

mp = MAndP()
mp.getMethod()
mp.birth = 1989
print(mp.age)


# 定制类

# __str__ 加上这个就能在调用的时候显示对应的一个文字输出了
# __str__ 这个是用print 打印出来的结果  __repr__ 这个是>>>方式打印的结果显示

class StudentSS(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'student object (name: %s)' % self.name

    __repr__ = __str__

print(StudentSS('zhang d'))

# __iter__(迭代对象)  __next__ (下一个返回值)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopAsyncIteration()
            # pass
        return self.a

# for n in Fib():
#     print(n)

# __getitem__ (表现的想list那样按照下表取出元素) (自定义一个 list dict 等类型时候使用但是没什么事还是少用)
# 与这个对应的还有一个__setitem__() __delitem__() 根据需要的不同进行定制.

class Fibg(object):

    def __getitem__(self, n):

        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a

fg = Fibg()
print('现在的输出是:', fg[100])

print(list(range(100))[5:10])


# __getattr__  可以用这个来捕获 获取的字符 __getattr__ 这个里面的还可以返回一个函数 调用的时候注意一下 有()

class StudentG(object):

    def __init__(self):
        self.name = 'zhang'

    def __getattr__(self, item):
        print("dont has a attr %s" % item)
        return lambda: 25
        # raise AttributeError('\'Student\' object has no attribute \'%s\'' % item) 可以提示用户并没有这个属性

sg = StudentG()
print(sg.name)
sg.score
print(sg.score())


# 这个__getattr__ 这个可以用来这么去查找和存储一个路径

class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)


class ChainL(object):
    def __init__(self, path=''):
        self._path = path


    def currentName(self,user_name):
            return ChainL('%s/users:%s' % (self._path, user_name))


    def __getattr__(self, attr):
        if attr == 'users':            # 这个是查找方法的检测有没有这个方法 然后接受的参数是括号里面的
            return self.currentName    # 以后需要记住这个了 别再犯这个错误了~

        return ChainL("%s/%s" % (self._path, attr))

    def __str__(self):
        return self._path

# print(ChainL().status.users('ZhangSan').timeline.list)
# print(ChainL().status.users.repo)


class MyChainL(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, attr):
        if attr == 'users':
            return lambda user_name: MyChainL('%susers=%s' % (self._path, user_name))
        return MyChainL("%s/%s" % (self._path, attr))

    def __str__(self):
        return self._path

print(MyChainL().status.users('ZhangSan').timeline.list)


#  上面的还是需要好好理解一下  有一个 递归的概念  有一个 匿名函数的概念  有一个 闭包的概念

# __call__

class StudentC(object):
    def __init__(self, name=''):
        self._name = name

    def __call__(self, *args, **kwargs):
        print('My name is %s' % self._name)


sc = StudentC('zhang')
print(sc())


# 教程上面说 对象和函数 其实本质上的区别就不是那么明显通过__call__ 的方式 直接调用对象相当于调用了__call__函数
# 那么如果要判断 是函数还是对象就需要下面的方式了

print(callable(sc))   # true
print(callable([1, 2, 3])) #False






