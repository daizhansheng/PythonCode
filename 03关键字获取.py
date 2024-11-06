# Python中一共有35个关键字，在定义变量的时候不能和关键字重复
# 关键字分类
# 控制语句：if elif else for while  break continue pass 8
# 函数和类：assert def class lambda return yield 6
# 异常处理：try except as finally raise 5
# 布尔：False True  None(空)3
# 导入模块：import from  2
# 逻辑运算符：and or not 3
# 变量修饰：global nolocal del 3
# 身份：in is 2
# 异步io:async await 2
# 资源回收：width 1
# 关键字的获取方法需要导入keyword模块
import keyword
import keyword as kw
import asyncio as io
from math import sqrt, pi

print(keyword.kwlist)  # 输出的结果如下
# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

# 判断是否是关键字的方法
print("是否是关键字 ：", keyword.iskeyword("sizeof"))


# False和True代表布尔类型的真和假
# None判断某个变量是否是空值
var = None
if var is None:
    print(f"var 是 {var}")

# and等价于c语言的&&,表示逻辑与
# or等价于c语言的||,表示逻辑或
# not等价于c语言的!,代表非
a = 15
b = 500
if a > 10 and b == 500:
    print(f"a = {a},b = {b}")
else:
    print("结果是假")

# Python中的as在导包的时候用于取别名，异常处理时用于捕获异常
# import keyword as kw 将keyword取别名为kw,以后可以使用kw
print(kw.kwlist)
# as作用异常捕获
try:
    x = int(input("input int > "))
    print(x)
except ValueError as e:
    print(f"input int error : {e}")
try:
    x = 10 / 0
    print(x)
except ZeroDivisionError as e:
    print(f"error : {e}")


# assert是断言，用于检测函数参数是否合法，在Python
# 中用于程序调试，assert会引发一个AssertionError异常
def check_data(t):
    assert t >= 0, "input x error"
    return t * t


try:
    check_data(-1)
except AssertionError as e:
    print(f"input error : {e}")


# async和await用于异步编程
async def say_hello():
    print("hello1111")
    await io.sleep(2)
    print("hello2222")


io.run(say_hello())

# break终止循环,continue跳过当前循环
# class用于声明类对象，def用于声明函数
# if elif else 用于编写空值语句
# try except as finally用于异常处理
# raise用于触发异常
# finally语句块的作用用于清理操作，如果关闭文件，释放锁，关闭数据库等操作


def read_file(name):
    fd = None
    try:
        fd = open(name, "r")
        print(fd.read())
    except FileNotFoundError as e:
        print("文件不存在")
    finally:
        print("关闭文件成功了")
        if fd is not None:
            fd.close()


read_file("hello.txt")


def divide(a, b):
    if b == 0:
        raise ValueError("分母不能是0！！！")
    return a / b


try:
    result = divide(10, 0)
except ValueError as e:
    print(e)
# for循环语句
# from和import用于导入模块
# from math import sqrt,pi
# from math import sqrt as square_root 从math中导入sqrt并重命名为square_root
# print(square_root(36))  # 输出: 6.0
print(sqrt(9))
print(pi)


# global在函数内声明变量为全局变量
x = 10


def change_x():
    global x
    x = 500  # 修改全局变量


change_x()
print(x)  # x=500

# Python中,in关键字用于检测一个值是否存在可迭代对象中，
# 如字符串、列表、元组、集合、字典中，如果在迭代器中返回真，否则返回假
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # 输出: True
print("orange" in fruits)  # 输出: False

# Python中的is关键字用于比较两个对象的身份（即内存中的地址）是否是
# 同一个对象，判断的是身份。与常用的运算符==不同，后者比较的是两个
# 值是否相等。
# 1.检查对象的身份,这里存在小整数的问题[-5,256],两个变量赋值这个区间的数据，他们的地址就是一样的
a = 10
b = 10
print(id(a), id(b))
print(a is b)  # 输出: True
# 2.用于None值的比较
x = None
if x is None:
    print("x is success")

# lambda是创建匿名函数
add = lambda x, y: x + y
print(add(100, 200))


def test_lambda(aa):
    return lambda y: y * aa


step1 = test_lambda(5)
print(step1(10))


# nonlocal 关键字用于在嵌套函数中声明一个变量，使得该变
# 量不是局部的，而是指向最近的外层（非全局）作用域中的变量。
def counter():
    count = 0  # 外层变量

    def increment():
        nonlocal count  # 声明 count 为非局部变量
        count += 1  # 修改外层变量
        return count

    return increment


increment_counter = counter()
print(increment_counter())  # 输出: 1
print(increment_counter())  # 输出: 2

# pass代表的是空，可以写在函数中，或者写在类中
# 就是一个占位符

# return 用于函数返回结果
# while 是循环
# with 关键字用于简化资源管理和清理操作，尤其是文
# 件操作和网络连接等需要显式关闭或释放资源的情况。使
# 用 with 可以确保在使用完资源后自动执行清理工作，
# 即使发生异常时也会执行。
with open("hello.txt",'r') as file:
    content = file.read()
    print(content)
# 文件在这里会自动关闭，无需显示调用file.close()函数

# yield 关键字用于定义生成器（generator），生成器是一
# 种特殊类型的迭代器。与普通函数不同，生成器可以暂停其执
# 行状态并在需要时恢复，从而生成一系列值。使用 yield 可
# 以有效管理内存，因为它在需要时生成值，而不是一次性生成
# 所有值。
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # 使用 yield 返回当前计数
        count += 1

# 使用生成器
for number in count_up_to(5):
    print(number)  # 输出: 1, 2, 3, 4, 5




