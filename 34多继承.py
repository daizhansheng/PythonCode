# 定义一个 Mother 类
class Mother:
    # 构造函数，用于初始化类的实例
    def __init__(self, name):
        # 将 name 参数赋值给实例的 name 属性
        self.name = name

    # 定义一个 show 方法
    def show(self):
        # 打印出 "Mother的show方法"
        print("Mother的show方法")


# 定义一个 Father 类
class Father:
    # 构造函数，用于初始化类的实例
    def __init__(self, age):
        # 将 age 参数赋值给实例的 age 属性
        self.age = age

    # 定义一个 show 方法
    def show(self):
        # 打印出 "Father的show方法"
        print("Father的show方法")


# 定义一个 Son 类，继承了 Mother 类和 Father 类
class Son(Mother, Father):
    # 构造函数，用于初始化类的实例
    def __init__(self, name, age, sex):
        # 调用 Mother 类的构造函数
        Mother.__init__(self, name)
        # 调用 Father 类的构造函数
        Father.__init__(self, age)
        # 将 sex 参数赋值给实例的 sex 属性
        self.sex = sex


# 创建一个 Son 类的实例 s
s = Son("张三", 20, "M")

# 打印出 s 对象的所有属性和方法
print(dir(s))

# 调用 s 对象的 show 方法
# 因为 Mother 和 Father 都有 show 方法，Python 会按顺序解析，调用 Mother 的 show 方法
s.show()