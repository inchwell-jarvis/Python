# Union 是 Python 中 typing 模块中定义的一个泛型类，用于表示多种可能的类型之一。在类型注解中，Union 可以用来指定一个变量、函数参数或函数返回值的类型为多个类型中的一个。下面是一些示例：

# 变量类型注解

from typing import Union

# 变量 x 可以是整数或浮点数
x: Union[int, float] = 10

# 变量 y 可以是字符串、列表或元组
y: Union[str, list, tuple] = "Hello"

# 变量 z 可以是整数、浮点数或布尔值
z: Union[int, float, bool] = True


# 函数参数类型注解

# def square_root(x: Union[int, float]) -> Union[int, float]:
#     return x ** 0.5
#
#
# result = square_root(9)  # 返回值可以是整数或浮点数


# 函数返回值类型注解

def divide(a: int, b: int) -> str | float:
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b


result = divide(10, 3)  # 返回值可以是整数或浮点数
