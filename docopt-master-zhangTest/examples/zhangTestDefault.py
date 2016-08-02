
# default 好像不太行呢. 可能是不太会用 但是写到 Argument里面应该就是解释说明而已.

"""
Usage:
    zhangTestDefault.py <kn>
    zhangTestDefault.py  zhangB [-vb] [<kn>]
    zhangTestDefault.py  ship <name> move <x> <y> [--speed=<kn>]


Options:
    -h --help       show this
    -v --version    111
    -b              222

Arguments:
    kn              zhang [default: 'zhang']

"""

from docopt import docopt


if __name__ == "__main__":
    argumnts = docopt(__doc__, version="你妹")
    print(argumnts)





