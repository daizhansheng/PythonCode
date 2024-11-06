# 在Python中变量类型根据赋值自动判断
# Python中值的类型：布尔，整形，浮点，字符串，复数
# Python中变量根据值自动修改类型
a = True
b = 0o123
c = 31345e-3
d = "hello world"
e = 3 + 4j

print(f"a = {a},type = {type(a)}")  # a = True,type = <class 'bool'>
print(f"b = {b},type = {type(b)}")  # b = 83,type = <class 'int'>
print(f"c = {c:.2f},type = {type(c)}")  # c = 31.34,type = <class 'float'>
print(f"d = {d},type = {type(d)}")  # d = hello world,type = <class 'str'>
print(f"e = {e},type = {type(e)}")  # e = (3+4j),type = <class 'complex'>


