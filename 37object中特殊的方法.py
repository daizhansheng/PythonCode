# 导入正则表达式模块
import re


# 定义一个 Person 类，继承自 object 类
class Person(object):
    # 构造函数，用于初始化类的实例
    def __init__(self, name, age):
        # 将 name 参数赋值给实例的 name 属性
        self.name = name
        # 将 age 参数赋值给实例的 age 属性
        self.age = age

    # 定义一个 show 方法，用于打印实例的信息
    def show(self):
        # 使用 format 方法打印实例的 name 和 age 属性
        print("name={},age={}".format(self.name, self.age))

    # 重写 __str__ 方法，用于获取实例对象的字符串表示
    def __str__(self):
        # 调用 super().__str__() 来获取实例对象的默认字符串表示
        str = super().__str__()
        # 使用正则表达式来匹配内存地址部分
        pattern = r"0x[\da-f]*"
        # 使用 re.search 函数来搜索匹配的字符串
        match = re.search(pattern, str)
        # 返回匹配的字符串，即内存地址部分
        return match.group()


# 创建一个 Person 类的实例 p
p = Person("张三", 20)

# 上述表达式等价于如下两句话
# p = Person.__new__(Person)
# Person.__init__(p,"张三",20)

# 调用 p 实例的 show 方法
p.show()

# 调用 print 函数，打印 p 实例的字符串表示
# 这会调用 Person 类的 __str__ 方法
print(p)  # 重写了 __str__ 方法，只获取地址部分