#!/usr/bin/env python3
# -*- coding: utf-8 -*-

                            ################文件相关的操作#####################

#  读文件  open() 函数 - read()

f = open('/Users/zhangxianqiang/Desktop/python创建文件夹/test.txt')
print(f)
s = f.read()
print(s)
f.close()  #直接调用close 这个如果有IO错误那么就不能调用 所以用下面的方式来搞一搞

try:
    f2 = open('/Users/zhangxianqiang/Desktop/python创建文件夹/test2.txt', 'r')
    print(f2.read())
finally:
    if f:
        f.close()

# 上面的方式和下面的方法其实也是一样的 这个的后面不用调用 f.close()方法.

with open('/Users/zhangxianqiang/Desktop/python创建文件夹/test2.txt', 'r', encoding='UTF-8', errors='ignore') as f:
    print('f.read() 1=>> ', f.read())
    # print('f.read() 2=>> ', f.read()) # ####实际测试这个地方的调用是不能多次的只能作用一次!!!!
    # print('f.read() 3=>> ', f.read())

with open('/Users/zhangxianqiang/Desktop/python创建文件夹/test2.txt', 'r', encoding='UTF-8', errors='ignore') as f:
    print('f.readline().strip() => ', f.readline().strip())  # 后面的这个strip() 作用是去掉末尾的 '\n'
with open('/Users/zhangxianqiang/Desktop/python创建文件夹/test2.txt', 'r', encoding='UTF-8', errors='ignore') as f:
    listLines = f.readlines()
    print('f.readlines() => %s' % listLines)

# 注意到 read() 方法中如果文件太大了 那么内存是承受不住的 ,所以可以用 #read(size)# 方法来读取其中的内容(其中size是字节数)
# readline() 这个方法可以每次都读取一行 的内容
# readlines() 这个方法是读取所有的内容并且按照行返回list

# 使用方法看自己的使用情景:

    # 如果文件很小，read()一次性读取最方便；
    # 如果不能确定文件大小，反复调用read(size)比较保险；
    # 如果是配置文件，调用readlines()最方便


# tip1 像open() 这样的方法有一个 read() 方法的对象称为file-like Object 这个类不要求从特定的类继承只要写一个read()就行了


# 写文件 open()  - write()

fw = open('/Users/zhangxianqiang/Desktop/python创建文件夹/test.txt', 'w')
fw.write('hello world')
f.close()

# 可以使用 上面的命令一直写文件, 不要忘记 close()因为要是忘记这个了 可能没有真正的写到文件里面而是缓存在内存中
# 所以还是用with命令来的好一点

with open('/Users/zhangxianqiang/Desktop/python创建文件夹/test.txt', 'w', encoding='UTF-8') as fw1:
    fw1.write('Hello World222')
    fw1.write('Hello World333')
    fw1.write('Hello World444')
    # 文件里面的内容就是 hello world222Hello World333Hello World444


# StringIO (在内存中读取str) 和 BytestIO (二进制的操作)
from io import StringIO

fs = StringIO()
fs.write('Hello')
fs.write(' ')
fs.write('world')
print(fs.getvalue())


from io import BytesIO
fb = BytesIO()
fb.write('中文'.encode('UTF-8'))
print(fb.getvalue())  # 输出的结果是 : b'\xe4\xb8\xad\xe6\x96\x87'

fb1 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(fb1.read())

import os
print(os.name)   # posix 说明是 unix 和 linux 内核  nt 是windows
print(os.uname())
print(os.environ)
print('PATH = ', os.environ.get('PATH'))  # 获取 环境中某一个变量的值


# 文件操作和目录.

# 查看当前目录的绝对路径
print('绝对路径', os.path.abspath('.'))     #这个里面的 . 可以不添加?? 也能打印这个再看看.

# 在某一个目录下面创建一个新的目录,首先把新的目录的完整路径表示出来:(一般都用这个拼接 因为 unix 下面是 / 来分割 win 是\ 来分割的)
makePath = os.path.join('/Users/zhangxianqiang/Desktop/pythonBrother', 'testdir')
print(makePath)
# 创建
os.mkdir(makePath)  # 创建
# 删除
os.rmdir(makePath)
# 返回一个元组分割了最后面的路径
print(os.path.split('/Users/zhangxianqiang/Desktop/pythonBrother/text.txt'))   # ('/Users/zhangxianqiang/Desktop/pythonBrother', 'text.txt')
# 返回一个元组 分割了 后面的扩展名ls
print(os.path.splitext('/Users/zhangxianqiang/Desktop/pythonBrother/text.txt')) # ('/Users/zhangxianqiang/Desktop/pythonBrother/text', '.txt')

# 重命名 和删除 重命名失败返回时 None 不知道为什么~.
# print(os.rename('/Users/zhangxianqiang/Desktop/pythonBrother/han.txt', 'zhang.txt'))
# print(os.remove('/Users/zhangxianqiang/Desktop/pythonBrother/han.txt'))


# 列出当前目录的下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 列出.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])



##  序列化  ### 这个貌似和 iOS中 NSUserDefault 差不多 但是不同版本的 可能会不成功 用的时候可能会悲剧.

ficP = dict(name='zhang', age='20')

import pickle

print('pickle.dumps(ficP) ===> ', pickle.dumps(ficP))  # 把任意对象转换为一个bytes 然后这个就能写入到一个file-like Object

fp = open('/Users/zhangxianqiang/Desktop/pythonBrother/pickle.txt', 'wb')
pickle.dump(ficP, fp) # 注意这里面还有一个是dumps 和这个函数是不一样的作用
fp.close()

fr = open('/Users/zhangxianqiang/Desktop/pythonBrother/pickle.txt', 'rb')
ficr = pickle.load(fr)
fr.close()
print(ficr)


# JSON
import json
dj = dict(name='han', age='18')
print(json.dumps(dj))  # {"age": "18", "name": "han"}

json_str = '{"age": "18", "name": "hanxiujuan"}'
print(json.loads(json_str))


# JSON进阶  -- 直接转换成对象 MJEtension?

class Stundent(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
sj = Stundent('Bob', 20, 88)

# 要写一个转换函数

def stu2dic(std):

    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(sj.name)

print(json.dumps(sj, default=stu2dic))  # 这个是对象转换为JSON 注意这里面的default是必须要写上的

# 上面的原理是 告诉转换的方式  其实每一个class 都有一个__dict__的属性(也有例外例如 定义了__slots__(tuple里面包含了允许添加属性的名字:__slots__ = ('name', 'age'))的class)
# 可以利用这个__dict__的属性来进行一个通用的操作如下..

print(json.dumps(sj, default=lambda obj: obj.__dict__))



# JSON 转换为Student实例对象

def dic2Stu(d):
    return Stundent(d['name'], d['age'], d['score'])

json_str_re = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str_re, object_hook=dic2Stu))
