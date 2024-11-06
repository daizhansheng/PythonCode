# 当前文件夹：继承.py
# ======================================


# 定义一个 Person 类（继承了 object 类）
class Person:
    # 构造函数，用于初始化类的实例
    def __init__(self, name, age):
        # 将 name 和 age 参数赋值给实例的 name 和 age 属性
        # 这两个属性是公有的，可以直接访问
        self.name = name
        self.age = age

    # 公有的方法
    def show(self):
        # 打印出实例的 name 和 age 属性
        print(f"name = {self.name},age = {self.age}")


# 定义一个 Teacher 类（继承了 Person 类）
class Teacher(Person):
    # 构造函数，用于初始化类的实例
    def __init__(self, name, age, salar):
        # 调用父类（Person）的构造函数
        # 这样可以避免重复代码
        super().__init__(name, age)
        # 将 salar 参数赋值给实例的 salar 属性
        # 这个属性是特定于 Teacher 类的
        self.salar = salar


# 定义一个 Student 类（继承了 Person 类）
class Student(Person):
    # 构造函数，用于初始化类的实例
    def __init__(self, name, age, score):
        # 调用父类（Person）的构造函数
        # 这样可以避免重复代码
        super().__init__(name, age)
        # 将 score 参数赋值给实例的 score 属性
        # 这个属性是特定于 Student 类的
        self.score = score


# 创建一个 Teacher 类的实例 t1
t1 = Teacher("张三", 30, 10000)

# 创建一个 Student 类的实例 s1
s1 = Student("李四", 20, 88.3)

# 调用实例 t1 的 show 方法
# 这个方法是从 Person 类继承来的
t1.show()

# 打印出实例 t1 的 salar 属性
# 这个属性是特定于 Teacher 类的
print(t1.salar)

# 调用实例 s1 的 show 方法
# 这个方法是从 Person 类继承来的
s1.show()

# 打印出实例 s1 的 score 属性
# 这个属性是特定于 Student 类的
print(s1.score)
