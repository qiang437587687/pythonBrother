
# <> 中间的是参数   -h --help 这样的是选项
# 短的选项可以一起写  -abc 等价于 -a -b -c.
# []这个里面是可选的项目需要就写上  参数，选项以及命令
# ()里面是必须要填写的 里面的选项不确定可以用 | 来区分
# 貌似后面的 参数 可选项好像只能放在后面~ 这个不太确定

"""Train tickets query via command-line.

Usage:
    docoptSecond.py [-gdtkz] <from> <to> <date>
    docoptSecond.py zhang [-dmm] <nimei>
    docoptSecond.py zhangB (-d|-mm) <nimei> [<nimei2>]...
    docoptSecond.py (zhangD|zhangC) (-g|-mm) <nimei> [<nimei2>]
    docoptSecond.py zhangE -n <N>

Options:
    -h,--help              显示帮助菜单
    -g                     高铁
    -d                     动车
    -t                     特快
    -k                     快速
    -z                     直达
    -mm                    你妹
    --apply                接受
    -p, --timeout TIMEOUT  set timeout TIMEOUT seconds
    -n, --number N         use N as a number

Example:

    tickets 南京 北京 2016-07-01
    tickets -dg 南京 北京 2016-07-01

"""

from docopt import docopt


def zhang():
    arguments = docopt(__doc__, version='1.0.0rc2')
    if arguments["<nimei>"] == "张野":
        print("=============>>>韩大宝<<<===============")
    print(arguments)

if __name__ == '__main__':
    zhang()
























