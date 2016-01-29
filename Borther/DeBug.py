#!/usr/bin/env python3
# -*- coding: utf-8 -*-



# debug

import logging
logging.basicConfig(level=logging.INFO)

# s = '0'
# n = int(s)
# logging.info(n)
# print(10/n)

L = ['M', 'S', 'Z', 'H', 'X']


def zhangTest():

    for test in L:
        logging.info(test)
        print(test)

zhangTest()


# 测试这个教程上还提了 assert 的方式 和上面的 logging这个差不多  还有IDE 的方式则个还没有研究
