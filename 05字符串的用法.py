# 1.Python中字符串创建
# 使用单引号，双引号，三引号
str1 = "这是字符串1"
str2 = "这是字符串2"
str3 = """
这是行字符串3
这里的行数你可以自由编写
这里还可以是三个单引号
"""
print(str1)
print(str2)
print(str3)

# 2.字符串长度获取通过len()函数
# 这里的中文，英文，数字都是算一个字符
print(len(str1))  # 6
print(len(str2))  # 6
print(len(str3))  # 34

# 3.字符串可以当成数组的形式进行访问
# 索引：字符串[下标]
# 切片：字符串[开始下标:结束-1]
# 逆序   ：-10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#  str4 = h  e  l  l  o  w  o  r  l  d
# 正序   ：0  1  2  3  4  5  6  7  8  9
str4 = "helloworld"
print(str4[0], str4[9])  # 正序访问，'h','d'
print(str4[-10], str4[-1])  # 倒序访问，'h','d'
print(str4[5:10])  # "world"

# 4.字符串拼接使用：+
str5 = "hello"
str6 = "world"
print(str5 + " " + str6)  # hello world
print(str5 + " Python")  # hello Python

# 5.字符串重复使用：*
str7 = "hqyj"
print(str7 * 5)  # 这里的含义是重复5遍str7字符串
print(5 * str7)  # 这里也可以倒着写
print("*" * 20)  # 打印20颗*

# 6.字符串查找和替换
str8 = "www.hqyj.com"
print("hqyj" in str8)  # 在：True    不在：False
print(str8.find("hqyj"))  # 查找到字符串，返回h下标是4,查找不到返回-1
try:
    print(str8.index("hqyjr"))  # 查找到字符串，返回h下标是4,查找不到抛出异常
except ValueError as e:
    print("find error", e)  # find error substring not found

str8 = str8.replace("hqyj", "baidu")
print(str8)

# 7.字符串格式化
name = "Alice"
age = 25
sex = "m"
score = 88.67123
# f-string格式化
print(f"name={name},age={age},sex={sex},score={score:.2f}")
# str.format()方法格式化
print("name={},age={},sex={},score={:.2f}".format(name, age, sex, score))
# %格式化
print("name=%s,age=%d,sex=%c,score=%.2f" % (name, age, sex, score))
# 字符串拼接和函数调用
print("name=", name, "age=", age, "sex=", sex, "score=", round(score, 2))

# 8.字符串大小写转换函数
str9 = "Hello Python"
print(str9.upper())  # HELLO PYTHON
print(str9.lower())  # hello python
print(str9.capitalize())  # Hello python
print(str9.title())  # Hello Python

# 9.去除空白字符
str10 = "   hello world    "
print(str10.strip(), "E")  # 去除两端空白字符，Tab或空格 hello world E
print(str10.lstrip(), "E")  # 去除左侧空白字符          hello world     E
print(str10.rstrip(), "E")  # 去除右侧空白字符             hello world E

# 10.字符串拆分
str11 = "hello,world,okay"
print(str11.split(sep=","))  # ['hello', 'world', 'okay']
lst1 = ["hello", "world", "okay"]
print("".join(lst1))  # "helloworldokay"

# 字符串的编解码
# Unicode:国际标准，一个汉字对应3个字节
# gbk    :中国标准，一个汉字对应2个字节
str12 = "祝贺神州19发射成功"
# str12 = str12.encode("utf-8",errors="strict")
# print(str12)
# print(bytes.decode(str12))
str12 = str12.encode("gbk",errors="strict")
print(str12)
print(bytes.decode(str12,"gbk"))