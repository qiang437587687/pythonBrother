
# 这个里面的 argument 参数 好像没有什么用.
"""
Usage:
    zhangTestArgument.py [-vrh] [FILE] ...
    zhangTestArgument.py (-left | -right) CORRECTION FILE


Arguments:
    FILE            optional input file
    CORRECTION      correction angle, needs FILE, --left or --right to be present


Options:
    -h --help           show this
    -v                  verbose mode
    -q, --quite Sel     quite mode
    -r                  make report
    --left              use left-hand side
    --fight             use right-hand side


Examples:
    zhangTestArgument.py -v 123.txt


"""


from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)


