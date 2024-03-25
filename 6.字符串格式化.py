# 占位符 %s %d %f
# 使用 %s 占位 使用 % 后面的数据进行填充
money = 123
name = '剩余金额：%s' % money
print(name)

# 多个数据拼接 按顺序进行插入
name2 = '剩余金额：%s and %s' % (123, 321)
print(name2)

# 多个数据拼接 按顺序进行插入
name3 = '剩余金额：%s and %d' % (123, 321)
print(name3)

