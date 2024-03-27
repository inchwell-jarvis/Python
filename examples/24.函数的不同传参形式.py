# 位置参数
# 调用函数时根据函数定义的参数位置来传递参数
def num_add(a, b):
    return a, b


num_add(1, 2)


# 关键字参数:函数调用时通过“键=值”形式传递参数
# 作用: 可以让函数更加清晰、容易使用,同时也清除了参数的顺序需求

def user_info(name, age, gender):
    print(f"您的名字是: {name},年龄是: {age},性别是: {gender}")


# 关键字传参
user_info(name="小明", age=20, gender="男")

# 可以不按照固定顺序
user_info(age=20, gender="男", name="小明")

# 可以和位置参数混用,位置参数必须在前,且匹配参数顺序
user_info("小明", age=20, gender="男")


# 缺省参数 预定义了默认参数  默认参数必须写在最后面
def user_info2(name, age, gender='男'):
    print(f"您的名字是: {name},年龄是: {age},性别是: {gender}")


user_info2('赵鸿飞', 18)


# 不定长参数
#     位置传递  args 可以接受多个参数，以元组的形式输出
def user_info(*args):
    print(args)


user_info(1, 2, 3, 4)


#     关键字传递   args 可以接受多个参数，以字典的形式输出
def user_info2(**args):
    print(args)


user_info2(name='赵鸿飞', value=1218)
