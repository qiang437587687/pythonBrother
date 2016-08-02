# 这个就做一个小练习吧  schema 这个简单的看了一下 貌似是一个验证的库, python风格 底层应该是正则差不多的吧
# 这个貌似不是练习  docopt 的这个是 搞 schema 的验证的 具体还是上 github 上面看看详情吧.
# 这里使用这个验证大概 是 因为docopt 输出的argument 是用字典的形式吧, 这个就是验证字典的,很方便.
"""
usage:
    zhangValidation.py

options:
    --count=N   number of operations

arguments:
    FILE        input file
    PATH        out directory

"""


import os
from docopt import docopt


try:
    from schema import Schema, And, Or, Use, SchemaError

except ImportError:
    exit('need schema plz install it')


if __name__ == "__main__":
    args = docopt(__doc__)
    schema = Schema({
        'FILE': [Use(open, error='FILE should be readable')],
        'PATH': And(os.path.exists, error='PATh should exist'),
        '--count': Or(None, And(Use(int), lambda n: 0 < n < 5), error='--count=N should be integer 0<n<5')})

    try:
        args = schema.validate(args)
    except SchemaError as e:
        exit(e)

    print(args)

