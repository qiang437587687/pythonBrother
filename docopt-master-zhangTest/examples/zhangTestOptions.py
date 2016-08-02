
# [-f NAME] 这个的意思是 可选项 如果写上了 -f 那么就要写上 NAME 这两个是一体的.

""" options 练习

Usage:
    zhangTestOptions.py [-f NAME]

Options:
    -f NAME,  --file=NAME  test12345
    -d WORD,  --word=WORD  就是说两个和到一起了,使用的时候同时 使用.~

Arguments:
    NAME       A name.
    WORD       A word

"""


from docopt import docopt

if __name__ == "__main__":
    arguments = docopt(__doc__)
    print(arguments)




