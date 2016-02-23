#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

print('今天犯了一个错误 不能直接建立一个base64这样的文件 切记.')
#  这里面需要加上一个 b'zhang' 这样的形式
s = base64.b64encode(b'zhang')
print(s)

ss = base64.b64decode(s)
print(ss)

# url safe

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))


