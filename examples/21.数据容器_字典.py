# 字典就类似js的对象
# key 不可为字典
# 定义字典
my_dict1 = {'王力宏': 89, '赵鸿飞': 99}

# 定义空字典
my_dict2 = {}
my_dict3 = dict()

# 取值
print(my_dict1['王力宏'])

# 字典嵌套
my_dict4 = {'分数': {
    '赵鸿飞': 100,
    '朱帅帅': 100
}}
print(my_dict4['分数']['赵鸿飞'])

# 新增
my_dict5 = {'王力宏': 89, '赵鸿飞': 99}
my_dict5['朱帅帅'] = 80
print(my_dict5)

# 修改
my_dict5['朱帅帅'] = 90
print(my_dict5)

# 删除
sor = my_dict5.pop('朱帅帅')
print(sor)
print(my_dict5)

# 清空
my_dict5.clear()
print(my_dict5)

# 获取全部的key
my_dict6 = {'王力宏': 89, '赵鸿飞': 99, '朱帅帅': 99}
keys = my_dict6.keys()
print(keys)

# 遍历
for key in keys:
    print(my_dict6[key])

# 这两种都可以
for key in my_dict6:
    print(my_dict6[key])


# 统计数量
print(len(my_dict6))