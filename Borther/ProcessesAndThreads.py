#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import os # (这里面注销了是因为进程开的多了会影响下面的线程执行过程.)
#
# print("进程和线程")
#
# print('Progress (%s) start...', os.getpid())
#
# pid = os.fork()
#
# if pid == 0:
#     print('child progress (%s) parent is %s' % (os.getpid(), os.getpid()))
# else:
#     print('%s created a child process (%s)' % (os.getpid(), pid))
#
#
# # 上面的fork() 方法是 mac 上用的win上是没法用的所以要用下面的方法 一个跨平台模块
#
# from multiprocessing import Process
#
# def run_proc(name):
#     print('Run child process %s (%s)' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent prgress %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test', ))
#     print('child progerss will start')
#     p.start()
#     p.join()
#     print('child process end.')
#     print('\n')
#     print('\n')
#     print('\n')
#     print('\n')
#     print('\n')

# 进程这里 还可以用pool来创建好几个进程  没太看懂 用的时候 回来再看看  下面是线程(上面注销了看到下面是正常的 要不就不行了)


import time, threading

def loop():
    print('In Loop thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('In Loop thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('In Loop thread %s ended.' % threading.current_thread().name)




print('In Loop thread %s ended.' % threading.current_thread().name)
t = threading.Thread(target=loop, name='ALoopThread')
t.start()
t.join()
print('ALoopThread thread %s ended.' % threading.current_thread().name)



# 线程锁

balance = 0
lock = threading.Lock()   # 创建线程锁

def run_thread(n):
    k = 0
    for i in range(n):
        lock.acquire()
        try:
            k += i
        finally:
            lock.release()
    print(k)

run_thread(101)


# python 的多线程是有GIL锁的 所以多线程再多也只能运行在一个核心上 也就是不管怎么样 只能是有一个核心在运行多线程.
# 想要多核利用那么要么写c(并不会) 要不就直接用多进程吧 每一个进程是有自己的GIL的所以要多核利用就多进程吧!



# 这个threading.local()怎么理解呢...就是定义一个相对于某一个线程的一个全局变量, 达到线程和线
# 程之间使用的是各自独立的变量.

location_school = threading.local()

def progress_student():

    std = location_school.student
    tea = location_school.teacher

    print(std, tea)
    print(threading.current_thread())

def process_thread(name, teacher):

    location_school.student = name
    location_school.teacher = teacher
    progress_student()

t1 = threading.Thread(target=process_thread, args=('zhang', 'wang'), name='thread-A')
t2 = threading.Thread(target=process_thread, args=('han', 'xiu'), name='thread-B')

t1.start()
t2.start()

t1.join()     #  上面说是为了同步进程 不知道 这个是不是会影响执行顺序测试 测试..
t2.join()





