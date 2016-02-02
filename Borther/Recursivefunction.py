print('开始学Recursive function啦')


# 下面这样的就是一个递归函数了
# def fact(n):
#     if n == 1:
#         return 1
#     nn = n * fact(n-1)
#     print(n)
#     return nn
#
# print(fact(100))

def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num*product)


# 尾随递归就相当于一个循环.

