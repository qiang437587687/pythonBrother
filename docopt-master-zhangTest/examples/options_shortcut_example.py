
# -t -n 两个选项的是简化后的?? .不好用 试验总是有问题


"""Example of program which uses [options] shortcut in pattern.

Usage:
  options_shortcut_example.py [options] <port>

Options:
  -h --help                show this help message and exit
  --version                show version and exit
  -n, --number N           use N as a number
  -t, --timeout TIMEOUT    set timeout TIMEOUT seconds
  --apply                  apply changes to database
  -q                       operate in quiet mode

arguments:
    N               A number
    TIMEOUT         timeout interval

"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0.0rc2')
    print(arguments)
