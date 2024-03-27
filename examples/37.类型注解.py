# 在 Python 中，类型注解是通过在变量、函数参数、函数返回值等位置添加类型说明来实现的。虽然 Python 是一种动态类型语言，但是从 Python 3.5 开始，引入了类型注解的语法规范（PEP 484），并且在
# Python 3.6 中进一步加强了对类型注解的支持。
#
# 以下是一个简单的 Python 函数示例，使用了类型注解：


def greet(name: str) -> str:
    """
    一个简单的函数，接受一个字符串参数，并返回一个字符串结果。
    """
    return f"Hello, {name}"


# 调用函数，并传入字符串参数
result = greet("Alice")
print(result)

# 在这个示例中：
#
# 函数 greet 的参数 name 和返回值都使用了类型注解，name: str 表示参数 name 的类型是 str，-> str 表示函数的返回值类型是 str。
# 类型注解并不会改变函数的行为，它只是提供了额外的类型信息，用于类型检查和文档说明。
# 在调用函数时，可以根据类型注解来确保传入正确类型的参数，并且可以清晰地了解函数的返回类型。
# 类型注解有助于提高代码的可读性、可维护性，并且在一些静态类型检查工具中（如 MyPy）可以进行类型检查，帮助发现潜在的类型错误。


# 使用类型注解为变量指定类型
age: int = 25
name: str = "Alice"
is_student: bool = True

# 打印变量的类型和值
print(f"age: {age}, type: {type(age)}")
print(f"name: {name}, type: {type(name)}")
print(f"is_student: {is_student}, type: {type(is_student)}")

# 列表（List）
from typing import List

# 注解一个包含整数的列表
numbers: List[int] = [1, 2, 3, 4, 5]

# 注解一个包含字符串的列表
names: List[str] = ["Alice", "Bob", "Charlie"]

# 注解一个空列表
empty_list: List[float] = []

# 元组（Tuple）

from typing import Tuple

# 注解一个包含整数和字符串的元组
person: Tuple[str, int] = ("Alice", 30)

# 注解一个空元组
empty_tuple: Tuple[int, ...] = ()

# 集合（Set）
from typing import Set

# 注解一个包含整数的集合
unique_numbers: Set[int] = {1, 2, 3, 4, 5}

# 注解一个包含字符串的集合
unique_names: Set[str] = {"Alice", "Bob", "Charlie"}

# 注解一个空集合
empty_set: Set[float] = set()

# 字典（Dictionary）
from typing import Dict

# 注解一个键为字符串，值为整数的字典
ages: Dict[str, int] = {"Alice": 30, "Bob": 25, "Charlie": 35}

# 注解一个空字典
empty_dict: Dict[str, float] = {}
