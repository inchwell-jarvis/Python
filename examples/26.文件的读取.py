# 使用open函数，可以打开一个已经存在的文件，或者创建一个新文件，语法如下

# 打开文件
# f = open("C:/Users/22379/Desktop/test.txt", "r", encoding='UTF-8')
# print(f)
# <_io.TextIOWrapper name='C:/Users/22379/Desktop/test.txt' mode='r' encoding='UTF-8'>

# 读取文件 read 参数为要读取的字节长度   不给参数读取全部内容
# 在程序中多次读取，下一次会继续上一次读取的位置开始读取
# print(f.read(10))
# print(f.read())


# print('------------------------------')
# 读取文件封装到list
# lines = f.readlines()
# print(lines)

# readline 一次读取一行
# lines = f.readline()
# print(lines)

# 循环一行一行读取
# for line in f:
#     print(line)


# 关闭文件
# f.close()


# with 读取文件自动解除占用
# with open("C:/Users/22379/Desktop/test.txt", "r", encoding='UTF-8') as f:
#     for line in f:
#         print(line)
