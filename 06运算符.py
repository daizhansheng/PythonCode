# Python中支持链式赋值
a = b = c = 100
print(a, b, c)  # 100 100 100
print(id(a), id(b), id(c))  # 4494203712 4494203712 4494203712

# Python的解包赋值
a, b = 10, 20
print(a, b)  # 10 20
# 利用解包赋值交换a和b的值
a, b = b, a
print(a, b)  # 20 10

# 算术运算
a = 2
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)
# 位运算
x = -9 >> 2
print(x, type(x))
print(hex(x), type(x))

# 在补码基础上进行位运算
# 0x8000 0009
# 0xFFFF FFF7
# 0xFFFF FFFd 1101
# 0x8000 0003  -->-3
# 使用hex()函数获取到的结果是-0x3


# 判断输入的字符中是否包含hello
x = input("请输入字符串> ")  # 比如输入hello world
print("hello在x中？", "hello" in x)  # True
print("hello不在x中？", "hello" not in x)  # False

# 身份运算符 "is" 和 "is not" 的示例
# 身份运算判断的是变量的地址，而非变量的值
x = 10
y = 10
z = x

print(x is y)  # 输出: True，x 和 y 引用同一个对象
print(x is z)  # 输出: True，x 和 z 引用同一个对象
print(x is not y)  # 输出: False，x 和 y 引用同一个对象
print(x is not z)  # 输出: False，x 和 z 引用同一个对象
