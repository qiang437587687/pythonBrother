# 1.我看以后要是用还是用小写字母来搞吧. 这样不但能识别还不容易出错 [options] 这里面写成 大写的 O 貌似还不行
# 2. 看来还是立即的不到位吧  options 里面天不添加 , 其实是一样的. 二者的效果是一样的,
#    值得注意的是 -t 包含了一个参数 然后 还有一个 <port> 这样就是两个参数了.
"""
usage:
    zhangTestShortcut.py [options] <port>

options:
    -h, --help       show this
    -v, --version    show version
    -t, --time  TIMEOUT     set time

arguments:
    N               A number
    TIMEOUT         timeout interval

"""

from docopt import docopt

if __name__ == "__main__":
    arguments = docopt(__doc__)
    print(arguments)




