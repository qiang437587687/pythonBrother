
# 总结 1 Argument 后面带上 ... 这个就能同时添加好几个 argument类型的参数
# 总结 2 加上了 ... 那么其中的 argument (例如Usage中的value) 在输出中是以数组的形式输出的


""" 写一个简单的计算器,只是练习 重点看看多个参数的 三个点的形式

Usage:
    zhangTestArgument.py <kild> ((+ | - | * | /) <value>)...
    zhangTestArgument.py [-vdfp] <kild> ((+ | - | * | /) <cali>)...

Arguments:
    value       数据
    cali        另一个数据
    kild        还是另一个数据
    mild        还是另一个数据

Options:
    -v          11
    -d          22
    -f          33
    -p          44
    -h          show this

Exapmles:
    zhangTestArgument.py 12 + 35 + 36

"""


from docopt import docopt

if __name__ == "__main__":
    arguments = docopt(__doc__)
    print(arguments)