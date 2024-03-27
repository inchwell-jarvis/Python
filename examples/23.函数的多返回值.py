# 函数只能有一个 return

def num_add(a, b):
    return a + b


print(num_add(1, 2))


# 多返回值 及其接收方式
def num_add2(a, b):
    return a, b


x, y = num_add2(1, 2)
print(x, y)

# 多返回值 及其接收方式，类型不受限制，位置对就行
def num_add3(a, b):
    return a, True


x, y = num_add3(1, 2)
print(x, y)
