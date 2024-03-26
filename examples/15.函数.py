# 函数
# def 定义函数的创建
# return 返回值

# def my_str_len(data):
#     """
#     函数说明
#     :param data: 字符串
#     """
#     num = 0
#     for x in data:
#         num += 1
#     print(f'{data}的长度为{num}')
#
#
# my_str_len('12345678')
#
# print(my_str_len('123'))


# 函数嵌套
def fun1():
    print('2')


def fun2():
    print('1')
    fun1()
    print('3')


fun2()
