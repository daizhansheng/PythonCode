# 定义一个 Student 类
class Student:
    # 构造函数，用于初始化类的实例
    # name 和 age 参数用于初始化实例的 name 和 age 属性
    def __init__(self, name, age):
        # 将 name 和 age 参数赋值给实例的 name 和 __age 属性
        # name 属性是公有的，可以直接访问
        self.name = name
        # __age 属性名前面有两个下划线，表示这个属性是私有的，不应该从外部直接访问
        self.__age = age

    # @property 装饰器是将方法当成属性使用
    # age 方法用于获取 __age 属性的值
    # 这样可以通过 s1.age 来访问 __age 属性的值，而不是直接访问 s1.__age
    @property
    def age(self):
        # 返回 __age 属性的值
        return self.__age

    # @age.setter 装饰器是将 age 方法转换为 setter 方法
    # age 方法用于设置 __age 属性的值
    # 这样可以通过 s1.age = 55 来设置 __age 属性的值，而不是直接修改 s1.__age
    @age.setter
    def age(self, age):
        # 将 age 参数赋值给 __age 属性
        self.__age = age


# 创建一个 Student 类的实例 s1
s1 = Student("张三", 22)

# 打印出 s1 的 name 和 age 属性
print(s1.name, s1.age)

# 使用 setter 方法将 s1 的 age 属性设置为 55
s1.age = 55

# 再次打印出 s1 的 name 和 age 属性
print(s1.name, s1.age)
