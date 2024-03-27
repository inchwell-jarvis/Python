# 语法
# try:
#     f = open('C:/sdasdas.text', 'r', encoding='UTF-8')
# except:
#     print('出现错误了')


# 捕获指定的异常
# try:
#     print(name)
# except NameError as e:
#     print(e)
#
#
# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print(e)
#
#
# # 捕获多个异常
# try:
#     print(1/0)
# except (ZeroDivisionError,NameError) as e:
#     print(e)


# 捕获所有异常
# try:
#     print(1/0)
# except Exception as e:
#     print(e)


# 没有出现异常
# try:
#     print(123)
# except NameError as e:
#     print(e)
# else:
#     print('没有出现异常')


# 无论有没有异常都执行
# try:
#     print(123)
# except NameError as e:
#     print(e)
# else:
#     print('没有出现异常')
# finally:
#     print('结束')


# --------------------------------------------------------
# def func1():
#     print(11111111111111)
#     print(1 / 0)
#
#
# def func2():
#     print(2222222222222)
#     func1()
#
#
# def main():
#     try:
#         func2()
#     except Exception as e:
#         print(e)
#
# main()
