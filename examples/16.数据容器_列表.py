# 数据容器
#
# # 列表
# list2 = [1, 2, 3, 4, 5, 6, 7]
# print(list2)
#
# # 嵌套列表
# list3 = [[1, 2, 3], [4, 5, 6]]
# print(list3)
#
# # 下标取数据   0,1,2,3
# print(list2[2])
# # 反向取下标  -1,-2,-3
# print(list2[-1])

# 列表常用的操作

# 查询元素下标
# mylist = ['123', '234', '345']
# print(mylist.index('123'))
# print(mylist.index('234'))

# 修改下标的值
# mylist = ['123', '234', '345']
# mylist[0] = '333'
# print(mylist)

# 插入元素  (下标，值)
# mylist = ['123', '234', '345']
# mylist.insert(0, '888')
# print(mylist)

# 追加元素
# mylist = ['123', '234', '345']
# mylist.append('888')
# print(mylist)

# 追加元素列表
# mylist = ['123', '234', '345']
# mylist.extend(['123', '423', '456'])
# print(mylist)

# 删除元素
# mylist = ['123', '234', '345']
# del mylist[0]
# print(mylist)

# 去除删除的元素元素
# mylist = ['123', '234', '345']
# element = mylist.pop(1)
# print(mylist)
# print(element)

# 删除第一个匹配项
# mylist = ['123', '234', '345', '123', '123']
# mylist.remove('123')
# print(mylist)

# 清空列表
# mylist = ['123', '234', '345', '123', '123']
# mylist.clear()
# print(mylist)

# 统计某个元素的数量
# mylist = ['123', '234', '345', '123', '123']
# count = mylist.count('123')
# print(count)


# 统计元素的数量
# mylist = ['123', '234', '345', '123', '123']
# count = len(mylist)
# print(count)