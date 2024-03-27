# 函数作为参数传入
def text_fun(num_add1):
    num = num_add1(1, 2)
    return num


def num_add1(a, b):
    return a + b


print(text_fun(num_add1))


# 匿名函数 lambda  临时使用一次的匿名函数
def text_fun2(num_add2):
    num = num_add2(1, 2)
    return num


print(text_fun2(lambda x, y: x + y))
