import json

# 准备数据
data = [{'name': '赵鸿飞', 'age': '18'}, {'name': '赵鸿飞2', 'age': '19'}]
# 转为json格式
# json_str = json.dumps(data)
# 加上 ensure_ascii=False 后中文不会被转义
json_str = json.dumps(data, ensure_ascii=False)
# json 就是字符串
print(type(json_str))
print(json_str)




# 将 json 转回 list
list1 = '[{"name": "赵鸿飞", "age": "18"}, {"name": "赵鸿飞2", "age": "19"}]'
list2 = json.loads(list1)
print(list2)