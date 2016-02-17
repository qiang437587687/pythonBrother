#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

print('Second Spider')


if __name__ == '__main__':

    classinfo = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    jikespider = spider()
    all_links = jikespider.changepage()























