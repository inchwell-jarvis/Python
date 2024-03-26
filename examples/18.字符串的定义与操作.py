# 再识字符串

# 尽管字符串看起来并不像:列表、元组那样，一看就是存放了许多数据的容器
# 但不可否认的是，字符串同样也是数据容器的一员。
# 字符串是字符的容器，一个字符串可以存放任意数量的字符
# 如，字符串:"atheism"


my_str = "hello and world it"
# 下标
print(my_str[2])

# index 方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找and，其起始下标是: {value}")

# replace万法
new_my_str = my_str.replace("it", "程序")
print(f"将字符串{my_str}，进行替换后得到: {new_my_str}")

# split方法
my_str = "hello python atheism it cast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到: {my_str_list}，类型是: {type(my_str_list)}")

# strip方法
my_str2 = " atheism and it cast "
new_my_str = my_str2.strip()  # 不传入参数去除首尾空格
print(f"字符串{my_str2}被strip后，结果: {new_my_str}")


# strip
my_str = "12atheism and it cast21"
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip('12')后，结果: {new_my_str}")

# 统计出现次数
my_str3 = "12atheism and it cast21"
#
print(my_str3.count('12'))


# 统计数量
my_str4 = "12atheism and it cast21"
#
print(len(my_str4))
