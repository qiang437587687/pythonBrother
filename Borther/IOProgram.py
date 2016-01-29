#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

fw = open('/Users/zhangxianqiang/Desktop/python创建文件夹/test.txt')



