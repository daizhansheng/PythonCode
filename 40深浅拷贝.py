# 定义一个 Person 类
class Person:
    pass


# 定义一个 Student 类
class Student:
    # 构造函数，初始化属性 per
    def __init__(self, p):
        self.per = p


# 创建一个 Person 对象 p
p = Person()
print(p)  # <__main__.Person object at 0x108621370>
# 创建一个 Student 对象 s1，并将 p 作为其属性 per
s1 = Student(p)

# 输出 s1 对象和其 per 属性
print(
    s1, s1.per
)  # <__main__.Student object at 0x108621310> <__main__.Person object at 0x108621370>

# 将 s1 对象的引用赋给 s2
s2 = s1

# 输出 s2 对象和其 per 属性
print(
    s2, s2.per
)  # <__main__.Student object at 0x108621310> <__main__.Person object at 0x108621370>

# 导入 copy 模块
import copy

# 使用 copy.copy() 函数创建 s2 对象的浅拷贝 s3
s3 = copy.copy(s2)

# 输出 s3 对象和其 per 属性
print(
    s3, s3.per
)  # <__main__.Student object at 0x108621490> <__main__.Person object at 0x108621370>

# 使用 copy.deepcopy() 函数创建 s2 对象的深拷贝 s4
s4 = copy.deepcopy(s2)

# 输出 s4 对象和其 per 属性
print(
    s4, s4.per
)  # <__main__.Student object at 0x108623dd0> <__main__.Person object at 0x108623e90>
