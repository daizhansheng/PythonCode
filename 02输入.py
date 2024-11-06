# # Python中输入的所有数据都认为是字符串类型
# x = input("input > ")
# print(type(x))  # <class 'str'>
#
# # 输入整形
# a = int(input("input int number > "))
# print(a, type(a))  # 123 <class 'int'>
#
# # 输入浮点数
# b = float(input("input float number > "))
# print(b, type(b))  # 123.0 <class 'float'>
#
# # 输入布尔类型,lower转化为小写
# c = input("input bool number > ").lower() == "true"
# print(c, type(c))
#
# # python中没有字符类型，只有字符串类型
# # ord()函数将单个字符转为对应的unicode或ASCII编码
# d = ord("A")
# print(d, type(d))  # 65 <class 'int'>
# # chr()函数将整数(unicode或ascii)转为对应的字符
# e = chr(d)
# print(e, type(e))  # A <class 'str'>
#
#
# # 在Python中使用try-except进行异常处理
# # 比如在输出错误的时候可以进行错误处理
# try:
#     f = int(input("input int type var > "))
#     print(f"输入的整数是：{f}")
# except ValueError:
#     print("input error,try again")
#
# # Python中的input可以练习输入多个字符串，可以使用split进行分割
# # str.split(sep=分隔符(默认是空格，Tab),maxsplit=-1(分割次数))
# try:
#     x, y, z = input("input multi str > ").split(sep=",")
#     print(f"x = {x},y = {y},z = {z}")
# except ValueError:
#     print("input multi str error")
#

# eval函数使用
exp = "3.14+10"
print(eval(exp))  # 去除exp的双引号

try:
    x = eval(input("input 表达式 > "))
    print(x)
except (SyntaxError,NameError) as e:
    print(e)
